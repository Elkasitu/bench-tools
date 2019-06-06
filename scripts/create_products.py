from random import randint


def main(env):
    Product = env['product.product']
    for i in range(2000):
        Product.create({'name': 'foo%d' % i, 'description': 'bar%d' % i, 'price': randint(1, 500)})
