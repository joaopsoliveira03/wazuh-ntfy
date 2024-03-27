# wazuh-ntfy
NTFY integration on Wazuh

Based on:
- https://wazuh.com/blog/how-to-integrate-external-software-using-integrator/
- https://docs.ntfy.sh/publish/#message-title

## Installation
1. Create the custom-ntfy file for Wazuh Manager: `/var/ossec/integrations/custom-ntfy`
2. Give Permissions and Change the Owner of the file: `chmod 755 custom-ntfy && chown root:wazuh custom-ntfy`
3. Add a integration entry in the `/var/ossec/etc/ossec.conf` file:
```
<integration>
  <name>custom-ntfy</name>
  <hook_url>https://ntfy.sh/alert</hook_url>
  <alert_format>json</alert_format>
</integration>
```
4. Restart the Wazuh Manager

Note: I recommend you self-hosting your own NTFY server and configure the rate limiting or perhaps limit this integration for specific rule levels.