from pathlib import Path
from envparse import env

env.read_envfile(Path(__file__).parent / ".env")