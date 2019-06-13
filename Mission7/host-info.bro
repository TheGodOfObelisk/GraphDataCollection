## It aims at getting hosts'
## USERNAME,    0      pay attention to NTLM PLZ
## HOSTNAME,      1
## MAC ADDRESS,  1
## OPERATING SYSTEM,     1
## IP ADDRESS    1

## New elements 2019.1.9

## How to sort ips?
## Type          (indicates devicetype, etc desktop, laptop, tablet)
## Applications  (Why do we need it? Should we guess during which period such applications are running?)
## Protocols     (so many protocols, how to handle them? It exists between two hosts.)

## New considerations  2019.1.10

## Maintain the information of hosts all the time and output it to log file every n seconds
## The value of n has not been determined.

module HOST_INFO;

export{
	# Create an ID for our new stream. By convention, this is
	# called "HOST_INFO_LOG".
	redef enum Log::ID += { HOST_INFO_LOG };

    # unfortunately, its json format is incorrect
    # redef LogAscii::use_json = T;
	# Define the record type that will contain the data to log.
    type host_info: record{
        ts: time    &log;
        ip: addr      &log;
        username: string    &default="" &log;
        hostname: string    &default="" &log;
        mac: string     &default="" &log;
        os: string      &default="" &log;
        description: string     &default="" &log;
    };
}

## Use it to store host-info
global hostlist: vector of host_info = {};

event OS_version_found(c: connection, host: addr, OS: OS_version){
    # print "an operating system has been fingerprinted";
    # print fmt("the host running this OS is %s", host);
    # print OS;
    if(OS$genre != "UNKNOWN"){
        local os_detail = fmt("%s %s", OS$genre, OS$detail);
        local rec: HOST_INFO::host_info = [$ts = network_time(), $ip = host, $os = os_detail, $description = "OS_version_found"];
        Log::write(HOST_INFO::HOST_INFO_LOG, rec);
    }
    # e.g [genre=UNKNOWN, detail=, dist=36, match_type=direct_inference]
    # How to utilize this message?
}

# There is no point in removing dulipcated messages for a specific ip. 
# Becuase ip addresses should not be the unique identification of a specific host.
# We should identity a specific host by ip and mac pairs which have the lastest network time.
event arp_reply(mac_src: string, mac_dst: string, SPA: addr, SHA: string, TPA: addr, THA: string){
    # print "arp reply";
    # print fmt("source mac: %s, destination mac: %s, SPA: %s, SHA: %s, TPA: %s, THA: %s", mac_src, mac_dst, SPA, SHA, TPA, THA);
    # record ip and its mac address
    # we don't these form of mac addresses:
    # 00:00:00:00:00:00 and ff:ff:ff:ff:ff:ff
    if(SHA != "ff:ff:ff:ff:ff:ff" && SHA != "00:00:00:00:00:00" && SPA != 0.0.0.0){
        local rec1: HOST_INFO::host_info = [$ts = network_time(), $ip = SPA, $mac = SHA, $description = "arp_reply" ];
        Log::write(HOST_INFO::HOST_INFO_LOG, rec1);
    }
    if(THA != "ff:ff:ff:ff:ff:ff" && THA != "00:00:00:00:00:00" && TPA != 0.0.0.0){
        local rec2: HOST_INFO::host_info = [$ts = network_time(), $ip = TPA, $mac = THA, $description = "arp_reply" ];
        Log::write(HOST_INFO::HOST_INFO_LOG, rec2);
    }
}

event arp_request(mac_src: string, mac_dst: string, SPA: addr, SHA: string, TPA: addr, THA: string){
    # print "arp request";
    # print fmt("source mac: %s, destination mac: %s, SPA: %s, SHA: %s, TPA: %s, THA: %s", mac_src, mac_dst, SPA, SHA, TPA, THA);
    if(SHA != "ff:ff:ff:ff:ff:ff" && SHA != "00:00:00:00:00:00" && SPA != 0.0.0.0){
        local rec1: HOST_INFO::host_info = [$ts = network_time(), $ip = SPA, $mac = SHA, $description = "arp_request" ];
        Log::write(HOST_INFO::HOST_INFO_LOG, rec1);
    }
    if(THA != "ff:ff:ff:ff:ff:ff" && THA != "00:00:00:00:00:00" && TPA != 0.0.0.0){
        local rec2: HOST_INFO::host_info = [$ts = network_time(), $ip = TPA, $mac = THA, $description = "arp_request" ];
        Log::write(HOST_INFO::HOST_INFO_LOG, rec2);
    }
}

event bad_arp(SPA: addr, SHA: string, TPA: addr, THA: string, explanation: string){
    print fmt("this arp packet is bad because: %s", explanation);
}

