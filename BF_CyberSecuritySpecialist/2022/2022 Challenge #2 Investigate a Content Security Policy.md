# 2022 Challenge #2 Investigate a Content Security Policy
## Task 1: Investigate Elements Blocked by CSP
- Open the Developer Tools
- Reload Page
- ![image](https://github.com/user-attachments/assets/de6445ca-a5f4-4105-b6e5-3dd470e16f75)
- 
Solution:

1. Resource: http://fonts.googleapis.com/css?family=Droid+Sans<br/>
Blocked by Directive: style-src 'self' cdn.jsdelivr.net

2. Resource: Inline style code.<br/>
Blocked by Directive: style-src 'self' cdn.jsdelivr.net

3. Resource: http://www.diato-cours.net/recmusicsegonde/166.mp3<br/>
Blocked by Directive: media-src 'self'

4. Resource: https://www.ict-berufsbildung.ch/<br/>
Blocked by Directive: frame-src www.whatsmybrowser.com

## Task 2: Investigate Why the External CSS File bootstrap.min.css Can Be Loaded with the Given CSP

- In the developer tools, in the "Network" tab we can see that "bootstrap.min.css" is loaded by "https://cdn.jsdelivr.net"
- ![image](https://github.com/user-attachments/assets/ba891568-0f4e-4ecd-94be-1eb6fd144e71)
- The CSP for the style files allows it:
- ![image](https://github.com/user-attachments/assets/13fc462a-51fb-48a4-a175-239cfc40af11)

## Task 3: Script execution 1

- Clicking the button, a js "alert" is opened
- ![image](https://github.com/user-attachments/assets/b4fd922d-2573-49d5-bee1-abd09ded77b1)
- Let's find where the script is loaded from:
- ![image](https://github.com/user-attachments/assets/ea87d17d-4298-40f0-9d13-93c7f128e6b3)
- Looks like it's in the "head" section of the html. So inline, with a nonce attribute. Let's look at the csp:
- ![image](https://github.com/user-attachments/assets/9974a5b9-51a6-4043-acc0-0e60370fc817)
- The csp accepts scripts from itself, with a nonce.

## Task 4: Script execution 2
- The script is still loaded from the "head" tag in the html.
- This time, it doesn't have a nonce, but the script csp contains an hash condition: "sha256-MVVTTrnP0Dz8favgr4y2gXhPmXy1oudZ9mddaf5PP90="
- Let's try to hash the script:
- ![image](https://github.com/user-attachments/assets/fc13aae2-4af9-41b3-8981-0e3f82450dbc)
- Once hashed and encoded in base64, the script matches the csp. This is why it executes

## Task 5: Testcases
### Testcase1: `<b>This is a <i>testcase</i></b>`
- Output:
![image](https://github.com/user-attachments/assets/3b733853-996f-4fed-9a5f-f7d0078f87f8)
- Since this input does not contain scripts or harmful code, it would not trigger a security mechanism like the CSP. However, the lack of input validation or output encoding could lead to XSS vulnerabilities if more dangerous inputs were allowed.

### Testcase2: `<script>alert(window.origin);</script>`
- Output: Nothing happens.
- The CSP contains the directive script-src 'self' 'nonce-...';, which restricts the execution of inline scripts unless they are explicitly allowed with a nonce. Since the submitted script does not have the correct nonce, it is blocked, preventing XSS.

### Testcase3: `<img src='xxx:x' alt='XSS' onerror="javascript:alert(window.origin)"/>`
- Output:
- ![image](https://github.com/user-attachments/assets/09eea41e-2222-4047-87d5-dd0e64d28a7c)
- The browser refuses to load the image (Refused to load the image 'xxx:x'...) due to the img-src 'self' CSP directive, which only allows images from the same origin.
- Additionally, the inline event handler (onerror="javascript:alert(window.origin)") is blocked because the CSP forbids inline event handlers without the proper nonce or hash
- The CSP is preventing this XSS attack by blocking both the image from loading and the inline JavaScript from being executed. The img-src directive only allows images from the same domain, and the script-src directive requires either a valid nonce or hash for inline event handlers.



  





