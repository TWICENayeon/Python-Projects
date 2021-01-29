# Deryck Wong dw1636
from socket import *
msg = "\r\n I love computer networks!"
endmsg = '\r\n.\r\n'
# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start
mailServer = 'smtp.nyu.edu'
#Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailServer, 25))
#Fill in end
recvconnect = clientSocket.recv(1024)
print recvconnect
if recvconnect[:3] != '220':
 print '220 reply not received from server.'
# Send HELO command and print server response.
print "Sending First HELO"
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recvhelo = clientSocket.recv(1024)
print recvhelo
if recvhelo[:3] != '250':
 print '250 reply not received from server.'
# Send MAIL FROM command and print server response.
# Fill in start
print "Sending MAIL FROM Command"
clientSocket.send('MAIL FROM: dw1636@nyu.edu\r\n')
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
 print 'mail from 250 reply not received from server.'
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
print "Sending RCPT TO Command"
clientSocket.send('RCPT TO: dw1636@nyu.edu\r\n')
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
 print 'rcpt to 250 reply not received from server.'
# Fill in end
# Send DATA command and print server response.
# Fill in start
print 'DATA Command'
clientSocket.send('DATA\r\n')
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
 print '250 reply not received from server.'
# Fill in end
# Send message data.
# Fill in start
print 'Data'
clientSocket.send(msg)
# Fill in end
# Message ends with a single period.
# Fill in start
print 'Period'
clientSocket.send(endmsg)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
 print '250 reply not received from server.'
# Fill in end
# Send QUIT command and get server response.
# Fill in start
print 'QUIT'
clientSocket.send('QUIT\r\n')
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
 print '250 reply not received from server.'
print 'Done