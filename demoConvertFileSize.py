sizeSequeue = {1000: ["KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"],
               1024: ["KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"]}


def convertFileSize(size, is_1024=False):
    """
    转换传入的大小
    :param size:
    :param is_1024:
    :return: String
    """
    if size < 0:
        raise ValueError("大小不能小于0")
    mulit=1024 if is_1024 else 1000
    for t in sizeSequeue[mulit]:
        size/=mulit
        if size<mulit:
            return "{0:.1f} {1}".format(size,t)
    raise ValueError("超过最大值")

if __name__=="__main__":
    print(convertFileSize(10000000))
    print(convertFileSize(10000000,True))
