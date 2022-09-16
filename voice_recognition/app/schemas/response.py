from typing import Generic, Optional, TypeVar
from pydantic.generics import GenericModel

DataType = TypeVar("DataType")

class ResponseBase(GenericModel, Generic[DataType]):
    message: str = ""
    meta: dict = {}
    text: str

class GetResponse(ResponseBase[DataType], Generic[DataType]):
    message: str = "Data got correctly"

class PostResponse(ResponseBase[DataType], Generic[DataType]):
    message: str = "Audio transcribed correctly"
