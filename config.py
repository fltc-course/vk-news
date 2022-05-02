import os
import dotenv

import time

env_path = dotenv.find_dotenv()
dotenv.load_dotenv(env_path)

TG_TOKEN: str = os.getenv("TG_TOKEN")
VK_TOKEN: str = os.getenv("VK_TOKEN")
START_TIME: int = int(os.getenv("START_TIME"))


def reset_start_time():
    dotenv.load_dotenv(env_path)
    global START_TIME

    START_TIME = int(time.time())
    dotenv.set_key(env_path, "START_TIME", str(START_TIME))
