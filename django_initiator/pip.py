import subprocess
import click


def check_and_update_pip():
    """
    Check the version of pip and update it if a new version is available.

    This function checks if your current version of pip is up-to-date. If a newer version
    is available, it provides an option to update pip. The function checks and updates
    pip in the following steps:

    1. Displays a message indicating that it's checking for pip updates.
    2. Retrieves the current version of pip.
    3. Runs the "pip install --upgrade pip --dry-run" command to simulate a pip update.
    4. If a newer version of pip is found, it offers to update pip and performs the update.
    5. If an internet connection issue occurs during the update check, it notifies the user.
    6. If pip is already up-to-date, it informs the user.

    Returns:
    - True if pip was successfully checked and updated or already up-to-date.
    - False if an error occurred during the check or update process.

    :return: True if pip was successfully checked and updated, False otherwise.
    """
    try:
        # Show a message indicating that a pip update work is going on
        click.secho("Checking if pip is up-to-date...",
                    color=True, fg="yellow")

        # Get the current pip version
        check_pip = subprocess.run(
            ["pip", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        current_pip_version = check_pip.stdout.strip().split()[1]

        # Run the "pip install --upgrade pip" command to check and update pip
        result = subprocess.run(["pip", "install", "--upgrade", "pip", "--dry-run"],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        update_version = ""

        if "Collecting pip" in result.stdout:
            # Extract the last word starting with "pip-"
            update_version = [word for word in result.stdout.strip(
            ).split() if word.startswith("pip-")][-1]
            # Remove "pip-" to show only the version number
            update_version = update_version.replace("pip-", "")
            click.secho(
                f"A pip update is available on your system. Current version: {current_pip_version}, Latest version: {update_version}", color=True, fg="yellow")

            update_pip = click.confirm(
                "Do you want to update pip to the latest version?")
            if update_pip:
                # Show progress message
                click.secho("Updating pip...", color=True, fg="yellow")

                # Run the "pip install --upgrade pip" command to update pip
                pip_updater = subprocess.run(
                    ["python", "-m", "pip", "install", "--upgrade", "pip"])
                if pip_updater.returncode != 0:
                    raise Exception("Failed to update pip.")
                click.secho(
                    "🎊🎊 pip has been updated to the latest version! 🎊🎊", color=True, fg="green")
            else:
                click.secho(
                    "pip is not up-to-date, but it won't be updated as per your choice.", color=True, fg="yellow")
                return True

        elif "Failed to establish a new connection" in result.stderr:
            click.secho(
                "\nAn error occurred while checking for pip updates. Please check your internet connectivity.", color=True, fg="red")

        if "Requirement already satisfied" in result.stdout and update_version == "":
            click.secho("\n🎊🎊 pip is already up-to-date 🎊🎊\n",
                        color=True, fg="green")
            return True
        
        return False
    
    except Exception as e:
        click.secho(
            f"An error occurred while checking and updating pip: {str(e)}", color=True, fg="red")
        return False


if __name__ == "__main__":
    check_and_update_pip()
