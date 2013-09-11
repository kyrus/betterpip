import logging
import os
import re
import subprocess
from utils import *


def install_r(requirements_txt_file, pip_commands=list(), build_cache=None,
              install_results=list()):
    with open(requirements_txt_file, 'rt') as f:
        for requirement in f.readlines():
            requirement = requirement.strip()

            if not requirement:
                continue

            if requirement.startswith('#'):
                continue

            install(requirement, pip_commands, build_cache, install_results)


def install(requirement, pip_commands=list(), build_cache=None, install_results=list()):
    # pip install <requirement>
    install_succeeded = True
    try:
        # run pip install
        output = subprocess.check_output(['pip', 'install'] + pip_commands + [requirement])
        print output

        # extract the package name from the output
        matcher = re.search('Successfully installed ([\w-]*)', output)
        if matcher:
            package_name = matcher.group(1)

            # install the package's requirements.txt file
            if build_cache:
                package_requirements_file = os.path.join(build_cache, package_name, 'requirements.txt')
                if os.path.isfile(package_requirements_file):
                    install_r(package_requirements_file, pip_commands, build_cache,
                              install_results)
        else:
            logging.warning("Warning: installation of package [%s] may not have succeeded" % requirement)

    except subprocess.CalledProcessError as ex:
        logging.exception("Error installing [%s]:\n%s", requirement, ex.output)
        install_succeeded = False

    install_results.append((requirement, install_succeeded))
