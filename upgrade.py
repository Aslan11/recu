import subprocess
import sys,os

print("\nThis script will upgrade all the nodes in a Redis Enterprise Cluster")

identity=input('\nEnter the path of the Identity File (.pem) to use for secure copy purposes: ')
tarball=input('\nEnter the path to the tarball (.tar) to upgrade with: ')
ipstring=input('\nEnter the Username & IP addresses of the nodes you wish to upgrade starting with the master node, comma seperated (ubuntu@1.1.1.1,ubuntu@2.2.2.2,ubuntu@3.3.3.3,...): ')
directory=input('\nEnter the directory to scp the tar ball into (blank ok):')
iplist=ipstring.split(',')
# for each node
for ip in iplist:
    # scp the tar ball
    path = ip+":"+directory
    print('\nSecurely copying {0} to {1}'.format(tarball, ip)) 
    p = subprocess.Popen(["scp", "-i", identity, tarball, path])
    sts = os.waitpid(p.pid, 0)
    print(sts)
    print('\nTar ball uploaded to {0}'.format(ip))
    # unpack the tar ball
    print('\nLogging into {0}'.format(ip))
    sesh = subprocess.Popen(["ssh", "-i", identity, ip], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, bufsize=0)
    sesh.stdin.write('sudo tar -xvf {0}\n'.format(tarball))
    sesh.stdin.write('echo END\n')
    sesh.stdin.close() 
    for line in sesh.stdout:
        if line == "END\n":
            break
        print(line,end="")
    print('\nTarball Unpacked\nRunning install script...')
    # run install.sh 
    sesh = subprocess.Popen(["ssh", "-i", identity, ip], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, bufsize=0)
    sesh.stdin.write('sudo ./install.sh -y\n')
    sesh.stdin.write('echo END\n')
    sesh.stdin.close()
    for line in sesh.stdout:
        if line == "END\n":
            break
        print(line,end="")

print('\nScript Completed!')

    


