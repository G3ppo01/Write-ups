# [CSS Exam 2023 - 02] Examine an email
## Task 1
- I used https://mxtoolbox.com/ and phishtool.com to analyse the headers
- I installed an .eml extension on vscode to have it as text
- First thing, we notice that the DKIM body hash is wrong:
-   ![image](https://github.com/user-attachments/assets/16e68f12-3581-412d-92a5-faf7e35ee2a0)
- Looking at the mail on VsCode, we notice that the plaintext version of the message and the html version are differents:
-   ![image](https://github.com/user-attachments/assets/4c557c03-7465-4994-be78-e4175686871f)
- Finnaly, if we convert the epoch timestamp from the dkim tags, it does not corresponds with what the other headers say.

## Task 2
- Converting the DKIM timespamp, we get the answer.
  ![image](https://github.com/user-attachments/assets/47c83499-cbc8-4f57-8da7-29b21651536f)

