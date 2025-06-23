"""
🧩 Problem: Pluggable Report Generator System

You’re building a system that can generate reports in different formats: PDF, HTML, and Markdown.
More formats may be added in the future by external teams.

Each report generator must:
- Implement a common interface with a generate(data: dict) -> str method.
- Output the report as a string (no need for actual file creation).

🏗 Requirements

1. Interface
   - A base class `ReportGenerator` with a `generate(data: dict)` method.

2. Concrete Generators
   - `PDFReportGenerator`, `HTMLReportGenerator`, and `MarkdownReportGenerator`.
   - Each should return a string simulating the report in their format.

3. Factory
   - `ReportFactory.register_report_format(format_name: str, generator_cls)`
   - `ReportFactory.create_report_generator(format_name: str) -> ReportGenerator`

4. Demo
   - Register all three formats.
   - Generate a report in each format using the factory.

🧠 Bonus
- Raise a ValueError for unknown formats.
- Support registering custom formats from outside the factory module.

✨ Example Usage

ReportFactory.register_report_format("pdf", PDFReportGenerator)
pdf_gen = ReportFactory.create_report_generator("pdf")
output = pdf_gen.generate({"title": "Q2 Report", "body": "Data here."})
print(output)
"""
from enum import Enum
from abc import abstractmethod, ABC
from typing import Dict, Type

class ReportType(Enum):
    PDF = "PDF"
    MARKDOWN = "MARKDOWN"
    HTML = "HTML"

class ReportGenerator(ABC):
    @abstractmethod
    def generate(self, data: dict):
        pass

class HTMLReportGenerator(ReportGenerator):
    @staticmethod
    def generate(data):
        report = ["<div>"]
        for k, v in data.items():
            title = f"\n\t\t<h1>{k}</h1>"
            body = f"\n\t\t<p>{v}</p>"
            container = f"\n\t<div>{title}{body}\n\t</div>"
            report.append(container)
        report.append("\n</div>")
        return ''.join(report)
        
class PDFReportGenerator(ReportGenerator):
    @staticmethod
    def generate(data):
        report = ["\n"]
        for k, v in data.items():
            title = f"{k}: "
            body = f"{v}"
            container = f"\n\t{title}{body}"
            report.append(container)
        report.append("\n")
        return ''.join(report)
        
class MarkdownReportGenerator(ReportGenerator):
    @staticmethod
    def generate(data):
        report = ["\n"]
        for k, v in data.items():
            title = f"{k}: "
            body = f"{v}"
            container = f"## {title}\n{body}\n\n"
            report.append(container)
        report.append("\n")
        return ''.join(report)

class ReportFactory:
    def __init__(self, report_generators: Dict[str, ReportGenerator]):
        self.report_generators = report_generators
    
    def normalize_key(self, key):
        return key.strip().lower()
    
    def register_report_format(self, format_name: str, generator_cls: Type[ReportGenerator]):
        format_name = self.normalize_key(format_name)
        if format_name in self.report_generators:
            raise KeyError("Have a report of that format name already registered.")
        self.report_generators[format_name] = generator_cls
        
    def create_report_generator(self, format_name: str):
        format_name = self.normalize_key(format_name)
        if not format_name in self.report_generators:
            raise ValueError("Do not have a report of that format type registered.")
        return self.report_generators[format_name]()

if __name__ == "__main__":
    factory = ReportFactory({})
    factory.register_report_format("HTML", HTMLReportGenerator)
    factory.register_report_format("PDF", PDFReportGenerator)
    factory.register_report_format("MARKDOWN", MarkdownReportGenerator)
    
    html = factory.create_report_generator("HTML")
    pdf = factory.create_report_generator("PDF")
    markdown = factory.create_report_generator("MARKDOWN")
    
    properties = {"from": "George Ward", "to": "Phillip Mejia", "body": "Hello Phillip!"}
    print(html.generate(properties))
    print(pdf.generate(properties))
    print(markdown.generate(properties))