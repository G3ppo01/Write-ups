# 2022 Challenge #6 Analyze network traffic
## Task 1
- Add "Stream index" as column
- ![image](https://github.com/user-attachments/assets/b5fbb133-1ef8-4992-b83c-22d408ad924f)
- Follow the TCP handshakes (SYN;SYN, ACK; ACK) with the help of the indexes (The packets with the same index are from the same tcp stream).
## Task 2
- ![image](https://github.com/user-attachments/assets/39c7f73e-3fa2-4f1c-a268-c6449d3adbd0)
- The request type is "PSH, ACK", as seen in the picture. 
- PSH (Push): Commands immediate transmission of data, bypassing buffered data transfer to ensure timely delivery of information.
- The intent could be to cause potential buffering issues.
## Task 3
- An attacker can prevent the server from responding to valid traffic by flooding a server with spurious PUSH and ACK requests. This technique is called a PUSH or ACK flood.
- It is a type of DOS attack, which aims to disturb a service's availability.
## Task 4
- ![image](https://github.com/user-attachments/assets/9cdcd558-ff52-49fd-84f4-6d6da1d28cb8)
- You can find the User Agent in a PSH packet. Use internet/chatgpt/your notes and knowledge to answer the OS, browser and version.
## Task 5
- Denial Of Service attack defeats availability (Confidentiality, Integrity, Availability)
## Task 6
- **Denial** of service (Denial, Alteration, Disclosure)
