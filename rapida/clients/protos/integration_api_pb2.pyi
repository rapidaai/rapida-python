import rapida.clients.protos.common_pb2 as _common_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Credential(_message.Message):
    __slots__ = ("id", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: int
    value: _struct_pb2.Struct
    def __init__(self, id: _Optional[int] = ..., value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ToolDefinition(_message.Message):
    __slots__ = ("type", "functionDefinition")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONDEFINITION_FIELD_NUMBER: _ClassVar[int]
    type: str
    functionDefinition: FunctionDefinition
    def __init__(self, type: _Optional[str] = ..., functionDefinition: _Optional[_Union[FunctionDefinition, _Mapping]] = ...) -> None: ...

class FunctionDefinition(_message.Message):
    __slots__ = ("name", "description", "parameters")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    parameters: FunctionParameter
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., parameters: _Optional[_Union[FunctionParameter, _Mapping]] = ...) -> None: ...

class FunctionParameter(_message.Message):
    __slots__ = ("required", "type", "properties")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FunctionParameterProperty
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[FunctionParameterProperty, _Mapping]] = ...) -> None: ...
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    required: _containers.RepeatedScalarFieldContainer[str]
    type: str
    properties: _containers.MessageMap[str, FunctionParameterProperty]
    def __init__(self, required: _Optional[_Iterable[str]] = ..., type: _Optional[str] = ..., properties: _Optional[_Mapping[str, FunctionParameterProperty]] = ...) -> None: ...

class FunctionParameterProperty(_message.Message):
    __slots__ = ("type", "description", "enum", "items")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    type: str
    description: str
    enum: _containers.RepeatedScalarFieldContainer[str]
    items: FunctionParameter
    def __init__(self, type: _Optional[str] = ..., description: _Optional[str] = ..., enum: _Optional[_Iterable[str]] = ..., items: _Optional[_Union[FunctionParameter, _Mapping]] = ...) -> None: ...

class Embedding(_message.Message):
    __slots__ = ("index", "embedding", "base64")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_FIELD_NUMBER: _ClassVar[int]
    BASE64_FIELD_NUMBER: _ClassVar[int]
    index: int
    embedding: _containers.RepeatedScalarFieldContainer[float]
    base64: str
    def __init__(self, index: _Optional[int] = ..., embedding: _Optional[_Iterable[float]] = ..., base64: _Optional[str] = ...) -> None: ...

