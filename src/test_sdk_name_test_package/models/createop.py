"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from test_sdk_name_test_package.types import BaseModel
from typing_extensions import TypedDict


class CreateRequestBodyTypedDict(TypedDict):
    url: str
    r"""URL to shorten"""


class CreateRequestBody(BaseModel):
    url: str
    r"""URL to shorten"""
