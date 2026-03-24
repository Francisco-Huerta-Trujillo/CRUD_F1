# 🏎️ F1 Standings API (CRUD Backend en Java)

## 📌 Descripción

Este proyecto consiste en una API RESTful desarrollada en **Java con Spring Boot** que permite gestionar información histórica de la Fórmula 1, específicamente las posiciones de **pilotos (drivers)** y **constructores (equipos)**.

Los datos utilizados provienen de un dataset real de Kaggle que contiene información del campeonato mundial de F1 desde 1950 hasta 2020.

La aplicación implementa operaciones CRUD (*Create, Read, Update, Delete*), permitiendo consultar, registrar, actualizar y eliminar datos de standings.

---

## 🎯 Objetivo

Desarrollar un backend robusto y escalable que demuestre:

* Diseño de APIs REST
* Manejo de datos reales
* Arquitectura en capas
* Buenas prácticas en desarrollo backend

---

## ⚙️ Tecnologías utilizadas

* ☕ Java 17+
* 🌱 Spring Boot
* 🗄️ Spring Data JPA (Hibernate)
* 🐬 MySQL / PostgreSQL
* 📦 Maven
* 🔗 REST APIs

---

## 📊 Fuente de datos

Dataset utilizado:

https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020

Archivos principales:

* `driver_standings.csv`
* `drivers.csv`
* `constructor_standings.csv`
* `constructors.csv`

---

## 🧱 Arquitectura

El proyecto sigue una arquitectura en capas:

* **Controller** → Manejo de endpoints HTTP
* **Service** → Lógica de negocio
* **Repository** → Acceso a base de datos
* **Model** → Entidades

---

## 🚀 Cómo ejecutar el proyecto

### 1. Clonar repositorio

```bash
git clone https://github.com/Francisco-Huerta-Trujillo/CRUD_F1.git
```

### 2. Entrar al proyecto

```bash
cd CRUD_F1
```

### 3. Configurar base de datos

Editar `application.properties` o `application.yml`:

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/f1db
spring.datasource.username=tu_usuario
spring.datasource.password=tu_password
spring.jpa.hibernate.ddl-auto=update
```

### 4. Ejecutar la aplicación

```bash
mvn spring-boot:run
```

---

## 🔌 Endpoints principales

### 🏁 Drivers

* `GET /drivers` → Obtener todos los standings
* `GET /drivers/{id}` → Obtener un driver específico
* `POST /drivers` → Crear nuevo registro
* `PUT /drivers/{id}` → Actualizar registro
* `DELETE /drivers/{id}` → Eliminar registro

---

### 🏎️ Constructors

* `GET /constructors` → Obtener todos los standings
* `GET /constructors/{id}` → Obtener un constructor
* `POST /constructors` → Crear nuevo registro
* `PUT /constructors/{id}` → Actualizar registro
* `DELETE /constructors/{id}` → Eliminar registro

---

## 📌 Ejemplo de JSON

```json
{
  "driverName": "Lewis Hamilton",
  "season": 2020,
  "points": 347,
  "position": 1
}
```

---

## 🧠 Funcionalidades adicionales

* 🔍 Filtros por temporada
* 📊 Ordenamiento por puntos o posición
* ✅ Validación de datos
* ⚠️ Manejo de errores HTTP

---

## 🧪 Pruebas

Puedes probar la API usando:

* Postman
* cURL
* Thunder Client (VS Code)

---

## 📜 Licencia

Este proyecto está bajo la licencia **MIT**.
Puedes usarlo, modificarlo y distribuirlo libremente.

---

## 🙌 Aprendizajes

Durante el desarrollo de este proyecto se reforzaron conocimientos en:

* Arquitectura de software
* Desarrollo backend con Spring Boot
* Integración de datos externos (CSV → DB)
* Buenas prácticas en APIs REST

---

## 🚀 Mejoras futuras

* Autenticación con JWT
* Paginación de resultados
* Documentación con Swagger
* Deploy en la nube (AWS / Docker)

---

## 👨‍💻 Autor

Desarrollado por **Francisco Huerta y Máximo Flores**

---
