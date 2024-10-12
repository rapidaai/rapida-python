from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WEB_PLUGIN: _ClassVar[Source]
    RAPIDA_APP: _ClassVar[Source]
    PYTHON_SDK: _ClassVar[Source]
    NODE_SDK: _ClassVar[Source]
    GO_SDK: _ClassVar[Source]
    TYPESCRIPT_SDK: _ClassVar[Source]
    JAVA_SDK: _ClassVar[Source]
    PHP_SDK: _ClassVar[Source]
    RUST_SDK: _ClassVar[Source]
WEB_PLUGIN: Source
RAPIDA_APP: Source
PYTHON_SDK: Source
NODE_SDK: Source
GO_SDK: Source
TYPESCRIPT_SDK: Source
JAVA_SDK: Source
PHP_SDK: Source
RUST_SDK: Source

class Criteria(_message.Message):
    __slots__ = ("key", "value", "logic")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LOGIC_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    logic: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., logic: _Optional[str] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("errorCode", "errorMessage", "humanMessage")
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    HUMANMESSAGE_FIELD_NUMBER: _ClassVar[int]
    errorCode: int
    errorMessage: str
    humanMessage: str
    def __init__(self, errorCode: _Optional[int] = ..., errorMessage: _Optional[str] = ..., humanMessage: _Optional[str] = ...) -> None: ...

class Paginate(_message.Message):
    __slots__ = ("page", "pageSize")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGESIZE_FIELD_NUMBER: _ClassVar[int]
    page: int
    pageSize: int
    def __init__(self, page: _Optional[int] = ..., pageSize: _Optional[int] = ...) -> None: ...

class Paginated(_message.Message):
    __slots__ = ("currentPage", "totalItem")
    CURRENTPAGE_FIELD_NUMBER: _ClassVar[int]
    TOTALITEM_FIELD_NUMBER: _ClassVar[int]
    currentPage: int
    totalItem: int
    def __init__(self, currentPage: _Optional[int] = ..., totalItem: _Optional[int] = ...) -> None: ...

class Ordering(_message.Message):
    __slots__ = ("column", "order")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    column: str
    order: str
    def __init__(self, column: _Optional[str] = ..., order: _Optional[str] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("id", "name", "email", "role", "createdDate", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    email: str
    role: str
    createdDate: _timestamp_pb2.Timestamp
    status: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., role: _Optional[str] = ..., createdDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[str] = ...) -> None: ...

class BaseResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.ScalarMap[str, str]
    error: Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Mapping[str, str]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ("id", "key", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: int
    key: str
    value: str
    def __init__(self, id: _Optional[int] = ..., key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Variable(_message.Message):
    __slots__ = ("id", "name", "type", "defaultValue", "required", "label")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULTVALUE_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    type: str
    defaultValue: str
    required: bool
    label: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., defaultValue: _Optional[str] = ..., required: bool = ..., label: _Optional[str] = ..., **kwargs) -> None: ...

class ProviderModelParameter(_message.Message):
    __slots__ = ("id", "providerModelVariableId", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDERMODELVARIABLEID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: int
    providerModelVariableId: int
    value: str
    def __init__(self, id: _Optional[int] = ..., providerModelVariableId: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...

class Provider(_message.Message):
    __slots__ = ("id", "name", "description", "humanName", "image", "website", "status", "connectConfiguration")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HUMANNAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTCONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    humanName: str
    image: str
    website: str
    status: str
    connectConfiguration: _containers.RepeatedCompositeFieldContainer[Variable]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., humanName: _Optional[str] = ..., image: _Optional[str] = ..., website: _Optional[str] = ..., status: _Optional[str] = ..., connectConfiguration: _Optional[_Iterable[_Union[Variable, _Mapping]]] = ...) -> None: ...

class ProviderModelVariable(_message.Message):
    __slots__ = ("id", "providerModelId", "key", "name", "description", "defaultValue", "type", "place", "metadatas")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDERMODELID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEFAULTVALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PLACE_FIELD_NUMBER: _ClassVar[int]
    METADATAS_FIELD_NUMBER: _ClassVar[int]
    id: int
    providerModelId: int
    key: str
    name: str
    description: str
    defaultValue: str
    type: str
    place: str
    metadatas: _containers.RepeatedCompositeFieldContainer[Metadata]
    def __init__(self, id: _Optional[int] = ..., providerModelId: _Optional[int] = ..., key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., defaultValue: _Optional[str] = ..., type: _Optional[str] = ..., place: _Optional[str] = ..., metadatas: _Optional[_Iterable[_Union[Metadata, _Mapping]]] = ...) -> None: ...

class ProviderModel(_message.Message):
    __slots__ = ("id", "name", "description", "humanName", "category", "status", "owner", "provider", "parameters", "metadatas", "providerId", "endpoint")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HUMANNAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    METADATAS_FIELD_NUMBER: _ClassVar[int]
    PROVIDERID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    humanName: str
    category: str
    status: str
    owner: str
    provider: Provider
    parameters: _containers.RepeatedCompositeFieldContainer[ProviderModelVariable]
    metadatas: _containers.RepeatedCompositeFieldContainer[Metadata]
    providerId: int
    endpoint: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., humanName: _Optional[str] = ..., category: _Optional[str] = ..., status: _Optional[str] = ..., owner: _Optional[str] = ..., provider: _Optional[_Union[Provider, _Mapping]] = ..., parameters: _Optional[_Iterable[_Union[ProviderModelVariable, _Mapping]]] = ..., metadatas: _Optional[_Iterable[_Union[Metadata, _Mapping]]] = ..., providerId: _Optional[int] = ..., endpoint: _Optional[str] = ...) -> None: ...

class Tag(_message.Message):
    __slots__ = ("id", "tag")
    ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    id: int
    tag: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[int] = ..., tag: _Optional[_Iterable[str]] = ...) -> None: ...

class Organization(_message.Message):
    __slots__ = ("id", "name", "description", "industry", "contact", "size")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    industry: str
    contact: str
    size: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., industry: _Optional[str] = ..., contact: _Optional[str] = ..., size: _Optional[str] = ...) -> None: ...

