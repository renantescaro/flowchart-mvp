from .index_ctrl import bp as index_bp
from .login_ctrl import bp as login_bp
from .user_ctrl import bp as user_bp
from .user_group_ctrl import bp as user_group_bp
from .user_group_access_ctrl import bp as user_group_access_bp
from .work_ctrl import bp as work_bp
from .worker_ping_ctrl import bp as worker_ping_bp


blueprints_ctrl = [
    index_bp,
    login_bp,
    user_bp,
    user_group_bp,
    user_group_access_bp,
    work_bp,
    worker_ping_bp,
]
