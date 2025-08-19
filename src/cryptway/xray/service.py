import aiofiles
import json
import os
import uuid

from .models import Client

def generate_uuid_as_str() -> str:
    return str(uuid.uuid4())


def get_config_path() -> str:
    return os.path.join("usr", "local", "etc", "xray", "config.json")


async def load_config(path: str):
    async with aiofiles.open(path, "r", ) as config:
        cfg = await config.read()

        return json.loads(cfg)


async def update_config(path: str):
    async with aiofiles.open(path, "w") as config:
        await config.write()


async def add_new_client() -> Client:
    path = get_config_path()

    uuid = generate_uuid_as_str()
    flow = "xtls-rprx-vision"

    config = await load_config(path=path)

    config["inbounds"][1]["clients"].append(
        {
            "id": uuid,
            "flow": flow
        }
    )