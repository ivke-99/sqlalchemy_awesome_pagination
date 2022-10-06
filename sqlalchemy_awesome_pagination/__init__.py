"""
SqlAlchemy Awesome Pagination namespace
"""
from .module.pagination import paginate

__all__ = [
    "paginate"
]

__import__("pkg_resources").declare_namespace(__name__)