# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2023/7/4 9:53
from pydantic import BaseModel, Field

from flask_openapi3.models import MyBaseModel


class Reference(MyBaseModel):
    """
    https://spec.openapis.org/oas/v3.1.0#reference-object
    """

    ref: str = Field(..., alias="$ref")

    model_config = {
        "extra": "allow", "defer_build": True,
    }
