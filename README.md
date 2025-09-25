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
- `"Usuario no autorizado"` → usuario inválido
- `"Libro no disponible"` → libro no apto para préstamo
- `"Préstamo exitoso"` → flujo correcto

### 🔹 Stubs

**AuthStub**: autoriza usuarios con ID > 0

**DatabaseStub**:
- Libros con ID par están disponibles
- Registra préstamos de manera simulada (sin acceso real a BD)

### 🔹 Pruebas (test_top_down.py)

Se implementaron pruebas con pytest:

- ✅ `test_prestamo_exitoso` → usuario válido y libro disponible
- ✅ `test_usuario_no_autorizado` → usuario inválido

*(puede extenderse con casos de libro no disponible, errores de registro, etc.)*

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
test_top_down.py::test_prestamo_exitoso PASSED       [50%]
test_top_down.py::test_usuario_no_autorizado PASSED  [100%]
================= 2 passed in 0.03s =================
```

## 🏆 Beneficios del Enfoque Top Down

- **Permite probar la lógica principal primero**
- **Se reemplazan dependencias externas** por stubs simples y deterministas
- **Facilita feedback temprano** sin necesidad de una base de datos ni sistema de autenticación real
- **Reduce costo y tiempo** en las primeras etapas de desarrollo

## 📷 Captura de Pantalla

<img width="799" height="254" alt="image" src="https://github.com/user-attachments/assets/0611e9f2-7e99-43ee-959b-8cf69862590f" />

