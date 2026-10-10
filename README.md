# cat/cat-harness/beans: qou's bean work-plan

This orphan branch holds qou's bean graph (`beans/beans.json` plus `beans/defs/`)
mirrored at the checkout's own paths. qou.json declares it:
`{ "id": "beans", "path": "beans/", "source": { "kind": "branch", "branch": "cat/cat-harness/beans", "keyedBy": "tip" } }`.
It was seeded by hand from `main:beans` (a steward act; no platform command
creates a new state branch). The seed is verified: this branch's `beans` tree id
equals `main:beans` at the `source.sha` in `manifest.json`. Issue
litlfred/qou#7642, owner ruling 2026-10-10.

- **Mount:** the session-start hook runs `state:mount`, which places these files
  at `beans/` in the checkout (gitignored there once the cutover lands).
- **Write back:** `bun run folio-assistant/cat-harness/scripts/branch-store.ts push --id beans`.
  This splices with `expect` and never forces. Two writers of the same file
  produce `conflict`; re-read and retry.
- **Status:** `authoritative: false` until the PR that removes `beans/` from
  `main` merges. Until then `main` is still the store, and this branch must be
  refreshed from `main:beans` (tree ids equal) immediately before that merge.
