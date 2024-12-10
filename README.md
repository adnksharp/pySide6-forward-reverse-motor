# Forward-Reverse motor control
![](https://i.imgur.com/1yIAWnF.png)

Control de giro de un motor DC con un puente H, Arduino y Python.

## Requisitos

[FirmataExpress](https://mryslab.github.io/pymata4/firmata_express/#installation-instructions)

### Librerías de Python

- PySide6
- pymata4

```bash
pip install -r requirements.txt
```

### Hardware usado

| ![](https://i.imgur.com/AjvL7W4.png) | ![](https://i.imgur.com/S6z3rQN.png) |
|----|----|

- Placa de Arduino MEGA 2560
- Controlador de motores L298N
- Motor DC 12V 

## Características
- Control de un motor CC con un puente H y dos salidas PWM.
- Configuración del pulso modulado de salida mediante un `slider` y un `spin box`.
- Control de la dirección de salida con dos botones.

### En proceso

> [!TIP]
>
> - `slider` personalizado (rotativo).

