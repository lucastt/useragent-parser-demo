import subprocess

from docker import common


def logs(arguments):
    print(">>>>>>>>>>>>>>>>>>>> Logs <<<<<<<<<<<<<<<<<<<<")
    command = common.COMPOSE_COMMAND + ' logs --follow ' + ' '.join(arguments)
    print(command)
    return subprocess.call(command, shell=True)
