# 📊 Proyecto de Business Intelligence | Papelería PyM

### 🐍 Python | 🗄️ SQL | 📊 Power BI | ⚙️ Automatización | 📈 Data Analytics

## 📌 Descripción del proyecto

Este proyecto simula un entorno empresarial de una cadena de papelerías, donde se desarrolla un flujo integral para la **generación, procesamiento, ingesta, almacenamiento, análisis y visualización de datos de ventas**.

El objetivo principal es integrar herramientas de **Python, SQL y Power BI** para construir una solución de Business Intelligence que permita automatizar procesos operativos, analizar información histórica y transformar datos comerciales en indicadores estratégicos para la toma de decisiones.

El proyecto está estructurado en tres componentes principales:

1. **Python:** generación de datos simulados, automatización de procesos e ingesta de información.
2. **SQL:** consulta, exploración y análisis de datos para responder preguntas de negocio.
3. **Power BI:** modelado de datos, desarrollo de medidas DAX y construcción de dashboards interactivos.

Esta arquitectura permite representar un flujo de trabajo de datos, desde su origen hasta su presentación mediante reportes ejecutivos.

---

## 🎯 Objetivos

- Desarrollar un proceso automatizado para generar y almacenar registros de ventas diarias.
- Implementar funciones reutilizables en Python para facilitar el procesamiento y la gestión de información.
- Construir una base de datos relacional utilizando SQLite3.
- Aplicar consultas SQL para explorar, transformar, agrupar y analizar información comercial.
- Diseñar un modelo de datos que facilite el análisis mediante Power BI.
- Desarrollar indicadores clave de rendimiento (KPIs) utilizando DAX.
- Construir dashboards interactivos para analizar el desempeño comercial.
- Identificar tendencias, oportunidades de mejora y patrones en las ventas.
- Transformar datos operativos en información accionable que contribuya a la toma de decisiones.

---

## 📂 Estructura del proyecto

```text
Proyecto-Papeleria-PyM/
│
├── pym_externo.py
│   └── Funciones de generación, ingesta y consulta
│
├── analisis.ipynb
│   └── Consultas SQL y análisis de negocio
│
├── VentasPrueba.db
│   └── Base de datos SQLite3
│
├── Ventas Papelería PyM.pbix
│   └── Dashboard interactivo desarrollado en Power BI
│
└── README.md
    └── Documentación general del proyecto
```

*Nota: la estructura representa los archivos que componen la solución. Su disponibilidad en GitHub dependerá de cuáles se incorporen al repositorio.*

---

## 🐍 1. pym_externo.py | Procesamiento y automatización

Módulo desarrollado en Python que concentra las funciones necesarias para gestionar el flujo de información comercial de la papelería.

Su objetivo es automatizar la generación y almacenamiento de registros de ventas, reduciendo la intervención manual y facilitando la disponibilidad de información para los procesos analíticos.

### Principales funcionalidades

- Generación de registros de ventas simulados.
- Construcción y manipulación de estructuras de datos mediante Pandas.
- Implementación de funciones reutilizables para el procesamiento de información.
- Ingesta y almacenamiento de datos en SQLite3.
- Automatización de procesos de carga de información.
- Ejecución de consultas SQL desde Python.
- Organización y documentación de funciones para facilitar su mantenimiento.

**Propósito:** construir un proceso de datos organizado y reutilizable que permita simular las operaciones comerciales de una empresa y alimentar una base de datos histórica.

**Habilidades desarrolladas:** Python, Pandas, automatización, SQL, manipulación de datos y fundamentos de Data Engineering.

---

## 🗄️ 2. analisis.ipynb | Análisis de datos con SQL

Notebook desarrollado para explorar y analizar la información comercial almacenada en la base de datos SQLite3.

Este componente se enfoca en transformar consultas SQL en respuestas a preguntas relevantes del negocio, aplicando técnicas de análisis de datos y lógica de negocio.

### Actividades principales

