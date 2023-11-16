## XML

XML (eXtensible Markup Language) je označevalni jezik, ki se uporablja za shranjevanje strukturiranih podatkov. Za razliko od JSON XML uporablja oznake, podobne HTML, za definiranje elementov in podatkov v teh elementih.

### Razlaga elementov XML
1. **Oznake**: Podatki XML so zaprti med začetno oznako `<tag>` in končno oznako `</tag>`.
2. **Elementi**: Element je sestavljen iz začetne oznake, podatkov in zaključne oznake. Na primer, `<name>Janez</name>`.
3. **Atributi**: Elementi imajo lahko atribute, ki nudijo dodatne informacije o elementu. Na primer, `<book id="101">`.
4. **Gnezdenje**: Elemente je mogoče ugnezditi znotraj drugih elementov, kar ustvari hierarhično strukturo.
5. **Komentarji**: Komentarji XML so podobni komentarjem HTML in so zaprti med `<!--` in `-->`.

#### Primeri
1. **Enostaven element**
     ```xml
     <name>Janez</name>
     ```
2. **Element z atributom**
     ```xml
     <book id="101">Lovilec v rži</book>
     ```
3. **Ugnezdeni elementi**
     ```xml
     <oseba>
       <name>Janez</name>
       <starost>30</starost>
     </oseba>
     ```
4. **Komentarji**
     ```xml
     <!-- To je komentar -->
     ```

---
Pythonova standardna knjižnica vključuje modul `ElementTree`, ki ponuja metode za razčlenjevanje in ustvarjanje dokumentov XML. To je bistveno za naloge, ki zahtevajo shranjevanje, prenos ali manipulacijo hierarhičnih ali strukturiranih podatkov v formatu XML.

### Operacije XML z uporabo Pythonove knjižnice ElementTree

1. **Serializacija**: Pretvarjanje pythonovih predmetov v format XML
     - `ElementTree.write()`: zapiše dokument XML v datoteko.
  
2. **Deserializacija**: pretvorba formata XML nazaj v pythonov objekt
     - `ElementTree.parse()`: razčleni celoten dokument XML v objekt ElementTree.
  
---
  
#### Vaja: Serializiraj, deserializiraj in manipuliraj s podatki XML

##### Serializirajte datoteko XML
Najprej bomo ustvarili predstavitev XML našega slovarja (isti kot pri JSON vaji).

```python
import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("person")

# Create sub-elements and set their values
name = ET.SubElement(root, "name")
name.text = "Alice"

age = ET.SubElement(root, "age")
age.text = "30"

address = ET.SubElement(root, "address")
street = ET.SubElement(address, "street")
street.text = "Dunajska"

city = ET.SubElement(address, "city")
city.text = "Ljubljana"

married = ET.SubElement(root, "married")
married.text = "True"

# Serialize to XML file
tree = ET.ElementTree(root)
tree.write("./DATA/person.xml")
```

##### Deserializacija XML datoteke

```python
# Parse the XML file
tree = ET.parse('./DATA/person.xml')
root = tree.getroot()
```

##### Manipulacija s podatki
Spremenimo `starost` na 31 in nastavimo status `poročena` na `False`.

```python
# Update age and married status
root.find("age").text = "31"
root.find("married").text = "False"

# Write the manipulated data back to the same XML file
tree.write("./DATA/person_updated.xml")
```
---
### Razlika med XML in JSON

XML in JSON imata bistveno različne strukture in konvencije, zato slovarja Python ne moremo neposredno prevesti v XML na enako preprost način kot smo to storili z JSON. JSON je seveda bolj primeren za podatkovne strukture, kot so slovarji ali asociativna polja, medtem ko je XML bolj dokumentno usmerjen in hierarhičen.

V XML morate upoštevati elemente, atribute in potencialno mešano vsebino, ki nimajo neposrednih analogij v slovarjih Python.

#### Ročno prevajanje z ElementTree

Pri uporabi knjižnic, kot je `ElementTree` v Pythonu, boste ročno ustvarili oznake XML, nastavili atribute in definirali hierarhične odnose med elementi.

Tukaj je preprost primer pretvorbe slovarja Python v XML:

```python
import xml.etree.ElementTree as ET

# Define the dictionary
person = {
  "name": "Alice",
  "age": 30,
  "address": {
    "street": "Dunajska",
    "city": "Ljubljana"
  },
  "married": True
}

# Create the root element
root = ET.Element("Person")

# Add child elements based on the dictionary
for key, value in person.items():
    if isinstance(value, dict):
        sub_elem = ET.SubElement(root, key)
        for sub_key, sub_value in value.items():
            sub_sub_elem = ET.SubElement(sub_elem, sub_key)
            sub_sub_elem.text = str(sub_value)
    else:
        elem = ET.SubElement(root, key)
        elem.text = str(value)

# Serialize to an XML string
tree = ET.ElementTree(root)
tree.write("./DATA/personNOVI.xml")
```
#### Funkcije serializacije po meri

Za bolj zapletene podatkovne strukture ali razrede bi običajno napisali funkcije serializacije in deserializacije, podobno kot smo implementirali  `to_dict()` in `from_dict()`,  za serializacijo JSON razreda `Person`.


