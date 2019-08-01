def main(env):
    SO = env['sale.order']
    so = SO.search([('name', '=', 'foobarbazquux')])
    env['sale.advance.payment.inv'].create({}).with_context(**{
        'active_model': 'sale.order',
        'active_ids': so.ids,
        'active_id': so.id,
    }).create_invoices()
