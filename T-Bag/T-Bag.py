import os
from colorama import Fore, init
import random

init(autoreset=True)
clear = lambda: os.system('cls')

RED = Fore.LIGHTRED_EX
BLUE = Fore.LIGHTBLUE_EX
GREEN = Fore.LIGHTGREEN_EX
CYAN = Fore.LIGHTCYAN_EX
MAGENTA = Fore.LIGHTMAGENTA_EX
YELLOW = Fore.LIGHTYELLOW_EX
WHITE = Fore.LIGHTWHITE_EX
RESET = Fore.RESET

class Weapon:
	def __init__(self):
		self.style_list = ["SWORD","MAUL","AXE","DAGGER","WAND","STAFF"]
		self.att_list = ["SLASHED","BASHED","CHOPPED","STABBED","BLASTED","WACKED"]
		self.die_opt = [4, 6, 8, 10, 12]
		self.rarity_opt = [WHITE, GREEN, BLUE, YELLOW, MAGENTA]

		self.t = random.randint(0, 5)
		self.w = random.choices([0,1,2,3,4], weights=[500, 200, 100, 50, 1])

		self.style = self.style_list[self.t]
		self.att = self.att_list[self.t]
		self.die = self.die_opt[self.w[0]] # weapon damage 1d(x)
		self.rarity = self.rarity_opt[self.w[0]] # color of weapon
		self.stat_up = random.choice(["STR","DEX","WIS"]) # stat that gets an inc
		self.stat_up_num = random.randint(1, 3) # inc to stats

	def print_loot(self, C=True):
		if C == True:
			clear()
		if p.has_weapon == True:
			print(f"{MAGENTA} -= Equiped =-")
			print(f"<Type>   <{equiped.rarity}{equiped.style}{RESET}>")
			print(f"<Attack> <{RED}{equiped.att}{RESET}>")
			print(f"<Damage> <d{RED}{equiped.die}{RESET}>")
			print(f"<Bonus>  <+{equiped.stat_up_num} {equiped.stat_up}{RESET}>\n")
		print(f"{MAGENTA} -= LOOT =-")
		print(f"<Type>   <{w.rarity}{w.style}{RESET}>")
		print(f"<Attack> <{RED}{w.att}{RESET}>")
		print(f"<Damage> <d{RED}{w.die}{RESET}>")
		print(f"<Bonus>  <+{w.stat_up_num} {w.stat_up}{RESET}>\n")

