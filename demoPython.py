array = [1, 2, 3, 4, 5, 6]
print(array)
print(array[0:3])
print(array[0:4:1])
map(lambda a: print(a), array)
print(type(array))
print(type(array[1]))
# dir(array)
# help(array)
a1 = array.pop(1)
print(a1)
print(len(array))
str1 = '-'
seq = ('a', 'c', 'c')
print(str1.join(['a', 'c']))


class printDemo(object):
    def printDemoPython(self):
        print("demoPython")
