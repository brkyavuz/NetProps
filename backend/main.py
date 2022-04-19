from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from nornir import InitNornir
from fastapi.responses import JSONResponse

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

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/inventory")
async def get_inventory():
    nr = InitNornir(config_file="config.yaml")

    hosts = inventory_constructor(nr)
    

    return {"message": hosts}

