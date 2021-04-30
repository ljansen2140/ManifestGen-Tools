# Note: This file is specifically designed to work with the IARPA FMoW dataset.

from PIL import Image
import time

# Target directory to copy data to
directory = "/home/ubuntu/fmow-rgb-dataset/"

# Specific tag for manifest
tag = "multi_set"
# Manifest name
man_name = "manifest.files"


train_loc = "/home/ubuntu/fmow_dataset/"+tag+"/train/"
val_loc = "/home/ubuntu/fmow_dataset/"+tag+"/val/"
man_loc = "/home/ubuntu/fmow_dataset/"+tag+"/"

# Targets for determining training versus validation
target1 = "val/"
target2 = "train/"


mf_file = open(man_name, "r")

o = []

data = mf_file.read()
data = data.split(" ")

train_ims = []
val_ims = []

for im in data:
	if target1 in im:
		val_ims.append(im)
	if target2 in im:
		train_ims.append(im)

train_manifest = []
val_manifest = []


name = 0

#Dimensions to save this file as
dim = (512,512)
for loc in train_ims:
	im = Image.open(directory + loc)
	im = im.resize(dim)
	im.save(train_loc + str(name) + ".jpg")
	train_manifest.append(train_loc + str(name) + ".jpg")
	name += 1
	print("Saved Image '" + loc + "'")
	
name = 0
for loc in val_ims:
	im = Image.open(directory + loc)
	im = im.resize(dim)
	im.save(val_loc + str(name) + ".jpg")
	val_manifest.append(val_loc + str(name) + ".jpg")
	name += 1
	print("Saved Image '" + loc + "'")

# Training Manifest Generated Here
w_train_man = open(man_loc + "train.manifest", "w")
for entry in train_manifest:
	w_train_man.write(entry + " ")
w_train_man.close()
print("Training Manifest Written")

# Validation Manifest Generated Here
w_val_man = open(man_loc + "val.manifest", "w")
for entry in val_manifest:
	w_val_man.write(entry  + " ")
w_val_man.close()
print("Validation Manifest Written")

