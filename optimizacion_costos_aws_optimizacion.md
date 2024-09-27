# Optimización de Costos en AWS

## Recomendaciones
1. **Instancias EC2**
   - Cambiar a instancias reservadas si se usan a largo plazo.
   - Usar instancias spot para cargas de trabajo flexibles.

2. **S3**
   - Utilizar la clase de almacenamiento de S3 más adecuada (por ejemplo, S3 Infrequent Access).
   - Configurar políticas de ciclo de vida para mover datos a almacenamiento más barato.

3. **RDS**
   - Ajustar el tamaño de la instancia a lo necesario y desactivar los backups automáticos si no se requieren.
