import dao as dao
import model as model

def doAction():
    userInput = input("What Action you need : "
                      "\n1 - Find a Breed"
                      "\n2 - Find a Pupper"
                      "\n3 - enter a new Breed"
                      "\n4 - Enter a new Pupper\n:::")
    if(userInput == "1"):
        breadID = int(input("Enter Breed ID : "))
        dao.readBreed(breadID)

    if(userInput == "2"):
        pupperID = int(input("Enter Pupper ID : "))
        dao.readPupper(pupperID)

    if (userInput == "3"):
        breedName = input("Enter Breed Name:")
        temperament = input("Enter Temperament:")
        coat = input("Enter Coat:")
        breedObj = model.breed(breedName,temperament,coat)
        dao.insertBreed(breedObj)


    if (userInput == "4"):
        pupperName = input("Enter Pupper Name:")
        sex = input("Enter Sex:")
        height = input("Enter height:")
        Weight = input("Enter Weight:")
        Weight = input("Enter Weight:")
        Weight = input("Enter Weight:")
        breedObj = model.breed(breedName,temperament,coat)
        dao.insertBreed(breedObj)






doAction()