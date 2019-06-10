import subprocess

from docker import common


def dev(arguments):
    print(">>>>>>>>>>>>>>>>>>>> Starting Containers <<<<<<<<<<<<<<<<<<<<")
    command = common.COMPOSE_COMMAND + ' up ' + ' '.join(arguments)
    print(command)
    return subprocess.call(command, shell=True)
