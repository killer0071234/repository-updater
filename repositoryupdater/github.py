"""
GitHub module.

This module extends the main PyGitHub class in order to add some extra
functionality.
"""

from git import Repo
from github import Github as PyGitHub
from github import Repository


class GitHub(PyGitHub):
    """Object for communicating with GitHub and cloning repositories."""

    token: str

    def __init__(self, login_or_token: str | None = None) -> None:
        """Initialize a new GitHub object."""
        super().__init__(
            login_or_token=login_or_token,
        )
        self.token = login_or_token

    def clone(self, repository: Repository, destination: str) -> Repo:
        """Clone a GitHub repository and return a Git object."""
        environ = {
            "GIT_ASKPASS": "repository-updater-git-askpass",
            "GIT_USERNAME": self.token,
            "GIT_PASSWORD": "",
        }

        repo = Repo.clone_from(repository.clone_url, destination, None, environ)

        user = self.get_user()
        email = user.email or f"{user.id}+{user.login}@users.noreply.github.com"
        with repo.config_writer() as config:
            config.set_value("user", "email", email)
            config.set_value("user", "name", user.name or user.login)
            config.set_value("commit", "gpgsign", "false")

        return repo
