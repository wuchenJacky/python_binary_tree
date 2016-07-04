with open("test.log",mode="w",encoding="utf-8") as a_file:
    a_file.write("test suceeesed")
with open("test.log",encoding="utf-8") as a_file:
    print("{0:>4},{1}".format("1",a_file.read()))
import io
a_string="papayaWhis is the new black."
a_file=io.StringIO(a_string)
print(a_file.read())
print(a_file.read())
print(a_file.tell())
a_file.seek(0)
print(a_file.read(10))
print(a_file.tell())
a_file.seek(18)
print(a_file.read())
