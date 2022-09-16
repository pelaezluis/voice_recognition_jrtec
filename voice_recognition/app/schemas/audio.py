from typing import Optional
from pydantic import BaseModel

class Audio(BaseModel):
    id: Optional[str]
    audio_in: str
    text: str