# 2022 Challenge #8 Analyze certificates
## Task 1
- Use nmap to scan ports with certificates:`nmap -Pn --script ssl-cert`
- ![image](https://github.com/user-attachments/assets/a30b31a2-3404-4d84-95fe-dfca8df38434)
- List of ports with certificates

## Task 2
- Scan a port certificate with `sslscan IP:port`
 ```
  └─$ sslscan 152.96.15.2:443   
Version: 2.1.3-static
OpenSSL 3.0.12 24 Oct 2023

Connected to 152.96.15.2

Testing SSL server 152.96.15.2 on port 443 using SNI name 152.96.15.2

  SSL/TLS Protocols:
SSLv2     disabled
SSLv3     disabled
TLSv1.0   enabled
TLSv1.1   disabled
TLSv1.2   enabled
TLSv1.3   enabled

  TLS Fallback SCSV:
Server supports TLS Fallback SCSV

  TLS renegotiation:
Secure session renegotiation supported

  TLS Compression:
Compression disabled

  Heartbleed:
TLSv1.3 not vulnerable to heartbleed
TLSv1.2 not vulnerable to heartbleed
TLSv1.0 not vulnerable to heartbleed

  Supported Server Cipher(s):
Preferred TLSv1.3  128 bits  TLS_AES_128_GCM_SHA256        Curve 25519 DHE 253
Accepted  TLSv1.3  256 bits  TLS_AES_256_GCM_SHA384        Curve 25519 DHE 253
Accepted  TLSv1.3  256 bits  TLS_CHACHA20_POLY1305_SHA256  Curve 25519 DHE 253
Preferred TLSv1.2  256 bits  ECDHE-RSA-AES256-GCM-SHA384   Curve 25519 DHE 253
Accepted  TLSv1.2  256 bits  ECDHE-RSA-CHACHA20-POLY1305   Curve 25519 DHE 253
Accepted  TLSv1.2  256 bits  ECDHE-ARIA256-GCM-SHA384      Curve 25519 DHE 253
Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-GCM-SHA256   Curve 25519 DHE 253
Accepted  TLSv1.2  128 bits  ECDHE-ARIA128-GCM-SHA256      Curve 25519 DHE 253
Accepted  TLSv1.2  256 bits  ECDHE-RSA-AES256-SHA384       Curve 25519 DHE 253
Accepted  TLSv1.2  256 bits  ECDHE-RSA-CAMELLIA256-SHA384  Curve 25519 DHE 253
Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-SHA256       Curve 25519 DHE 253
Accepted  TLSv1.2  128 bits  ECDHE-RSA-CAMELLIA128-SHA256  Curve 25519 DHE 253
Accepted  TLSv1.2  256 bits  ECDHE-RSA-AES256-SHA          Curve 25519 DHE 253
Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-SHA          Curve 25519 DHE 253
Accepted  TLSv1.2  256 bits  AES256-GCM-SHA384            
Accepted  TLSv1.2  256 bits  AES256-CCM8                  
Accepted  TLSv1.2  256 bits  AES256-CCM                   
Accepted  TLSv1.2  256 bits  ARIA256-GCM-SHA384           
Accepted  TLSv1.2  128 bits  AES128-GCM-SHA256            
Accepted  TLSv1.2  128 bits  AES128-CCM8                  
Accepted  TLSv1.2  128 bits  AES128-CCM                   
Accepted  TLSv1.2  128 bits  ARIA128-GCM-SHA256           
Accepted  TLSv1.2  256 bits  AES256-SHA256                
Accepted  TLSv1.2  256 bits  CAMELLIA256-SHA256           
Accepted  TLSv1.2  128 bits  AES128-SHA256                
Accepted  TLSv1.2  128 bits  CAMELLIA128-SHA256           
Accepted  TLSv1.2  256 bits  AES256-SHA                   
Accepted  TLSv1.2  256 bits  CAMELLIA256-SHA              
Accepted  TLSv1.2  128 bits  AES128-SHA                   
Accepted  TLSv1.2  128 bits  CAMELLIA128-SHA              
Preferred TLSv1.0  256 bits  ECDHE-RSA-AES256-SHA          Curve 25519 DHE 253
Accepted  TLSv1.0  128 bits  ECDHE-RSA-AES128-SHA          Curve 25519 DHE 253
Accepted  TLSv1.0  256 bits  AES256-SHA                   
Accepted  TLSv1.0  256 bits  CAMELLIA256-SHA              
Accepted  TLSv1.0  128 bits  AES128-SHA                   
Accepted  TLSv1.0  128 bits  CAMELLIA128-SHA              

  Server Key Exchange Group(s):
TLSv1.3  128 bits  secp256r1 (NIST P-256)
TLSv1.3  192 bits  secp384r1 (NIST P-384)
TLSv1.3  260 bits  secp521r1 (NIST P-521)
TLSv1.3  128 bits  x25519
TLSv1.3  224 bits  x448
TLSv1.2  128 bits  secp256r1 (NIST P-256)
TLSv1.2  192 bits  secp384r1 (NIST P-384)
TLSv1.2  260 bits  secp521r1 (NIST P-521)
TLSv1.2  128 bits  x25519
TLSv1.2  224 bits  x448

  SSL Certificate:
Signature Algorithm: sha256WithRSAEncryption
RSA Key Strength:    2048

Subject:  www.mycompany.local
Altnames: DNS:domain
Issuer:   Root CA

Not valid before: Sep 20 13:05:53 2024 GMT
Not valid after:  Sep 20 13:05:53 2025 GMT
```
- Find security improvements to do, for exemple:
  - Disable TLS 1.0
  - Enable HSTS
  - Disable weak cyphers (128 bit key)

 ## Task 3
 
- Download the CSV and check for:
  - Expired/Revoked certificates
  - Wildcard/subwildcard domains
  - Selfsigned certs and R3 (Let's Encrypt) are considered weak in the exam
    - Depends on the context and use, but the exam specifies " business context"
  - CRL + OCSP missing
  - Weak signature algorithm or public key
  - DNS name not matching with CN
 
 
