"""Helper functions"""

import subprocess


def run(command):
    """
    Execute shell command
    :param command: string, required
    :return: string
    """

    output = subprocess.run(command, capture_output=True, text=True)

    if output.returncode != 0:  # An error occurred
        return 'error: ' + output.stderr
    else:
        return output.stdout
