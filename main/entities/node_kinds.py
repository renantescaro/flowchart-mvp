from typing import Any, Dict, List
from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json


@dataclass
class LinkNode:
    from_node: int = field(metadata=config(field_name="from"))
    to_node: int = field(metadata=config(field_name="to"))


@dataclass
class FlowchartNode:
    text: str
    color: str
    data_content: Dict = field(metadata=config(field_name="dataContent"))
    key: int


@dataclass_json
@dataclass
class FlowchartParams:
    kind: str = field(metadata=config(field_name="class"))
    node_data: List[FlowchartNode] = field(metadata=config(field_name="nodeDataArray"))
    link_data: List[LinkNode] = field(metadata=config(field_name="linkDataArray"))


@dataclass_json
@dataclass
class GetRequest:
    node_type: str = field(metadata=config(field_name="nodeType"))
    url: str
    params: str
    result: Any = None
    status_code: int = 200


@dataclass_json
@dataclass
class PostRequest:
    node_type: str = field(metadata=config(field_name="nodeType"))
    url: str
    body: str
    headers: Dict = field(metadata=config(field_name="headers"))
    result: Any = None
    status_code: int = 200


@dataclass_json
@dataclass
class ParserData:
    data_input: Dict = field(metadata=config(field_name="dataInput"))
    data_exit: Dict = field(metadata=config(field_name="dataExit"))
