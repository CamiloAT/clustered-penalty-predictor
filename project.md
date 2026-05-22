##### PREDICCIÓN Y ANÁLISIS DE PENALES EN FÚTBOL MEDIANTE MACHINE

##### LEARNING

##### AGUIRRE TENJO DIEGO FERNANDO

##### ARIAS TENJO CAMILO ANDRES

##### APLICACIONES WEB PROGRESIVAS

##### INGENIERA:

##### VIVIANA ALEXANDRA VILLANUEVA CIPAGAUTA

##### UNIVERSIDAD PEDAGÓGICA Y TECNOLÓGICA DE COLOMBIA

##### FACULTAD DE INGENIERÍA

##### INGENIERÍA DE SISTEMAS Y COMPUTACIÓN

##### 21/04/


- 1. Título del proyecto.....................................................................................................................
- 2. Planteamiento del problema.....................................................................................................
- 3. Pregunta problema....................................................................................................................
- 4. Objetivo general.........................................................................................................................
- 5. Objetivos específicos..................................................................................................................
- 6. Metodología propuesta..............................................................................................................
   - Fase 1 – Comprensión del negocio y del problema...................................................................
   - Fase 2 – Adquisición y comprensión de los datos.....................................................................
   - Fase 3 – Preparación de los datos..............................................................................................
   - Fase 4 – Modelado no supervisado............................................................................................
   - Fase 5 – Modelado supervisado.................................................................................................
    - Fase 6 – Evaluación...................................................................................................................
    - Fase 7 – Despliegue de API REST..........................................................................................
    - Fase 8 – Desarrollo del Frontend Web.....................................................................................
    - Fase 9 – Documentación y socialización...................................................................................
- 7. Planteamiento inicial del software............................................................................................
   - Requerimientos funcionales.......................................................................................................
- 8. Técnicas de Machine Learning propuestas.............................................................................
   - Supervisado – Clasificación multiclase.....................................................................................
      - Variables de entrada (features – X)......................................................................................
      - Variable objetivo (target – Y)..............................................................................................
   - No supervisado – Agrupamiento (Clustering)...........................................................................
      - Variables de entrada para clustering....................................................................................
- 9. Arquitectura propuesta.............................................................................................................
    - Capa 1 – Ingesta y preprocesamiento........................................................................................
    - Capa 2 – Modelado dual (Pipeline ML)....................................................................................
    - Capa 3 – Evaluación y predicción.............................................................................................
    - Capa 4 – API REST (FastAPI).................................................................................................
    - Capa 5 – Frontend Web...........................................................................................................
    - Tecnologías................................................................................................................................
- 10. Cronograma............................................................................................................................
- Referencias....................................................................................................................................


## 1. Título del proyecto.....................................................................................................................

Predicción y Análisis de Penales en Fútbol mediante un Pipeline de Machine Learning:
Clasificación Supervisada del Resultado y Descubrimiento de Perfiles de Cobro mediante
Clustering.

## 2. Planteamiento del problema.....................................................................................................

El fútbol es el deporte más popular del mundo, y dentro de sus múltiples situaciones de juego, el
tiro penal representa uno de los momentos de mayor tensión emocional, psicológica y
estratégica. En su concepción más básica, el penal parece ser una situación asimétrica y
relativamente simple a favor del atacante (un jugador frente al portero, a 11 metros de distancia,
sin obstáculos y con el control total del balón). Estadísticamente, la ventaja es innegable, ya que
entre el 70% y el 80% de los penales en torneos de alto nivel terminan en gol; sin embargo, la
paradoja de esta situación radica en que, en instancias decisivas como rondas eliminatorias,
semifinales o finales de torneos mundiales, esta tasa de efectividad puede descender
drásticamente (Morya et al., 2003). Esta caída en el rendimiento evidencia que el desenlace de un
penal está determinado por una cantidad significativa de factores que van mucho más allá del
talento técnico individual del jugador (Jordet et al., 2007).
El comportamiento humano bajo niveles extremos de estrés no es aleatorio, sino que tiende a
refugiarse en patrones predecibles. Desde la perspectiva de la Teoría de Juegos, la estrategia
óptima para un cobrador sería alcanzar la imprevisibilidad total, distribuyendo sus tiros de
manera aleatoria en las distintas zonas del arco para que el portero no pueda anticipar la
dirección. No obstante, las limitaciones cognitivas y biomecánicas del ser humano impiden
alcanzar esta verdadera aleatoriedad. Bajo presión, los jugadores desarrollan sesgos
subconscientes: tienden a asegurar el disparo hacia el lado natural de su pierna hábil, evitan
realizar tiros altos por el miedo al escarnio público de fallar por completo la portería, y sus
posturas corporales previas al impacto (como la orientación del pie de apoyo o la apertura de los
brazos) revelan milisegundos antes la trayectoria del balón.
A pesar de que estos sesgos son observables y cuantificables, en el entorno profesional actual la
toma de decisiones sigue estando rezagada. Hoy en día, los cuerpos técnicos y analistas


