# evaluacionGit: microservicios para una EPS

Taller práctico de **Ingeniería de Software III (FI303290)**, Universidad Antonio José Camacho (UNIAJC).
Tema: control de versiones con Git y GitHub y gestión de ramas en un proyecto de microservicios para una EPS (Entidad Promotora de Salud).

## Ramas del repositorio

Cada rama tiene un propósito distinto y un contenido diferente. Las ramas **no se fusionan** entre sí.

| Rama | Propósito | Contenido |
|---|---|---|
| `main` | Base estable del proyecto | `README.md`, `eps-microservicios/`, `EstructuraMicroservicios_EPS.docx` |
| `desarrollo` | Trabajo de diseño y desarrollo | Lo de `main` + `Docs/` (arquitectura) + `Algoritmos_pruebas/` |
| `pruebas` | Insumos de validación | Lo de `main` + `Algoritmos_pruebas/` (sin `Docs/`) |

`pruebas` se creó a partir de `main`, no de `desarrollo`. Por eso no tiene la carpeta `Docs/`.

## Estructura de microservicios

```
eps-microservicios/
├── api-gateway/            Punto único de entrada al sistema
├── infraestructura/        Config server, service discovery, message broker y monitoreo
├── servicios/              Microservicios de negocio (cada uno con src/, tests/ y config/)
│   ├── ms-autenticacion/   Usuarios, roles y tokens
│   ├── ms-afiliados/       Afiliados y beneficiarios
│   ├── ms-prestadores/     Red de IPS, sedes y médicos
│   ├── ms-citas/           Agendamiento de citas médicas
│   ├── ms-autorizaciones/  Autorización de servicios de salud
│   ├── ms-historia-clinica/ Atenciones y diagnósticos
│   ├── ms-medicamentos/    Fórmulas y dispensación
│   ├── ms-facturacion/     Copagos y cuentas médicas
│   └── ms-notificaciones/  Correo, SMS y notificaciones push
└── frontend/               Portal de afiliados y portal administrativo
```

El esqueleto solo tiene carpetas, sin código. Git no versiona carpetas vacías, así que cada carpeta tiene un archivo `info.txt` de una línea que describe su propósito.

La explicación detallada de la estructura está en `EstructuraMicroservicios_EPS.docx`.
