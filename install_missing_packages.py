import os
import subprocess
import sys
import importlib.metadata

# Función para instalar paquetes
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Buscar librerías importadas en los archivos Python del proyecto
def find_imports(directory):
    imports = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    for line in f:
                        if line.startswith("import") or line.startswith("from"):
                            # Extraer el nombre de la librería importada
                            parts = line.split()
                            if len(parts) > 1:  # Asegurarse de que la línea tenga suficiente contenido
                                if "import" in parts:
                                    imports.add(parts[1].split('.')[0])
                                elif "from" in parts:
                                    imports.add(parts[1].split('.')[0])
    return imports

# Directorio del proyecto
project_directory = os.path.dirname(os.path.abspath(__file__))

# Detectar las librerías importadas
imported_packages = find_imports(project_directory)

# Obtener los paquetes instalados
installed_packages = {pkg.metadata['Name'].lower() for pkg in importlib.metadata.distributions()}

# Instalar las librerías que faltan
missing_packages = imported_packages - installed_packages

if missing_packages:
    print(f"Faltan {len(missing_packages)} librerías. Instalando...")
    for package in missing_packages:
        try:
            print(f"Instalando {package}...")
            install(package)
        except Exception as e:
            print(f"No se pudo instalar {package}: {e}")
else:
    print("Todas las librerías necesarias ya están instaladas.")
