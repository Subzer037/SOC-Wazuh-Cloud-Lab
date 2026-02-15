🔐 SOC Wazuh Cloud Lab – Challenges, Achievements & Outcomes
📌 Project Overview

This project demonstrates the design and implementation of a Security Operations Center (SOC) monitoring environment using Wazuh SIEM, Ubuntu Linux, and Kali Linux. The lab simulates real-world attack scenarios and analyzes system logs to detect and visualize security threats.

The environment consists of:

Wazuh Manager deployed on Ubuntu (Google Cloud)

Wazuh Agent deployed on Ubuntu (VMware)

Kali Linux as the attacker machine

Attack simulation using Nmap and Hydra

Log monitoring and alert analysis via Wazuh Dashboard

⚠️ Challenges Encountered

During the setup and testing phase, several technical challenges were faced:

1. SSH Service Misconfiguration

The Ubuntu Wazuh Agent initially did not have the SSH service running.

All SSH connection attempts returned “Connection refused” errors.

This blocked both legitimate login and attack simulation activities.

2. Missing User Account

The required test account (testuser) for SSH authentication testing was not present initially.

Without a valid user, authentication-based attacks could not be simulated.

3. Network Connectivity Issues

Incorrect IP address usage (e.g., typing 198.x.x.x instead of 192.168.x.x) caused repeated connection failures.

Required troubleshooting of VM networking and connectivity between Kali and Ubuntu systems.

4. Hydra Brute-Force Errors

Running Hydra with large wordlists and default thread settings resulted in the error:

“all children were disabled due to too many connection errors”

This occurred due to SSH rate-limiting and connection drops from excessive parallel attempts.

5. Security Control Interference

SSH connection limits and potential security tools (e.g., fail2ban) interfered with brute-force attempts.

Required reducing Hydra speed and validating events through system logs.

6. Log Visibility in Wazuh Dashboard

Initially unclear where authentication and attack logs were visible within Wazuh.

Required learning how to navigate:

Threat Hunting

Security Events

MITRE ATT&CK mapping views

✅ Achievements

Despite the challenges, the project successfully achieved the following objectives:

1. User and Service Configuration

Created and validated the testuser account on Ubuntu.

Installed, started, and enabled the OpenSSH service.

Verified both local and remote SSH connectivity from Kali Linux.

2. Attack Simulation Environment

Built a controlled attack lab using:

Kali Linux (attacker)

Ubuntu with Wazuh Agent (victim)

Generated security events using:

Manual SSH login failures

Hydra brute-force attempts

Nmap scanning

3. Log Generation and Collection

SSH authentication failures were successfully recorded in:

/var/log/auth.log


Logs were forwarded from the Ubuntu agent to the Wazuh Manager.

4. SIEM Integration and Monitoring

Ubuntu agent was correctly registered with the Wazuh Manager.

Security events appeared in the Wazuh Dashboard in real time.

5. Alert Detection and MITRE Mapping

Wazuh generated alerts mapped to:

MITRE ATT&CK Technique T1110 – Brute Force

Events were visible under:

Threat Hunting

Security Events

6. Practical Security Skills Gained

Hands-on experience was gained in:

Linux user and service management

SSH configuration and troubleshooting

Network debugging

Attack simulation techniques

SIEM log analysis and alert investigation

🧠 Overall Outcome

This project demonstrates the complete SOC workflow:

Environment Setup → Troubleshooting → Attack Simulation → Log Collection → Threat Detection → Analysis

Each technical issue strengthened understanding of:

Service communication between systems

How attacks are detected at the log level

How Wazuh visualizes and correlates security events

🏁 Final Conclusion

Key Challenges:

SSH misconfiguration

Missing user accounts

Network addressing errors

Hydra connection limits

Difficulty locating security logs in the dashboard

Key Achievements:

A fully operational Wazuh monitoring lab

Successful SSH brute-force attack simulation from Kali Linux

Real-time alert generation and visualization in Wazuh Dashboard

Detection of brute-force activity mapped to MITRE ATT&CK techniques

This project validates the ability to design, deploy, troubleshoot, and operate a basic SOC monitoring environment using open-source security tools.
