# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2023/7/4 9:47
from typing import Dict, Optional

from pydantic import BaseModel

from flask_openapi3.models import MyBaseModel


class OAuthFlow(MyBaseModel):
    """
    https://spec.openapis.org/oas/v3.1.0#oauth-flow-object
    """

    authorizationUrl: Optional[str] = None
    tokenUrl: Optional[str] = None
    refreshUrl: Optional[str] = None
    scopes: Dict[str, str]

    model_config = {
        "extra": "allow", "defer_build": True,
    }
