# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2023/7/4 9:41
from typing import Dict, Optional

from pydantic import BaseModel

from flask_openapi3.models import MyBaseModel


class Discriminator(MyBaseModel):
    """
    https://spec.openapis.org/oas/v3.1.0#discriminator-object
    """

    propertyName: str
    mapping: Optional[Dict[str, str]] = None

    model_config = {
        "extra": "allow", "defer_build": True,
    }
