# Manifest generator specifically for the IARPA FMoW Dataset
# This works only with the JPG dataset

# Specific Files to target
target_list = ["val/tower/","train/tower/"]
# Only grab msrgb images
validator = "msrgb.jpg"

# Open the manifest file from FMoW
mf_file = open("manifest.json", "r")

o = []

data = mf_file.read()
#print(len(data))

new_list = data[1:-1].split(",")
for item in new_list:
	#print(item)
	f = item.replace("\"", "")
	if (True in (t in f for t in target_list)) and validator in f:
		o.append(f)

mf_file.close()


# Save our manifest here
o_file = open("manifest.files", "w")
for item in o:
	o_file.write(item)