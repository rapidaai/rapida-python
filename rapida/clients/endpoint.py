#  Copyright (c) 2024. Rapida
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#
#  Author: Prashant <prashant@rapida.ai>

from typing import Any, Union

from rapida.clients.protos.common_pb2 import BaseResponse
from rapida.clients.protos.endpoint_api_pb2 import (
    CreateEndpointCacheConfigurationRequest,
    CreateEndpointCacheConfigurationResponse,
    CreateEndpointProviderModelRequest,
    CreateEndpointProviderModelResponse,
    CreateEndpointRequest,
    CreateEndpointResponse,
    CreateEndpointRetryConfigurationRequest,
    CreateEndpointRetryConfigurationResponse,
    CreateEndpointTagRequest,
    ForkEndpointRequest,
    GetAllEndpointLogRequest,
    GetAllEndpointLogResponse,
    GetAllEndpointProviderModelRequest,
    GetAllEndpointProviderModelResponse,
    GetAllEndpointRequest,
    GetAllEndpointResponse,
    GetEndpointLogRequest,
    GetEndpointLogResponse,
    GetEndpointRequest,
    GetEndpointResponse,
    UpdateEndpointDetailRequest,
    UpdateEndpointVersionRequest,
    UpdateEndpointVersionResponse,
)
from rapida.connections import ClientAuthInfo, ConnectionConfig, UserAuthInfo


AuthMetadata = Union[UserAuthInfo, ClientAuthInfo, None]


def _resolve_auth(
    client_cfg: ConnectionConfig,
    auth: AuthMetadata,
) -> Union[UserAuthInfo, ClientAuthInfo]:
    return client_cfg.auth if auth is None else auth


def _call_endpoint_client(
    client_cfg: ConnectionConfig,
    method_name: str,
    request: Any,
    auth: AuthMetadata = None,
) -> Any:
    return getattr(client_cfg.endpoint_client, method_name)(
        request,
        metadata=_resolve_auth(client_cfg, auth),
    )


def get_endpoint(
    client_cfg: ConnectionConfig,
    request: GetEndpointRequest,
    auth: AuthMetadata = None,
) -> GetEndpointResponse:
    return _call_endpoint_client(client_cfg, "GetEndpoint", request, auth)


def get_all_endpoint(
    client_cfg: ConnectionConfig,
    request: GetAllEndpointRequest,
    auth: AuthMetadata = None,
) -> GetAllEndpointResponse:
    return _call_endpoint_client(client_cfg, "GetAllEndpoint", request, auth)


def get_all_endpoint_provider_model(
    client_cfg: ConnectionConfig,
    request: GetAllEndpointProviderModelRequest,
    auth: AuthMetadata = None,
) -> GetAllEndpointProviderModelResponse:
    return _call_endpoint_client(
        client_cfg,
        "GetAllEndpointProviderModel",
        request,
        auth,
    )


def update_endpoint_version(
    client_cfg: ConnectionConfig,
    request: UpdateEndpointVersionRequest,
    auth: AuthMetadata = None,
) -> UpdateEndpointVersionResponse:
    return _call_endpoint_client(client_cfg, "UpdateEndpointVersion", request, auth)


def create_endpoint(
    client_cfg: ConnectionConfig,
    request: CreateEndpointRequest,
    auth: AuthMetadata = None,
) -> CreateEndpointResponse:
    return _call_endpoint_client(client_cfg, "CreateEndpoint", request, auth)


def create_endpoint_provider_model(
    client_cfg: ConnectionConfig,
    request: CreateEndpointProviderModelRequest,
    auth: AuthMetadata = None,
) -> CreateEndpointProviderModelResponse:
    return _call_endpoint_client(
        client_cfg,
        "CreateEndpointProviderModel",
        request,
        auth,
    )


def create_endpoint_cache_configuration(
    client_cfg: ConnectionConfig,
    request: CreateEndpointCacheConfigurationRequest,
    auth: AuthMetadata = None,
) -> CreateEndpointCacheConfigurationResponse:
    return _call_endpoint_client(
        client_cfg,
        "CreateEndpointCacheConfiguration",
        request,
        auth,
    )


def create_endpoint_retry_configuration(
    client_cfg: ConnectionConfig,
    request: CreateEndpointRetryConfigurationRequest,
    auth: AuthMetadata = None,
) -> CreateEndpointRetryConfigurationResponse:
    return _call_endpoint_client(
        client_cfg,
        "CreateEndpointRetryConfiguration",
        request,
        auth,
    )


def create_endpoint_tag(
    client_cfg: ConnectionConfig,
    request: CreateEndpointTagRequest,
    auth: AuthMetadata = None,
) -> GetEndpointResponse:
    return _call_endpoint_client(client_cfg, "CreateEndpointTag", request, auth)


def fork_endpoint(
    client_cfg: ConnectionConfig,
    request: ForkEndpointRequest,
    auth: AuthMetadata = None,
) -> BaseResponse:
    return _call_endpoint_client(client_cfg, "ForkEndpoint", request, auth)


def update_endpoint_detail(
    client_cfg: ConnectionConfig,
    request: UpdateEndpointDetailRequest,
    auth: AuthMetadata = None,
) -> GetEndpointResponse:
    return _call_endpoint_client(client_cfg, "UpdateEndpointDetail", request, auth)


def get_endpoint_log(
    client_cfg: ConnectionConfig,
    request: GetEndpointLogRequest,
    auth: AuthMetadata = None,
) -> GetEndpointLogResponse:
    return _call_endpoint_client(client_cfg, "GetEndpointLog", request, auth)


def get_all_endpoint_log(
    client_cfg: ConnectionConfig,
    request: GetAllEndpointLogRequest,
    auth: AuthMetadata = None,
) -> GetAllEndpointLogResponse:
    return _call_endpoint_client(client_cfg, "GetAllEndpointLog", request, auth)


__all__ = [
    "get_endpoint",
    "get_all_endpoint",
    "get_all_endpoint_provider_model",
    "update_endpoint_version",
    "create_endpoint",
    "create_endpoint_provider_model",
    "create_endpoint_cache_configuration",
    "create_endpoint_retry_configuration",
    "create_endpoint_tag",
    "fork_endpoint",
    "update_endpoint_detail",
    "get_endpoint_log",
    "get_all_endpoint_log",
]
