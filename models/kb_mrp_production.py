from odoo import models, fields, api, _
from datetime import date, datetime
from odoo.exceptions import ValidationError

import xlrd
import base64
import os

class kb_mrp_pembahanan(models.Model):
    _name = 'kb.mrp.pembahanan'

    @api.model
    def func_create(self):
        if self.name == "New":
            seq = self.env['ir.sequence'].next_by_code('kb.mrp.pembahanan') or '/'
            self.name = seq

    name = fields.Char(string='No', default="New")
    tahun = fields.Char(string="Tahun")
    tanggal_masuk_oven = fields.Date(string="Tanggal Masuk Oven")
    tanggal_selesai_vakum = fields.Date(string="Tanggal Selesai Vakum")
    tanggal_selesai_stick = fields.Date(string="Tanggal Selesai Stick")
    item = fields.Many2one('product.product', string="Item")
    code = fields.Char(string="Code")
    tebal = fields.Float(string="Tebal")
    pcs = fields.Float(string="PCS")
    m3 = fields.Float(string="M3")
    jenis_kayu = fields.Char(string="Jenis Kayu")
    no_chamber = fields.Char(string="No Chamber")
    tanggal_keluar_oven = fields.Date(string="Tanggal Keluar Oven")
    grade = fields.Char(string="Grade")
    fsc = fields.Char(string="FSC")
    vakum_celup = status = fields.Selection([('vakum','Vakum'),('celup','Celup')])
    shift = fields.Char(string="Shift")
    keterangan = fields.Text(string="Keterangan")
