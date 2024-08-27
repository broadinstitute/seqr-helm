import os
import subprocess
import unittest

WORK_DIR = os.path.dirname(__file__)
DEFAULT_ARGS = [
    'helm',
    'install',
    'test', 
    'charts/seqr', 
    '--dry-run',
    '--debug', 
    '-f',
    os.path.join(WORK_DIR, 'values.yaml')
]

class TestSeqrChart(unittest.TestCase):

    def test_open_source_values(self):
        p = subprocess.run(DEFAULT_ARGS[:-2], capture_output=True, text=True) # NB: text=True here to avoid opening the output in binary mode
        p.check_returncode()
        self.assertEqual(p.stdout.count('kind: CronJob'), 0)

    def test_values(self):
        p = subprocess.run(DEFAULT_ARGS, capture_output=True, text=True)
        p.check_returncode()
        self.assertIn('kind: Deployment\nmetadata:\n  name: test-seqr', p.stdout)
        self.assertIn('echo starting CronJob test-cron-1;', p.stdout)
        self.assertIn('iam.gke.io/gcp-service-account: test-service-account@developer.gserviceaccount.com', p.stdout)
        self.assertIn('cloud-sql-proxy', p.stdout)
        self.assertIn('serviceAccountName: test-seqr', p.stdout)
        self.assertIn('SEQR_ES_PASSWORD', p.stdout)
        self.assertEqual(p.stdout.count('kind: CronJob'), 2)

    def test_no_deployment_sidecars(self):
        p = subprocess.run([*DEFAULT_ARGS, '-f', os.path.join(WORK_DIR, 'no-deployment-sidecars.yaml')], capture_output=True, text=True)
        p.check_returncode()
        self.assertNotIn('cloud-sql-proxy', p.stdout)

    def test_no_service_account(self):
        p = subprocess.run([*DEFAULT_ARGS, '-f', os.path.join(WORK_DIR, 'no-service-account.yaml')], capture_output=True, text=True)
        p.check_returncode()
        self.assertNotIn('serviceAccountName: test-seqr\n', p.stdout)

    def test_incorrectly_formatted_cronjob(self):
        p = subprocess.run([*DEFAULT_ARGS, '-f', os.path.join(WORK_DIR, 'incorrectly-formatted-cronjob.yaml')], capture_output=True, text=True)
        self.assertRaises(subprocess.CalledProcessError, p.check_returncode)
        self.assertIn('invalid resource name "test-seqr-a/bad/cron/1": [may not contain \'/\']\nhelm.go', p.stderr)

    def test_check_new_samples_job(self):
        p = subprocess.run([*DEFAULT_ARGS, '-f', os.path.join(WORK_DIR, 'check-new-samples-job.yaml')], capture_output=True, text=True)
        p.check_returncode()
        self.assertIn('python manage.py check_for_new_samples_from_pipeline GRCh38/MITO manual_run_123;\n', p.stdout)

if __name__ == '__main__':
    unittest.main()
