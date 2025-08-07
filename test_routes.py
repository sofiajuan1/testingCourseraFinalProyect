def test_get_product_by_name(self):
    product = ProductFactory()
    product.create()
    response = self.client.get(f"/products?name={product.name}")
    self.assertEqual(response.status_code, status.HTTP_200_OK)
