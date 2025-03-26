from dataclasses import dataclass, asdict
import datetime
from functools import cache
import yaml
import atexit
import logging
import os

@dataclass
class __Config:
    db_path: str = "endemica.db"
    log_file_path: str = ".log/endemica_log (%d-%m-%Y).log"
    log_format: str = "[\033[;35m%(name)s\033[0m]  \033[32m%(levelname)s\033[0m: %(asctime)s - %(message)s"
    workers: int = 3
# fi

config: __Config
try:
    with open("config.yaml", "r") as config_file:
        config = __Config(**yaml.safe_load(config_file))
    # fi
# fi

except FileNotFoundError:
    config = __Config()

    @atexit.register
    def __save_conig():
        yaml.safe_dump(data=asdict(config), stream=open("config.yaml", "w"))
    # fi
# fi

@cache
def __init_logger():
    format = config.log_format
    file = datetime.datetime.today().strftime(config.log_file_path)

    os.makedirs(
        name = os.path.dirname(file),
        exist_ok = True,
    )

    logger = logging.getLogger(f"endemica:{__name__}")
    fh = logging.FileHandler(
        filename = file,
        mode="a"
    )

    fh.setFormatter(fmt=logging.Formatter(format))
    logger.addHandler(fh)

    logging.basicConfig(filename="", level=logging.INFO, format=format)
    return logger
#fi

def get_logger(): return __init_logger()
