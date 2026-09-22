# Selectores utilizados — Proyecto Pre-Entrega (SauceDemo)

**Jerarquía aplicada:** `ID` → `data-test` → `name` → `Clase`

## Login (`test_1_login.py`)

| Elemento    | Selector             | Tipo |
|-------------|-----------------------|------|
| Usuario     | `#user-name`           | ID   |
| Contraseña  | `#password`             | ID   |
| Botón Login | `#login-button`         | ID   |

## Catálogo (`test_2_catalogo.py`)

| Elemento                | Selector                                    | Tipo      |
|---------------------------|-----------------------------------------------|-----------|
| Título de sección        | `div.header_secondary_container .title`       | CSS       |
| Tarjeta de producto      | `div.inventory_item`                           | CSS       |
| Nombre del producto      | `[data-test='inventory-item-name']`            | Data-test |
| Precio del producto      | `[data-test='inventory-item-price']`           | Data-test |

## Carrito (`test_3_carrito.py`)

| Elemento                    | Selector                                | Tipo      |
|-------------------------------|--------------------------------------------|-----------|
| Botón "Add to cart"          | `button` (`By.TAG_NAME`, dentro de la tarjeta) | Tag name  |
| Contador del carrito         | `[data-test='shopping-cart-badge']`          | Data-test |
| Ícono del carrito            | `[data-test='shopping-cart-link']`           | Data-test |
| Cantidad en el carrito       | `[data-test='item-quantity']`                | Data-test |
| Descripción del producto     | `[data-test='inventory-item-desc']`          | Data-test |
