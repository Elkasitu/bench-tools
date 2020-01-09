def main(env):
    so = env['sale.order'].search([('name', '=', 'foobarbazquux')])
    so.copy()
