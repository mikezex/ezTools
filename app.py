from flask import Flask

from controllers.user_controller import user_bp

app = Flask(__name__)

# 注册用户相关的蓝图到 Flask 应用
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run()
