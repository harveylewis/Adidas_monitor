# **Requirements:** #
* Python 2.7.12 - https://www.python.org/downloads/
* Modules to install - Requests, Virtualenv (optional but used in instructions)


To install Virtual Environment type (or copy & paste) this code in the terminal: (Only once per install)

```
pip install virtualenv
```


# **Installing:** #
**1)** Download this repo using the green button

**2)** Unzip the download folder to your Home directory

**3)** Rename the folder to 
```
'adidas_monitor'
```
if it isn't already

**4)** Open up a terminal and type

```
   cd adidas_monitor
```

**5)** Create the virtual environment (Only needs to be done once per install):

```
   virtualenv -p python --no-site-packages env
```

**6)** Activate the virtual environment (needs to be done for once for an active session in your terminal):

Mac/Linux:

```
source env/bin/activate
```

Windows:

```
   env\Scripts\activate
```

**7)** Install the requirements (needs to be done once per install):

```
pip install -r requirements.txt
```


That is the installation done. Everytime you close and re-open the terminal to run the monitor you will only need to do step **4** & **6**

# **Configuration:** #
The only file you need to edit is the config.cfg. Right click and open with a text editor.


# **How to run:** #

1) Open new terminal and navigate to adidas_monitor file.


```
cd adidas_monitor
```

2) Activate virtualenv (Copy and paste into terminal)

```
source env/bin/activate
```
Windows:

```
   env\Scripts\activate
```

**3)** After editing 'config.cfg' and saving you can run by typing:

```
python inventory.py
```

