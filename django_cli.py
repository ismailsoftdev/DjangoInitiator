import os
import subprocess
import click

@click.command()
def create_django_project():
    # Prompt the destination directory
    destination_dir = click.prompt("Enter the destination directory")
    
    # Prompt the project name
    project_name = click.prompt("Enter the project name")
    
    # Create the Django project directory
    project_dir = os.path.join(destination_dir, project_name)
    os.mkdir(project_dir)
    
    # Save the current working directory
    original_dir = os.getcwd()
    
    # Change to the project directory
    os.chdir(project_dir)
    
    # Prompt the venv directory
    venv_dir = click.prompt("Enter the venv directory:", default="venv")
    
    # Create the virtual environment
    subprocess.run(["python", "-m", "venv", venv_dir], cwd=project_dir)
    
    # Activate the virtual environment in the project directory
    activate_script = os.path.join(venv_dir, "Scripts", "activate")
    
    # On Windows, use "cmd.exe" to activate the virtual environment
    if os.name == "nt":
        subprocess.run([activate_script], shell=True, cwd=project_dir)
    
    # Install the Django dependencies
    subprocess.run([os.path.join(venv_dir, "Scripts", "pip"), "install", "django"], cwd=project_dir)
    
    # Create the project
    subprocess.run(["django-admin", "startproject", project_name, "."], cwd=project_dir)
    
    # Prompt if the user wants to install additional dependencies
    install_dependencies = click.confirm("Do you want to install additional dependencies?")
    
    if install_dependencies:
        # Prompt the dependencies to install and comma separate them
        dependencies_str = click.prompt("Enter the dependencies to install (space separated)")
        
        # Split the dependencies string into a list
        dependencies = dependencies_str.split()
        
        for dependency in dependencies:
            # Install the dependency
            subprocess.run([os.path.join(venv_dir, "Scripts", "pip"), "install", dependency], cwd=project_dir)
    
    # Generate requirements.txt file from the virtual environment
    requirements_file = os.path.join(project_dir, "requirements.txt")
    with open(requirements_file, "w") as file:
        subprocess.run([os.path.join(venv_dir, "Scripts", "pip"), "freeze"], stdout=file, cwd=project_dir)

    
    # Create the .gitignore file in the project directory
    with open(os.path.join(project_dir, ".gitignore"), "w") as gitignore_file:
        # Get the .gitignore file from the current working directory
        gitignore_path = os.path.join(original_dir, ".gitignore")
        with open(gitignore_path, "r") as gitignore:
            gitignore_file.write(gitignore.read())

    # Print the success message
    click.secho("🙌🙌🙌🙌 Django project created successfully! 🎇🎇🎇🎇🎈🎈", color=True, fg="green")

if __name__ == "__main__":
    create_django_project()