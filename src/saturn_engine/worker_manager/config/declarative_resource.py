from typing import Any

import dataclasses

from saturn_engine.core import api
from saturn_engine.utils.declarative_config import BaseObject


@dataclasses.dataclass
class ResourceSpec:
    type: str
    data: dict[str, Any]
    default_delay: float = 0
    concurrency: int = 1


@dataclasses.dataclass
class Resource(BaseObject):
    spec: ResourceSpec

    def to_core_object(self) -> api.ResourceItem:
        return api.ResourceItem(
            name=self.metadata.name,
            type=self.spec.type,
            data=self.spec.data,
            default_delay=self.spec.default_delay,
        )
