import sys
from pathlib import Path
import matplotlib.pyplot as plt 
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.helpers import clean_lines, parse_products
from utils.product import Product


def main():
    data_file_path = PROJECT_ROOT / "data" / "raw" / "data.txt"

    if not data_file_path.exists():
        print(f"Error: Data file not found at {data_file_path}")
        return

    with open(data_file_path, "r", encoding="utf-8") as file:
        raw_lines = file.readlines()

    cleaned_lines = clean_lines(raw_lines)

    parsed_tuples = parse_products(cleaned_lines)

    products = [Product(name, price, qty) for name, price, qty in parsed_tuples]

    X= [    p.name for p in products ]
    y= [   p.total_value() for p in products]

    plt.bar(X,y)

    plt.title("total sales by product")
    plt.xlabel("Name Products")
    plt.ylabel("Total Sales")
    plt.show()
    
    


if __name__ == "__main__":
    main()
