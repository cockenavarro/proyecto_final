import netCDF4 as nc

# 1. Abrir el archivo NetCDF
ruta_archivo = "C:/PROYECTOS VSC/PROYECTO_FINAL/app/archivos_netCDF/temperaturas/CR2MET_t2m_v2.0_mon_1979_2019_005deg.nc"
archivo_nc = nc.Dataset(ruta_archivo)

# 2. Acceder a la variable de temperatura
# Supongamos que la variable de temperatura se llama 'temperatura'
temperatura = archivo_nc.variables['t2m'][:]

# 3. Calcular la temperatura máxima
temperatura_maxima = temperatura.max()

# 4. Obtener el valor máximo de temperatura
print("La temperatura máxima es:", temperatura_maxima)

# Cerrar el archivo NetCDF
archivo_nc.close()