deportivos aún toman decisiones sobre la elección de los cobradores y el orden de ejecución en
tandas de penales de forma mayoritariamente empírica e intuitiva. Si bien es cierto que existe
una abundancia masiva de datos y métricas disponibles en las principales ligas gracias a la
recolección de eventos con coordenadas exactas y cinemática, la explotación analítica de esta
información suele limitarse a la estadística descriptiva básica. No existe en el mercado actual una
herramienta de apoyo computacional ampliamente adoptada que integre múltiples fuentes de
información compleja (como la fatiga acumulada, las tácticas de distracción psicológica del
portero y la presión del marcador) para brindar una predicción objetiva y probabilística sobre el
desenlace de un penal, ni que descubra automáticamente perfiles de comportamiento entre los
cobradores (Rein & Memmert, 2016).
Es en esta brecha analítica donde radica el problema central: la incapacidad humana para
procesar simultáneamente múltiples variables no lineales en tiempo real. Esto sugiere de manera
concluyente que variables contextuales e históricas (como la presión específica del torneo, el
minuto exacto del partido, el historial previo de enfrentamientos directos entre el cobrador y un
portero específico, o la pierna hábil del ejecutante) tienen una influencia real, medible y
predecible en el resultado final. Desde la perspectiva de la ciencia de datos y el aprendizaje
automático (Machine Learning), este problema no resuelto presenta dos dimensiones
complementarias y de altísima relevancia tanto académica como práctica:
La primera dimensión corresponde a la predicción directa del evento mediante aprendizaje
supervisado. La interrogante científica es clara: dado un conjunto estructurado de variables
conocidas estrictamente antes del silbato del árbitro (perfil biomecánico del cobrador,
características de atajada del portero, contexto temporal del partido, factor de presión de la fase
del torneo y el marcador), ¿es posible entrenar un modelo computacional que prediga con alta
precisión si el penal terminará en gol, fallo o atajada?. La resolución empírica de esta pregunta se
plantea a través de una tarea de clasificación multiclase, lo que permite la aplicación y
evaluación de algoritmos de ensamble, tales como Random Forest, o
modelos base como la Regresión Logística (Géron, 2022). Estos modelos tienen la capacidad
matemática de encontrar relaciones ocultas, descubriendo dinámicas no lineales complejas de los
deportistas bajo presión.


