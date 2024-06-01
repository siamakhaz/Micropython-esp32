import socket
import os
import json
import base64

def read_html_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def read_binary_file(filepath):
    with open(filepath, 'rb') as file:
        return file.read()

def format_size(size):
    for unit in ['bytes', 'KB', 'MB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} MB"

def get_storage_stats():
    stats = os.statvfs('/')
    total = stats[0] * stats[2]
    free = stats[0] * stats[3]
    used = total - free
    return f"Total: {format_size(total)}, Used: {format_size(used)}, Free: {format_size(free)}"

def send_response_header(client, content_type):
    client.send(b'HTTP/1.0 200 OK\r\n')
    client.send(f'Content-type: {content_type}\r\n'.encode())
    client.send(b'\r\n')

def send_file_content(client, filepath):
    with open(filepath, 'rb') as file:
        while True:
            chunk = file.read(1024)
            if not chunk:
                break
            client.sendall(chunk)

def handle_client(cl, addr):
    cl_file = cl.makefile('rwb', 0)
    request = cl_file.readline().decode()

    if 'POST /test' in request:
        print("POST request received for /test")
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        test_html = read_html_file('html/test.html')
        cl.send(b'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(test_html.encode())
        print("Test file sent successfully")

    elif 'POST /' in request:
        print("POST request received")
        content_length = 0

        while True:
            line = cl_file.readline().decode().strip()
            if line.startswith('Content-Length:'):
                content_length = int(line.split(':')[1].strip())
                print(f"Content-Length: {content_length}")
            if line == '':
                break

        if content_length > 0:
            body = cl_file.read(content_length).decode('utf-8')
            data = json.loads(body)
            filename = data['filename']
            file_content = base64.b64decode(data['content'])

            with open(filename, 'wb') as f:
                f.write(file_content)

            cl.send(b'HTTP/1.0 200 OK\r\nContent-type: text/plain\r\n\r\n')
            cl.send(file_content)
            print(f"File {filename} uploaded successfully")
        else:
            cl.send(b'HTTP/1.0 400 Bad Request\r\nContent-type: text/html\r\n\r\n')
            cl.send(b"<html><body><h1>File upload failed!</h1></body></html>")
            print("File upload failed")
            
    elif 'GET /storage' in request:
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        print("GET request received for /storage")
        storage_stats = get_storage_stats()
        cl.send(b'HTTP/1.0 200 OK\r\nContent-type: text/plain\r\n\r\n')
        cl.send(storage_stats.encode())
        print("Storage stats sent successfully")
        
    elif 'GET /html/test.html' in request:
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        test_html = read_html_file('html/test.html')
        cl.send(b'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(test_html.encode())
        print("Test file sent successfully")
        
    elif request.startswith('GET /html/static/'):
        print("GET request received for static file")
        filepath = request.split(' ')[1][1:]  # Remove leading '/'
        print(filepath)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        try:
            if filepath.endswith('.css'):
                content_type = 'text/css'
            elif filepath.endswith('.js'):
                content_type = 'application/javascript'
            elif filepath.endswith('.png'):
                content_type = 'image/png'
            else:
                content_type = 'application/octet-stream'
            
            send_response_header(cl, content_type)
            send_file_content(cl, filepath)
            print(f"Static file {filepath} sent successfully")
        except Exception as e:
            cl.send(b'HTTP/1.0 404 Not Found\r\nContent-type: text/html\r\n\r\n')
            cl.send(b"<html><body><h1>File not found!</h1></body></html>")
            print(f"Failed to read static file {filepath}: {e}")

    else:
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        html = read_html_file('html/index.html')
        cl.send(b'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(html.encode())

    cl.close()

def start_server(html):
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)

    while True:
        try:
            cl, addr = s.accept()
            print('Client connected from', addr)
            handle_client(cl, addr)
        except OSError as e:
            print(f"OSError: {e}")
        except Exception as e:
            print(f"Error: {e}")
