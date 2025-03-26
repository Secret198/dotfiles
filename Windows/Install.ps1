# winget install -id Microsoft.VisualStudioCode --silent --accept-package-agreements --accept-source-agreements
# winget install -id 9N0DX20HK701 --silent --accept-package-agreements --accept-source-agreements #This is the terminal
# winget install -id Starship.Starship --silent --accept-package-agreements --accept-source-agreements

New-Item -itemtype symboliclink -path C:\Users\User\Documents\WindowsPowerShell -name Microsoft.PowerShell_profile.ps1 -value Microsoft.PowerShell_profile.ps1
New-Item -itemtype symboliclink -path C:\Users\User -name .gitconfig -value .gitconfig
New-Item -itemtype symboliclink -path C:\Users\User -name .vscode -value .vscode
New-Item -itemtype symboliclink -path C:\Users\User -name .glzr -value .glzr
New-Item -itemtype symboliclink -path C:\Users\User\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe -name LocalState -value LocalState
