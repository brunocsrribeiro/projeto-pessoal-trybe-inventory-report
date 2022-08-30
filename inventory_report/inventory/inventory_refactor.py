from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor:
    def __init__(self, Importer):
        self.importer = Importer
        self.inventory_report = list()

    def __iter__(self):
        return InventoryIterator(self.inventory_report)

    def import_data(self, path, report_type):
        self.inventory_report += self.importer.import_data(path)

        if report_type == "simples":
            return SimpleReport.generate(self.inventory_report)

        if report_type == "completo":
            return CompleteReport.generate(self.inventory_report)
