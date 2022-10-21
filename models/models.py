from odoo import models, fields

class SaleOrder(models.Model):
    _name = 'sale.order'

    sale_type = fields.Selection(selection=[("national", "National"), ("international", "International")])
    is_international = fields.Boolean(string='Internacional?')
    operator_type = fields.Selection(selection=[("import", "Import"), ("export", "Export")])
    product_id = fields.Many2one('producto.template', string='Código Producto')
    reference_type = fields.Char(string='Referencia')
    is_danger = fields.Boolean(string='Peligroso?')
    value = fields.Float(string='Precio')