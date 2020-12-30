from contextlib import contextmanager

class MessageReader:
    
    @contextmanager
    def open(self):
        try:
            fileread = open("test.txt", 'r')
            yield fileread
        finally:
            fileread.close()

mr = MessageReader()
with  mr.open() as rf:
    print(rf.read())


