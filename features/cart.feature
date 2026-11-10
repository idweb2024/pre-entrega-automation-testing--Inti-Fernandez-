@ui @regression
Feature: Carrito de compras en SauceDemo
  Como usuario logueado
  Quiero agregar productos al carrito
  Para poder comprarlos después

  Background:
    Given que inicié sesión con usuario "standard_user" y clave "secret_sauce"

  Scenario: Agregar un producto al carrito
    When agrego el producto "Sauce Labs Backpack" al carrito
    Then el contador del carrito muestra "1"