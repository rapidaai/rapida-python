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

from rapida.clients.protos.invoker_api_pb2 import (
    InvokeRequest,
    InvokeResponse,
    ProbeRequest,
    ProbeResponse,
    UpdateRequest,
    UpdateResponse,
)
from rapida.connections import ClientAuthInfo, ConnectionConfig, UserAuthInfo


AuthMetadata = Union[UserAuthInfo, ClientAuthInfo, None]


def _resolve_auth(
    client_cfg: ConnectionConfig,
    auth: AuthMetadata,
) -> Union[UserAuthInfo, ClientAuthInfo]:
    return client_cfg.auth if auth is None else auth


def _call_deployment_client(
    client_cfg: ConnectionConfig,
    method_name: str,
    request: Any,
    auth: AuthMetadata = None,
) -> Any:
    return getattr(client_cfg.deployment_client, method_name)(
        request,
        metadata=_resolve_auth(client_cfg, auth),
    )


def invoke(
    client_cfg: ConnectionConfig,
    request: InvokeRequest,
    auth: AuthMetadata = None,
) -> InvokeResponse:
    return _call_deployment_client(client_cfg, "Invoke", request, auth)


def update(
    client_cfg: ConnectionConfig,
    request: UpdateRequest,
    auth: AuthMetadata = None,
) -> UpdateResponse:
    return _call_deployment_client(client_cfg, "Update", request, auth)


def probe(
    client_cfg: ConnectionConfig,
    request: ProbeRequest,
    auth: AuthMetadata = None,
) -> ProbeResponse:
    return _call_deployment_client(client_cfg, "Probe", request, auth)


__all__ = [
    "invoke",
    "update",
    "probe",
]
