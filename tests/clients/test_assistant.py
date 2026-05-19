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

"""Tests for assistant client helper functions."""

import importlib.util
import os
import sys
from unittest.mock import MagicMock, Mock

import pytest


for module_name in (
    "rapida.clients.protos.assistant_analysis_pb2",
    "rapida.clients.protos.assistant_api_pb2",
    "rapida.clients.protos.assistant_knowledge_pb2",
    "rapida.clients.protos.assistant_provider_pb2",
    "rapida.clients.protos.assistant_tool_pb2",
    "rapida.clients.protos.assistant_webhook_pb2",
    "rapida.clients.protos.common_pb2",
    "rapida.connections",
):
    sys.modules[module_name] = MagicMock()


module_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "rapida",
    "clients",
    "assistant.py",
)
spec = importlib.util.spec_from_file_location("assistant", module_path)
assistant_module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(assistant_module)


FUNCTION_CASES = [
    ("get_assistant", "GetAssistant"),
    ("get_all_assistant", "GetAllAssistant"),
    ("create_assistant", "CreateAssistant"),
    ("delete_assistant", "DeleteAssistant"),
    ("get_all_assistant_provider", "GetAllAssistantProvider"),
    ("create_assistant_provider", "CreateAssistantProvider"),
    ("create_assistant_tag", "CreateAssistantTag"),
    ("update_assistant_version", "UpdateAssistantVersion"),
    ("update_assistant_detail", "UpdateAssistantDetail"),
    ("get_all_assistant_message", "GetAllAssistantMessage"),
    ("get_all_conversation_message", "GetAllConversationMessage"),
    ("get_all_message", "GetAllMessage"),
    ("get_all_assistant_telemetry", "GetAllAssistantTelemetry"),
    ("get_assistant_telemetry_provider", "GetAssistantTelemetryProvider"),
    ("get_all_assistant_telemetry_provider", "GetAllAssistantTelemetryProvider"),
    ("create_assistant_telemetry_provider", "CreateAssistantTelemetryProvider"),
    ("update_assistant_telemetry_provider", "UpdateAssistantTelemetryProvider"),
    ("delete_assistant_telemetry_provider", "DeleteAssistantTelemetryProvider"),
    ("create_assistant_authentication", "CreateAssistantAuthentication"),
    ("get_assistant_authentication", "GetAssistantAuthentication"),
    ("disable_assistant_authentication", "DisableAssistantAuthentication"),
    ("get_assistant_conversation", "GetAssistantConversation"),
    ("get_all_assistant_conversation", "GetAllAssistantConversation"),
    ("get_assistant_http_log", "GetAssistantHTTPLog"),
    ("get_all_assistant_http_log", "GetAllAssistantHTTPLog"),
    ("retry_assistant_http_log", "RetryAssistantHTTPLog"),
    ("get_assistant_webhook", "GetAssistantWebhook"),
    ("get_all_assistant_webhook", "GetAllAssistantWebhook"),
    ("create_assistant_webhook", "CreateAssistantWebhook"),
    ("update_assistant_webhook", "UpdateAssistantWebhook"),
    ("delete_assistant_webhook", "DeleteAssistantWebhook"),
    ("get_assistant_tool_log", "GetAssistantToolLog"),
    ("get_all_assistant_tool_log", "GetAllAssistantToolLog"),
    ("get_assistant_analysis", "GetAssistantAnalysis"),
    ("create_assistant_analysis", "CreateAssistantAnalysis"),
    ("update_assistant_analysis", "UpdateAssistantAnalysis"),
    ("delete_assistant_analysis", "DeleteAssistantAnalysis"),
    ("get_all_assistant_analysis", "GetAllAssistantAnalysis"),
    ("create_assistant_tool", "CreateAssistantTool"),
    ("get_assistant_tool", "GetAssistantTool"),
    ("get_all_assistant_tool", "GetAllAssistantTool"),
    ("delete_assistant_tool", "DeleteAssistantTool"),
    ("update_assistant_tool", "UpdateAssistantTool"),
    ("create_assistant_knowledge", "CreateAssistantKnowledge"),
    ("get_assistant_knowledge", "GetAssistantKnowledge"),
    ("get_all_assistant_knowledge", "GetAllAssistantKnowledge"),
    ("delete_assistant_knowledge", "DeleteAssistantKnowledge"),
    ("update_assistant_knowledge", "UpdateAssistantKnowledge"),
]


@pytest.fixture
def mock_connection_config():
    """Create a mock ConnectionConfig."""
    config = Mock()
    config.auth = [("x-api-key", "test-key")]
    config.assistant_client = Mock()
    return config


@pytest.fixture
def mock_auth():
    """Create mock auth metadata."""
    return [("authorization", "Bearer test-token")]


@pytest.mark.parametrize("function_name, client_method", FUNCTION_CASES)
def test_helper_uses_default_auth(function_name, client_method, mock_connection_config):
    request = Mock()
    expected_response = Mock()
    getattr(mock_connection_config.assistant_client, client_method).return_value = (
        expected_response
    )

    result = getattr(assistant_module, function_name)(mock_connection_config, request)

    getattr(mock_connection_config.assistant_client, client_method).assert_called_once_with(
        request,
        metadata=mock_connection_config.auth,
    )
    assert result == expected_response


@pytest.mark.parametrize("function_name, client_method", FUNCTION_CASES)
def test_helper_uses_custom_auth(
    function_name,
    client_method,
    mock_connection_config,
    mock_auth,
):
    request = Mock()
    expected_response = Mock()
    getattr(mock_connection_config.assistant_client, client_method).return_value = (
        expected_response
    )

    result = getattr(
        assistant_module,
        function_name,
    )(mock_connection_config, request, auth=mock_auth)

    getattr(mock_connection_config.assistant_client, client_method).assert_called_once_with(
        request,
        metadata=mock_auth,
    )
    assert result == expected_response


def test_http_log_helpers_replace_removed_webhook_log_helpers():
    assert hasattr(assistant_module, "get_assistant_http_log")
    assert hasattr(assistant_module, "get_all_assistant_http_log")
    assert hasattr(assistant_module, "retry_assistant_http_log")
    assert not hasattr(assistant_module, "get_assistant_webhook_log")
    assert not hasattr(assistant_module, "get_all_assistant_webhook_log")
