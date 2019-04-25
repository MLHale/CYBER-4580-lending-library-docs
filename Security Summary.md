# Security Summary

The application is naturally fairly secure, being built with Djangos native authorization functions. While there are CVEs for Django, the version we are using (1.11) has only 3 known vulnerabilities, and only one of those is applicable to our application. That is CVE-2018-14574 which is an Open Redirection Vulnerability. This could allow an attacker to redirect one of our users to a malicious site of their choosing using our page as the launching pad. As this will not affect the usability of our application, we consider this to be a low priority to fix.

The application is also built on Ember (3.4.6). There are very few known vulnerabilities for Ember in general, and none have been released for the version we are using.

An Armitage (Metasploit) Hail Mary attack was executed against the application which resulted in no sessions being created, which is the best outcome possible from a security standpoint. An NMap scan was also conducted, and no excess ports were left open and susceptible to attack. One area of possible concern was located via a DirBuster attack. This tool uses wordlists to constantly send GET requests to the server and documents the response from each request. Using one of the included wordlists in DirBuster
