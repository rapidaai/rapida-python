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

from rapida.clients.protos.assistant_analysis_pb2 import (
    CreateAssistantAnalysisRequest,
    DeleteAssistantAnalysisRequest,
    GetAllAssistantAnalysisRequest,
    GetAllAssistantAnalysisResponse,
    GetAssistantAnalysisRequest,
    GetAssistantAnalysisResponse,
    UpdateAssistantAnalysisRequest,
)
from rapida.clients.protos.assistant_api_pb2 import (
    CreateAssistantAuthenticationRequest,
    CreateAssistantRequest,
    CreateAssistantTagRequest,
    CreateAssistantTelemetryProviderRequest,
    DeleteAssistantRequest,
    DeleteAssistantTelemetryProviderRequest,
    DisableAssistantAuthenticationRequest,
    GetAllAssistantMessageRequest,
    GetAllAssistantMessageResponse,
    GetAllAssistantRequest,
    GetAllAssistantResponse,
    GetAllAssistantTelemetryProviderRequest,
    GetAllAssistantTelemetryProviderResponse,
    GetAllAssistantTelemetryRequest,
    GetAllAssistantTelemetryResponse,
    GetAllMessageRequest,
    GetAllMessageResponse,
    GetAssistantAuthenticationRequest,
    GetAssistantAuthenticationResponse,
    GetAssistantConversationRequest,
    GetAssistantConversationResponse,
    GetAssistantRequest,
    GetAssistantResponse,
    GetAssistantTelemetryProviderRequest,
    GetAssistantTelemetryProviderResponse,
    UpdateAssistantDetailRequest,
    UpdateAssistantTelemetryProviderRequest,
)
from rapida.clients.protos.assistant_knowledge_pb2 import (
    CreateAssistantKnowledgeRequest,
    DeleteAssistantKnowledgeRequest,
    GetAllAssistantKnowledgeRequest,
    GetAllAssistantKnowledgeResponse,
    GetAssistantKnowledgeRequest,
    GetAssistantKnowledgeResponse,
    UpdateAssistantKnowledgeRequest,
)
from rapida.clients.protos.assistant_provider_pb2 import (
    CreateAssistantProviderRequest,
    GetAllAssistantProviderRequest,
    GetAllAssistantProviderResponse,
    GetAssistantProviderResponse,
    UpdateAssistantVersionRequest,
)
from rapida.clients.protos.assistant_tool_pb2 import (
    CreateAssistantToolRequest,
    DeleteAssistantToolRequest,
    GetAllAssistantToolLogRequest,
    GetAllAssistantToolLogResponse,
    GetAllAssistantToolRequest,
    GetAllAssistantToolResponse,
    GetAssistantToolLogRequest,
    GetAssistantToolLogResponse,
    GetAssistantToolRequest,
    GetAssistantToolResponse,
    UpdateAssistantToolRequest,
)
from rapida.clients.protos.assistant_webhook_pb2 import (
    CreateAssistantWebhookRequest,
    DeleteAssistantWebhookRequest,
    GetAllAssistantHTTPLogRequest,
    GetAllAssistantHTTPLogResponse,
    GetAllAssistantWebhookRequest,
    GetAllAssistantWebhookResponse,
    GetAssistantHTTPLogRequest,
    GetAssistantHTTPLogResponse,
    GetAssistantWebhookRequest,
    GetAssistantWebhookResponse,
    RetryAssistantHTTPLogRequest,
    UpdateAssistantWebhookRequest,
)
from rapida.clients.protos.common_pb2 import (
    GetAllAssistantConversationRequest,
    GetAllAssistantConversationResponse,
    GetAllConversationMessageRequest,
    GetAllConversationMessageResponse,
)
from rapida.connections import ClientAuthInfo, ConnectionConfig, UserAuthInfo


AuthMetadata = Union[UserAuthInfo, ClientAuthInfo, None]


def _resolve_auth(
    client_cfg: ConnectionConfig,
    auth: AuthMetadata,
) -> Union[UserAuthInfo, ClientAuthInfo]:
    return client_cfg.auth if auth is None else auth


