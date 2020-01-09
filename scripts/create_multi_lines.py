def main(env):
    SO = env['sale.order']
    products = env['product.product'].search([], limit=1000)
    partner = env['res.partner'].search([], limit=1)

    vals = []
    for i, p in enumerate(products):
        vals.append({
            'name': f'foobarbaz_{i}',
            'partner_id': partner.id,
            'order_line': [(0, 0, {'product_id': p.id})],
        })
    SO.create(vals)
