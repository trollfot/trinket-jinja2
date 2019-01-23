from pathlib import Path
from jinja2 import (
    Environment, FileSystemBytecodeCache, FileSystemLoader, select_autoescape)


class Jinja2Extension:

    __slots__ = ('loader', 'environment')
    
    def __init__(self, cache: str=None, filters: dict=None):
        if cache is not None:
            bc_cache = FileSystemBytecodeCache(cache, '%s.cache')
        self.loader = FileSystemLoader([])
        self.environment = Environment(
            loader=self.loader,
            enable_async=True,
            autoescape=select_autoescape(['html', 'xml'])
        )
        self.environment.filters = filters or {}

    def __getitem__(self, path: str):
        path = Path(path)
        if not path.is_file():
            raise LookupError(f'Template file {path} does not exist.')
        path = path.resolve()
        parent = path.parent
        if not parent in self.loader.searchpath:
            self.loader.searchpath.append(parent)
        return self.environment.get_template(path.name, parent=parent)

    def template(self, path: str):
        template = self[path]
        return template.render_async
