import os

def rename():
	SRC = "./"
	DST = "./"
	ceiling = 20
	# read file in this dir
	for i in range (2,ceiling):
		try:
			file = SRC + `ceiling-i`.zfill(2) + '.jpg'
			newname = DST + `ceiling-i+1`.zfill(2) + '.jpg'
			os.rename(file,newname)
			print (file)
		except IOError as e:
			print e

rename()