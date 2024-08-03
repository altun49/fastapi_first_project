from pydantic import BaseModel


class STask(BaseModel):
    name: str
    description: str | None


class STaskAdd(STask):
    id: int


class STaskId(BaseModel):
    ok: bool = True
    task_id: int