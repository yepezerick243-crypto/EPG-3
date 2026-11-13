
import requests
import json

URL = "https://www.directv.com.ec/guia/ChannelDetail.aspx/GetProgramming"

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.directv.com.ec/guia/ChannelDetail.aspx?id=1206&name=WTVHD",
    "Origin": "https://www.directv.com.ec",
}

payload = {
    "filterParameters": None
}

try:
    response = requests.post(
        URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    print("ESTADO HTTP:", response.status_code)
    print("TIPO DE RESPUESTA:", response.headers.get("Content-Type"))
    print("\nRESPUESTA:")

    response.raise_for_status()
    data = response.json()

    canales = data.get("d", [])

    for canal in canales:
        print("\nCANAL:", canal.get("ChannelFullName"))
        print("NUMERO:", canal.get("ChannelNumber"))

        for programa in canal.get("ProgramList", []):
            print(
                programa.get("startTimeString"),
                "-",
                programa.get("endTimeString"),
                "|",
                programa.get("title")
            )

except Exception as e:
    print("ERROR:", e)