def _call_assistant_client(
    client_cfg: ConnectionConfig,
    method_name: str,
    request: Any,
    auth: AuthMetadata = None,
) -> Any:
    return getattr(client_cfg.assistant_client, method_name)(
        request,
        metadata=_resolve_auth(client_cfg, auth),
    )


def get_assistant(
    client_cfg: ConnectionConfig,
    request: GetAssistantRequest,
    auth: AuthMetadata = None,
) -> GetAssistantResponse:
    return _call_assistant_client(client_cfg, "GetAssistant", request, auth)


def get_all_assistant(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantRequest,
    auth: AuthMetadata = None,
) -> GetAllAssistantResponse:
    return _call_assistant_client(client_cfg, "GetAllAssistant", request, auth)


def create_assistant(
    client_cfg: ConnectionConfig,
    request: CreateAssistantRequest,
    auth: AuthMetadata = None,
) -> GetAssistantResponse:
    return _call_assistant_client(client_cfg, "CreateAssistant", request, auth)


def delete_assistant(
    client_cfg: ConnectionConfig,
    request: DeleteAssistantRequest,
    auth: AuthMetadata = None,
) -> GetAssistantResponse:
    return _call_assistant_client(client_cfg, "DeleteAssistant", request, auth)


def get_all_assistant_provider(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantProviderRequest,
    auth: AuthMetadata = None,
) -> GetAllAssistantProviderResponse:
    return _call_assistant_client(client_cfg, "GetAllAssistantProvider", request, auth)


def create_assistant_provider(
    client_cfg: ConnectionConfig,
    request: CreateAssistantProviderRequest,
    auth: AuthMetadata = None,
) -> GetAssistantProviderResponse:
    return _call_assistant_client(client_cfg, "CreateAssistantProvider", request, auth)


def create_assistant_tag(
    client_cfg: ConnectionConfig,
    request: CreateAssistantTagRequest,
    auth: AuthMetadata = None,
) -> GetAssistantResponse:
    return _call_assistant_client(client_cfg, "CreateAssistantTag", request, auth)


def update_assistant_version(
    client_cfg: ConnectionConfig,
    request: UpdateAssistantVersionRequest,
    auth: AuthMetadata = None,
) -> GetAssistantResponse:
    return _call_assistant_client(client_cfg, "UpdateAssistantVersion", request, auth)


def update_assistant_detail(
    client_cfg: ConnectionConfig,
    request: UpdateAssistantDetailRequest,
    auth: AuthMetadata = None,
) -> GetAssistantResponse:
    return _call_assistant_client(client_cfg, "UpdateAssistantDetail", request, auth)


def get_all_assistant_message(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantMessageRequest,
    auth: AuthMetadata = None,
) -> GetAllAssistantMessageResponse:
    return _call_assistant_client(client_cfg, "GetAllAssistantMessage", request, auth)


def get_all_conversation_message(
    client_cfg: ConnectionConfig,
    request: GetAllConversationMessageRequest,
    auth: AuthMetadata = None,
) -> GetAllConversationMessageResponse:
    return _call_assistant_client(client_cfg, "GetAllConversationMessage", request, auth)


def get_all_message(
    client_cfg: ConnectionConfig,
    request: GetAllMessageRequest,
    auth: AuthMetadata = None,
) -> GetAllMessageResponse:
    return _call_assistant_client(client_cfg, "GetAllMessage", request, auth)


def get_all_assistant_telemetry(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantTelemetryRequest,
    auth: AuthMetadata = None,
) -> GetAllAssistantTelemetryResponse:
    return _call_assistant_client(client_cfg, "GetAllAssistantTelemetry", request, auth)


def get_assistant_telemetry_provider(
    client_cfg: ConnectionConfig,
    request: GetAssistantTelemetryProviderRequest,
    auth: AuthMetadata = None,
) -> GetAssistantTelemetryProviderResponse:
    return _call_assistant_client(
        client_cfg,
        "GetAssistantTelemetryProvider",
        request,
        auth,
    )


