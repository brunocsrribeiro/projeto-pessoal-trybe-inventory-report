import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(path, encoding="utf-8") as file:
            file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            report_file = list(csv_info for csv_info in file_reader)

        return report_file