class Player:
	def __init__(self, name):
		self.name = name
		self.lv = 1
		self.max_hp = 100
		self.hp = self.max_hp
		self.max_mana = 30
		self.mana = self.max_mana
		self.ac = 8
		self.exp = 0
		self.STR = 1 # damage modifier
		self.DEX = 1 # hit modifier
		self.CON = 1 # health modifier
		self.WIS = 1 # spell damage modifier
		self.INT = 1 # spell hit modifier / max mana
		self.has_weapon = False
		self.dice = 1
		self.exp_2_lv = 10

	def regen_mana(self):
		if self.mana <= self.max_mana - 5:
			self.mana += 5
		else:
			self.mana = self.max_mana

	def is_alive(self):
		if self.hp > 0:
			return True
		else:
			self.hp = 0
			return False

	def add_lv_point(self):
		self.exp -= self.exp_2_lv
		self.exp_2_lv *= 1.5
		while(True):
			self.print_stats()
			skill = input("(1) points left: STR|DEX|CON|WIS|INT\n> ")
			skill = skill.upper()
			if skill == "STR" and self.STR < 10:
				self.STR += 1
				break
			elif skill == "DEX" and self.DEX < 10:
				self.DEX += 1
				break
			elif skill == "CON" and self.CON < 10:
				self.CON += 1
				self.max_hp += 10
				self.hp += 10
				break
			elif skill == "WIS" and self.WIS < 10:
				self.WIS += 1
				break
			elif skill == "INT" and self.INT < 10:
				self.INT += 1
				self.max_mana += 10
				self.mana += 10
				break
			else:
				print("Enter STR|DEX|CON|WIS|INT")
		self.lv += 1
		self.hp = self.max_hp
		self.mana = self.max_mana
		if self.lv%5 == 0:
			self.dice += 1
		self.print_stats(True)
		input("Press enter")

	def check_DEX(self):
		stat = self.DEX 
		if equiped.stat_up == "DEX":
			stat += equiped.stat_up_num
		else:
			pass
		if stat >= 13:
			return 5
		elif stat >= 12:
			return 4
		elif stat >= 9:
			return 3
		elif stat >= 6:
			return 2
		else:
			return 1
	def check_STR(self):
		stat = self.STR 
		if equiped.stat_up == "STR":
			stat += equiped.stat_up_num
		if stat >= 13:
			return 5
		elif stat >= 12:
			return 4
		elif stat >= 9:
			return 3
		elif stat >= 6:
			return 2
		else:
			return 1
	def check_WIS(self):
		stat = self.WIS 
		if equiped.stat_up == "WIS":
			stat += equiped.stat_up_num
		if stat >= 13:
			return 5
		elif stat >= 12:
			return 4
		elif stat >= 9:
			return 3
		elif stat >= 6:
			return 2
		else:
			return 1

	def print_stats(self, l=False):
		clear()
		print(f"<Name>{WHITE}{self.name}")
		if l == True:
			print(f"<lv>  {RED}{str(self.lv)}{MAGENTA} -LEVEL UP-")
		else:
			print(f"<lv>  {RED}{str(self.lv)}")

		if self.hp < 10:
			print(f"<HP> {RED}{str(self.hp)}{WHITE}/{GREEN}{str(self.max_hp)}")
		elif self.hp < self.max_hp:
			print(f"<HP> {YELLOW}{str(self.hp)}{WHITE}/{GREEN}{str(self.max_hp)}")
		else:
			print(f"<HP>  {GREEN}{str(self.hp)}{WHITE}/{GREEN}{str(self.max_hp)}")

		print(f"<Mana>{CYAN}{str(self.mana)}{WHITE}/{CYAN}{str(self.max_mana)}")
		print(f"<AC>  {BLUE}{str(self.ac)}")
		print("<STR> "+YELLOW+(str(self.STR+equiped.stat_up_num) if equiped.stat_up=="STR" and self.has_weapon==True else str(self.STR))+WHITE+"/"+YELLOW+"10")
		print("<DEX> "+YELLOW+(str(self.DEX+equiped.stat_up_num) if equiped.stat_up=="DEX" and self.has_weapon==True else str(self.DEX))+WHITE+"/"+YELLOW+"10")
		print(f"<CON> {YELLOW}{str(self.CON)}{WHITE}/{YELLOW}10")
		print("<WIS> "+YELLOW+(str(self.WIS+equiped.stat_up_num) if equiped.stat_up=="WIS" and self.has_weapon==True else str(self.WIS))+WHITE+"/"+YELLOW+"10")
		print(f"<INT> {YELLOW}{str(self.INT)}{WHITE}/{YELLOW}10")
		print("<Weapon> "+MAGENTA+("<UNARMED>" if p.has_weapon==False else equiped.rarity+equiped.style+WHITE+" <+"+str(equiped.stat_up_num)+" "+equiped.stat_up+">"))
		print(f"<Armor>  {MAGENTA}<NONE>\n")

	def display_player_stats(self, C=True):
		if C == True:
			clear()
		print(f"Lv: {RED}{str(self.lv)}    {WHITE}{self.name}")
		print("["+GREEN+("|"*int(self.hp/(self.max_hp/20)))+(" "*(20-int(self.hp/(self.max_hp/20))))+RESET+"]"+GREEN+str(self.hp)+WHITE+"/"+GREEN+str(int(self.max_hp)))
		print("["+CYAN+(">"*int(self.mana/(self.max_mana/20)))+(" "*(20-int(self.mana/(self.max_mana/20))))+RESET+"]"+CYAN+str(self.mana)+WHITE+"/"+CYAN+str(self.max_mana))
		print("["+YELLOW+(":"*int(self.exp/(self.exp_2_lv/20)))+(" "*(20-int(self.exp/(self.exp_2_lv/20))))+RESET+"]"+YELLOW+str(int(self.exp))+WHITE+"/"+YELLOW+str(int(self.exp_2_lv)))
	
	def display_options(self):
		print("[ "+WHITE+"("+RED+"A"+WHITE+")"+RED+"TTACK"+RESET+" ][ "+WHITE+"("+GREEN+"S"+WHITE+")"+GREEN+"TATS"+RESET+" ]")
		print("[ "+WHITE+"("+CYAN+"M"+WHITE+")"+CYAN+"AGIC"+RESET+"  ][  "+WHITE+"("+YELLOW+"R"+WHITE+")"+YELLOW+"UN"+RESET+"  ]")

