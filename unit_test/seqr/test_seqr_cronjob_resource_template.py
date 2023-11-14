import os
import subprocess
import unittest

WORK_DIR = os.path.dirname(__file__)
DEFAULT_ARGS = [
    'helm',
    'template',
    'test-seqr', 
    'charts/seqr', 
    '-s',
    'templates/cronjob.yaml',
    '-f',
    os.path.join(WORK_DIR, 'values.yaml'),
]

class TestSeqrCronJobResourceChart(unittest.TestCase):

    def test_values(self):
        p = subprocess.run(DEFAULT_ARGS, capture_output=True, text=True)
        p.check_returncode()
        self.assertIn('serviceAccountName: test-seqr', p.stdout)
        self.assertIn('test-cron-1', p.stdout)
        self.assertIn('test-cron-2', p.stdout)
        self.assertEqual(p.stdout.count('kind: CronJob'), 2)
        self.assertEqual(p.stdout.count('nodeSelector:\n            cloud.google.com/gke-nodepool: test-pool'), 2)

if __name__ == '__main__':
    unittest.main()
