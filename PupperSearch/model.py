#!/usr/bin/python

import mysql.connector

class breed:
   breedCount = 0

   def __init__(self, id, name, temperament, coat):
      self.id = id
      self.name = name
      self.temperament = temperament
      self.coat = coat

   def __init__(self, name, temperament, coat):
         self.name = name
         self.temperament = temperament
         self.coat = coat
	  



   def writebreed(self, id, name, temperament, coat):
      print("")

class pupper:
   pupperCount = 0

   def __init__(self, id, name, sex, weight, height, color, birthdate, breed):
      self.id = id
      self.name = name
      self.sex = sex
      self.weight = weight
      self.height = height
      self.color = color
      self.birthdate = birthdate
      self.breed = breed

   def __init__(self, name, sex, weight, height, color, birthdate, breed):
      self.id = id
      self.name = name
      self.sex = sex
      self.weight = weight
      self.height = height
      self.color = color
      self.birthdate = birthdate
      self.breed = breed
	  
   def readpupper(self, id, name, sex, weight, height, color, birthdate, breed):
      print("")
	  
   def writepupper(self, id, name, sex, weight, height, color, birthdate, breed):
      print("")



