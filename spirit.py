import time
import sys

def approval():
	global user_name
	user_approval = input('Do you wish to continue?(y/n): ')
	if user_approval == 'y':
		user_name = input('Please enter your name: ')
		time.sleep(2)
		chapter_1()
	else:
		print('Did we Bore You!! Goodbye')
		time.sleep(3)
		print('With Love from noob-wale™')
		time.sleep(3)
		sys.exit(4)

def chapter_1():
	print('You wake up in a dark room, lost and confused. You look around and locate the switch. You switch on the light to check out the room')
	time.sleep(3)
	print('Scared and shaking you survey room. In the middle of the room you notice a rugged misplaced floor rag concealing a hole and across the wall there is a small door key.')
	time.sleep(4)
	print('Panicking and pacing up and down trying to figure out how you got here. Last you could remember is walking back home from the store.')
	time.sleep(3)
	chap_2 = input('1. Check out the floor rag. \n2. Take the key and open the door. \n(1/2)')
	if chap_2 == '1':
		chapter_2()
	else:
		chapter_3()

def chapter_2():
	time.sleep(3)
	print('Walking to the center of the room, you notice a camera. Panicking, You shout at the camera.')
	time.sleep(3)
	print(f'{user_name} shouting, get me out here. \nWhat do you want?')
	time.sleep(3)
	print('Unwillingly you open')
	print('STILL WORKING ON CHAPTER!!!')
	time.sleep(3)
	sys.exit(4)
	
def chapter_3():
	time.sleep(3)
	print('CHAPTER COMING SOON')
	time.sleep(3)
	sys.exit(4)
	
def dead():
	print('GAMEOVER')
	time.sleep(3)
	sys.exit(4)

def g_ending():
	print(f'Congratulations {user_name}, you completed the game')
	time.sleep(3)
	gcredits()

def restart_game():
	play_again = input('Do you want to play again? (y/n): ')
	while True:
		if play_again == 'y':
			time.sleep(3)
			chapter_1()
		else:
			time.sleep(3)
			gcredits()

def gcredits():
	print('Written by James Wallace')
	time.sleep(3)
	print('Code by James Wallace')
	time.sleep(3)
	print('Design by James Wallace')
	time.sleep(3)
	print('TimeOutOracle®')
	time.sleep(3)
	print('Special Thanks to: \nMy Parents Mr&Mrs Ndakalu \nMy Brother George \nMy dear Friend Bruce Wayne')
	time.sleep(3)
	print('Thank you for your support and belief through out this project')
	time.sleep(3)
	print('Goodbye!!!!!!')
	time.sleep(4)
	sys.exit(4)

print('Spirit™ 1.0')
time.sleep(2)
print("This game has been rated 13+. Please assume this game MAY contain graphic language, sexually explicit text, violence and/or any other displeasing topic you can or can't think up!")
time.sleep(3)
print("To be certain you don't encounter textual content that may be offensive, you should leave this area and not continue on within this game.")
time.sleep(4)

approval()