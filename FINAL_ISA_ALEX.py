#Music program
#_______________________________________________________________________
#*Create a program for writing chord progressions
# Based on the Modes of the Major Scale

# 12 notes
#[A, A#, B, C, C#, D, D#, E, F, F#, G, G#]
#Same notes in flat (EX: A# = Bb)
#[A, Bb, B, C, Db, D, Eb, E, F, Gb, G, Ab]

#**Number Theory representation
#Capital Roman Numerals = Major Chord (maj) (Ex. I IV)
#Lowercase Numerals = Minor (min) (Ex. ii iii vi)
#SPECIAL CASES = V is always dominant (dom)
#vii is  Minor flat 5 (minb5) 

#**Each note of a scale has a respective Chord and Mode for it
#** The Chord order is always:
# Major-Minor-Minor-Major-Dominant-Minor-Minor7Flat5
#  	I 	 ii    iii   IV      V       vi     vii

#Whole Step - 'W' Moves 2 Steps up (EX D - > E| F# -> D#)
#Half Step - One step Up (EX: B -> C| G-> G#)
#**There are no notes inbetween B-C and E-F
#Major Scale always goes W-W-H-W-W-W-H

#EX: C major (C is the Root = R)
#[A, A#, B, C, C#, D, D#, E, F, F#, G, G#]
# 6 (W)  7(H)R (W) 2  (W) 3(H)4 (W) 5      (Notes Loop again)
#C Major = C   D    E    F    G    A     B    C
#		   I   ii  iii   IV   V    vi   vii   R(I)

#12 notes
#[A, A#, B, C, C#, D, D#, E, F, F#, G, G#]

#___________________________________________________________________
#START HERE
#___________________________________________________________________
print("Welcome to the Music Program \n")
print("Use natural or Sharp Notes Ex. A, A# \n")
key = input("please enter the Key you wish to start in. \n")
key = key.upper()
print('the key is ', key)

#____________________________________________________________________________________________
def get_notes_in_scale(key, scale):
  """Find all of the notes within a given scale at key"""

  #define notes in the chromatic scale
  chromatic = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

  #rearrange the chromatic scale in the proper key
  pos = chromatic.index(key)
  chromatic = chromatic[pos:] + chromatic[0:pos]
  
  #reset the position to zero and build the scale using the step mapping
  pos = 0
  notes = [chromatic[pos]]
  for step in scale:
    pos = pos + step
    notes.append(chromatic[pos])

  return notes

  
if (key != None ):
  scale_choice = input("which scale would you like to Use." "\n 1 Major" "\n 2 Minor\n")
	#major or minor scale(
  if scale_choice == '1':
	  major = [2, 2, 1, 2, 2, 2]
	  user_scale = major
	  chords_in_scale =["maj","min","min","maj","dom","min","minb5"]

  elif scale_choice == '2':
			minor = [2, 1, 2, 2, 1, 2]
			user_scale = minor
			chords_in_scale =["min","minb5","maj","min","min","maj","dom"]
  else:
   print("please enter 1 or 2")

user_scale = get_notes_in_scale(key,user_scale)
print("The notes of the Major Scale are: \n", user_scale)

Ichord = user_scale[0] + chords_in_scale[0]
iichord = user_scale[1] + chords_in_scale[1]
iiichord = user_scale[2] + chords_in_scale[2]
IVchord = user_scale[3] + chords_in_scale[3]
Vchord = user_scale[4] + chords_in_scale[4]
vichord = user_scale[5] + chords_in_scale[5]
viichord = user_scale[6] + chords_in_scale[6]

number_chords = Ichord + ' ' + iichord + ' ' + iiichord + ' ' + IVchord + ' ' + Vchord + ' ' + vichord + ' ' + viichord

print("\nThe chords are: \n", number_chords)

