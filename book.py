class Book:

    def __init__(self,id=0,name=" ",author=" ",status=1):
        self.bid=id
        self.bname=name
        self.bauthor=author
        self.status = status

    def __str__(self):
        data= str(self.bid) + "," + self.bname + "," + self.bauthor+","+str(self.status)
        return data