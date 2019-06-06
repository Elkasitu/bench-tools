def main(env):
    SO = env['sale.order']
    so = SO.search([('name', '=', 'foobarbazquux')])
    so.action_invoice_create()
