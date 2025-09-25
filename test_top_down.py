import pytest
from biblioteca_sistema import BibliotecaSistema
from stubs.database_stub import DatabaseStub
from stubs.auth_stub import AuthStub

def test_prestamo_exitoso():
    """Prueba el flujo exitoso usando stubs"""
    # ARRANGE: Configurar stubs
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    # ACT: Ejecutar operación
    resultado = sistema.prestar_libro(usuario_id=1, libro_id=2)

    # ASSERT: Verificar resultado
    assert resultado == "Préstamo exitoso"

def test_usuario_no_autorizado():
    """Prueba rechazo por usuario no autorizado"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado = sistema.prestar_libro(usuario_id=0, libro_id=2)
    assert resultado == "Usuario no autorizado"
    
def test_libro_no_disponible():
    from biblioteca_sistema import BibliotecaSistema
    from stubs.database_stub import DatabaseStub
    from stubs.auth_stub import AuthStub

    sistema = BibliotecaSistema(DatabaseStub(), AuthStub())
    # 3 es impar → no disponible en el stub
    assert sistema.prestar_libro(usuario_id=1, libro_id=3) == "Libro no disponible"

def test_no_registro_si_no_disponible(monkeypatch):
    from biblioteca_sistema import BibliotecaSistema
    from stubs.database_stub import DatabaseStub
    from stubs.auth_stub import AuthStub

    db = DatabaseStub()
    llamado_registrar = {"count": 0}
    monkeypatch.setattr(db, "registrar_prestamo", lambda *_: llamado_registrar.__setitem__("count", llamado_registrar["count"]+1))

    sistema = BibliotecaSistema(db, AuthStub())
    assert sistema.prestar_libro(usuario_id=1, libro_id=3) == "Libro no disponible"
    assert llamado_registrar["count"] == 0  # no debe registrarse
