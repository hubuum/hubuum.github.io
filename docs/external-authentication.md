# External authentication

Hubuum Server handles sign-in with an external identity provider. The web frontend,
CLI and SDKs discover the methods the server offers. You authenticate in the browser,
approve the requesting client in Hubuum, and return to that client with a Hubuum
session. The server handles callbacks and keeps the provider credentials. Local
passwords, LDAP and personal access tokens (PATs) remain available.

This guide covers the Project #6 candidates qualified on 21 November 2026. The
release to `main` and stable packages requires separate review. [Qualification
record][acceptance] · [Release tracking][promotion]

## Sign in or integrate a client

| Task | Product guide |
| --- | --- |
| Sign in on the web and return to your workspace | [Browser login and approvals][browser] |
| Sign in from the CLI, including a terminal on another machine | [CLI browser and remote-device login][cli-login] |
| Integrate a Rust client | [Async and blocking interactions, session persistence and approval][rust-guide] |
| Integrate a Python client | [Sync and async interactions, session persistence and approval][python-guide] |

## Choose a provider

| Provider | Qualified behavior |
| --- | --- |
| Keycloak OIDC | Hubuum validates the realm issuer and subject. Group claims can come from the signed ID token or subject-matched UserInfo. Keycloak can supply fresh authentication for a privileged operation. [Keycloak setup][keycloak] |
| GitHub.com OAuth App | Public identity is sufficient for CLI and web sign-in. Hubuum uses the stable numeric GitHub ID and local memberships. GitHub OAuth cannot supply fresh credential approval. Hubuum invalidates its own session on logout. Upstream token revocation is best effort. [GitHub setup and limits][oauth] |
| Generic OAuth | The administrator defines how to read a stable subject from one authenticated JSON user endpoint. Qualification covered a synthetic provider. Check a specific provider’s endpoint, subject type and capabilities before adoption. [JSON profile requirements][json-profile] |
| Brokered identity | If a user signs in to Keycloak through an upstream provider, Hubuum trusts the Keycloak realm. Direct Google and Apple integrations have separate qualification work. [Google tracking][google] · [Apple tracking][apple] |

## Configure access and recover service

Keep a password-capable local recovery administrator. To add or change a provider
at runtime, create a candidate and supply its secret through the write-only field
or a deployment-managed secret reference. A connectivity check alone cannot
verify a user's identity or groups. Complete an actual test sign-in to preview
the proposed result. The preview leaves users, memberships and sessions untouched.
The local administrator then uses the verification receipt and a fresh approval
to activate that exact revision. Replicas apply the change without a restart,
subject to deployment locks. [Server setup][candidate] · [Web administration][web-admin] · [CLI administration][cli-admin]

Admission controls who may sign in. Access comes from Hubuum group memberships.
Administrators can grant local memberships manually. With synchronization enabled,
explicit mappings turn complete provider claims into groups scoped to that provider.
When a claim disappears from a complete set, Hubuum removes only that provider's grant.
Manual grants and grants from other sources survive. Group reads show effective
membership and omit the per-source history. Direct mappings into existing local
groups and automatic account linking by email are deferred. [Identity and membership policy][membership]

A required claim that is missing or incomplete invalidates cached provider authority.
During a temporary outage, an existing session can use its last verified membership
only within the configured maximum stale interval. Rotating a Hubuum token does
not extend that interval. A Treetop outage can also block privileged access and new
logins. Restore connectivity or follow the offline local-administrator recovery
procedure. [Freshness policy][freshness] · [Offline recovery][recovery]

## Qualified versions and upgrade order

Use the commit links to identify the tested builds. The manifest versions also
appear in release histories and do not by themselves identify an authentication
candidate. The automated matrix covered 255 checks across 16 product and provider
combinations. The subsequent live GitHub test covered the CLI and web frontend
against server PR #608. [Automated matrix][matrix] · [Live sign-in evidence][acceptance]

| Component | Manifest version | Qualified project source |
| --- | --- | --- |
| Server | 0.0.22 | [`bb5f3765`][server-source] (live GitHub), [`8e6e8344`][matrix-server] (automated matrix) |
| Rust client | 0.21.0 | [`53649969`][rust-source] |
| Python client | 0.0.15 | [`7d76b19a`][python-source] |
| CLI | 0.0.23 | [`ffb4e6f2`][cli-source] |
| Web frontend | 0.0.25 | [`760665ad`][web-source] |

1. Upgrade the server first. Stop all API and worker replicas, back up the database
   and configuration, apply the migrations and role grants, then restart matching
   binaries and begin fresh interactions. Move legacy OAuth bindings with missing
   or conflicting header history to a new scope. A downgrade requires the pre-upgrade
   snapshot and matching configuration. [Server upgrade notes][upgrade]
