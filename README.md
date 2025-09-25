# 📚 Proyecto Biblioteca – Pruebas Top Down con Stubs

## 📖 Descripción

Este proyecto implementa un sistema de gestión de biblioteca con enfoque de **pruebas Top-Down**. Se valida el caso de uso principal "prestar libro", utilizando stubs que simulan los módulos de autenticación y base de datos.

El objetivo es probar primero la lógica de negocio sin necesidad de implementar aún los servicios reales (DB y autenticación).

## 🏗️ Estructura del Proyecto

```
proyecto_biblioteca/
├── biblioteca_sistema.py      # Sistema principal (lógica de negocio)
├── test_top_down.py           # Pruebas unitarias con pytest
└── stubs/                     # Carpeta de stubs simulados
    ├── __init__.py
    ├── auth_stub.py           # Stub de autenticación
    └── database_stub.py       # Stub de base de datos
```

## ⚙️ Funcionamiento del Sistema

### 🔹 BibliotecaSistema

Clase principal que orquesta el proceso de préstamo de un libro:

1. **Verificar usuario** → mediante `AuthStub`
2. **Verificar disponibilidad del libro** → mediante `DatabaseStub`
3. **Registrar el préstamo** → simulado en el `DatabaseStub`

#### Mensajes posibles:
- `"Usuario no autorizado"` → usuario con ID ≤ 0
- `"Libro no disponible"` → libro con ID impar o no existente
- `"Préstamo exitoso"` → usuario válido (ID > 0) y libro disponible (ID par)

### 🔹 Stubs

**AuthStub**: autoriza usuarios con ID > 0

**DatabaseStub**:
- **Libros disponibles**: ID par (2, 4, 6, 8...)
- **Libros no disponibles**: ID impar (1, 3, 5, 7...)
- Registra préstamos de manera simulada (sin acceso real a BD)

### 🔹 Pruebas (test_top_down.py)

Se implementaron **4 pruebas unitarias** con pytest utilizando el patrón **AAA** (Arrange, Act, Assert):

#### ✅ Pruebas básicas de flujo
- **`test_prestamo_exitoso`** → usuario válido (ID=1) y libro disponible (ID=2)
- **`test_usuario_no_autorizado`** → usuario inválido (ID=0)

#### ✅ Pruebas avanzadas de validación
- **`test_libro_no_disponible`** → libro con ID impar (no disponible según stub)
- **`test_no_registro_si_no_disponible`** → verifica que no se registre préstamo si el libro no está disponible (usa `monkeypatch`)

## ▶️ Ejecución de Pruebas

### 1. Instalar dependencias

En la raíz del proyecto:

```bash
python -m pip install --upgrade pip
python -m pip install pytest
```

### 2. Ejecutar las pruebas

Use el siguiente comando:

```bash
python -m pytest test_top_down.py -v --tb=short
```

### 3. Resultado esperado

```
================= test session starts =================
test_top_down.py::test_prestamo_exitoso PASSED            [25%]
test_top_down.py::test_usuario_no_autorizado PASSED       [50%]
test_top_down.py::test_libro_no_disponible PASSED         [75%]
test_top_down.py::test_no_registro_si_no_disponible PASSED [100%]
================= 4 passed in 0.05s =================
```

## 🧪 Casos de Prueba Implementados

### Prueba 1: `test_prestamo_exitoso`
```python
# Usuario válido (ID=1) + Libro disponible (ID=2)
resultado = sistema.prestar_libro(usuario_id=1, libro_id=2)
assert resultado == "Préstamo exitoso"
```

### Prueba 2: `test_usuario_no_autorizado`  
```python
# Usuario inválido (ID=0) + Cualquier libro
resultado = sistema.prestar_libro(usuario_id=0, libro_id=2)
assert resultado == "Usuario no autorizado"
```

### Prueba 3: `test_libro_no_disponible`
```python
# Usuario válido (ID=1) + Libro no disponible (ID=3, impar)
resultado = sistema.prestar_libro(usuario_id=1, libro_id=3)
assert resultado == "Libro no disponible"
```

### Prueba 4: `test_no_registro_si_no_disponible` (con monkeypatch)
```python
# Verifica que NO se llame a registrar_prestamo si el libro no está disponible
# Usa monkeypatch para interceptar la llamada al método
resultado = sistema.prestar_libro(usuario_id=1, libro_id=3)
assert resultado == "Libro no disponible"
assert llamado_registrar["count"] == 0  # No debe registrarse
```

## 🏆 Beneficios del Enfoque Top Down

- **Permite probar la lógica principal primero**
- **Se reemplazan dependencias externas** por stubs simples y deterministas
- **Facilita feedback temprano** sin necesidad de una base de datos ni sistema de autenticación real
- **Reduce costo y tiempo** en las primeras etapas de desarrollo
- **Validación completa del flujo** incluyendo casos de error y edge cases
- **Uso de mocking avanzado** con `monkeypatch` para verificar que no se ejecuten operaciones innecesarias

## 📷 Captura de Pantalla

<img width="825" height="311" alt="image" src="https://github.com/user-attachments/assets/762fe6ee-b437-4fa8-be8f-0fbe45533198" />

