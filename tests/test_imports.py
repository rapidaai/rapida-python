import pytest
from rapida import *

def test_import_rapida():
    # Try importing key symbols that should be available
    from rapida import AgentKitStub, AgentKit, AgentKitServicer, add_AgentKitServicer_to_server
    # Add more imports as needed for your public API

def test_import_everything_from_rapida():
    # If this test runs, all public exports are importable
    assert True
