import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import rapida.clients.protos.common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthenticateRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class RegisterUserRequest(_message.Message):
    __slots__ = ("email", "password", "name")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    name: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class Token(_message.Message):
    __slots__ = ("id", "token", "tokenType", "isExpired")
    ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKENTYPE_FIELD_NUMBER: _ClassVar[int]
    ISEXPIRED_FIELD_NUMBER: _ClassVar[int]
    id: int
    token: str
    tokenType: str
    isExpired: bool
    def __init__(self, id: _Optional[int] = ..., token: _Optional[str] = ..., tokenType: _Optional[str] = ..., isExpired: bool = ...) -> None: ...

class OrganizationRole(_message.Message):
    __slots__ = ("id", "organizationId", "role", "organizationName")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONNAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    organizationId: int
    role: str
    organizationName: str
    def __init__(self, id: _Optional[int] = ..., organizationId: _Optional[int] = ..., role: _Optional[str] = ..., organizationName: _Optional[str] = ...) -> None: ...

class ProjectRole(_message.Message):
    __slots__ = ("id", "projectId", "role", "projectName")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PROJECTNAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    projectId: int
    role: str
    projectName: str
    def __init__(self, id: _Optional[int] = ..., projectId: _Optional[int] = ..., role: _Optional[str] = ..., projectName: _Optional[str] = ...) -> None: ...

class FeaturePermission(_message.Message):
    __slots__ = ("id", "feature", "isEnable")
    ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    ISENABLE_FIELD_NUMBER: _ClassVar[int]
    id: int
    feature: str
    isEnable: bool
    def __init__(self, id: _Optional[int] = ..., feature: _Optional[str] = ..., isEnable: bool = ...) -> None: ...

class Authentication(_message.Message):
    __slots__ = ("user", "token", "organizationRole", "projectRoles", "featurePermissions")
    USER_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONROLE_FIELD_NUMBER: _ClassVar[int]
    PROJECTROLES_FIELD_NUMBER: _ClassVar[int]
    FEATUREPERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    user: _common_pb2.User
    token: Token
    organizationRole: OrganizationRole
    projectRoles: _containers.RepeatedCompositeFieldContainer[ProjectRole]
    featurePermissions: _containers.RepeatedCompositeFieldContainer[FeaturePermission]
    def __init__(self, user: _Optional[_Union[_common_pb2.User, _Mapping]] = ..., token: _Optional[_Union[Token, _Mapping]] = ..., organizationRole: _Optional[_Union[OrganizationRole, _Mapping]] = ..., projectRoles: _Optional[_Iterable[_Union[ProjectRole, _Mapping]]] = ..., featurePermissions: _Optional[_Iterable[_Union[FeaturePermission, _Mapping]]] = ...) -> None: ...

class ScopedAuthentication(_message.Message):
    __slots__ = ("userId", "organizationId", "projectId", "status")
    USERID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    userId: int
    organizationId: int
    projectId: int
    status: str
    def __init__(self, userId: _Optional[int] = ..., organizationId: _Optional[int] = ..., projectId: _Optional[int] = ..., status: _Optional[str] = ...) -> None: ...

class AuthenticationError(_message.Message):
    __slots__ = ("errorCode", "errorMessage", "humanMessage")
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    HUMANMESSAGE_FIELD_NUMBER: _ClassVar[int]
    errorCode: int
    errorMessage: str
    humanMessage: str
    def __init__(self, errorCode: _Optional[int] = ..., errorMessage: _Optional[str] = ..., humanMessage: _Optional[str] = ...) -> None: ...

class AuthenticateResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: Authentication
    error: AuthenticationError
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[Authentication, _Mapping]] = ..., error: _Optional[_Union[AuthenticationError, _Mapping]] = ...) -> None: ...

class ForgotPasswordRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class ForgotPasswordResponse(_message.Message):
    __slots__ = ("code", "success", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    error: AuthenticationError
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., error: _Optional[_Union[AuthenticationError, _Mapping]] = ...) -> None: ...

class CreatePasswordRequest(_message.Message):
    __slots__ = ("token", "password")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    token: str
    password: str
    def __init__(self, token: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class CreatePasswordResponse(_message.Message):
    __slots__ = ("code", "success", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    error: AuthenticationError
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., error: _Optional[_Union[AuthenticationError, _Mapping]] = ...) -> None: ...

class VerifyTokenRequest(_message.Message):
    __slots__ = ("tokenType", "token")
    TOKENTYPE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    tokenType: str
    token: str
    def __init__(self, tokenType: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class VerifyTokenResponse(_message.Message):
    __slots__ = ("code", "success", "data")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: Token
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[Token, _Mapping]] = ...) -> None: ...

class AuthorizeRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ScopeAuthorizeRequest(_message.Message):
    __slots__ = ("scope",)
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    scope: str
    def __init__(self, scope: _Optional[str] = ...) -> None: ...

class ScopedAuthenticationResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: ScopedAuthentication
    error: AuthenticationError
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[ScopedAuthentication, _Mapping]] = ..., error: _Optional[_Union[AuthenticationError, _Mapping]] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("code", "success", "data")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _common_pb2.User
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[_common_pb2.User, _Mapping]] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("email", "name")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    name: str
    def __init__(self, email: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class UpdateUserResponse(_message.Message):
    __slots__ = ("code", "success", "data")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _common_pb2.User
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[_common_pb2.User, _Mapping]] = ...) -> None: ...

class SocialAuthenticationRequest(_message.Message):
    __slots__ = ("state", "code")
    STATE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    state: str
    code: str
    def __init__(self, state: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class GetAllUserRequest(_message.Message):
    __slots__ = ("paginate", "criterias")
    PAGINATE_FIELD_NUMBER: _ClassVar[int]
    CRITERIAS_FIELD_NUMBER: _ClassVar[int]
    paginate: _common_pb2.Paginate
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    def __init__(self, paginate: _Optional[_Union[_common_pb2.Paginate, _Mapping]] = ..., criterias: _Optional[_Iterable[_Union[_common_pb2.Criteria, _Mapping]]] = ...) -> None: ...

class GetAllUserResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error", "paginated")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[_common_pb2.User]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[_common_pb2.User, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., paginated: _Optional[_Union[_common_pb2.Paginated, _Mapping]] = ...) -> None: ...

class OrganizationError(_message.Message):
    __slots__ = ("errorCode", "errorMessage", "humanMessage")
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    HUMANMESSAGE_FIELD_NUMBER: _ClassVar[int]
    errorCode: int
    errorMessage: str
    humanMessage: str
    def __init__(self, errorCode: _Optional[int] = ..., errorMessage: _Optional[str] = ..., humanMessage: _Optional[str] = ...) -> None: ...

class CreateOrganizationRequest(_message.Message):
    __slots__ = ("organizationName", "organizationSize", "organizationIndustry", "organizationContact")
    ORGANIZATIONNAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONSIZE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONINDUSTRY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONCONTACT_FIELD_NUMBER: _ClassVar[int]
    organizationName: str
    organizationSize: str
    organizationIndustry: str
    organizationContact: str
    def __init__(self, organizationName: _Optional[str] = ..., organizationSize: _Optional[str] = ..., organizationIndustry: _Optional[str] = ..., organizationContact: _Optional[str] = ...) -> None: ...

class UpdateOrganizationRequest(_message.Message):
    __slots__ = ("organizationId", "organizationName", "organizationIndustry", "organizationContact")
    ORGANIZATIONID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONNAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONINDUSTRY_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONCONTACT_FIELD_NUMBER: _ClassVar[int]
    organizationId: int
    organizationName: str
    organizationIndustry: str
    organizationContact: str
    def __init__(self, organizationId: _Optional[int] = ..., organizationName: _Optional[str] = ..., organizationIndustry: _Optional[str] = ..., organizationContact: _Optional[str] = ...) -> None: ...

class GetOrganizationRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetOrganizationResponse(_message.Message):
    __slots__ = ("code", "success", "data", "role", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _common_pb2.Organization
    role: OrganizationRole
    error: OrganizationError
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[_common_pb2.Organization, _Mapping]] = ..., role: _Optional[_Union[OrganizationRole, _Mapping]] = ..., error: _Optional[_Union[OrganizationError, _Mapping]] = ...) -> None: ...

class CreateOrganizationResponse(_message.Message):
    __slots__ = ("code", "success", "data", "role", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _common_pb2.Organization
    role: OrganizationRole
    error: OrganizationError
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[_common_pb2.Organization, _Mapping]] = ..., role: _Optional[_Union[OrganizationRole, _Mapping]] = ..., error: _Optional[_Union[OrganizationError, _Mapping]] = ...) -> None: ...

class UpdateOrganizationResponse(_message.Message):
    __slots__ = ("code", "success", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    error: OrganizationError
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., error: _Optional[_Union[OrganizationError, _Mapping]] = ...) -> None: ...

