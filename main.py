'''
	https://coderpad.io/MGMYMWXZ

	Problem defination: 

  This function would traverse dirPath and return a mapping of
  (f -> a list of files that have the exact same content as f)
 
  Examples:
 
  /
  /a.txt
  /b.bin
  /c.jpg
  /dir1/j.whatever
  /dir2/subdir1/q.whatever
  /dir2/subdir1/j.whatever
 
  If a.txt == b.bin (content-wise):
 
  One possible:
 
  a.txt -> [b.bin, c.jpg, /dir2/subdir1/j.whatever]
  dir1/j.whatever -> []
  dir2/subdir1/q.whatever -> []
 
  Another:
 
  b.bin -> [a.txt, c.jpg, /dir2/subdir1/j.whatever]
  dir1/j.whatever -> []
  dir2/subdir1/q.whatever -> []
 
  You're allowed to use:
 
  - listDir(dir: Path): List[Path] // list all files in dir
  - isDir(path: Path): Boolean    // 
  - you can read a file (byte-by-byte or content) // readFile(f)

'''

def list_all_files(path):
	''' returns a list of all files in this dir path'''

	files = []
	for p in path:
		# is a dir
		if(is_dir(p)):
			files = files + list_all_files(p)
		# is a file	
		else:
			files.append(p)	

	return files		


def is_same(file1,file2):
	''' returns a boolean indicating file is same or not. use md5 to compare contents of file '''

	file1_content,file2_content
	with open(file1) as f:
		file1_content = f.read()
	with open(file1) as f:
		file2_content = f.read()

	if file1_content == file2_content:
		return True
	else:
		return False	

def groupFilesByContent(dirPath):
	''' returns a Map<String,List<Path>>. the key is path and the value is a list of files that have the same content as key'''

	grouped_files = {}
	file_list = list_all_files(dirPath)

	# file_list size = 0
	if(file_list.size() == 0):
		return grouped_files

	# file_list size = 1
	if(file_list.size() == 1):
		return grouped_files[file_list[0]] = []

	# file_lise size > 1

	# add first elemnt as key with empty list
	grouped_files[file_list[0]] = []

	# traverse from 1 to n
	for file in file_list[1:]:

		# file matches any of the keys -  append file
		for key in grouped_files.keys():
			if(is_same(file_list[key] , file_list[file] )):

				temp_list = file_list[key]
				temp_list.append( file_list[file] )
				file_list[key] = temp_list

		# file does not matches any key - create a entry in hashmap for it
		file_list[file] = []



def main():
	groupFilesByContent("/Users/kmangtani/")


if __name__ == __main__:
	main()	