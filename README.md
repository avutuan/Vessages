# Communication Networks Final Project - _Vessages_

Created by: **Tuan Vu**

Description of App: **An instant messaging platform that is defined by a client-server architecture that has user authentication and real-time online status.**

## Required Features

The following **required** functionality is completed:

- [ ] **Client-Server Architecture**
  - [ ] **Client can connect to the server using correct IP and port**
  - [ ] **Client can send and receive msgs to/from the server following TCP connection**
  - [ ] Client reconnects to the server if a connection is lost (Bonus)
  - [ ] Client gracefully exits without affecting other connected clients (Bonus)
  - [ ] **Server can bind to a specific IP and port for incoming client connections**
  - [ ] **Server can handle multiple simultaneous client connections using threads or async I/O**
  - [ ] Server can gracefully handle client disconnections without crashing (Bonus)
  - [ ] **Server maintains a list of active client connections in memory**
  - [ ] **Server interprets and responds to client commands**
- [ ] **User Authentication**
  - [ ] **Clients can register new accounts with REGISTER <username> <password> command**
  - [ ] **Server should validate unique username on registration and stores new user into file**
  - [ ] **Server sends error if the username already exists on registration**
  - [ ] **Client can log into account with LOGIN <username> <password> command**
  - [ ] **Server validates the username and password**
  - [ ] **Server sends success or error message upon login attempt**
  - [ ] **Server keeps track of logged-in users and prevents duplicate logins with the same username**
- [ ] **Online Clients**
  - [ ] **Server maintains an updated list of online clients in-memory**
  - [ ] **Clients receive a list of online users upon login**
  - [ ] Server broadcasts updates to all connected clients when a user logs in or out
  - [ ] **Clients can send a WHO command to request a current list of online users**
- [ ] **Messaging**
  - [ ] **Client can send a direct message to another online user using SEND <username> <message> command**
  - [ ] **Server validates recipient username is online and forwards message, else server sends error to sender client**
  - [ ] **Client receives the message in real-time**
  - [ ] Messages are displayed with a sender's username and timestamp
- [ ] **Database/File Storage**
  - [ ] **File schema includes a users object that contains fields for a username, password, and status**
  - [ ] **File is updated in real-time for user registration and login attempts
  - [ ] File can be backed up and restored without data loss
