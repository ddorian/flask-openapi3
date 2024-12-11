# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2023/7/4 9:42
from typing import Any, Optional

from pydantic import BaseModel

from flask_openapi3.models import MyBaseModel


class Example(MyBaseModel):
    """
    https://spec.openapis.org/oas/v3.1.0#example-object
    """

    summary: Optional[str] = None
    description: Optional[str] = None
    value: Optional[Any] = None
    externalValue: Optional[str] = None

    model_config = {
        "extra": "allow", "defer_build": True,
    }
