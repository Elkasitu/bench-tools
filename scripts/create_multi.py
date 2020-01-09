def main(env):
    P = env['product.product']
    P.create([{'name': f"foo_{i}"} for i in range(1000)])
    P.flush()
