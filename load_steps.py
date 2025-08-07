@given('los siguientes productos')
def step_impl(context):
    for row in context.table:
        product = Product(name=row['name'], category=row['category'], ...)
        product.create()
