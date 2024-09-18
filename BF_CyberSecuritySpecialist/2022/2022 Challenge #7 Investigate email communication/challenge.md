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

The email headers and metadata don't show any signs of end-to-end encryption (like PGP or S/MIME).
End-to-end encryption would require the email to be encrypted by the sender and only decrypted by the final recipient. In this case, no encryption keys or indicators (like application/pgp-encrypted or S/MIME) are visible in the email headers or content.
The message likely travels unencrypted through the MTAs, meaning it could be accessed by intermediaries unless additional measures are taken.
Encryption in Transit
Partially Used:

As seen in the email flow, some hops use ESMTPS and LMTP, which encrypts the communication between Mail Transfer Agents (MTAs) using TLS. This ensures that the data is encrypted during transit between those specific hops, preventing interception of the email in transit.
Examples of encrypted connections:
ESMTPS between some of the MTAs indicates that TLS was used to encrypt data between the server exchanges.
TLS 1.2 is explicitly mentioned between smtp06.mail.qldc.ch and mailin036.protonmail.ch, ensuring that this part of the communication was encrypted.
However, not all MTAs use encryption, so parts of the route may still expose the email to interception. Some hops only use plain SMTP, which means the email could travel unencrypted during these segments.
Encryption at Rest
Unknown:

There is no explicit information in the email headers about whether encryption at rest is enabled on the mail servers involved in the transmission (such as Zoho's, Quickline's, or ProtonMail's mail servers).
Encryption at rest would depend on the policies of each mail provider, but the headers don't provide insights into the encryption of the stored email on the MTAs along the route.
ProtonMail, being known for privacy features, is likely to use encryption at rest for their mail storage. However, we cannot confirm the same for the other MTAs based on this email alone.
Conclusion:
End-to-End Encryption is not implemented in this email transmission.
Encryption in Transit is used partially between certain MTAs, but not consistently throughout the entire email route.
Encryption at Rest remains unknown, and it would depend on each mail provider's policy, though ProtonMail likely offers encryption at rest.