class Metric(_message.Message):
    __slots__ = ("name", "value", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    description: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class Content(_message.Message):
    __slots__ = ("name", "contentType", "contentFormat", "content", "meta")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENTTYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENTFORMAT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    name: str
    contentType: str
    contentFormat: str
    content: bytes
    meta: _struct_pb2.Struct
    def __init__(self, name: _Optional[str] = ..., contentType: _Optional[str] = ..., contentFormat: _Optional[str] = ..., content: _Optional[bytes] = ..., meta: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("role", "contents", "toolCalls")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    TOOLCALLS_FIELD_NUMBER: _ClassVar[int]
    role: str
    contents: _containers.RepeatedCompositeFieldContainer[Content]
    toolCalls: _containers.RepeatedCompositeFieldContainer[ToolCall]
    def __init__(self, role: _Optional[str] = ..., contents: _Optional[_Iterable[_Union[Content, _Mapping]]] = ..., toolCalls: _Optional[_Iterable[_Union[ToolCall, _Mapping]]] = ...) -> None: ...

class ToolCall(_message.Message):
    __slots__ = ("id", "type", "function")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    function: FunctionCall
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., function: _Optional[_Union[FunctionCall, _Mapping]] = ...) -> None: ...

class FunctionCall(_message.Message):
    __slots__ = ("name", "arguments", "args")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    arguments: str
    args: _struct_pb2.Struct
    def __init__(self, name: _Optional[str] = ..., arguments: _Optional[str] = ..., args: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class Knowledge(_message.Message):
    __slots__ = ("id", "name", "description", "visibility", "language", "embeddingProviderModelId", "embeddingProviderModel", "status", "createdBy", "createdUser", "updatedBy", "updatedUser", "createdDate", "updatedDate", "organizationId", "projectId", "organization", "knowledgeTag", "documentCount", "tokenCount", "wordCount", "embeddingProviderId")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    EMBEDDINGPROVIDERMODELID_FIELD_NUMBER: _ClassVar[int]
    EMBEDDINGPROVIDERMODEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATEDBY_FIELD_NUMBER: _ClassVar[int]
    CREATEDUSER_FIELD_NUMBER: _ClassVar[int]
    UPDATEDBY_FIELD_NUMBER: _ClassVar[int]
    UPDATEDUSER_FIELD_NUMBER: _ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGETAG_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTCOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKENCOUNT_FIELD_NUMBER: _ClassVar[int]
    WORDCOUNT_FIELD_NUMBER: _ClassVar[int]
    EMBEDDINGPROVIDERID_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    visibility: str
    language: str
    embeddingProviderModelId: int
    embeddingProviderModel: ProviderModel
    status: str
    createdBy: int
    createdUser: User
    updatedBy: int
    updatedUser: User
    createdDate: _timestamp_pb2.Timestamp
    updatedDate: _timestamp_pb2.Timestamp
    organizationId: int
    projectId: int
    organization: Organization
    knowledgeTag: Tag
    documentCount: int
    tokenCount: int
    wordCount: int
    embeddingProviderId: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., visibility: _Optional[str] = ..., language: _Optional[str] = ..., embeddingProviderModelId: _Optional[int] = ..., embeddingProviderModel: _Optional[_Union[ProviderModel, _Mapping]] = ..., status: _Optional[str] = ..., createdBy: _Optional[int] = ..., createdUser: _Optional[_Union[User, _Mapping]] = ..., updatedBy: _Optional[int] = ..., updatedUser: _Optional[_Union[User, _Mapping]] = ..., createdDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updatedDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., organizationId: _Optional[int] = ..., projectId: _Optional[int] = ..., organization: _Optional[_Union[Organization, _Mapping]] = ..., knowledgeTag: _Optional[_Union[Tag, _Mapping]] = ..., documentCount: _Optional[int] = ..., tokenCount: _Optional[int] = ..., wordCount: _Optional[int] = ..., embeddingProviderId: _Optional[int] = ...) -> None: ...

class AgentPromptTemplate(_message.Message):
    __slots__ = ("type", "prompt", "promptVariables")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    PROMPTVARIABLES_FIELD_NUMBER: _ClassVar[int]
    type: str
    prompt: str
    promptVariables: _containers.RepeatedCompositeFieldContainer[Variable]
    def __init__(self, type: _Optional[str] = ..., prompt: _Optional[str] = ..., promptVariables: _Optional[_Iterable[_Union[Variable, _Mapping]]] = ...) -> None: ...

class TextPrompt(_message.Message):
    __slots__ = ("role", "content")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    role: str
    content: str
    def __init__(self, role: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class FilePrompt(_message.Message):
    __slots__ = ("name", "accepts")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCEPTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    accepts: str
    def __init__(self, name: _Optional[str] = ..., accepts: _Optional[str] = ...) -> None: ...

class TextChatCompletePrompt(_message.Message):
    __slots__ = ("prompt", "promptVariables")
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    PROMPTVARIABLES_FIELD_NUMBER: _ClassVar[int]
    prompt: _containers.RepeatedCompositeFieldContainer[TextPrompt]
    promptVariables: _containers.RepeatedCompositeFieldContainer[Variable]
    def __init__(self, prompt: _Optional[_Iterable[_Union[TextPrompt, _Mapping]]] = ..., promptVariables: _Optional[_Iterable[_Union[Variable, _Mapping]]] = ...) -> None: ...

class TextCompletePrompt(_message.Message):
    __slots__ = ("prompt", "promptVariables")
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    PROMPTVARIABLES_FIELD_NUMBER: _ClassVar[int]
    prompt: TextPrompt
    promptVariables: _containers.RepeatedCompositeFieldContainer[Variable]
    def __init__(self, prompt: _Optional[_Union[TextPrompt, _Mapping]] = ..., promptVariables: _Optional[_Iterable[_Union[Variable, _Mapping]]] = ...) -> None: ...

class TextToImagePrompt(_message.Message):
    __slots__ = ("prompt", "promptVariables")
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    PROMPTVARIABLES_FIELD_NUMBER: _ClassVar[int]
    prompt: TextPrompt
    promptVariables: _containers.RepeatedCompositeFieldContainer[Variable]
    def __init__(self, prompt: _Optional[_Union[TextPrompt, _Mapping]] = ..., promptVariables: _Optional[_Iterable[_Union[Variable, _Mapping]]] = ...) -> None: ...

class TextToSpeechPrompt(_message.Message):
    __slots__ = ("prompt", "promptVariables")
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    PROMPTVARIABLES_FIELD_NUMBER: _ClassVar[int]
    prompt: TextPrompt
    promptVariables: _containers.RepeatedCompositeFieldContainer[Variable]
    def __init__(self, prompt: _Optional[_Union[TextPrompt, _Mapping]] = ..., promptVariables: _Optional[_Iterable[_Union[Variable, _Mapping]]] = ...) -> None: ...

class SpeechToTextPrompt(_message.Message):
    __slots__ = ("prompt", "promptVariables")
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    PROMPTVARIABLES_FIELD_NUMBER: _ClassVar[int]
    prompt: FilePrompt
    promptVariables: _containers.RepeatedCompositeFieldContainer[Variable]
    def __init__(self, prompt: _Optional[_Union[FilePrompt, _Mapping]] = ..., promptVariables: _Optional[_Iterable[_Union[Variable, _Mapping]]] = ...) -> None: ...

class AssistantMessageStage(_message.Message):
    __slots__ = ("stage", "additionalData", "timetaken", "lifecycleId", "startTimestamp", "endTimestamp")
    class AdditionalDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _any_pb2.Any
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    STAGE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONALDATA_FIELD_NUMBER: _ClassVar[int]
    TIMETAKEN_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLEID_FIELD_NUMBER: _ClassVar[int]
    STARTTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ENDTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    stage: str
    additionalData: _containers.MessageMap[str, _any_pb2.Any]
    timetaken: int
    lifecycleId: str
    startTimestamp: _timestamp_pb2.Timestamp
    endTimestamp: _timestamp_pb2.Timestamp
    def __init__(self, stage: _Optional[str] = ..., additionalData: _Optional[_Mapping[str, _any_pb2.Any]] = ..., timetaken: _Optional[int] = ..., lifecycleId: _Optional[str] = ..., startTimestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endTimestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AssistantConversationMessage(_message.Message):
    __slots__ = ("id", "assistantConversationId", "requestRole", "request", "responseRole", "response", "externalAuditId", "source", "metrics", "status", "createdBy", "updatedBy", "suggestedQuestions", "stages", "liked", "disliked", "createdDate", "updatedDate", "assistantId", "assistantProviderModelId")
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTCONVERSATIONID_FIELD_NUMBER: _ClassVar[int]
    REQUESTROLE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESPONSEROLE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    EXTERNALAUDITID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATEDBY_FIELD_NUMBER: _ClassVar[int]
    UPDATEDBY_FIELD_NUMBER: _ClassVar[int]
    SUGGESTEDQUESTIONS_FIELD_NUMBER: _ClassVar[int]
    STAGES_FIELD_NUMBER: _ClassVar[int]
    LIKED_FIELD_NUMBER: _ClassVar[int]
    DISLIKED_FIELD_NUMBER: _ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTPROVIDERMODELID_FIELD_NUMBER: _ClassVar[int]
    id: int
    assistantConversationId: int
    requestRole: str
    request: Message
    responseRole: str
    response: Message
    externalAuditId: int
    source: str
    metrics: _containers.RepeatedCompositeFieldContainer[Metric]
    status: str
    createdBy: int
    updatedBy: int
    suggestedQuestions: _containers.RepeatedScalarFieldContainer[str]
    stages: _containers.RepeatedCompositeFieldContainer[AssistantMessageStage]
    liked: bool
    disliked: bool
    createdDate: _timestamp_pb2.Timestamp
    updatedDate: _timestamp_pb2.Timestamp
    assistantId: int
    assistantProviderModelId: int
    def __init__(self, id: _Optional[int] = ..., assistantConversationId: _Optional[int] = ..., requestRole: _Optional[str] = ..., request: _Optional[_Union[Message, _Mapping]] = ..., responseRole: _Optional[str] = ..., response: _Optional[_Union[Message, _Mapping]] = ..., externalAuditId: _Optional[int] = ..., source: _Optional[str] = ..., metrics: _Optional[_Iterable[_Union[Metric, _Mapping]]] = ..., status: _Optional[str] = ..., createdBy: _Optional[int] = ..., updatedBy: _Optional[int] = ..., suggestedQuestions: _Optional[_Iterable[str]] = ..., stages: _Optional[_Iterable[_Union[AssistantMessageStage, _Mapping]]] = ..., liked: bool = ..., disliked: bool = ..., createdDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updatedDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., assistantId: _Optional[int] = ..., assistantProviderModelId: _Optional[int] = ...) -> None: ...
