import os

def rename():
	SRC = "./"
	DST = "./"
	# read file in this dir
	for i in range (1,19):
		try:
			file = SRC + `19-i`.zfill(2) + '.jpg'
			newname = DST + `19-i+1`.zfill(2) + '.jpg'
			os.rename(file,newname)
			print (file)
		except IOError as e:
			print e

rename()