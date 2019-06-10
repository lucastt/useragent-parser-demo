import subprocess


def status(arguments):
    print(">>>>>>>>>>>>>>>>>>>> DOCKER STATUS <<<<<<<<<<<<<<<<<<<<")
    print("\n\nDOCKER CONTAINERS:")
    ret = subprocess.call('docker container ls -a', shell=True)

    print("\n\nDOCKER IMAGES:")
    ret += subprocess.call('docker image ls', shell=True)

    print("\n\nDOCKER VOLUMES:")
    ret += subprocess.call('docker volume ls', shell=True)

    print("\n\nDOCKER NETWORKS:")
    ret += subprocess.call('docker network ls', shell=True)

    return ret
