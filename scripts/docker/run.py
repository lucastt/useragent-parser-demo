import subprocess

from docker import common


def run(arguments, deps = False):
    print(">>>>>>>>>> Running Command <<<<<<<<<<")
    COMPOSE_ARGUMENTS = ' run --rm ' if deps else ' run --rm --no-deps '

    command = common.COMPOSE_COMMAND + COMPOSE_ARGUMENTS + ' '.join(arguments)

    print(command)
    return subprocess.call(command, shell=True)
