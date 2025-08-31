import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import rapida.clients.protos.common_pb2 as _common_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateKnowledgeRequest(_message.Message):
    __slots__ = ("name", "description", "tags", "visibility", "embeddingModelProviderId", "embeddingModelProviderName", "knowledgeEmbeddingModelOptions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    EMBEDDINGMODELPROVIDERID_FIELD_NUMBER: _ClassVar[int]
    EMBEDDINGMODELPROVIDERNAME_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGEEMBEDDINGMODELOPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    visibility: str
    embeddingModelProviderId: int
    embeddingModelProviderName: str
    knowledgeEmbeddingModelOptions: _containers.RepeatedCompositeFieldContainer[_common_pb2.Metadata]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., visibility: _Optional[str] = ..., embeddingModelProviderId: _Optional[int] = ..., embeddingModelProviderName: _Optional[str] = ..., knowledgeEmbeddingModelOptions: _Optional[_Iterable[_Union[_common_pb2.Metadata, _Mapping]]] = ...) -> None: ...

class CreateKnowledgeResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _common_pb2.Knowledge
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[_common_pb2.Knowledge, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class GetAllKnowledgeRequest(_message.Message):
    __slots__ = ("paginate", "criterias")
    PAGINATE_FIELD_NUMBER: _ClassVar[int]
    CRITERIAS_FIELD_NUMBER: _ClassVar[int]
    paginate: _common_pb2.Paginate
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    def __init__(self, paginate: _Optional[_Union[_common_pb2.Paginate, _Mapping]] = ..., criterias: _Optional[_Iterable[_Union[_common_pb2.Criteria, _Mapping]]] = ...) -> None: ...

class GetAllKnowledgeResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error", "paginated")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[_common_pb2.Knowledge]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[_common_pb2.Knowledge, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., paginated: _Optional[_Union[_common_pb2.Paginated, _Mapping]] = ...) -> None: ...

class GetKnowledgeRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetKnowledgeResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _common_pb2.Knowledge
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[_common_pb2.Knowledge, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class CreateKnowledgeTagRequest(_message.Message):
    __slots__ = ("knowledgeId", "tags")
    KNOWLEDGEID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    knowledgeId: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, knowledgeId: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class KnowledgeDocument(_message.Message):
    __slots__ = ("id", "knowledgeId", "language", "name", "description", "documentSource", "documentType", "documentSize", "documentPath", "indexStatus", "retrievalCount", "tokenCount", "wordCount", "DisplayStatus", "status", "createdBy", "createdUser", "updatedBy", "updatedUser", "createdDate", "updatedDate")
    ID_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGEID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTSOURCE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTTYPE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTSIZE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTPATH_FIELD_NUMBER: _ClassVar[int]
    INDEXSTATUS_FIELD_NUMBER: _ClassVar[int]
    RETRIEVALCOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKENCOUNT_FIELD_NUMBER: _ClassVar[int]
    WORDCOUNT_FIELD_NUMBER: _ClassVar[int]
    DISPLAYSTATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATEDBY_FIELD_NUMBER: _ClassVar[int]
    CREATEDUSER_FIELD_NUMBER: _ClassVar[int]
    UPDATEDBY_FIELD_NUMBER: _ClassVar[int]
    UPDATEDUSER_FIELD_NUMBER: _ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    knowledgeId: int
    language: str
    name: str
    description: str
    documentSource: _struct_pb2.Struct
    documentType: str
    documentSize: int
    documentPath: str
    indexStatus: str
    retrievalCount: int
    tokenCount: int
    wordCount: int
    DisplayStatus: str
    status: str
    createdBy: int
    createdUser: _common_pb2.User
    updatedBy: int
    updatedUser: _common_pb2.User
    createdDate: _timestamp_pb2.Timestamp
    updatedDate: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., knowledgeId: _Optional[int] = ..., language: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., documentSource: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., documentType: _Optional[str] = ..., documentSize: _Optional[int] = ..., documentPath: _Optional[str] = ..., indexStatus: _Optional[str] = ..., retrievalCount: _Optional[int] = ..., tokenCount: _Optional[int] = ..., wordCount: _Optional[int] = ..., DisplayStatus: _Optional[str] = ..., status: _Optional[str] = ..., createdBy: _Optional[int] = ..., createdUser: _Optional[_Union[_common_pb2.User, _Mapping]] = ..., updatedBy: _Optional[int] = ..., updatedUser: _Optional[_Union[_common_pb2.User, _Mapping]] = ..., createdDate: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedDate: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetAllKnowledgeDocumentRequest(_message.Message):
    __slots__ = ("knowledgeId", "paginate", "criterias")
    KNOWLEDGEID_FIELD_NUMBER: _ClassVar[int]
    PAGINATE_FIELD_NUMBER: _ClassVar[int]
    CRITERIAS_FIELD_NUMBER: _ClassVar[int]
    knowledgeId: int
    paginate: _common_pb2.Paginate
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    def __init__(self, knowledgeId: _Optional[int] = ..., paginate: _Optional[_Union[_common_pb2.Paginate, _Mapping]] = ..., criterias: _Optional[_Iterable[_Union[_common_pb2.Criteria, _Mapping]]] = ...) -> None: ...

class GetAllKnowledgeDocumentResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error", "paginated")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[KnowledgeDocument]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[KnowledgeDocument, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., paginated: _Optional[_Union[_common_pb2.Paginated, _Mapping]] = ...) -> None: ...

class CreateKnowledgeDocumentRequest(_message.Message):
    __slots__ = ("knowledgeId", "documentSource", "dataSource", "contents", "preProcess", "separator", "maxChunkSize", "chunkOverlap", "name", "description", "documentStructure")
    class PRE_PROCESS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUTOMATIC: _ClassVar[CreateKnowledgeDocumentRequest.PRE_PROCESS]
        CUSTOM: _ClassVar[CreateKnowledgeDocumentRequest.PRE_PROCESS]
    AUTOMATIC: CreateKnowledgeDocumentRequest.PRE_PROCESS
    CUSTOM: CreateKnowledgeDocumentRequest.PRE_PROCESS
    class DOCUMENT_SOURCE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DOCUMENT_SOURCE_MANUAL: _ClassVar[CreateKnowledgeDocumentRequest.DOCUMENT_SOURCE]
        DOCUMENT_SOURCE_TOOL: _ClassVar[CreateKnowledgeDocumentRequest.DOCUMENT_SOURCE]
    DOCUMENT_SOURCE_MANUAL: CreateKnowledgeDocumentRequest.DOCUMENT_SOURCE
    DOCUMENT_SOURCE_TOOL: CreateKnowledgeDocumentRequest.DOCUMENT_SOURCE
    KNOWLEDGEID_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTSOURCE_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    PREPROCESS_FIELD_NUMBER: _ClassVar[int]
    SEPARATOR_FIELD_NUMBER: _ClassVar[int]
    MAXCHUNKSIZE_FIELD_NUMBER: _ClassVar[int]
    CHUNKOVERLAP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTSTRUCTURE_FIELD_NUMBER: _ClassVar[int]
    knowledgeId: int
    documentSource: CreateKnowledgeDocumentRequest.DOCUMENT_SOURCE
    dataSource: str
    contents: _containers.RepeatedCompositeFieldContainer[_common_pb2.Content]
    preProcess: CreateKnowledgeDocumentRequest.PRE_PROCESS
    separator: str
    maxChunkSize: int
    chunkOverlap: int
    name: str
    description: str
    documentStructure: str
    def __init__(self, knowledgeId: _Optional[int] = ..., documentSource: _Optional[_Union[CreateKnowledgeDocumentRequest.DOCUMENT_SOURCE, str]] = ..., dataSource: _Optional[str] = ..., contents: _Optional[_Iterable[_Union[_common_pb2.Content, _Mapping]]] = ..., preProcess: _Optional[_Union[CreateKnowledgeDocumentRequest.PRE_PROCESS, str]] = ..., separator: _Optional[str] = ..., maxChunkSize: _Optional[int] = ..., chunkOverlap: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., documentStructure: _Optional[str] = ...) -> None: ...

class CreateKnowledgeDocumentResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error", "paginated")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[KnowledgeDocument]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[KnowledgeDocument, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., paginated: _Optional[_Union[_common_pb2.Paginated, _Mapping]] = ...) -> None: ...

class KnowledgeDocumentSegment(_message.Message):
    __slots__ = ("index", "document_hash", "document_id", "text", "metadata", "entities")
    class Metadata(_message.Message):
        __slots__ = ("document_hash", "document_id", "knowledge_document_id", "knowledge_id", "project_id", "organization_id", "document_name")
        DOCUMENT_HASH_FIELD_NUMBER: _ClassVar[int]
        DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
        KNOWLEDGE_DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
        KNOWLEDGE_ID_FIELD_NUMBER: _ClassVar[int]
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
        DOCUMENT_NAME_FIELD_NUMBER: _ClassVar[int]
        document_hash: str
        document_id: str
        knowledge_document_id: int
        knowledge_id: int
        project_id: int
        organization_id: int
        document_name: str
        def __init__(self, document_hash: _Optional[str] = ..., document_id: _Optional[str] = ..., knowledge_document_id: _Optional[int] = ..., knowledge_id: _Optional[int] = ..., project_id: _Optional[int] = ..., organization_id: _Optional[int] = ..., document_name: _Optional[str] = ...) -> None: ...
    class Entities(_message.Message):
        __slots__ = ("organizations", "dates", "products", "events", "people", "times", "quantities", "locations", "industries")
        ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
        DATES_FIELD_NUMBER: _ClassVar[int]
        PRODUCTS_FIELD_NUMBER: _ClassVar[int]
        EVENTS_FIELD_NUMBER: _ClassVar[int]
        PEOPLE_FIELD_NUMBER: _ClassVar[int]
        TIMES_FIELD_NUMBER: _ClassVar[int]
        QUANTITIES_FIELD_NUMBER: _ClassVar[int]
        LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        INDUSTRIES_FIELD_NUMBER: _ClassVar[int]
        organizations: _containers.RepeatedScalarFieldContainer[str]
        dates: _containers.RepeatedScalarFieldContainer[str]
        products: _containers.RepeatedScalarFieldContainer[str]
        events: _containers.RepeatedScalarFieldContainer[str]
        people: _containers.RepeatedScalarFieldContainer[str]
        times: _containers.RepeatedScalarFieldContainer[str]
        quantities: _containers.RepeatedScalarFieldContainer[str]
        locations: _containers.RepeatedScalarFieldContainer[str]
        industries: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, organizations: _Optional[_Iterable[str]] = ..., dates: _Optional[_Iterable[str]] = ..., products: _Optional[_Iterable[str]] = ..., events: _Optional[_Iterable[str]] = ..., people: _Optional[_Iterable[str]] = ..., times: _Optional[_Iterable[str]] = ..., quantities: _Optional[_Iterable[str]] = ..., locations: _Optional[_Iterable[str]] = ..., industries: _Optional[_Iterable[str]] = ...) -> None: ...
    INDEX_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    index: str
    document_hash: str
    document_id: str
    text: str
    metadata: KnowledgeDocumentSegment.Metadata
    entities: KnowledgeDocumentSegment.Entities
    def __init__(self, index: _Optional[str] = ..., document_hash: _Optional[str] = ..., document_id: _Optional[str] = ..., text: _Optional[str] = ..., metadata: _Optional[_Union[KnowledgeDocumentSegment.Metadata, _Mapping]] = ..., entities: _Optional[_Union[KnowledgeDocumentSegment.Entities, _Mapping]] = ...) -> None: ...

class GetAllKnowledgeDocumentSegmentRequest(_message.Message):
    __slots__ = ("knowledgeId", "paginate", "criterias")
    KNOWLEDGEID_FIELD_NUMBER: _ClassVar[int]
    PAGINATE_FIELD_NUMBER: _ClassVar[int]
    CRITERIAS_FIELD_NUMBER: _ClassVar[int]
    knowledgeId: int
    paginate: _common_pb2.Paginate
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    def __init__(self, knowledgeId: _Optional[int] = ..., paginate: _Optional[_Union[_common_pb2.Paginate, _Mapping]] = ..., criterias: _Optional[_Iterable[_Union[_common_pb2.Criteria, _Mapping]]] = ...) -> None: ...

class GetAllKnowledgeDocumentSegmentResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error", "paginated")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[KnowledgeDocumentSegment]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[KnowledgeDocumentSegment, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., paginated: _Optional[_Union[_common_pb2.Paginated, _Mapping]] = ...) -> None: ...

class UpdateKnowledgeDetailRequest(_message.Message):
    __slots__ = ("knowledgeId", "name", "description")
    KNOWLEDGEID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    knowledgeId: int
    name: str
    description: str
    def __init__(self, knowledgeId: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class UpdateKnowledgeDocumentSegmentRequest(_message.Message):
    __slots__ = ("organizations", "dates", "products", "events", "people", "times", "quantities", "locations", "industries", "documentName", "documentId", "index")
    ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
    DATES_FIELD_NUMBER: _ClassVar[int]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    PEOPLE_FIELD_NUMBER: _ClassVar[int]
    TIMES_FIELD_NUMBER: _ClassVar[int]
    QUANTITIES_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    INDUSTRIES_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTNAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    organizations: _containers.RepeatedScalarFieldContainer[str]
    dates: _containers.RepeatedScalarFieldContainer[str]
    products: _containers.RepeatedScalarFieldContainer[str]
    events: _containers.RepeatedScalarFieldContainer[str]
    people: _containers.RepeatedScalarFieldContainer[str]
    times: _containers.RepeatedScalarFieldContainer[str]
    quantities: _containers.RepeatedScalarFieldContainer[str]
    locations: _containers.RepeatedScalarFieldContainer[str]
    industries: _containers.RepeatedScalarFieldContainer[str]
    documentName: str
    documentId: str
    index: str
    def __init__(self, organizations: _Optional[_Iterable[str]] = ..., dates: _Optional[_Iterable[str]] = ..., products: _Optional[_Iterable[str]] = ..., events: _Optional[_Iterable[str]] = ..., people: _Optional[_Iterable[str]] = ..., times: _Optional[_Iterable[str]] = ..., quantities: _Optional[_Iterable[str]] = ..., locations: _Optional[_Iterable[str]] = ..., industries: _Optional[_Iterable[str]] = ..., documentName: _Optional[str] = ..., documentId: _Optional[str] = ..., index: _Optional[str] = ...) -> None: ...

class DeleteKnowledgeDocumentSegmentRequest(_message.Message):
    __slots__ = ("documentId", "index", "reason")
    DOCUMENTID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    documentId: str
    index: str
    reason: str
    def __init__(self, documentId: _Optional[str] = ..., index: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...
