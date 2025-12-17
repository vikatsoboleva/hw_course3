import time

def delay_100ms(func):
    def wrapper(*args, **kwargs):
        time.sleep(0.1)  # задержка ~100 мс
        return func(*args, **kwargs)
    return wrapper


@delay_100ms
def say_hello(name):
    return f"Привет, {name}!"


# Проверка
print(say_hello("Вика Соболева"))