- Exploración de tablas y estructuras de información.
- Aplicación de filtros y condiciones mediante SQL.
- Agrupación de registros y funciones de agregación.
- Implementación de consultas mediante JOIN.
- Uso de subconsultas y expresiones de tabla comunes (CTE).
- Construcción de cálculos condicionales mediante CASE WHEN.
- Análisis de ventas por sucursal, zona y periodo.
- Desarrollo de indicadores comerciales mediante consultas SQL.
- Interpretación de resultados para identificar oportunidades de mejora.

### Preguntas de negocio

- ¿Qué sucursales generan mayores ingresos?
- ¿Cómo evolucionan las ventas durante un periodo determinado?
- ¿Qué zonas comerciales presentan mejores resultados?
- ¿Cuáles son los productos con mayor participación en los ingresos?
- ¿Qué sucursales cumplen con sus objetivos comerciales?
- ¿Cómo se distribuyen los ingresos entre los distintos meses?
- ¿Qué patrones pueden identificarse en las operaciones diarias?

**Propósito:** aplicar SQL como herramienta de análisis para transformar datos almacenados en información relevante para el negocio.

**Habilidades desarrolladas:** SQL básico-intermedio, consultas analíticas, agregaciones, JOIN, CTE, lógica condicional y resolución de preguntas comerciales.

---

## 📊 3. Power BI | Dashboard de análisis comercial

Desarrollo de un dashboard interactivo en Power BI utilizando los datos históricos de ventas almacenados en SQLite3.

El objetivo es integrar procesos de transformación, modelado y visualización de datos para construir una herramienta que permita monitorear el desempeño comercial y facilitar la toma de decisiones.

El tablero incorpora indicadores clave de rendimiento, análisis temporal, comparativos entre sucursales y herramientas interactivas para explorar información.

### 🔧 Preparación y modelado de datos

- Conexión con la información almacenada en SQLite3.
- Transformación y preparación de datos mediante Power Query.
- Construcción de un modelo de datos relacional.
- Implementación de una dimensión de fechas (DimFecha).
- Creación de relaciones entre tablas de hechos y dimensiones.
- Desarrollo de medidas DAX para calcular indicadores comerciales.
- Aplicación de filtros y segmentadores para facilitar la exploración de información.

### 📈 Dashboard principal | Resumen ejecutivo

Página enfocada en proporcionar una visión general del desempeño comercial de la papelería.

**Indicadores principales:**

- **Ventas totales:** ingresos generados durante el periodo seleccionado.
- **Número de tickets:** cantidad de operaciones comerciales registradas.
- **Ticket promedio:** ingreso promedio por transacción.
- **Crecimiento de ventas:** variación porcentual respecto al periodo anterior.

**Análisis visuales:**

- Evolución de las ventas en el tiempo.
- Comparativo de ingresos por sucursal.
- Ranking de productos más vendidos.
- Participación de las sucursales en las ventas.
- Filtros por fecha y sucursal.

Esta página permite identificar rápidamente el comportamiento general de las ventas y detectar variaciones en el rendimiento comercial.

### 📉 Dashboard secundario | Análisis detallado

Página enfocada en profundizar en el comportamiento de las ventas, los productos y el desempeño de las sucursales.

**Análisis desarrollados:**

**1. Análisis ABC de productos**

Clasificación de productos de acuerdo con su contribución a los ingresos, utilizando porcentajes acumulados y medidas DAX.

- Categoría A: productos que representan aproximadamente el primer 80 % de las ventas acumuladas.
- Categoría B: productos que representan el siguiente 15 %.
- Categoría C: productos que representan el porcentaje restante.

Este análisis permite identificar los productos de mayor importancia comercial.

**2. Análisis de rentabilidad**

Evaluación de los resultados económicos mediante indicadores como:

- Ingresos totales.
- Costos asociados a las ventas.
- Utilidad bruta.
- Margen de utilidad.

**3. Análisis temporal**

Evaluación del comportamiento de las ventas mediante:

- Comparativos mensuales.
- Crecimiento respecto al mes anterior.
- Identificación de tendencias.
- Análisis de variaciones comerciales.

