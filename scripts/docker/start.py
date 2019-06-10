import subprocess

from docker import common


def start(arguments):
    print(">>>>>>>>>>>>>>>>>>>> Starting Containers <<<<<<<<<<<<<<<<<<<<")
    command = common.COMPOSE_COMMAND + ' up -d ' + ' '.join(arguments)
    print(command)
    return subprocess.call(command, shell=True)
