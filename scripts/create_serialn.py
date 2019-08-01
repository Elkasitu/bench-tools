def main(env):
    Lot = env['stock.production.lot']
    p = env['product.product'].create({
        'name': 'foobar3000', 'description': 'foobar', 'price': 5, 'tracking': 'serial',
    })
    vals_list = []
    for i in range(10000):
        vals_list.append({'product_id': p.id})
    Lot.create(vals_list)
