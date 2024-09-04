import os
import subprocess
import unittest

WORK_DIR = os.path.dirname(__file__)
DEFAULT_ARGS = [
    'helm',
    'install',
    'test', 
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
        self.assertIn('serviceAccountName: hail-search', p.stdout)
        self.assertIn('checksum/config', p.stdout)
        self.assertIn('a/deployment', p.stdout)
        self.assertIn('checksum/datasetVersions: a3455105c5ed96d20f9422cbcf71ab28e9057ced7e048c8892ffaf721e5b7946', p.stdout)
        self.assertIn('claimName: hail-search-pvc', p.stdout)
        self.assertIn('local:', p.stdout)
        self.assertNotIn('9ff0a', p.stdout)

    def test_persistent_volume(self):
        p = subprocess.run([*DEFAULT_ARGS, '-f', os.path.join(WORK_DIR, 'persistentvolume.yaml')], capture_output=True, text=True)
        p.check_returncode()
        self.assertIn('claimName: hail-search-pvc-9ff0a', p.stdout)
        self.assertIn('volumeHandle: projects/test-project/zones/us-central3-a/disks/test-disk', p.stdout)
        self.assertIn('checksum/datasetVersions', p.stdout)

if __name__ == '__main__':
    unittest.main()
