def main(env):
    picking = env['stock.picking'].search([('name', '=','WH/OUT/00008')], limit=1)
    product = env['product.product'].search([('name', '=', 'foobar3000')], limit=1)
    lots = env['stock.production.lot'].search([('product_id', '=', product.id)])

    for line, lot in zip(picking.move_line_ids, lots):
        line.lot_id = lot
