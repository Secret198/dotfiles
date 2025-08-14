# winget install -id Microsoft.VisualStudioCode --silent --accept-package-agreements --accept-source-agreements
# winget install -id 9N0DX20HK701 --silent --accept-package-agreements --accept-source-agreements #This is the terminal
# winget install -id Starship.Starship --silent --accept-package-agreements --accept-source-agreements

$userName = "Yeah"

$homePath = "C:\Users\"+$userName
$powerShellPath = $homePath + "\Documents\WindowsPowerShell"

New-Item -itemtype symboliclink -path $powerShellPath -name Microsoft.PowerShell_profile.ps1 -value Microsoft.PowerShell_profile.ps1

New-Item -itemtype symboliclink -path $homePath -name .gitconfig -value .gitconfig
New-Item -itemtype symboliclink -path $homePath -name .vscode -value .vscode
New-Item -itemtype symboliclink -path $homePath -name .glzr -value .glzr