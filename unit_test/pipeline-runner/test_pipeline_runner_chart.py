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
]

class TestPipelineRunnerChart(unittest.TestCase):

    def test_values(self):
        p = subprocess.run(DEFAULT_ARGS, capture_output=True, text=True) # NB: text=True here to avoid opening the output in binary mode
        p.check_returncode()
        self.assertIn('serviceAccountName: pipeline-runner', p.stdout)
        self.assertIn('checksum/config', p.stdout)
        self.assertIn('pipeline-runner-ui', p.stdout)
        self.assertIn('pipeline-runner-api-sidecar', p.stdout)
        for job in [
            'rsync-reference-data-grch37',
            'rsync-reference-data-grch38',
            'download-vep-reference-data-grch37',
            'download-vep-reference-data-grch38',
        ]:
            self.assertIn(job, p.stdout)
        self.assertIn(
            'sqlite:///var/seqr/luigi-state/luigi-task-hist.db',
            p.stdout
        )

    def test_additional_secrets(self):
        p = subprocess.run([*DEFAULT_ARGS, '-f', os.path.join(WORK_DIR, 'alleleregistry.yaml')], capture_output=True, text=True)
        self.assertIn(
            'clingen_allele_registry_password',
            p.stdout
        )

if __name__ == '__main__':
    unittest.main()
