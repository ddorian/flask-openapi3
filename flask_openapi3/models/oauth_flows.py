# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2023/7/4 9:47
from typing import Optional

from pydantic import BaseModel

from . import MyBaseModel
from .oauth_flow import OAuthFlow


class OAuthFlows(MyBaseModel):
    """
    https://spec.openapis.org/oas/v3.1.0#oauth-flows-object
    """

    implicit: Optional[OAuthFlow] = None
    password: Optional[OAuthFlow] = None
    clientCredentials: Optional[OAuthFlow] = None
    authorizationCode: Optional[OAuthFlow] = None

    model_config = {
        "extra": "allow", "defer_build": True,
    }
