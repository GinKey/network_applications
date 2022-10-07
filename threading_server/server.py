import socket
import threading


def proc(n):
	while True:
		sock = socket.socket()
		print("Запуск сервера")
		sock.bind(('', 100+ int(n)))
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

	print("Отключение клиента")
	print(msg)
	conn.close()
	print("Остановка сервера")


p1 = threading.Thread(target=proc, name="t1", args=["1"])
p2 = threading.Thread(target=proc, name="t2", args=["2"])
p1.start()
p2.start()
