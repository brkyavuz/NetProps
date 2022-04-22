import json
from fastapi import Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Commands
from nornir import InitNornir
from nornir_scrapli.tasks import send_command, send_commands
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from fastapi.responses import JSONResponse
from global_vars import TEMPLATES_DIR
import os


app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def inventory_constructor(nrobject):
    hosts = []

    for host in nrobject.inventory.hosts:
        host_dict = nrobject.inventory.hosts[host].dict()
        host_data = [
            host_dict["name"],
            host_dict["hostname"],
            ",".join(host_dict["groups"]),
            host_dict["data"]["model"]
        ]
        hosts.append(host_data)

    return hosts


def get_facts(task):
    commands = ["show version"]
    if task.host.platform == "iosxr":
        command = "show platform"
    else:
        command = "show ver"

    res = task.run(task=send_command, command=command)
    print(res.scrapli_response.genie_parse_output())
    # for r in res:
    #     print(type(r.scrapli_response))
    #     # print(r.scrapli_response.genie_parse_output())


def get_config_from_devices(task, commands):
    if isinstance(commands,str):
        task.run(task=send_command, command=commands)
    else:
        task.run(task=send_commands, commands=commands)


@app.get("/")
async def root():
    # nr = InitNornir(config_file="config.yaml")
    # res = nr.run(task=napalm_get, getters=["get_facts"])
    # print_result(res)
    return {"message": "Hello World"}

@app.get("/inventory")
async def get_inventory():
    nr = InitNornir(config_file="config.yaml")

    hosts = inventory_constructor(nr)
    

    return {"message": hosts}


@app.get("/cm/templates")
async def get_templates():
    current_templates = os.listdir(TEMPLATES_DIR)
    print(current_templates)
    return {"message": TEMPLATES_DIR}


@app.post("/cm/getconfig/")
async def get_config(commands:Commands):
    nr = InitNornir(config_file="config.yaml")
    command_list = commands.commands.split('\n')
    results = nr.run(task=send_commands, commands=command_list)
    
    return {"results": results}