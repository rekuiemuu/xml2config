import xml.etree.ElementTree as ET

def translate(xml_data):
    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError as e:
        raise SyntaxError(f"Invalid XML: {e}")

    return parse_element(root)

def parse_element(element):
    if element.tag == "root":
        # Обрабатываем все дочерние элементы
        return "\n".join(parse_element(child) for child in element)
    elif element.tag == "dict":
        return parse_dict(element)
    elif element.tag == "comment":
        return f"\\ {element.text.strip()}"
    elif element.tag == "const":
        name = element.get("name")
        value = element.text.strip()
        return f"{name} is {value}"
    elif element.tag == "expr":
        return f"@[{element.text.strip()}]"
    else:
        raise SyntaxError(f"Unknown element: {element.tag}")

def parse_dict(element):
    entries = [
        f"{entry.get('key')} = {entry.text.strip()}" for entry in element.findall("entry")
    ]
    return "{\n  " + "\n  ".join(entries) + "\n}"

