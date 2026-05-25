# Release process

QOU publishes 7 packages under `tools/` via [release-please](https://github.com/googleapis/release-please) with `separate-pull-requests: true`. Each package has its own version, CHANGELOG, and release lifecycle.

## Tracked packages

See `.github/release-please-config.json` for the full list. As of 2026-05-25:

| Package | Path | Type |
|---|---|---|
| `pyhecke` | `tools/pyhecke/` | Python (PyPI) |
| `qou-substrate` | `tools/qou-substrate/` | Python (PyPI) |
| `witness-schema` | `tools/witness-schema/` | Python (PyPI) |
| `pyhecke-native` | `tools/pyhecke-native/` | Python (PyPI, PyO3 wheel) |
| `hecke-engine` | `tools/hecke-engine/` | Rust (crates.io) |
| `hecke-engine-wasm` | `tools/hecke-engine-wasm/` | Rust → npm |
| `hecke-engine-node` | `tools/hecke-engine-node/` | Rust → npm |

## Normal flow (when working)

1. Land a conventional-commit (`feat:`, `fix:`, `feat!:`) touching files under a tracked package's directory on `main`.
2. `.github/workflows/release-please.yml` runs on push-to-main.
3. release-please opens (or updates) a `release-please--branches--main--components--<pkg>` PR with the next version bump + CHANGELOG.
4. Owner reviews the release PR, merges when ready.
5. release-please's second pass cuts the GitHub release + tag `<pkg>-v<version>`.
6. Owner manually triggers the corresponding publish workflow (`pyhecke-pypi-publish.yml`, `pyhecke-native-wheels.yml`, etc.) via `workflow_dispatch` to push to PyPI / npm.

## Known issue — silent PR-creation failure

Observed 2026-05-24/25: release-please creates the release branch on origin but does not open the PR.

### Diagnosis

`secrets.GITHUB_TOKEN` cannot create pull requests unless the repo setting **Settings → Actions → General → Workflow permissions → Allow GitHub Actions to create and approve pull requests** is enabled. The workflow's `pull-requests: write` permission line is necessary but not sufficient — it's gated by this repo-level toggle.

### Fix options (in preference order)

**A. Enable the setting (one click; persistent).**

Repo owner navigates to `Settings → Actions → General` and checks the "Allow GitHub Actions to create and approve pull requests" box.

**B. Use a fine-grained PAT (lifetime: rotate every 90 days).**

1. Owner creates a fine-grained PAT under their account with:
   - Repository access: `litlfred/qou` only
   - Permissions: `Contents: write`, `Pull requests: write`
2. Add as repo secret `RELEASE_PLEASE_TOKEN`
3. `release-please.yml` already coalesces to the PAT when set:
   `token: ${{ secrets.RELEASE_PLEASE_TOKEN || secrets.GITHUB_TOKEN }}`

Bonus: PRs created via PAT trigger downstream CI (whereas `GITHUB_TOKEN`-created PRs don't, by design).

### Manual rescue when stranded

If a release branch landed on origin without a PR:

```sh
# Find stranded release branches
git ls-remote origin "refs/heads/release-please*"

# Open the PR manually (via gh CLI or the GitHub MCP create_pull_request tool)
gh pr create \
  --base main \
  --head release-please--branches--main--components--<pkg> \
  --title "chore(main): release <pkg> <version>" \
  --body "Manually opened; release-please workflow silent-failed PR creation."
```

This is what PRs #1234 (pyhecke 0.1.1) and #1235 (qou-substrate 0.1.1) did when the workflow first manifested the silent-fail issue.

## Conventional-commit cheat sheet

| Prefix | Effect | Example |
|---|---|---|
| `fix(scope):` | patch bump (`0.1.0 → 0.1.1`) | `fix(phase-b): address PR #1147 Copilot review` |
| `feat(scope):` | minor bump (`0.1.0 → 0.2.0`) | `feat(node): add chi_lambda_braid wrapper` |
| `feat!:` or `fix!:` | major bump (`0.1.0 → 1.0.0`) | `feat!: rename markov_z → markovParam` |
| `chore:`, `docs:`, `test:`, `build:`, `ci:` | hidden by default; no release | `chore: bump cargo deps` |

Scopes are free-form per release-please defaults. Recommended convention in this repo:

| Scope | Meaning |
|---|---|
| `(phase-a)`, `(phase-b)`, etc. | matches the workplan phase the change addresses |
| `(<pkg>)` | the affected tools/ package — e.g. `fix(pyhecke):`, `feat(node):` |
| `(ci)` | CI workflow files |
| `(witness)` | witness JSON regenerations |
