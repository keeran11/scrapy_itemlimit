from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable
from typing import Any

from scrapy import Request


class PerTargetItemLimitSpiderMiddleware:
    """Stop pagination per target key once item limit is reached for that target.

    Configure with:
    - PER_TARGET_ITEM_LIMIT: int
    - TARGET_META_KEY: str (default: brand_token)
    """

    def __init__(self, settings: Any):
        self.per_target_limit = settings.getint("PER_TARGET_ITEM_LIMIT", 0)
        self.target_meta_key = settings.get("TARGET_META_KEY", "brand_token")
        self.target_counts = defaultdict(int)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_spider_output(self, response, result: Iterable, spider):
        target_key = response.meta.get(self.target_meta_key)

        for obj in result:
            if isinstance(obj, Request):
                req_target = obj.meta.get(self.target_meta_key, target_key)
                if self.per_target_limit and req_target and self.target_counts[req_target] >= self.per_target_limit:
                    continue
                yield obj
                continue

            if self.per_target_limit and target_key:
                if self.target_counts[target_key] >= self.per_target_limit:
                    continue
                self.target_counts[target_key] += 1

            yield obj
