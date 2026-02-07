from fastapi import APIRouter
from sse_starlette import EventSourceResponse
from .events import broadcaster


router = APIRouter()

@router.get("/events")
async def get_events():

    async def event_generator():
        async for broadcast in broadcaster.register():
            yield f"data: {broadcast}\n\n"
    return EventSourceResponse(event_generator(), media_type="text/event-stream")