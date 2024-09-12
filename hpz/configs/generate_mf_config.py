import getpass
import platform
import os
from pathlib import Path



def main():
    if platform.node()[:7] == "spartan":
        # Prompt user for input
        print("Enter your UoM credentials you use for Mediaflux")
        username = input("Enter your username: ")
        print("ATTENTION: Password will be stored as plain text. If left empty it has to be entered every time when copying files from Mediaflux")
        password = getpass.getpass("Enter your password: ")

        # Config file adapted from
        # https://gitlab.unimelb.edu.au/resplat-mediaflux/unimelb-mf-clients/-/blob/master/src/main/config/samples/mflux.cfg
        config_content = f"""
# This is a sample configuration file contains Mediaflux server connection details and user credentials for authentication.
# 
# To install this configuration file:
#      1) Edit this file according to your Mediaflux server details and user credentials;
#      2) Move this file to $HOME/.Arcitecta/mflux.cfg if on Unix platform, or %userprofile%\.Arcitecta\mflux.cfg if on Windows platform

# Mediaflux server host
host=mediaflux.researchsoftware.unimelb.edu.au
# Mediaflux server port
port=443
# Mediaflux server transport protocol, can be http, https or tcpip
transport=https
# User's Domain
domain=unimelb
# Secure identity token, if specified, no user password is needed.
# Contact RCS to request a token
# See: https://rcs-knowledge-hub.atlassian.net/wiki/spaces/KB/pages/5474302/Configuration+File#ConfigurationFile-Authenticatingwithasecureidentitytoken
#token=XXXXXXXXXXXXXXXXXX
# User's login
user={username}
# User's password
"""
        # Comment out password field if it was left empty
        if password == "":
            config_content += f"""#password="""
        else:
            config_content += f"""password={password}"""

        # Write the config file in the user's home folder
        mflux_cfg_path = os.path.expanduser('~/.Arcitecta/mflux2.cfg')
        with open(mflux_cfg_path, 'w') as config_file:
            config_file.write(config_content.strip())

        # Add the config file as environment variable to the user's bashrc
        env_var = 'MFLUX_CFG'
        shell_config_file = os.path.expanduser('~/.bashrc')

        # Read the current content of the shell configuration file
        with open(shell_config_file, 'r') as file:
            lines = file.readlines()

        # Check if the environment variable is already set
        var_set = False
        for i, line in enumerate(lines):
            if line.startswith(f'export {env_var}='):
                # Update the value if the variable is already set
                lines[i] = f'export {env_var}="{mflux_cfg_path}"\n'
                var_set = True
                break

        # Add the variable to the end if it is not set
        if not var_set:
            lines.append('# Set MFLUX_CFG environment variable')
            lines.append(f'export {env_var}="{mflux_cfg_path}"\n')

        # Write the updated content back to the shell configuration file
        with open(shell_config_file, 'w') as file:
            file.writelines(lines)

        print("To apply the changes, run: source ~/.bashrc")


if __name__ == "__main__":
    main()
