from dataclasses import dataclass

@dataclass
class User(object):
    id: int
    username: str
    password: str
    name: str
    budget: float
    salary: float
