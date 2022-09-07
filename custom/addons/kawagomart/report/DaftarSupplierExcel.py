from odoo import models, fields


class DaftarSupplierExcel(models.AbstractModel):
    _name = 'report.kawagomart.report_kawagomart.supplier_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, supplier):
        sheet = workbook.add_worksheet('Daftar Supplier')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'Nama Supplier', bold)
        sheet.write(1, 1, 'Alamat', bold)
        sheet.write(1, 2, 'No. Telp', bold)
        sheet.write(1, 3, 'List Barang', bold)
        sheet.write(1, 4, 'Harga Modal', bold)
        sheet.write(1, 5, 'Harga Jual', bold)
        sheet.write(1, 6, 'Stok', bold)
        sheet.write(1, 7, 'Kelompok Barang', bold)
        row = 2
        col = 0

        for obj in supplier:
            sheet.write(row, col, obj.name)
            sheet.write(row, col + 1, obj.alamat)
            sheet.write(row, col + 2, obj.no_telp)
            for x in obj.barang_id:
                sheet.write(row, col + 3, x.name)
                sheet.write(row, col + 4, x.harga_beli)
                sheet.write(row, col + 5, x.harga_jual)
                sheet.write(row, col + 6, x.stok)
                sheet.write(row, col + 7, x.kelompokbarang_id.name)
                row += 1
            row += 1
