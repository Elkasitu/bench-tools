def main(env):
    so = env['sale.order'].search([('name', '=', 'foobarbazquux')], limit=1)
    picking = so.picking_ids[0]
    picking.action_assign()
    act = picking.button_validate()
    transfer = env['stock.immediate.transfer'].browse(act['res_id'])
    transfer.process()
