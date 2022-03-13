from tortoise import Tortoise, run_async


async def init_db():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['__main__']}
    )

    await Tortoise.generate_schemas()

