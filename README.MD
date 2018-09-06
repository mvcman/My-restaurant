# Making a restaurant app:

>A simple web server file here we can edit ,delete,create our restaurnats name... Build a web service in python that uses your database to implement CRUD operation by n using python framework.

# How to run this code:
>1. Install the VM and Vagrant: This project uses a virtual machine (VM) to run a SQL database server.

>2. If you don't already have virtual box on your machine, you can download it here: https://www.virtualbox.org/wiki/DownloadOldBuilds51 or for ubuntu type this command: sudo apt-get install virtual box

>3. Download and install Vagrant (if you do not already have it installed). This is the software that configures the VM and allows the host (your machine) to talk to the VM: -->https://www.vagrantup.com/ or for ubuntu type this commnad: sudo apt-get install vagrant ->you should be able to run $ vagrant --version after installation to see the version that was installed.

>4. Download and unzip this file:https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.
Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

>5. cd into this(FSND_Virtual_Machine) directory

>6. cd into the vagrant/ subdirectory

>7. Bring the VM up with the command vagrant up

>8. Log into the VM with vagrant ssh


# Download and run the file:

> 1. Clone this repository to your local drive: https://github.com/mvcman/My-restaurant

>2. Copy the file into the FSND_Virtual_Machine/vagrant directory.

>3. Open a terminal window from the FSND_Virtual_Machine/vagrant directory, or simply open a terminal window and cd into that directory.

>4. Run vagrant ssh at the prompt to log in to the VM. $ vagrant ssh

>5. cd into the vagrant subdirectory vagrant@vagrant:~$ cd /vagrant

>6. Run the database.py program vagrant@vagrant:/vagrant$ python database.py

>7. Run the create_menu.py program to add the menu in database file vagrant@vagrant:/vagrant$ python create_menu.py

>8. Run the my-restaurant.py program vagrant@vagrant:/vagrant$ python my-restaurant.py

>9. Folder template contanins editmenu.html, deletemenu.html, menu.html, addmenu.html files this folder in same directory as hello.py file.

>10. Folder static contains style.css file this folder also in same directory where hello.py file present.

>11. Run the hello.py program to add the menu in database file vagrant@vagrant:/vagrant$ python hello.py

>12. Open the browser and run the 'localhost:8080/hello' as per given in the file

>13. The program's output will be displayed in browser.
