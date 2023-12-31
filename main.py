import socket

URLS = {
    '/': 'hello world',
    '/index': 'hello index',
}


def generate_headers(method, url):
    if method != 'GET':
        return 'HTTP/1.1 405 Method not allowed\n\n', 405
    if url not in URLS:
        return 'HTTP/1.1 404 Not found\n\n', 404

    return 'HTTP/1.1 200 OK\n\n', 200


def generate_response(request):
    method, url = request.split(' ')[:2]
    headers, code = generate_headers(method, url)
    return (headers + 'Hello, World!').encode()


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8000))

    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(request)

        response = generate_response(request.decode('utf-8'))

        client_socket.sendall(response)
        client_socket.close()


if __name__ == '__main__':
    run()
