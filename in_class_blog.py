from selenium import webdriver
from selenium.webdriver.common.by import By
from ai import checkChatGPT
import os
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.firefox.service import Service as FFService

# Load browser and navigate to url
options = FFOptions()
options.add_argument("-headless")
service = FFService(executable_path="/snap/bin/geckodriver")
browser = webdriver.Firefox(options=options, service=service)

# Initiate the first browser request
url = 'https://hacking4lawyers.com/blog/index.php'
browser.get(url)

# Login to the blog
browser.find_element(By.ID, "username").send_keys(os.environ.get('blog_username'))
browser.find_element(By.ID, "password").send_keys(os.environ.get('blog_password'))
browser.find_element(By.ID, "loginbutton").click()

# Generate blog content
user = "You are a Hawaii based legal tech attorney who is very busy."
blog_prompt = "Write a blog that is relevant to legal technology today and how tech will take over the law."
blog_post = checkChatGPT(user, blog_prompt)
title = checkChatGPT("You are a great title writer", "Give me a title for a blog post that matches this blog.\n" + blog_post)

print(blog_post)
print(title)

# Fill in the blog title and content
browser.find_element(By.ID, "blogtitle").send_keys(title)
browser.find_element(By.ID, "blogpost").send_keys(blog_post)
browser.find_element(By.ID, "submitpostbutton").click()

#End Browser Session
browser.close()
