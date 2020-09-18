from app.models import Candlestick

def apca_bar_to_candle(apca_bar) -> Candlestick:
    return Candlestick(high=apca_bar.h, low=apca_bar.l, open=apca_bar.o, close=apca_bar.c, volume=apca_bar.v, time=apca_bar.t)