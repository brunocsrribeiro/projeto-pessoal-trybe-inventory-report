from inventory_report.importer.importer import Importer
from xml.etree import ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(path, encoding="utf-8") as file:
            file_reader = ET.parse(file).getroot()
            report_file = list(
                {info.tag: info.text for info in xml_info}
                for xml_info in file_reader
            )

        return report_file
