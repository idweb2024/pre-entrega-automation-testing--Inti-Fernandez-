@ui
Feature: Login en SauceDemo
  Como usuario registrado
  Quiero iniciar sesión con mis credenciales
  Para acceder al inventario de productos

  Background:
    Given que estoy en la página de login

  @smoke
  Scenario: Login exitoso con credenciales válidas
    When ingreso usuario "standard_user" y clave "secret_sauce"
    Then la URL contiene "inventory.html"

  Scenario Outline: Login fallido - <caso>
    When ingreso usuario "<usuario>" y clave "<clave>"
    Then veo un mensaje de error que contiene "<mensaje>"

    Examples:
      | caso                    | usuario         | clave          | mensaje              |
      | credenciales inválidas  | invalid_user    | wrong_password | do not match         |
      | usuario bloqueado       | locked_out_user | secret_sauce   | locked out           |
      | campos vacíos           |                 |                | Username is required |