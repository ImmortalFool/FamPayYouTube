from fastapi import FastAPI
from routes.routes import router
from scheduler.initial_scheduler import initial_scheduler
from scheduler.frequent_sechduler import frequent_scheduler
from aiocron import crontab
import asyncio

search_query = 'smartphones'
app = FastAPI()
app.include_router(router)
initial_scheduler(search_query)


@crontab('*/10 * * * * *')  # Runs at every 10 secs
async def cron_job():
    await frequent_scheduler(search_query)


async def execute_cron():
    await asyncio.sleep(1)
