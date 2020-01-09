from random import randint


def prepare_so_lines(env):
    products = env['product.product'].search([('name', 'like', 'foo%')])

    vals = []
    for prod in products:
        vals.append((0, False, {'product_id': prod.id, 'price_unit': randint(1, 500)}))
    return vals

def main(env):
    AM = env['account.move']
    AM.create({
        'name': 'foobarbazquux',
        'type': 'out_invoice',
        'partner_id': env['res.partner'].search([], limit=1).id,
        'invoice_line_ids': prepare_so_lines(env),
    })
