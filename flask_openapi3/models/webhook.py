# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2023/7/4 9:35
from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:  # pragma: no cover
    from .path_item import PathItem
else:
    PathItem = "PathItem"

"""
https://spec.openapis.org/oas/v3.1.0#oasWebhooks
"""
Webhook = Dict[str, PathItem]
