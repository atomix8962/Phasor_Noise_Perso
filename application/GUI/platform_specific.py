import platform
import os
global config_directory
global images_directory
if platform.system() == "Linux":
	global config_directory
	global images_directory
	config_directory = "/etc/phasor-generator"
	images_directory = f"/home/{os.environ['USER']}/phasor-generator"
if platform.system() == "Windows":
	global config_directory
	global images_directory
	config_directory = "C:/Program Files/phasor-generator/config"
	images_directory = f"{os.environ['UserProfile']}/phasor-generator"
