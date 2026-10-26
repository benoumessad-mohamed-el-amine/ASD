

from typing import List, Tuple


def clean_lines_without_comprehension(lines: List[str]) -> List[str]:

    cleaned = []
    for line in lines:
        stripped = line.strip()
        if stripped != "":
            cleaned.append(stripped)
    return cleaned


def clean_lines(lines: List[str]) -> List[str]:
    
    return [line.strip() for line in lines if line.strip() != ""]


def parse_products(lines: List[str]) -> List[Tuple[str, float, int]]:
 
    products: List[Tuple[str, float, int]] = []

    for line in lines:
        parts = [part.strip() for part in line.split(",")]
        if len(parts) != 3:
            continue

        name, price_str, qty_str = parts
        try:
            price = float(price_str)
            quantity = int(qty_str)
            products.append((name, price, quantity))
        except ValueError:
            continue

    return products
