# Linked_in_automation_beta
# using selenium for automating the jobs and creating a selenium bot . 

![binh](https://www.kinesisinc.com/wp-content/uploads/2020/04/linkedin-101-hero@2x-901x475.png)

## what is Linkedin?
LinkedIn is a popular social network with a specific purpose. While other social networks like Facebook and Twitter focus more on your personal life, LinkedIn is all about professional networking—that is, building a group of contacts to help advance your career.
More and more businesses use LinkedIn to screen and recruit potential employees. This is why creating a LinkedIn account can make a difference when searching for your next job. Once you've signed up, you can add information to your profile page, which is a brief summary of your skills and employment history that effectively serves as an online resume. 
LinkedIn has a powerful job search tool that can find openings around the world. You can then filter these results by company, experience level, and more. Some openings also have an Easy Apply option, which allows you to apply to a job with only a few clicks by submitting the information in your LinkedIn profile.

## what is a bot ?
A bot is a software application that is programmed to do certain tasks. Bots are automated, which means they run according to their instructions without a human user needing to manually start them up every time. Bots often imitate or replace a human user's behavior. Typically they do repetitive tasks, and they can do them much faster than human users could.

Bots usually operate over a network; more than half of Internet traffic is bots scanning content, interacting with webpages, chatting with users, or looking for attack targets. Some bots are useful, such as search engine bots that index content for search or customer service bots that help users. Other bots are "bad" and are programmed to break into user accounts, scan the web for contact information for sending spam, or perform other malicious activities. If it's connected to the Internet, a bot will have an associated IP address.

Bots can be:

- Chatbots: Bots that simulate human conversation by responding to certain phrases with programmed responses,
- Web crawlers (Googlebots): Bots that scan content on webpages all over the Internet,
- Social bots: Bots that operate on social media platforms,
- Malicious bots: Bots that scrape content, spread spam content, or carry out credential stuffing attacks 

### name of our bot, *Natasha Sharma* https://www.linkedin.com/in/natasha-sharma-8339b4220/

## what is selenium ?
![sel](https://www.edureka.co/blog/wp-content/uploads/2017/06/selenium.png)

Selenium refers to a suite of tools that are widely used in the testing community when it comes to cross-browser testing. Selenium cannot automate desktop applications; it can only be used in browsers. It is considered to be one of the most preferred tool suites for automation testing of web applications as it provides support for popular web browsers which makes it very powerful.

It supports a number of browsers (Google Chrome 12+, Internet Explorer 7,8,9,10, Safari 5.1+, Opera 11.5, Firefox 3+) and operating systems (Windows, Mac, Linux/Unix).

Selenium also provides compatibility with different programming languages – C#, Java, JavaScript, Ruby, Python, PHP. Testers can choose which language to design test cases in, thus making Selenium highly favorable for its flexibility.

## what is beautiful soup ? 
Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.


# project overview
*The project is primarily build with one thing in mind which is to automate the job application and resume submission to different recruiters wihout even touching the keyboard , this will save a ton of time when an applicant is applying for a job. 
The project also gives the brief Idea of how powerful the mixture of selenium and beautiful soup is . You can use this project at the moment and use the power of automation to apply for 1000 job openings in a few seconds ! , just mention the category that you want the jobs in,
this project is programmed in such a way that it can anytime adjust dynamically to user requirements. Just turn on your notifications and let the incoming recruiter messsages flood your linked in account!!*

before moving forward , it is crucial to know the data-mining and data-scraping ethics , you can read it with the links below -
- https://www.promptcloud.com/blog/is-data-scraping-ethical/#:~:text=Data%20scraping%20is%20ethical%20as,legal%20aspects%20of%20data%20scraping.
- https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01
- https://monashdatafluency.github.io/python-web-scraping/section-5-legal-and-ethical-considerations/
- https://aisel.aisnet.org/cais/vol47/iss1/22/

# files to refer 
 ```main.py```

# important  imports
```
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException    #common exceptions
from selenium.common.exceptions import ElementNotInteractableException   #for not interactable objects

```

# code-flow 
below is the main.py 
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException    #common exceptions
from selenium.common.exceptions import ElementNotInteractableException   #for not interactable objects


webdriver_path="D:\chrome driver\chromedriver_win32\chromedriver.exe"     #common path element

driver=webdriver.Chrome(executable_path=webdriver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2813582804&geoId=92000000&keywords=marketing%20intern&location=Worldwide")

sign_in=driver.find_element(by=By.XPATH,value='/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()
id=driver.find_element(by=By.ID,value='username')
password=driver.find_element(by=By.ID,value='password')
id.send_keys('youremail)      #please enter your own email here
# id.send_keys(Keys.ENTER)    
password.send_keys("yourpassword") #please enter your own password here
down_sign_in=driver.find_element(by=By.XPATH,value='/html/body/div/main/div[2]/div[1]/form/div[3]/button')
down_sign_in.click()
# down_sign_in=driver.find_elements(by=By.CSS_SELECTOR,value='.ember-view a')
# down_sign_in=driver.find_element(by=By.ID,value='ember246')
time.sleep(3)

all_listings = driver.find_elements(by=By.CSS_SELECTOR,value=".job-card-container--clickable")

for i in all_listings:
    i.click()              #listing of the jobs
    time.sleep(2)

    try:    #trying the following code for each iteration

        apply_button=driver.find_element(by=By.CSS_SELECTOR,value='.jobs-s-apply button')
        apply_button.click()
        #Now we have to fill the phone number
        phone = driver.find_element(by=By.CLASS_NAME,value="fb-single-line-text__input")
        phone.send_keys('34434343')
        time.sleep(4)      #sleeping for 4 seconds  

        submit_button=driver.find_element(by=By.CSS_SELECTOR,value='footer button')
        time.sleep(2)
        if submit_button.get_attribute('data-control-name')=='continue_unify':
            cross_button=driver.find_element(by=By.CLASS_NAME,value='artdeco-modal__dismiss')
            cross_button.click()
            time.sleep(2)
            discard_button=driver.find_element(by=By.CSS_SELECTOR,value='.artdeco-modal__actionbar .artdeco-button--primary')
            discard_button.click()
            print('complex application skipped')
            continue

        else:
            submit_button.click()
            continue

    except NoSuchElementException:
        print('the exceptions are handled dont worry ')

    except ElementNotInteractableException:
        continue
        
```
if we look carefully at the starting of the code we see that there are methods such as ```find_element(by=By.XPATH```,```find_elements(by=By.CSS_SELECTOR```,```find_element(by=By.CLASS_NAME``` etc.
these all are the elements selector in the selenium . The element selector select the position and the displacement of the inforamtion that we need on a particular HTML page . 

Selenium offers an array of selectors -

- find_element_by_id
- find_element_by_name
- find_element_by_xpath
- find_element_by_link_text
- find_element_by_partial_link_text
- find_element_by_tag_name
- find_element_by_class_name
- find_element_by_css_selector

 we have used the command find_element(by=By.XPATH) again here to find the screen toggles . We have written send_keys() in the place of login Id and password , the send keys inputs the value that the programmer has given at the time of building the program . Sendkeys can use Float,List and even dictionary type characters.
 
        sign_in=driver.find_element(by=By.XPATH,value='/html/body/div[1]/header/nav/div/a[2]')
        sign_in.click()
        id=driver.find_element(by=By.ID,value='username')
        password=driver.find_element(by=By.ID,value='password')
        id.send_keys('youremail)      #please enter your own email here
        # id.send_keys(Keys.ENTER)    
        password.send_keys("yourpassword") #please enter your own password here
        down_sign_in=driver.find_element(by=By.XPATH,value='/html/body/div/main/div[2]/div[1]/form/div[3]/button')
        down_sign_in.click()
        # down_sign_in=driver.find_elements(by=By.CSS_SELECTOR,value='.ember-view a')
        # down_sign_in=driver.find_element(by=By.ID,value='ember246')
        time.sleep(3)
 from the 1st line of the above code block to the last line the operation that we are seeing here is the login in the linkedin page by carefully selecting the selectors . The selectors at the last two lines consist of selecting the card stack where all th jobs are posted .
 thus in return we get a  list of the whole card for the jobs in the particular area we want to . 
 
 the list easily generates upto 200 jobs and thus we can make a loop to select the jobs and fill up the form as per the requirements . 
 
for the next step we use the following code snippet 

            for i in all_listings:
                i.click()              #listing of the jobs
                time.sleep(2)

                try:    #trying the following code for each iteration

                    apply_button=driver.find_element(by=By.CSS_SELECTOR,value='.jobs-s-apply button')
                    apply_button.click()
                    #Now we have to fill the phone number
                    phone = driver.find_element(by=By.CLASS_NAME,value="fb-single-line-text__input")
                    phone.send_keys('34434343')
                    time.sleep(4)      #sleeping for 4 seconds  

                    submit_button=driver.find_element(by=By.CSS_SELECTOR,value='footer button')
                    time.sleep(2)
                    if submit_button.get_attribute('data-control-name')=='continue_unify':
                        cross_button=driver.find_element(by=By.CLASS_NAME,value='artdeco-modal__dismiss')
                        cross_button.click()
                        time.sleep(2)
                        discard_button=driver.find_element(by=By.CSS_SELECTOR,value='.artdeco-modal__actionbar .artdeco-button--primary')
                        discard_button.click()
                        print('complex application skipped')
                        continue

                    else:
                        submit_button.click()
                        continue

                except NoSuchElementException:
                    print('the exceptions are handled dont worry ')

                except ElementNotInteractableException:
                    continue
the primaray focus of the second block is to iterate over the list from the first block and make targets using specific functions as discussed before . A careful observation of the code will let you know that we have used 
```try``` and ```except``` to catch the exception to avoid the failure of the program . The two such exceptions are -
- ```NoSuchElementException:```
- ``` ElementNotInteractableException:```

The program throughout the iteration may experience some forms which are unpredictible to fill and it doesnt follow the algorithm that we have constructed .For example suppose we have a form that requires an additional step
for verification or some other process , the selenium webdriver will then result is giving or raising an exception  , this exception is handled by ``` ElementNotInteractableException:```

- ```NoSuchElementException:```will handle if there is no element found. 

once the form are filled and we have created a bot(natasha sharma ).Its time to run our program .

we have well responded to some of the recruiters that the applicant is a bot.

<a href="https://ibb.co/TgryrxN"><img src="https://i.ibb.co/yQV2Vcx/Screenshot-28.png" alt="Screenshot-28" border="0"></a>

one more 

<a href="https://ibb.co/k48DvvQ"><img src="https://i.ibb.co/sKw1zzy/Screenshot-29.png" alt="Screenshot-29" border="0"></a>






