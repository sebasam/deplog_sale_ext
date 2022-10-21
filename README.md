# my-first-odoo-module

## Prueba Odoo

Se requiere agregar campos al modelo de sale.order en Odoo, lo ideal sería crear un módulo que herede del __sale_management__ (módulo base).

1. __Crear Campos:__
  - sale_type: Que sea de tipo selection con las opciones (national,
international).
  - Is_international : Campo tipo Boolean.
  - operator_type: Campo de tipo selection con las opciones (import,
export).
  - producto_id: Campo Many2one que relacione el modelo
producto.template.
  - reference_type: Campo de tipo Char.
  - Is_danger: Campo de tipo Boolean.
  - value: Campo de tipo Float.
  
2. __Heredar vistas:__
  - Agregar campos creados a la vista formulario (el orden de los campos y
la ubicación no importa).
  - Agregar campos creados a la vista árbol. formulario (el orden de los
campos y la ubicación no importa).


__NOTA:__ El modulo se debe llamar deplog_sale_ext, debe tener las
dependencias de __sale_management__.
