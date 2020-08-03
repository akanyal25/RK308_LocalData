from selenium import webdriver  
import time  
import pyautogui
import sys

try:
 fname = sys.argv[1]
except Exception:
    fname=" "
    print("No first name.")

try:
 sname = sys.argv[2]
except Exception:
    sname=" "
    print("No surname name.") 

try:
 Plocation= sys.argv[3]
except Exception:
    Plocation=" "
    print("No location.") 

Pname=fname+" "+sname


pyautogui.FAILSAFE = False

def Automate(name, loc):
    new =2;
    query = name 
    query1 = loc 
    quer=query+" "+query1;
    appended = quer.replace(' ','+');
    url="https://www.google.com/search?tbm=isch&sxsrf=ALeKk00cEaZtWu-EG6Ew0-1EpCxZm6sgTQ%3A1596206679952&source=hp&ei=Vy4kX7-MONHw9QPesIa4Bg&q=";
    url+=appended;
    browser = webdriver.Chrome('chromedriver') 
  
    for i in range(1): 
     matched_elements = browser.get(url);

     time.sleep(3);
     

     pyautogui.moveTo(250, 250);
     for k in range(50):
         pyautogui.scroll(-20);
         time.sleep(.80);
     time.sleep(3);
     browser.close();

     uurl="https://www.facebook.com/";
     browser = webdriver.Chrome('chromedriver') 
  
    for i in range(1): 
         matched_elements = browser.get(uurl);
         
         pyautogui.write('smartindiahackathonlocaldata@gmail.com');
         pyautogui.press('tab');
         pyautogui.write('sih_2020');
         pyautogui.press('tab');
         pyautogui.press('enter');
         pyautogui.click(x=392, y=184);
         time.sleep(10);
         pyautogui.click();
         pyautogui.click(x=70, y=156);
         pyautogui.write(quer);
         pyautogui.press('enter');
         time.sleep(5);
         pyautogui.click(x=480,y=358);
         time.sleep(2);
         pyautogui.click();
         time.sleep(5);
         pyautogui.click(x=259, y=303);
         time.sleep(7);
         for k in range(8):
             pyautogui.scroll(-200);
             time.sleep(3);
         time.sleep(5);
         browser.close();
    """ smartindiahackathonlocaldata@gmail.com sih_2020
    appended = query.replace(' ','%20');
    prl ="https://www.linkedin.com/search/results/all/?keywords=";
    tail="&origin=GLOBAL_SEARCH_HEADER";
    prl+=appended+tail;"""

    uurl="https://www.linkedin.com/home";
    browser = webdriver.Chrome('chromedriver') 
  
    for i in range(1): 
         matched_elements = browser.get(uurl);
         pyautogui.click(x=283, y=475);
         pyautogui.write('smartindiahackathonlocaldata@gmail.com');
         pyautogui.press('tab');
         pyautogui.write('his_2020');
         pyautogui.press('tab');
         pyautogui.press('tab');
         pyautogui.press('tab');
         pyautogui.press('enter');
         time.sleep(5);
         pyautogui.click(x=726, y=619);
         time.sleep(15);
         pyautogui.click(x=431,y=597);
         time.sleep(3);
         pyautogui.click();
         time.sleep(1);    


         pyautogui.click(x=909, y=171)
         pyautogui.click(x=137, y=159);
         pyautogui.write(query);
         time.sleep(6);
         pyautogui.press('enter');
         pyautogui.keyDown('ctrl');
         pyautogui.press('+');
         pyautogui.press('+');
         pyautogui.press('+');
         pyautogui.press('+');
         pyautogui.press('+');
         pyautogui.press('+');
         pyautogui.keyUp('ctrl');
         pyautogui.hscroll(1000);
         pyautogui.scroll(900);
         time.sleep(1);
         for k in range(8):
             pyautogui.scroll(-200);
             time.sleep(3);
         time.sleep(5);
         browser.close();
    uurl="https://www.instagram.com/";
    browser = webdriver.Chrome('chromedriver') 
    for i in range(1):
         matched_elements = browser.get(uurl);
         time.sleep(3);    
         pyautogui.press('tab');
         pyautogui.press('enter');
         pyautogui.write("smartindiahackathonlocaldata@gmail.com");
         pyautogui.press('tab');
         pyautogui.write('sih_2020');
         pyautogui.press('tab');
         pyautogui.press('tab');
         pyautogui.press('enter');
         time.sleep(3);
         pyautogui.press('tab');
         pyautogui.press('tab');
         pyautogui.press('enter');
         
         pyautogui.click(x=652,y=700);
         time.sleep(3);
         pyautogui.click(x=656,y=756);
         time.sleep(4);
         v=0;dl=80;
         for v in range(6):
             pyautogui.click(x=647,y=198);
             pyautogui.write(query);
             time.sleep(1);  
             pyautogui.click(x=543,y=275+dl);
             time.sleep(2);
             for k in range(2):
                 pyautogui.scroll(-200);
                 time.sleep(3);
             time.sleep(1);
             pyautogui.click(x=47,y=99);
             dl+=80;
         browser.close();
    
    appended = query.replace(' ','%20');
    pprl ="https://in.pinterest.com/search/pins/?q=";
    tail="&rs=typed";
    pprl+=appended+tail;
    browser = webdriver.Chrome('chromedriver') 
    for i in range(1): 
         matched_elements = browser.get(pprl);
         pyautogui.moveTo(250, 250);
         for k in range(1):
             pyautogui.scroll(-800);
             time.sleep(3);
    time.sleep(3);
    browser.close();
    

Automate(Pname, Plocation)