class Monster:
	def __init__(self):
		self.mon_type_opt = ['Zombie', 'Demon', 'Goblin', 'Orc', 'Ghost', 'Cyclops', 'Wolf']

		self.mon_lv = p.lv
		self.mon_type = random.choice(self.mon_type_opt)
		self.mon_max_hp = (self.mon_lv * random.randint(1,5))+ random.randint(10, 50)
		self.mon_hp = self.mon_max_hp
		self.mon_ac = random.randint(7, 12)

		if self.mon_lv >= 15:
			self.mon_dice = 3
			self.mon_die = 12
		elif self.mon_lv >= 10:
			self.mon_dice = 2
			self.mon_die = 8
		else:
			self.mon_dice = 1
			self.mon_die = 4

		self.mon_hit_mod = self.mon_dice
		self.mon_dam_mod = self.mon_dice
		self.mon_exp = random.randint(1, 10) * self.mon_lv

	def is_avile(self):
		if self.mon_hp > 0:
			return True
		else:
			self.mon_hp = 0
			return False

	def display_monster_stats(self, C=True):
		if C == True:
			clear()
		print(f"Lv: {RED}{str(self.mon_lv)}    {WHITE}{str(self.mon_type)}")
		print("["+GREEN+("|"*int(self.mon_hp/(self.mon_max_hp/20)))+(" "*(20-int(self.mon_hp/(self.mon_max_hp/20))))+RESET+"]"+GREEN+str(self.mon_hp)+WHITE+"/"+GREEN+str(self.mon_max_hp))
		print("\n")




def use_action():
	p.display_options()
	while(True):
		action = input("> ")
		action = action.upper()
		if action == "A":
			att_output = attack_monster()
			dam_output = attck_player()
			m.display_monster_stats()
			p.display_player_stats(False)
			print(att_output + dam_output)
			return
		elif action == "S":
			p.print_stats()
			m.display_monster_stats(False)
			p.display_player_stats(False)
			print("Displaying Stats")
			p.display_options()
		elif action == "M":
			pass
		elif action == "R":
			m.display_monster_stats()
			p.display_player_stats(False)
			print("You got away safely")
			return action
		else:
			m.display_monster_stats()
			p.display_player_stats(False)
			print(f"{RED}-Please enter a valid option-")
			p.display_options()

def loot():
	while True:
		w.print_loot()
		print(f"Do you want to {CYAN}equip{RESET} this Y|N")
		equip = input("> ")
		if equip.upper() == "Y":
			p.has_weapon = True
			equiped = w
			return True
		elif equip.upper() == "N":
			return False
		else:
			pass
