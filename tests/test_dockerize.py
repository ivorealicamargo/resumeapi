import os
from unittest import mock
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from resumeapi.dockerize import (
    load_env_vars,
    build_and_run,
    destroy_all,
    kill_container,
    main,
)


@mock.patch("resumeapi.dockerize.subprocess.run")
@mock.patch("resumeapi.dockerize.os.path.exists", return_value=True)
def test_load_env_vars(mock_exists, mock_run):
    """Test loading environment variables from a .envrc file."""
    with mock.patch("builtins.open", mock.mock_open(read_data='export TEST_KEY="value"\n')):
        env_vars = load_env_vars()
    assert env_vars == {"TEST_KEY": "value"}


@mock.patch("resumeapi.dockerize.subprocess.run")
@mock.patch("resumeapi.dockerize.load_env_vars", return_value={"TEST_KEY": "value"})
def test_build_and_run(mock_load_env_vars, mock_run):
    """Test building and running the Docker container."""
    build_and_run("test_image", "test_container", "8080", "/local/dir", "/container/dir")
    assert mock_run.call_count == 3  # build, stop, and run


@mock.patch("resumeapi.dockerize.subprocess.run")
def test_destroy_all(mock_run):
    """Test destroying all Docker resources."""
    destroy_all("test_image", "test_container")
    assert mock_run.call_count == 2  # rm and rmi commands


@mock.patch("resumeapi.dockerize.subprocess.run")
def test_kill_container(mock_run):
    """Test stopping and removing a Docker container."""
    kill_container("test_container")
    assert mock_run.call_count == 1  # rm command


@mock.patch("resumeapi.dockerize.build_and_run")
@mock.patch("resumeapi.dockerize.destroy_all")
@mock.patch("resumeapi.dockerize.kill_container")
@mock.patch("resumeapi.dockerize.argparse.ArgumentParser.parse_args")
def test_main(mock_parse_args, mock_kill_container, mock_destroy_all, mock_build_and_run):
    """Test the main function with different CLI arguments."""
    # Test --destroy-all
    mock_parse_args.return_value = mock.Mock(destroy_all=True, kill_container=False)
    main()
    mock_destroy_all.assert_called_once()
    mock_kill_container.assert_not_called()
    mock_build_and_run.assert_not_called()

    # Test --kill-container
    mock_parse_args.return_value = mock.Mock(destroy_all=False, kill_container=True)
    main()
    mock_kill_container.assert_called_once()
    mock_destroy_all.assert_called_once()  # Confirm it was called only in the previous case
    mock_build_and_run.assert_not_called()

    # Test default (build_and_run)
    mock_parse_args.return_value = mock.Mock(destroy_all=False, kill_container=False)
    main()
    mock_build_and_run.assert_called_once()
