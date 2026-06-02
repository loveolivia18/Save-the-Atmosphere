class Ruimteschip:
   def __init__(self, name, size):
       self.name = name
       self.size = size


       #gameplay
       self.speed = 5
       self.health = 100
       self.lives = 3


       self.boost = False
  
   def myfunc(self):
       print("Hello, my name is " + self.name)


p1 = Ruimteschip("De Zeven Provincies", 50)
p1.myfunc()



class Fragmenten:
	def __init__(self, naam, size, kleur, vorm):
		self.naam: naam
		self.size: size
		self.kleur: kleur
		self.vorm: vorm
	
	p2 = Fragment("Heat stabilizer", 30, "Rood", )
	p3 = Fragment("Toxic filter module", 30, "Green", )
	p4 = Fragment("Dust shield layer", 30, "Brown", )
	p5 = Fragment("Storm dampener", 30, "White", )
	p6 = Fragment("Debris shield", 30, "Zwart", ) 
    p7 = Fragment("Gravitity stabilizer”, 30, “Grey”, )" 
    p8 = Fragment("Cryo regulation core", 30, "Yellow",)

class Planeten:
	def __init__(self, naam, size, vorm)
		self.naam = naam
		self.size = size
		self.vorm = vorm
	
	#p9 = Planeet("Mercurius", 15, cirkel)
	#p10 = Planeet("Venus", 40, cirkel)
	#p11 = Planeet("Mars", 20, cirkel)
	#p12 = Planeet("Jupiter", 50, cirkel)
	#p13 = Planeet("Saturnus", 40, cirkel)
	#p14 = Planeet("Uranus", 40, cirkel)
	#p15 = Planeet("Neptunus", 40, cirkel)

