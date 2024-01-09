import os
import subprocess
import unittest

WORK_DIR = os.path.dirname(__file__)
DEFAULT_ARGS = [
    'helm',
    'install',
    'test-hail-search', 
    'charts/hail-search', 
    '--dry-run',
    '--debug', 
    '-f',
    os.path.join(WORK_DIR, 'values.yaml')
]

class TestHailSearchChart(unittest.TestCase):

    def test_values(self):
        p = subprocess.run(DEFAULT_ARGS, capture_output=True, text=True) # NB: text=True here to avoid opening the output in binary mode
        p.check_returncode()
        self.assertIn('serviceAccountName: test-hail-search', p.stdout)
        self.assertIn('name: sync-grch38-snv-indel', p.stdout)
        self.assertIn('name: sync-ssd-grch38-snv-indel', p.stdout)
        self.assertIn('checksum/datasetVersions', p.stdout)
        self.assertIn('checksum/config', p.stdout)


if __name__ == '__main__':
    unittest.main()
