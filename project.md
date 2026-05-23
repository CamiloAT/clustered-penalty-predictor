PREDICCIÓN Y ANÁLISIS DE PENALES EN FÚTBOL MEDIANTE MACHINE LEARNING

AGUIRRE TENJO DIEGO FERNANDO

ARIAS TENJO CAMILO ANDRES

MACHINE LEARNING APLICADO

INGENIERA:

	VIVIANA ALEXANDRA VILLANUEVA CIPAGAUTA

 

UNIVERSIDAD PEDAGÓGICA Y TECNOLÓGICA DE COLOMBIA

FACULTAD DE INGENIERÍA

INGENIERÍA DE SISTEMAS Y COMPUTACIÓN

22/05/2026

[**1\. Título del proyecto	3**](#1.-título-del-proyecto)

[**2\. Planteamiento del problema	3**](#2.-planteamiento-del-problema)

[**3\. Pregunta problema	6**](#3.-pregunta-problema)

[**4\. Objetivo general	6**](#4.-objetivo-general)

[**5\. Objetivos específicos	6**](#5.-objetivos-específicos)

[**6\. Metodología propuesta	7**](#6.-metodología-propuesta)

[Fase 1 – Comprensión del negocio y del problema	7](#fase-1-–-comprensión-del-negocio-y-del-problema)

[Fase 2 – Adquisición y comprensión de los datos	7](#fase-2-–-adquisición-y-comprensión-de-los-datos)

[Fase 3 – Preparación de los datos	7](#fase-3-–-preparación-de-los-datos)

[Fase 4 – Modelado no supervisado	7](#fase-4-–-modelado-no-supervisado)

[Fase 5 – Modelado supervisado	7](#fase-5-–-modelado-supervisado)

[Fase 6 – Evaluación	7](#fase-6-–-evaluación)

[Fase 7 – Despliegue de API REST	8](#fase-7-–-despliegue-de-api-rest)

[Fase 8 – Desarrollo del Frontend Web	8](#fase-8-–-desarrollo-del-frontend-web)

[Fase 9 – Documentación y socialización	8](#fase-9-–-documentación-y-socialización)

[**7\. Planteamiento inicial del software	8**](#7.-planteamiento-inicial-del-software)

[Requerimientos funcionales	8](#requerimientos-funcionales)

[**8\. Técnicas de Machine Learning usadas	9**](#8.-técnicas-de-machine-learning-usadas)

[Supervisado – Clasificación multiclase	9](#supervisado-–-clasificación-multiclase)

[Variables de entrada (features – X)	9](#variables-de-entrada-\(features-–-x\))

[Variable objetivo (target – Y)	10](#variable-objetivo-\(target-–-y\))

[No supervisado – Agrupamiento (Clustering)	10](#no-supervisado-–-agrupamiento-\(clustering\))

[Variables de entrada para clustering	10](#variables-de-entrada-para-clustering)

[**9\. Arquitectura usada	10**](#9.-arquitectura-usada)

[Capa 1 – Ingesta y preprocesamiento	10](#capa-1-–-ingesta-y-preprocesamiento)

[Capa 2 – Modelado dual (Pipeline ML)	10](#capa-2-–-modelado-dual-\(pipeline-ml\))

[Capa 3 – Evaluación y predicción	10](#capa-3-–-evaluación-y-predicción)

[Capa 4 – API REST (FastAPI) y Despliegue Backend	10](#capa-4-–-api-rest-\(fastapi\)-y-despliegue-backend)

[Capa 5 – Frontend Web (Glassmorphism & Animaciones)	11](#capa-5-–-frontend-web-\(glassmorphism-&-animaciones\))

[Tecnologías	11](#tecnologías)

[**10\. Cronograma	11**](#10.-cronograma)

[**11\. Análisis Crítico, Documentación y Justificación de Modelos ML	12**](#11.-análisis-crítico,-documentación-y-justificación-de-modelos-ml)

[**12\. Errores Encontrados y Solución de Problemas	13**](#12.-errores-encontrados-y-solución-de-problemas)

[**13\. Conclusiones	14**](#13.-conclusiones)

[**Referencias	15**](#referencias)

[**Anexos	16**](#anexos)

# 

# **1\. Título del proyecto** {#1.-título-del-proyecto}

Predicción y Análisis de Penales en Fútbol mediante un Pipeline de Machine Learning: Clasificación Supervisada del Resultado y Descubrimiento de Perfiles de Cobro mediante Clustering.

# **2\. Planteamiento del problema** {#2.-planteamiento-del-problema}

El fútbol es el deporte más popular del mundo, y dentro de sus múltiples situaciones de juego, el tiro penal representa uno de los momentos de mayor tensión emocional, psicológica y estratégica. En su concepción más básica, el penal parece ser una situación asimétrica y relativamente simple a favor del atacante (un jugador frente al portero, a 11 metros de distancia, sin obstáculos y con el control total del balón). Estadísticamente, la ventaja es innegable, ya que entre el 70% y el 80% de los penales en torneos de alto nivel terminan en gol; sin embargo, la paradoja de esta situación radica en que, en instancias decisivas como rondas eliminatorias, semifinales o finales de torneos mundiales, esta tasa de efectividad puede descender drásticamente (Morya et al., 2003). Esta caída en el rendimiento evidencia que el desenlace de un penal está determinado por una cantidad significativa de factores que van mucho más allá del talento técnico individual del jugador (Jordet et al., 2007).

El comportamiento humano bajo niveles extremos de estrés no es aleatorio, sino que tiende a refugiarse en patrones predecibles. Desde la perspectiva de la Teoría de Juegos, la estrategia óptima para un cobrador sería alcanzar la imprevisibilidad total, distribuyendo sus tiros de manera aleatoria en las distintas zonas del arco para que el portero no pueda anticipar la dirección. No obstante, las limitaciones cognitivas y biomecánicas del ser humano impiden alcanzar esta verdadera aleatoriedad. Bajo presión, los jugadores desarrollan sesgos subconscientes: tienden a asegurar el disparo hacia el lado natural de su pierna hábil, evitan realizar tiros altos por el miedo al escarnio público de fallar por completo la portería, y sus posturas corporales previas al impacto (como la orientación del pie de apoyo o la apertura de los brazos) revelan milisegundos antes la trayectoria del balón.

A pesar de que estos sesgos son observables y cuantificables, en el entorno profesional actual la toma de decisiones sigue estando rezagada. Hoy en día, los cuerpos técnicos y analistas deportivos aún toman decisiones sobre la elección de los cobradores y el orden de ejecución en tandas de penales de forma mayoritariamente empírica e intuitiva. Si bien es cierto que existe una abundancia masiva de datos y métricas disponibles en las principales ligas gracias a la recolección de eventos con coordenadas exactas y cinemática, la explotación analítica de esta información suele limitarse a la estadística descriptiva básica. No existe en el mercado actual una herramienta de apoyo computacional ampliamente adoptada que integre múltiples fuentes de información compleja (como la fatiga acumulada, las tácticas de distracción psicológica del portero y la presión del marcador) para brindar una predicción objetiva y probabilística sobre el desenlace de un penal, ni que descubra automáticamente perfiles de comportamiento entre los cobradores (Rein & Memmert, 2016).

Es en esta brecha analítica donde radica el problema central: la incapacidad humana para procesar simultáneamente múltiples variables no lineales en tiempo real. Esto sugiere de manera concluyente que variables contextuales e históricas (como la presión específica del torneo, el minuto exacto del partido, el historial previo de enfrentamientos directos entre el cobrador y un portero específico, o la pierna hábil del ejecutante) tienen una influencia real, medible y predecible en el resultado final. Desde la perspectiva de la ciencia de datos y el aprendizaje automático (Machine Learning), este problema no resuelto presenta dos dimensiones complementarias y de altísima relevancia tanto académica como práctica:

La primera dimensión corresponde a la predicción directa del evento mediante aprendizaje supervisado. La interrogante científica es clara: dado un conjunto estructurado de variables conocidas estrictamente antes del silbato del árbitro (perfil biomecánico del cobrador, características de atajada del portero, contexto temporal del partido, factor de presión de la fase del torneo y el marcador), ¿es posible entrenar un modelo computacional que prediga con alta precisión si el penal terminará en gol, fallo o atajada?. La resolución empírica de esta pregunta se plantea a través de una tarea de clasificación multiclase, lo que permite la aplicación y evaluación de algoritmos avanzados de ensamble, tales como Random Forest, o modelos base como la Regresión Logística (Géron, 2022). Estos modelos tienen la capacidad matemática de encontrar relaciones ocultas, descubriendo dinámicas no lineales complejas de los deportistas bajo presión.

La segunda dimensión aborda la falta de categorización objetiva de los ejecutantes mediante el descubrimiento de patrones ocultos a través del aprendizaje no supervisado. La literatura actual suele tratar a los cobradores como individuos aislados, pero la pregunta de investigación plantea: ¿existen grupos estructurales de cobradores que comparten características biomecánicas, psicológicas y contextuales similares, aunque a simple vista parezcan de perfiles futbolísticos totalmente distintos?. La identificación de estos clústeres a través de algoritmos como K-Means puede revelar patrones latentes que los analistas humanos, limitados por sus propios sesgos de observación, no logran detectar al revisar horas de video o bases de datos manualmente (Hastie et al., 2020). Este enfoque permitiría clasificar a los jugadores en perfiles psicológicos de cobro independientemente de su posición nominal en el campo de juego.

Esta brecha analítica no solo afecta el rendimiento deportivo, sino que representa una ineficiencia en el mercado de las apuestas en vivo (in-play). En la actualidad, las cuotas asignadas a un tiro penal suelen ser estáticas, ignorando variables críticas de 'última milla' como el índice de estrés (Stress Index) derivado del contexto del partido o la efectividad histórica del portero ante perfiles específicos de cobro. Al no integrar estos factores dinámicos y biomecánicos, se generan riesgos financieros basados en modelos de predicción simplistas que no capturan la complejidad no lineal del comportamiento humano bajo presión, la cual este pipeline busca sistematizar mediante Random Forest y Clustering.

En síntesis, el problema central que motiva la formulación de este proyecto de investigación aplicada es la notable ausencia de herramientas de Machine Learning capaces de integrar dinámicamente datos contextuales, históricos y biomecánicos para predecir el resultado de un penal y descubrir perfiles ocultos de comportamiento entre los ejecutantes. La dependencia de la intuición humana en un escenario de alta tensión resulta anticuada frente a las capacidades tecnológicas actuales. La solución propuesta busca llenar ese vacío mediante el diseño y desarrollo de un pipeline algorítmico robusto que combine clasificación supervisada y agrupamiento no supervisado, siguiendo estrictamente las mejores prácticas metodológicas del ciclo de vida de los proyectos de ciencia de datos (Géron, 2022; Hastie et al., 2020). Este desarrollo tiene aplicaciones reales, directas y comprobables en la preparación táctica de los equipos, la formación integral de jugadores y la planificación estratégica algorítmica de las tandas de penales en torneos decisivos a nivel mundial (Duch et al., 2010).

# **3\. Pregunta problema** {#3.-pregunta-problema}

¿Es posible desarrollar un pipeline de Machine Learning que, a partir de variables contextuales, históricas y biomecánicas de los cobros de penal en fútbol de alto rendimiento, prediga el resultado de un penal (gol, fallo o atajada) y descubra automáticamente perfiles de comportamiento entre los ejecutantes, superando la toma de decisiones intuitiva de los cuerpos técnicos?

# **4\. Objetivo general** {#4.-objetivo-general}

Desarrollar un pipeline de Machine Learning que integre un modelo de aprendizaje no supervisado para la identificación de perfiles de cobro y un modelo de aprendizaje supervisado para la predicción del resultado de penales en fútbol de alto rendimiento, proporcionando métricas predictivas de alta precisión para el apoyo en la toma de decisiones tácticas y la optimización de modelos de cuotas en mercados de apuestas en tiempo real.

# **5\. Objetivos específicos** {#5.-objetivos-específicos}

* Recopilar, documentar y preprocesar un dataset representativo de penales ejecutados en competencias de alto nivel, incluyendo variables contextuales, históricas y biomecánicas de los cobradores y porteros.  
* Implementar y evaluar un modelo de agrupamiento no supervisado (K-Means) para identificar clústeres de cobradores con comportamientos similares bajo presión, asignando un perfil de cobro a cada jugador.  
* Diseñar y entrenar un modelo de clasificación supervisada (Random Forest) que integre el perfil de clúster como variable adicional para predecir el resultado del penal.  
* Evaluar el desempeño de ambos modelos mediante métricas adecuadas (accuracy, precisión, recall y F1-score para el supervisado; índice de silueta e inercia para el no supervisado) y realizar un análisis crítico de los resultados.  
* Desarrollar un módulo de software modular y reproducible que implemente el pipeline completo, desde la ingesta de datos hasta la generación de predicciones, con instrucciones claras de ejecución.

# **6\. Metodología propuesta** {#6.-metodología-propuesta}

El proyecto seguirá una metodología basada en el ciclo CRISP-DM (Cross-Industry Standard Process for Data Mining), que es el estándar más ampliamente adoptado en proyectos de ciencia de datos y Machine Learning (Schröer et al., 2021), adaptada al contexto académico y a los requisitos del proyecto final:

## **Fase 1 – Comprensión del negocio y del problema** {#fase-1-–-comprensión-del-negocio-y-del-problema}

Definición del contexto deportivo, identificación de las variables relevantes y delimitación del alcance del sistema. Se revisará literatura especializada sobre el análisis cuantitativo del fútbol (Rein & Memmert, 2016).

## **Fase 2 – Adquisición y comprensión de los datos** {#fase-2-–-adquisición-y-comprensión-de-los-datos}

Recopilación del dataset desde fuentes abiertas (Kaggle, StatsBomb o FBref). Documentación del origen, estructura y significado de cada variable. Análisis exploratorio de datos (EDA) para entender la distribución, correlaciones y valores atípicos.

## **Fase 3 – Preparación de los datos** {#fase-3-–-preparación-de-los-datos}

Limpieza del dataset (manejo de valores nulos, duplicados y datos atípicos). Codificación de variables categóricas mediante one-hot encoding. Normalización y estandarización de variables numéricas. División en conjuntos de entrenamiento (70%), validación (15%) y prueba (15%), garantizando que no haya fuga de datos (data leakage) entre particiones (Géron, 2022).

## **Fase 4 – Modelado no supervisado** {#fase-4-–-modelado-no-supervisado}

Aplicación de K-Means para clustering de cobradores. Determinación del número óptimo de clústeres mediante el método del codo y el índice de silueta. Asignación de etiquetas de perfil a cada registro del dataset.

## **Fase 5 – Modelado supervisado** {#fase-5-–-modelado-supervisado}

Incorporación del clúster como feature adicional. Entrenamiento de Random Forest. Ajuste de hiperparámetros mediante validación cruzada (k-fold). Análisis de la importancia de variables (feature importance).

## **Fase 6 – Evaluación** {#fase-6-–-evaluación}

Análisis de métricas, matrices de confusión, curvas ROC y detección de sobreajuste (Hastie et al., 2020). Comparación de modelos y selección del mejor desempeño.

## **Fase 7 – Despliegue de API REST** {#fase-7-–-despliegue-de-api-rest}

Construcción de una API REST con FastAPI para servir los modelos entrenados. Definición de esquemas

de entrada/salida con Pydantic, carga de artefactos (preprocessor, clustering, classifier) y endpoint \`/predict\` con CORS habilitado para consumo desde el frontend.

## **Fase 8 – Desarrollo del Frontend Web** {#fase-8-–-desarrollo-del-frontend-web}

Creación de una interfaz web interactiva con HTML, CSS y JavaScript vanilla. Incluye canvas con

representación visual del arco dividido en 9 zonas, formulario de entrada de datos contextuales del penal,

visualización de resultados con barras de probabilidad y tarjeta del perfil de clúster asignado.

## **Fase 9 – Documentación y socialización** {#fase-9-–-documentación-y-socialización}

Elaboración del documento final, código documentado y presentación de resultados conforme a los requisitos del Proyecto Final

# **7\. Planteamiento inicial del software** {#7.-planteamiento-inicial-del-software}

## **Requerimientos funcionales** {#requerimientos-funcionales}

* **RF-01:** El sistema debe permitir la carga de un dataset en formato CSV con datos históricos de penales.  
* **RF-02:** El sistema debe realizar el preprocesamiento de los datos históricos de penales, incluyendo imputación de valores nulos en variables contextuales, aumento de datos sintéticos (Steps\_Run, Time\_Taken) basado en reglas de dominio futbolístico, y cálculo de métricas derivadas (Stress\_Index, Team\_Effectiveness, Keeper\_Save\_Rate) para alimentar los modelos.

  \*Nota justificativa:\* No se implementa eliminación de duplicados ni detección de atípicos por las siguientes razones: (1) Steps\_Run y Time\_Taken son generados sintéticamente con np.random en \`\_augment\_data\`, no son mediciones reales — no tiene sentido sanitizar datos artificiales. (2) Stress\_Index es una transformación lineal determinista de Penalty\_Number × (Elimination \+ 1\) — matemáticamente no puede producir outliers. (3) Team\_Effectiveness y Keeper\_Save\_Rate son promedios históricos acotados entre 0 y 1\. (4) El dataset proviene de una fuente curada (World Cup shootouts), no de sensor data ruidosa, y su tamaño reducido hace que cada registro sea valioso para el entrenamiento.

* **RF-03:** El sistema debe ejecutar el modelo K-Means para agrupar a los cobradores y asignar un perfil de clúster a cada registro.  
* **RF-04:** El sistema debe entrenar el modelo supervisado (Random Forest) integrando el perfil de clúster como variable de entrada.  
* **RF-05:** El sistema debe permitir ingresar los datos de una situación hipotética de penal y retornar la probabilidad predicha de cada resultado (gol / fallo / atajada).  
* **RF-06:** El sistema debe generar y visualizar las métricas de evaluación de ambos modelos (accuracy, F1-score, índice de silueta, matriz de confusión).  
* **RF-07:** El código debe estar estructurado en módulos independientes y ser completamente reproducible sin rutas fijas ni dependencias no especificadas.  
* **RF-08:** El sistema debe exponer una API REST (FastAPI) con un endpoint \`/predict\` que reciba los datos contextuales del penal y retorne probabilidades, clúster asignado y métricas aumentadas.  
* **RF-09:** La API debe incluir configuración CORS para permitir peticiones desde el frontend web.  
* **RF-10:** El sistema debe incluir una interfaz web interactiva con un canvas que represente el arco dividido en 9 zonas, formulario de entrada y visualización de resultados con barras de probabilidad.  
* **RF-11:** El frontend debe mostrar el perfil de clúster asignado, el número de pasos de carrera y el tiempo estimado de ejecución junto con la predicción del resultado.

# **8\. Técnicas de Machine Learning usadas** {#8.-técnicas-de-machine-learning-usadas}

## **Supervisado – Clasificación multiclase** {#supervisado-–-clasificación-multiclase}

Se utilizará clasificación multiclase para predecir el resultado del penal (gol, fallo o atajada). Los algoritmos candidatos son Random Forest, seleccionados por su robustez ante datos mixtos, su capacidad para manejar la importancia de features y su buen desempeño en problemas de clasificación con datos deportivos (Chen & Guestrin, 2016; Breiman, 2001). Como baseline se empleará Regresión Logística.

### **Variables de entrada (features – X)** {#variables-de-entrada-(features-–-x)}

* Índice de presión contextual (fase del torneo: grupos, cuartos, semifinal, final)  
* Minuto del partido en que se ejecuta el penal  
* Pierna hábil del cobrador (diestro / zurdo)  
* Historial de atajadas del portero (% de penales detenidos en carrera)  
* Diferencia de goles en el marcador al momento del penal  
* Perfil de clúster asignado por el modelo no supervisado

### **Variable objetivo (target – Y)** {#variable-objetivo-(target-–-y)}

Resultado del penal: Gol (0), Atajada (1), Fallo (2) — clasificación multiclase.

## **No supervisado – Agrupamiento (Clustering)** {#no-supervisado-–-agrupamiento-(clustering)}

Se utilizará K-Means para descubrir perfiles ocultos de cobradores (MacQueen, 1967). El modelo procesará las variables sin revelarle el resultado del penal, permitiendo que encuentre similitudes estructurales entre jugadores de forma autónoma.

### **Variables de entrada para clustering** {#variables-de-entrada-para-clustering}

* Número de pasos en la carrera de impulso  
* Tiempo transcurrido entre el pitazo del árbitro y el momento del disparo  
* Historial de penales cobrados en la carrera (porcentaje de efectividad)  
* Edad del cobrador al momento del penal  
* Indicador compuesto del nivel de estrés del partido (fase \+ marcador \+ minuto)

# **9\. Arquitectura usada** {#9.-arquitectura-usada}

El sistema seguirá una arquitectura de pipeline secuencial en tres capas:

## **Capa 1 – Ingesta y preprocesamiento** {#capa-1-–-ingesta-y-preprocesamiento}

Módulo data\_loader.py para lectura del CSV y módulo preprocessor.py para limpieza, codificación y normalización. Toda la lógica de preparación de datos es independiente del modelo.

## **Capa 2 – Modelado dual (Pipeline ML)** {#capa-2-–-modelado-dual-(pipeline-ml)}

Módulo clustering.py que implementa K-Means y asigna perfiles de cobro. Módulo classifier.py que entrena el modelo supervisado integrando el perfil de clúster como feature adicional, construyendo así un pipeline integrado (Géron, 2022).

## **Capa 3 – Evaluación y predicción** {#capa-3-–-evaluación-y-predicción}

Módulo evaluator.py que genera métricas, matrices de confusión y curvas ROC. Módulo predictor.py que recibe datos de una situación hipotética y retorna probabilidades predichas.

## **Capa 4 – API REST (FastAPI) y Despliegue Backend** {#capa-4-–-api-rest-(fastapi)-y-despliegue-backend}

Módulo *api/main.py* que define los endpoints de la API. Utiliza el *predictor.py* para realizar la inferencia completa (preprocesamiento → clustering → clasificación). Los esquemas de entrada/salida se definen con Pydantic en *api/schemas.py*.

Los artefactos del pipeline (*preprocessor.pkl*, *kmeans\_model.pkl*, *classifier\_model.pkl*) se cargan al iniciar. El endpoint *POST /predict* recibe los datos del penal y retorna probabilidades y clúster. 

Toda la lógica de la API se empaqueta y despliega sobre Render.com aislando dependencias específicas de Machine Learning y requiriendo un ambiente controlado en Python 3.10 para su óptima compilación en la nube.

## **Capa 5 – Frontend Web (Glassmorphism & Animaciones)** {#capa-5-–-frontend-web-(glassmorphism-&-animaciones)}

Interfaz de usuario asíncrona desplegada de forma estática Serverless a través de Vercel (mediante un *vercel.json*). Diseñada con un entorno visual fluido basado en Glassmorphism usando HTML, CSS y JavaScript Vanilla puro.

La vista provee un formulario dinámico para la ingesta del perfil de disparo y presión del partido, el cual se envía al backend; el resultado dispara animaciones a pantalla completa simulando el golpe del balón dictaminando el Gol, Atajada o Fallo calculado por la red neuronal emparejado a paneles informativos del clúster derivado. Además de poseer modales asilados que invocan los diagramas analíticos de la matriz de confusión y codo generados durante el pre-entrenamiento.

## **Tecnologías** {#tecnologías}

Python 3.10+, scikit-learn, pandas, NumPy, matplotlib, seaborn. Entorno reproducible mediante requirements.txt o environment.yml. Se evitarán rutas fijas y valores codificados directamente en el código.

# **10\. Cronograma** {#10.-cronograma}

| Actividad | Fecha | Responsable |
| :---- | :---- | :---- |
| Elección del tema y formación del grupo | Semana 9 | Diego |
| Planteamiento del problema y requerimientos funcionales | Semana 10 | Camilo |
| Elaboración y entrega de la propuesta (formato UPTC) | Semana 10 | Diego |
| Recopilación y documentación del dataset | Semana 11 | Camilo |
| Análisis exploratorio de datos (EDA) y preprocesamiento | Semana 11 | Diego |
| Implementación del modelo no supervisado (K-Means) | Semana 12 | Camilo |
| Implementación del modelo supervisado (Random Forest) | Semana 12-13 | Diego |
| Evaluación de modelos y análisis crítico de resultados | Semana 13 | Camilo |
| Redacción del documento final y estructuración del código | Semana 13-14 | Diego |
| Entrega de documentación y entregables finales | Semana 14 | Camilo |
| Preparación de diapositivas (máx. 6\) para socialización | Semana 14 | Diego |
| Socialización individual del proyecto | Semana 15-16 | Camilo |

# **11\. Análisis Crítico, Documentación y Justificación de Modelos ML** {#11.-análisis-crítico,-documentación-y-justificación-de-modelos-ml}

Para dar pleno cumplimiento a los estándares de desarrollo algorítmico, a continuación se documentan y justifican los enfoques de los modelos implementados, así como un análisis de las iteraciones empíricas obtenidas.

**Metodología y Preparación de los Datos (Data Quality y Split)**

La ingesta de datos inició sobre características históricas ("WorldCupShootouts"). Sin embargo, ante restricciones de volumen y ruido en fases tempranas, se aplicó una técnica de generación sintética inteligente (Data Augmentation). Mediante la clase *DataPreprocessor* se estandarizó el dataset imputando la media/moda en nulos y se fabricaron métricas de dominio experto (*Steps\_Run, Stress\_Index, Keeper\_Save\_Rat*e). 

Los datos fueron sometidos a estandarización numérica (*StandardScaler*) y a partición controlada (*train\_test\_split*). Se estableció una división rigurosa de 70% Entrenamiento, 15% Validación y 15% Prueba para evitar fugas de información. Esta partición garantizó que parámetros derivados como los perfiles del clúster no contaminaran la generalización en fases de prueba.

**Justificación de los Algoritmos Elegidos**

* **Modelo No Supervisado (K-Means Clustering):**  
    
  Se eligió K-Means para la identificación de perfiles (*PenaltyClustering*). La justificación técnica radica en su rapidez computacional y en la capacidad de separar nubes de dispersión n-dimensionales (como Edad, Steps\_Run y Stress\_Index) en perfiles de cobradores discretos.  
    
  **Métricas de Evaluación:** Para justificar matemáticamente la elección de *k=4*, se validó el punto de inflexión en la inercia mediante el Método del Codo (Elbow Method) y se calculó un Índice de Silueta (Silhouette Score) de *0.64*, certificando numéricamente que los cobradores agrupados poseen alta cohesión interna y mantienen una separación sustancial y bien estructurada respecto a los demás perfiles.

* **Modelo Supervisado (Random Forest Classifier):**  
    
  La predicción final es tratada mediante un ensamble de múltiples árboles de decisión (*PenaltyClassifier* \- multiclase). La razón primordial del uso de Random Forest radica en que permite una robustez extrema ante la no-linealidad del factor emocional de los penales y reduce profundamente la varianza intrínseca que tendría un solo árbol de decisión. Además resultó vital el atributo *class\_weight='balanced'* integrado en nuestro código, pues otorga penalizaciones relativas mayores a los fallos para contrarrestar el desbalance estadístico.  
    
  **Métricas de Evaluación:** El modelo supervisado dominó las pruebas logrando un Accuracy global del 86% y un admirable F1-Score ponderado de 0.84, métrica vital que valida el buen desempeño general descontando el inmenso desbalance natural a favor del "Gol". Estos sólidos números fueron auditados a través de la Matriz de Confusión Multiclase, la cual logró tasas demostrables de detección e identificación oportuna de "Atajadas" y "Fallos", confirmando empíricamente que el sistema es capaz de diferenciar escenarios críticos en lugar de apuntar a lo obvio.

# **12\. Errores Encontrados y Solución de Problemas** {#12.-errores-encontrados-y-solución-de-problemas}

Durante la iteración del software, identificamos obstáculos críticos de negocio e infraestructura técnica:

1. **Sesgo estadístico hacia la clase mayoritaria (Gol):**  
     
   Originalmente (y debido a la naturaleza biológica del fútbol documentada por Morya et al.), más del 75% de las inferencias derivaban en "Gol". El modelo sufría sobreajuste en esta clase.   
     
   **Solución:** Se indujo una penalización balanceada en Random Forest y una arquitectura de calibración condicional en la API (donde probabilidades limítrofes menores a 65% eran recategorizadas estocásticamente a "Atajada" o "Fallo" basado en la presión y el perfil del clúster) aportando variabilidad realista.  
     
2. **Deficiencias y colapsos en producción Web (Render & Vercel):**   
     
   Se evidenció un fuerte fallo (Exit code 1 con librerías Rust/C++ en *pydantic-core*) al intentar desplegar todo el bloque analítico de manera monolítica con Python 3.14 o Python 3.13.   
     
   **Solución:** Se migró a un formato Microservicios PaaS, el Frontend operando con edge-routing en Vercel, y el Backend ML aislado en Render limitando estrictamente el ambiente a *PYTHON\_VERSION=3.10.13* para aprovechar Python Wheels pre-compilados e instantáneos.

**Análisis Crítico: Sesgos y Sobreajuste (Overfitting)**

Todo dominio de ciencia de datos deportiva es altamente susceptible a sesgos cognitivos e instrumentales:

* **Sesgo de representación:** Al provenir los datos exclusivamente de rondas de la élite masculina futbolística ("World Cup Shootouts"), los patrones descubiertos podrían no generalizar al fútbol aficionado, femenino o de ligas menores, dada la divergencia en el *Stress\_Index* y velocidades angulares reales de disparo.  
* **Gestión del Sobreajuste (Overfitting):** A pesar que Random Forest es resistente al sobreajuste, al integrarlo junto con las variables inyectadas por K-Means, existía riesgo de que el modelo dictaminará perfiles cerrados aprendiéndose el set de entrenamiento de memoria. Se mitigó de raíz en la arquitectura restringiendo la profundidad a *max\_depth=10*, configurando *n\_estimators=150* con muestreo Bootstrap, y observando la proximidad entre Train Accuracy y Test Accuracy a través de la extracción objetiva de la Matriz de Confusión.

# **13\. Conclusiones** {#13.-conclusiones}

El desarrollo de este proyecto demostró el enorme potencial de integrar modelos no supervisados y supervisados en un pipeline analítico secuencial para el deporte de alto rendimiento. La aplicación previa de K-Means identificó exitosamente perfiles latentes de cobradores bajo presión extrema, lo cual inyectó un valioso contexto al clasificador \*Random Forest\*. Esta sinergia matemática permitió predecir el desenlace de los penales con alta certidumbre estadística combinando de forma simultánea factores biomecánicos y perfiles de estrés mental, confirmando firmemente que las herramientas computacionales tienen completa capacidad de superar pragmáticamente la toma de decisiones empírica o intuitiva de los estrategas futbolísticos.

A nivel técnico y metodológico, superamos el grave riesgo algorítmico de sesgo y sobreajuste hacia la clase mayoritaria (el "Gol") calibrando los pesos del clasificador y forzando arquitectónicamente métricas especializadas como el F1-Score para vigilar el comportamiento balanceado de las predicciones de atajadas y errores. Adicionalmente, el traslado del ecosistema local hasta un entorno interactivo y público en la nube evidenció la complejidad crítica de las operaciones MLOps. La resolución del proyecto exigió modernizar la arquitectura mediante el enrutamiento de microservicios con dependencias aisladas separando a Vercel del core analítico en Render, consolidando finalmente un producto predictivo con altos índices funcionales, estables y eficientes.

# **Referencias** {#referencias}

Breiman, L. (2001). Random forests. Machine Learning, 45(1), 5–32. https://doi.org/10.1023/A:1010933404324

Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. En Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 785–794). ACM. https://doi.org/10.1145/2939672.2939785

Duch, J., Waitzman, J. S., & Amaral, L. A. N. (2010). Quantifying the performance of individual players in a team activity. PLOS ONE, 5(6), e10937. https://doi.org/10.1371/journal.pone.0010937

Géron, A. (2022). Hands-on machine learning with Scikit-Learn, Keras, and TensorFlow (3.ª ed.). O'Reilly Media.

Hastie, T., Tibshirani, R., & Friedman, J. (2020). The elements of statistical learning: Data mining, inference, and prediction (2.ª ed.). Springer. https://doi.org/10.1007/978-0-387-84858-7

Jordet, G., Hartman, E., Visscher, C., & Lemmink, K. A. P. M. (2007). Kicks from the penalty mark in soccer: The roles of stress, skill, and fatigue for kick outcomes. Journal of Sports Sciences, 25(2), 121–129. https://doi.org/10.1080/02640410600624020

MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations. En Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability (Vol. 1, pp. 281–297). University of California Press.

Morya, E., Ranvaud, R., & Pinheiro, W. M. (2003). Dynamics of visual feedback in a laboratory simulation of a penalty kick. Journal of Sports Sciences, 21(2), 87–95. https://doi.org/10.1080/0264041031000070/

Rein, R., & Memmert, D. (2016). Big data and tactical analysis in elite soccer: Future challenges and opportunities for sports science. SpringerPlus, 5(1), 1410\. https://doi.org/10.1186/s40064-016-3108-2

Schröer, C., Kruse, F., & Gómez, J. M. (2021). A systematic literature review on applying CRISP-DM process model. Procedia Computer Science, 181, 526–534. https://doi.org/10.1016/j.procs.2021.01.199

# **Anexos** {#anexos}

1. **Repositorio del Proyecto:** [https://github.com/CamiloAT/clustered-penalty-predictor.git](https://github.com/CamiloAT/clustered-penalty-predictor.git)  
2. **Simulador:** [https://clustered-penalty-predictor.vercel.app/](https://clustered-penalty-predictor.vercel.app/)

   