class EmbeddingRequest(_message.Message):
    __slots__ = ("credential", "content", "modelParameters", "additionalData")
    class ContentEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class ModelParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _any_pb2.Any
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    class AdditionalDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MODELPARAMETERS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONALDATA_FIELD_NUMBER: _ClassVar[int]
    credential: Credential
    content: _containers.ScalarMap[int, str]
    modelParameters: _containers.MessageMap[str, _any_pb2.Any]
    additionalData: _containers.ScalarMap[str, str]
    def __init__(self, credential: _Optional[_Union[Credential, _Mapping]] = ..., content: _Optional[_Mapping[int, str]] = ..., modelParameters: _Optional[_Mapping[str, _any_pb2.Any]] = ..., additionalData: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EmbeddingResponse(_message.Message):
    __slots__ = ("code", "success", "requestId", "data", "error", "metrics")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    requestId: int
    data: _containers.RepeatedCompositeFieldContainer[Embedding]
    error: _common_pb2.Error
    metrics: _containers.RepeatedCompositeFieldContainer[_common_pb2.Metric]
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., requestId: _Optional[int] = ..., data: _Optional[_Iterable[_Union[Embedding, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., metrics: _Optional[_Iterable[_Union[_common_pb2.Metric, _Mapping]]] = ...) -> None: ...

class Reranking(_message.Message):
    __slots__ = ("index", "content", "RelevanceScore")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    RELEVANCESCORE_FIELD_NUMBER: _ClassVar[int]
    index: int
    content: _common_pb2.Content
    RelevanceScore: float
    def __init__(self, index: _Optional[int] = ..., content: _Optional[_Union[_common_pb2.Content, _Mapping]] = ..., RelevanceScore: _Optional[float] = ...) -> None: ...

class RerankingRequest(_message.Message):
    __slots__ = ("credential", "query", "content", "modelParameters", "additionalData")
    class ContentEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _common_pb2.Content
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_common_pb2.Content, _Mapping]] = ...) -> None: ...
    class ModelParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _any_pb2.Any
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    class AdditionalDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MODELPARAMETERS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONALDATA_FIELD_NUMBER: _ClassVar[int]
    credential: Credential
    query: str
    content: _containers.MessageMap[int, _common_pb2.Content]
    modelParameters: _containers.MessageMap[str, _any_pb2.Any]
    additionalData: _containers.ScalarMap[str, str]
    def __init__(self, credential: _Optional[_Union[Credential, _Mapping]] = ..., query: _Optional[str] = ..., content: _Optional[_Mapping[int, _common_pb2.Content]] = ..., modelParameters: _Optional[_Mapping[str, _any_pb2.Any]] = ..., additionalData: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RerankingResponse(_message.Message):
    __slots__ = ("code", "success", "requestId", "data", "error", "metrics")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    requestId: int
    data: _containers.RepeatedCompositeFieldContainer[Reranking]
    error: _common_pb2.Error
    metrics: _containers.RepeatedCompositeFieldContainer[_common_pb2.Metric]
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., requestId: _Optional[int] = ..., data: _Optional[_Iterable[_Union[Reranking, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., metrics: _Optional[_Iterable[_Union[_common_pb2.Metric, _Mapping]]] = ...) -> None: ...

class ChatResponse(_message.Message):
    __slots__ = ("code", "success", "requestId", "data", "error", "metrics", "finishReason")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    FINISHREASON_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    requestId: int
    data: _common_pb2.Message
    error: _common_pb2.Error
    metrics: _containers.RepeatedCompositeFieldContainer[_common_pb2.Metric]
    finishReason: str
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., requestId: _Optional[int] = ..., data: _Optional[_Union[_common_pb2.Message, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., metrics: _Optional[_Iterable[_Union[_common_pb2.Metric, _Mapping]]] = ..., finishReason: _Optional[str] = ...) -> None: ...

class ChatRequest(_message.Message):
    __slots__ = ("credential", "conversations", "additionalData", "modelParameters", "toolDefinitions")
    class AdditionalDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ModelParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _any_pb2.Any
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONALDATA_FIELD_NUMBER: _ClassVar[int]
    MODELPARAMETERS_FIELD_NUMBER: _ClassVar[int]
    TOOLDEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    credential: Credential
    conversations: _containers.RepeatedCompositeFieldContainer[_common_pb2.Message]
    additionalData: _containers.ScalarMap[str, str]
    modelParameters: _containers.MessageMap[str, _any_pb2.Any]
    toolDefinitions: _containers.RepeatedCompositeFieldContainer[ToolDefinition]
    def __init__(self, credential: _Optional[_Union[Credential, _Mapping]] = ..., conversations: _Optional[_Iterable[_Union[_common_pb2.Message, _Mapping]]] = ..., additionalData: _Optional[_Mapping[str, str]] = ..., modelParameters: _Optional[_Mapping[str, _any_pb2.Any]] = ..., toolDefinitions: _Optional[_Iterable[_Union[ToolDefinition, _Mapping]]] = ...) -> None: ...

class VerifyCredentialRequest(_message.Message):
    __slots__ = ("credential",)
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    credential: Credential
    def __init__(self, credential: _Optional[_Union[Credential, _Mapping]] = ...) -> None: ...

class VerifyCredentialResponse(_message.Message):
    __slots__ = ("code", "success", "requestId", "response", "errorMessage")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    requestId: int
    response: str
    errorMessage: str
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., requestId: _Optional[int] = ..., response: _Optional[str] = ..., errorMessage: _Optional[str] = ...) -> None: ...

class Moderation(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class GetModerationRequest(_message.Message):
    __slots__ = ("credential", "model", "version", "content", "additionalData", "modelParameters")
    class AdditionalDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ModelParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _any_pb2.Any
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONALDATA_FIELD_NUMBER: _ClassVar[int]
    MODELPARAMETERS_FIELD_NUMBER: _ClassVar[int]
    credential: Credential
    model: str
    version: str
    content: _common_pb2.Content
    additionalData: _containers.ScalarMap[str, str]
    modelParameters: _containers.MessageMap[str, _any_pb2.Any]
    def __init__(self, credential: _Optional[_Union[Credential, _Mapping]] = ..., model: _Optional[str] = ..., version: _Optional[str] = ..., content: _Optional[_Union[_common_pb2.Content, _Mapping]] = ..., additionalData: _Optional[_Mapping[str, str]] = ..., modelParameters: _Optional[_Mapping[str, _any_pb2.Any]] = ...) -> None: ...

class GetModerationResponse(_message.Message):
    __slots__ = ("code", "success", "requestId", "data", "error", "metrics")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    requestId: int
    data: _containers.RepeatedCompositeFieldContainer[Moderation]
    error: _common_pb2.Error
    metrics: _containers.RepeatedCompositeFieldContainer[_common_pb2.Metric]
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., requestId: _Optional[int] = ..., data: _Optional[_Iterable[_Union[Moderation, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., metrics: _Optional[_Iterable[_Union[_common_pb2.Metric, _Mapping]]] = ...) -> None: ...
