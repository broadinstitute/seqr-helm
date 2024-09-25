import os
import subprocess
import unittest

WORK_DIR = os.path.dirname(__file__)
DEFAULT_ARGS = [
    'helm',
    'install',
    'test', 
    'charts/pipeline-runner', 
    '--dry-run',
    '--debug', 
    '-f',
    os.path.join(WORK_DIR, 'values.yaml')
]

class TestPipelineRunnerChart(unittest.TestCase):

    def test_values(self):
        p = subprocess.run(DEFAULT_ARGS, capture_output=True, text=True) # NB: text=True here to avoid opening the output in binary mode
        p.check_returncode()
        self.assertIn('serviceAccountName: pipeline-runner', p.stdout)
        self.assertIn('checksum/config', p.stdout)
        self.assertIn('pipeline-runner-ui', p.stdout)
        self.assertIn('pipeline-runner-api-sidecar', p.stdout)

if __name__ == '__main__':
    unittest.main()
