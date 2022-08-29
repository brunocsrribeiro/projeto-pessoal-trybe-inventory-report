from abc import abstractmethod
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @abstractmethod
    def generate(data_structure):
        simple_report = SimpleReport.generate(data_structure)

        in_stock_product_report = dict()

        for report in data_structure:
            company = report["nome_da_empresa"]

            if company in in_stock_product_report:
                in_stock_product_report[company] += 1
            else:
                in_stock_product_report[company] = 1

        report_co = ""

        for key, value in in_stock_product_report.items():
            report_co += f"- {key}: {value}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{report_co}"
        )
