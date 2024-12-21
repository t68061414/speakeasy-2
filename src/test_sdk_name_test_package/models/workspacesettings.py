"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from test_sdk_name_test_package.types import BaseModel
from typing_extensions import TypedDict


class WorkspaceSettingsTypedDict(TypedDict):
    workspace_id: str
    webhook_url: str
    created_at: datetime
    updated_at: datetime


class WorkspaceSettings(BaseModel):
    workspace_id: str

    webhook_url: str

    created_at: datetime

    updated_at: datetime
