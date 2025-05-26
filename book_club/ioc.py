from typing import AsyncIterable
from uuid import uuid4

from dishka import Provider, Scope, provide, AnyOf, from_context
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from book_club.application import interfaces
from book_club.application.interactors import (
    GetBookInteractor,
    NewBookInteractor
)
from book_club.config import Config
from book_club.infrastructure.database import new_session_maker
from dbook_club.infrastructure.gateways import BookGateway


class AppProvider(Provider):
    ...