2. Upgrade the Rust and Python clients against the accepted server contract.
   External storage adapter authors must also upgrade the ten storage SDK crates
   together to 0.11.0. [Storage adapter upgrade][storage]
3. Upgrade the CLI and frontend. Stable CLI packaging must pin the released Rust
   client. Use the compatibility matrix published with the reviewed release when
   selecting stable packages. [Promotion sequence][promotion]

[acceptance]: https://github.com/hubuum/hubuum/issues/581#issuecomment-7063706082
[promotion]: https://github.com/hubuum/hubuum/issues/582
[browser]: https://github.com/hubuum/hubuum-frontend/blob/760665ada7e5a7e25f2538fcb5e1df454969a6ba/docs/session-security.md#project-login-and-approval-interface
[cli-login]: https://github.com/hubuum/hubuum-cli/blob/ffb4e6f25b462e413609367225e64673a3814449/docs/authentication.md#authentication-project-candidate
[rust-guide]: https://github.com/hubuum/hubuum-client-rust/blob/53649969ed2816a1f99a4d7033da5c06ce7cb27c/docs/external-authentication.md
[python-guide]: https://github.com/hubuum/hubuum-client-python/blob/7d76b19a03cd049ce70f89577c990e8a74ce3787/docs/authentication.md
[keycloak]: https://github.com/hubuum/hubuum/blob/bb5f376544d45343c83e29037eb9c2164ccc97fa/docs/authentication/keycloak.md
[oauth]: https://github.com/hubuum/hubuum/blob/bb5f376544d45343c83e29037eb9c2164ccc97fa/docs/authentication/oauth.md#githubcom
[json-profile]: https://github.com/hubuum/hubuum/blob/bb5f376544d45343c83e29037eb9c2164ccc97fa/docs/authentication/oauth.md#bounded-json-user-profiles
[google]: https://github.com/hubuum/hubuum/issues/579
[apple]: https://github.com/hubuum/hubuum/issues/580
[candidate]: https://github.com/hubuum/hubuum/blob/bb5f376544d45343c83e29037eb9c2164ccc97fa/docs/security_candidates.md#create-verify-and-activate
[web-admin]: https://github.com/hubuum/hubuum-frontend/blob/760665ada7e5a7e25f2538fcb5e1df454969a6ba/docs/session-security.md#runtime-security-administration
[cli-admin]: https://github.com/hubuum/hubuum-cli/blob/ffb4e6f25b462e413609367225e64673a3814449/docs/authentication.md#runtime-setup-for-ldap-oidc-and-oauth
[membership]: https://github.com/hubuum/hubuum/blob/bb5f376544d45343c83e29037eb9c2164ccc97fa/docs/authentication/contract.md#provider-identity-admission-and-groups
[freshness]: https://github.com/hubuum/hubuum/blob/bb5f376544d45343c83e29037eb9c2164ccc97fa/docs/authentication/contract.md#upstream-freshness-credentials-and-privileged-actions
[recovery]: https://github.com/hubuum/hubuum/blob/bb5f376544d45343c83e29037eb9c2164ccc97fa/docs/security_candidates.md#upgrade-and-recovery
[matrix]: https://github.com/hubuum/hubuum/blob/ccfa220cd8f69e74d4c705273c1b86098e2d79e7/docs/authentication/ecosystem_qualification.md#recorded-automated-matrix
[server-source]: https://github.com/hubuum/hubuum/commit/bb5f376544d45343c83e29037eb9c2164ccc97fa
[matrix-server]: https://github.com/hubuum/hubuum/commit/8e6e8344c458765af556890572593775ca4fd9a0
[rust-source]: https://github.com/hubuum/hubuum-client-rust/commit/53649969ed2816a1f99a4d7033da5c06ce7cb27c
[python-source]: https://github.com/hubuum/hubuum-client-python/commit/7d76b19a03cd049ce70f89577c990e8a74ce3787
[cli-source]: https://github.com/hubuum/hubuum-cli/commit/ffb4e6f25b462e413609367225e64673a3814449
[web-source]: https://github.com/hubuum/hubuum-frontend/commit/760665ada7e5a7e25f2538fcb5e1df454969a6ba
[upgrade]: https://github.com/hubuum/hubuum/blob/bb5f376544d45343c83e29037eb9c2164ccc97fa/CHANGELOG.md#unreleased
[storage]: https://github.com/hubuum/hubuum/blob/bb5f376544d45343c83e29037eb9c2164ccc97fa/docs/storage_adapter_sdk.md
