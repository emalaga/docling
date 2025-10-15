from docling.document_converter import DocumentConverter

source = "https://www.popakademie.de/media/?download=&file=978_241021-ki-whitepaper-en.pdf&utm_source=chatgpt.com"  # file path or URL
converter = DocumentConverter()
doc = converter.convert(source).document

print(doc.export_to_markdown())  # output: "### Docling Technical Report[...]"