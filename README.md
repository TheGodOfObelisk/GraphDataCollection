<!-- TOC -->

- [GraphDataCollection missions](#graphdatacollection-missions)
    - [Mission 1](#mission-1)
        - [Collect by type](#collect-by-type)
        - [Data format](#data-format)
    - [Mission 2](#mission-2)
        - [Url lists](#url-lists)
        - [Data format](#data-format-1)
            - [Malwares(Symantec)](#malwaressymantec)
            - [Malicious domains](#malicious-domains)
            - [NVD](#nvd)
            - [CNVD](#cnvd)
    - [Mission 3](#mission-3)
    - [Mission 4](#mission-4)

<!-- /TOC -->
# GraphDataCollection missions
1. Collect the knowledge data from STUCCO demo using APIs provided by it.
2. Collect the network security data from several websites using python crawlers.
3. Store data collected in mission 2 in MYSQL database.
4. Relation analysis.
## Mission 1
### Collect by type
Types available are listed below.  
    Account: An account on some specific system(s), either belonging to some specific user or a system account. All software runs as some account. All accounts are associated with a user or users (such as system accounts.)  
    Host: Any entity on the network, including PCs, routers, switches, virtual machines, etc.  
    Software: Any software components on a system, including OSes, applications, services, and libraries.  
    Vulnerability: A flaw in some software, that can cause improper, unintended operation, and can potentially be exploited as part of an attack.  
    Malware: Any malicious software. This can refer to either a stored binary or a running instance. Malware can contain code to launch an exploit. Malware can itself be an asset that an attacker uses in future attacks (eg. a backdoor left on a compromised system.) or can automatically launch additional attacks on behalf of the original attacker. Malware can be hosted by or communicate with servers controlled by the attacker. Malware can contain code to load other malware. Malware can reuse components from other malware samples.  
    IP: A specific IP address.  
    DNS Name: A DNS name (and possibly associated info - registration info, etc.).  
    Port: A specific network port.  
    Address: Any address (IP:Port), either inside or outside of the network.  
    Flow: A flow of traffic between two addresses.  
    Address Range: A range of IP addresses.  
### Data format
Store data in json-schema. 
## Mission 2
### Url lists
Malwares:  
https://www.symantec.com/security-center/a-z/A  
Malicious domains:  
http://www.malwaredomainlist.com/mdl2.php?search=&colsearch=All&quantity=All  
NVD:  
https://nvd.nist.gov/vuln/data-feeds  
CNVD:  
http://www.cnvd.org.cn/shareData/list  
### Data format
It is not recommended that we use GitHub to store backups and database dumps.
#### Malwares(Symantec)
Data is stored in json files. Each item has four basic records: title, link, description and pubDate. Other records are collected from web pages their links referring to.
#### Malicious domains
Data is stored in a csv file. Each record has six properties.
#### NVD
Data is stored in xml/json files. Because these files exceed GitHub's file size limit of 100.00 MB, they are not uploaded.
#### CNVD
Data is stored in xml files.
## Mission 3
Use the file named "symantec_insert.py" to store data from symantec. The table structure is shown in "symantec.sql" file.  
malware_init.py: store data into table Malware from symantec.  
malware_os.py: analyze data in symantec and extract os information from it, update Edges and vertex tables. It refers to the relation of "malware affects os".  
malware_cve.py: If refers to the relation of "malware exploits vulnerability". Vulneraility is indicated by CVE.
## Mission 4
Initialize vulnerability table. Ensure that data is available to "malware_cve.py".  
There are 3 steps to initialize vulnerability table. We divide vulnerabilities into 3 types. Type 1 indicates that NVD only and type 3 indicates CNVD only. Type 2 indicates that this entry is the output by combining NVD and CNVD entries. Type 2 records may have more than one CNVD id in its "cnvdId" column.  
The "vulnerability_init.py" file is used to complete step 1. The "vulnerability_fusion.py" file is used to complete step 2. The "vulnerability_remain.py" file is used to complete step 3.  