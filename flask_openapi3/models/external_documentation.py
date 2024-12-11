# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2023/7/4 9:43
from typing import Optional

from pydantic import BaseModel

from flask_openapi3.models import MyBaseModel


class ExternalDocumentation(MyBaseModel):
    """
    https://spec.openapis.org/oas/v3.1.0#external-documentation-object
    """

    description: Optional[str] = None
    url: str

    model_config = {
        "extra": "allow", "defer_build": True,
    }
