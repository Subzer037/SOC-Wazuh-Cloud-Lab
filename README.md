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