def attack_monster():
	hit = random.randint(1,20)
	if hit == 20:
		hit += p.check_DEX()
		if hit >= m.mon_ac:
			if p.has_weapon == False:
				damage = damage_monster(p.dice,4) + damage_monster(p.dice,4)
				m.mon_hp -= damage
				if m.is_avile() == False:
					return f"{WHITE}{m.mon_type}{RESET} had {RED}DIED"
				else:
					return f"{WHITE}You{RESET} criticaly hit the {WHITE}{m.mon_type}{RESET} for {YELLOW}{str(damage)}{RESET}"
			else:
				damage = damage_monster(p.dice, equiped.die) + damage_monster(p.dice, equiped.die)
				m.mon_hp -= damage
				if m.is_avile() == False:
					return f"{WHITE}{m.mon_type}{RESET} had {RED}DIED"
				else:
					return f"{WHITE}You{RESET} criticaly hit the {WHITE}{m.mon_type}{RESET} for {YELLOW}{str(damage)}{RESET}"
		else:
			return f"{WHITE}Your{RESET} attack missed"
	else:
		hit += p.check_DEX()
		if hit >= m.mon_ac:
			if p.has_weapon == False:
				damage = damage_monster(p.dice,4)
				m.mon_hp -= damage
				if m.is_avile() == False:
					return f"{WHITE}{m.mon_type}{RESET} has {RED}DIED"
				else:
					return f"{WHITE}You {RED}PUNCHED{RESET} the {WHITE}{m.mon_type}{RESET} for {RED}{str(damage)}{RESET}"
	
			else:
				damage = damage_monster(p.dice, equiped.die)
				m.mon_hp -= damage
				if m.is_avile() == False:
					return f"{WHITE}{m.mon_type}{RESET} has {RED}DIED"
				else:
					return f"{WHITE}You {RED}{equiped.att}{RESET} the {WHITE}{m.mon_type}{RESET} with your {equiped.rarity}{equiped.style}{RESET} for {RED}{str(damage)}{RESET}"
		else:
			return f"{WHITE}Your{RESET} attack missed"
	

def damage_monster(dice, die):
	damage = 0
	for x in range(dice):
		damage += random.randint(1, die) + p.check_STR()
	return damage

def attck_player():
	hit = random.randint(1,20)
	if hit == 20:
		hit += m.mon_hit_mod
		if hit >= p.ac:
			damage = damage_player(m.mon_dice, m.mon_die) + damage_player(m.mon_dice, m.mon_die)
			p.hp -= damage
			if p.is_alive() == False:
				return f" and {WHITE}you {RED}DIED"
			else:
				return f" and the {WHITE}{m.mon_type}{RESET} criticaly hit {WHITE}you {RESET}for {YELLOW}{str(damage)} "
		else:
			return f" and the {WHITE}{m.mon_type}{RESET} attack missed"		

	else:
		hit += m.mon_hit_mod
		if hit >= p.ac:
			damage = damage_player(m.mon_dice, m.mon_die)
			p.hp -= damage
			if p.is_alive() == False:
				return f" and {WHITE}you {RED}DIED"
			else:
				return f" and the {WHITE}{m.mon_type}{RESET} hit {WHITE}you{RESET} for {RED}{str(damage)}"
		else:
			return f" and the {WHITE}{m.mon_type}{RESET} attack missed"

def damage_player(dice, die):
	damage = 0 
	for x in range(dice):
		damage += random.randint(1, die) + m.mon_dam_mod
	return damage
############################ GAME START #######################################

p = Player("Izzawa")
m = Monster()
equiped = Weapon()

m.display_monster_stats()
p.display_player_stats(False)
print(f"A lv {RED}{m.mon_lv} {WHITE}{m.mon_type}{RESET} has appered")

while(True):
	
	action = use_action()
	if p.hp <= 0:
		p.print_stats()
		print(f"{RED}-GAME OVER-")
		break
	if action == "R":
		p.print_stats()
		print(f"{RED}-GAME OVER-")
		break
	p.regen_mana()
	if m.is_avile() == False:
		p.exp += m.mon_exp
		if p.exp >= p.exp_2_lv:
			p.add_lv_point()

		w = Weapon()
		if loot() == True:
			equiped = w
		del w

		del m
		m = Monster()
		m.display_monster_stats()
		p.display_player_stats(False)
		print(f"A lv {RED}{m.mon_lv} {WHITE}{m.mon_type}{RESET} has appered")


#############################################################################