import os
import subprocess
import argparse
from typing import Dict


def load_env_vars() -> Dict[str, str]:
    """
    Load environment variables from a .envrc file.

    Returns:
        Dict[str, str]: A dictionary of environment variables loaded from .envrc.
    """
    env_vars = {}
    envrc_path = ".envrc"
    if os.path.exists(envrc_path):
        with open(envrc_path, "r") as file:
            for line in file:
                if line.startswith("export"):
                    key_value = line.split("export")[-1].strip()
                    key, value = key_value.split("=", 1)
                    env_vars[key] = value.strip('"')
    return env_vars


def build_and_run(image_name: str, container_name: str, port: str) -> None:
    """
    Build and run the Docker container.

    Args:
        image_name (str): Name of the Docker image to be built.
        container_name (str): Name of the Docker container to be created.
        port (str): Port to expose the application.
    """

    env_vars = load_env_vars()

    print("Building the Docker image...")
    build_command = ["docker", "build", "-t", image_name, "."]
    subprocess.run(build_command, check=True)

    print("Stopping any running container...")
    stop_command = ["docker", "rm", "-f", container_name]
    subprocess.run(stop_command, stderr=subprocess.DEVNULL, check=False)

    docker_env_flags = []
    for key, value in env_vars.items():
        docker_env_flags.extend(["-e", f"{key}={value}"])

    print("Running the Docker container...")
    run_command = [
        "docker",
        "run",
        "--name",
        container_name,
        "-d",
        "-p",
        f"{port}:{port}",
        "-e",
        f"APP_PORT={port}",
        *docker_env_flags,
        image_name,
    ]
    subprocess.run(run_command, check=True)

    url = f"http://localhost:{port}/process/playground/"

    clickable_link = f"\033]8;;{url}\033\\{url}\033]8;;\033\\"
    print(f"\nThe application is running on: {clickable_link}\n")


def destroy_all(image_name: str, container_name: str) -> None:
    """
    Destroy both the container and the Docker image.

    Args:
        image_name (str): Name of the Docker image to be removed.
        container_name (str): Name of the Docker container to be stopped and removed.
    """
    print(f"Stopping and removing container '{container_name}'...")
    stop_command = ["docker", "rm", "-f", container_name]
    subprocess.run(stop_command, check=False)

    print(f"Removing image '{image_name}'...")
    remove_image_command = ["docker", "rmi", "-f", image_name]
    subprocess.run(remove_image_command, check=False)

    print("All Docker resources have been cleaned up.")


def kill_container(container_name: str) -> None:
    """
    Stop and remove a running Docker container.

    Args:
        container_name (str): Name of the Docker container to be stopped and removed.
    """
    print(f"Stopping and removing container '{container_name}'...")
    stop_command = ["docker", "rm", "-f", container_name]
    subprocess.run(stop_command, stderr=subprocess.DEVNULL, check=False)

    print(f"Container '{container_name}' has been stopped and removed.")


def main() -> None:
    """
    Main entry point for the script to manage the Dockerized ResumeAPI application.

    Command-line Arguments:
        --destroy-all: Remove both the container and the image.
        --kill-container: Stop and remove the container only.
    """
    parser = argparse.ArgumentParser(
        description="Manage the Dockerized ResumeAPI application."
    )
    parser.add_argument(
        "--destroy-all",
        action="store_true",
        help="Remove both the container and the image.",
    )
    parser.add_argument(
        "--kill-container",
        action="store_true",
        help="Stop and remove the container only.",
    )
    args = parser.parse_args()

    port = os.getenv("APP_PORT", "8080")
    image_name = "resumeapi_image"
    container_name = "resumeapi_container"

    if args.destroy_all:
        destroy_all(image_name, container_name)
    elif args.kill_container:
        kill_container(container_name)
    else:
        build_and_run(image_name, container_name, port)


if __name__ == "__main__":
    main()
