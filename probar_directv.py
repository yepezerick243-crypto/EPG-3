
import requests
import json

url = "https://www.directv.com.ec/guia/ChannelDetail.aspx/GetProgramming"
pagina = "https://www.directv.com.ec/guia/ChannelDetail.aspx?id=1206&name=WTVHD"

session = requests.Session()

headers = {
    "Accept": "*/*",
    "Content-Type": "application/json; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": pagina,
    "Origin": "https://www.directv.com.ec",
    "User-Agent": "Mozilla/5.0"
}

print("1. ABRIENDO LA PAGINA...")
r = session.get(pagina, headers=headers, timeout=30)
print("HTTP:", r.status_code)
print("Cookies obtenidas:", len(session.cookies))

print("\n2. CONSULTANDO PROGRAMACION...")

response = session.post(
    url,
    headers=headers,
    json={"filterParameters": None},
    timeout=30
)

print("HTTP:", response.status_code)
print("LONGITUD:", len(response.text))
print("RESPUESTA:", response.text[:12000])

try:
    data = response.json()
    canales = data.get("d", [])

    if isinstance(canales, list):
        print("\nCANTIDAD DE CANALES:", len(canales))

        for canal in canales:
            print("\nCANAL:", canal.get("ChannelFullName"))
            print("NUMERO:", canal.get("ChannelNumber"))

            for p in canal.get("ProgramList", []):
                print(
                    p.get("startTimeString"),
                    "-",
                    p.get("endTimeString"),
                    "|",
                    p.get("title")
                )
    else:
        print("\nEl campo d no contiene una lista.")

except Exception as e:
    print("ERROR:", e)
