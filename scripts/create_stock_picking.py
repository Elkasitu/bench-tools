def main(env):
    env['stock.picking'].create({
        'name': 'foobarbaz',
        'picking_type_id': env['stock.picking.type'].search([], limit=1).id,
    })
