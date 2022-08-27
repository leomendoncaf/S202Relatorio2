from db.pokedex import Pokedex
from helper.WriteAJson import writeAJson

pokedex = Pokedex()


tipos = ["Water", "Ground"]
pokemons = db.collection.find({ "type": {"$in": tipos}})

pokemons = db.collection.find({"weaknesses": {"$size": 2}})

pokemons = db.collection.find({"$or": [{"type":"Grass"},{"weaknesses": "Lightning"}]})

pokemons = db.getPokemonEvolutionsByName("Charmeleon")

types = ["Rock","Grass"]
pokemons = db.getPokemonsByType(types)


