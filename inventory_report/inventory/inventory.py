import csv
import json
from xml.etree import ElementTree as ET
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def file_csv(cls, path, report_type):
        with open(path, encoding="utf-8") as file:
            file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            report_file = list(csv_info for csv_info in file_reader)

        if report_type == "simples":
            return SimpleReport.generate(report_file)
        else:
            return CompleteReport.generate(report_file)

    @classmethod
    def file_json(cls, path, report_type):
        with open(path, encoding="utf-8") as file:
            file_reader = json.loads(file.read())

        if report_type == "simples":
            return SimpleReport.generate(file_reader)
        else:
            return CompleteReport.generate(file_reader)

    @classmethod
    def file_xml(cls, path, report_type):
        with open(path, encoding="utf-8") as file:
            file_reader = ET.parse(file).getroot()
            report_file = list(
                {info.tag: info.text for info in xml_info}
                for xml_info in file_reader
            )

        if report_type == "simples":
            return SimpleReport.generate(report_file)
        else:
            return CompleteReport.generate(report_file)

    @classmethod
    def import_data(cls, path, report_type):
        if path.endswith(".csv"):
            return cls.file_csv(path, report_type)

        if path.endswith(".json"):
            return cls.file_json(path, report_type)

        if path.endswith(".xml"):
            return cls.file_xml(path, report_type)