La segunda dimensión aborda la falta de categorización objetiva de los ejecutantes mediante el
descubrimiento de patrones ocultos a través del aprendizaje no supervisado. La literatura actual
suele tratar a los cobradores como individuos aislados, pero la pregunta de investigación plantea:
¿existen grupos estructurales de cobradores que comparten características biomecánicas,
psicológicas y contextuales similares, aunque a simple vista parezcan de perfiles futbolísticos
totalmente distintos?. La identificación de estos clústeres a través de algoritmos como K-Means
puede revelar patrones latentes que los analistas humanos, limitados por sus propios sesgos de
observación, no logran detectar al revisar horas de video o bases de datos manualmente (Hastie
et al., 2020). Este enfoque permitiría clasificar a los jugadores en perfiles psicológicos de cobro
independientemente de su posición nominal en el campo de juego.
En síntesis, el problema central que motiva la formulación de este proyecto de investigación
aplicada es la notable ausencia de herramientas de Machine Learning capaces de integrar
dinámicamente datos contextuales, históricos y biomecánicos para predecir el resultado de un
penal y descubrir perfiles ocultos de comportamiento entre los ejecutantes. La dependencia de la
intuición humana en un escenario de alta tensión resulta anticuada frente a las capacidades
tecnológicas actuales. La solución propuesta busca llenar ese vacío mediante el diseño y
desarrollo de un pipeline algorítmico robusto que combine clasificación supervisada y
agrupamiento no supervisado, siguiendo estrictamente las mejores prácticas metodológicas del
ciclo de vida de los proyectos de ciencia de datos (Géron, 2022; Hastie et al., 2020). Este
desarrollo tiene aplicaciones reales, directas y comprobables en la preparación táctica de los
equipos, la formación integral de jugadores y la planificación estratégica algorítmica de las
tandas de penales en torneos decisivos a nivel mundial (Duch et al., 2010).

## 3. Pregunta problema....................................................................................................................

¿Es posible desarrollar un pipeline de Machine Learning que, a partir de variables contextuales,
históricas y biomecánicas de los cobros de penal en fútbol de alto rendimiento, prediga el
resultado de un penal (gol, fallo o atajada) y descubra automáticamente perfiles de
comportamiento entre los ejecutantes, superando la toma de decisiones intuitiva de los cuerpos
técnicos?


## 4. Objetivo general.........................................................................................................................

Desarrollar un pipeline de Machine Learning que integre un modelo de aprendizaje no
supervisado para la identificación de perfiles de cobro y un modelo de aprendizaje supervisado
para la predicción del resultado de penales en fútbol de alto rendimiento, a partir de datos
históricos, contextuales y biomecánicos, con el fin de apoyar la toma de decisiones tácticas de
los cuerpos técnicos.

## 5. Objetivos específicos..................................................................................................................

```
● Recopilar, documentar y preprocesar un dataset representativo de penales ejecutados en
competencias de alto nivel, incluyendo variables contextuales, históricas y biomecánicas
de los cobradores y porteros.
● Implementar y evaluar un modelo de agrupamiento no supervisado (K-Means) para
identificar clústeres de cobradores con comportamientos similares bajo presión,
asignando un perfil de cobro a cada jugador.
● Diseñar y entrenar un modelo de clasificación supervisada (Random Forest) que integre
el perfil de clúster como variable adicional para predecir el resultado del penal.
● Evaluar el desempeño de ambos modelos mediante métricas adecuadas (accuracy,
precisión, recall y F1-score para el supervisado; índice de silueta e inercia para el no
supervisado) y realizar un análisis crítico de los resultados.
● Desarrollar un módulo de software modular y reproducible que implemente el pipeline
completo, desde la ingesta de datos hasta la generación de predicciones, con instrucciones
claras de ejecución.
```
## 6. Metodología propuesta..............................................................................................................

El proyecto seguirá una metodología basada en el ciclo CRISP-DM (Cross-Industry Standard Process for
Data Mining), que es el estándar más ampliamente adoptado en proyectos de ciencia de datos y Machine
Learning (Schröer et al., 2021), adaptada al contexto académico y a los requisitos del proyecto final:

### Fase 1 – Comprensión del negocio y del problema...................................................................


Definición del contexto deportivo, identificación de las variables relevantes y delimitación del alcance del
sistema. Se revisará literatura especializada sobre el análisis cuantitativo del fútbol (Rein & Memmert,
2016).

### Fase 2 – Adquisición y comprensión de los datos.....................................................................

Recopilación del dataset desde fuentes abiertas (Kaggle, StatsBomb o FBref). Documentación del origen,
estructura y significado de cada variable. Análisis exploratorio de datos (EDA) para entender la
distribución, correlaciones y valores atípicos.

### Fase 3 – Preparación de los datos..............................................................................................

