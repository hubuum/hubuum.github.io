# Choose your starting point

| Your goal | Start here | Then explore |
| --- | --- | --- |
| Understand whether Hubuum fits your organization | [Server documentation](https://hubuum.github.io/hubuum/) | The data model, permissions, and integration contracts |
| Evaluate a complete installation | [Server deployment guides](https://hubuum.github.io/hubuum/) | [Frontend deployment](https://hubuum.github.io/hubuum-frontend/) |
| Run and recover a service | [Server administration](https://hubuum.github.io/hubuum/) | Monitoring, identity, backups, and upgrades |
| Work from a terminal | [CLI installation and guides](https://hubuum.github.io/hubuum-cli/) | Search, output pipelines, extensions, and examples |
| Build a Rust integration | [Rust client](https://hubuum.github.io/hubuum-client-rust/) | Client setup, querying, and generated API reference |
| Build Python automation | [Python client](https://hubuum.github.io/hubuum-client-python/) | Synchronous and asynchronous APIs, credentials, and tasks |
| Contribute a change | [Community and contributing](community.md) | The contributor guide in the affected repository |

## Start with a server

The frontend, CLI, and libraries connect to a Hubuum server. Production server
installations use PostgreSQL. Choose a deployment method from the server guides,
configure an administrator and access permissions, then connect the interface
that suits your workflow.

The frontend is an application with its own server and session storage.
GitHub Pages hosts these documentation sites; deploy the application using the
frontend's deployment instructions.

## Keep versions explicit

A client version does not imply the same server version. Read the compatibility
record for the release you deploy, including any credential-approval or backup
format requirements. Share an exact `/vX.Y.Z/` documentation URL when discussing
an older release; use `main` only when working on unreleased behavior.
