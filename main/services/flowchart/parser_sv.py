from typing import Dict, Any


class ParserSv:
    def _set_values_exit_template(self, template_exit: Any, key: str, new_value: str):
        if type(template_exit) is dict:
            for item in template_exit:
                if type(template_exit[item]) is str:
                    if str(template_exit[item]).find(key) > -1:
                        result = str(template_exit[item]).replace(key, new_value)
                        template_exit[item] = result

                if type(item) is list:
                    for index in range(item):
                        template_exit[item[index]] = self._set_values_exit_template(
                            template_exit, key, new_value
                        )

        if type(template_exit) is str:
            if str(template_exit[item]).find(key) > -1:
                result = str(template_exit[item]).replace(key, new_value)
                template_exit[item] = result

        return template_exit

    def _search_wildcard(self, node: Dict, final_values: Any, exit_data: Any):
        for index in node:
            if type(node[index]) is dict:
                exit_data = self._search_wildcard(
                    node[index], final_values[index], exit_data
                )

            if type(node[index]) is str:
                if str(node[index]).find("((") > -1:
                    key = str(node[index]).strip()
                    new_value = final_values[index]
                    exit_data = self._set_values_exit_template(
                        exit_data, key, str(new_value)
                    )

            if type(node[index]) is list:
                print("List: ", node[index])
                for sub_index in range(len(node[index])):
                    if str(node[index][sub_index]).find("((") > -1:
                        key = str(node[index][sub_index]).strip()
                        new_value = final_values[index][sub_index]
                        exit_data = self._set_values_exit_template(
                            exit_data, key, str(new_value)
                        )
        return exit_data

    def execute(self, input_data_template: Any, input_data, exit_data_template):
        return self._search_wildcard(
            input_data_template,
            input_data,
            exit_data_template,
        )
