
def get_file_list_in_path(relative_path):
    # listing directories
    listafile = os.listdir(os.getcwd() + "/" + str(relative_path))
    return listafile

def write_text_on_file(file, string_list):
    outputFile = open("./lista.txt","w")
    for file in listafile:
        outputFile.write(file + "\n")
    outputFile.close()

def is_a_mp3_file(file):
	if len(file) <= 1:
		return False
	if (file[-4:].lower() == ".mp3"):
		return True
	else:
		return False

def already_exists(filePath):
	if (os.path.exists(filePath)):
		return True
	else:
		return False

def try_to_create_folder(path):
	try:
		os.mkdir(path)
	except:
		pass
