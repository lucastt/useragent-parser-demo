import subprocess

from docker import common


def restart(arguments):
    print(">>>>>>>>>>>>>>>>>>>> Restarting Containers <<<<<<<<<<<<<<<<<<<<")
    command = common.COMPOSE_COMMAND + ' restart ' + ' '.join(arguments)
    print(command)
    return subprocess.call(command, shell=True)
