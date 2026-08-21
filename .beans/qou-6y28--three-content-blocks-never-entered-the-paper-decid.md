---
# qou-6y28
title: 'Three content blocks never entered the paper — decide: wire in or remove'
status: completed
type: task
priority: normal
created_at: 2026-08-15T21:23:35Z
updated_at: 2026-08-21T15:36:38Z
---


## What was found

Three content blocks have `.ts` manifests written against APIs that
**have never existed in this repository** — `git log --all` on each
import target returns zero commits. They have never imported, never
rendered, and are absent from the paper.

| block | broken import | landed |
|---|---|---|
| `mass-theory/atomic-q-reeb-universal-rho` | `../../pipeline/content-block` | `649f5eb701` 2026-06-28 |
| `mass-endomorphism/qbeta-toroidal-harmonics-basis` | `../../ontologist` | `290ce47222` 2026-07-06 |
| `nuclear-interactions/audit/wigner-su4-alpha-cluster-probe` | `../../../../../schema/block-schema` (leaves the repo) | `1b60cb2fa2` 2026-08-03 |

`run-validate` walks the chapter manifests' block lists, not the
filesystem, so none of this is a validation error — the blocks are just
invisible. Validation is green with all three in place. They also get no
`.qa.json` criteria refreshed, so one-voice, canonical-watcher, q-usage
and devils-advocate all skip them.

Each landed in a commit whose message announces the content as delivered
("codify universal-rho normalisation and the 1.67% mirror asymmetry
prediction"; "draft toroidal harmonics basis in paper and scaffold
lean"). The history overstates what is in the paper.

Two further defects of the same class were mechanical and are already
fixed on PR #5138 — `delta-max-numerical-scale` (`audit:` label on a
`proposition`) and `ugb-main-theorem-proof` (`proof:` for `prf:`).

## Why this needs the author

The content is not empty — it carries substantive unreviewed claims:

- `qbeta-toroidal-harmonics-basis` asserts the Habiro trace continuum
  limit is governed by half-integer toroidal harmonics, and that the
  topological normalization *fixes* `c_4 = 2`, enforcing `C = -22`.
  Its manifest also stores `status: "verified"`, which AGENTS.md §4
  forbids outright (status is derived, never stored).
- `atomic-q-reeb-universal-rho` asserts the Lever-3 normalisation
  `B(K) = ρ · S(K)` on a Markov-weighted q-Reeb phase sum.

Writing schema-correct manifests for these would make them *look*
adopted while nothing has reviewed the mathematics. Wiring them into
their chapters is a content decision, not a mechanical repair, so it is
left here rather than taken on the render-drain PR.

## Options

1. **Wire in** — convert each manifest to the real builders API, add to
   the chapter manifest, run `qa-sweep`, and let the watchers review the
   claims. Drop `status: "verified"` (schema-forbidden).
2. **Remove** — delete the `.ts`/`.md`/`.qa.json` triples as abandoned
   drafts. Cheapest, and loses nothing that is currently in the paper.
3. **Park** — leave them and let `block-manifest-audit` keep reporting.

Also debris from the same commit: `content/quantum-observable-universe/mass-endomorphism.ts`
is a stray 1-line file at paper level whose entire content is
`export * from "./mass-endomorphism/qbeta-toroidal-harmonics-basis";`.
The real chapter manifest is `mass-endomorphism/mass-endomorphism.ts`
and does not list the block. Remove the stray under options 1 or 2.

## Recurrence is closed

`content/pipeline/block-manifest-audit.ts` (PR #5138) detects this class
and is wired into `scripts/check-sidecars.sh`, so a changed block whose
manifest does not load now fails the pre-commit preflight.
