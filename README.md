# Django Initiator

**Django Initiator** is a command-line tool that simplifies the process of creating a new Django project. It guides you through setting up your project's directory, creating a virtual environment, installing Django and additional dependencies, and generating a requirements.txt file. This makes it easy to start new Django projects without the hassle of manually setting up the environment.

## Features

- Create a new Django project with ease.
- Set the project directory, project name, and virtual environment name.
- Install Django and additional Python packages.
- Generate a requirements.txt file for your project.
- Utilize an existing .gitignore file for your project.

## Requirements

- Python 3.6+
- pip (Python package manager)

## Installation

1. Clone the repository or download the source code.

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

- On Windows:

  ```
  venv\Scripts\activate
  ```

- On macOS and Linux:

  ```
  source venv/bin/activate
  ```

4. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

5. Run the Django Initiator:
    ```
    python -m django_initiator.cli
    ```

## Usage

Follow the on-screen prompts to create a new Django project with the desired options.

## Planned Improvements

I have exciting plans to enhance Django Initiator in the future:

- **Python Library (Future Enhancement):** Transform Django Initiator into a Python library, enabling users to initiate projects effortlessly from anywhere in their system.

- **Executable File (.exe):** Streamline the process by creating an executable file for direct tool execution.

- **Specify Django apps:** Allow users to customize their project by specifying which Django apps to include during project creation.

- **Git Integration:** Explore adding Git repository initialization and first commit functionality for streamlined version control setup.

- **Database Client Selection:** Offer users the choice of database clients during project setup.


I'm committed to making Django Initiator more powerful and user-friendly. Stay tuned for these exciting updates!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you'd like to improve this project, please fork the repository and create a pull request.

## Contact

If you have questions or need assistance, feel free to reach out to [Ismail Ibrahim](https://twitter.com/ismailsoftdev).

Enjoy using Django Initiator!
