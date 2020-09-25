import schedule
import threading
import time
from typing import List
from app.messaging import PriceInfoMessenger

class Scheduler:
    # spawn thread to use schedule API async
    @staticmethod
    def schedule(messengers: List[PriceInfoMessenger]) -> threading.Event:
        for messenger in messengers:
            schedule.every(messenger.interval).seconds.do(messenger.publish_all_info)

        schedstop = threading.Event()

        def timer():
            while not schedstop.is_set():
                schedule.run_pending()
                time.sleep(5)

        schedthread = threading.Thread(target=timer)
        schedthread.start()
        return schedstop

