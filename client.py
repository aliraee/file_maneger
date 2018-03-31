import socket
def main ():

    host = "127.0.0.1"
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    filename = raw_input("Filename?")

    if filename !="q":
        s.send(filename)
        data = s.recv(1024)
        if data [:6] == 'EXISTS':
            filesize = long (data[6:])
            message = raw_input("File Exists  , "+str(filesize)+ \
                                "BYTES .Download? (Y/N)")
            if message == "Y":
                s.send('OK')
                f = open("NEW" + filename , 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize :
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print("(0:.2f)".format((totalRecv/float(filesize))*100)+\
                          "\Done")
                    print("DOwnload Complete")
        else:

            print("FILE does not Exists!!")

    s.close()


if __name__=="__main__":
    main()
