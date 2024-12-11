# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2023/7/4 9:37
from typing import Optional

from pydantic import BaseModel

from flask_openapi3.models import MyBaseModel


class Contact(MyBaseModel):
    """
    https://spec.openapis.org/oas/v3.1.0#contact-object
    """

    name: Optional[str] = None
    url: Optional[str] = None
    email: Optional[str] = None

    model_config = {
        "extra": "allow", "defer_build": True,
    }
