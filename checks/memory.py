import psutil
import json

with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def check_memory():
    memory_percent = psutil.virtual_memory().percent

    if memory_percent > data["MEMORY_ALERT"]:
        status = "ALERTA"
    else:
        status = "OK"

    return{
        "type": "memory",
        "usage": memory_percent,
        "status": status
    }