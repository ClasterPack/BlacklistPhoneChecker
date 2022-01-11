from dataclasses import dataclass, field
from typing import Optional

import marshmallow
from marshmallow_dataclass import class_schema


@dataclass
class BlacklistRequest:
    """Объект запроса чёрного списка."""

    blacklist_data: str
    expire_date: Optional[str] = field(
        metadata={'validate': marshmallow.fields.Date},
    )


@dataclass
class BlacklistResponse:
    """Объект результата запроса чёрношо списка."""

    answer: Optional[list]


@dataclass
class BlacklistFunctionResponse:
    """Объект результата функций чёрного списка."""

    function_answer: Optional[bool]


BlacklistRequestSchema = class_schema(BlacklistRequest)
BlacklistResponseSchema = class_schema(BlacklistResponse)
BlacklistFunctionResponseSchema = class_schema(BlacklistFunctionResponse)
