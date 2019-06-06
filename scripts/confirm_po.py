def main(env):
    env['purchase.order'].search([('name', '=', 'foobarbazquux')]).button_confirm()
