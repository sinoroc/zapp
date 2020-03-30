#


""" Command line interface """


import argparse

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
    parser.add_argument(
        '--requirement',
        '-r',
        dest='requirements_txt',
        metavar='requirements.txt',
        type=argparse.FileType(),
    )
    args = parser.parse_args()
    core.build_zapp(
        args.output_file,
        args.entry_point,
        args.requirements,
        getattr(args.requirements_txt, 'name', None),
    )


# EOF
