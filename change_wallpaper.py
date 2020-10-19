import os
import time
import ctypes
import requests as rq
import sys
import threading
# import urllib.request as url, urllib.parse, urllib.error

dir="wallpapers"    # directory name where the image file will be downloaded
img_list=[]         # list of all image files path
 
def change_wallpaper():            # This function used for set baground image  
    global img_list   
    i=0
    while(len(img_list)>0):
        
        path=img_list[i]
        img_path=os.getcwd()+"\\"+path     # get the absloute path of the image file
        time.sleep(120)                    # sleep time in sec
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path , 0)     # this line set the baground image 
        print("background image changed ........",img_path)
        i=(i+1)%len(img_list)
        



def run():
    global img_list
    
    if not os.path.exists(dir):              #check for the download drectory,
                                             #if not exist create one
        os.makedirs(dir)

    flag=0 
    for page_no in range(1,100):

                                             # Make request to the api with the access key,
                                             # get responsse json data

        r=rq.get('https://api.unsplash.com/search/photos?query={}&page={}&per_page=20&orientation=landscape&client_id=KEY'.format("".join(sys.argv[1:]),page_no))
        
        data=r.json()                            
        
        for img in data['results']:                          
                                                             
            file_name=str(img['id']) + ".jpg"   # set a name for the image file

            img_url=img['urls']['raw']          # get image url from JSON data 

            ing_data=rq.get(img_url).content    # get the bytes from the image file

            img_loc=dir+ "/"+ file_name         # get image path 
            

            with open(img_loc,'wb+') as f:       # write the bytes on image file
                f.write(ing_data)
                                         
                time.sleep(60)
                img_list.append(img_loc)        # Add path to image list
                f.close()                       # close the image file
                if(flag==0):
                    bacground_t=threading.Thread(target=change_wallpaper)        # initilize to change baground image in a seperate thread
                    bacground_t.start()
                   
                    flag=1
#             print(img_url)
            

if __name__ == "__main__":
    run()
    































