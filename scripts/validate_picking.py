def main(env):
    picking = env['stock.picking'].search([('name', '=','WH/IN/00008')], limit=1)
    act = picking.button_validate()
    transfer = env['stock.immediate.transfer'].browse(act['res_id'])
    transfer.process()
