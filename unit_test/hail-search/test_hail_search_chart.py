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
        self.assertNotIn('name: sync-annotations-grch38-snv-indel', p.stdout)
        self.assertNotIn('claimName: seqr-platform-pvc-9ff0a', p.stdout)

    def test_persistent_volume(self):
        p = subprocess.run([*DEFAULT_ARGS, '-f', os.path.join(WORK_DIR, 'persistentvolume.yaml')], capture_output=True, text=True)
        p.check_returncode()
        self.assertIn('claimName: seqr-platform-pvc-9ff0a', p.stdout)
        self.assertIn('rsync', p.stdout)
        self.assertIn('/in-memory-datasets', p.stdout)
        self.assertIn('volumeHandle: projects/test-project/zones/us-central3-a/disks/test-disk', p.stdout)

if __name__ == '__main__':
    unittest.main()
