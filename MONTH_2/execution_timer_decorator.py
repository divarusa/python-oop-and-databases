import time

# Основное задание

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} работала {execution_time:.2f} секунды")
        
        return result
    return wrapper


@timer
def calculate_sum(n):
    return sum(range(n))



# Проверка основного задания

result = calculate_sum(1_000_000)
print(result)
