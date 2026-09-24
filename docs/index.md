---
hide:
  - navigation
  - toc
---

# Your inventory, connected

Hubuum brings operational data into a shared model. Describe your resources,
connect them with relationships, and give people and applications consistent
access through an API, browser, terminal, or typed client library.

[Choose your starting point](get-started.md) · [Explore server documentation](https://hubuum.github.io/hubuum/)

## One ecosystem, five ways in

<!-- markdownlint-disable-next-line MD033 -->
<div class="grid cards" markdown>

- **Server**

    The data model, permissions, search, API, and background workflows.
    Start here to deploy Hubuum or understand how it works.

    [Documentation](https://hubuum.github.io/hubuum/) · [Source](https://github.com/hubuum/hubuum) · [Releases](https://github.com/hubuum/hubuum/releases)

- **Web frontend**

    Work with your inventory in a browser. Find configuration, deployment,
    observability, and contributor guides for the web console.

    [Documentation](https://hubuum.github.io/hubuum-frontend/) · [Source](https://github.com/hubuum/hubuum-frontend) · [Releases](https://github.com/hubuum/hubuum-frontend/releases)

- **CLI**

    Explore interactively, run one-shot commands, or build repeatable automation
    with scripts, pipelines, and extensions.

    [Documentation](https://hubuum.github.io/hubuum-cli/) · [Source](https://github.com/hubuum/hubuum-cli) · [Releases](https://github.com/hubuum/hubuum-cli/releases)

- **Rust client**

    Integrate Hubuum into Rust applications with typed resources, queries,
    pagination, and asynchronous or blocking clients.

    [Documentation](https://hubuum.github.io/hubuum-client-rust/) · [Source](https://github.com/hubuum/hubuum-client-rust) · [Releases](https://github.com/hubuum/hubuum-client-rust/releases)

- **Python client**

    Connect Python applications and automation using typed synchronous and
    asynchronous clients, models, and task helpers.

    [Documentation](https://hubuum.github.io/hubuum-client-python/) · [Source](https://github.com/hubuum/hubuum-client-python) · [Releases](https://github.com/hubuum/hubuum-client-python/releases)

</div>

## Model the resources you have

Collections organize access. Classes describe kinds of resources. Objects hold
your data, and relationships connect it. Optional JSON Schema validation,
computed fields, history, and audit events help maintain a useful inventory as
it grows.

Use Hubuum alongside the systems that already own your data. Import their facts,
connect related records, and query the resulting model through one API.

## Choose compatible releases

Each project releases independently. Its documentation opens the latest stable
release, retains older versions at `/vX.Y.Z/`, and labels explicitly selected
`main` documentation as development. Check the client's or frontend's declared
server compatibility before combining versions.

Hubuum is open-source and pre-1.0. Pin the versions you deploy and review release
notes for upgrade requirements. [Get help or contribute](community.md).