def get_all_assistant_telemetry_provider(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantTelemetryProviderRequest,
    auth: AuthMetadata = None,
) -> GetAllAssistantTelemetryProviderResponse:
    return _call_assistant_client(
        client_cfg,
        "GetAllAssistantTelemetryProvider",
        request,
        auth,
    )


def create_assistant_telemetry_provider(
    client_cfg: ConnectionConfig,
    request: CreateAssistantTelemetryProviderRequest,
    auth: AuthMetadata = None,
) -> GetAssistantTelemetryProviderResponse:
    return _call_assistant_client(
        client_cfg,
        "CreateAssistantTelemetryProvider",
        request,
        auth,
    )


def update_assistant_telemetry_provider(
    client_cfg: ConnectionConfig,
    request: UpdateAssistantTelemetryProviderRequest,
    auth: AuthMetadata = None,
) -> GetAssistantTelemetryProviderResponse:
    return _call_assistant_client(
        client_cfg,
        "UpdateAssistantTelemetryProvider",
        request,
        auth,
    )


def delete_assistant_telemetry_provider(
    client_cfg: ConnectionConfig,
    request: DeleteAssistantTelemetryProviderRequest,
    auth: AuthMetadata = None,
) -> GetAssistantTelemetryProviderResponse:
    return _call_assistant_client(
        client_cfg,
        "DeleteAssistantTelemetryProvider",
        request,
        auth,
    )


def create_assistant_authentication(
    client_cfg: ConnectionConfig,
    request: CreateAssistantAuthenticationRequest,
    auth: AuthMetadata = None,
) -> GetAssistantAuthenticationResponse:
    return _call_assistant_client(
        client_cfg,
        "CreateAssistantAuthentication",
        request,
        auth,
    )


def get_assistant_authentication(
    client_cfg: ConnectionConfig,
    request: GetAssistantAuthenticationRequest,
    auth: AuthMetadata = None,
) -> GetAssistantAuthenticationResponse:
    return _call_assistant_client(
        client_cfg,
        "GetAssistantAuthentication",
        request,
        auth,
    )


def disable_assistant_authentication(
    client_cfg: ConnectionConfig,
    request: DisableAssistantAuthenticationRequest,
    auth: AuthMetadata = None,
) -> GetAssistantAuthenticationResponse:
    return _call_assistant_client(
        client_cfg,
        "DisableAssistantAuthentication",
        request,
        auth,
    )


def get_assistant_conversation(
    client_cfg: ConnectionConfig,
    request: GetAssistantConversationRequest,
    auth: AuthMetadata = None,
) -> GetAssistantConversationResponse:
    return _call_assistant_client(client_cfg, "GetAssistantConversation", request, auth)


def get_all_assistant_conversation(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantConversationRequest,
    auth: AuthMetadata = None,
) -> GetAllAssistantConversationResponse:
    return _call_assistant_client(
        client_cfg,
        "GetAllAssistantConversation",
        request,
        auth,
    )


def get_assistant_http_log(
    client_cfg: ConnectionConfig,
    request: GetAssistantHTTPLogRequest,
    auth: AuthMetadata = None,
) -> GetAssistantHTTPLogResponse:
    return _call_assistant_client(client_cfg, "GetAssistantHTTPLog", request, auth)


def get_all_assistant_http_log(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantHTTPLogRequest,
    auth: AuthMetadata = None,
) -> GetAllAssistantHTTPLogResponse:
    return _call_assistant_client(client_cfg, "GetAllAssistantHTTPLog", request, auth)


def retry_assistant_http_log(
    client_cfg: ConnectionConfig,
    request: RetryAssistantHTTPLogRequest,
    auth: AuthMetadata = None,
) -> GetAssistantHTTPLogResponse:
    return _call_assistant_client(client_cfg, "RetryAssistantHTTPLog", request, auth)


