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

"""Tests for call client helper functions."""

import importlib.util
import os
import sys
from unittest.mock import MagicMock, Mock

import pytest


sys.modules["rapida.clients.protos.talk_api_pb2"] = MagicMock()
sys.modules["rapida.connections"] = MagicMock()


module_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "rapida",
    "clients",
    "call.py",
)
spec = importlib.util.spec_from_file_location("call", module_path)
call_module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(call_module)


FUNCTION_CASES = [
    ("create_message_metric", "CreateMessageMetric"),
    ("create_conversation_metric", "CreateConversationMetric"),
    ("create_phone_call", "CreatePhoneCall"),
    ("create_bulk_phone_call", "CreateBulkPhoneCall"),
]


@pytest.fixture
def mock_connection_config():
    """Create a mock ConnectionConfig."""
    config = Mock()
    config.auth = [("x-api-key", "test-key")]
    config.conversation_client = Mock()
    return config


@pytest.fixture
def mock_auth():
    """Create mock auth metadata."""
    return [("authorization", "Bearer test-token")]


@pytest.mark.parametrize("function_name, client_method", FUNCTION_CASES)
def test_helper_uses_default_auth(function_name, client_method, mock_connection_config):
    request = Mock()
    expected_response = Mock()
    getattr(mock_connection_config.conversation_client, client_method).return_value = (
        expected_response
    )

    result = getattr(call_module, function_name)(mock_connection_config, request)

    getattr(mock_connection_config.conversation_client, client_method).assert_called_once_with(
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
    getattr(mock_connection_config.conversation_client, client_method).return_value = (
        expected_response
    )

    result = getattr(call_module, function_name)(
        mock_connection_config,
        request,
        auth=mock_auth,
    )

    getattr(mock_connection_config.conversation_client, client_method).assert_called_once_with(
        request,
        metadata=mock_auth,
    )
    assert result == expected_response


@pytest.mark.parametrize("function_name, client_method", FUNCTION_CASES)
def test_helper_uses_config_auth_when_none_explicitly_passed(
    function_name,
    client_method,
    mock_connection_config,
):
    request = Mock()
    expected_response = Mock()
    getattr(mock_connection_config.conversation_client, client_method).return_value = (
        expected_response
    )

    result = getattr(call_module, function_name)(
        mock_connection_config,
        request,
        auth=None,
    )

    getattr(mock_connection_config.conversation_client, client_method).assert_called_once_with(
        request,
        metadata=mock_connection_config.auth,
    )
    assert result == expected_response
