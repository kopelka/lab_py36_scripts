from xml.dom.minidom import parse
import xml.dom.minidom


def replace_text(node, new_text):
    if node.firstChild.nodeType != node.TEXT_NODE:
        raise Exception("node does not contain text")
    node.firstChild.replaceWholeText(new_text)


if __name__ == '__main__':
    DOMTree = xml.dom.minidom.parse("xml_file.xml")
    collection = DOMTree.documentElement
    meal = collection.getElementsByTagName("food")
    for food in meal:
        print("*****Food*****")
        if food.hasAttribute("name"):
            print("Name: %s" % food.getAttribute("name"))
        price = food.getElementsByTagName('price')[0]
        print("Price: %s" % price.childNodes[0].data)
        calories = food.getElementsByTagName('calories')[0]
        print("Calories: %s" % calories.childNodes[0].data)
        description = food.getElementsByTagName('description')[0]
        print("Description: %s" % description.childNodes[0].data)
        replace_text(description, "New description")

    file_handle = open("xml_file.xml", "w")
    collection.writexml(file_handle)
    file_handle.close()