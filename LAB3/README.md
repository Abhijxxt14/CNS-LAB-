# Experiment 3 – Access Control List (ACL) Configuration

## Overview

This experiment demonstrates the configuration and implementation of Access Control Lists (ACLs) in a router using Cisco Packet Tracer. ACLs are used to control network traffic by permitting or denying packets based on predefined rules. In this setup, a standard ACL is configured to restrict a specific host from accessing a remote server while allowing other hosts.

---

# Network Topology

Devices used:

* 1 Router (Cisco 2901)
* 1 Switch (2960)
* 3 PCs
* 1 Server

Topology structure:

```
PC0
PC1
PC2
 │
 └── Switch ─── Router ─── Server
```

All PCs are connected to the switch, the switch connects to the router, and the router connects to the server.

---

# IP Addressing Scheme

### PCs

| Device | IP Address  | Subnet Mask   | Default Gateway |
| ------ | ----------- | ------------- | --------------- |
| PC0    | 192.168.1.2 | 255.255.255.0 | 192.168.1.1     |
| PC1    | 192.168.1.3 | 255.255.255.0 | 192.168.1.1     |
| PC2    | 192.168.1.4 | 255.255.255.0 | 192.168.1.1     |

### Server

| Device | IP Address  | Subnet Mask   | Default Gateway |
| ------ | ----------- | ------------- | --------------- |
| Server | 192.168.2.2 | 255.255.255.0 | 192.168.2.1     |

### Router Interfaces

| Interface          | IP Address  | Network        |
| ------------------ | ----------- | -------------- |
| GigabitEthernet0/0 | 192.168.1.1 | LAN Network    |
| GigabitEthernet0/1 | 192.168.2.1 | Server Network |

---

# Router Configuration

## Interface Configuration

```bash
enable
configure terminal

interface gigabitEthernet0/0
ip address 192.168.1.1 255.255.255.0
no shutdown

interface gigabitEthernet0/1
ip address 192.168.2.1 255.255.255.0
no shutdown
```

---

# Standard ACL Configuration

### Goal

Block **PC1 (192.168.1.3)** from accessing the server while allowing other PCs.

```bash
access-list 10 deny 192.168.1.3
access-list 10 permit any
```

Apply ACL to the router interface connected to the server:

```bash
interface g0/1
ip access-group 10 out
```

---

# Testing the Configuration

Connectivity tests were performed using **ping** commands from each PC.

## Test Results

| Source Device | Destination          | Result     |
| ------------- | -------------------- | ---------- |
| PC0           | Server (192.168.2.2) | Successful |
| PC2           | Server (192.168.2.2) | Successful |
| PC1           | Server (192.168.2.2) | Blocked    |

PC1 was successfully restricted from accessing the server as defined by the ACL rule.

---

# Verification Command

To verify ACL functionality on the router:

```bash
show access-lists
```

This command displays the ACL rules and packet match counters, confirming that the deny and permit rules are being applied.

---

# Conclusion

The experiment successfully demonstrated the configuration and implementation of a **standard Access Control List** in Cisco Packet Tracer. The ACL was used to block a specific host from accessing a remote server while allowing other hosts to communicate normally. This shows how ACLs can be used to enhance network security and control traffic flow within a network.
