import psutil
import json

with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)


def check_cpu(): 
    cpu_percent = psutil.cpu_percent(interval=1)
    
    if cpu_percent > data["CPU_ALERT"]:
        status = "ALERTA"
    else:
        status = "OK"

    return {
        "type": "CPU",
        "usage": cpu_percent,
        "status": status
    }

