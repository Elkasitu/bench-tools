def main(env):
    P = env['product.product']
    for i in range(1000):
        P.create({'name': f"foo_{i}"})
    P.flush()
