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
        sheet.write(1, 3, 'List Barang', bold)
        sheet.write(1, 4, 'Harga Satuan', bold)
        sheet.write(1, 5, 'Quantity', bold)
        sheet.write(1, 6, 'Subtotal', bold)
        sheet.write(1, 7, 'Total Bayar', bold)
        row = 2
        col = 0

        for obj in penjualan:
            sheet.write(row, col, obj.name)
            sheet.write(row, col + 1, obj.nama_pembeli)
            sheet.write(
                row, col + 2, obj.tgl_penjualan.strftime("%m/%d/%Y, %H:%M:%S"))
            sheet.write(row, col + 7, obj.total_bayar)
            for x in obj.detailpenjualan_ids:

                sheet.write(
                    row, col + 3, x.barang_id.name)
                sheet.write(row, col + 4, x.harga_satuan)
                sheet.write(row, col + 5, x.qty)
                sheet.write(row, col + 6, x.subtotal)
                row += 1
            row += 1
