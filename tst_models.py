def test_find_by_name(self):
    product = ProductFactory()
    product.create()
    results = Product.find_by_name(product.name)
    self.assertEqual(len(results), 1)
