import os  # For working with environment variables
from pathlib import Path  # For safe file path handling

def load_env(file_path: str = ".env") -> None:
   
    env_path = Path(file_path)

    # Check if the .env file exists
    if not env_path.exists():
        print(f" No .env file found at: {env_path.resolve()}")
        return

    # Read and parse the file line by line
    with env_path.open("r") as file:
        for line in file:
            line = line.strip()  # Remove extra whitespace
            if not line or line.startswith("#"):
                continue  # Skip empty lines or comments

            # Split into key and value
            if "=" in line:
                key, value = line.split("=", 1)
                key, value = key.strip(), value.strip().strip('"').strip("'")

                # Set the variable in the environment
                os.environ[key] = value

    print("Environment variables successfully loaded.")


if __name__ == "__main__":
    # Example usage: load variables from .env file
    load_env()

    # Access environment variables after loading
    db_user = os.getenv("DB_USER", "default_user")
    print("Database user is:", db_user)
