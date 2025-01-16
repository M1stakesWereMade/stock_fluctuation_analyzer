import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    """
    Загружает исторические данные о ценах акций с Yahoo Finance.

    :param ticker: str, тикер акции (например, 'AAPL').
    :param period: str, период данных (например, '1mo', '1y', 'max').
    :return: pandas.DataFrame с данными о ценах акций.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    """
    Добавляет столбец скользящего среднего к данным о ценах акций.

    :param data: pandas.DataFrame, данные о ценах акций.
    :param window_size: int, размер окна для вычисления скользящего среднего.
    :return: pandas.DataFrame с добавленным столбцом 'Moving_Average'.
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data
