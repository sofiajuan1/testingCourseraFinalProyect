import factory
from factory.fuzzy import FuzzyChoice
from service.models import Product

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker("word")
    category = factory.Faker("word")
    available = FuzzyChoice(choices=[True, False])
    price = factory.Faker("pydecimal", left_digits=4, right_digits=2, positive=True)
    quantity = factory.Faker("random_int", min=1, max=100)
