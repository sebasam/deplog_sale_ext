from odoo import models, fields

class Order(models.Model):
    _name = 'sales.order'

    sale_type = fields.Selection(['National', 'International'], string='Tipo de venta')
    is_international = fields.Boolean(string='Internacional?')
    operator_type = fields.Selection(['Import', 'Export'], string='Operation')
    product_id = fields.Many2One('producto.template', string='Código Producto')
    reference_type = fields.Char(string='Referencia')
    is_danger = fields.Boolean(string='Peligroso?')
    value = fields.Float(string='Precio')