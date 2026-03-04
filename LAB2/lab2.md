# Experiment–2: AAA Server Based Authentication Using Cisco Packet Tracer

## Subject
Computer Networking: Security (CSE 3752)

---

## Aim
To implement an **AAA (Authentication, Authorization, and Accounting) server** as a user authentication technique for remote access to a network device using **Cisco Packet Tracer**.

---

## Objectives

1. To study the concept of AAA used in a secure system  
2. To configure and verify **AAA server-based username–password authentication using Telnet**  
3. To configure and verify **AAA server-based username–password authentication using SSH**

---

## Software / Tools Used
- Cisco Packet Tracer  
- Router (2901)  
- Switch (2960)  
- PC-PT  
- Server-PT (AAA Server)

---

## Network Topology

```
PC1 ---- Switch ---- Router1
           |
        Server0
```

---

## IP Address Configuration

### PC1
- IP Address: 192.168.1.10  
- Subnet Mask: 255.255.255.0  
- Gateway: 192.168.1.1  

### Server0
- IP Address: 192.168.1.20  
- Subnet Mask: 255.255.255.0  
- Gateway: 192.168.1.1  

### Router1 (Gi0/0)
- IP Address: 192.168.1.1  
- Subnet Mask: 255.255.255.0  

---

## Objective 1: Overview of AAA

AAA provides centralized control over:
- **Authentication** – verifies user identity  
- **Authorization** – controls access privileges  
- **Accounting** – records user activities  

In this experiment, the router authenticates users using a **central AAA server** instead of local credentials.

---

## Objective 2: AAA-Based Authentication Using Telnet

### Router Configuration

```bash
enable
configure terminal
aaa new-model

radius-server host 192.168.1.20 key radius123

aaa authentication login default group radius local

line vty 0 4
login authentication default
transport input telnet
exit

end
write memory
```

---

### Server Configuration (AAA Server)

- AAA Service: **ON**
- RADIUS: **Enabled**
- Shared Secret: `radius123`

#### User Setup

```
Username: CNSLab
Password: cisco
```

#### Network Configuration (RADIUS Client)

```
Client Name  : Router1
Client IP    : 192.168.1.1
Server Type  : Radius
Key          : radius123
```

---

### Verification (Objective 2)

From PC1:

```bash
telnet 192.168.1.1
```

Login using:

```
Username: CNSLab
Password: cisco
```

**Result:** Telnet login successful using AAA server authentication.

---

## Objective 3: AAA-Based Authentication Using SSH

### Router Configuration

```bash
enable
configure terminal
hostname Router1
ip domain-name cnslab.com

crypto key generate rsa
# Key size: 1024

line vty 0 4
login authentication default
transport input ssh
exit

end
write memory
```

---

### Verification (Objective 3)

From PC1:

```bash
ssh -l CNSLab 192.168.1.1
```

Password:

```
cisco
```

**Result:** SSH login successful with AAA server authentication.

---

## Comparison: Telnet vs SSH

| Feature      | Telnet        | SSH           |
|--------------|---------------|---------------|
| Encryption   | Unencrypted   | Encrypted     |
| Port         | Port 23       | Port 22       |
| Security     | Less secure   | Highly secure |

---

## Conclusion
AAA server-based authentication was successfully configured and verified on a Cisco router using **Telnet** and **SSH**. Telnet provided basic authentication, while SSH ensured secure and encrypted remote access.

---
