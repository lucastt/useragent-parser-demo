RED = '\033[91m'
BLUE = '\033[94m'
END = '\033[0m'


def red(str):
    return RED + str + END


def blue(str):
    return BLUE + str + END


def usage(arguments):
    print('''
    Usage:
        python3 devenv.py <command> <arguments>
        devenv.py <command> <arguments>

    Commands:
        build                     Downloads and builds images.
        clean                     Removes all containers, networks {volumes}.
        dev                       Starts containers.
        kill                      Runs clean and {images}.
        logs                      Attaches logs to terminal.
        restart                   Restarts containers.
        run                       Runs an arbitrary command in a specified service (eg. 'run frontend build')
        start                     Start containers in detached mode.
        status                    Shows all containers, images, networks and volumes.
        stop                      Stops all containers.'''
    .format(
        volumes=red('and volumes'),
        images=red('removes all images'),
    ))
