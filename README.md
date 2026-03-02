# 🔍 Port Scanner + Banner Grabber (Localhost)

Este proyecto es una herramienta en Python que permite escanear puertos en una IP objetivo y capturar banners de los servicios que se ejecutan en ellos.  
En esta versión, la IP objetivo está configurada como **localhost (127.0.0.1)**, lo que significa que el escaneo se realiza únicamente sobre tu propia máquina, garantizando seguridad y evitando problemas legales.

---

## ⚙️ Cómo funciona

1. El script recorre los puertos del **1 al 200** en la dirección `127.0.0.1`.
2. Usa la función `connect_ex()` de la librería `socket` para verificar si un puerto está abierto.
3. Si el puerto está abierto:
   - Intenta capturar el **banner** del servicio con `recv(1024)`.
   - Aplica un **timeout de 2 segundos** para evitar bloqueos.
4. Muestra resultados claros en pantalla:
   - Lista de puertos abiertos.
   - Banner capturado (si está disponible).
5. Al final, imprime un resumen con todos los puertos abiertos encontrados.

---

## 📦 Requisitos

- Python 3.x
- Librería estándar `socket` (ya incluida en Python, no requiere instalación adicional).

---

## ▶️ Ejecución

1. Guarda el script en un archivo, por ejemplo:  
   	scanner.py
2. Ejecuta el script desde la terminal:
	python port_scanner.py
3. El programa escaneará automáticamente la IP 127.0.0.1 en el rango de puertos 1–200.

## 📊 Ejemplo de salida
Supongamos que tienes un servidor HTTP corriendo en el puerto 8080 y un servicio SSH en el puerto 22. La salida podría verse así:

Escaneando 127.0.0.1 de puerto 1 a 200...
--------------------------------------------------

[+] Puerto 22: ABIERTO
    Banner: SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5

[+] Puerto 80: ABIERTO
    Banner: HTTP/1.1 400 Bad Request
    Date: Mon, 02 Mar 2026 15:00:00 GMT
    Server: SimpleHTTP/0.6 Python/3.10.12

--------------------------------------------------
[+] Escaneo completado.
Puertos abiertos encontrados: [22, 80]

## ⚠️ Nota importante
Este script está configurado para escanear solo localhost (127.0.0.1).

No lo uses en sistemas externos sin autorización, ya que podría considerarse un ataque de red.

Es ideal para prácticas de ciberseguridad y para aprender cómo funcionan los escáneres de puertos y el banner grabbing.

Ejemplo educativo de Port Scanner + Banner Grabber en Python, adaptado para uso seguro en localhost.
