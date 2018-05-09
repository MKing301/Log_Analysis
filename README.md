# News Database Report Generator

This _**news_database_report.py**_ program generates a report using SQL queries to analyze information from an existing database of a newspaper site to answer the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

# Resources

**IMPORTANT**
The instruction material under the following listed sections ONLY are from the Udacity NanoDegree Program: [Intro to Programming](https://www.udacity.com/course/intro-to-programming-nanodegree--nd000) to meet the installation requirements for the specific Log Analysis project:

* Installing a Linux VM with Vagrant
* Installing VirtualBox
* Installing Vagrant
* Download the Data

# Installation

To run this project, you will need to download the news site's data and load it into a PostgreSQL database of your own. Your database server will be running in a Linux virtual machine.

## Installing a Linux VM with Vagrant

We have put together a Linux virtual machine (VM) configuration that already contains the PostgreSQL database software. To run it, you will need to install three things on your computer (if you don't already have them):

* The **VirtualBox** VM environment
* The **Vagrant** configuration program

## Installing VirtualBox

VirtualBox is the program that runs your Linux virtual machine. [Install_it_from_this_site](https://www.virtualbox.org/wiki/Downloads). Install the _platform package_ for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

## Installing Vagrant

Vagrant is the program that will download a Linux operating system and run it inside the virtual machine. [Install_it_from_this_site](https://www.vagrantup.com/downloads.html).
Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

## Bringing up the database server

Vagrant takes a configuration file called `Vagrantfile` that tells it how to start your Linux VM. [Download_the_Vagrantfile_here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f73b_vagrantfile/vagrantfile). Put this file into a new directory (folder) on your computer. Using your terminal, change directory (with the cd command) to that directory, then run vagrant up. You should see something like the following:

```
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Checking if box 'bento/ubuntu-16.04-i386' is up to date...
==> default: Clearing any previously set forwarded ports...
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 8000 (guest) => 8000 (host) (adapter 1)
    default: 8080 (guest) => 8080 (host) (adapter 1)
    default: 5000 (guest) => 5000 (host) (adapter 1)
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Connection reset. Retrying...
    default: Warning: Connection aborted. Retrying...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default:
    default: Guest Additions Version: 5.1.21
    default: VirtualBox Version: 5.2
==> default: Mounting shared folders...
    default: /vagrant => C:/Users/--your computer name--/Downloads/fsnd-virtual-machine/FSND-Virtual-Machine/vagrant
==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
==> default: flag to force provisioning. Provisioners marked to run always will still run.

```


 
[Successful_vagrant_up_results:_"Done_)installing_PostgreSQL_database!"](https://classroom.udacity.com/nanodegrees/nd000/parts/b910112d-b5c0-4bfe-adca-6425b137ed12/modules/a3a0987f-fc76-4d14-a759-b2652d06ab2b/lessons/0aa64f0e-30be-455e-a30d-4cae963f75ea/concepts/eaf58af6-a1fa-43a0-b4de-311e04689748)

Now you have a PostgreSQL server running in a Linux virtual machine. This setup is independent of any other database or web services you might have running on your computer, for instance for other projects you might work on. The VM is linked to the directory where you ran `vagrant up`.

To log into the VM, use a terminal in that same directory and run `vagrant ssh` or `winpty vagrant ssh`(Git Bash on Windows). You'll then see something like this:

```
Welcome to Ubuntu 16.04.4 LTS (GNU/Linux 4.4.0-75-generic i686)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

0 packages can be updated.
0 updates are security updates.


The shared directory is located at /vagrant
To access your shared files: cd /vagrant
Last login: Thu Mar 15 22:19:07 2018 from 10.0.2.2
vagrant@vagrant:~$

```

[A_shell_prompt_on_the_Vagrant-managed_Linux-VM.](https://classroom.udacity.com/nanodegrees/nd000/parts/b910112d-b5c0-4bfe-adca-6425b137ed12/modules/a3a0987f-fc76-4d14-a759-b2652d06ab2b/lessons/0aa64f0e-30be-455e-a30d-4cae963f75ea/concepts/eaf58af6-a1fa-43a0-b4de-311e046897480)

In this shell, if you `cd /vagrant` and run ls there, you will see the `Vagrantfile` you downloaded ... and any other files you put into that directory from your computer. 


## Download the Data
Next, [download_the-data_here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called `newsdata.sql`. Put this file into the vagrant directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the `psql` command in this lesson: ([FSND_version](https://classroom.udacity.com/nanodegrees/nd000/parts/b910112d-b5c0-4bfe-adca-6425b137ed12/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/96869cfc-c67e-4a6c-9df2-9f93267b7be5/concepts/0b4079f5-6e64-4dd8-aee9-5c3a0db39840)) ([IPND_version](https://classroom.udacity.com/nanodegrees/nd000/parts/75cc998e-2ab7-4dcb-9ee7-a562efcf8c89/modules/a3a0987f-fc76-4d14-a759-b2652d06ab2b/lessons/477edebf-b8f6-4eab-88bb-0456c9084bc5/concepts/0b4079f5-6e64-4dd8-aee9-5c3a0db39840))
To load the data, cd into the vagrant directory and use the command `psql -d news -f newsdata.sql`.
Here's what this command does:

* `psql` — the PostgreSQL command line program
* `-d` news — connect to the database named news which has been set up for you
* `-f newsdata.sql` — run the SQL statements in the file `newsdata.sql`

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data. 


# Explore the data

Once you have the data loaded into your database, connect to your database using `psql -d news` and explore the tables using the `\dt` and `\d table` commands:

```
vagrant@vagrant:/vagrant$ psql news
psql (9.5.12)
Type "help" for help.

news=> \dt
```

 | Schema |   Name   | Type  |  Owner|
 |-------|----------|-------|--------|
 | public | articles | table | vagrant |
 | public | authors  | table | vagrant |
 | public | log      | table | vagrant |


You will need to create the 2 views for this project using the following queries:

```
create view total_request_count as
select cast(time as date) as totalcountdate, count(id) as totalrequestcount
from log
group by cast(time as date)
order by cast(time as date);
```

```
create view total_error_count as
select cast(time as date) as ErrorDate, count(id) as ErrorCount
from log
where status != '200 OK' and (status like '4%' OR status like '5%')
group by cast(time as date)
order by cast(time as date);
```

Once you have executed the above queries you can use the `\dv` command to verify the views:

```
news=> \dv
```

 | Schema |        Name         | Type |  Owner |
 |--------|---------------------|------|-------|
 | public | total_error_count   | view | vagrant |
 | public | total_request_count | view | vagrant |


# Run the program

Requirements
* You have Python 2.7 installed on your computer
* You successfully installed Vagrant
* You successfully installed VirtualBox
* Downloaded and loaded the data into the vagrant directory

1. Create a directory called `report` in your vagrant directory
2. You will need to download the program `news_database_report.py` to your `/vagrant/report` directory.
3. Access the `/vagrant/report` directory using the command line
4. At `report $` prompt type `vagrant up`
5. Next type `python vagrant ssh` OR `winpty vagrant ssh` (if using Git Bash on Windows)
6. At `vagrant@vagrant:~$ prompt` type `cd /vagrant`
7. At `vagrant@vagrant:/vagrant$` prompt type `cd report`
8. At `vagrant@vagrant:/vagrant/report$` prompt type `python news_database_report.py`
9. Press the `ENTER` key to run the program
