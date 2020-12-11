import time

def timing(get_response):
    # Единовременная настройка и инициализация.
    def middleware(request):
        # Код должен быть выполнен для каждого запроса
        # до view
        t1 = time.time()
        response = get_response(request)
        # Код должен быть выполнен ответа после view
        t2 = time.time()
        print("TOTAL TIME:", (t2 - t1))
        return response
    return middleware
