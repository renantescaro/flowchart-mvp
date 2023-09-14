from flask import Flask
from werkzeug.routing.rules import Rule
from main.database.models.database import Database, select
from main.database.models.routes_model import Routes
from main.database.models.user_model import User
from main.database.models.user_group_model import UserGroup
from main.services.access_control_sv import AccessControlSv
from main.helpers.enums.dot_env import DotEnvEnum
from main.helpers.settings import Settings


class InsertInitialData:
    def __init__(self, app: Flask) -> None:
        self._app = app

    def execute(self):
        print("Insert Initial Data")
        self._insert_routes()

        if self._check_exist_data():
            return

        id_user_group = self._insert_user_group()
        self._insert_admin_user(id_user_group)

    def _check_exist_data(self) -> bool:
        stm = select(User)
        users_data = Database().get_all(stm)
        return True if users_data else False

    def _insert_user_group(self) -> int:
        stm = select(UserGroup)
        users_group_data = Database().get_all(stm)

        if not users_group_data:
            user_group = UserGroup(
                name="admin",
                is_admin=True,
            )
            Database().save(user_group)
            return user_group.id

    def _insert_admin_user(self, id_user_group: int):
        username = Settings.get(
            DotEnvEnum.USER_ADM.value,
        )
        password = Settings.get(
            DotEnvEnum.USER_ADM_PASSWORD.value,
        )
        hash_password = AccessControlSv().create_hash(password)

        user = User(
            username=username,
            email="",
            password=hash_password,
            id_user_group=id_user_group,
        )
        Database().save(user)

    def _insert_routes(self) -> None:
        stm = select(Routes)
        routes_data = Database().get_all(stm)

        if not routes_data:
            for rule in self._app.url_map.iter_rules():
                self._register_route(rule)

    def _register_route(self, rule: Rule):
        if not rule.methods:
            return

        for method in rule.methods:
            if method in ["HEAD", "OPTIONS"]:
                continue

            route = Routes(name=str(rule), method=method)
            Database().save(route)
