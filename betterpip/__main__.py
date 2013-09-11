import logging
import sys
import betterpip


def main(args):
    logging.root.setLevel(logging.DEBUG if '-v' in args else logging.INFO)

    args.remove('install')

    if '-v' in args:
        args.remove('-v')

    # todo: strip any other args out that we don't want to pass along
    pip_commands = list(args)

    # todo: parse this out correctly
    build_cache = None

    install_results = []

    if '-r' in args:
        requirements_file = pip_commands.remove(pip_commands.indexof('-r') + 1)
        pip_commands.remove('-r')
        betterpip.install_r(requirements_file, pip_commands, build_cache, install_results)
    else:
        requirement = pip_commands.pop()
        betterpip.install(requirement, pip_commands, build_cache, install_results)


if __name__ == '__main__':
    exit(main(sys.argv[1:]))
