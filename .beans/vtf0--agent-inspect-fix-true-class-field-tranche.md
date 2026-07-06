---
# vtf0
title: 'Fix the 2 remaining needs-agent vacuity candidates (brings-surface BorromeanQuark, pre-existing file breakage)'
status: completed
type: task
priority: normal
created_at: 2026-06-28T02:00:00Z
updated_at: 2026-06-28T07:30:00Z
---

> **DONE (2026-06-28).** Both `brings-surface/orbital-*` `BorromeanQuark`
> carriers fixed + compile-verified (`lake env lean` exit 0): content-bearing
> classes (`orbitalDim` + the SO(3)/Fourier decomposition law) with conditional
> theorems deriving `dim O_n = n²`; the pre-existing breakage (orbital-fourier
> had no imports; orbital-space imported the split-out `Mathlib.LinearAlgebra.Dimension`;
> orphaned proof bodies; axiom modeling) repaired. `--check-ledger` now exits 0
> tree-wide (8 candidates remain, all `legit` with agent verdicts).


The `true-class-field` tranche surfaced by the upgraded heuristics (PR #2881) is
**34/36 resolved** (the tranche-2 swarm encoded real `: True`-field content or
honest `opaque marker` annotations, all `lake env lean` exit 0). Only **2**
candidates remain `needs-agent` in the ledger
([`docs/audits/lean-vacuity-review-ledger.json`](docs/audits/lean-vacuity-review-ledger.json)):

- `brings-surface/orbital-fourier-decomposition.lean` :: `BorromeanQuark`
- `brings-surface/orbital-space-normal-bundle.lean` :: `BorromeanQuark`

The `BorromeanQuark` content fix itself is straightforward (mirror the canonical
`observations/borromean-quark.lean` class — `borromean_volume`, `bare_mass`,
`volume_calibrates_mass`). The blocker is **pre-existing, vacuity-unrelated file
breakage**: both files have **zero / broken imports**
(`Mathlib.LinearAlgebra.Dimension`), a stray `noncomputable section`, and
commented-out signatures leaving orphaned proof bodies, so they do not compile
standalone — which is why the fix was reverted rather than shipped unverified.

**Do this (a working Lean cache is available — `lake env lean <file>`):**
1. Repair each file's structural breakage (real imports; remove the stray
   `section`; reattach or delete the orphaned proof bodies) so it compiles.
2. Encode `BorromeanQuark`'s real content (mirror the canonical class); no
   fabricated instance (honest open state).
3. Consider whether these are §0a shadow-stub orphans — if the `.ts` `lean.ref`
   resolves to the canonical library `BorromeanQuark`, the local duplicate may
   simply be deleted instead (check the ref first).
4. Verify `lake env lean` exit 0, then `--check-ledger` must exit 0.

**Done when:** both entries carry a fresh `genuine`/`legit` verdict (sha-matched)
and `bun run content/pipeline/lean-vacuity-axiom-audit.ts content/quantum-observable-universe --check-ledger docs/audits/lean-vacuity-review-ledger.json`
exits 0. Commit + push.