class UpdateBillingInformationRequest(_message.Message):
    __slots__ = ("paymentMethod", "billingInterval", "taxInformation", "address", "email")
    class BillingInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Annually: _ClassVar[UpdateBillingInformationRequest.BillingInterval]
        Monthly: _ClassVar[UpdateBillingInformationRequest.BillingInterval]
    Annually: UpdateBillingInformationRequest.BillingInterval
    Monthly: UpdateBillingInformationRequest.BillingInterval
    PAYMENTMETHOD_FIELD_NUMBER: _ClassVar[int]
    BILLINGINTERVAL_FIELD_NUMBER: _ClassVar[int]
    TAXINFORMATION_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    paymentMethod: str
    billingInterval: UpdateBillingInformationRequest.BillingInterval
    taxInformation: str
    address: str
    email: str
    def __init__(self, paymentMethod: _Optional[str] = ..., billingInterval: _Optional[_Union[UpdateBillingInformationRequest.BillingInterval, str]] = ..., taxInformation: _Optional[str] = ..., address: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class Project(_message.Message):
    __slots__ = ("id", "name", "description", "members", "status", "createdDate")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    members: _containers.RepeatedCompositeFieldContainer[_common_pb2.User]
    status: str
    createdDate: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., members: _Optional[_Iterable[_Union[_common_pb2.User, _Mapping]]] = ..., status: _Optional[str] = ..., createdDate: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateProjectRequest(_message.Message):
    __slots__ = ("projectName", "projectDescription")
    PROJECTNAME_FIELD_NUMBER: _ClassVar[int]
    PROJECTDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    projectName: str
    projectDescription: str
    def __init__(self, projectName: _Optional[str] = ..., projectDescription: _Optional[str] = ...) -> None: ...

class CreateProjectResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: Project
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[Project, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class UpdateProjectRequest(_message.Message):
    __slots__ = ("projectId", "projectName", "projectDescription")
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    PROJECTNAME_FIELD_NUMBER: _ClassVar[int]
    PROJECTDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    projectId: int
    projectName: str
    projectDescription: str
    def __init__(self, projectId: _Optional[int] = ..., projectName: _Optional[str] = ..., projectDescription: _Optional[str] = ...) -> None: ...

class UpdateProjectResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: Project
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[Project, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class GetProjectRequest(_message.Message):
    __slots__ = ("projectId",)
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    projectId: int
    def __init__(self, projectId: _Optional[int] = ...) -> None: ...

class GetProjectResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: Project
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[Project, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class GetAllProjectRequest(_message.Message):
    __slots__ = ("paginate", "criterias")
    PAGINATE_FIELD_NUMBER: _ClassVar[int]
    CRITERIAS_FIELD_NUMBER: _ClassVar[int]
    paginate: _common_pb2.Paginate
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    def __init__(self, paginate: _Optional[_Union[_common_pb2.Paginate, _Mapping]] = ..., criterias: _Optional[_Iterable[_Union[_common_pb2.Criteria, _Mapping]]] = ...) -> None: ...

class GetAllProjectResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error", "paginated")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[Project]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[Project, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., paginated: _Optional[_Union[_common_pb2.Paginated, _Mapping]] = ...) -> None: ...

class AddUsersToProjectRequest(_message.Message):
    __slots__ = ("email", "role", "projectIds")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PROJECTIDS_FIELD_NUMBER: _ClassVar[int]
    email: str
    role: str
    projectIds: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, email: _Optional[str] = ..., role: _Optional[str] = ..., projectIds: _Optional[_Iterable[int]] = ...) -> None: ...

class ArchiveProjectRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ArchiveProjectResponse(_message.Message):
    __slots__ = ("code", "success", "id", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    id: int
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., id: _Optional[int] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class AddUsersToProjectResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[Project]
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[Project, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class ProjectCredential(_message.Message):
    __slots__ = ("id", "projectId", "organizationId", "name", "key", "status", "createdBy", "updatedBy", "createdDate", "updatedDate", "createdUser")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATEDBY_FIELD_NUMBER: _ClassVar[int]
    UPDATEDBY_FIELD_NUMBER: _ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    CREATEDUSER_FIELD_NUMBER: _ClassVar[int]
    id: int
    projectId: int
    organizationId: int
    name: str
    key: str
    status: str
    createdBy: int
    updatedBy: int
    createdDate: _timestamp_pb2.Timestamp
    updatedDate: _timestamp_pb2.Timestamp
    createdUser: _common_pb2.User
    def __init__(self, id: _Optional[int] = ..., projectId: _Optional[int] = ..., organizationId: _Optional[int] = ..., name: _Optional[str] = ..., key: _Optional[str] = ..., status: _Optional[str] = ..., createdBy: _Optional[int] = ..., updatedBy: _Optional[int] = ..., createdDate: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedDate: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., createdUser: _Optional[_Union[_common_pb2.User, _Mapping]] = ...) -> None: ...

class CreateProjectCredentialRequest(_message.Message):
    __slots__ = ("projectId", "name")
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    projectId: int
    name: str
    def __init__(self, projectId: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class GetAllProjectCredentialRequest(_message.Message):
    __slots__ = ("paginate", "criterias", "projectId")
    PAGINATE_FIELD_NUMBER: _ClassVar[int]
    CRITERIAS_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    paginate: _common_pb2.Paginate
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    projectId: int
    def __init__(self, paginate: _Optional[_Union[_common_pb2.Paginate, _Mapping]] = ..., criterias: _Optional[_Iterable[_Union[_common_pb2.Criteria, _Mapping]]] = ..., projectId: _Optional[int] = ...) -> None: ...

class CreateProjectCredentialResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: ProjectCredential
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[ProjectCredential, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class GetAllProjectCredentialResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error", "paginated")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[ProjectCredential]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[ProjectCredential, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., paginated: _Optional[_Union[_common_pb2.Paginated, _Mapping]] = ...) -> None: ...
