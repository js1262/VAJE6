## JSON

JSON ima preprosto in berljivo sintakso, ki vključuje elemente, kot so objekti (objects), matrike (arrays), ključi (keys) in vrednosti (values).

### JSON elementi

1. **Objekti (Objects)**: Objekt v JSON je neurejen nabor ključ-vrednost parov, zaprt v zavitih oklepajih `{}`.  
2. **Matrike-vektorji (Arrays)**: Matrika JSON je urejena zbirka vrednosti, zaprta v oglatih oklepajih `[]`.
3. **Ključi (Keys)**: Ključi so nizi, ki identificirajo vrednosti znotraj objekta. Morajo biti edinstveni znotraj tega objekta.
4. **Vrednosti (Values)**: Vrednosti so lahko nizi, števila, objekti, matrike, `true`, `false` ali `null`.
5. **Gnezdjenje (Nesting)**: Tako objekti kot matrike se lahko gnezdijo drug v drugega, kar omogoča kompleksne, hierarhične strukture podatkov.

Ta tabela pomaga hitro identificirati preslikavo med podatkovnimi tipi Python in podatkovnimi tipi JSON, kar je bistveno pri delu s seralizacijo in deseralizacijo med obema.

Kodiranje/seralizacija (Pisanje podatkov na disk) ->    

Decodiranje/deseralizacija (Branje podatkov v pomnilnik) <-   

| Python       | JSON    |
|--------------|---------|
| `dict`       | object  |
| `list`, `tuple` | array  |
| `str`        | string  |
| `int`, `long`, `float` | number |
| `True`       | true    |
| `False`      | false   |
| `None`       | null    |

---
#### Primer JSON sintakse

1. **preprost Objekt**
    ```json
    {
      "name": "John",
      "age": 30,
      "is_student": false
    }
    ```
2. **Preprosta matrika/vektor**
    ```json
    [10, 20, 30, 40, 50]
    ```
3. **Gnezdenje**
    ```json
    {
      "name": "John",
      "details": {
        "age": 30,
        "is_student": false
      }
    }
    ```
4. **Objekt z vektorji**
    ```json
    {
      "name": "John",
      "scores": [90, 85, 77, 92]
    }
    ```


### Operacije z JSON s pomočjo Pythonove knjižnice json

1. **Serializacija**: Pretvorba Pythonovih objektov v format JSON
    - `json.dump()`: Zapiše Pythonov objekt v datotečni objekt v formatu JSON.
    - `json.dumps()`: Vrne niz, ki predstavlja Pythonov objekt v formatu JSON.
  
2. **Deserializacija**: Pretvorba formata JSON v Pythonove objekte
    - `json.load()`: Prebere datotečni objekt, ki vsebuje dokument JSON, in vrne Pythonov objekt.
    - `json.loads()`: Prebere niz v formatu JSON in vrne Pythonov objekt.

3. **Uporabni ključni argumenti (estetika)**: 
    - `indent`: Določa število presledkov za zamik ravni objekta JSON.
    - `sort_keys`: Uredi ključe v izhodu.

---
#### Vaja: Seraliziraj, deseraliziraj in manipuliraj podatke JSON

##### Serializacija datoteke JSON
Uporabili bomo dani Pythonov slovar, da ga seraliziramo v datoteko JSON.

```python
import json

person = {
  "name": "Alice",
  "age": 30,
  "address": {
    "street": "Dunajska",
    "city": "Ljubljana"
  },
  "married": True
}

with open('./DATA/person.json', 'w') as f:
    json.dump(person, f, indent=4, sort_keys=True)
```

Output je JSON datoteka z imenom `person.json` kjer imamo serializiran pythonov dictionary.

##### Deserializacija JSON datoteke
Zdaj pa preberimo JSON datoteko v Pythonov object.

```python
with open('./DATA/person.json', 'r') as f:
    deserialized_person = json.load(f)
```

##### Manipulacija podatkov
Spremenili bomo  `age` osebe in nastavili status `married` na `False`.

```python
deserialized_person['age'] = 31
deserialized_person['married'] = False
```

##### Ponovni zapis (serializacija) v JSON datoteko


```python
with open('./DATA/person.json', 'w') as f:
    json.dump(deserialized_person, f, indent=4, sort_keys=True)
```


---

### Opozorilo: Pretvorbe niso popolne, kar pomeni, da če predmet kodirate zdaj in ga dekodirate pozneje, morda ne boste dobili popolnoma enakega predmeta nazaj.

```python
blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)

blackjack_hand == decoded_hand

type(blackjack_hand)

type(decoded_hand)

blackjack_hand == tuple(decoded_hand)
```

