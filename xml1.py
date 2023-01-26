import xml.etree.ElementTree as ET

data = """
<person>
    <name>Isuru</name>
    <phone type="intl">0763222186</phone>
    <email hide="yes"/>
</person>

"""
tree = ET.fromstring(data)
print("name : ",tree.find("name").text)
print("name : ",tree.find("email").get("hide"))