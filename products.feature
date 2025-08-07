Scenario: Buscar producto por nombre
  Given los siguientes productos
    | name    | category | available | price | quantity |
    | Laptop  | Tech     | True      | 1200  | 10       |
  When busco el producto con nombre "Laptop"
  Then debería ver el producto "Laptop" en la lista