event dhcp_message(c: connection, is_orig: bool, msg: DHCP::Msg, options: DHCP::Options){
    # print "A dhcp message is coming!";
    # print msg;
    # print options;
    if(options ?$ host_name && options ?$ addr_request && options ?$ client_id){ # It occurred once: missing client_id, check it in advance
        print "haha";
        # print options;
        local rec1: HOST_INFO::host_info = [$ts = network_time(), $ip = options$addr_request, $mac = options$client_id$hwaddr, $hostname = options$host_name, $description = "dhcp_message1" ];
        Log::write(HOST_INFO::HOST_INFO_LOG, rec1);
    } else{
        if(msg$yiaddr != 0.0.0.0){
            local rec2: HOST_INFO::host_info = [$ts = network_time(), $ip = msg$yiaddr, $mac = msg$chaddr, $description = "dhcp_message2" ];
            Log::write(HOST_INFO::HOST_INFO_LOG, rec2);
        }
    }
}

function check_ssh_hostname(id: conn_id, uid: string, host: addr){
    when(local hostname = lookup_addr(host)){
        local rec: HOST_INFO::host_info = [$ts = network_time(), $ip = host, $hostname = hostname, $description = "shh_auth"];
        Log::write(HOST_INFO::HOST_INFO_LOG, rec);
    }
}

event ssh_auth_successful(c: connection, auth_method_none: bool){
	for ( host in set(c$id$orig_h, c$id$resp_h) )
	{
		check_ssh_hostname(c$id, c$uid, host);
	}
}

event dns_query_reply(c: connection, msg: dns_msg, query: string, qtype: count, qclass: count){
    # print "here comes a dns query reply";
    # print c;
    # print msg;        
    # print query;      
    # print qtype;
}

event dns_A_reply(c: connection, msg: dns_msg, ans: dns_answer, a: addr){
    # print "********************************TYPE A REPLY*********************";
    # print c;
    # print msg;#[id=0, opcode=0, rcode=0, QR=T, AA=T, TC=F, RD=F, RA=F, Z=0, num_queries=0, num_answers=1, num_auth=0, num_addl=0]
    # print ans;#[answer_type=1, query=brwa86bad339915.local, qtype=1, qclass=32769, TTL=4.0 mins]
    # print a;#192.168.1.108
    local rec: HOST_INFO::host_info = [$ts = network_time(), $ip = a, $hostname = ans$query, $description = "dns_A_reply" ];
    Log::write(HOST_INFO::HOST_INFO_LOG, rec);    
}

event dns_AAAA_reply(c: connection, msg: dns_msg, ans: dns_answer, a: addr){
    local rec: HOST_INFO::host_info = [$ts = network_time(), $ip = a, $hostname = ans$query, $description = "dns_AAAA_reply" ];
    Log::write(HOST_INFO::HOST_INFO_LOG, rec); 
}

# I want to get hostnames by event related to DNS.
event dns_message(c: connection, is_orig: bool, msg: dns_msg, len: count){
    # print "dns_message";
    # print "1";
    # print c$dns_state$pending_queries;
    if(c ?$dns_state){
        for(index1 in c$dns_state$pending_queries){
            # print "2";
            # print c$dns_state$pending_queries[index1];
            for(index2 in c$dns_state$pending_queries[index1]$vals){
                local rec: DNS::Info = c$dns_state$pending_queries[index1]$vals[index2];
                # print rec;
                if(rec ?$ answers){
                    print "It has answers!!!!";
                    print rec;
                }
                if(rec ?$ qtype_name){
                    switch(rec$qtype_name){
                        case "A":
                            # print "type A";
                            # print fmt("host %s's query field: %s", rec$id$orig_h, rec$query);
                            break;
                        case "AAAA":
                            # print "type AAAA";
                            break;
                        case "CNAME":
                            # print "type CNAME";
                            break;
                        case "PTR":
                            # print "type PTR";
                            break;
                        case "MX":
                            # print "type MX";
                            break;
                        case "NS":
                            # print "type NS";
                            break;
                        default:
                            # print fmt("unexpected type: %s", rec$qtype_name);
                            break;
                    }
                }
                # Unfortunately, it is not the hostname. :(
            }
        }
    }
}

event dns_mapping_valid(dm: dns_mapping){
    print "dns_mapping_valid";
    print dm;
}

event dns_mapping_altered(dm: dns_mapping, old_addrs: addr_set, new_addrs: addr_set){
    print "dns_mapping_altered";
    print dm;
}

event dns_mapping_lost_name(dm: dns_mapping){
    print "dns_mapping_lost_name";
    print dm;
}

event dns_mapping_new_name(dm: dns_mapping){
    print "dns_mapping_new_name";
    print dm;
}

event dns_mapping_unverified(dm: dns_mapping){
    print "dns_mapping_unverified";
    print dm;
}



event ntlm_authenticate(c: connection, request: NTLM::Authenticate){
    print c;
    print request;
    if(request ?$ user_name){
        print fmt("username: %s", request$user_name);
    }
}

event bro_init() &priority=10{
    # create our log stream at the very beginning
	Log::create_stream(HOST_INFO::HOST_INFO_LOG, [$columns=host_info, $path="host-info"]);
}

event bro_init(){
    print "start";
}

event bro_done(){
    print "finish";
}