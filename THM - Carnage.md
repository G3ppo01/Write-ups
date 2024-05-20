<h1>TryHackMe room - Carnage</h1>
<h4>Write-up by G3ppo01</h4>
<p>Room Link: https://tryhackme.com/r/room/c2carnage</p>
<p>Categories:</p>
<ul>
  <li>Network</li>
  <li>Traffic Analysis</li>
  <li>Wireshark</li>
</ul>

<h2>Scenario</h2>
<span>Eric Fischer from the Purchasing Department at Bartell Ltd has received an email from a known contact with a Word document attachment.  Upon opening the document, he accidentally clicked on "Enable Content."  The SOC Department immediately received an alert from the endpoint agent that Eric's workstation was making suspicious connections outbound. The pcap was retrieved from the network sensor and handed to you for analysis. 

Task: Investigate the packet capture and uncover the malicious activities. 

*Credit goes to Brad Duncan for capturing the traffic and sharing the pcap packet capture with InfoSec community. 

NOTE: DO NOT directly interact with any domains and IP addresses in this challenge. </span>

<h2>Tasks and investigations</h2>

<p>First, we need to start the THM virtual machine, so that we can search the pcap file with Wireshark and answer the questions.<br>
Once the VM is ready, let's open the "carnage.pcap" in the /home/ubuntu/Desktop/Analysis/ directory. </p>

<h3>Question 1 - What was the date and time for the first HTTP connection to the malicious IP?</h3>
<p>I set a filter to <strong>"HTTP"</strong> and add a column to have the requested date format</p>
<img src="https://github.com/G3ppo01/Write-ups/assets/170022041/91ce77a1-7465-41d4-bed0-9ad8ead9dbdc">


<h3>Question 2 - What is the name of the zip file that was downloaded?</h3>
<p>We can see the answer to this one in the tacket we already found, in the "info" column</p>

<h3>Question 3 - What was the domain hosting the malicious zip file?</h3>
<p>In Wireshark, open "Edit --> Preferences --> Name Resolution" and tick "Resolve network(IP) addresses".<br>
You will now find the answer in the destination column</p>

<h3>Question 4 - Without downloading the file, what is the name of the file in the zip file?</h3>
<p>Find the answer packet, it comes from the same IP address, with a 200 code. Open the packet detail and search in the "data" field</p>
<img src="https://github.com/G3ppo01/Write-ups/assets/170022041/e21006ba-cbba-4ebc-90b5-c649b1b2d17a">

<h3>Question 5 - What is the name of the webserver of the malicious IP from which the zip file was downloaded?</h3>
<p>Search for the "server" field in the "HTTP" layer of the same packet</p>

<h3>Question 6 - What is the version of the webserver from the previous question?</h3>
<p>Search for the "x-powered-by" field in the "HTTP" layer of the same packet</p>

<h3>Question 7 - Malicious files were downloaded to the victim host from multiple domains. What were the three domains involved with this activity?</h3>
<p>I used the hint for this one: <em>Check HTTPS traffic. Narrow down the timeframe from 16:45:11 to 16:45:30.</em><br>
Wireshark will show the HTTP traffic as "TLS" by default, so I set a filter to <strong>tls</strong><br>
Then, scrolling through the pcap, I see that some addresses have sent many packets.<br>
I tried using those as answers and they are the Malicious domains</p>

<h3>Question 8 - Which certificate authority issued the SSL certificate to the first domain from the previous question?</h3>
<p>Search for the TLS handshake ("Client Hello", "Server Hello" and "Server Hello done" packets). <br>
We can find the answer in the "Server Hello Done" packet </p>
<img src="https://github.com/G3ppo01/Write-ups/assets/170022041/381b214d-0d00-435d-8b74-1654b71dacb9">

<h3>Question 9 - What are the two IP addresses of the Cobalt Strike servers? Use VirusTotal (the Community tab) to confirm if IPs are identified as Cobalt Strike C2 servers. (answer format: enter the IP addresses in sequential order)</h3>
<p>I made a quick Google search to find how cobalt strike servers communicate and found out it does by HTTP. </br>
I set my filter to HTTP again and scrolling through the pcap, I see that some addresses have sent many packets constantly through the whole capture.</br>
I then search those IPs in Virustotal. In the community section, there is the following post, that confirms the IP is identified as Cobalt Strike C2 server</p>
<img src=https://github.com/G3ppo01/Write-ups/assets/170022041/fccbebe3-3505-4759-9e15-2ce6a96944b2>

<h3>Question 10 - What is the Host header for the first Cobalt Strike IP address from the previous question?</h3>
<p>I filter to see only the IP address I'm searching for (ip.addr == IP address). </br>
Take the first HTTP packet in the list, and check for the info I need</p>
<img src=https://github.com/G3ppo01/Write-ups/assets/170022041/553c6518-3b8e-4be3-a8c5-277a883721fb>

<h3>Question 11 - What is the domain name for the first IP address of the Cobalt Strike server? You may use VirusTotal to confirm if it's the Cobalt Strike server (check the Community tab).</h3>
<p>As said in the question, I checked the comment in the Virustotal Community tab, and the domain is written there</p>

<h3>Question 12 - What is the domain name of the second Cobalt Strike server IP?  You may use VirusTotal to confirm if it's the Cobalt Strike server (check the Community tab).</h3>
<p>As said in the question, I checked the comment in the Virustotal Community tab, and the domain is written there</p>

<h3>Question 13 - What is the domain name of the post-infection traffic?</h3>
<p>I enabled the IP resolution in Wireshark and filtered for HTTP.</br>
I found that the domain for the first connection after the .zip download was constantly present for a part of the HTTP communications.</p>

<h3>Question 14 - What are the first eleven characters that the victim host sends out to the malicious domain involved in the post-infection traffic? </h3>
<p>Take the first packet sent to the previous domain, and take the first 11 characters in the POST request (POST /xxxx)</p>

<h3>Question 15 - What was the length for the first packet sent out to the C2 server?</h3>
<p>The length of the packet we were looking at for question 14</p>

<h3>Question 16 - What was the Server header for the malicious domain from the previous question?</h3>
<p>Check for a response packet from this domain (HTTP 200). In the packet details, in the HTTP layer, search for the "server" field</p>

<h3>Question 17 - The malware used an API to check for the IP address of the victim’s machine. What was the date and time when the DNS query for the IP check domain occurred? (answer format: yyyy-mm-dd hh:mm:ss UTC)</h3>
<p>I filtered for every DNS request containing the victim IP address, and the keyword "API". The first request corresponded to an MSN API, so I took the second one. </br>
Look at the date on which the packet was sent and you have the answer.</p>

<h3>Question 18 - What was the domain in the DNS query from the previous question?</h3>
<p>The answer is in the "info" column for the packet we were investigating in the last question.</p>

<h3>Question 19 - Looks like there was some malicious spam (malspam) activity going on. What was the first MAIL FROM address observed in the traffic?</h3>
<p>I filtered for the SMTP protocol, and searched for the packets containing "MAIL FROM". (smtp && frame contains "MAIL FROM")</p>

<h3>Question 20 - How many packets were observed for the SMTP traffic?</h3>
<p>Just filter for SMTP packets, and look at the "Displayed" number on the lower right corner of Wireshark</p>




