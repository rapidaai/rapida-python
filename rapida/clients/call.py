from typing import Union
from rapida.clients.protos.talk_api_pb2 import (
    CreateBulkPhoneCallRequest,
    CreateBulkPhoneCallResponse,
    CreatePhoneCallRequest,
    CreatePhoneCallResponse,
)
from rapida.connections import ConnectionConfig, UserAuthInfo, ClientAuthInfo


def create_phone_call(
    client_cfg: ConnectionConfig,
    request: CreatePhoneCallRequest,
    auth: Union[UserAuthInfo, ClientAuthInfo, None],
) -> CreatePhoneCallResponse:
    if auth is None:
        auth = client_cfg.auth
    return client_cfg.conversation_client.CreatePhoneCall(
        request,
        metadata=auth,
    )


def create_bulk_phone_call(
    client_cfg: ConnectionConfig,
    request: CreateBulkPhoneCallRequest,
    auth: Union[UserAuthInfo, ClientAuthInfo, None],
) -> CreateBulkPhoneCallResponse:
    if auth is None:
        auth = client_cfg.auth
    return client_cfg.conversation_client.CreateBulkPhoneCall(
        request,
        metadata=auth,
    )
