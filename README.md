# Introducción

Este proyecto tiene como objetivo diseñar y desarrollar un sistema P2P (Peer to Peer) para compartir archivos en un sistema distribuido y descentralizado, utilizando el esquema de red P2P de manera no estructurada. Cada nodo del sistema está compuesto por dos módulos principales: un módulo Servidor y un módulo Cliente, que cuenta con una interfaz de consola para consultar y compartir archivos disponibles. El proyecto empleará tecnologías como gRPC, API REST y Middleware MOM para la comunicación en el sistema distribuido. Se utilizarán instancias AWS EC2 para el despliegue de los nodos, simulando la comunicación de archivos en un sistema descentralizado.

## Arquitectura de la Solución
![Diagrama de Arquitectura - Reto1y2](https://github.com/majogonzalezp/mariajosegonzalez-st0263/assets/89041466/00377676-bd90-47d9-a0e7-8e43ed011a55)

## Servicios de los Componentes del Sistema

### Módulo del Cliente

- *Servicios ECO o DUMMY*: Incluyen servicios para simular la descarga y envío de archivos, aunque la transferencia y sincronización real no se implementará aún.
- *Interfaz en Consola*: El cliente contará con una interfaz en consola para buscar y compartir archivos.

### Módulo del Servidor

- *Listado de Archivos*: Se mostrarán índices de archivos disponibles en cada peer.
- *Concurrencia*: Posibilita la comunicación simultánea con múltiples procesos remotos.
- *Consulta de Recursos*: Se encarga de realizar consultas sobre los archivos disponibles en cada peer.

## Interacción entre Componentes

- *Interacciones entre Nodos P2P*: Los nodos pueden comunicarse entre sí, y la transferencia efectiva de archivos se lleva a cabo directamente entre el nodo poseedor del recurso y el solicitante.
- *Funcionamiento Interno de los Nodos*: Cada nodo consta de dos módulos principales, Servidor y Cliente, además de un main y un gestor de archivos.

## Métodos de Comunicación

- *RPC (Remote Procedure Call)*: Facilita las solicitudes y operaciones entre nodos.

## Middleware

- *API REST*: Para comunicaciones basadas en solicitudes HTTP.
- *gRPC*: Comunicación entre los servidores.

## Plan de Desarrollo

![Plan de desarrolloo](https://github.com/majogonzalezp/mariajosegonzalez-st0263/assets/89041466/df19ee35-f77e-49bd-ae8c-cd005ac96dc6)
