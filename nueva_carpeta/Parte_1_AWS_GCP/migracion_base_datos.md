# Migración de MySQL a Cloud SQL

## Pasos Detallados
1. **Planificación de la Migración**
   - Evaluar el tamaño y la complejidad de la base de datos.
   - Establecer un cronograma y un plan de contingencia.

2. **Exportación de Datos**
   - Usar `mysqldump` para exportar la base de datos:
     ```bash
     mysqldump -u usuario -p base_de_datos > backup.sql
     ```

3. **Importación en Cloud SQL**
   - Subir el archivo `backup.sql` a Google Cloud Storage.
   - Importar en Cloud SQL mediante la consola o el comando `gcloud`:
     ```bash
     gcloud sql import sql INSTANCE_NAME gs://BUCKET_NAME/backup.sql
     ```

4. **Verificación de la Integridad de los Datos**
   - Comparar el conteo de filas y realizar consultas de muestra en ambas bases de datos.
