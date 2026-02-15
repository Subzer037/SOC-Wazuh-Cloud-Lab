## CI/CD Automation (DevSecOps)
A GitHub Actions pipeline was implemented to automate security log analysis. 
On every code push, a Python script analyzes Wazuh alert logs and detects high severity events automatically.

## Attacks Simulated
- Nmap port scanning
- Hydra brute force attack

## Logs Monitored
- Authentication logs
- Network activity logs
- Security alerts

## Results
The system successfully detected brute force and scanning attacks and generated alerts in the Wazuh dashboard.

---

## 🔴 Issues Faced (Challenges)

During the setup and testing of the Wazuh security monitoring lab, several technical challenges were encountered:

1. **SSH Service Not Running on Ubuntu**
   - Initially, the Ubuntu VM (Wazuh Agent) did not have the SSH service running.
   - All connection attempts from Kali Linux failed with “Connection refused” errors.
   - This prevented both SSH login and Hydra attack simulation.

2. **User Account Not Created**
   - The testuser account required for SSH authentication testing did not exist initially.
   - Without a valid user, authentication attempts could not be performed.

3. **Network and Connectivity Confusion**
   - Incorrect IP addresses (198.x.x.x instead of 192.168.x.x) caused failed connections.
   - Confusion existed around firewall rules, SSH configuration, and VM networking.

4. **Hydra Connection Errors**
   - Hydra with large wordlists and default threads caused:
     > "all children were disabled due to too many connection errors"
   - This occurred due to SSH rate-limiting and connection drops.

5. **Possible Blocking by Security Controls**
   - SSH limits and security tools such as fail2ban interfered with brute-force attempts.
   - Hydra speed had to be reduced and logs examined.

6. **Understanding Where to Monitor Logs in Wazuh**
   - Initially unclear where to view SSH logs in the Wazuh Dashboard.
   - Learned to use Threat Hunting and Security Events sections.

---

## 🟢 Achievements

1. **Successful User Creation**
   - Created and verified `testuser` on Ubuntu.
   - Confirmed local and remote SSH login.

2. **SSH Service Enabled and Verified**
   - Installed and enabled OpenSSH server.
   - Verified SSH connectivity from Kali.

3. **Attack Simulation Environment Built**
   - Kali Linux as attacker.
   - Ubuntu (Wazuh Agent) as victim.
   - Used Hydra and manual SSH attempts.

4. **Log Generation on Ubuntu**
   - SSH failures recorded in:
     ```
     /var/log/auth.log
     ```

5. **Integration with Wazuh Monitoring**
   - Ubuntu agent successfully connected to Wazuh Manager.
   - Logs forwarded to Wazuh Dashboard.

6. **Visibility of Security Events in Wazuh**
   - Alerts visible in:
     - Threat Hunting
     - Security Events
   - Mapped to MITRE ATT&CK technique T1110 (Brute Force).

7. **Practical Cybersecurity Learning Outcome**
   - Hands-on experience in:
     - Linux user management
     - SSH configuration
     - Network troubleshooting
     - Attack simulation
     - SIEM log monitoring

---

## 🧠 Overall Outcome

This project demonstrated the complete lifecycle of a SOC lab:

**Setup → Troubleshooting → Attack Simulation → Log Monitoring → Analysis**

Each error improved understanding of:
- Service communication
- Attack detection
- Security alert visualization in Wazuh

---

## 🏁 Final Conclusion

**Issues faced:**  
SSH not running, missing user account, incorrect IP usage, Hydra connection errors, and difficulty locating logs in the Wazuh Dashboard.

**Achievements:**  
A fully functional Wazuh monitoring environment with a connected Ubuntu agent, successful SSH attack simulation from Kali, and real-time visualization of security alerts in the Wazuh Dashboard.
