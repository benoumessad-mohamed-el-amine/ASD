class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name: str = name
        self.price: float = float(price)
        self.quantity: int = int(quantity)

    def total_value(self) -> float:
        return self.price * self.quantity

    def __repr__(self) -> str:
        return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"

