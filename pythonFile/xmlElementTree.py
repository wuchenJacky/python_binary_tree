import xml.etree.ElementTree as etree
tree=etree.parse("D:/TRPACS/PrintServer/Config/RisVerify.xml")
root=tree.getroot()
print(root)
for child in root:
    print(child)
    print(child.attrib)
txt=input("输入信息：")
print(txt)