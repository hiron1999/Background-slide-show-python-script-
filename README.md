# Background-slide-show-python-script




## *Project description :*

  This program is running on background of the system and change the background wallpaper of your  desktop every 2-5 minutes. You can download wallpaper as your preference.

***

## *Tools Used :**

**
		

 - Visual Studio Code (Editor)
 - Python 3 (programming language)
		*Libraries used :* 
							 os
							 time
							 ctypes
							 requests 
							 sys
							 threading
		
 - API used :  Unsplash API (for download Hd images)

 - Windows 10 (OS)

**

## Requirements :**

	This program is only for Windows 10 operating system

 - Make sure you have installed Python 3 in your system . You can
   download this from (https://www.python.org/downloads/) and set the System path variable accordingly
   

 - you need to download the python 3 libraries . you can install it by using  pip (https://pip.pypa.io/en/stable/installing/) .
After installing pip you can download the libraries using the command : `pip install library_name`

 - You need a stable internet connection to download images

**

## Setup :

**
"*In this process you need to always connect with internet*"

**Install library :**  os , ctypes ,time , threading , sys libraries are normaly come with python package . we need to install requests 
	Open command prompt and run the command : 
	`pip install requests`
	

 **API setup** :
 
 - Go to the link https://unsplash.com/developers
 - Create an developer account 
 - Go to  'Your apps' tab and create a new demo app . Inside your app you will gate the access key of the API . 
 

 

 **How to run the program?**
 

 - First clone the github repo
 - Open **change_wallpaper.py** 
 - go to the line `r=rq.get('https://api.unsplash.com/search/photos?query={}&page={}&per_page=20&orientation=landscape&client_id=KEY'.format("".join(sys.argv[1:]),page_no))`
 and replace **KEY**(after client_id= ) with your own access key of the **unsplash api**  save the changes.
 
 - Open command prompt in windows and go to the directory where the repo downloaded
 - Enter the command : `python change_wallpaper.py  search_key` replace the **search_key** as your preference like ( sea,mountain,tree etc.) 

After this the program will start and you can see the  background image changes in every 2-5 minutes.
To stop the process press `ctrl + c` in the command line if it not works kill the process by close the command prompt window.


 
    

   
                      
