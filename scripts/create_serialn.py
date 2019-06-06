def main(env):
    Lot = env['stock.production.lot']
    product = env['product.product'].search([('name', '=', 'foobar3000')], limit=1)
    vals_list = []
    for i in range(10000):
        vals_list.append({'product_id': product.id})
    Lot.create(vals_list)
