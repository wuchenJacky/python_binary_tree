import sys


class RedirectStdoutTo:
    def __init__(self,out_new):
        self.out_new=out_new
    def __enter__(self):
        self.out_old=sys.stdout
        sys.stdout=self.out_new
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout=self.out_old

class RdirectStderrTo:
    def __init__(self,error_new):
        self.error_new=error_new
    def __enter__(self):
        self.error_old=sys.stderr
        sys.stderr=self.error_new
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stderr=self.error_old

print("A")

with open("out.log",mode="w",encoding="utf-8") as a_file,RdirectStderrTo(a_file):
    print("B")
    try:
        print("ss{1}".format(1))
    except Exception:
        sys.stderr.write("test")
    finally:
        pass
print("C")
