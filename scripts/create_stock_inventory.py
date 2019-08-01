def get_line_ids(env, location):
    product = env['product.product'].search([('name', '=', 'foobar3000')])
    lots = env['stock.production.lot'].search([('product_id', '=', product.id)])
    cmd_list = []
    for lot in lots:
        cmd_list.append((0, False, {
            'product_id': product.id,
            'prod_lot_id': lot.id,
            'product_qty': 1,
            'location_id': location.id,
            }))
    return cmd_list


def main(env):
    inv = env['stock.inventory'].search([('name', '=', 'foobarbaz')])
    inv.line_ids = get_line_ids(env, inv.location_id)
    inv._action_done()
