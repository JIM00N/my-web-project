from model.explorer import Explorer

_explorers = [
    Explorer(name="Claude Hande",
             country="FR",
             description="보름달이 뜨면 만나기 힘듦"),
    
    Explorer(name="Noah Weiser",
             country="DE",
             description="눈이 나쁘고 벌목도를 가지고 다님"),
]

def get_all() -> list[Explorer]:
    return _explorers

def get_one(name: str) -> Explorer:
    for explorer in _explorers:
        if explorer.name == name:
            return explorer
    return None

def create(explorer: Explorer) -> Explorer:
    _explorers.append(explorer)
    return explorer

def modify(name: str, explorer: Explorer) -> Explorer:
    for i, e in enumerate(_explorers):
        if e.name == name:
            _explorers[i] = explorer
            return explorer
    return None

def replace(name: str, explorer: Explorer) -> Explorer:
    for i, e in enumerate(_explorers):
        if e.name == name:
            _explorers[i] = explorer
            return explorer
    return None

def delete(name: str) -> bool:
    for i, e in enumerate(_explorers):
        if e.name == name:
            del _explorers[i]
            return True
    return False
