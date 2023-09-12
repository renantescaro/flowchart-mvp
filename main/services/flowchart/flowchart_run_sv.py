import requests
from typing import Any, Dict, Optional, Tuple
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

    def _order_by_link(self):
        data_orderly = []
        for item in self.params.link_data:
            if len(data_orderly) == 0:
                data_orderly.append(self.get_node_by_key(item.from_node))

            if len(data_orderly) > 0:
                if item.from_node != data_orderly[-1]:
                    data_orderly.append(self.get_node_by_key(item.from_node))

            data_orderly.append(self.get_node_by_key(item.to_node))

        self.params.node_data = data_orderly

    def _parser_data(
        self,
        data_content: Dict,
        iteration_result: Optional[Any] = None,
    ):
        try:
            parser: ParserData = ParserData.from_dict(data_content)

            return self._parser_sv.execute(
                parser.data_input,
                iteration_result,
                parser.data_exit,
            )
        except Exception as e:
            print("Error _parser_data: ", e)
            raise Exception("Error _parser_data: ", e)

    def _get_request(
        self,
        node_text: str,
        data_content: Dict,
    ) -> Dict:
        try:
            get_request: GetRequest = GetRequest.from_dict(data_content)
            result = requests.get(
                url=get_request.url,
                params=get_request.params,
            )
            print(result.status_code)
            if result.status_code != get_request.status_code:
                raise Exception(
                    f"node: {node_text}, response: {result.content}", result.status_code
                )
            return result.json()

        except Exception as e:
            print("Error _get_request: ", e)
            raise Exception("Error _get_request: ", e)

    def _post_request(
        self,
        node_text: str,
        data_content: Dict,
        parser_result: Optional[Dict] = None,
    ) -> Dict:
        try:
            post_request: PostRequest = PostRequest.from_dict(data_content)
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
                raise Exception(
                    f"node: {node_text}, response: {result.content}",
                    result.status_code,
                )
            return result.json()

        except Exception as e:
            print("Error _get_request: ", e)
            raise Exception("Error _get_request: ", e)

    def execute(self, params: Dict) -> Tuple[Any, int]:
        try:
            self.params: FlowchartParams = FlowchartParams.from_dict(params)

            self._order_by_link()

            iteration_result = None
            parser_result = None
            for node in self.params.node_data:
                print(node)

                # Parser Data
                if node.data_content.get("nodeType") == "parserData":
                    parser_result = self._parser_data(
                        node.data_content, iteration_result
                    )

                # Get Request
                if node.data_content.get("nodeType") == "getRequest":
                    iteration_result = self._get_request(node.text, node.data_content)

                # Post Request
                if node.data_content.get("nodeType") == "postRequest":
                    iteration_result = self._post_request(
                        node.text,
                        node.data_content,
                        parser_result,
                    )
            return {}, 200

        except Exception as e:
            print("Error flowchart run: ", e)
            return {}, 400
