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

<!-- /TOC -->
# GraphDataCollection missions
1. Collect the knowledge data from STUCCO demo using APIs provided by it.
2. Collect the network security data from several websites using python crawlers.
3. Store data collected in mission 2 in MYSQL database.
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
#### Malwares(Symantec)
Data is stored in json files. Each item has four basic records: title, link, description and pubDate. Other records are collected from web pages their links referring to.
#### Malicious domains
Data is stored in a csv file. Each record has six properties.
#### NVD
Data is stored in xml/json files.
#### CNVD
Data is stored in xml files.
## Mission 3