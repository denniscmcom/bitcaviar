"""Helper functions"""

import subprocess


def __run(command):
    """
    Execute shell command
    :param command: list, required
    :return: string
    """

    output = subprocess.run(command, capture_output=True, text=True)

    if output.returncode != 0:  # An error occurred
        raise ValueError(output.stderr)
    else:
        return output.stdout
