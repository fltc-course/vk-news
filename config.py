import os
import dotenv

import time


dotenv.load_dotenv()

TG_TOKEN: str = os.getenv("TG_TOKEN")
VK_TOKEN: str = os.getenv("VK_TOKEN")
START_TIME: int = int(os.getenv("START_TIME", time.time() - 300))

