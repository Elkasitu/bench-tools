def main(env):
    Partner = env['res.partner']
    for i in range(1000):
        Partner.create({'name': f'mister_{i}'})
