class AttackingSkills():
    def skills(self):
        print("Dribbling",", Pace")

class DefendingSkills():
    def skills(self):
        print("Strength",", Command")

class Player(AttackingSkills,DefendingSkills):
    def skills(self):
        AttackingSkills.skills(self)
        DefendingSkills.skills(self)
        print("Hardworking")



kante=Player()
kante.skills()