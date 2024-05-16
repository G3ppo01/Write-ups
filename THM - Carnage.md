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
<p>I set a filter to <strong>"http"</strong> and add a column to have the requested date format</p>
<img src="https://github.com/G3ppo01/Write-ups/assets/170022041/91ce77a1-7465-41d4-bed0-9ad8ead9dbdc">


<h3>Question 2 - What is the name of the zip file that was downloaded?</h3>
<p>We can see the answer to this one ine the tacket we already fond, in the "info" column</p>

<h3>Question 3 - What was the domain hosting the malicious zip file?</h3>
<p>In Wireshark, open "Edit --> Preferences --> Name Resolution" and tick "Resolve network(IP) addresses".<br>
You will now find the answer in the destination column</p>

<h3>Question 4 - Without downloading the file, what is the name of the file in the zip file?</h3>
<p>Find the answer packet, it comes from the same ip address, with a 200 code. Open the packet detail and search in the "data" field</p>
<img src="https://github.com/G3ppo01/Write-ups/assets/170022041/e21006ba-cbba-4ebc-90b5-c649b1b2d17a">

<h3>Question 5 - What is the name of the webserver of the malicious IP from which the zip file was downloaded?</h3>
<p>Search for the "server" field in the "http" layer of the same packet</p>

<h3>Question 6 - What is the version of the webserver from the previous question?</h3>
<p>Search for the "x-powered-by" field in the "http" layer of the same packet</p>

<h3>Question 7 - Malicious files were downloaded to the victim host from multiple domains. What were the three domains involved with this activity?</h3>
<p>I used the hint for this one: <em>Check HTTPS traffic. Narrow down the timeframe from 16:45:11 to 16:45:30.</em><br>
Wireshark will show the https traffic as "TLS" by default, so I set a filter to <strong>tls</strong><br>
Then, scrolling trought the pcap, I can see that some adresses have sent a lot of packets.<br>
I try using thoses as answer and they are un fact the Mmlicious domains</p>

<h3>Question 8 - Which certificate authority issued the SSL certificate to the first domain from the previous question?</h3>
<p>Search for the TLS handshake ("Client Hello", "Server Hello" and "Server Hello done" packets). <br>
We can find the answer in the "Server Hello done" packet </p>
<img src="https://github.com/G3ppo01/Write-ups/assets/170022041/381b214d-0d00-435d-8b74-1654b71dacb9">







