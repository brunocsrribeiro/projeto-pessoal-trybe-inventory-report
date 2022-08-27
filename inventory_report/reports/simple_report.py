from abc import abstractmethod
from datetime import date


class SimpleReport:
    @abstractmethod
    def manufacture(data_structure):
        oldest_manufacture = list()
        for report in data_structure:
            oldest_manufacture.append(report["data_de_fabricacao"])

        return oldest_manufacture

    @abstractmethod
    def expiration(data_structure):
        expire = list()
        for report in data_structure:
            if report["data_de_validade"] >= date.strftime(
                    date.today(), "%Y-%m-%d"):
                expire.append(report["data_de_validade"])
        return expire

    @abstractmethod
    def company(data_structure):
        companies = list()
        for report in data_structure:
            companies.append(report["nome_da_empresa"])
        return companies

    @abstractmethod
    def generate(data_structure):
        oldest_manufacture = min(SimpleReport.manufacture(data_structure))

        nearest_expiration_date = min(SimpleReport.expiration(data_structure))

        companies = SimpleReport.company(data_structure)
        company_with_more_products = max(set(companies), key=companies.count)

        return (
            f"Data de fabricação mais antiga: {oldest_manufacture}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
