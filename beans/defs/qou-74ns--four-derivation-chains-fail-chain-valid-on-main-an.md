---
# qou-74ns
title: Four derivation chains fail chain_valid on main, and main's committed audit witness says allPassed:True because it is stale
status: completed
type: task
priority: high
created_at: 2026-09-04T11:15:20Z
updated_at: 2026-09-05T08:46:50Z
---

Found 2026-09-04 on PR #6519, by running `derivation_chain_validator.py` after
merging 72 commits of `origin/main` into `claude/standard-model-terms-status-ftoejr`.
The validator exits **2** and writes `allPassed: False`. The failure is **not
numerical and not this branch's** — see the attribution below before treating
it as merge breakage.

## The four failing chains

| chain | reason reported |
|---|---|
| `D-tr-M-q0.derivation.json` | step *"Atomic D Hecke element T_w(Z=1, N=1) — NOT a braid word"*: script-cited step requires a `script: <path>` note |
| `n-tr-M-q0.derivation.json` | same shape, step *"Atomic n Hecke element T_w(Z=0, N=1)"* |
| `p-tr-M-q0.derivation.json` | same shape, step *"Atomic p Hecke element T_w(Z=1, N=0)"* |
| `markov-trace-assembly-deuteron.derivation.json` | step *"Per-irrep characters χ^λ_q(β_D) via Hoefsmit recipe"* cites `computations/hecke_character_symbolic.py`, **which does not exist** |

Three are a metadata defect in the derivation JSON (a step names a script
without carrying the `script:` key the schema requires). The fourth is a
dangling citation.

## The citation has NEVER resolved

`computations/hecke_character_symbolic.py` is absent at the branch's merge-base,
absent on `origin/main`, absent on this branch, and `git log --all -- <path>`
returns **no commit that ever touched it**. So this is not a file someone
deleted; the chain has cited a path that has never existed in this repository.

## Why `main` looks green: its audit witness is STALE, provably

`origin/main`'s committed `computations/derivation-chain-audit.witness.json`
records `allPassed: True` — measured against a tree that no longer exists.
Compare `origin/main` against itself:

    markov-trace-assembly-deuteron.derivation.json  (on main)  value = 0.5751722439177719
    derivation-chain-audit.witness.json             (on main)  leaf  = 0.3882864240747888

The witness records a leaf value the derivation JSON beside it has not held
since `9b00d47036` / `aec2eaa7cf` (the `qou-1ucq` fix, 2026-08-30..09-04),
which rewrote five derivation JSONs. Those commits did not regenerate this
audit, and the audit's own last regeneration (`038faafb73`) predates them.
So **`allPassed: True` on main is an artifact, not a passing run.**

## Attribution — measured, not assumed

- This branch changed **0** `*.derivation.json` files
  (`git diff --name-only <merge-base> <branch-head> -- '*.derivation.json'` is empty).
- `origin/main` changed **5**, and they are exactly the five involved here.
- The audit witness at `origin/main` **and** at this branch's pre-merge head
  (`47a5aca7f7`) both read `allPassed: True` with zero failing assertions; the
  failures appear only once main's derivation JSONs and a fresh validator run
  are in the same tree.

## Disposition on PR #6519

The freshly-computed witness is committed **as it stands, red**, rather than
reverted to main's stale green one. Restoring the stale artifact would be the
"make a red run green by widening a baseline" move AGENTS.md forbids, one
artifact type over.

## Next honest step (not taken here — out of this PR's scope)

1. Add the missing `script:` note to the three `T_w(Z,N)` steps, or drop the
   script citation if the step is not script-backed.
2. Decide what `hecke_character_symbolic.py` was meant to name. The Hoefsmit
   character route does exist in the corpus under other filenames; the chain
   should cite the real producer or say the step is narrative.
3. Regenerate `derivation-chain-audit.witness.json` on `main` in the same
   commit as either fix, so the artifact stops disagreeing with its own tree.

Related: `qou-1ucq` (completed — the 73×/122× numerical contradiction whose fix
rewrote these JSONs), `qou-rm57` (the convention-frame scoping of the same
documents).


## CLOSED 2026-09-05 — headline resolved; all three "next honest steps" checked individually

Verified in a session that picked this bean off `scripts/bean-completion-candidates.py`
(bean `qou-bstl`). Each item was measured, not assumed.

**Headline — RESOLVED.** The bean claims *"Four derivation chains fail chain_valid on
main, and main's committed audit witness says allPassed:T"*. Fresh run of
`computations/derivation_chain_validator.py` on `main` `c1a61ec8b2a`:

    ✓ Witness: derivation-chain-audit.witness.json (103 assertions, all passed)
    derivation_chain_validator: PASS

Fixed by `29ea25f485b` (*"derivation_chain_validator goes GREEN — two mechanical
defects, 4 failures to 0"*). Run twice this session, hours apart, both PASS.

**Item 1 — NOT a defect, and the count was wrong (3 -> 5).** Measured over every
`computations/*.derivation.json`: **9** steps name `T_w(...)`, and **5** carry no
`script:` note — not three. All five are `Atom assembly rule T_w(...)` steps in
`atomic-braid-recipe-{4he,4he-canonical,d-canonical,p-canonical,n-canonical}.derivation.json`,
and their own `operation` text says *"Pure algebra; sequence of disjoint-block braids
concatenated in B_{3A}"*. This bean's item 1 offers exactly this disposition — *"or drop
the script citation if the step is not script-backed"* — and the validator PASSES with
them absent, so the absence is correct rather than missing. The four that DO carry the
note are the Hecke-element / braid-word steps, which are script-backed. Nothing to add.

**Item 2 — RESOLVED, and it was STALE WHEN WRITTEN.** The item reads *"Decide what
`hecke_character_symbolic.py` was meant to name. The Hoefsmit character route does exist
in the corpus under other filenames."* The file **exists**, at
`computations/hecke/hecke_character_symbolic.py`, added by merge `b831ff34c3d` on
**2026-08-29 09:44** — **six days before this bean's own updated_at
(2026-09-04T11:15:59Z)**. And every citing chain uses **exactly that path**:
`n-tr-M-q0`, `p-tr-M-q0`, `D-tr-M-q0`, `D-tau-M-q0` and
`markov-trace-assembly-deuteron` all write
`script: computations/hecke/hecke_character_symbolic.py`. There is no phantom and no
path mismatch — `computations/hecke_character_symbolic.py` (root) correctly does not
exist and nothing cites it.

**Item 3 — structural, not a defect.** Regenerating `derivation-chain-audit.witness.json`
on `main` still produces a diff, but it is **volatile fields plus accretion**:
`computedAt`, `commitSha`, `pyhecke_native_build`, and 8 newly-landed witnesses joining
the computational-only list (`d1b-52-cusp-shape-bar-parity`,
`qbeta-bounded-degree-cannot-carry-coulomb`, `qbeta-fibre-unit-circle-opens-route5`, ...).
That list **grows as the corpus grows**, so the artifact can never be permanently equal
to a fresh run — the disagreement this bean was about was the `allPassed` contradiction,
and that is gone. The regenerated witness was **reverted rather than committed**: it is a
tree-measuring audit output, and committing it from a feature branch records this
branch's tree, not main's.

## Cross-reference for `qou-bstl`

This bean is a candidate the audit surfaced, and it closes — but item 2 is a finding
`qou-bstl` does not yet carry: **a bean's own remediation list can be stale on arrival**.
An agent following item 2 would have hunted for a producer that had existed for six days,
at the very path the chains already cite.
