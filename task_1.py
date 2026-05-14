from queue import Queue
import time

request_queue = Queue()
request_id = 1

def generate_request():
    global request_id
    request = f"Заявка #{request_id}"
    request_queue.put(request)
    print(f"Створено: {request}")
    request_id += 1

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробляється: {request}")
    else:
        print("Черга пуста")

while True:
    generate_request()
    process_request()

    choice = input("Натисніть Enter, щоб продовжити, або q для виходу: ")

    if choice.lower() == "q":
        break

    time.sleep(1)
    