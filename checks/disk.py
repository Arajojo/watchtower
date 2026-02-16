import psutil
import json

with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)


def check_disk():
    disk_percent = psutil.disk_usage('/').percent

    if disk_percent > data["DISK_ALERT"]:
        status = "ALERTA"
    else:
        status = "OK"
    
    return{
        "type": "disk",
        "usage": disk_percent,
        "status": status
    }