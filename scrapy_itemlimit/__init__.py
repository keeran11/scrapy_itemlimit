"""Reusable Scrapy middleware for per-target item limiting."""

from .middlewares import PerTargetItemLimitSpiderMiddleware

__version__ = "0.2.0"

__all__ = [
    "PerTargetItemLimitSpiderMiddleware",
    "__version__",
]
