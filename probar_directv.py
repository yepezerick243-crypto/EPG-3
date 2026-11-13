
import requests
import json

url = "https://www.directv.com.ec/guia/ChannelDetail.aspx/GetProgramming"

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.directv.com.ec/guia/ChannelDetail.aspx?id=1206&name=WTVHD",
    "Origin": "https://www.directv.com.ec"
}

payload = {"filterParameters": None}

response = requests.post(
    url,
    headers=headers,
    json=payload,
    timeout=30
)

print("HTTP:", response.status_code)
print("Longitud:", len(response.text))
print("\nCONTENIDO ORIGINAL:")
print(response.text[:12000])

try:
    data = response.json()
    print("\nESTRUCTURA JSON:")
    print(json.dumps(data, indent=2, ensure_ascii=False)[:12000])

    canales = data.get("d", [])

    print("\nCANTIDAD DE CANALES:", len(canales))

    for canal in canales:
        programas = canal.get("ProgramList", [])
        print("\nCANAL:", canal.get("ChannelFullName"))
        print("NUMERO:", canal.get("ChannelNumber"))
        print("PROGRAMAS:", len(programas))

        for p in programas:
            print(
                p.get("startTimeString"),
                "-",
                p.get("endTimeString"),
                "|",
                p.get("title")
            )

except Exception as e:
    print("\nERROR AL INTERPRETAR JSON:", e)
