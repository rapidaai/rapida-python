from typing import Union
from rapida.clients.protos.assistant_knowledge_pb2 import (
    GetAllAssistantKnowledgeRequest,
    GetAllAssistantKnowledgeResponse,
    GetAssistantKnowledgeRequest,
    GetAssistantKnowledgeResponse,
)

from rapida.clients.protos.common_pb2 import (
    GetAllAssistantConversationRequest,
    GetAllAssistantConversationResponse,
)
from rapida.clients.protos.assistant_webhook_pb2 import (
    GetAllAssistantWebhookLogRequest,
    GetAllAssistantWebhookLogResponse,
    GetAllAssistantWebhookRequest,
    GetAllAssistantWebhookResponse,
    GetAssistantWebhookLogRequest,
    GetAssistantWebhookLogResponse,
    GetAssistantWebhookRequest,
    GetAssistantWebhookResponse,
)
from rapida.clients.protos.assistant_tool_pb2 import (
    GetAllAssistantToolRequest,
    GetAllAssistantToolResponse,
    GetAssistantToolRequest,
    GetAssistantToolResponse,
)
from rapida.clients.protos.assistant_api_pb2 import (
    GetAllAssistantRequest,
    GetAllAssistantResponse,
    GetAssistantConversationRequest,
    GetAssistantConversationResponse,
)
from rapida.clients.protos.talk_api_pb2 import GetAssistantRequest, GetAssistantResponse
from rapida.connections import ConnectionConfig, UserAuthInfo, ClientAuthInfo


def get_assistant(
    client_cfg: ConnectionConfig,
    request: GetAssistantRequest,
    auth: Union[UserAuthInfo, ClientAuthInfo, None],
) -> GetAssistantResponse:
    if auth is None:
        auth = client_cfg.auth
    return client_cfg.assistant_client.GetAssistant(
        request,
        metadata=auth,
    )


def get_all_assistant(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantRequest,
    auth: Union[UserAuthInfo, ClientAuthInfo, None],
) -> GetAllAssistantResponse:
    if auth is None:
        auth = client_cfg.auth
    return client_cfg.assistant_client.GetAllAssistant(
        request,
        metadata=auth,
    )


def get_assistant_conversation(
    client_cfg: ConnectionConfig,
    request: GetAssistantConversationRequest,
    auth: Union[UserAuthInfo, ClientAuthInfo, None],
) -> GetAssistantConversationResponse:
    if auth is None:
        auth = client_cfg.auth
    return client_cfg.assistant_client.GetAssistantConversation(
        request,
        metadata=auth,
    )


def get_all_assistant_conversation(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantConversationRequest,
    auth: Union[UserAuthInfo, ClientAuthInfo, None],
) -> GetAllAssistantConversationResponse:
    if auth is None:
        auth = client_cfg.auth
    return client_cfg.assistant_client.GetAllAssistantConversation(
        request,
        metadata=auth,
    )


def get_assistant_webhook(
    client_cfg: ConnectionConfig,
    request: GetAssistantWebhookRequest,
    auth: Union[UserAuthInfo, ClientAuthInfo, None],
) -> GetAssistantWebhookResponse:
    if auth is None:
        auth = client_cfg.auth
    return client_cfg.assistant_client.GetAssistantWebhook(
        request,
        metadata=auth,
    )


def get_all_assistant_webhook(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantWebhookRequest,
    auth: Union[UserAuthInfo, ClientAuthInfo, None],
) -> GetAllAssistantWebhookResponse:
    if auth is None:
        auth = client_cfg.auth
    return client_cfg.assistant_client.GetAllAssistantWebhook(
        request,
        metadata=auth,
    )


def get_assistant_knowledge(
    client_cfg: ConnectionConfig,
    request: GetAssistantKnowledgeRequest,
    auth: Union[UserAuthInfo, ClientAuthInfo, None],
) -> GetAssistantKnowledgeResponse:
    if auth is None:
        auth = client_cfg.auth
    return client_cfg.assistant_client.GetAssistantKnowledge(
        request,
        metadata=auth,
    )


def get_all_assistant_knowledge(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantKnowledgeRequest,
    auth: Union[UserAuthInfo, ClientAuthInfo, None],
) -> GetAllAssistantKnowledgeResponse:
    if auth is None:
        auth = client_cfg.auth
    return client_cfg.assistant_client.GetAllAssistantKnowledge(
        request,
        metadata=auth,
    )


def get_assistant_tool(
    client_cfg: ConnectionConfig,
    request: GetAssistantToolRequest,
    auth: Union[UserAuthInfo, ClientAuthInfo, None],
) -> GetAssistantToolResponse:
    if auth is None:
        auth = client_cfg.auth
    return client_cfg.assistant_client.GetAssistantTool(
        request,
        metadata=auth,
    )


def get_all_assistant_tool(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantToolRequest,
    auth: Union[UserAuthInfo, ClientAuthInfo, None],
) -> GetAllAssistantToolResponse:
    if auth is None:
        auth = client_cfg.auth
    return client_cfg.assistant_client.GetAllAssistantTool(
        request,
        metadata=auth,
    )


def get_assistant_webhook_log(
    client_cfg: ConnectionConfig,
    request: GetAssistantWebhookLogRequest,
    auth: Union[UserAuthInfo, ClientAuthInfo, None],
) -> GetAssistantWebhookLogResponse:
    if auth is None:
        auth = client_cfg.auth
    return client_cfg.assistant_client.GetAssistantTool(
        request,
        metadata=auth,
    )


def get_all_assistant_webhook_log(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantWebhookLogRequest,
    auth: Union[UserAuthInfo, ClientAuthInfo, None],
) -> GetAllAssistantWebhookLogResponse:
    if auth is None:
        auth = client_cfg.auth
    return client_cfg.assistant_client.GetAllAssistantTool(
        request,
        metadata=auth,
    )
