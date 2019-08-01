def main(env):
    invoice = env['account.move'].search([('invoice_origin', '=', 'foobarbazquux')])
    invoice.post()
