import rapida.artifacts.protos.common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAllModelRequest(_message.Message):
    __slots__ = ("criterias",)
    CRITERIAS_FIELD_NUMBER: _ClassVar[int]
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    def __init__(self, criterias: _Optional[_Iterable[_Union[_common_pb2.Criteria, _Mapping]]] = ...) -> None: ...

class GetAllModelResponse(_message.Message):
    __slots__ = ("code", "success", "data")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[_common_pb2.ProviderModel]
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[_common_pb2.ProviderModel, _Mapping]]] = ...) -> None: ...

class GetModelRequest(_message.Message):
    __slots__ = ("modelId",)
    MODELID_FIELD_NUMBER: _ClassVar[int]
    modelId: int
    def __init__(self, modelId: _Optional[int] = ...) -> None: ...

class GetModelResponse(_message.Message):
    __slots__ = ("code", "success", "model")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    model: _common_pb2.ProviderModel
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., model: _Optional[_Union[_common_pb2.ProviderModel, _Mapping]] = ...) -> None: ...

class GetAllProviderRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAllProviderResponse(_message.Message):
    __slots__ = ("code", "success", "data")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[_common_pb2.Provider]
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[_common_pb2.Provider, _Mapping]]] = ...) -> None: ...
