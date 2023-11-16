
# Prevajanje sheme med JSON, XML in PB v Pythonu


## Predpostavke:

1. Tipi shem med temi formati podatkov so združljivi. Če niso, bi bila potrebna dodatna logika preslikave za pretvorbo med nezdružljivimi vrstami.
2. Polja, ki manjkajo v eni shemi, vendar so prisotna v drugi, so prezrta ali nastavljena na privzete vrednosti.
3. Razred PB `Person` je vnaprej določen in preveden iz datoteke `.proto`.


## Notable Improvements:

**Added Type Handling**: The improved code considers the type of the field when translating between XML and Protocol Buffers. This ensures that numerical and boolean values are handled correctly.

**Boolean Field Example**: Added an example with a boolean field in JSON to show how different types could be handled.

**Commented Protocol Buffers**: The Protocol Buffers section is commented out because it requires a .proto file and generated Python classes which can't be shown in this isolated example.

## Vaje:

### 1. JSON -> XML

1. Uporabite `json.loads()` za razčlenitev podatkov JSON v slovar Python.
2. Ustvarite korenski element XML (XML root element) in napolnite njegove podrejene elemente s pari ključ-vrednost iz python slovarja.

Example:

```python
import json
import xml.etree.ElementTree as ET

# Load JSON from a file
with open('/Users/jaybojic/VAJE/VAJE/VAJE-3/DATA/POMOC/person.json', 'r') as f:
    parsed_json = json.load(f)

# Function to recursively convert JSON to XML
def json_to_xml(json_obj, line_padding=""):
    json_obj_type = type(json_obj)
    if json_obj_type is list:
        for sub_elem in json_obj:
            yield from json_to_xml(sub_elem, line_padding)
    elif json_obj_type is dict:
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            yield f"{line_padding}<{tag_name}>"
            yield from json_to_xml(sub_obj, "\t" + line_padding)
            yield f"{line_padding}</{tag_name}>"
    else:
        yield f"{line_padding}{json_obj}"

# Convert JSON to XML
xml_content = "\n".join(json_to_xml(parsed_json))
xml_content = f"<person>\n{xml_content}\n</person>"

# Save XML to a file
with open("personPrevajanje.xml", 'w') as f:
    f.write(xml_content)
```


### 2. XML -> Protocol Buffers

1. Za branje datoteke XML uporabite `ET.parse()`.
2. Napolnite objekt Protocol Buffer z elementi XML.

Example:

```python
# ce ne dela import pazi kje imas trenutno skripto/jupyterNotebook in kje imas compilan person_pb2!
# ce nista na enakem mesto lahko dodas path do datoteke tako :
# import sys
# sys.path.append('PATH DO person_pb2.py')                #spremeni za svoj PATH! naprimer'/Users/user/VAJE_3//PB'

from xml.etree import ElementTree as ET
from person_pb2 import Person

def xml_to_pb(xml_file_path, pb_file_path):
    # Parsamo/preberemo XML datoteko
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Inicializacija PB objekta v pythonu
    person_pb = Person()

    # napolnemo PB objekt glede na XML, ki ga imamo DATA folder person.xml
    for elem in root:
        if elem.tag == 'name':
            person_pb.name = elem.text
        elif elem.tag == 'age':
            person_pb.age = int(elem.text)
        elif elem.tag == 'address':
            for sub_elem in elem:
                if sub_elem.tag == 'street':
                    person_pb.street = sub_elem.text
                elif sub_elem.tag == 'city':
                    person_pb.city = sub_elem.text
        elif elem.tag == 'married':
            person_pb.married = elem.text.lower() == 'true'

    # Serializacija PB objekte v binary
    with open(pb_file_path, 'wb') as f:
        f.write(person_pb.SerializeToString())

# Uporabi tako da zamenjas 'PATH' z naslovom do  xml fajla v DATA folderju!
xml_to_pb('PATH', 'person_Prevajanje.pb')


# preberi
person_updated = person_pb2.Person()

with open("./person_Prevajanje.pb", "rb") as f:
    person_updated.ParseFromString(f.read())

print(person_updated)
```

### 3. Protocol Buffers -> JSON



#### PRIMER ROCNO:

Več nadzora nad končno JSON strukturo, vendar je potrebno vse sprogramirati

```python
# ce ne dela import pazi kje imas trenutno skripto/jupyterNotebook in kje imas compilan person_pb2!
# ce nista na enakem mesto lahko dodas path do datoteke tako :
# import sys
# sys.path.append('PATH DO person_pb2.py')                #spremeni za svoj PATH! naprimer'/Users/user/VAJE_3//PB'

import json
from person_pb2 import Person  

def pb_to_json(pb_file_path, json_file_path):
    # Inicializiramo prazen Person PB objekt
    person_pb = Person()

    # Deserializiramo  PB datoteko v objekt Person
    with open(pb_file_path, 'rb') as f:
        person_pb.ParseFromString(f.read())

    # Pretvorimo PB objekt v slovar
    person_dict = {
        'name': person_pb.name,
        'age': person_pb.age,
        'address': {
            'street': person_pb.street,
            'city': person_pb.city,
        },
        'married': person_pb.married,
    }

    # Serializiraj slovar v JSON datoteko
    with open(json_file_path, 'w') as f:
        json.dump(person_dict, f, indent=4)

# Uporabi tako da vstavis PATH do prej generiranega PB datoteke
pb_to_json('PATH do pb fajla', 'person_output.json')
```

#### Primer uporaba ukaza iz knjiznice
1. Uporabite `MessageToJson` iz `google.protobuf.json_format` za serializacijo objekta Protocol Buffer v JSON.

Lažje in hitrejše ampak struktura JSON ni popolnoma tako kot bi si jo želeli

```python
# ce ne dela import pazi kje imas trenutno skripto/jupyterNotebook in kje imas compilan person_pb2!
# ce nista na enakem mesto lahko dodas path do datoteke tako :
# import sys
# sys.path.append('PATH DO person_pb2.py')                #spremeni za svoj PATH! naprimer'/Users/user/VAJE_3//PB'

from google.protobuf.json_format import MessageToJson
from person_pb2 import Person

def pb_to_json(pb_file_path, json_file_path):
    person_pb = Person()

    with open(pb_file_path, 'rb') as f:
        person_pb.ParseFromString(f.read())

    json_str = MessageToJson(person_pb)

    with open(json_file_path, 'w') as f:
        f.write(json_str)

# Uporaba, zamenji PATH 
pb_to_json('PATH', 'person_prevajanje.json')
```