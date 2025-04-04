from model.creature import Creature

_creatures = [
    Creature(name="Yeti",
             aka="Abominable Snowman",
             area="Himalayas",
             country="CN",
             description="A large ape-like creature said to inhabit the Himalayan mountains."),
    Creature(name="Bigfoot",
             aka="Sasquatch",
             area="*",
             country="US",
             description="A large hairy humanoid said to inhabit North American forests.")
]

def get_all() -> list[Creature]:
    return _creatures

def get_one(name: str) -> Creature:
    for creature in _creatures:
        if creature.name == name:
            return creature
    return None

def create(creature: Creature) -> Creature:
    _creatures.append(creature)
    return creature

def modify(name: str, creature: Creature) -> Creature:
    for i, e in enumerate(_creatures):
        if e.name == name:
            _creatures[i] = creature
            return creature
    return None

def replace(name: str, creature: Creature) -> Creature:
    for i, e in enumerate(_creatures):
        if e.name == name:
            _creatures[i] = creature
            return creature
    return None

def delete(name: str) -> bool:
    for i, e in enumerate(_creatures):
        if e.name == name:
            del _creatures[i]
            return True
    return False
