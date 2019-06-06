def do(env):
    import time
    so = env['sale.order'].search([('name', '=', 'SO020')])
    start = time.time()
    cpy = so.copy()
    print("Elapsed time: %f" % (time.time() - start))
