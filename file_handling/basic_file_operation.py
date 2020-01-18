class File:
    def file_read(self):
        """
        Open a file in read mode.
        Note: If the file is not exists then it produce a FileNotFoundError exception.
        :return:
        """
        try:
            file = open('test.txt','r')
            # To read the whole file body
            contents = file.read()
            print("######### Whole File Body is ######### \n",contents)

            # To see the particular lines or particular part of the file
            file_lines = file.readlines()
            print(file_lines)
            for lines in file_lines:
                print(lines)

            file.close()

        except FileNotFoundError:
            print("No File Named 'test.txt'")



    def file_wrtie(self):
        """
        Open a file in write mode
        Here, 1st argument is the file to be opened and second argument is the mode
        Note: if the file is not exists then it will open a new file with same name otherwise open the file
        """
        file = open('test.txt', 'w+')
        # write something in the file
        for i in range(10):
            file.write('line number {} \n'.format(i))
        file.close()  # best practice is to close a file after open
        """
        Note another thing that write mode every time write something in the file after deleting/overwriting 
        everything from that particular file. So one have to pay attention in this regard.
        """

    def file_append(self):
        """
        As we Discussed before that write mode normally write something after deleting the content.
        so if we wants to write something at the end of file content that is if we want to append something
        to existing file content we have to use append mode
        :return:
        """
        file = open('test.txt', 'a+')
        for i in range(10):
            file.write('line number {} \n'.format(i))
        print('append something in the file to see result, open the file')
        file.close()  # best practice is to close a file after open


if __name__ == '__main__':
    f = File()
    f.file_read()
