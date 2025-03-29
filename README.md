# Dotfiles

Config files for:
- Windows
    - GlazeWM
    - VsCode
    - Git

## Installation
Clone the repository
```sh
git clone git@github.com:Secret198/dotfiles.git .dotfiles
```

```sh
git clone https://github.com/Secret198/dotfiles.git .dotfiles
```

### Windows
Run the Install.ps1 script from powershell
```sh
.\Install.ps1
```

## Expanding the scripts with new files
Put the script config file in the corresponding folder

### Windows
Put a new command at the end of the **Install.ps1** script
```powershell
New-Item -itemtype symboliclink -path <path_for_the_new_link> -name <name_of_the_new_link> -value <path_to_originial_file>
```