Imputación de valores nulos en variables contextuales, aumento de datos sintéticos (Steps_Run,
Time_Taken) basado en reglas de dominio, y cálculo de métricas derivadas (Stress_Index,
Team_Effectiveness, Keeper_Save_Rate). Codificación de variables
categóricas mediante one-hot encoding. Normalización y estandarización de variables numéricas.
División en conjuntos de entrenamiento (70%), validación (15%) y prueba (15%), garantizando que no
haya fuga de datos (data leakage) entre particiones (Géron, 2022).

### Fase 4 – Modelado no supervisado............................................................................................

Aplicación de K-Means para clustering de cobradores. Determinación del número óptimo de clústeres
mediante el método del codo y el índice de silueta. Asignación de etiquetas de perfil a cada registro del
dataset.

### Fase 5 – Modelado supervisado.................................................................................................

Incorporación del clúster como feature adicional. Entrenamiento de Random Forest. Ajuste
de hiperparámetros mediante validación cruzada (k-fold). Análisis de la importancia de variables (feature
importance).

### Fase 6 – Evaluación...................................................................................................................

Análisis de métricas, matrices de confusión, curvas ROC y detección de sobreajuste (Hastie et al., 2020).
Comparación de modelos y selección del mejor desempeño.

### Fase 7 – Despliegue de API REST.............................................................................................

Construcción de una API REST con FastAPI para servir los modelos entrenados. Definición de esquemas
de entrada/salida con Pydantic, carga de artefactos (preprocessor, clustering, classifier) y endpoint `/predict`
con CORS habilitado para consumo desde el frontend.

### Fase 8 – Desarrollo del Frontend Web.........................................................................................

Creación de una interfaz web interactiva con HTML, CSS y JavaScript vanilla. Incluye canvas con
representación visual del arco dividido en 9 zonas, formulario de entrada de datos contextuales del penal,
visualización de resultados con barras de probabilidad y tarjeta del perfil de clúster asignado.

### Fase 9 – Documentación y socialización...................................................................................

Elaboración del documento final, código documentado y presentación de resultados conforme a los
requisitos del Proyecto Final

## 7. Planteamiento inicial del software............................................................................................

### Requerimientos funcionales.......................................................................................................


```
● RF-01: El sistema debe permitir la carga de un dataset en formato CSV con datos históricos de
penales.
● RF-02: El sistema debe realizar el preprocesamiento de los datos históricos de penales,
incluyendo imputación de valores nulos en variables contextuales, aumento de datos sintéticos
(Steps_Run, Time_Taken) basado en reglas de dominio futbolístico, y cálculo de métricas
derivadas (Stress_Index, Team_Effectiveness, Keeper_Save_Rate) para alimentar los modelos.

  *Nota justificativa:* No se implementa eliminación de duplicados ni detección de atípicos por
  las siguientes razones: (1) Steps_Run y Time_Taken son generados sintéticamente con
  np.random en `_augment_data`, no son mediciones reales — no tiene sentido sanitizar datos
  artificiales. (2) Stress_Index es una transformación lineal determinista de Penalty_Number ×
  (Elimination + 1) — matemáticamente no puede producir outliers. (3) Team_Effectiveness y
  Keeper_Save_Rate son promedios históricos acotados entre 0 y 1. (4) El dataset proviene de
  una fuente curada (World Cup shootouts), no de sensor data ruidosa, y su tamaño reducido
  hace que cada registro sea valioso para el entrenamiento.
● RF-03: El sistema debe ejecutar el modelo K-Means para agrupar a los cobradores y asignar un
perfil de clúster a cada registro.
● RF-04: El sistema debe entrenar el modelo supervisado (Random Forest) integrando
el perfil de clúster como variable de entrada.
● RF-05: El sistema debe permitir ingresar los datos de una situación hipotética de penal y retornar
la probabilidad predicha de cada resultado (gol / fallo / atajada).
● RF-06: El sistema debe generar y visualizar las métricas de evaluación de ambos modelos
(accuracy, F1-score, índice de silueta, matriz de confusión).
● RF-07: El código debe estar estructurado en módulos independientes y ser completamente
reproducible sin rutas fijas ni dependencias no especificadas.
● RF-08: El sistema debe exponer una API REST (FastAPI) con un endpoint `/predict` que reciba los
datos contextuales del penal y retorne probabilidades, clúster asignado y métricas aumentadas.
● RF-09: La API debe incluir configuración CORS para permitir peticiones desde el frontend web.
● RF-10: El sistema debe incluir una interfaz web interactiva con un canvas que represente el arco
dividido en 9 zonas, formulario de entrada y visualización de resultados con barras de probabilidad.
● RF-11: El frontend debe mostrar el perfil de clúster asignado, el número de pasos de carrera y el
tiempo estimado de ejecución junto con la predicción del resultado.
```
## 8. Técnicas de Machine Learning propuestas.............................................................................

