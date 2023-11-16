
# Preverjanje lastnosti sporočil v JSON, XML in PB

## Opis

Ogledali si bomo metode za pregled različnih lastnosti, kot so velikost datoteke, vrste podatkov in metapodatki.

---

## JSON

### Velikost datoteke

Če želite preveriti velikost datoteke JSON, lahko uporabite Pythonovo metodo `os.path.getsize`.

```python
import os

file_size = os.path.getsize("./DATA/POMOC/person.json")
print(f"JSON file size: {file_size} bytes")
```

### Vrste podatkov (podatkovni tipi)

Vrste podatkov v objektu JSON lahko pregledate šele, ko ga naložite v Python slovar/dictionary.

```python
import json

with open("./DATA/POMOC/person.json", "r") as f:
    data = json.load(f)

for key, value in data.items():
    print(f"{key}: {type(value)}")
```

---

## XML

### Velikost datoteke

Podobno kot pri JSON lahko uporabite `os.path.getsize` za določitev velikosti datoteke XML.

```python
file_size = os.path.getsize("./DATA/POMOC/person.xml")
print(f"XML file size: {file_size} bytes")
```

### Vrste podatkov oz elementi in atributi

Elemente in atribute znotraj datoteke XML lahko pregledate z uporabo `xml.etree.ElementTree`.

```python
import xml.etree.ElementTree as ET

tree = ET.parse('./DATA/POMOC/person.xml')
root = tree.getroot()

for elem in root:
    print(f"Element: {elem.tag}, Text: {elem.text}")
```

---

## Protocol-Buffers (PB)

### Velikost datoteke

Velja enako kot pri JSON in XML

```python
file_size = os.path.getsize("./DATA/POMOC/person.pb")
print(f"Protocol Buffers file size: {file_size} bytes")
```

### Message Fields

Če želite preveriti polja in njihove vrste v sporočilu PB, lahko uporabite metodo `ListFields`.

```python
from person_pb2 import Person

person_pb = Person()

with open('./DATA/POMOC/person_updated.pb', 'rb') as f:
    person_pb.ParseFromString(f.read())


for field, value in person_pb.ListFields():
    print(f"Field: {field.name}, Type: {field.type}, Value: {value}")
```

TYPE: To je številčna koda, ki predstavlja podatkovni tip polja v skladu z notranjim sistemom tipov PB. Te številke se preslikajo na določene vrste. Na primer:
9 ustreza vrsti niza (string).
5 ustreza vrstam fixed32, sfixed32 ali float (v nasem primeru je najverjetneje int32)

---
