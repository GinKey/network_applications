import socket
import threading


def proc(n):
	while True:
		sock = socket.socket()
		print("Запуск сервера")
		sock.bind(('', int(n)))
		print("Начало прослушивания порта\n")
		sock.listen(1)
		conn, addr = sock.accept()
		print("Клиент подключен")
		print(addr)
		msg = ''
		data = conn.recv(2048)
		print("Прием данных от клиента")
		if not data:
			break
		msg += data.decode()
		print("Отправка данных клиенту")
		conn.send(data)
		if not data:
			break
	print("Отключение клиента")
	print(msg)
	conn.close()
	print("Остановка сервера")


p1 = threading.Thread(target=proc, name="t1", args=["101"])
p2 = threading.Thread(target=proc, name="t2", args=["102"])
p1.start()
p2.start()
