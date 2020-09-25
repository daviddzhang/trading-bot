import dotenv
dotenv.load_dotenv()

from app.messaging.pubsub import PyPubSubPriceMessenger
from app.data.apca_rest_stock_info import ScheduledAlpacaRestStockInfoFetcher
from app.scheduling.scheduler import Scheduler

def start_bot():
    fetcher = ScheduledAlpacaRestStockInfoFetcher("AAPL", 10)
    pubsub_messenger = PyPubSubPriceMessenger([fetcher])
    Scheduler.schedule([pubsub_messenger])

if __name__ == "__main__":
    start_bot()
