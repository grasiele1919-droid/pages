import sys
import zipfile
import xml.etree.ElementTree as ET

def docx_to_text(path):
    with zipfile.ZipFile(path) as z:
        with z.open('word/document.xml') as f:
            tree = ET.parse(f)
            root = tree.getroot()
            # Namespaces
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            texts = []
            for paragraph in root.findall('.//w:p', ns):
                parts = []
                for node in paragraph.findall('.//w:t', ns):
                    parts.append(node.text or '')
                texts.append(''.join(parts))
            return '\n\n'.join(texts)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python extract_docx_text.py <file.docx>')
        sys.exit(2)
    path = sys.argv[1]
    try:
        text = docx_to_text(path)
        out = path + '.txt'
        with open(out, 'w', encoding='utf-8') as f:
            f.write(text)
        print(out)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
