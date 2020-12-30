class myTmpFileWriter:

    def __enter__(self):
        self.file = open("myFileWriter.tmp", 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with myTmpFileWriter() as tmpWriter:
    tmpWriter.write("This is a test")

