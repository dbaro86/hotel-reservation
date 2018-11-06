# Created by duany at 11/6/18
Feature: Listar hoteles
  Como usuario del sistema
  deseo ver todos los hoteles del sistema.

  Scenario Outline: Aplicado a los hoteles
    When el usuario lista los hoteles
    Then se listan los hoteles <name> <city> <country>

    Examples:
    | name          |  city     |  country |
    | Hotel Manzana | La Habana |    Cuba  |
    |    Konly      | La Habana |    Cuba  |