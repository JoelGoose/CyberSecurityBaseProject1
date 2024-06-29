# CSB2024 Course Project 1
Project files can be found https://github.com/JoelGoose/CyberSecurityBaseProject1/tree/main/CyberSecurityBaseProject1/
This project is based on the [2017 OWASP list](https://owasp.org/www-project-top-ten/2017/Top_10)

To run the project, clone the repository and run the following command with all the required dependencies used in the course:

```
python manage.py runserver
```

If all is done correctly, a notes website application can be found at http://127.0.0.1:8000/

The website has the following users:
   |Username|Password|
   |:------:|:------:|
   |bob|squarepants|
   |alice|redqueen|

and an additional super user with the username: super and password: super

## FLAW 1: CSRF (Cross-Site Request Forgery)
Links pinpointing to flaw 1 with fixes commented:
https://github.com/JoelGoose/CyberSecurityBaseProject1/blob/de95d676b61af686e6186a16fc94eb9e50d8fc4c/CyberSecurityBaseProject1/cybersecurityproject/notes/templates/pages/index.html#L32
https://github.com/JoelGoose/CyberSecurityBaseProject1/blob/de95d676b61af686e6186a16fc94eb9e50d8fc4c/CyberSecurityBaseProject1/cybersecurityproject/notes/templates/pages/index.html#L39
https://github.com/JoelGoose/CyberSecurityBaseProject1/blob/de95d676b61af686e6186a16fc94eb9e50d8fc4c/CyberSecurityBaseProject1/cybersecurityproject/notes/views.py#L13
https://github.com/JoelGoose/CyberSecurityBaseProject1/blob/de95d676b61af686e6186a16fc94eb9e50d8fc4c/CyberSecurityBaseProject1/cybersecurityproject/notes/views.py#L38-39
https://github.com/JoelGoose/CyberSecurityBaseProject1/blob/de95d676b61af686e6186a16fc94eb9e50d8fc4c/CyberSecurityBaseProject1/cybersecurityproject/notes/views.py#L13

Cross-Site Request Forgery (CSRF) is an attack that forces an authenticated user to execute an unwanted action. In this type of attack, an attacker tricks the user into performing an action of the attacker’s choosing, such as changing their password. The confirmation window that appears during the attack is not sufficient to prevent it, as it relies on client-side scripting. Therefore, additional forms of protection are necessary.

For example, an attacker could change someone’s password while they are logged in by creating an HTML file with an <img> tag. Instead of displaying an image, the tag would execute the password-changing script. This scenario is similar to the programming exercise part3-18.csrf in the course [Securing Software](https://cybersecuritybase.mooc.fi/module-2.3/1-security)

To fix these issues and prevent unwanted actions, GET method should be avoided as they can skip the validation process, which is why the password changing should use POST instead. Along that implementing CSRF tokens is essential. When the user submits a form, the server checks if the token matches the expected value.

## FLAW 2: Injection

Link pinpointing to flaw 2 with fixes commented:
https://github.com/JoelGoose/CyberSecurityBaseProject1/blob/de95d676b61af686e6186a16fc94eb9e50d8fc4c/CyberSecurityBaseProject1/cybersecurityproject/notes/views.py#L15-21

Injections were extremely prevalent security issues in the past, even though they are easily spotted. Nonetheless, injections remain a serious concern, even in modern times. Injections occur when an attacker can send damaging data to an interpreter. In the context of web applications, one common type of injection is SQL injection.

The current implementation for adding notes works with unsanitized SQL query inputs, which allows an attacker to manipulate the database on which the web application is based. This vulnerability poses a serious risk, as SQL injections can lead to catastrophic damages, including data deletion, unauthorized modification, and unauthorized access to sensitive information. In this application, attackers can input their malicious queries in the ‘Post additional note’ section to gain unauthorized access.

To address this issue, we have to consider an alternative approach. Instead of manipulating the database directly through queries, creating objects using the application’s models through django will allow the application to safely secure them.

## FLAW 3: Broken Access Control

Link pinpointing to flaw 3 with fixes commented:
https://github.com/JoelGoose/CyberSecurityBaseProject1/blob/de95d676b61af686e6186a16fc94eb9e50d8fc4c/CyberSecurityBaseProject1/cybersecurityproject/notes/views.py#L36
https://github.com/JoelGoose/CyberSecurityBaseProject1/blob/de95d676b61af686e6186a16fc94eb9e50d8fc4c/CyberSecurityBaseProject1/cybersecurityproject/notes/views.py#L38-39

Users should not be allowed to do whatever they please. Therefore, restrictions are imposed on their actions. However, these restrictions are sometimes not properly enforced, allowing attackers to exploit them to their advantage. Potential attacks include gaining access to other accounts, viewing sensitive files, and modifying user data, among others. In this application, attackers can manipulate user accounts by changing their passwords. For instance, by simply opening the following link: http://127.0.0.1:8000/changepassword/?user=alice&password=attacked, an attacker can swap Alice’s password to “hacked” and gain unauthorized access.

to fix this issue, the application needs to use POST requests instead of relying on GET requests, which can be manipulated, ensure that sensitive actions. Due to the change from GET to POST,  additional CSRF tokens need to be implemented. However, this is not sufficient enough as you still can easily fake POST calls in the user field. Changes need to be made on how the user is retrieved. 

## FLAW 4: Security Misconfiguration

Link pinpointing to flaw 4 with fixes commented:
https://github.com/JoelGoose/CyberSecurityBaseProject1/blob/de95d676b61af686e6186a16fc94eb9e50d8fc4c/CyberSecurityBaseProject1/cybersecurityproject/cybersecurityproject/settings.py#L27-29

Security misconfigurations occur when a web application is not set up securely, allowing unintended and potentially harmful access or exposure of sensitive information. These misconfigurations can manifest at various layers of the application stack, including web servers, databases, and application frameworks. They are often overlooked issues that can sneak into a production web application. Such misconfigurations may happen at any level of the application and typically arise when security considerations are disregarded due to other development priorities. In the case of security misconfiguration, attackers can potentially gain access to the system’s functionality. For instance, if an application is running in debug mode and allows any hosts, it becomes vulnerable to arbitrary host headers. These headers can be manipulated by attackers to execute code based on a forged domain.

To fix these issues, the debug option should be set to false and along that a whitelist of allowed hosts and domain names to mitigate unwanted requests



## FLAW 5: Insufficient Logging & Monitoring

Link pinpointing to flaw 5 with fixes commented:
https://github.com/JoelGoose/CyberSecurityBaseProject1/blob/de95d676b61af686e6186a16fc94eb9e50d8fc4c/CyberSecurityBaseProject1/cybersecurityproject/notes/views.py#L7-9
https://github.com/JoelGoose/CyberSecurityBaseProject1/blob/de95d676b61af686e6186a16fc94eb9e50d8fc4c/CyberSecurityBaseProject1/cybersecurityproject/notes/views.py#L28
https://github.com/JoelGoose/CyberSecurityBaseProject1/blob/de95d676b61af686e6186a16fc94eb9e50d8fc4c/CyberSecurityBaseProject1/cybersecurityproject/notes/views.py#L43

An often overlooked issue is proper logging and monitoring of what is happening in a web application, and it has a surprisingly easy fix. By enabling logging throughout the code, system administrators can monitor changes made by users. This allows administrators to detect odd and suspicious activity, which could signal that the web application is under attack.

[Django offers a logging system](https://docs.djangoproject.com/en/5.0/topics/logging/) that can be used and configured according to the application’s needs in settings.py. However, for this application, we will use the default logger, which is sufficient.
