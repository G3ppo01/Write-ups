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

