@when('busco el producto con nombre "{name}"')
def step_impl(context, name):
    context.browser.visit(context.get_url('/'))
    context.browser.fill('name', name)
    context.browser.find_by_id('search').click()
