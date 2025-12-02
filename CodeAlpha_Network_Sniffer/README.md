
# 🕵️‍♀️ Python Network Sniffer

A simple Python based network traffic sniffer built using Scapy.

---

## ✨ Features

* 📡 **Live packet capture** (no file needed)
* 🧭 **Source and Destination IP extraction**
* 🔎 **Protocol identification** (TCP, UDP, ICMP)
* ⏱ **Timestamp logging**
* 📄 **Payload extraction** (Raw layer)
* 🧾 **Optional logging to file**
* 🌐 **Works on Linux, CentOS, and Kali machines**

---

## 📂 Project Structure

```
python-network-sniffer/
│
├── sniffer.py          # Main script for packet capture
├── packet_logs.txt     # Log file (optional)
└── README.md           # Documentation
```

---

## ⚙ Requirements

Install Scapy:

```bash
pip3 install scapy
```

You must run the script with **root privileges**:

```bash
sudo python3 sniffer.py
```

---

## ▶️ How It Works

The script uses Scapy’s `sniff()` function to:

1. Capture real time packets
2. Extract source IP
3. Extract destination IP
4. Identify protocol (TCP, UDP, ICMP)
5. Extract payload
6. Print output in readable format
7. (Optional) Log packets to a file

---

## 📥 Example Output

```
========== PACKET ==========
Time: 2025-12-02 18:00:53
Source IP: 172.67.212.105
Destination IP: 192.168.149.145
Protocol: TCP
Payload: b'HTTP/1.1 301 Moved Permanently...'
```

---

## 🚀 Run the Sniffer

```bash
python3 sniffer.py
```

---

## 📌 Future Improvements

* Colorful CLI output
* Filter packets by port/protocol
* Export packets to CSV or JSON
* Web dashboard for packet visualization
* GUI using PyQt5
* Multi interface support

---

## 🧑‍💻 Author

**Aailah**
Cybersecurity and Automation
GitHub: [https://github.com/Aaila-IO](https://github.com/Aaila-IO)

---
