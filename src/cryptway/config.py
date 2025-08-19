from environs import Env

env = Env()

env.read_env()

API_KEY_HASH = env.str("API_KEY_HASH")