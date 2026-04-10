import time
import random

# Lista de IPs para simular tráfego, incluindo o alvo do filtro
ips = ['192.168.0.1', '10.0.0.5', '172.16.0.10', '16.180.70.237', '200.150.10.5']
methods = ['GET', 'POST', 'DELETE']
resources = ['/home', '/login', '/products', '/cart', '/api/v1/data']

def generate_log_line():
    ip = random.choice(ips)
    method = random.choice(methods)
    resource = random.choice(resources)
    timestamp = time.strftime('%d/%b/%Y:%H:%M:%S', time.localtime())
    return f'{ip} - - [{timestamp}] "{method} {resource} HTTP/1.1" 200 {random.randint(100, 5000)}\n'

print("Iniciando geração de logs em /tmp/access_log...")
while True:
    with open('/tmp/access_log', 'a') as f:
        line = generate_log_line()
        f.write(line)
    time.sleep(random.uniform(0.1, 1.0)) # Simula tráfego irregular

    #Esse codigo nao foi criado por mim, foi diponibilizado pela intituição FIAP na aula de Streaming
