# [CSS Exam 2023 - 07] Analyze certificates
## Task 1
- Scann the host with nmap: `nmap -Pn -p1-65535 --script ssl-cert [IP]`
![image](https://github.com/user-attachments/assets/da1a8807-25ba-4a84-88d1-6081f921a9f4)
- Open ports with certificate: 4443; 8080; 9990; 30443
- Port 4786; 8081; 21021 are open but no certificate.

## Task 2
- I will scan port 4443 with the command `sslscan [IP:PORT]` on a Kali VM to get the full certificate:
![image](https://github.com/user-attachments/assets/93521f8a-d354-4432-a259-1a08cc88eb49)

- We can see some security improvements to do by looking at it:
1. Disable SSL v3
2. Enable TLS v1.3
3. Disable weak ciphers (DHE 1024 bits ciphers; 128 bits cyphers like TLS_RSA_WITH_RC4_128_SHA or TLS_RSA_WITH_RC4_128_MD5)

## Task 3
|Certificate Number|Serial Number|Reason|
| -------------| -------------| -------------|
|2|34682d8bbc9e2a6ee7aab92c905c30f12cd78497|Certificate is Revoked|
|17|116b2ee79cd966e56d09da640bb9a12f080b5a36|MD5 signature|
|10|40af19f317960c8e2818520e387c1dfe6267ee41|Redirect: Invalid DNS|
|15|116b2ee79cd966e56d09da640bb9a12f080b5a29|No CRL/OCSP|
|3|2ad0eca813cc632f839222524e7cb5a9a5c8bb57|SHA1 signature|
|1|4347bd35cdd8ffeca943775957063ac6827|R3 Let's Encrypt not suitable for business use|
|5|463398b2924189f46a19a4b4207cd5b97f1|R3 Let's Encrypt not suitable for business use; Expired|
|13|5075d31269e8bca983c247eabe77c26a7b7d440d|TLS 1.1 is weak; TLS1_1, ALPN_HTTP2, ALPN|
|6|760ada9c476ddbc0964f98bd17f297750e6c5568|SubWildcard|
|12|760ada9c476ddbc0964f98bd17f297750e6c5564|Wildcard|
|14|1ddf0950fcfc0ef81259120e981c336f44c5a6ae|Duration to long + Self-Signed|
|19|597f85084860344ff5fef2abf201839b3c6cab0|Expired|



