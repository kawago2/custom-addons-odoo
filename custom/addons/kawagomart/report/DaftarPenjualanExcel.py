from pyexpat import model
from odoo import models, fields, api


class DaftarPenjualanExcel(models.AbstractModel):
    _name = 'report.kawagomart.report_kawagomart.penjualan_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, penjualan):
        sheet = workbook.add_worksheet('Daftar Penjualan')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap), bold)
        sheet.write(1, 0, 'Nama Barang', bold)
        sheet.write(1, 1, 'Nama Pembeli', bold)
        sheet.write(1, 2, 'Tanggal Penjualan', bold)
        sheet.write(1, 3, 'Total Bayar', bold)
        sheet.write(1, 4, 'Detail Penjualan', bold)
        row = 2
        col = 0

        for obj in penjualan:
            sheet.write(row, col, obj.name)
            sheet.write(row, col + 1, obj.nama_pembeli)
            sheet.write(
                row, col + 2, obj.tgl_penjualan.strftime("%m/%d/%Y, %H:%M:%S"))
            sheet.write(row, col + 3, obj.total_bayar)
            sheet.write(
                row, col + 4, obj.detailpenjualan_ids.barang_id.name)
            sheet.write(row, col + 5, obj.detailpenjualan_ids.harga_satuan)
            sheet.write(row, col + 6, obj.detailpenjualan_ids.qty)
            sheet.write(row, col + 7, obj.detailpenjualan_ids.subtotal)
            row += 1
