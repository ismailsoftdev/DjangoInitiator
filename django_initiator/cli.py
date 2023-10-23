import os
import subprocess
import click
from django_initiator import pip

def create_django_project():
    click.echo("\n\t ☄️☄️🔥🔥 Welcome to Django Initiator! ☄️☄️🔥🔥\n")
    
    try:
        # Check and update pip
        check_and_update =  pip.check_and_update_pip()
        if check_and_update:
            # Prompt the destination directory
            destination_dir = click.prompt("Enter the destination directory")
            if not os.path.exists(destination_dir):
                raise FileNotFoundError(f"The destination directory '{destination_dir}' does not exist.")
            click.secho(f"The destination directory of '{destination_dir}' will be used to create the Django project.", color=True, fg="green")
            
            # Prompt the project name
            project_name = click.prompt("Enter the project name")
            
            # Create the Django project directory
            project_dir = os.path.join(destination_dir, project_name)
            os.mkdir(project_dir)
            # Sucessfully created the directory
            click.secho(f"The directory '{project_dir}' was created successfully!", color=True, fg="green")
            
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
                click.secho("Sucessfully created the virtual environment and activated it!", color=True, fg="green")
            
            # Install the Django dependencies
            result = subprocess.run([os.path.join(venv_dir, "Scripts", "pip"), "install", "django"], cwd=project_dir)
            if result.returncode != 0:
                raise Exception("Failed to install Django. Check your internet connectivity.")
            
            click.secho("Sucessfully installed Django!", color=True, fg="green")
            
            # Create the project
            django_admin = os.path.join(venv_dir, "Scripts", "django-admin" if os.name == "nt" else "django-admin")
            result = subprocess.run([django_admin, "startproject", project_name, "."], cwd=project_dir)
            if result.returncode != 0:
                raise Exception("Failed to create the Django project. Make sure Django is installed.")
            
            click.secho("Sucessfully created the Django project!", color=True, fg="green")
            
            # Prompt if the user wants to install additional dependencies
            install_dependencies = click.confirm("Do you want to install additional dependencies?")
            
            if install_dependencies:
                # Prompt the dependencies to install and space separate them
                dependencies_str = click.prompt("Enter the dependencies to install (space separated)")
                
                # Split the dependencies string into a list
                dependencies = dependencies_str.split()
                
                for dependency in dependencies:
                    # Install the dependency
                    result = subprocess.run([os.path.join(venv_dir, "Scripts", "pip"), "install", dependency], cwd=project_dir)
                    if result.returncode != 0:
                        click.echo(f"Failed to install dependency: {dependency}")
                    
                click.secho(f"Sucessfully installed additional dependencies of {dependencies}", color=True, fg="green")
            
            # Generate requirements.txt file from the virtual environment
            requirements_file = os.path.join(project_dir, "requirements.txt")
            with open(requirements_file, "w") as file:
                subprocess.run([os.path.join(venv_dir, "Scripts", "pip"), "freeze"], stdout=file, cwd=project_dir)
            
            click.secho("Sucessfully generated requirements.txt file!", color=True, fg="green")
            
            # Create the .gitignore file in the project directory
            with open(os.path.join(project_dir, ".gitignore"), "w") as gitignore_file:
                # Get the .gitignore file from the current working directory
                gitignore_path = os.path.join(original_dir, ".gitignore")
                with open(gitignore_path, "r") as gitignore:
                    gitignore_file.write(gitignore.read())
            
            click.secho("Sucessfully created .gitignore file!", color=True, fg="green")
            
            # Print the success message
            click.secho("🙌🙌🙌🙌 Django project created successfully! 🎇🎇🎇🎇🎈🎈", color=True, fg="green")
    
    except FileNotFoundError as e:
        click.secho(f"Error: {str(e)}", color=True, fg="red")
    except Exception as e:
        click.secho(f"An error occurred: {str(e)}", color=True, fg="red")

if __name__ == "__main__":
    create_django_project()
