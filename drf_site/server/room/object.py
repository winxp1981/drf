
"""
  Test non model api
"""
class Task(object):
    def __init__(self, **kwargs):
        for field in ('id', 'name', 'owner'):
            setattr(self, field, kwargs.get(field, None))

tasks = {
    1: Task(id=1, name='Demo', owner='xordoquy'),
    2: Task(id=2, name='Model less demo', owner='xordoquy'),
    3: Task(id=3, name='Sleep more', owner='xordoquy'),
}
