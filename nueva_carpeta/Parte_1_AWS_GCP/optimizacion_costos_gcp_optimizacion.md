# Optimización de Costos en GCP

## Recomendaciones
1. **Compute Engine**
   - Usar instancias preemptibles para cargas de trabajo temporales.
   - Revisar el tamaño y tipo de instancia para ajustarlo a las necesidades reales.

2. **Cloud Storage**
   - Configurar reglas de ciclo de vida para mover objetos antiguos a almacenamiento Nearline o Coldline.
   - Utilizar almacenamiento regional o multirregional según la necesidad.

3. **Cloud SQL**
   - Ajustar el tamaño de la instancia y utilizar réplicas de lectura para aliviar la carga.