### Supervisado – Clasificación multiclase.....................................................................................

Se utilizará clasificación multiclase para predecir el resultado del penal (gol, fallo o atajada). El
algoritmo seleccionado es Random Forest, por su robustez ante datos mixtos,
su capacidad para manejar la importancia de features y su buen desempeño en problemas de clasificación
con datos deportivos (Chen & Guestrin, 2016; Breiman, 2001). Como baseline se empleará Regresión
Logística.

#### Variables de entrada (features – X)......................................................................................

```
● Índice de presión contextual (fase del torneo: grupos, cuartos, semifinal, final)
● Minuto del partido en que se ejecuta el penal
● Pierna hábil del cobrador (diestro / zurdo)
● Historial de atajadas del portero (% de penales detenidos en carrera)
● Diferencia de goles en el marcador al momento del penal
● Perfil de clúster asignado por el modelo no supervisado
```
#### Variable objetivo (target – Y)..............................................................................................

Resultado del penal: Gol (0), Atajada (1), Fallo (2) — clasificación multiclase.


### No supervisado – Agrupamiento (Clustering)...........................................................................

Se utilizará K-Means para descubrir perfiles ocultos de cobradores (MacQueen, 1967). El modelo
procesará las variables sin revelarle el resultado del penal, permitiendo que encuentre similitudes
estructurales entre jugadores de forma autónoma.

#### Variables de entrada para clustering....................................................................................

```
● Número de pasos en la carrera de impulso
● Tiempo transcurrido entre el pitazo del árbitro y el momento del disparo
● Historial de penales cobrados en la carrera (porcentaje de efectividad)
● Edad del cobrador al momento del penal
● Indicador compuesto del nivel de estrés del partido (fase + marcador + minuto)
```
## 9. Arquitectura propuesta.............................................................................................................

El sistema seguirá una arquitectura de pipeline secuencial en tres capas:

### Capa 1 – Ingesta y preprocesamiento........................................................................................

Módulo data_loader.py para lectura del CSV y módulo preprocessor.py para limpieza, codificación y
normalización. Toda la lógica de preparación de datos es independiente del modelo.

### Capa 2 – Modelado dual (Pipeline ML)....................................................................................

Módulo clustering.py que implementa K-Means y asigna perfiles de cobro. Módulo classifier.py que
entrena el modelo supervisado integrando el perfil de clúster como feature adicional, construyendo así un
pipeline integrado (Géron, 2022).

### Capa 3 – Evaluación y predicción.............................................................................................

Módulo evaluator.py que genera métricas, matrices de confusión y curvas ROC. Módulo predictor.py que
recibe datos de una situación hipotética y retorna probabilidades predichas.

### Capa 4 – API REST (FastAPI)...................................................................................................

Módulo api/main.py que define los endpoints de la API. Utiliza el predictor.py para realizar la inferencia
completa (preprocesamiento → clustering → clasificación). Los esquemas de entrada/salida se definen
con Pydantic en api/schemas.py. Configuración CORS para permitir peticiones desde cualquier origen.
Los artefactos del pipeline (preprocessor.pkl, kmeans_model.pkl, classifier_model.pkl) se cargan en el
evento de startup desde la carpeta models/. El endpoint POST /predict recibe los datos contextuales del
penal y retorna las probabilidades, el clúster asignado y las métricas aumentadas.

