# 2022 Challenge #7 Investigate email communication
## Task 1
- Open the mail in https://app.phishtool.com/
- Got to "Received Lines"
  -  Here we can see every MTA (hop) the mail passed through.
  -  ![image](https://github.com/user-attachments/assets/36f75632-ca9d-4657-8201-5b0242510aa0)
- Create a flowchart diagram with draw.io or https://www.eraser.io/diagramgpt
## Task 2
- The header X-Sieve-Redirected-From indicates that the mail was redirected
- The change in receiver happens here:
- ![image](https://github.com/user-attachments/assets/3a6e790b-b7a4-4ec8-83ea-e85da8da9c7d)
- We can tell that mbox09.prod.qlmail.ch has a forwarding rule in place for emails addressed to bkchagent@quickline.ch
- The LMTP protocol is used for delivering emails from an email server to a local delivery agent or mailbox system, but not between MTAs

## Task 3
- Look at the headers in VS code: User-Agent tag says "Zoho mail"
- Zoho mail is a mail service provider. The sender used it to send the mail
- ![image](https://github.com/user-attachments/assets/16dbe6ad-f11a-44f8-855e-1435981e732a)

## Task 4
End-to-End Encryption
Not Used:
End-to-end encryption would require the sender to encode the email and only decrypt it by the final recipient. In this case, no encryption keys or indicators (like application/PGP or S/MIME) are visible in the email headers or content.

Encryption in Transit
Partially Used:
As seen in the email flow, some hops use ESMTPS and LMTP, which encrypts the communication between Mail Transfer Agents (MTAs) using TLS. 
Examples of encrypted connections:
ESMTPS between some MTAs indicates that TLS was used to encrypt data between the server exchanges.
TLS 1.2 is explicitly mentioned between smtp06.mail.qldc.ch and mailin036.protonmail.ch, ensuring that this communication is encrypted. (X-Pm-Transfer-Encryption: TLSv1.2 with cipher ECDHE-RSA-AES256-GCM-SHA384 (256/256 bits); X-Pm-Content-Encryption: on-delivery)

Encryption at Rest
Unknown:
There is no explicit information in the email headers about whether encryption at rest is enabled on the mail servers involved in the transmission.
Encryption at rest would depend on the policies of each mail provider, but the headers don't provide insights into the encryption of the stored email on the MTAs along the route.
