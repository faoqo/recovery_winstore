import subprocess

proc = subprocess.Popen(['powershell', 'cd C:\PS\Store'])
proc.wait()
proc = subprocess.Popen(['powershell', 'Get-Childitem $Path -filter *.appx| %{Add-AppxPackage -Path $_.FullName}'])
proc.wait()
proc = subprocess.Popen(['powershell', 'Get-Childitem $Path -filter *.appxbundle | %{Add-AppxPackage -Path $_.FullName}'])
proc.wait()