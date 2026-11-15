# Coordination ledger — proof-integration-watcher tranche

**Date:** 2026-05-22
**Branches:** `copilot/integration-backlog-proof` (PR #875), `claude/friendly-wright-GH0qG` (PR #880)
**Goal:** drain proof-axis QA backlog; repair Lean MCP layer for remote-execution sessions.

## Scope map

| PR | Branch | Status | Domain | Files touched |
|----|--------|--------|--------|---------------|
| **#875** | `copilot/integration-backlog-proof` | rebased onto `07e272f4`, ready-pending | proof axis | `content/pipeline/qa-checkers-extended.ts`, `content/pipeline/script-sidecars/proof-no-trivial-skeleton.script.json` |
| **#880** | `claude/friendly-wright-GH0qG` | open, ready | proof axis + MCP | `scripts/start-folio-assistant.sh` |
| #883 | `claude/cool-newton-JXanC` | open | MCP (paper-search / openalex) | `.mcp.json`, `folio/bib-qa-verifications.json`, `scripts/bib-papers-list.txt`, `docs/coordination/…` |
| #881 | `claude/prepare-merge-no-squash-default-2026-05-22` | open | skill policy | `.claude/commands/prepare-merge.md` |
| #882 | `claude/eager-gauss-S36Uk` | open | one-voice axis | one-voice sidecars |
| #878 | `claude/wenzl-lr-consumer-fix-2026-05-22` | open | canonical axis | docs-only |

## Sibling classification (per `coordinate.md §2`)

| Sibling | Overlap vs #875/#880 | Dependency | Cherry-pick |
|---------|----------------------|------------|-------------|
| #880 ↔ #875 | additive (same proof axis, different criterion) | independent | none |
| #883 vs #880 | additive (same MCP layer, different files) | independent | none |
| #881 vs #875 merge | policy: `merge_method: merge` per its rule | I depend on the rule | none (using it) |
| #882 | none (different axis) | independent | none |
| #878 | none | independent | none |

## Decisions

### 2026-05-22T14:39Z — PR #875 takeover

Owner directed: "agent 875 is sleeping for a few days. you can finish their work and then /prepare-merge on 875 resolve comments and merge it".

Steps executed on `copilot/integration-backlog-proof`:

1. **Rebased** onto current `origin/main` (`2f7eabe1 → 07e272f4`). Was 12 commits behind; pre-rebase diff appeared to delete `.github/workflows/copilot-setup-steps.yml`, `.github/workflows/publish.yml`, `.mcp.json`, `latex/preamble.tex`, `docs/copilot-lean-mcp-quickstart.md` (all artefacts of the stale base). Post-rebase diff is clean: `+77/-2 across 2 files`.
2. **Validated**: `bun run validate quantum-observable-universe` passes with 1 pre-existing warning (`lr-tensor-character-bridge`'s cross-refs).
3. **Empirical**: `qa-sweep --axis proof --paper quantum-observable-universe --dry-run` reports `0 critical, 0 major, 0 minor; needs-agent: 575` (was `1 major` for the false positive at `braid-link-types.lean:66`).
4. **Gemini-review asks** (commit `f7f02c26`):
   - Wider search window → ✓ `±10 lines` in `checkProofNoTrivialSkeleton`
   - Multi-line snippet matching → ✓ `span = max(1, newline_count + 1)` + `source.slice(...).join("\n")`
   - Comment stripping → ✓ `stripLeanComments(text)` handles nested block + line comments
5. **Pushed** force-with-lease: `ce8f3eaf → 64bbbb76`.
6. **Pending merge** (blocked on GraphQL rate limit for `update_pull_request draft=false`).

### 2026-05-22T14:39Z — PR #880 work-tranche

Owner directed: `/integration-watch proof and also do associated audits and backlog` + `see lean skills/mcp` + `if MCP doesn't work for lean, lets fix`.

Lean MCP diagnosis:
- `release.lean-lang.org` → 403 `host_not_allowed`
- `lakecache.blob.core.windows.net` → 403
- `mathlib4.lean-cache.cloud` → 403
- `cache.lean-lang.org` → 403
- `github.com` + `releases.githubusercontent.com` → 200

Sideloaded `leanprover/lean4:v4.24.0` from `https://github.com/leanprover/lean4/releases/download/v4.24.0/lean-4.24.0-linux.tar.zst`; linked via `elan toolchain link`. `lean --version` confirms 4.24.0 working in shell.

`mcp__paper-assistant__lean_status` still reports `mode: none` because the MCP server inherited the pre-install PATH. The durable fix is the `scripts/start-folio-assistant.sh` PATH edit (PR #880); next session start picks it up.

Mathlib build cache cannot be fetched due to the same egress policy. Per-file `lean_diagnostic_messages` LSP queries will work for files whose import closure is already built; full `lake build` would require building Mathlib from scratch (hours).

## Cross-PR notes

- **#880 vs #883**: Both touch the MCP layer but DIFFERENT FILES (PR #880 = `start-folio-assistant.sh`, PR #883 = `.mcp.json`). Independently confirmed each other's network-policy probe results. No merge conflict.
- **#881 vs #875 merge**: PR #881 sets the default `merge_method: merge` policy. Following it here since the owner's "merge it" did not contain the `squash` keyword.

## Pending work (after #875 lands)

1. Switch back to PR #880 branch `claude/friendly-wright-GH0qG`.
2. Per [PR #880 §answered-question](https://github.com/litlfred/qou/pull/880): user picked three options for proof-axis drain:
   - Small chapters first (`q-geometric-langlands` 6 + `models-of-qous` 5 + `organic-chemistry` 2 + `appendix-knot-periodic-table` 1 + `quantum-universes` 9 + `molecular-construction` 7 = 30 blocks)
   - First braids-and-knots sub-batch (49 of 237 blocks)
   - `/integration-audit proof` first
3. Execute in that order: audit → small chapters → braids-and-knots.

## Escalations

None.

## Resume targets

- This file (`docs/coordination/2026-05-22-proof-integration-watch.md`) for any future session continuing the tranche.
- Future sessions: check sibling-PR state (`mcp__github__list_pull_requests state=open`) and the `needs-agent: 575` count via the sweep CLI.
