from fastapi import APIRouter
from model.creature import Creature
import fake.creature as service

router = APIRouter(prefix="/creature")

@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()

@router.get("/{name}")
def get_one(name: str) -> Creature:
    return service.get_one(name)

@router.post("/")
def create(Creature: Creature) -> Creature:
    return service.create(Creature)

@router.patch("/{name}")
def modify(name: str, Creature: Creature) -> Creature:
    return service.modify(name, Creature)

@router.put("/{name}")
def replace(name: str, Creature: Creature) -> Creature:
    return service.replace(name, Creature)

@router.delete("/{name}")
def delete(name: str) -> bool:
    return service.delete(name)