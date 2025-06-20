from google.protobuf import timestamp_pb2 as _timestamp_pb2
import rapida.artifacts.protos.common_pb2 as _common_pb2
import assistant_deployment_pb2 as _assistant_deployment_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssistantTool(_message.Message):
    __slots__ = ("id", "assistantId", "toolId", "name", "projectId", "organizationId", "options", "tool", "code", "status", "createdDate", "updatedDate")
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    TOOLID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TOOL_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    assistantId: int
    toolId: int
    name: str
    projectId: int
    organizationId: int
    options: _struct_pb2.Struct
    tool: Tool
    code: str
    status: str
    createdDate: _timestamp_pb2.Timestamp
    updatedDate: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., assistantId: _Optional[int] = ..., toolId: _Optional[int] = ..., name: _Optional[str] = ..., projectId: _Optional[int] = ..., organizationId: _Optional[int] = ..., options: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., tool: _Optional[_Union[Tool, _Mapping]] = ..., code: _Optional[str] = ..., status: _Optional[str] = ..., createdDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updatedDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Assistant(_message.Message):
    __slots__ = ("id", "status", "visibility", "source", "sourceIdentifier", "assistantTools", "projectId", "organizationId", "assistantProviderModelId", "assistantProviderModel", "name", "description", "assistantTag", "language", "organization", "assistantKnowledgeConfigurations", "createdBy", "createdUser", "updatedBy", "updatedUser", "createdDate", "updatedDate", "appAppearance", "webAppearance", "debuggerDeployment", "phoneDeployment", "whatsappDeployment", "webPluginDeployment", "apiDeployment", "assistantConversations")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCEIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTTOOLS_FIELD_NUMBER: _ClassVar[int]
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
    DEBUGGERDEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    PHONEDEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    WHATSAPPDEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    WEBPLUGINDEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    APIDEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTCONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    id: int
    status: str
    visibility: str
    source: str
    sourceIdentifier: int
    assistantTools: _containers.RepeatedCompositeFieldContainer[AssistantTool]
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
    debuggerDeployment: _assistant_deployment_pb2.AssistantDebuggerDeployment
    phoneDeployment: _assistant_deployment_pb2.AssistantPhoneDeployment
    whatsappDeployment: _assistant_deployment_pb2.AssistantWhatsappDeployment
    webPluginDeployment: _assistant_deployment_pb2.AssistantWebpluginDeployment
    apiDeployment: _assistant_deployment_pb2.AssistantApiDeployment
    assistantConversations: _containers.RepeatedCompositeFieldContainer[_common_pb2.AssistantConversation]
    def __init__(self, id: _Optional[int] = ..., status: _Optional[str] = ..., visibility: _Optional[str] = ..., source: _Optional[str] = ..., sourceIdentifier: _Optional[int] = ..., assistantTools: _Optional[_Iterable[_Union[AssistantTool, _Mapping]]] = ..., projectId: _Optional[int] = ..., organizationId: _Optional[int] = ..., assistantProviderModelId: _Optional[int] = ..., assistantProviderModel: _Optional[_Union[AssistantProviderModel, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., assistantTag: _Optional[_Union[_common_pb2.Tag, _Mapping]] = ..., language: _Optional[str] = ..., organization: _Optional[_Union[_common_pb2.Organization, _Mapping]] = ..., assistantKnowledgeConfigurations: _Optional[_Iterable[_Union[AssistantKnowledgeConfiguration, _Mapping]]] = ..., createdBy: _Optional[int] = ..., createdUser: _Optional[_Union[_common_pb2.User, _Mapping]] = ..., updatedBy: _Optional[int] = ..., updatedUser: _Optional[_Union[_common_pb2.User, _Mapping]] = ..., createdDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updatedDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., appAppearance: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., webAppearance: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., debuggerDeployment: _Optional[_Union[_assistant_deployment_pb2.AssistantDebuggerDeployment, _Mapping]] = ..., phoneDeployment: _Optional[_Union[_assistant_deployment_pb2.AssistantPhoneDeployment, _Mapping]] = ..., whatsappDeployment: _Optional[_Union[_assistant_deployment_pb2.AssistantWhatsappDeployment, _Mapping]] = ..., webPluginDeployment: _Optional[_Union[_assistant_deployment_pb2.AssistantWebpluginDeployment, _Mapping]] = ..., apiDeployment: _Optional[_Union[_assistant_deployment_pb2.AssistantApiDeployment, _Mapping]] = ..., assistantConversations: _Optional[_Iterable[_Union[_common_pb2.AssistantConversation, _Mapping]]] = ...) -> None: ...

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

class AssistantToolConfigurationAttribute(_message.Message):
    __slots__ = ("toolId", "code", "options", "status")
    TOOLID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    toolId: int
    code: str
    options: _struct_pb2.Struct
    status: str
    def __init__(self, toolId: _Optional[int] = ..., code: _Optional[str] = ..., options: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., status: _Optional[str] = ...) -> None: ...

class CreateAssistantRequest(_message.Message):
    __slots__ = ("assistantProviderModelAttribute", "assistantAttribute", "tags", "assistantKnowledgeConfigurationAttributes", "assistantToolConfigurationAttribute")
    ASSISTANTPROVIDERMODELATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTKNOWLEDGECONFIGURATIONATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTTOOLCONFIGURATIONATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    assistantProviderModelAttribute: AssistantProviderModelAttribute
    assistantAttribute: AssistantAttribute
    tags: _containers.RepeatedScalarFieldContainer[str]
    assistantKnowledgeConfigurationAttributes: _containers.RepeatedCompositeFieldContainer[AssistantKnowledgeConfigurationAttribute]
    assistantToolConfigurationAttribute: _containers.RepeatedCompositeFieldContainer[AssistantToolConfigurationAttribute]
    def __init__(self, assistantProviderModelAttribute: _Optional[_Union[AssistantProviderModelAttribute, _Mapping]] = ..., assistantAttribute: _Optional[_Union[AssistantAttribute, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ..., assistantKnowledgeConfigurationAttributes: _Optional[_Iterable[_Union[AssistantKnowledgeConfigurationAttribute, _Mapping]]] = ..., assistantToolConfigurationAttribute: _Optional[_Iterable[_Union[AssistantToolConfigurationAttribute, _Mapping]]] = ...) -> None: ...

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

class CreateAssistantToolConfigurationRequest(_message.Message):
    __slots__ = ("assistantId", "assistantToolConfigurationAttribute")
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTTOOLCONFIGURATIONATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    assistantId: int
    assistantToolConfigurationAttribute: _containers.RepeatedCompositeFieldContainer[AssistantToolConfigurationAttribute]
    def __init__(self, assistantId: _Optional[int] = ..., assistantToolConfigurationAttribute: _Optional[_Iterable[_Union[AssistantToolConfigurationAttribute, _Mapping]]] = ...) -> None: ...

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

class GetAllAssistantUserConversationRequest(_message.Message):
    __slots__ = ("assistantId", "paginate", "criterias", "source")
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    PAGINATE_FIELD_NUMBER: _ClassVar[int]
    CRITERIAS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    assistantId: int
    paginate: _common_pb2.Paginate
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    source: _common_pb2.Source
    def __init__(self, assistantId: _Optional[int] = ..., paginate: _Optional[_Union[_common_pb2.Paginate, _Mapping]] = ..., criterias: _Optional[_Iterable[_Union[_common_pb2.Criteria, _Mapping]]] = ..., source: _Optional[_Union[_common_pb2.Source, str]] = ...) -> None: ...

class GetAllAssistantUserConversationResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error", "paginated")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[_common_pb2.AssistantConversation]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[_common_pb2.AssistantConversation, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., paginated: _Optional[_Union[_common_pb2.Paginated, _Mapping]] = ...) -> None: ...

class GetAllAssistantToolRequest(_message.Message):
    __slots__ = ("assistantId", "paginate", "criterias")
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    PAGINATE_FIELD_NUMBER: _ClassVar[int]
    CRITERIAS_FIELD_NUMBER: _ClassVar[int]
    assistantId: int
    paginate: _common_pb2.Paginate
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    def __init__(self, assistantId: _Optional[int] = ..., paginate: _Optional[_Union[_common_pb2.Paginate, _Mapping]] = ..., criterias: _Optional[_Iterable[_Union[_common_pb2.Criteria, _Mapping]]] = ...) -> None: ...

class GetAllAssistantToolResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error", "paginated")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[AssistantTool]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[AssistantTool, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., paginated: _Optional[_Union[_common_pb2.Paginated, _Mapping]] = ...) -> None: ...

class Tool(_message.Message):
    __slots__ = ("id", "code", "name", "description", "setupOptions", "intializeOptions", "icon", "visibility")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SETUPOPTIONS_FIELD_NUMBER: _ClassVar[int]
    INTIALIZEOPTIONS_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    id: int
    code: str
    name: str
    description: str
    setupOptions: _struct_pb2.Struct
    intializeOptions: _struct_pb2.Struct
    icon: str
    visibility: str
    def __init__(self, id: _Optional[int] = ..., code: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., setupOptions: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., intializeOptions: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., icon: _Optional[str] = ..., visibility: _Optional[str] = ...) -> None: ...

class GetToolRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetToolResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: Tool
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[Tool, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class GetAllToolRequest(_message.Message):
    __slots__ = ("paginate", "criterias")
    PAGINATE_FIELD_NUMBER: _ClassVar[int]
    CRITERIAS_FIELD_NUMBER: _ClassVar[int]
    paginate: _common_pb2.Paginate
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    def __init__(self, paginate: _Optional[_Union[_common_pb2.Paginate, _Mapping]] = ..., criterias: _Optional[_Iterable[_Union[_common_pb2.Criteria, _Mapping]]] = ...) -> None: ...

class GetAllToolResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error", "paginated")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[Tool]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[Tool, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., paginated: _Optional[_Union[_common_pb2.Paginated, _Mapping]] = ...) -> None: ...
