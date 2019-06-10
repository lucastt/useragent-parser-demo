import subprocess

from docker.clean import clean
from docker import common


# runs command and captures output
def run(command):
    print(command)
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    return p.communicate()[0].replace("\n", " ")


def kill(arguments):
    clean(arguments)
    print("\n>>>>>>>>>> Removing Images Containers <<<<<<<<<<")
    images = run('docker images \"*' + common.PROJECT_PREFIX + '*\" -q')
    run('docker rmi -f ' + images)

    # ignore return codes since stuff may have already been removed and break
    return 0
