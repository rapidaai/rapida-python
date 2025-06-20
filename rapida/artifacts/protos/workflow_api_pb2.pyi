from google.protobuf import timestamp_pb2 as _timestamp_pb2
import rapida.artifacts.protos.common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Workflow(_message.Message):
    __slots__ = ("id", "edges", "flowNodes", "name", "description", "source", "sourceIdentifier", "visibility", "workflowTag", "workflowVersionId", "workflowVersion", "status", "createdBy", "createdUser", "updatedBy", "updatedUser", "createdDate", "updatedDate")
    ID_FIELD_NUMBER: _ClassVar[int]
    EDGES_FIELD_NUMBER: _ClassVar[int]
    FLOWNODES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCEIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    WORKFLOWTAG_FIELD_NUMBER: _ClassVar[int]
    WORKFLOWVERSIONID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOWVERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATEDBY_FIELD_NUMBER: _ClassVar[int]
    CREATEDUSER_FIELD_NUMBER: _ClassVar[int]
    UPDATEDBY_FIELD_NUMBER: _ClassVar[int]
    UPDATEDUSER_FIELD_NUMBER: _ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    edges: _containers.RepeatedCompositeFieldContainer[Edge]
    flowNodes: _containers.RepeatedCompositeFieldContainer[FlowNode]
    name: str
    description: str
    source: str
    sourceIdentifier: int
    visibility: str
    workflowTag: _common_pb2.Tag
    workflowVersionId: int
    workflowVersion: WorkflowVersion
    status: str
    createdBy: int
    createdUser: _common_pb2.User
    updatedBy: int
    updatedUser: _common_pb2.User
    createdDate: _timestamp_pb2.Timestamp
    updatedDate: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., edges: _Optional[_Iterable[_Union[Edge, _Mapping]]] = ..., flowNodes: _Optional[_Iterable[_Union[FlowNode, _Mapping]]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., source: _Optional[str] = ..., sourceIdentifier: _Optional[int] = ..., visibility: _Optional[str] = ..., workflowTag: _Optional[_Union[_common_pb2.Tag, _Mapping]] = ..., workflowVersionId: _Optional[int] = ..., workflowVersion: _Optional[_Union[WorkflowVersion, _Mapping]] = ..., status: _Optional[str] = ..., createdBy: _Optional[int] = ..., createdUser: _Optional[_Union[_common_pb2.User, _Mapping]] = ..., updatedBy: _Optional[int] = ..., updatedUser: _Optional[_Union[_common_pb2.User, _Mapping]] = ..., createdDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updatedDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class WorkflowVersion(_message.Message):
    __slots__ = ("id", "workflowJson")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOWJSON_FIELD_NUMBER: _ClassVar[int]
    id: int
    workflowJson: str
    def __init__(self, id: _Optional[int] = ..., workflowJson: _Optional[str] = ...) -> None: ...

class Edge(_message.Message):
    __slots__ = ("id", "out", "condition", "conditionalTaskId")
    ID_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    OUT_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    CONDITIONALTASKID_FIELD_NUMBER: _ClassVar[int]
    id: int
    out: int
    condition: str
    conditionalTaskId: int
    def __init__(self, id: _Optional[int] = ..., out: _Optional[int] = ..., condition: _Optional[str] = ..., conditionalTaskId: _Optional[int] = ..., **kwargs) -> None: ...

class FlowNode(_message.Message):
    __slots__ = ("id", "type", "nodeInputs", "inputTask", "endpointTask", "outputTask", "conditionalTask")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NODEINPUTS_FIELD_NUMBER: _ClassVar[int]
    INPUTTASK_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTTASK_FIELD_NUMBER: _ClassVar[int]
    OUTPUTTASK_FIELD_NUMBER: _ClassVar[int]
    CONDITIONALTASK_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: str
    nodeInputs: _containers.RepeatedCompositeFieldContainer[NodeInputs]
    inputTask: InputTask
    endpointTask: EndpointTask
    outputTask: OutputTask
    conditionalTask: ConditionalTask
    def __init__(self, id: _Optional[int] = ..., type: _Optional[str] = ..., nodeInputs: _Optional[_Iterable[_Union[NodeInputs, _Mapping]]] = ..., inputTask: _Optional[_Union[InputTask, _Mapping]] = ..., endpointTask: _Optional[_Union[EndpointTask, _Mapping]] = ..., outputTask: _Optional[_Union[OutputTask, _Mapping]] = ..., conditionalTask: _Optional[_Union[ConditionalTask, _Mapping]] = ...) -> None: ...

class NodeInputs(_message.Message):
    __slots__ = ("id", "flowNodeId", "inputId", "variable", "identifier", "inputType", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    FLOWNODEID_FIELD_NUMBER: _ClassVar[int]
    INPUTID_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    INPUTTYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    flowNodeId: int
    inputId: int
    variable: WorkflowVariable
    identifier: str
    inputType: str
    name: str
    def __init__(self, id: _Optional[int] = ..., flowNodeId: _Optional[int] = ..., inputId: _Optional[int] = ..., variable: _Optional[_Union[WorkflowVariable, _Mapping]] = ..., identifier: _Optional[str] = ..., inputType: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class WorkflowVariable(_message.Message):
    __slots__ = ("id", "variableType", "valueType", "defaultValue", "name", "identifier")
    ID_FIELD_NUMBER: _ClassVar[int]
    VARIABLETYPE_FIELD_NUMBER: _ClassVar[int]
    VALUETYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULTVALUE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    id: int
    variableType: str
    valueType: str
    defaultValue: str
    name: str
    identifier: str
    def __init__(self, id: _Optional[int] = ..., variableType: _Optional[str] = ..., valueType: _Optional[str] = ..., defaultValue: _Optional[str] = ..., name: _Optional[str] = ..., identifier: _Optional[str] = ...) -> None: ...

class RunWorkflowRequest(_message.Message):
    __slots__ = ("workflowId", "variables")
    WORKFLOWID_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    workflowId: int
    variables: _containers.RepeatedCompositeFieldContainer[WorkflowVariable]
    def __init__(self, workflowId: _Optional[int] = ..., variables: _Optional[_Iterable[_Union[WorkflowVariable, _Mapping]]] = ...) -> None: ...

class GetWorkflowRequest(_message.Message):
    __slots__ = ("workflowId",)
    WORKFLOWID_FIELD_NUMBER: _ClassVar[int]
    workflowId: int
    def __init__(self, workflowId: _Optional[int] = ...) -> None: ...

class EndpointTask(_message.Message):
    __slots__ = ("id", "endpointId")
    ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTID_FIELD_NUMBER: _ClassVar[int]
    id: int
    endpointId: int
    def __init__(self, id: _Optional[int] = ..., endpointId: _Optional[int] = ...) -> None: ...

class OutputTask(_message.Message):
    __slots__ = ("id", "outputs")
    ID_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    id: int
    outputs: _containers.RepeatedCompositeFieldContainer[Outputs]
    def __init__(self, id: _Optional[int] = ..., outputs: _Optional[_Iterable[_Union[Outputs, _Mapping]]] = ...) -> None: ...

class ConditionalTask(_message.Message):
    __slots__ = ("id", "conditions")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    id: int
    conditions: _containers.RepeatedCompositeFieldContainer[Condition]
    def __init__(self, id: _Optional[int] = ..., conditions: _Optional[_Iterable[_Union[Condition, _Mapping]]] = ...) -> None: ...

class Condition(_message.Message):
    __slots__ = ("id", "conditionalTaskId", "type", "precedence", "ruleGroups", "ruleGroupEdges")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONDITIONALTASKID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PRECEDENCE_FIELD_NUMBER: _ClassVar[int]
    RULEGROUPS_FIELD_NUMBER: _ClassVar[int]
    RULEGROUPEDGES_FIELD_NUMBER: _ClassVar[int]
    id: int
    conditionalTaskId: int
    type: str
    precedence: int
    ruleGroups: _containers.RepeatedCompositeFieldContainer[RuleGroup]
    ruleGroupEdges: _containers.RepeatedCompositeFieldContainer[Edge]
    def __init__(self, id: _Optional[int] = ..., conditionalTaskId: _Optional[int] = ..., type: _Optional[str] = ..., precedence: _Optional[int] = ..., ruleGroups: _Optional[_Iterable[_Union[RuleGroup, _Mapping]]] = ..., ruleGroupEdges: _Optional[_Iterable[_Union[Edge, _Mapping]]] = ...) -> None: ...

class RuleGroup(_message.Message):
    __slots__ = ("id", "conditionId", "precedence", "connectingOperator", "rules")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONDITIONID_FIELD_NUMBER: _ClassVar[int]
    PRECEDENCE_FIELD_NUMBER: _ClassVar[int]
    CONNECTINGOPERATOR_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    id: int
    conditionId: int
    precedence: int
    connectingOperator: str
    rules: _containers.RepeatedCompositeFieldContainer[Rule]
    def __init__(self, id: _Optional[int] = ..., conditionId: _Optional[int] = ..., precedence: _Optional[int] = ..., connectingOperator: _Optional[str] = ..., rules: _Optional[_Iterable[_Union[Rule, _Mapping]]] = ...) -> None: ...

class Rule(_message.Message):
    __slots__ = ("id", "ruleGroupId", "operatorName", "precedence", "connectingOperator", "ruleVariables")
    ID_FIELD_NUMBER: _ClassVar[int]
    RULEGROUPID_FIELD_NUMBER: _ClassVar[int]
    OPERATORNAME_FIELD_NUMBER: _ClassVar[int]
    PRECEDENCE_FIELD_NUMBER: _ClassVar[int]
    CONNECTINGOPERATOR_FIELD_NUMBER: _ClassVar[int]
    RULEVARIABLES_FIELD_NUMBER: _ClassVar[int]
    id: int
    ruleGroupId: int
    operatorName: str
    precedence: int
    connectingOperator: str
    ruleVariables: _containers.RepeatedCompositeFieldContainer[RuleVariable]
    def __init__(self, id: _Optional[int] = ..., ruleGroupId: _Optional[int] = ..., operatorName: _Optional[str] = ..., precedence: _Optional[int] = ..., connectingOperator: _Optional[str] = ..., ruleVariables: _Optional[_Iterable[_Union[RuleVariable, _Mapping]]] = ...) -> None: ...

class RuleVariable(_message.Message):
    __slots__ = ("id", "position", "variableType", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    VARIABLETYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: int
    position: str
    variableType: str
    value: str
    def __init__(self, id: _Optional[int] = ..., position: _Optional[str] = ..., variableType: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Outputs(_message.Message):
    __slots__ = ("id", "outputTaskId", "outputId", "outputType")
    ID_FIELD_NUMBER: _ClassVar[int]
    OUTPUTTASKID_FIELD_NUMBER: _ClassVar[int]
    OUTPUTID_FIELD_NUMBER: _ClassVar[int]
    OUTPUTTYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    outputTaskId: int
    outputId: int
    outputType: str
    def __init__(self, id: _Optional[int] = ..., outputTaskId: _Optional[int] = ..., outputId: _Optional[int] = ..., outputType: _Optional[str] = ...) -> None: ...

class InputTask(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class RunWorkflowResponse(_message.Message):
    __slots__ = ("code", "success", "workflowId", "workflowRunId", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    WORKFLOWID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOWRUNID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    workflowId: int
    workflowRunId: int
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., workflowId: _Optional[int] = ..., workflowRunId: _Optional[int] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class GetWorkflowResponse(_message.Message):
    __slots__ = ("code", "success", "Data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    Data: Workflow
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., Data: _Optional[_Union[Workflow, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class GetAllWorkflowRequest(_message.Message):
    __slots__ = ("paginate", "criterias")
    PAGINATE_FIELD_NUMBER: _ClassVar[int]
    CRITERIAS_FIELD_NUMBER: _ClassVar[int]
    paginate: _common_pb2.Paginate
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    def __init__(self, paginate: _Optional[_Union[_common_pb2.Paginate, _Mapping]] = ..., criterias: _Optional[_Iterable[_Union[_common_pb2.Criteria, _Mapping]]] = ...) -> None: ...

class GetAllWorkflowResponse(_message.Message):
    __slots__ = ("code", "success", "Data", "error", "paginated")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    Data: _containers.RepeatedCompositeFieldContainer[Workflow]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., Data: _Optional[_Iterable[_Union[Workflow, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., paginated: _Optional[_Union[_common_pb2.Paginated, _Mapping]] = ...) -> None: ...

class WorkflowAttributes(_message.Message):
    __slots__ = ("name", "description", "source", "sourceIdentifier", "visibility", "tags", "edges", "flowNodes", "Workflow")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCEIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    EDGES_FIELD_NUMBER: _ClassVar[int]
    FLOWNODES_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    source: str
    sourceIdentifier: int
    visibility: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    edges: _containers.RepeatedCompositeFieldContainer[Edge]
    flowNodes: _containers.RepeatedCompositeFieldContainer[FlowNode]
    Workflow: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., source: _Optional[str] = ..., sourceIdentifier: _Optional[int] = ..., visibility: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., edges: _Optional[_Iterable[_Union[Edge, _Mapping]]] = ..., flowNodes: _Optional[_Iterable[_Union[FlowNode, _Mapping]]] = ..., Workflow: _Optional[str] = ...) -> None: ...

class CreateWorkflowRequest(_message.Message):
    __slots__ = ("workflowAttributes", "variables")
    WORKFLOWATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    workflowAttributes: WorkflowAttributes
    variables: _containers.RepeatedCompositeFieldContainer[WorkflowVariable]
    def __init__(self, workflowAttributes: _Optional[_Union[WorkflowAttributes, _Mapping]] = ..., variables: _Optional[_Iterable[_Union[WorkflowVariable, _Mapping]]] = ...) -> None: ...

class GetWorkflowRunOutputRequest(_message.Message):
    __slots__ = ("workflowId", "workflowRunId")
    WORKFLOWID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOWRUNID_FIELD_NUMBER: _ClassVar[int]
    workflowId: int
    workflowRunId: int
    def __init__(self, workflowId: _Optional[int] = ..., workflowRunId: _Optional[int] = ...) -> None: ...

class GetWorkflowRunOutputResponse(_message.Message):
    __slots__ = ("code", "success", "Data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    Data: WorkflowRunResponse
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., Data: _Optional[_Union[WorkflowRunResponse, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class WorkflowRunResponse(_message.Message):
    __slots__ = ("workflowRunId", "status", "outputs")
    WORKFLOWRUNID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    workflowRunId: int
    status: str
    outputs: _containers.RepeatedCompositeFieldContainer[WorkflowOutput]
    def __init__(self, workflowRunId: _Optional[int] = ..., status: _Optional[str] = ..., outputs: _Optional[_Iterable[_Union[WorkflowOutput, _Mapping]]] = ...) -> None: ...

class WorkflowOutput(_message.Message):
    __slots__ = ("id", "workflowRunId", "flowNodeId", "output", "status", "outputType", "responseCode", "flowNode")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOWRUNID_FIELD_NUMBER: _ClassVar[int]
    FLOWNODEID_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTTYPE_FIELD_NUMBER: _ClassVar[int]
    RESPONSECODE_FIELD_NUMBER: _ClassVar[int]
    FLOWNODE_FIELD_NUMBER: _ClassVar[int]
    id: int
    workflowRunId: int
    flowNodeId: int
    output: str
    status: str
    outputType: str
    responseCode: int
    flowNode: FlowNode
    def __init__(self, id: _Optional[int] = ..., workflowRunId: _Optional[int] = ..., flowNodeId: _Optional[int] = ..., output: _Optional[str] = ..., status: _Optional[str] = ..., outputType: _Optional[str] = ..., responseCode: _Optional[int] = ..., flowNode: _Optional[_Union[FlowNode, _Mapping]] = ...) -> None: ...

class CreateWorkflowTagRequest(_message.Message):
    __slots__ = ("workflowId", "tags")
    WORKFLOWID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    workflowId: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, workflowId: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class PublishWorkflowVersionRequest(_message.Message):
    __slots__ = ("workflowId", "workflowJson")
    WORKFLOWID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOWJSON_FIELD_NUMBER: _ClassVar[int]
    workflowId: int
    workflowJson: str
    def __init__(self, workflowId: _Optional[int] = ..., workflowJson: _Optional[str] = ...) -> None: ...

class UpdateWorkflowDetailRequest(_message.Message):
    __slots__ = ("workflowId", "name", "description")
    WORKFLOWID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    workflowId: int
    name: str
    description: str
    def __init__(self, workflowId: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
