def main(env):
    Partner = env['res.partner']
    Partner.create([{'name': f'mister_{i}'} for i in range(1000)])
