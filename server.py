#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Создаем сокет
# Хост — оставдяем строку пустой, чтобы наш сервер был доступен для всех интерфейсов
# Порт указан в задании
sock.bind(('', 8000)) # Связываем наш сокет с данными хостом и портом
sock.listen(1) # Запускаем для данного сокета режим прослушивания
# Метод принимает один аргумент — максимальное количество подключений в очереди


while True:    
    # Принимаем подключение с помощью метода, возвращающего кортеж - новый сокет и адрес клиента
    # Этот сокет и будет использоваться для приема и посылке клиенту данных
    conn, addr = sock.accept()
    request = conn.recv(1024) # Получаем (читаем) данные
    print(request)
    if not request:  
        break
    requestArr = request.decode().split("\n", 1)[0]
    url = requestArr.split(" ")[1]
 
    if url == "/":
        page_name = "./index.html"
    elif url == "/index.html":
        page_name = "./index.html"
    elif url == "/about/aboutme.html":
        page_name = "./about/aboutme.html"
    else:
        page_name = "404.html"
    
    f=open(page_name,'rb')

    # Возвращаем клтенту данные
    conn.send(("HTTP/1.1 200 OK\nContent-Type: text/html\nServer: my_server\n\n\n").encode() + f.read())
    f.close()
# Закрываем соединение
conn.close()
sock.close()
