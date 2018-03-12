
>>> from hello import app
>>> from flask import current_app
>>> current_app.name

>>> app_ctx = app.app_context()
>>> app_ctx.push()
>>> current_app.name
'hello'
>>> app_ctx.pop()
