# Hubuum ecosystem website

Source for <https://hubuum.github.io/>, the entry point for Hubuum Server,
Frontend, CLI, and the Rust and Python clients.

This site introduces the ecosystem and links to each project's independently
versioned documentation. It shares the theme and publishing tools from
[hubuum/.github](https://github.com/hubuum/.github), pinned in
`.github/docs-tools.env` and the documentation workflow.

## Homepage and shared styling

The production Orbit homepage is `overrides/home.html`, with its layout,
progressive enhancements, and SVG illustrations in `docs/assets/landing/`.
The original [design studies](design/README.md) remain outside the published site.

`docs/assets/stylesheets/hubuum.css` is the canonical theme for all six sites,
including retained release editions. Each page loads the same unversioned URL:
<https://hubuum.github.io/assets/stylesheets/hubuum.css>. Change the palette tokens
or shared documentation rules here and merge to `main`; other repositories need
no commit, rebuild, or release. GitHub Pages' normal browser cache lifetime applies.
Keep styles compatible with older Zensical output and check light/dark modes,
tables, search, and mobile layouts before publishing. Revert the CSS commit here
to roll back a theme change.

The root homepage uses the same palette tokens. Its layout remains separate from
the documentation shell, so changes to landing-page composition do not affect
reference pages. Navigation uses normal page loads between these two layouts.

## Preview

Requirements: Python 3.11+, Git, Bash, and Docker.

```sh
bash scripts/docs.sh build
bash scripts/docs.sh serve
```

Open `http://127.0.0.1:8000/`. Rebuild after editing `docs/`, `overrides/`, or `zensical.toml`.
Generated files stay in `target/`. Every page must appear in the navigation;
strict builds check links and anchors.

## Publish

Pull requests build a downloadable preview. Merging to `main` publishes through
GitHub Actions Pages. The shared setup script enables the repository's Pages
settings. This editorial landing page is unversioned; product sites default to
their latest release and provide their own version selectors.

Update the tooling and reusable-workflow pins together after reviewing a build
or publishing change; stylesheet-only changes do not need new tooling pins. Keep detailed API, deployment, language, and command reference in the
repository that owns it. Links to product documentation use stable entry URLs,
so this page does not need editing for every product release.
