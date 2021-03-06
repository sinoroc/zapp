""" Unit tests
"""


import unittest

import zapp


class TestProjectVersion(unittest.TestCase):
    """ Project version string
    """

    def test_project_has_version_string(self):
        """ Project should have a vesion string
        """
        try:
            zapp.__version__
        except AttributeError as version_exception:
            self.fail(version_exception)


# EOF