chords_choice = input("Do you want to use 7th or 9th chords?\n 7 -7th\n 9 - 9th\n N - for no changes\n")
if (chords_choice != None):
#7th Chords
 if chords_choice == '7':
		Ichord = user_scale[0] + chords_in_scale[0] + '7'
		iichord = user_scale[1] + chords_in_scale[1]  + '7'
		iiichord = user_scale[2] + chords_in_scale[2] + '7'
		IVchord = user_scale[3] + chords_in_scale[3] + '7'
		Vchord = user_scale[4] + chords_in_scale[4] + '7'
		vichord = user_scale[5] + chords_in_scale[5] + '7'
		viichord = user_scale[6] + chords_in_scale[6] + '7'

		#9th Chords
 elif chords_choice == '9':
		Ichord = user_scale[0] + chords_in_scale[0] + '9'
		iichord = user_scale[1] + chords_in_scale[1] + '9'
		iiichord = user_scale[2] + chords_in_scale[2] + '9'
		IVchord = user_scale[3] + chords_in_scale[3] + '9'
		Vchord = user_scale[4] + chords_in_scale[4] + '9'
		vichord = user_scale[5] + chords_in_scale[5] + '9'
		viichord = user_scale[6] + chords_in_scale[6] + '9'
 elif chords_choice == 'N' or 'n':
    pass

#__________________________________________________________________________________
#vii note + 1 = I note 
#major scale loops back

#MENU
#________________________________________________________________________________
if (scale_choice != None):
	menu = ("Chord Progressions, based on modes for the major scale\n"
			"	Mode	  	Chord Progression\n"
			"1)	Ionion	 	I-V-VI-I\n"
			"2)	Dorian		ii-iii-ii-V\n"
			"3)	Phrygian	iii-IV-iii-ii\n"
			"4)	Lydian		IV-V\n"
			"5)	Mixolydian	V-ii-V-IV\n"
			"6)	Aeolian		vi-IV-V\n"
			"7)	Locrian 	ii-vii-I \n"
			"D)  Delete Progressions \n"
			"J)	  Jazzy Options  \n"
			"E)	  Exit to exit at any time\n"
			"P)  	Show Phrase\n")

	menuChoice =input(menu)
menuChoice = menuChoice.upper()

while menuChoice != 'E' or 'e':
		 #I - V - VI - I
	if menuChoice == '1':
		#ask the user which progression of the two 
		Phrase = (Ichord + ' '+ Vchord + ' ' +  vichord + ' ' +  Ichord + '\n')
			#Phrase = Phrase + ' ' + (Ichord + iichord + Vchord)
		print(Phrase)
		pd = open("phrase.txt","a")
		pd.write(Phrase + '\n')
		pd.close()

		#ii - iii - ii - V
	elif menuChoice == '2':
		Phrase = (iichord +' '+  iiichord +' '+  iichord +' '+  Vchord + "\n")
		print(Phrase)
		pd = open("phrase.txt","a")
		pd.write(Phrase + "\n")
		pd.close()

	elif menuChoice == '3': #iii - IV - iii - ii 
		Phrase = (iiichord +' '+ IVchord +' '+ iiichord +' '+ iichord + '\n')
		print('\n', Phrase)
		pd = open("phrase.txt","a")
		pd.write(Phrase + '\n')
		pd.close()

	elif menuChoice == '4': #IV - V
		Phrase = (IVchord +' '+ Vchord + '\n')
		print(Phrase)
		pd = open("phrase.txt","a")
		pd.write(Phrase + '\n')
		pd.close()

	elif menuChoice == '5': #V - ii - V - IV
		Phrase = (Vchord +' '+ iichord +' '+ Vchord +' '+ IVchord + '\n')
		print('\n', Phrase)
		pd = open("phrase.txt","a")
		pd.write(Phrase + '\n')
		pd.close()

	elif menuChoice == '6': #vi - IV - V
		Phrase = (vichord +' '+ IVchord +' '+ Vchord + '\n')
		print(Phrase)
		pd = open("phrase.txt","a")
		pd.write(Phrase + '\n')
		pd.close()

	elif menuChoice == '7': #ii - vii - I 
		Phrase = (iichord +' '+ viichord +' '+ Ichord + "\n")
		print(Phrase)
		pd = open("phrase.txt","a")
		pd.write(Phrase + '\n')
		pd.close()

	elif menuChoice == 'E' or 'e':
		print("\nToo Much Jazz\n")
		exit()

	else: print("please make another choice")
	menuChoice = input(menu)
