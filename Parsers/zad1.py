from xml.sax import make_parser
from xml.sax.saxutils import XMLFilterBase, XMLGenerator


class Project1Filter(XMLFilterBase):
    def __init__(self, new_body, parent=None):
        super().__init__(parent)
        self.body = new_body
        self.check = 0

    def startElement(self, name, attrs):
        super().startElement(name, attrs)
        if name == 'body':
            self.check = 1

    def endElement(self, name):
        super().endElement(name)

    def characters(self, content):
        if self.check:
            super().characters(self.body)
            self.check = 0
        else:
            super().characters(content)


new_xml_body = "Jednak nie"
reader = Project1Filter(new_xml_body, make_parser())

with open('file2.xml', 'w') as f:
    handler = XMLGenerator(f)
    reader.setContentHandler(handler)
    reader.parse('file.xml')
