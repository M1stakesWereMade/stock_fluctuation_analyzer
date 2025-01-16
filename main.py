from data_download import fetch_stock_data, add_moving_average
from data_plotting import create_and_save_plot


def notify_if_strong_fluctuations(data, threshold):
    """
    Анализирует данные о ценах акций и уведомляет, если колебания цен превышают заданный порог.

    :param data: pandas.DataFrame, данные о ценах акций с колонкой 'Close'.
    :param threshold: float, порог колебаний цен в процентах.
    """
    if 'Close' not in data:
        print("Ошибка: В предоставленных данных отсутствует столбец 'Close'.")
        return

    max_close = data['Close'].max()
    min_close = data['Close'].min()
    fluctuation_percentage = ((max_close - min_close) / min_close) * 100

    if fluctuation_percentage > threshold:
        print(f"Внимание! Цена акций колебалась на {fluctuation_percentage:.2f}% за период.")
        print(f"Максимальная цена закрытия: {max_close:.2f}")
        print(f"Минимальная цена закрытия: {min_close:.2f}")
    else:
        print(f"Колебания цен в {fluctuation_percentage:.2f}% не превышают порог {threshold}%.")


def main():
    """
    Основная функция программы. Позволяет пользователю выбрать тикер, период,
    анализировать данные и строить график цен.
    """
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Примеры тикеров: AAPL, GOOGL, MSFT, AMZN, TSLA.")
    print("Примеры периодов: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    # Fetch stock data
    stock_data = fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = add_moving_average(stock_data)

    # Plot the data
    create_and_save_plot(stock_data, ticker, period)

    # Analyze fluctuations
    threshold = float(input("Введите порог колебания цен в процентах (например, 5): "))
    notify_if_strong_fluctuations(stock_data, threshold)


if __name__ == "__main__":
    main()