### Capa 5 – Frontend Web.............................................................................................................

Interfaz de usuario en frontend/index.html con CSS y JavaScript vanilla. Incluye un canvas
interactivo que representa el arco de fútbol dividido en 9 zonas numeradas, formulario con campos
para equipo, pie del cobrador, movimiento del portero, número de penal y presión del partido. Los
resultados se visualizan con barras de probabilidad para cada clase (Gol, Atajada, Fallo), el perfil de
clúster asignado y métricas contextuales (pasos de carrera y tiempo de ejecución).

### Tecnologías................................................................................................................................

**Backend**: Python 3.10+, scikit-learn, pandas, NumPy, matplotlib, seaborn, FastAPI, Uvicorn, Pydantic,
joblib.

**Frontend**: HTML5, CSS3, JavaScript vanilla (Canvas API).

Infraestructura reproducible mediante requirements.txt. Los artefactos de los modelos se serializan con
joblib y se almacenan en la carpeta models/. Se evitarán rutas fijas y valores codificados directamente
en el código.


## 10. Cronograma............................................................................................................................

```
Actividad Fecha Responsable
Elección del tema y formación del grupo Semana 9 Grupo
Planteamiento del problema y requerimientos funcionales Semana 10 Grupo
Elaboración y entrega de la propuesta (formato UPTC) Semana 10 Grupo
Recopilación y documentación del dataset Semana 11 Grupo
Análisis exploratorio de datos (EDA) y preprocesamiento Semana 11 Grupo
Implementación del modelo no supervisado (K-Means) Semana 12 Grupo
Implementación del modelo supervisado (Random Forest)
Semana 12-13 Grupo
Evaluación de modelos y análisis crítico de resultados Semana 13 Grupo
Despliegue de API REST (FastAPI) y Frontend Web Semana 13-14 Grupo
Redacción del documento final y estructuración del código Semana 13-14 Grupo
Entrega de documentación y entregables finales Semana 14 Grupo
Preparación de diapositivas (máx. 6) para socialización Semana 14 Grupo
Socialización individual del proyecto Semana 15-16 Individual
```

## Referencias....................................................................................................................................

Breiman, L. (2001). Random forests. Machine Learning, 45(1), 5–32.
https://doi.org/10.1023/A:
Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. En Proceedings of the 22nd
ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp.
785–794). ACM. https://doi.org/10.1145/2939672.
Duch, J., Waitzman, J. S., & Amaral, L. A. N. (2010). Quantifying the performance of individual players
in a team activity. PLOS ONE, 5(6), e10937. https://doi.org/10.1371/journal.pone.
Géron, A. (2022). Hands-on machine learning with Scikit-Learn, Keras, and TensorFlow (3.ª ed.).
O'Reilly Media.
Hastie, T., Tibshirani, R., & Friedman, J. (2020). The elements of statistical learning: Data mining,
inference, and prediction (2.ª ed.). Springer. https://doi.org/10.1007/978-0-387-84858-
Jordet, G., Hartman, E., Visscher, C., & Lemmink, K. A. P. M. (2007). Kicks from the penalty mark in
soccer: The roles of stress, skill, and fatigue for kick outcomes. Journal of Sports Sciences, 25(2),
121–129. https://doi.org/10.1080/
MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations. En
Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability (Vol. 1,
pp. 281–297). University of California Press.
Morya, E., Ranvaud, R., & Pinheiro, W. M. (2003). Dynamics of visual feedback in a laboratory
simulation of a penalty kick. Journal of Sports Sciences, 21(2), 87–95.
https://doi.org/10.1080/0264041031000070/
Rein, R., & Memmert, D. (2016). Big data and tactical analysis in elite soccer: Future challenges and
opportunities for sports science. SpringerPlus, 5(1), 1410.
https://doi.org/10.1186/s40064-016-3108-
Schröer, C., Kruse, F., & Gómez, J. M. (2021). A systematic literature review on applying CRISP-DM
process model. Procedia Computer Science, 181, 526–534.
https://doi.org/10.1016/j.procs.2021.01.


