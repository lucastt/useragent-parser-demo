import subprocess

from docker import common


def stop(arguments):
    print(">>>>>>>>>>>>>>>>>>>> Stopping services <<<<<<<<<<<<<<<<<<<<")
    command = common.COMPOSE_COMMAND + ' stop ' + ' '.join(arguments)
    print(command)
    return subprocess.call(command, shell=True)