def get_assistant_webhook(
    client_cfg: ConnectionConfig,
    request: GetAssistantWebhookRequest,
    auth: AuthMetadata = None,
) -> GetAssistantWebhookResponse:
    return _call_assistant_client(client_cfg, "GetAssistantWebhook", request, auth)


def get_all_assistant_webhook(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantWebhookRequest,
    auth: AuthMetadata = None,
) -> GetAllAssistantWebhookResponse:
    return _call_assistant_client(client_cfg, "GetAllAssistantWebhook", request, auth)


def create_assistant_webhook(
    client_cfg: ConnectionConfig,
    request: CreateAssistantWebhookRequest,
    auth: AuthMetadata = None,
) -> GetAssistantWebhookResponse:
    return _call_assistant_client(client_cfg, "CreateAssistantWebhook", request, auth)


def update_assistant_webhook(
    client_cfg: ConnectionConfig,
    request: UpdateAssistantWebhookRequest,
    auth: AuthMetadata = None,
) -> GetAssistantWebhookResponse:
    return _call_assistant_client(client_cfg, "UpdateAssistantWebhook", request, auth)


def delete_assistant_webhook(
    client_cfg: ConnectionConfig,
    request: DeleteAssistantWebhookRequest,
    auth: AuthMetadata = None,
) -> GetAssistantWebhookResponse:
    return _call_assistant_client(client_cfg, "DeleteAssistantWebhook", request, auth)


def get_assistant_tool_log(
    client_cfg: ConnectionConfig,
    request: GetAssistantToolLogRequest,
    auth: AuthMetadata = None,
) -> GetAssistantToolLogResponse:
    return _call_assistant_client(client_cfg, "GetAssistantToolLog", request, auth)


def get_all_assistant_tool_log(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantToolLogRequest,
    auth: AuthMetadata = None,
) -> GetAllAssistantToolLogResponse:
    return _call_assistant_client(client_cfg, "GetAllAssistantToolLog", request, auth)


def get_assistant_analysis(
    client_cfg: ConnectionConfig,
    request: GetAssistantAnalysisRequest,
    auth: AuthMetadata = None,
) -> GetAssistantAnalysisResponse:
    return _call_assistant_client(client_cfg, "GetAssistantAnalysis", request, auth)


def create_assistant_analysis(
    client_cfg: ConnectionConfig,
    request: CreateAssistantAnalysisRequest,
    auth: AuthMetadata = None,
) -> GetAssistantAnalysisResponse:
    return _call_assistant_client(client_cfg, "CreateAssistantAnalysis", request, auth)


def update_assistant_analysis(
    client_cfg: ConnectionConfig,
    request: UpdateAssistantAnalysisRequest,
    auth: AuthMetadata = None,
) -> GetAssistantAnalysisResponse:
    return _call_assistant_client(client_cfg, "UpdateAssistantAnalysis", request, auth)


def delete_assistant_analysis(
    client_cfg: ConnectionConfig,
    request: DeleteAssistantAnalysisRequest,
    auth: AuthMetadata = None,
) -> GetAssistantAnalysisResponse:
    return _call_assistant_client(client_cfg, "DeleteAssistantAnalysis", request, auth)


def get_all_assistant_analysis(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantAnalysisRequest,
    auth: AuthMetadata = None,
) -> GetAllAssistantAnalysisResponse:
    return _call_assistant_client(client_cfg, "GetAllAssistantAnalysis", request, auth)


def create_assistant_tool(
    client_cfg: ConnectionConfig,
    request: CreateAssistantToolRequest,
    auth: AuthMetadata = None,
) -> GetAssistantToolResponse:
    return _call_assistant_client(client_cfg, "CreateAssistantTool", request, auth)


def get_assistant_tool(
    client_cfg: ConnectionConfig,
    request: GetAssistantToolRequest,
    auth: AuthMetadata = None,
) -> GetAssistantToolResponse:
    return _call_assistant_client(client_cfg, "GetAssistantTool", request, auth)


