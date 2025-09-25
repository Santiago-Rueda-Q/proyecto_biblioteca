class BibliotecaSistema:
    def __init__(self, db, auth):
        self.db = db      # Inyección de dependencia (stub o real)
        self.auth = auth  # Inyección de dependencia (stub o real)

    def prestar_libro(self, usuario_id, libro_id):
        # Paso 1: verificar autorización
        if not self.auth.verificar_usuario(usuario_id):
            return "Usuario no autorizado"

        # Paso 2: verificar disponibilidad
        if not self.db.libro_disponible(libro_id):
            return "Libro no disponible"

        # Paso 3: registrar préstamo
        ok = self.db.registrar_prestamo(usuario_id, libro_id)
        if not ok:
            return "Error al registrar préstamo"

        return "Préstamo exitoso"
