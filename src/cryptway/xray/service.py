import aiofiles
import json
import os
import uuid

from typing import Any

from .models import Client

def generate_uuid_as_str() -> str:
    return str(uuid.uuid4())


def get_config_path() -> str:
    return os.path.join("/", "usr", "local", "etc", "xray", "config.json")


def make_client() -> Client:
    client_id = generate_uuid_as_str()
    flow = "xtls-rprx-vision"

    return Client(
        uuid=client_id,
        flow=flow
    )


async def load_config(path: str):
    async with aiofiles.open(path, "r", ) as config:
        cfg = await config.read()

        return json.loads(cfg)


async def update_config(path: str, old_config: Any, client: Client):
    old_config["inbounds"][1]["clients"].append(
        {
            "id": client.uuid,
            "flow": client.flow
        }
    )
    async with aiofiles.open(path, "w") as config:
        await config.write(json.dumps(old_config, indent=4))


async def add_new_client() -> Client:
    path = get_config_path()

    client = make_client()
    old_config = await load_config(path=path)

    await update_config(path=path, old_config=old_config, client=client)

    return client