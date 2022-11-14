# Librería.
from win10toast import ToastNotifier

# Características notificación.
TITULO = "¡Holaaa!"
MENSAJE = "Que tengas una bonita tarde <3"
ICONO = "./bruja.ico"
DURACION = 5 #segs

# Crear y mostrar notificación.
notificacion = ToastNotifier()
notificacion.show_toast(title=TITULO, msg=MENSAJE, icon_path=ICONO, duration=DURACION)
