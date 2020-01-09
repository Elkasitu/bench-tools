def main(env):
    po = env['purchase.order'].search([('name', '=', 'foobarbazquux')])
    po.copy()
