from typing import Optional

from pydantic import BaseModel

from . import MyBaseModel
from .external_documentation import ExternalDocumentation


class Tag(MyBaseModel):
    """
    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md#tag-object
    """

    name: str
    description: Optional[str] = None
    externalDocs: Optional[ExternalDocumentation] = None

    model_config = {
        "extra": "allow", "defer_build": True,
    }