**4. Desempeño por sucursal**

Comparación de resultados comerciales para identificar sucursales con mayor participación en las ventas y evaluar su desempeño.

### 🧮 Desarrollo de medidas DAX

Implementación de medidas para construir indicadores dinámicos que respondan a los filtros aplicados en el dashboard.

Entre los cálculos abordados se encuentran:

- Ingresos totales.
- Número de operaciones.
- Ticket promedio.
- Crecimiento porcentual.
- Ranking de productos.
- Porcentaje de participación.
- Porcentaje acumulado de ventas.
- Clasificación ABC.
- Utilidad bruta.

**Propósito:** transformar la información histórica en una herramienta visual e interactiva que facilite la interpretación de resultados, el seguimiento de indicadores y la identificación de oportunidades comerciales.

**Habilidades desarrolladas:** Power BI, Power Query, DAX, modelado dimensional, Data Visualization, KPI Design y Business Intelligence.

---

## 🛠️ Tecnologías y herramientas

| Tecnología | Aplicación |
|---|---|
| Python | Automatización y procesamiento de datos |
| Pandas | Manipulación y preparación de información |
| SQLite3 | Almacenamiento de datos relacionales |
| SQL | Consultas y análisis comercial |
| Google Colab / Jupyter Notebook | Desarrollo de análisis y documentación |
| Power BI Desktop | Construcción de dashboards interactivos |
| Power Query | Transformación y preparación de datos |
| DAX | Desarrollo de medidas e indicadores |
| GitHub | Control de versiones y documentación |

---

## 🔄 Arquitectura y flujo general de datos

**1. Generación de datos — Python**

Simulación de operaciones comerciales y generación de registros de ventas.

⬇️

**2. Procesamiento e ingesta — Python + Pandas**

Preparación de información y automatización de la carga de datos.

⬇️

**3. Almacenamiento — SQLite3**

Persistencia de información histórica en una base de datos relacional.

⬇️

**4. Análisis exploratorio — SQL**

Consultas, agrupaciones, cálculos e identificación de patrones comerciales.

⬇️

**5. Transformación y modelado — Power Query + Power BI**

Preparación de tablas, construcción de relaciones y desarrollo del modelo de datos.

⬇️

**6. Indicadores y análisis — DAX**

Creación de medidas para evaluar el desempeño comercial.

⬇️

**7. Visualización — Power BI**

Construcción de dashboards interactivos para monitorear resultados y apoyar decisiones.

---

## 📈 Valor del proyecto

Este proyecto representa una solución práctica de Business Intelligence que integra diferentes etapas del ciclo de vida de los datos.

Su principal aportación consiste en demostrar cómo una organización puede aprovechar información operativa para construir herramientas analíticas que faciliten el seguimiento de sus resultados comerciales.

Desde una perspectiva técnica, el proyecto permite aplicar conocimientos de automatización, administración de bases de datos, SQL, modelado dimensional, DAX y visualización de información.

Desde una perspectiva de negocio, permite:

- Monitorear el comportamiento de las ventas.
- Identificar productos con mayor contribución a los ingresos.
- Comparar el desempeño entre sucursales.
- Analizar tendencias y variaciones comerciales.
- Evaluar indicadores de rentabilidad.
- Facilitar la interpretación de información para la toma de decisiones.

El enfoque combina habilidades de **Data Analytics, Business Intelligence y fundamentos de Data Engineering**, aplicadas a un caso práctico que representa procesos comunes dentro de un entorno empresarial.

---

## 👨‍💻 Autor

**Jorge Luis Ordoñez García**

*Ingeniero en Sistemas Computacionales | Business Intelligence | Data Analytics*

Proyecto desarrollado como parte del fortalecimiento de habilidades técnicas en Python, SQL, Power BI, automatización y análisis de datos, con un enfoque práctico en la transformación de información operativa en soluciones analíticas para el negocio.

---

⭐ *Los datos por sí solos son registros; su verdadero valor surge cuando se transforman en información que permite comprender el negocio y tomar mejores decisiones.*
