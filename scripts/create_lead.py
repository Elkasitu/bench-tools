def do(env):
    Lead = env['crm.lead']
    vals_list = []
    import time
    start = time.time()
    for i in range(1000):
        vals_list.append({
            'name': 'foo%d' % i,
            'partner_id': env['res.partner'].search([], limit=1).id,
            'user_id': 2,
        })
    Lead.create(vals_list)
    print("Elapsed time: %f" % (time.time() - start))
