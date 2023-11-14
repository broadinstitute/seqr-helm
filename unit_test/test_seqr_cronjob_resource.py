import os
import subprocess
import unittest

import unit_test.test_seqr_chart as test_seqr_chart

WORK_DIR = os.path.dirname(__file__)
DEFAULT_ARGS = [
    *test_seqr_chart.DEFAULT_ARGS,
    '-s',
    'templates/cronjob.yaml',
]

class TestSeqrCronJobResourceChart(unittest.TestCase):

    def test_values(self):
        p = subprocess.run(DEFAULT_ARGS, capture_output=True, text=True)
        p.check_returncode()
        self.assertIn('serviceAccountName: test-seqr', p.stdout)
        self.assertIn('test-cron-1', p.stdout)
        self.assertIn('test-cron-2', p.stdout)
        self.assertEqual(p.stdout.count('kind: CronJob'), 2)

if __name__ == '__main__':
    unittest.main()
