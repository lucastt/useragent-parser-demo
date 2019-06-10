import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_HOME = os.path.abspath(os.path.join(BASE_DIR, os.pardir, os.pardir))

PROJECT_PREFIX = "useragent-parser-"

COMPOSE_FILE = os.path.join(PROJECT_HOME, "docker-compose.dev.yml")

COMPOSE_COMMAND = "docker-compose -f \"" + COMPOSE_FILE + "\""
