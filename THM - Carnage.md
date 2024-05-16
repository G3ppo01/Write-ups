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
<img src="https://github.com/G3ppo01/Write-ups/assets/170022041/544d9d95-e501-4214-b266-2cbd7f13a275">
