import os
import subprocess
import unittest

WORK_DIR = os.path.dirname(__file__)
DEFAULT_ARGS = [
    'helm',
    'install',
    'test-seqr', 
    'charts/seqr', 
    '--dry-run',
    '--debug', 
    '-f',
    os.path.join(WORK_DIR, 'values.yaml')
]

class TestSeqrChart(unittest.TestCase):

    def test_values(self):
        p = subprocess.run(DEFAULT_ARGS, capture_output=True, text=True) # NB: text=True here to avoid opening the output in binary mode
        p.check_returncode()
        self.assertIn('kind: Deployment\nmetadata:\n  name: seqr', p.stdout)
        self.assertIn('echo starting CronJob test-cron-1;', p.stdout)
        self.assertIn('iam.gke.io/gcp-service-account: test-service-account@developer.gserviceaccount.com', p.stdout)
        self.assertIn('cloud-sql-proxy', p.stdout)
        self.assertIn('serviceAccountName: test-seqr', p.stdout)

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
        self.assertIn('invalid resource name "test-seqr-test/cron/1-cronjob": [may not contain \'/\']\nhelm.go', p.stderr)

if __name__ == '__main__':
    unittest.main()
