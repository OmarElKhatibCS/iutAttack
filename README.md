# iutAttack

## What is this Tool ?
this is a tool that exploit IUT university Students System , that work on blocking Users Accounts.

## follow Instructions :

* First you should had an Linux System to run this Code.
* you need python 2.7 to run this script , generally every Linux System had pre-installed python .
* install selenium package for python which can done with :
```
pip install selenium
```
* then you need to install chrome driver you can download it from [ChromeWebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* you need to unzip file downloaded , you need an unzip tool , simply you can download it , open your terminal then type
### Debian or Ubuntu
```
sudo apt-get install unzip
```
### Archlinux 
```
sudo pacman -S unzip
```
* after successfully install it , you need to type into your terminal to navigate to download folder in my case is Downloads and unzip it then give permission to excutable file , which can Done with
```
cd Downloads
unzip chromedriver_linux64.zip
chmod a+x chromedriver
mv chromedriver /usr/local/bin
```
* and the same we need to install PhantomJs which can downloaded from [PhantomJS](http://phantomjs.org/download.html) , after downloading it open terminal then
```
cd Downloads
chmod a+x phantomjs
mv phantomjs /usr/local/bin
```
* now we end all steps and the script is ready to Run , you can Run it using python2 the code using
```
python IUTattack.py	
```
### this Script is just For Education Purpose , I Am Not Responsible For Your Evil Mind , if you use script in closing accounts the police can know your location , so be careful.
