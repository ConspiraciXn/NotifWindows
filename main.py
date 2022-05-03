# Librerias. ====================================================================
import time
from win10toast import ToastNotifier

# Constantes. ===================================================================
TITULO = "¡Hola!"
MENSAJE = "Bonita tarde <3"
ICONO = "./finn.ico"
DURACION = 10 #segs

# Objeto Notificacion. ==========================================================
notificacion = ToastNotifier()
notificacion.show_toast(title=TITULO, msg=MENSAJE, icon_path=ICONO, duration=DURACION)

# Esperar notificaciones en hilo. ================================================
while notificacion.notification_active(): time.sleep(0.1)