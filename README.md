# Hubuum ecosystem website

Source for <https://hubuum.github.io/>, the entry point for Hubuum Server,
Frontend, CLI, and the Rust and Python clients.

This site introduces the ecosystem and links to each project's independently
versioned documentation. It shares the theme and publishing tools from
[hubuum/.github](https://github.com/hubuum/.github), pinned in
`.github/docs-tools.env` and the documentation workflow.

## Preview

Requirements: Python 3.11+, Git, Bash, and Docker.

```sh
bash scripts/docs.sh build
bash scripts/docs.sh serve
```

Open `http://127.0.0.1:8000/`. Rebuild after editing `docs/` or `zensical.toml`.
Generated files stay in `target/`. Every page must appear in the navigation;
strict builds check links and anchors.

## Publish

Pull requests build a downloadable preview. Merging to `main` publishes through
GitHub Actions Pages. The shared setup script enables the repository's Pages
settings. This editorial landing page is unversioned; product sites default to
their latest release and provide their own version selectors.

Update the tooling and reusable-workflow pins together after reviewing a shared
change. Keep detailed API, deployment, language, and command reference in the
repository that owns it. Links to product documentation use stable entry URLs,
so this page does not need editing for every product release.
