# Redis Enterprise Cluster Upgrade Script
-----
##### Dependencies:
1. Python3
2. .pem file to ssh / scp into servers
3. .tar of the version of Redis Enterprise you wish to upgrade to
4. Sudo permission on the server

##### Instructions:
1. `python3 upgrade.py` and follow the prompts. Make sure you enter the master of the cluster first when it comes time to enter in the username and ip's of the nodes.
