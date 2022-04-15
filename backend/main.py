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


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/inventory")
async def get_inventory():
    nr = InitNornir(config_file="config.yaml")

    data = []

    for host in nr.inventory.hosts:
        host_dict = nr.inventory.hosts[host].dict()
        device_data = [
            host_dict["name"],
            host_dict["hostname"],
            host_dict["platform"],
            host_dict["data"]["role"],
            ",".join(host_dict["groups"])
        ]
        data.append(device_data)

    return {"message": data}

