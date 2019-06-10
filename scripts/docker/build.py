import subprocess

from docker import common


def build(arguments):
    print(">>>>>>>>>>>>>>>>>>>> Building <<<<<<<<<<<<<<<<<<<<")
    command = common.COMPOSE_COMMAND + ' build --pull ' + ' '.join(arguments)
    print(command)
    return subprocess.call(command, shell=True)
