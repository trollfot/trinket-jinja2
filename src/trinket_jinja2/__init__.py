from pathlib import Path
from trinket_jinja2.extension import Jinja2Extension


def jinja2(app, cache: str=None):
    if cache is not None:
        cache = Path(cache)
    app['jinja2'] = Jinja2Extension(cache)
    return app
