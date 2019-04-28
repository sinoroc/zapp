#


""" Command line interface """


import argparse
import tempfile

from . import core
from . import meta


def main():
    """ CLI main function
    """
    parser = argparse.ArgumentParser(
        allow_abbrev=False,
    )
    parser.add_argument('--version', action='version', version=meta.VERSION)
    parser.add_argument('output_file')
    parser.add_argument('entry_point')
    parser.add_argument('requirements', metavar='requirement', nargs='*')
    args = parser.parse_args()
    with tempfile.TemporaryDirectory() as install_dir:
        if args.requirements:
            core.install_to_dir(install_dir, args.requirements)
        core.build_zipapp(install_dir, args.entry_point, args.output_file)


# EOF