def get_all_assistant_tool(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantToolRequest,
    auth: AuthMetadata = None,
) -> GetAllAssistantToolResponse:
    return _call_assistant_client(client_cfg, "GetAllAssistantTool", request, auth)


def delete_assistant_tool(
    client_cfg: ConnectionConfig,
    request: DeleteAssistantToolRequest,
    auth: AuthMetadata = None,
) -> GetAssistantToolResponse:
    return _call_assistant_client(client_cfg, "DeleteAssistantTool", request, auth)


def update_assistant_tool(
    client_cfg: ConnectionConfig,
    request: UpdateAssistantToolRequest,
    auth: AuthMetadata = None,
) -> GetAssistantToolResponse:
    return _call_assistant_client(client_cfg, "UpdateAssistantTool", request, auth)


def create_assistant_knowledge(
    client_cfg: ConnectionConfig,
    request: CreateAssistantKnowledgeRequest,
    auth: AuthMetadata = None,
) -> GetAssistantKnowledgeResponse:
    return _call_assistant_client(client_cfg, "CreateAssistantKnowledge", request, auth)


def get_assistant_knowledge(
    client_cfg: ConnectionConfig,
    request: GetAssistantKnowledgeRequest,
    auth: AuthMetadata = None,
) -> GetAssistantKnowledgeResponse:
    return _call_assistant_client(client_cfg, "GetAssistantKnowledge", request, auth)


def get_all_assistant_knowledge(
    client_cfg: ConnectionConfig,
    request: GetAllAssistantKnowledgeRequest,
    auth: AuthMetadata = None,
) -> GetAllAssistantKnowledgeResponse:
    return _call_assistant_client(client_cfg, "GetAllAssistantKnowledge", request, auth)


def delete_assistant_knowledge(
    client_cfg: ConnectionConfig,
    request: DeleteAssistantKnowledgeRequest,
    auth: AuthMetadata = None,
) -> GetAssistantKnowledgeResponse:
    return _call_assistant_client(client_cfg, "DeleteAssistantKnowledge", request, auth)


def update_assistant_knowledge(
    client_cfg: ConnectionConfig,
    request: UpdateAssistantKnowledgeRequest,
    auth: AuthMetadata = None,
) -> GetAssistantKnowledgeResponse:
    return _call_assistant_client(client_cfg, "UpdateAssistantKnowledge", request, auth)


__all__ = [
    "get_assistant",
    "get_all_assistant",
    "create_assistant",
    "delete_assistant",
    "get_all_assistant_provider",
    "create_assistant_provider",
    "create_assistant_tag",
    "update_assistant_version",
    "update_assistant_detail",
    "get_all_assistant_message",
    "get_all_conversation_message",
    "get_all_message",
    "get_all_assistant_telemetry",
    "get_assistant_telemetry_provider",
    "get_all_assistant_telemetry_provider",
    "create_assistant_telemetry_provider",
    "update_assistant_telemetry_provider",
    "delete_assistant_telemetry_provider",
    "create_assistant_authentication",
    "get_assistant_authentication",
    "disable_assistant_authentication",
    "get_assistant_conversation",
    "get_all_assistant_conversation",
    "get_assistant_http_log",
    "get_all_assistant_http_log",
    "retry_assistant_http_log",
    "get_assistant_webhook",
    "get_all_assistant_webhook",
    "create_assistant_webhook",
    "update_assistant_webhook",
    "delete_assistant_webhook",
    "get_assistant_tool_log",
    "get_all_assistant_tool_log",
    "get_assistant_analysis",
    "create_assistant_analysis",
    "update_assistant_analysis",
    "delete_assistant_analysis",
    "get_all_assistant_analysis",
    "create_assistant_tool",
    "get_assistant_tool",
    "get_all_assistant_tool",
    "delete_assistant_tool",
    "update_assistant_tool",
    "create_assistant_knowledge",
    "get_assistant_knowledge",
    "get_all_assistant_knowledge",
    "delete_assistant_knowledge",
    "update_assistant_knowledge",
]
