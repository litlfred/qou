---
# qou-lsib
title: '69 content-block Lean siblings do not compile — nothing builds them, and 66 back a declared lean: ref'
status: in-progress
type: task
priority: high
created_at: 2026-08-22T20:45:00Z
updated_at: 2026-08-22T20:45:00Z
---

Measured while fixing `qou-rhax`, which was one instance of this population.
Audit: [`docs/audits/2026-08-22-inconsistent-axioms-and-unbuilt-lean-siblings.md`](../docs/audits/2026-08-22-inconsistent-axioms-and-unbuilt-lean-siblings.md) §4.
Per-file data: [`docs/audits/2026-08-22-unbuilt-lean-siblings-triage.tsv`](../docs/audits/2026-08-22-unbuilt-lean-siblings-triage.tsv).

## The population

Content-block `.lean` siblings live at
`content/<paper>/<chapter>/<block>.lean` — **outside**
`content/<paper>/lean/`, so outside the `qou` package's
`globs = ["QOU", "QOU.+"]`. `lake build QOU` never touches them, and
`lean-content-siblings.yml` does not gate them either.

**CORRECTED 2026-08-28 — right conclusion, wrong reason.** That workflow's
`content-sibling-compile` job **does** cover content-block siblings; it runs
`lean`-direct on the `.lean` files a PR changes. Two separate things stop it
reaching this population: it is **`workflow_dispatch:` only** (auto-triggers
disabled repo-wide, 2026-06-30, Actions billing), so it never fires; and it is
**diff-scoped by design**, so even when dispatched it gates new drift and never
the pre-existing backlog. The second is why remedy 2 below must *widen* the
gate rather than merely re-enable it.

`lean`-direct across all **958**, with all three paper build dirs plus
`.lake/packages/*` on `LEAN_PATH`:

| | count | share |
|---|---:|---:|
| exit 0 | 885 | 92.4 % |
| fail | 73 | 7.6 % |
| — of which environment artifacts (missing dependency olean) | 4 | |
| **confirmed file defects** | **69** | **7.2 %** |

## Why it matters

**66 of the 73 back a block that declares a `lean:` ref** — 25
propositions, 21 definitions, 5 lemmas, 5 corollaries, 4 theorems, 4
conjectures, 7 remarks. Sibling resolution takes precedence over the
library path (§0a), so for those blocks the paper's claimed formalisation
*is* the file that does not compile. The 21 definitions are the sharpest
case: a `definition` block requires a Lean sibling at type level.

This is the population that let `macroscopic-stability-equivalence.lean`
sit in the tree with 22 errors **and an axiom proving `False`**.

## Triage — most of it is cheap

| first-error class | files |
|---|---:|
| `RESOLVE` — unknown identifier/constant | 30 |
| `INSTANCE` — failed to synthesize / bad binder | 13 |
| `PARSE` — unexpected token, unterminated comment | 9 |
| `PROOF` — unsolved goals, unknown tactic, no goals | 6 |
| `TYPE` — function expected, mismatch, not a field | 5 |
| `ENV` — not a defect | 4 |
| `DUPLICATE` — name already declared | 3 |
| `NONCOMPUTABLE` | 2 |
| `OTHER` | 1 |

**339 errors across 73 files, median 2 per file, 30 files with exactly
one error.** One file dominates (`frobenius-codim-universal.lean`, 101).
The shape says accumulated drift in unchecked files — renamed Mathlib
lemmas at 41 %, a missing instance argument, a stray token — not 73
unfinished formalisations.

By chapter: `mass-theory` 27, `predicted-spectra` 10,
`quantum-observable-universes` 8, then ≤ 3 each.

## What would close this

Two halves, and the second is what stops it recurring:

1. **Repair the 69.** Start with the 30 one-error files and the 21
   definition-backed ones; adjudicate the 4 `ENV` cases in a container
   with the full QOU olean set built.
2. **Bring the population under a gate.** Either widen the package globs
   to reach `content/<paper>/<chapter>/*.lean`, or extend
   `lean-content-siblings.yml` to `lean`-direct every sibling. Without
   this, the count regrows. Precedent: bean `qou-rc7b` widened
   `QOU.lean`-root → `QOU`/`QOU.+` and recovered 785 unbuilt modules
   *inside* `lean/`; these 958 are the population that widening did not
   reach.

## Method note

The first pass of this measurement reported **297 / 31 %**. That was wrong:
`LEAN_PATH` held only `.lake/packages/*`, so every file importing `QOU.*`
failed on an unresolvable module. Adding the three paper build dirs moved
224 of the 297 to exit 0. Anyone re-running this must include
`content/*/lean/.lake/build/lib/lean` or they will overstate by ~4x.


## Update 2026-08-28 — 73 → 34, and the gate half is still open

Re-swept all 944 siblings on `main` @ `cdbdc84af1` + the 2026-08-28 tranche:
**907 pass / 34 fail / 3 neutral-skip**. Per-file TSV:
`docs/audits/2026-08-28-unbuilt-lean-siblings-resweep.tsv`. Audit §5.

All four named residuals are closed. Three here; `frobenius-codim-universal` by
a **sibling agent** on `main` (`d16f2b6273`), not by this bean.

Three findings beyond the count:

- **A third axiom proving `False`** — `eigenvalue_norm_sq_axiom` in
  `hasse-weil-bound.lean`, missing `αᵢ ≠ 0`. Machine-checked artifact at
  `docs/audits/artifacts/2026-08-28-eigenvalue-norm-sq-axiom-refutation.lean`.
  Discharged with a real proof, not deleted. The class from `qou-rhax` is not
  closed, and a file that cannot compile is where these survive.
- **`LocalQZetaFunction.q` was formal where it had to be real**, which made both
  its consumers *unstatable* rather than unproved. Its `q_pos` had been
  commented out as "not meaningful over R_q" — a prior author at the same wall.
- **The structural fix wired nothing into the build.** Both modules #5505 added
  were `qou-orph` orphans until 2026-08-28.

**Remaining work — the half that stops it regrowing.** Remedy 2 is untouched:
widen the gate. `lean-content-siblings.yml` already compiles content siblings,
but diff-scoped and `workflow_dispatch:`-only, so it reaches neither the 34 nor
anything on a push. Widening it — not re-enabling it — is what closes this.
