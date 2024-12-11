# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2023/7/4 9:53
from typing import Dict, Optional

from pydantic import BaseModel

from . import MyBaseModel
from .media_type import MediaType


class RequestBody(MyBaseModel):
    """
    https://spec.openapis.org/oas/v3.1.0#request-body-object
    """

    description: Optional[str] = None
    content: Dict[str, MediaType]
    required: Optional[bool] = True

    model_config = {
        "extra": "allow", "defer_build": True,
    }
