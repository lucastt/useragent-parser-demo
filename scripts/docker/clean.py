import subprocess

from docker import common


# runs command and captures output
def run(command):
    print(command)
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    return p.communicate()[0].replace("\n", " ")


def clean(arguments):
    print(">>>>>>>>>> Removing Docker Containers <<<<<<<<<<")
    containers = run('docker ps -a -q -f \"name=' + common.PROJECT_PREFIX + '\"')
    run('docker rm -f ' + containers)

    print("\n>>>>>>>>>> Removing Docker Volumes <<<<<<<<<<")
    volume_prefix = common.PROJECT_PREFIX.replace('-', '_')  # docker volumes cant use '-'
    volumes = run('docker volume ls -q -f \"name=' + volume_prefix + '\" -f \"dangling=true\"')
    run('docker volume rm ' + volumes)

    print("\n>>>>>>>>>> Removing Docker Networks <<<<<<<<<<")
    networks = run('docker network ls -q -f \"name=' + common.PROJECT_PREFIX + '\"')
    run('docker network rm ' + networks)

    # ignore return codes since stuff may have already been removed and break
    return 0
