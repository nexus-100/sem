def diagnose(signal: float | int) -> None:
    """
    Принимает значения датчика (мА) и выдает полную текстовую диагностику
    состояния датчика и коровы
    """
    if (type(signal) != float) and (type(signal) != int):
        raise TypeError("Неверные входные данные!")
    signal = float(signal)

    if signal == 0:
        print("Датчик отключен! Температура и состояние коровы неизвестны")
        return None

    if (signal > 20.1) or (signal < 3.9):
        print("Датчик неисправен! Температура и состояние коровы неизвестны")
        return None

    print(f"Получен сигнал датчика {signal}мА, датчик исправен")

    PVmin = 0.0
    PVmax = 75.0

    temperature = (signal - 4) * (PVmax - PVmin)/(20 - 4) + PVmin

    if temperature > 39.6:
        status = "корова заболела, срочно нужен ветеринар"
    elif 39.1 <= temperature <= 39.5:
        status = "корова перегрелась, требуется охлаждение"
    elif 37.5 <= temperature <= 39.0:
        status = "с коровой все ок"
    elif 35.0 <= temperature <= 37.4:
        status = "корова замерзла, требуется обогрев"
    elif temperature < 34.9:
        status = "требуется внимание, датчик свалился или корова плохо себя чувствует"
    else:
        """
        здесь пограничные значения (34.95, 37.45, 39.05)
        """
        status = "неопределенное состояние"
    print(f"Температура {round(temperature, 1)} градусов, {status}")

diagnose(12.11)
