# -*- coding: utf-8 -*-
from crypt import methods
from odoo import http, models, fields
from odoo.http import request
import json


class Kawagomart(http.Controller):
    @http.route('/kawagomart/getbarang', auth='public', methods=['GET'])
    def getBarang(self, **kw):
        barang = request.env['kawagomart.barang'].search([])
        isi = []
        for bb in barang:
            isi.append({
                'nama_barang': bb.name,
                'harga': bb.harga_jual,
                'stock': bb.stok,
            })
        return json.dumps(isi)

    @http.route('/kawagomart/getsupplier', auth='public', methods=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['kawagomart.supplier'].search([])
        sup = []
        for ss in supplier:
            barang = []
            for bb in ss.barang_id:
                barang.append({'nama_barang': bb.name,
                               'harga_satuan': bb.harga_jual,
                               'stok': bb.stok,
                               })
            sup.append({
                'nama_supplier': ss.name,
                'alamat': ss.alamat,
                'telepon': ss.no_telp,
                'barang': barang,
            })

        return json.dumps(sup)
