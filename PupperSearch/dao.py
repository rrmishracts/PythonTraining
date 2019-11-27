import  DBConnector as dbConnector

def readBreed(id):
    read_sql = "select * from pythontest.breed WHERE ID=%s"
    idList = [str(id)]
    dbConnector.readBreed(read_sql,idList)


def readPupper(id):
    read_sql = "select * from pythontest.pupper WHERE ID=%s"
    idList = [str(id)]
    dbConnector.readPupper(read_sql, idList)

def insertBreed(breed):
    insert_sql = "insert into pythontest.breed (name,temperament,coat) values (%s,%s,%s)"
    data = (breed.name,breed.temperament,breed.coat)
    dbConnector.writeBreed(insert_sql, data)


def insertPupper(pupper):
    insert_sql = "insert into pythontest.pupper (name,sex,weight,height,color,date_of_birth,breed_id) values (%s,%s,%s,%s,%s,%s,%s)"
    data = (pupper.name, pupper.sex, pupper.weight, pupper.height, pupper.color, pupper.date_of_birth, pupper.breed_id)
    dbConnector.writePupper(insert_sql, data)

