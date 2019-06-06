def prepare_so_lines(env):
    SOL = env['sale.order.line']
    products = env['product.product'].search([])

    vals = []
    for prod in products:
        vals.append((0, False, {'product_id': prod.id}))
    return vals

def main(env):
    SO = env['sale.order']
    SO.create({
        'name': 'foobarbazquux',
        'partner_id': env['res.partner'].search([], limit=1).id,
        'order_line': prepare_so_lines(env),
    })
