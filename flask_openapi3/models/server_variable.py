# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2023/7/4 9:57
from typing import List, Optional

from pydantic import BaseModel

from flask_openapi3.models import MyBaseModel


class ServerVariable(MyBaseModel):
    """
    https://spec.openapis.org/oas/v3.1.0#server-variable-object
    """

    enum: List[str]
    default: str
    description: Optional[str] = None

    model_config = {
        "extra": "allow", "defer_build": True,
    }
