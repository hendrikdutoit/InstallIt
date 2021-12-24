'''Testing installit()'''

from pathlib import Path
from beetools.beearchiver import Archiver
import installit


_PROJ_DESC = __doc__.split('\n')[0]
_PROJ_PATH = Path(__file__)


b_tls = Archiver(_PROJ_DESC, _PROJ_PATH)


class TestInstallIt:
    def test__init__(self, env_setup_self_destruct):
        """Assert class __init__"""
        # env_setup = env_setup_self_destruct
        t_installit = installit.InstallIt()

        assert t_installit.success
        pass

    def test_do_examples(self):
        installit.do_examples()


del b_tls
