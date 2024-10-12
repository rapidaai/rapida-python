from google.protobuf import timestamp_pb2 as _timestamp_pb2
import rapida.artifacts.protos.common_pb2 as _common_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Assistant(_message.Message):
    __slots__ = ("id", "status", "visibility", "source", "sourceIdentifier", "projectId", "organizationId", "assistantProviderModelId", "assistantProviderModel", "name", "description", "assistantTag", "language", "organization", "assistantKnowledgeConfigurations", "createdBy", "createdUser", "updatedBy", "updatedUser", "createdDate", "updatedDate", "appAppearance", "webAppearance")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCEIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTPROVIDERMODELID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTPROVIDERMODEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTTAG_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTKNOWLEDGECONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
    CREATEDBY_FIELD_NUMBER: _ClassVar[int]
    CREATEDUSER_FIELD_NUMBER: _ClassVar[int]
    UPDATEDBY_FIELD_NUMBER: _ClassVar[int]
    UPDATEDUSER_FIELD_NUMBER: _ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    APPAPPEARANCE_FIELD_NUMBER: _ClassVar[int]
    WEBAPPEARANCE_FIELD_NUMBER: _ClassVar[int]
    id: int
    status: str
    visibility: str
    source: str
    sourceIdentifier: int
    projectId: int
    organizationId: int
    assistantProviderModelId: int
    assistantProviderModel: AssistantProviderModel
    name: str
    description: str
    assistantTag: _common_pb2.Tag
    language: str
    organization: _common_pb2.Organization
    assistantKnowledgeConfigurations: _containers.RepeatedCompositeFieldContainer[AssistantKnowledgeConfiguration]
    createdBy: int
    createdUser: _common_pb2.User
    updatedBy: int
    updatedUser: _common_pb2.User
    createdDate: _timestamp_pb2.Timestamp
    updatedDate: _timestamp_pb2.Timestamp
    appAppearance: _struct_pb2.Struct
    webAppearance: _struct_pb2.Struct
    def __init__(self, id: _Optional[int] = ..., status: _Optional[str] = ..., visibility: _Optional[str] = ..., source: _Optional[str] = ..., sourceIdentifier: _Optional[int] = ..., projectId: _Optional[int] = ..., organizationId: _Optional[int] = ..., assistantProviderModelId: _Optional[int] = ..., assistantProviderModel: _Optional[_Union[AssistantProviderModel, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., assistantTag: _Optional[_Union[_common_pb2.Tag, _Mapping]] = ..., language: _Optional[str] = ..., organization: _Optional[_Union[_common_pb2.Organization, _Mapping]] = ..., assistantKnowledgeConfigurations: _Optional[_Iterable[_Union[AssistantKnowledgeConfiguration, _Mapping]]] = ..., createdBy: _Optional[int] = ..., createdUser: _Optional[_Union[_common_pb2.User, _Mapping]] = ..., updatedBy: _Optional[int] = ..., updatedUser: _Optional[_Union[_common_pb2.User, _Mapping]] = ..., createdDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updatedDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., appAppearance: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., webAppearance: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class AssistantProviderModel(_message.Message):
    __slots__ = ("id", "template", "description", "providerId", "modelModeType", "providerModelId", "providerModel", "assistantProviderModelParameters", "status", "createdBy", "createdUser", "updatedBy", "updatedUser", "createdDate", "updatedDate")
    ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROVIDERID_FIELD_NUMBER: _ClassVar[int]
    MODELMODETYPE_FIELD_NUMBER: _ClassVar[int]
    PROVIDERMODELID_FIELD_NUMBER: _ClassVar[int]
    PROVIDERMODEL_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTPROVIDERMODELPARAMETERS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATEDBY_FIELD_NUMBER: _ClassVar[int]
    CREATEDUSER_FIELD_NUMBER: _ClassVar[int]
    UPDATEDBY_FIELD_NUMBER: _ClassVar[int]
    UPDATEDUSER_FIELD_NUMBER: _ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    template: _common_pb2.AgentPromptTemplate
    description: str
    providerId: int
    modelModeType: str
    providerModelId: int
    providerModel: _common_pb2.ProviderModel
    assistantProviderModelParameters: _containers.RepeatedCompositeFieldContainer[_common_pb2.ProviderModelParameter]
    status: str
    createdBy: int
    createdUser: _common_pb2.User
    updatedBy: int
    updatedUser: _common_pb2.User
    createdDate: _timestamp_pb2.Timestamp
    updatedDate: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., template: _Optional[_Union[_common_pb2.AgentPromptTemplate, _Mapping]] = ..., description: _Optional[str] = ..., providerId: _Optional[int] = ..., modelModeType: _Optional[str] = ..., providerModelId: _Optional[int] = ..., providerModel: _Optional[_Union[_common_pb2.ProviderModel, _Mapping]] = ..., assistantProviderModelParameters: _Optional[_Iterable[_Union[_common_pb2.ProviderModelParameter, _Mapping]]] = ..., status: _Optional[str] = ..., createdBy: _Optional[int] = ..., createdUser: _Optional[_Union[_common_pb2.User, _Mapping]] = ..., updatedBy: _Optional[int] = ..., updatedUser: _Optional[_Union[_common_pb2.User, _Mapping]] = ..., createdDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updatedDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AssistantKnowledgeConfiguration(_message.Message):
    __slots__ = ("id", "knowledgeId", "rerankerEnable", "rerankerProviderModelId", "rerankerProviderModel", "topK", "scoreThreshold", "knowledge", "retrievalMethod")
    ID_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGEID_FIELD_NUMBER: _ClassVar[int]
    RERANKERENABLE_FIELD_NUMBER: _ClassVar[int]
    RERANKERPROVIDERMODELID_FIELD_NUMBER: _ClassVar[int]
    RERANKERPROVIDERMODEL_FIELD_NUMBER: _ClassVar[int]
    TOPK_FIELD_NUMBER: _ClassVar[int]
    SCORETHRESHOLD_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_FIELD_NUMBER: _ClassVar[int]
    RETRIEVALMETHOD_FIELD_NUMBER: _ClassVar[int]
    id: int
    knowledgeId: int
    rerankerEnable: bool
    rerankerProviderModelId: int
    rerankerProviderModel: _common_pb2.ProviderModel
    topK: int
    scoreThreshold: float
    knowledge: _common_pb2.Knowledge
    retrievalMethod: str
    def __init__(self, id: _Optional[int] = ..., knowledgeId: _Optional[int] = ..., rerankerEnable: bool = ..., rerankerProviderModelId: _Optional[int] = ..., rerankerProviderModel: _Optional[_Union[_common_pb2.ProviderModel, _Mapping]] = ..., topK: _Optional[int] = ..., scoreThreshold: _Optional[float] = ..., knowledge: _Optional[_Union[_common_pb2.Knowledge, _Mapping]] = ..., retrievalMethod: _Optional[str] = ...) -> None: ...

class AssistantProviderModelAttribute(_message.Message):
    __slots__ = ("description", "template", "providerId", "providerModelId", "providerModel", "assistantProviderModelParameters", "modelModeType")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    PROVIDERID_FIELD_NUMBER: _ClassVar[int]
    PROVIDERMODELID_FIELD_NUMBER: _ClassVar[int]
    PROVIDERMODEL_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTPROVIDERMODELPARAMETERS_FIELD_NUMBER: _ClassVar[int]
    MODELMODETYPE_FIELD_NUMBER: _ClassVar[int]
    description: str
    template: _common_pb2.AgentPromptTemplate
    providerId: int
    providerModelId: int
    providerModel: _common_pb2.ProviderModel
    assistantProviderModelParameters: _containers.RepeatedCompositeFieldContainer[_common_pb2.ProviderModelParameter]
    modelModeType: str
    def __init__(self, description: _Optional[str] = ..., template: _Optional[_Union[_common_pb2.AgentPromptTemplate, _Mapping]] = ..., providerId: _Optional[int] = ..., providerModelId: _Optional[int] = ..., providerModel: _Optional[_Union[_common_pb2.ProviderModel, _Mapping]] = ..., assistantProviderModelParameters: _Optional[_Iterable[_Union[_common_pb2.ProviderModelParameter, _Mapping]]] = ..., modelModeType: _Optional[str] = ...) -> None: ...

class AssistantAttribute(_message.Message):
    __slots__ = ("source", "sourceIdentifier", "name", "description", "visibility", "language")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCEIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    source: str
    sourceIdentifier: int
    name: str
    description: str
    visibility: str
    language: str
    def __init__(self, source: _Optional[str] = ..., sourceIdentifier: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., visibility: _Optional[str] = ..., language: _Optional[str] = ...) -> None: ...

class AssistantKnowledgeConfigurationAttribute(_message.Message):
    __slots__ = ("knowledgeId", "rerankerEnable", "rerankerProviderModelId", "topK", "scoreThreshold", "retrievalMethod", "active")
    KNOWLEDGEID_FIELD_NUMBER: _ClassVar[int]
    RERANKERENABLE_FIELD_NUMBER: _ClassVar[int]
    RERANKERPROVIDERMODELID_FIELD_NUMBER: _ClassVar[int]
    TOPK_FIELD_NUMBER: _ClassVar[int]
    SCORETHRESHOLD_FIELD_NUMBER: _ClassVar[int]
    RETRIEVALMETHOD_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    knowledgeId: int
    rerankerEnable: bool
    rerankerProviderModelId: int
    topK: int
    scoreThreshold: float
    retrievalMethod: str
    active: bool
    def __init__(self, knowledgeId: _Optional[int] = ..., rerankerEnable: bool = ..., rerankerProviderModelId: _Optional[int] = ..., topK: _Optional[int] = ..., scoreThreshold: _Optional[float] = ..., retrievalMethod: _Optional[str] = ..., active: bool = ...) -> None: ...

class CreateAssistantRequest(_message.Message):
    __slots__ = ("assistantProviderModelAttribute", "assistantAttribute", "tags", "assistantKnowledgeConfigurationAttributes")
    ASSISTANTPROVIDERMODELATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTKNOWLEDGECONFIGURATIONATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    assistantProviderModelAttribute: AssistantProviderModelAttribute
    assistantAttribute: AssistantAttribute
    tags: _containers.RepeatedScalarFieldContainer[str]
    assistantKnowledgeConfigurationAttributes: _containers.RepeatedCompositeFieldContainer[AssistantKnowledgeConfigurationAttribute]
    def __init__(self, assistantProviderModelAttribute: _Optional[_Union[AssistantProviderModelAttribute, _Mapping]] = ..., assistantAttribute: _Optional[_Union[AssistantAttribute, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ..., assistantKnowledgeConfigurationAttributes: _Optional[_Iterable[_Union[AssistantKnowledgeConfigurationAttribute, _Mapping]]] = ...) -> None: ...

class CreateAssistantProviderModelRequest(_message.Message):
    __slots__ = ("assistantId", "assistantProviderModelAttribute")
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTPROVIDERMODELATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    assistantId: int
    assistantProviderModelAttribute: AssistantProviderModelAttribute
    def __init__(self, assistantId: _Optional[int] = ..., assistantProviderModelAttribute: _Optional[_Union[AssistantProviderModelAttribute, _Mapping]] = ...) -> None: ...

class CreateAssistantProviderModelResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: AssistantProviderModel
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[AssistantProviderModel, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class CreateAssistantResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: Assistant
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[Assistant, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class CreateAssistantKnowledgeConfigurationRequest(_message.Message):
    __slots__ = ("assistantId", "assistantKnowledgeConfigurationAttributes")
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTKNOWLEDGECONFIGURATIONATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    assistantId: int
    assistantKnowledgeConfigurationAttributes: _containers.RepeatedCompositeFieldContainer[AssistantKnowledgeConfigurationAttribute]
    def __init__(self, assistantId: _Optional[int] = ..., assistantKnowledgeConfigurationAttributes: _Optional[_Iterable[_Union[AssistantKnowledgeConfigurationAttribute, _Mapping]]] = ...) -> None: ...

class CreateAssistantTagRequest(_message.Message):
    __slots__ = ("assistantId", "tags")
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    assistantId: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, assistantId: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class GetAssistantRequest(_message.Message):
    __slots__ = ("id", "assistantProviderModelId")
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTPROVIDERMODELID_FIELD_NUMBER: _ClassVar[int]
    id: int
    assistantProviderModelId: int
    def __init__(self, id: _Optional[int] = ..., assistantProviderModelId: _Optional[int] = ...) -> None: ...

class GetAssistantResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: Assistant
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[Assistant, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class GetAllAssistantRequest(_message.Message):
    __slots__ = ("paginate", "criterias")
    PAGINATE_FIELD_NUMBER: _ClassVar[int]
    CRITERIAS_FIELD_NUMBER: _ClassVar[int]
    paginate: _common_pb2.Paginate
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    def __init__(self, paginate: _Optional[_Union[_common_pb2.Paginate, _Mapping]] = ..., criterias: _Optional[_Iterable[_Union[_common_pb2.Criteria, _Mapping]]] = ...) -> None: ...

class GetAllAssistantResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error", "paginated")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[Assistant]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[Assistant, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., paginated: _Optional[_Union[_common_pb2.Paginated, _Mapping]] = ...) -> None: ...

class GetAllAssistantProviderModelRequest(_message.Message):
    __slots__ = ("paginate", "criterias", "assistantId")
    PAGINATE_FIELD_NUMBER: _ClassVar[int]
    CRITERIAS_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    paginate: _common_pb2.Paginate
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    assistantId: int
    def __init__(self, paginate: _Optional[_Union[_common_pb2.Paginate, _Mapping]] = ..., criterias: _Optional[_Iterable[_Union[_common_pb2.Criteria, _Mapping]]] = ..., assistantId: _Optional[int] = ...) -> None: ...

class GetAllAssistantProviderModelResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error", "paginated")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[AssistantProviderModel]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[AssistantProviderModel, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., paginated: _Optional[_Union[_common_pb2.Paginated, _Mapping]] = ...) -> None: ...

class GetAllAssistantMessageRequest(_message.Message):
    __slots__ = ("paginate", "criterias", "assistantId", "order")
    PAGINATE_FIELD_NUMBER: _ClassVar[int]
    CRITERIAS_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    paginate: _common_pb2.Paginate
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    assistantId: int
    order: _common_pb2.Ordering
    def __init__(self, paginate: _Optional[_Union[_common_pb2.Paginate, _Mapping]] = ..., criterias: _Optional[_Iterable[_Union[_common_pb2.Criteria, _Mapping]]] = ..., assistantId: _Optional[int] = ..., order: _Optional[_Union[_common_pb2.Ordering, _Mapping]] = ...) -> None: ...

class GetAllAssistantMessageResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error", "paginated")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[_common_pb2.AssistantConversationMessage]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[_common_pb2.AssistantConversationMessage, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., paginated: _Optional[_Union[_common_pb2.Paginated, _Mapping]] = ...) -> None: ...

class UpdateAssistantVersionRequest(_message.Message):
    __slots__ = ("assistantId", "assistantProviderModelId")
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTPROVIDERMODELID_FIELD_NUMBER: _ClassVar[int]
    assistantId: int
    assistantProviderModelId: int
    def __init__(self, assistantId: _Optional[int] = ..., assistantProviderModelId: _Optional[int] = ...) -> None: ...

class UpdateAssistantVersionResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: Assistant
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[Assistant, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class UpdateAssistantDetailRequest(_message.Message):
    __slots__ = ("assistantId", "name", "description")
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    assistantId: int
    name: str
    description: str
    def __init__(self, assistantId: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class TextToSpeechConfig(_message.Message):
    __slots__ = ("providerId", "providerModelId", "additionalParameters")
    PROVIDERID_FIELD_NUMBER: _ClassVar[int]
    PROVIDERMODELID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONALPARAMETERS_FIELD_NUMBER: _ClassVar[int]
    providerId: int
    providerModelId: int
    additionalParameters: _containers.RepeatedCompositeFieldContainer[_common_pb2.ProviderModelParameter]
    def __init__(self, providerId: _Optional[int] = ..., providerModelId: _Optional[int] = ..., additionalParameters: _Optional[_Iterable[_Union[_common_pb2.ProviderModelParameter, _Mapping]]] = ...) -> None: ...

class SpeechToTextConfig(_message.Message):
    __slots__ = ("providerId", "providerModelId", "additionalParameters")
    PROVIDERID_FIELD_NUMBER: _ClassVar[int]
    PROVIDERMODELID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONALPARAMETERS_FIELD_NUMBER: _ClassVar[int]
    providerId: int
    providerModelId: int
    additionalParameters: _containers.RepeatedCompositeFieldContainer[_common_pb2.ProviderModelParameter]
    def __init__(self, providerId: _Optional[int] = ..., providerModelId: _Optional[int] = ..., additionalParameters: _Optional[_Iterable[_Union[_common_pb2.ProviderModelParameter, _Mapping]]] = ...) -> None: ...

class FileUploadConfig(_message.Message):
    __slots__ = ("enabledFileSource",)
    ENABLEDFILESOURCE_FIELD_NUMBER: _ClassVar[int]
    enabledFileSource: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, enabledFileSource: _Optional[_Iterable[str]] = ...) -> None: ...

class PersonalizeAssistantRequest(_message.Message):
    __slots__ = ("assistantId", "deploymentType", "openingStatement", "suggestedQuestions", "assistantIconUrl", "textToSpeechConfig", "speechToTextConfig", "fileUploadConfig", "assistantIcon", "assistantName")
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENTTYPE_FIELD_NUMBER: _ClassVar[int]
    OPENINGSTATEMENT_FIELD_NUMBER: _ClassVar[int]
    SUGGESTEDQUESTIONS_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTICONURL_FIELD_NUMBER: _ClassVar[int]
    TEXTTOSPEECHCONFIG_FIELD_NUMBER: _ClassVar[int]
    SPEECHTOTEXTCONFIG_FIELD_NUMBER: _ClassVar[int]
    FILEUPLOADCONFIG_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTICON_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTNAME_FIELD_NUMBER: _ClassVar[int]
    assistantId: int
    deploymentType: str
    openingStatement: str
    suggestedQuestions: _containers.RepeatedScalarFieldContainer[str]
    assistantIconUrl: str
    textToSpeechConfig: TextToSpeechConfig
    speechToTextConfig: SpeechToTextConfig
    fileUploadConfig: FileUploadConfig
    assistantIcon: _common_pb2.Content
    assistantName: str
    def __init__(self, assistantId: _Optional[int] = ..., deploymentType: _Optional[str] = ..., openingStatement: _Optional[str] = ..., suggestedQuestions: _Optional[_Iterable[str]] = ..., assistantIconUrl: _Optional[str] = ..., textToSpeechConfig: _Optional[_Union[TextToSpeechConfig, _Mapping]] = ..., speechToTextConfig: _Optional[_Union[SpeechToTextConfig, _Mapping]] = ..., fileUploadConfig: _Optional[_Union[FileUploadConfig, _Mapping]] = ..., assistantIcon: _Optional[_Union[_common_pb2.Content, _Mapping]] = ..., assistantName: _Optional[str] = ...) -> None: ...
