import orjson
from decimal import Decimal
from ninja.renderers import BaseRenderer


class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def default(self, target: any):
        if isinstance(target, Decimal):
            return str(target)
        raise TypeError(f'Type is not JSON serializable: {type(target)}')

    def render(self, request, data, *, response_status):
        return orjson.dumps(data, default=self.default)
