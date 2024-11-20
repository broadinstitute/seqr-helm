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
    '-f',
    os.path.join(WORK_DIR, 'values.yaml')
]

class TestSeqrChart(unittest.TestCase):

    def test_open_source_values(self):
        p = subprocess.run(DEFAULT_ARGS[:-2], capture_output=True, text=True) # NB: text=True here to avoid opening the output in binary mode
        p.check_returncode()
        self.assertEqual(p.stdout.count('kind: CronJob'), 1)
        self.assertEqual(p.stdout.count('update_all_reference_data'), 1)

    def test_values(self):
        p = subprocess.run(DEFAULT_ARGS, capture_output=True, text=True)
        p.check_returncode()
        self.assertIn('kind: Deployment\nmetadata:\n  name: seqr', p.stdout)
        self.assertIn('echo starting CronJob test-cron-1;', p.stdout)
        self.assertIn('iam.gke.io/gcp-service-account: test-service-account@developer.gserviceaccount.com', p.stdout)
        self.assertIn('cloud-sql-proxy', p.stdout)
        self.assertIn('serviceAccountName: seqr', p.stdout)
        self.assertIn('a/deployment', p.stdout)
        self.assertIn('NoSchedule', p.stdout)
        self.assertEqual(p.stdout.count('kind: CronJob'), 2)

    def test_no_deployment_sidecars(self):
        p = subprocess.run([*DEFAULT_ARGS, '-f', os.path.join(WORK_DIR, 'no-deployment-sidecars.yaml')], capture_output=True, text=True)
        p.check_returncode()
        self.assertNotIn('cloud-sql-proxy', p.stdout)

    def test_no_service_account(self):
        p = subprocess.run([*DEFAULT_ARGS, '-f', os.path.join(WORK_DIR, 'no-service-account.yaml')], capture_output=True, text=True)
        p.check_returncode()
        self.assertNotIn('serviceAccountName: seqr\n', p.stdout)

    def test_incorrectly_formatted_cronjob(self):
        p = subprocess.run([*DEFAULT_ARGS, '-f', os.path.join(WORK_DIR, 'incorrectly-formatted-cronjob.yaml')], capture_output=True, text=True)
        self.assertRaises(subprocess.CalledProcessError, p.check_returncode)
        self.assertIn('invalid resource name "seqr-a/bad/cron/1"', p.stderr)

    def test_redis(self):
        p = subprocess.run([*DEFAULT_ARGS, '-f', os.path.join(WORK_DIR, 'redis.yaml')], capture_output=True, text=True)
        p.check_returncode()
        self.assertIn('REDIS_SERVICE_HOSTNAME: seqr-redis-master', p.stdout)
        self.assertIn('app.kubernetes.io/name: redis', p.stdout)

    def test_postgres(self):
        p = subprocess.run([*DEFAULT_ARGS, '-f', os.path.join(WORK_DIR, 'postgresql.yaml')], capture_output=True, text=True)
        p.check_returncode()
        self.assertRegex(p.stdout, r'secretKeyRef:\s*name: postgres-secrets\s*key: password')
        self.assertRegex(p.stdout, r'kind: Service\s*metadata:\s*name: seqr-postgresql')
        self.assertIn('seqr-platform-pvc', p.stdout)

if __name__ == '__main__':
    unittest.main()
