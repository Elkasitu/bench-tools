def do(env):
    import time
    invoice = env['account.invoice'].search([('reference', '=', 'bar')])
    start = time.time()
    invoice.action_invoice_open()
    print("Elapsed time: %f" % (time.time() - start))
