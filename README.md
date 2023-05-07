# Getting Started

#### Aquí encontrarás las Prácticas de Ingeniería de Software a tomar en cuenta para el inicio de un nuevo proyecto.

- [Responsividad](#responsividad) 
- [Transversales](#transversales) 
- [Confiabilidad](#confiabilidad)
- [Costo Eficientes](#costo-eficientes)

  
## Responsividad

### ⚡️ Escalabilidad

-  **Horizontal Pod Autoscaling (Cloud Native)**

Esta practica nos permite definir una capacidad variable en computacion cloud native para una aplicación, garantizando la capacidad suficiente para manejar una carga diferente. El enfoque más directo para lograr tal comportamiento es mediante el uso de un HorizontalPodAutoscaler (HPA) para escalar horizontalmente el numero de pods de la arquitectura.

Toda la información la encuentras en: [HPA - Horizontal Pod Autoscaling](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki/1977/HPA-Horizontal-Pod-Autoscaling) En la wiki de Azure DevOps.

### ⚡️ Performance

-  **Connection pool sizing**

Es como se le conoce comúnmente a la cantidad de conexiones abiertas posibles que se pueden establecer desde un servicio de backend hacia una Base de Datos. Es importante una correcta definicion.

Toda la información la encuentras en: [Connection pool sizing](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki/9493/Connection-pool-sizing) En la wiki de Azure DevOps.

-  **Customizacion JVM Performance**

Cuando se inicia una aplicación Java se pueden especificar diferentes propiedades para personalizar el ambiente de ejecución.Estas propiedades pueden mejorar el uso de recursos, el performance y los tiempos de carga de la aplicación.

Toda la información la encuentras en: [Customizacion JVM Performance](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki/1552/Customizacion-JVM-Performance) En la wiki de Azure DevOps.

  
-  **Optimización dependencias Frontend**

El correcto uso de recursos es fundamental cuando se habla de software con calidad. Es común en un desarrollo que el seguir buenas prácticas de programación, depuración de dependencias y optimizaciones particulares al framework/lenguaje de construcción se traduzca en el uso razonable y esperado de recursos físicos.

Toda la información la encuentras en: [Optimización dependencias Frontend](https://grupoControl-Parental.visualstudio.com/b267af7c-3233-4ad1-97b3-91083943100d/_apis/git/repositories/1b927269-b4fe-422e-bbb7-6c60f64a9938/Items?path=/Lineamientos-Areas-Transversales-de-TI/Ingenier%C3%ADa-de-Software/Pr%C3%A1cticas-Ingenier%C3%ADa-de-Software/Responsividad/Performance/Performance%3A-package.json&download=false&resolveLfs=true&%24format=octetStream&api-version=5.0-preview.1&sanitize=true&versionDescriptor.version=wikiMaster) En la wiki de Azure DevOps.

  
## Transversales

### 📃 Documentación Proyectos

Es importante que los proyectos y las aplicaciones cuenten con la documentación suficiente para tener un entendimiento de la solución. La documentación debería ser relevante y no se debe documentar procesos que se consideren no aporta valor al entendimiento

Toda la información la encuentras en: [Documentación Proyectos](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Transversales/Documentaci%C3%B3n%20Proyectos) En la wiki de Azure DevOps.

  
### 📃 Licenciamiento Open Source

Uno de los criterios importantes a la hora de considerar el uso de una librería, framework o código open source es la licencia que tiene asociada. Elegir de manera inadecuada el uso de un código bajo una licencia específica, puede llegar a tener implicaciones legales para la organización

Toda la información la encuentras en: [Licenciamiento Open Source](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Transversales/Open%20Source/Licencias) En la wiki de Azure DevOps.

  
## Confiabilidad
  
### 🔒 Consistencia en sistemas distribuidos

- **Message Driven**

Cuando hablamos de arquitectura de microservicios, nos referimos en alto nivel a un conjunto de módulos independientes que colaboran para lograr un objetivo de negocio de un alcance mayor. Un sistema reactivo es un sistema distribuido robusto, para lo cual el enfoque de comunicación asíncrona dirigida por mensajes se hace fundamental.

Toda la información la encuentras en: [Message Driven](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Confiabilidad/Message%20Driven) En la wiki de Azure DevOps.


-  **CQRS - Command Query Responsability Segregation**

Es un patron arquitectónico en el que tenemos dos subsistemas diferenciados, uno responsable de los comandos, y otro responsable de las consultas, es decir lectura y escritura van por caminos diferentes.

Toda la información la encuentras en: [CQRS - Command Query Responsability Segregation](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Confiabilidad/Consistencia%20en%20sistemas%20distribuidos/CQRS%20%E2%80%93%20Command%20Query%20Responsabilty%20Segregation) En la wiki de Azure DevOps.

-  **Strong Eventual consistency(ACID 2.0)**

ACID es un acrónimo que significa Atomicity, Consistency, Isolation y Durability, características de las bases de datos SQL, y que básicamente garantizan la consistencia y la disponibilidad pero que no son fácilmente distribuibles o tolerantes al particionamiento como se indica en el teorema CAP.

Toda la información la encuentras en: [Strong Eventual consistency(ACID 2.0)](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Confiabilidad/Consistencia%20en%20sistemas%20distribuidos/Strong%20Eventual%20Consistency%20(ACID%202.0)) En la wiki de Azure DevOps.

  
### 🔒  Tolerancia a fallos

Esto significa que desde el principio sabemos que ocurrirán fallas y que debemos diseñar software y hardware que pueda manejar estas fallas y proporcionar un nivel de servicio aceptable incluso en la presencia de fallas.  

-  **Timeouts en Comunicaciones HTTP**

Mientras construimos u operamos aplicaciones que se comuniquen con otros recursos via HTTP, seguramente hemos encontrado errores como los siguientes:Connect timeout y Response timeout.

Cualquiera de estas dos operaciones tardaron mas de lo esperado, y el llamado fue descartado por el cliente HTTP. Este resultado es conocido como "Timeout".

Toda la información la encuentras en: [Timeouts en Comunicaciones HTTP](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Confiabilidad/Tolerancia%20a%20fallos/Timeouts%20en%20Comunicaciones%20HTTP) En la wiki de Azure DevOps.

  
-  **Circuit breakers and Fallback strategy**

Existen fallas que pueden tener una afectacion alta en dónde se ven implicados servicios de alta demanda. Si es uno de estos casos puede que reintentar implique un bloqueo en la petición y al hacer muchas peticiones se tengan muchas conexiones concurrentes abiertas bloqueadas esperando una respuesta que muy probablemente va a fallar lanzando un timeout.Allí es dónde aparece el concepto Circuit Breaker.

Toda la información la encuentras en: [Circuit breakers and Fallback strategy](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Confiabilidad/Tolerancia%20a%20fallos/Circuit%20breakers%20and%20Fallback%20strategy) En la wiki de Azure DevOps.

  
-  **Health Check**

El monitoreo es una práctica fundamental para conocer el estado de salud de los servicios y tomar acciones tempranas con el fin de ofrecer una alta disponibilidad.

Toda la información la encuentras en: [Health Check](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Confiabilidad/Tolerancia%20a%20fallos/Health%20Check) En la wiki de Azure DevOps.

  
-  **Idempotencia**

Es normal que las aplicaciones reintenten de forma automática peticiones fallidas a otros sistemas o que un usuario realice la misma acción ante una situación fallida de una solicitud. Es allí donde la idempotencia toma relevancia.

Toda la información la encuentras en: [Idempotencia](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Confiabilidad/Tolerancia%20a%20fallos/Idempotencia) En la wiki de Azure DevOps.

  
-  **Concurrency Safe Code**

Los hilos son una característica ineludible del lenguaje Java, y pueden simplificar el desarrollo de sistemas complejos convirtiendo el complicado código asíncrono en un código de línea recta más simple. La programación concurrente es más difícil que la de un solo hilo, porque más cosas pueden salir mal, y los fallos pueden ser difíciles de reproducir. El objetivo de este documento, es conocer en detalle las diferentes tecnicas para ayudarle a escribir programas concurrentes claros, correctos y bien documentados.

Toda la información la encuentras en: [Concurrency Safe Code](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Confiabilidad/Tolerancia%20a%20fallos/Concurrency%20Safe%20Code%E2%80%8B) En la wiki de Azure DevOps.

  
-  **Contenerización**

Es la practica de desarrollar, envíar y ejecuten aplicaciones distribuidas.

Toda la información la encuentras en: [Contenerización](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Confiabilidad/Tolerancia%20a%20fallos/Contenerizaci%C3%B3n) En la wiki de Azure DevOps.

-  **Monitoreo**

Los sistemas de trazabilidad y observabilidad ayudan a verificar que los desarrollos estén refinados y funcionando de forma correcta. Además, ayuda a los analistas a comprender algún comportamiento de la plataforma extraño y garantizar que no exista ningún método fallando.

Toda la información la encuentras en: [Monitoreo](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Confiabilidad/Tolerancia%20a%20fallos/Monitoreo) En la wiki de Azure DevOps.

  
### 🔒 Seguridad
-  **Autenticación-Autorización**

Se debe tener un modelo seguro para autenticar y autorizar los usuarios en nuestras soluciones.

Toda la información la encuentras en: [utenticación-Autorización](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Confiabilidad/Seguridad/Autenticaci%C3%B3n%20%252D%20Autorizaci%C3%B3n) En la wiki de Azure DevOps.

  
### 🔒 Desarollo Seguro
-  **Manejo de Secretos**

La administración y acceso a secretos tales como credenciales de acceso, llaves RSA y otro conjunto de información sensible debe ser realizada bajo un esquema seguro y fácil, que le permitan a las aplicaciones y administradores acceder y modificar dicha información de manera oportuna

Toda la información la encuentras en: [Manejo de Secretos](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Confiabilidad/Seguridad/Desarrollo%20seguro/Instructivo%20%252D%20Secretos) En la wiki de Azure DevOps.

-  **Headers de Seguridad**

Estos son los headers de seguridad que los proyectos deberán implementar en sus soluciones tecnológicas, de tal manera que se mitiguen problemas de seguridad ya identificados. A continuación podrá encontrar un listado y explicación de qué headers deberá implementar y a qué niveles, e igualmente se listarán otros headers que nunca deberá emitir en una respuesta.

Toda la información la encuentras en: [Headers de Seguridad](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Confiabilidad/Seguridad/Desarrollo%20seguro/Headers%20de%20Seguridad) En la wiki de Azure DevOps.

  
-  **Manejo de excepciones en Java**

El Correcto manejo de las excepciones es necesario para controlar los efectos no deseados y procesarlos de forma adecuada.

Toda la información la encuentras en: [Manejo de excepciones en Java](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Confiabilidad/Seguridad/Desarrollo%20seguro/Buenas%20pr%C3%A1cticas%20para%20manejo%20excepciones%20en%20Java) En la wiki de Azure DevOps.

  
## Costo Eficientes

### 💵 Diseño Efectivo 
-  **Haz tu propio DDD e Event Stoarming**

Hemos habilitado en Ingeniería de Software los insumos fundamentales para que así los equipos tengan completa autonomía en la etapa de Diseño Aplicativo y así puedan acelerar aun más el proceso de desarrollo. A continuación los dejamos a su disposición:

Toda la información la encuentras en: [Haz tu propio DDD e Event Stoarming](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Confiabilidad/Seguridad/Desarrollo%20seguro/Buenas%20pr%C3%A1cticas%20para%20manejo%20excepciones%20en%20Java) En la wiki de Azure DevOps.


### 💵 Eficiencia de Desarrollo

-  **Sistema de diseño** 

Un sistema de diseño es un conjunto de componentes visuales que se pueden reutilizar en diferentes combinaciones, permitiendo escalar fácilmente el diseño de una interfaz digital. Este permite generar piezas de desarrollo front end, que aceleran la creación de experiencias digitales (web, aplicaciones, etc), pero manteniendo nuestro estándar de diseño entre todas ellas.

Toda la información la encuentras en: [Sistema de diseño](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Costo%20Eficientes/Eficiencia%20Desarrollo/Sistema%20de%20dise%C3%B1o) En la wiki de Azure DevOps.

  
-  **Feautre Flags**

Es una técnica muy utilizada por las nuevas arquitecturas y modelos de despliegue que requieren liberación de características de una manera rápida y segura de cara a la experiencia de los usuarios, permitiendo habilitar o deshabilitar características en producción sin necesidad de realizar redespliegues a todos los usuarios o segmentos específicos de usuarios, favorece la práctica de Trunk Based Development, así como las variaciones en caliente de las características en los dispositivos móviles donde es complejo lograr una actualización masiva de todos los usuarios.

Toda la información la encuentras en: [Feature Flags](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Costo%20Eficientes/Eficiencia%20Desarrollo/Feature%20Flags) En la wiki de Azure DevOps.

  
  
### 💵 Mantenibilidad y eficiencia
-  **Tamaño, Clases y Funciones**

Las clases deben tener una responsabilidad concreta y un tamaño reducido, si se abusa de este tamaño la clase tiende a tener más responsabilidades de lo debido.

Toda la información la encuentras en: [Tamaño, Clases y Funciones](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Costo%20Eficientes/Mantenibilidad%20y%20eficiencia/Tama%C3%B1o%20Clases%20y%20Funciones) En la wiki de Azure DevOps.

  
-  **Complejidad Ciclomática**

La complejidad ciclomática ideal para los métodos desarrollados por los analistas del banco no debería superar el umbral de 7, sin embargo para métodos que lo ameriten pueden elevar su complejidad hasta un máximo de 10.

Toda la información la encuentras en: [Complejidad Ciclomática](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Costo%20Eficientes/Mantenibilidad%20y%20eficiencia/Tama%C3%B1o%20Clases%20y%20Funciones) En la wiki de Azure DevOps.

  
-  **Code Style**

El estilo está relacionado con el aspecto del código, codificar con un estilo adecuado aumenta la legibilidad, ayuda a detectar errores y disminuye la cantidad de esfuerzo en el estudio del código cuando requiere ser sometido a una refactorización. La intención de este documento es proporcionar un conjunto de convenciones que permitan unificar el estilo utilizado para la codificación, aumentando la legibilidad, la mantenibilidad y extensibilidad del código.

Toda la información la encuentras en: [Code Style](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Costo%20Eficientes/Mantenibilidad%20y%20eficiencia/Code%20Style) En la wiki de Azure DevOps.

  
- **Clean Architecture Arquitectura Limpia**

Con el fin de garantizar la confiabilidad, resiliencia y una evolución sostenible de los sistemas de software es necesario seguir ciertos principios básicos en su diseño, concepción y construcción, algunos principios pueden tener variaciones según la naturaleza del sistema o la priorización de los atributos de calidad.

Toda la información la encuentras en: [Clean Architecture Arquitectura Limpia](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Costo%20Eficientes/Mantenibilidad%20y%20eficiencia/Clean%20Architecture%20%252D%20Arquitectura%20limpia) En la wiki de Azure DevOps.

  
-  **Constant Code Reviews**

En nuestras practicas de desarrollo de software, es necesario implementar estrategias para mejorar la calidad del código. Los programadores tienen diferentes niveles de experiencia en el desarrollo y los estándares en los lenguajes de programación pueden cambiar por lo que debemos realizar una constante revisión de código.

Toda la información la encuentras en: [Constant Code Reviews](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Costo%20Eficientes/Mantenibilidad%20y%20eficiencia/Constant%20Code%20Reviews%E2%80%8B) En la wiki de Azure DevOps.

  
-  **Acomplamiento y Cohesion de Componentes**

Para determinar la correcta granularidad de los paquetes de una aplicación existen unos principios en los cuales podemos apoyarnos. Al hablar del correcto empaquetamiento de clases y artefactos de software estamos hablando de la correcta segregación de funciones del aplicativo, preparándonos para el crecimiento del mismo de una forma controlada y organizada

Toda la información la encuentras en: [Acomplamiento y Cohesion de Componentes](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Costo%20Eficientes/Mantenibilidad%20y%20eficiencia/Acoplamiento%20y%20Cohesi%C3%B3n%20de%20Componentes) En la wiki de Azure DevOps.

  
-  **Estrategias de despliegue**

El proceso de implementación de software es fundamental en el mundo Cloud Native, ya que es el mecanismo por el cual se envían nuevos desarrollos, módulos, parches y actualizaciones a los usuarios finales. La finalidad de las estrategias de despliegue es permitir el despliegue de aplicaciones, garantizando que el usuario final no experimente inactividad e indisponibilidad mientras navega por los aplicativos.

Toda la información la encuentras en: [Estrategias de despliegue](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Costo%20Eficientes/Mantenibilidad%20y%20eficiencia/Estrategias%20de%20despliegue) En la wiki de Azure DevOps.

  
-  **Event Stream Processing**

Es el continuo flujo de datos generados por una o múltiples fuentes de información, cuya información puede ser almacenada, procesada y analizada a medida que se va generando en tiempo real

Toda la información la encuentras en: [Event Stream Processing](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Costo%20Eficientes/Mantenibilidad%20y%20eficiencia/Event%20Stream%20Processing) En la wiki de Azure DevOps.

  
-  **Diseño de APIs**

Al igual que las APIs internas y las APIs públicas, las APIs internas de aplicación deben seguir un estándar para ser diseñadas y documentadas.

Toda la información la encuentras en: [Diseño de APIs](https://grupoControl-Parental.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_wiki/wikis/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa.wiki?wikiVersion=GBwikiMaster&pagePath=/Lineamientos%20Areas%20Transversales%20de%20TI/Ingenier%C3%ADa%20de%20Software/Pr%C3%A1cticas%20Ingenier%C3%ADa%20de%20Software/Costo%20Eficientes/Mantenibilidad%20y%20eficiencia/Pr%C3%A1ctica%20Dise%C3%B1o%20de%20APIs%20internas) En la wiki de Azure DevOps.