from aiohttp_session import get_session

from accounts.models import User
from database import objects



async def request_user_middleware(app, handler):
    async def middleware(request):
        session = await get_session(request)
        request.user = None
        user_id = session.get('user')
        if user_id is not None:
            request.user = objects.get(User, pk=user_id)
        return await handler(request)
    return middleware