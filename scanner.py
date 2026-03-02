import socket  # Importamos la librería socket, necesaria para trabajar con conexiones de red

# Configuración de la IP y rango de puertos
ip_objetivo = '127.0.0.1'   # Usamos localhost (tu propia máquina) para evitar problemas legales
puerto_inicio = 1           # Puerto inicial del escaneo
puerto_fin = 200            # Puerto final del escaneo

# Mensaje inicial informando qué se va a escanear
print(f'Escaneando {ip_objetivo} de puerto {puerto_inicio} a {puerto_fin}...')
print('-' * 50)

# Lista para guardar los puertos abiertos encontrados
puertos_abiertos = []

# Bucle que recorre todos los puertos en el rango definido
for puerto in range(puerto_inicio, puerto_fin + 1):
    try:
        # Crear un socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
        socket_conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Definimos un tiempo máximo de espera de 2 segundos para evitar bloqueos
        socket_conexion.settimeout(2)

        # Intentamos conectar al puerto actual en la IP objetivo
        resultado = socket_conexion.connect_ex((ip_objetivo, puerto))

        # Si resultado == 0 significa que el puerto está abierto
        if resultado == 0:
            print(f'[+] Puerto {puerto}: ABIERTO')
            puertos_abiertos.append(puerto)  # Guardamos el puerto abierto en la lista

            # Intentamos capturar el banner del servicio
            try:
                banner = socket_conexion.recv(1024)  # Recibimos hasta 1024 bytes
                banner_texto = banner.decode('utf-8', errors='ignore').strip()  # Decodificamos a texto

                # Si el banner contiene información, la mostramos
                if banner_texto:
                    print(f'    Banner: {banner_texto}')
                else:
                    print('    Banner: No disponible')
            except Exception:
                # Si ocurre un error al capturar el banner, lo indicamos
                print('    Banner: No capturado')

        # Cerramos el socket después de cada intento
        socket_conexion.close()

    except Exception as e:
        # Si ocurre un error inesperado, lo mostramos
        print(f'[-] Error en puerto {puerto}: {e}')

# Línea divisoria al terminar el escaneo
print('-' * 50)

# Mensaje final con resumen del escaneo
print('[+] Escaneo completado.')

# Mostramos los puertos abiertos encontrados
if puertos_abiertos:
    print(f'Puertos abiertos encontrados: {puertos_abiertos}')
else:
    print('No se encontraron puertos abiertos en el rango especificado.')
