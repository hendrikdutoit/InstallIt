'''Testing installit()'''

from pathlib import Path
from beetools import Archiver, beeutils
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

    def test_configure_mysql_remote_access(self, env_setup_self_destruct):
        env_setup = env_setup_self_destruct
        t_installit = installit.InstallIt()
        if t_installit.curr_os == beeutils.LINUX:
            t_installit.configure_mysql_remote_access(
                env_setup.mysql_user_admin,
                env_setup.mysql_user_remote_users,
                env_setup.mysql_user_remote_rights,
            )
        pass


del b_tls
