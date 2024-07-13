from typing import List

from pydantic import BaseModel

class Package(BaseModel):
    id: str
    name: str
    status: str
    

class OrderPackages(BaseModel):
    result: List[Package]