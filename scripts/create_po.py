from datetime import datetime
from random import randint


def prepare_po_lines(env):
    SOL = env['purchase.order.line']
    products = env['product.product'].search([])

    vals = []
    for i, prod in enumerate(products):
        vals.append((0, False, {
            'name': 'foo%d' % i, 'product_id': prod.id, 'date_planned': datetime.now(),
            'product_uom': 1, 'price_unit': randint(1, 20), 'product_qty': randint(1, 500),
        }))
    return vals


def main(env):
    SO = env['purchase.order']
    SO.create({
        'name': 'foobarbazquux',
        'partner_id': env['res.partner'].search([], limit=1).id,
        'order_line': prepare_po_lines(env),
    })
