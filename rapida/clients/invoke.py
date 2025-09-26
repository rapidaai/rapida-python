from typing import Union
from rapida.clients.protos.invoker_api_pb2 import (
    InvokeRequest,
    InvokeResponse,
)
from rapida.connections import ConnectionConfig, UserAuthInfo, ClientAuthInfo


def invoke(
    client_cfg: ConnectionConfig,
    request: InvokeRequest,
    auth: Union[UserAuthInfo, ClientAuthInfo, None],
) -> InvokeResponse:
    if auth is None:
        auth = client_cfg.auth

    return client_cfg.deployment_client.Invoke(
        request,
        metadata=auth,
    )
