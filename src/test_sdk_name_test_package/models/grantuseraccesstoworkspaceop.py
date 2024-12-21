"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from test_sdk_name_test_package.types import BaseModel
from test_sdk_name_test_package.utils import FieldMetadata, PathParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GrantUserAccessToWorkspaceGlobalsTypedDict(TypedDict):
    workspace_id: NotRequired[str]


class GrantUserAccessToWorkspaceGlobals(BaseModel):
    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None


class GrantUserAccessToWorkspaceRequestTypedDict(TypedDict):
    email: str
    r"""Email of the user to grant access to."""
    workspace_id: NotRequired[str]
    r"""Unique identifier of the workspace."""


class GrantUserAccessToWorkspaceRequest(BaseModel):
    email: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Email of the user to grant access to."""

    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None
    r"""Unique identifier of the workspace."""
