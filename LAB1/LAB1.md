# Experiment–1: User Authentication for Remote Access Using Cisco Packet Tracer

## Subject
Computer Networking: Security (CSE 3752)

---

## Aim
To implement **user authentication techniques** for remote access of a network device using **Cisco Packet Tracer**, and to configure and verify authentication using **Telnet** and **SSH**.

---

## Objectives

### Objective 1
- To understand the importance of user authentication in a secured system  
- To configure and verify **local username–password authentication using Telnet**

### Objective 2
- To configure and verify **local username–password authentication using SSH**

---

## Software / Tools Used
- Cisco Packet Tracer  
- Cisco Router 2901  
- Cisco Switch 2960-24TT  
- PC-PT  

---

## Network Topology (Logical View)

```
PC0 —— Switch0 —— Router0
```

### IP Configuration

| Device | Interface | IP Address | Subnet Mask | Gateway |
|------|----------|------------|-------------|---------|
| PC0 | Fa0 | 192.168.1.10 | 255.255.255.0 | 192.168.1.1 |
| Router0 | Gi0/0 | 192.168.1.1 | 255.255.255.0 | — |

---

## Objective 1: Local User Authentication Using Telnet

### Step 1: Enter Privileged and Global Configuration Mode

```cisco
enable
configure terminal
```

---

### Step 2: Configure Router Interface

```cisco
interface gigabitEthernet0/0
ip address 192.168.1.1 255.255.255.0
no shutdown
exit
```

---

### Step 3: Create Local User Account

```cisco
username CNSLab privilege 15 password cisco
```

---

### Step 4: Encrypt Passwords

```cisco
service password-encryption
```

---

### Step 5: Enable Telnet with Local Authentication

```cisco
line vty 0 4
login local
transport input telnet
exit
```

---

### Step 6: Save Configuration

```cisco
end
write memory
```

---

### Verification (Telnet)

From **PC0 → Desktop → Command Prompt**:

```bash
telnet 192.168.1.1
```

Login credentials:
- **Username:** CNSLab
- **Password:** cisco

**Result:** Telnet login successful.

---

## Objective 2: Local User Authentication Using SSH

### Step 1: Enter Global Configuration Mode

```cisco
enable
configure terminal
```

---

### Step 2: Configure Hostname and Domain Name

```cisco
hostname Router0
ip domain-name cnslab.com
```

---

### Step 3: Generate RSA Keys

```cisco
crypto key generate rsa
```

Key size: `1024`

---

### Step 4: Enable SSH on VTY Lines

```cisco
line vty 0 4
login local
transport input ssh
exit
```

---

### Step 5: Save Configuration

```cisco
end
write memory
```

---

### Verification (SSH)

From **PC0 → Desktop → Command Prompt**:

```bash
ssh -l CNSLab 192.168.1.1
```

Password: `cisco`


**Result:** SSH login successful.

---

## Viva / Exam Questions

### Importance of User Authentication
- Prevents unauthorized access  
- Protects network devices  
- Ensures accountability  
- Enhances network security  

---

### Commands

**Create user:**
```cisco
username CNSLab password cisco
```

**Set privilege level:**
```cisco
username CNSLab privilege 15 password cisco
```

**Encrypt passwords:**
```cisco
service password-encryption
```

---

### Features of SSH
- Encrypted communication  
- Secure remote access  
- Uses public key cryptography  
- Protects against eavesdropping  

---

### SSH vs Telnet

| Telnet | SSH |
|------|-----|
| Unencrypted | Encrypted |
| Insecure | Secure |
| Port 23 | Port 22 |

---

## Conclusion
Local user authentication for remote access was successfully implemented and verified using **Telnet** and **SSH** on a Cisco router using Cisco Packet Tracer.