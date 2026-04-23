import csv

def generate_report(results: list, filename: str):

    if not filename.endswith(".csv"):
        filename = f"{filename}.csv"

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = list(results[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)