# Flask-Migrate
Rel: https://github.com/miguelgrinberg/Flask-Migrate

Migrate: 使用是類似git 版本控制DB Table's Structures、出自於不同app version會使用不同的structure.

使用flask & click 實現指令方式管理DB的init、migrate、history etc.

python concept & source code structure:
```
/flask_migrate
- __init__.py  
- cli.py
```

* \_\_init__.py: 導入[alembic](https://alembic.sqlalchemy.org/en/latest/)實現對各種資料庫operation.
* cli.py: flask & click 非常棒的指令管理範例寫法

## model.py範例 using flask_migrate & flask_sqlalchemy
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
```
## Migrate(app, db)原理，app.cli.add_command(db_cli_group, name=self.command)添加flask cli command
```python
class Migrate(object):
    ...init class object ...
        from flask_migrate.cli import db as db_cli_group
        app.cli.add_command(db_cli_group, name=self.command)
```


Flask Cli 是獨立的Process, 跟App run是分開的。 If you need to run at least two Flask applications 建議使用Docker etc. 方式做隔離 to aoivd cli confusion。