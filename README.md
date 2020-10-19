# Background-slide-show-python-script




## *Project description :*

  This program is running on background of the system and change the background wallpaper of your  desktop every 2-5 minutes. You can download wallpaper as your preference.

***

## *Tools Used :*

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

## Requirements :

	This program is only for Windows 10 operating system

 - Make sure you have installed Python 3 in your system . You can
   download this from (https://www.python.org/downloads/) and set the System path variable accordingly
   

 - You need a stable internet connection to download images

**

## Setup :

**
"*In this process you need to always connect with internet*"



 **API setup** :
 
 - Go to the link https://unsplash.com/developers
 - Create an developer account 

 - Go to  'Your apps' tab and create a new demo app . Inside your app you will gate the access key of the API . 
 

 

 **How to run the program?**
 

 - First clone the github repo
 - Open **change_wallpaper.py** 
 - go to the line 40:
 
 
 `r=rq.get('https://api.unsplash.com/search/photos?query={}&page={}&per_page=20&orientation=landscape&client_id=KEY'.format("".join(sys.argv[1:]),page_no))`
 
 
 and replace **KEY**(after client_id= ) with your own access key of the **unsplash api** and  save the changes.
 
 - Open command prompt in windows and go to the directory where the repo downloaded
 - Enter the command : `python change_wallpaper.py  search_key` replace the **search_key** as your preference like ( sea,mountain,tree etc.) 

After this the program will start and you can see the  background image changes in every 2-5 minutes.
To stop the process press `ctrl + c` in the command line if it not works kill the process by close the command prompt window.


 
    
**How this program works?** 


Logical approach:

 - step 1 : Search for a image file
 - step 2 : Download image and store it in a directory
 - step 3 : Get the image files from a directory and change the background image

Programming approach: 

 1. Create a directory  for storing image files
 2. Use requests library to send request to the API we created  passing parameters with access key .
 3. Get the request response convert it into JSON format to get the objects
 4. Get the URL of the image ,
 
 Open a  '.jpg' file to write the bytes from the content of image URL.
 
 After write operation close the file. save it in the directory "wallpapers".
 
 5. Store the image paths in a global list .
 6. Now create a separate thread to change the background images.
 
 
In this program two separate thread used for increase the responsiveness  One thread is for download images and another is for change the background . the program uses sleep time of 2 minutes for changing the background wallpaper.

   
                      
