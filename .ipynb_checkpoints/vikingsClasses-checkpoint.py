import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength= strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health,strength)
        self.name=name
    def attack(self):
        return self.strength
    def battleCry(self):
       return "Odin Owns You All!"
        
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return  "A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, viking):
        self.vikingArmy.append(viking)
            
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        viking_soldier = random.choice(self.vikingArmy)
        saxon_soldier = random.choice(self.saxonArmy)

        damage = viking_soldier.strength
        result = saxon_soldier.receiveDamage(damage)

        if saxon_soldier.health <= 0:
            self.saxonArmy.remove(saxon_soldier)  # Remove dead Saxons

        return result  # Return the result
        
    def saxonAttack(self):
        viking_soldier = random.choice(self.vikingArmy)
        saxon_soldier = random.choice(self.saxonArmy)

        damage = saxon_soldier.strength
        result = viking_soldier.receiveDamage(damage)

        if viking_soldier.health <= 0:
            self.vikingArmy.remove(viking_soldier)  # Remove dead Saxons

        return result  # Return the result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    pass