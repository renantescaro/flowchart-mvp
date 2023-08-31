import requests
from typing import Any, Dict, Tuple
from main.services.flowchart.parser_sv import ParserSv
from main.entities.node_kinds import (
    FlowchartParams,
    ParserData,
    GetRequest,
    PostRequest,
    FlowchartNode,
)


class FlowchartRunSv:
    def __init__(self) -> None:
        self._parser_sv = ParserSv()

    def get_node_by_key(self, key: int) -> FlowchartNode | None:
        for item in self.params.node_data:
            if item.key == key:
                return item
        return None

    def order_by_link(self):
        data_orderly = []
        for item in self.params.link_data:
            if len(data_orderly) == 0:
                data_orderly.append(self.get_node_by_key(item.from_node))

            if len(data_orderly) > 0:
                if item.from_node != data_orderly[-1]:
                    data_orderly.append(self.get_node_by_key(item.from_node))

            data_orderly.append(self.get_node_by_key(item.to_node))

        self.params.node_data = data_orderly

    def execute(self, params: Dict) -> Tuple[Any, int]:
        self.params: FlowchartParams = FlowchartParams.from_dict(params)

        self.order_by_link()

        iteration_result = None
        parser_result = None
        for node in self.params.node_data:
            # Parser Data
            if node.data_content.get("nodeType") == "parserData":
                parser: ParserData = ParserData.from_dict(node.data_content)

                parser_result = self._parser_sv.execute(
                    parser.data_input,
                    iteration_result,
                    parser.data_exit,
                )

            # Get Request
            if node.data_content.get("nodeType") == "getRequest":
                get_request: GetRequest = GetRequest.from_dict(node.data_content)
                result = requests.get(
                    url=get_request.url,
                    params=get_request.params,
                )
                print(result.status_code)
                if result.status_code != get_request.status_code:
                    return (
                        f"node: {node.text}, response: {result.content}",
                        result.status_code,
                    )

                iteration_result = result.json()

            # Post Request
            if node.data_content.get("nodeType") == "postRequest":
                post_request: PostRequest = PostRequest.from_dict(node.data_content)
                body = post_request.body
                if parser_result:
                    body = parser_result

                print("body: ", body)
                result = requests.post(
                    url=post_request.url,
                    data=body,
                    headers=post_request.headers,
                )
                print(result.status_code)
                if result.status_code != post_request.status_code:
                    return (
                        f"node: {node.text}, response: {result.content}",
                        result.status_code,
                    )

                iteration_result = result.json()
        return {}, 200
