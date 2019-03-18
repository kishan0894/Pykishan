# Local setup

**To setup HUB**
Make a directory with `mkdir ~/selenium`

`cd ~/selenium`

`wget http://goo.gl/rQhaxb`
`mv selenium-server-standalone-2.49.1.jar ~/selenium/`


**Download dependencies**

`Download and install selenium WebDriver bindings for Python`

`Wget https://pypi.python.org/packages/source/s/selenium/selenium-2.49.2.tar.gz#md5=17cfe7c6adb2cad1f64a61cf753f0738`

`tar -zxvf selenium-2.49.2.tar.gz`

`cd selenium-2.49.2`

`python2.7 setup.py install --user`
	
**Dependencies**

`sudo apt-get install software-properties-common`

`sudo apt-get install oracle-java8-installer`
	
**Initiate the HUB**

 `java -jar selenium-server-standalone-3.10.0.jar -role hub`

	Now we have to configure our Node to the hub. 
		
Here is an example of node configuration for Chrome and Firefox nodes.

Firefox - [link](https://github.com/kishan0894/Pykishan/blob/master/selenium/configuration_firefox.json)

Chrome- [link](https://github.com/kishan0894/Pykishan/blob/master/selenium/configuration_chrome.json)
	
 The step which connects node and hub to communicate after the hub is initialized -

  `java -jar selenium-server-standalone-3.10.0.jar -role node --configuration_firefox.json/ --configuration_chrome.json`

**Create your Test case file. **
[link](https://github.com/kishan0894/Pykishan/blob/master/Automation_Script_selenium)


Executing the Automation_script_selenium.py will redirect request to node which is on hub. 

    



# Docker setup
**Install Docker**
`Sudo apt-get install docker.io`


**Find appropriate docker image for HUB and grids**


Image | Command
------------ | -------------
Selenium Hub | Docker pull selenium/hub
Selenium firefox node | docker pull selenium/node-firefox
Selenium chrome node | docker pull selenium/node-chrome
Selenium firefox debug | docker pull selenium/node-firefox-debug
Selenium chrome debug | docker pull selenium/node-chrome-debug

Command to run hub image 
`docker run -d -p 8080:4444 --name selenium-hub selenium/hub`

Command to run firefox image as node
`docker run -d -P --link selenium-hub:hub selenium/selenium/node-firefox`

Command to run chrome image as node
`docker run -d -P --link selenium-hub:hub selenium/selenium/node-chrome`


`Mention port id in executable_command in Automation_script_selenium`

`You have Environment Ready`
