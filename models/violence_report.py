from odoo import models, fields

class ViolenceReport(models.Model):
    _name = 'violence.report'
    _description = 'Laporan Tindak Kekerasan'

    name = fields.Char(string='Nama Pelapor', required=True)
    date = fields.Date(string='Tanggal Kejadian', required=True)
    location = fields.Char(string='Lokasi Kejadian', required=True)
    description = fields.Text(string='Deskripsi Kejadian', required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Dikonfirmasi'),
        ('investigated', 'Sedang Diselidiki'),
        ('resolved', 'Selesai'),
    ], string='Status', default='draft')