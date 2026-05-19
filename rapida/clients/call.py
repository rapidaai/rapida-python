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

from rapida.clients.protos.talk_api_pb2 import (
    CreateBulkPhoneCallRequest,
    CreateBulkPhoneCallResponse,
    CreateConversationMetricRequest,
    CreateConversationMetricResponse,
    CreateMessageMetricRequest,
    CreateMessageMetricResponse,
    CreatePhoneCallRequest,
    CreatePhoneCallResponse,
)
from rapida.connections import ClientAuthInfo, ConnectionConfig, UserAuthInfo


AuthMetadata = Union[UserAuthInfo, ClientAuthInfo, None]


def _resolve_auth(
    client_cfg: ConnectionConfig,
    auth: AuthMetadata,
) -> Union[UserAuthInfo, ClientAuthInfo]:
    return client_cfg.auth if auth is None else auth


def _call_conversation_client(
    client_cfg: ConnectionConfig,
    method_name: str,
    request: Any,
    auth: AuthMetadata = None,
) -> Any:
    return getattr(client_cfg.conversation_client, method_name)(
        request,
        metadata=_resolve_auth(client_cfg, auth),
    )


def create_message_metric(
    client_cfg: ConnectionConfig,
    request: CreateMessageMetricRequest,
    auth: AuthMetadata = None,
) -> CreateMessageMetricResponse:
    return _call_conversation_client(client_cfg, "CreateMessageMetric", request, auth)


def create_conversation_metric(
    client_cfg: ConnectionConfig,
    request: CreateConversationMetricRequest,
    auth: AuthMetadata = None,
) -> CreateConversationMetricResponse:
    return _call_conversation_client(
        client_cfg,
        "CreateConversationMetric",
        request,
        auth,
    )


def create_phone_call(
    client_cfg: ConnectionConfig,
    request: CreatePhoneCallRequest,
    auth: AuthMetadata = None,
) -> CreatePhoneCallResponse:
    return _call_conversation_client(client_cfg, "CreatePhoneCall", request, auth)


def create_bulk_phone_call(
    client_cfg: ConnectionConfig,
    request: CreateBulkPhoneCallRequest,
    auth: AuthMetadata = None,
) -> CreateBulkPhoneCallResponse:
    return _call_conversation_client(client_cfg, "CreateBulkPhoneCall", request, auth)


__all__ = [
    "create_message_metric",
    "create_conversation_metric",
    "create_phone_call",
    "create_bulk_phone_call",
]
