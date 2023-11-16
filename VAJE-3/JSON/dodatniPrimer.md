
# DODATNI PRIMER (NI POTREBEN) za custom python podatkovno strukturo Razred/Class  `Person`

Začeli bomo z razredom Python, imenovanim `Person`. Ta razred bo imel nekaj atributov, kot so `name`, `age`, `address` in `married`, skupaj z metodami za nastavitev in pridobivanje teh atributov.
V podatkovnem tipu razred lahko definiramo več podstruktur. V spodnjem primeru imamo:
- našo podatkovno strukturo `def __init__` kjer opredelimo shemo
- funkcijo `def to_dict` za pretvorbo v strukturo dictionary (zato da bomo lahko pretvorili v JSON datoteko)
- funkcijo `def from_dict` za pretvorbo iz dictionary nazaj v naš objekt, ki je class (kar je definirano po `__init__`


```python
class Person:
    def __init__(self, name, age, address, married):
        self.name = name
        self.age = age
        self.address = address
        self.married = married

    def to_dict(self):
        """Converts the object to a dictionary representation."""
        return {
            'name': self.name,
            'age': self.age,
            'address': self.address,
            'married': self.married
        }

    @classmethod
    def from_dict(cls, data):
        """Creates an object from its dictionary representation."""
        return cls(
            name=data['name'],
            age=data['age'],
            address=data['address'],
            married=data['married']
        )
```

#### Serializacija v JSON

Za serializacijo primerka `Person` v JSON, ga bomo najprej pretvorili v slovar z uporabo metode `to_dict()`, nato pa uporabili Pythonovo knjižnico `json` za serializacijo slovarja.

```python
import json

# Create a Person object
alice = Person("Alice", 30, "Dunajska, Ljubljana", True)

# Convert the Person object to a dictionary
alice_dict = alice.to_dict()

# Serialize the dictionary to a JSON-formatted string
alice_json = json.dumps(alice_dict, indent=4)
```

#### Deserializacija iz JSON

Za deserializacijo niza, oblikovanega v obliki JSON, nazaj v objekt `Person`, bomo uporabili Pythonovo knjižnico `json` za pretvorbo niza v slovar, nato pa uporabili metodo razreda `from_dict()` za ustvarjanje primerka `Person` .

```python
# Deserialize the JSON-formatted string to a dictionary
alice_dict_from_json = json.loads(alice_json)

# Create a Person object from the dictionary
alice_obj = Person.from_dict(alice_dict_from_json)
```
