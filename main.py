import os

# Create a folder directory
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)




#VIDEO - Include the folders you would like to have inside the "VIDEO" folder.
video_items = ["00_stock", "01_Movies", "02_YouTube"]

for item in video_items:
    createFolder('./00_VIDEO/' + item)

#IMAGES - Include the folders you would like to have inside the "IMAGE" folder.
image_items = ["00_stock", "01_Google", "02_Misc"]

for item in image_items:
    createFolder('./01_IMAGES/' + item)

#AUDIO - Include the folders you would like to have inside the "AUDIO" folder.
audio_items = ["00_Music", "01_SFX", "02_VO"]

for item in audio_items:
    createFolder('./02_AUDIO/' + item)

#PROGRAM FILES - Include the folders you would like to have inside the "PROGRAM_FILES" folder.
program_items = ["00_Premier", "01_After Effects", "02_Photoshop", "03_Illustrator"]

for item in program_items:
    createFolder('./03_PROGRAM FILES/' + item)

#EXPORTS - Include the folders you would like to have inside the "EXPORTS" folder.
export_items = ["00_FINAL", "01_Updates", "02_Archived"]

for item in export_items:
    createFolder('./04_EXPORTS/' + item)

#MISC - Include the folders you would like to have inside the "MISC" folder.
createFolder('./05_Misc/')

#misc_items = [""]

#for item in misc_items:
    #createFolder('./05_Misc/' + item)

