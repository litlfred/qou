---
# qou-lsib
title: 'Content-block Lean siblings: 34 unverified as of 2026-08-28, and nothing in CI builds them'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-22T20:45:00Z
updated_at: 2026-10-04T15:10:52Z
parent: qou-5vkl
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

---

## Note from `qou-eddc` / `qou-ox7y` (2026-09-07): "nothing builds them" ≠ "they do not build"

Not a resolution — a correction to the premise, from a session that was
**blocked by the stronger reading of this bean** and should not have been.

`qbeta-per-block-chi-closed-forms.lean` is one of this population. It compiles
at **0 errors** in this container, before and after a definition swap, with
`lean` invoked directly:

```sh
cd folio/quantum-observable-universe/lean
export PATH="$HOME/.elan/bin:$PATH"
LP=$(find "$PWD/.lake" -type d -path "*/build/lib/lean" | tr '\n' ':')
export LEAN_PATH="${LP}${PWD}/.lake/build/lib/lean"
lean -D autoImplicit=false --root="$PWD" ../mass-endomorphism/<block>.lean
```

The bean's own measurement is right and unchanged: these files are outside the
package globs, so `lake build QOU` never touches them and nothing in CI does
either. What does not follow — and what a reader takes away — is that they are
broken. At least one is not.

This mattered concretely. `qou-eddc` recorded itself as blocked on Lean, citing
this bean, and left a definition unmigrated across three attempts. Both halves
of that were wrong: `lake` was on disk the whole time at `~/.elan/bin`, and the
sibling built.

**Worth measuring before triaging:** run the invocation above across all 69 and
split the population into *green but unwired* and *actually broken*. If most are
green, this is a CI-wiring task, not a repair backlog, and the 66 declared
`lean:` refs it backs are in better shape than the bean currently implies. I
have not run that sweep — one file is one file.

---

## 2026-09-07 — the gate half, and a re-measure of the 34

### Correcting my own note above

The note I appended earlier today recommended running a whole-tree sweep. That
was redundant — the 2026-08-28 update on this bean had already run it (944
swept, 907/34/3), and even records the `LEAN_PATH` gotcha I rediscovered. What
misled me is that this bean's **title** still says 69, and a reader takes the
title, not the fourth section. Retitling is the cheap half of the fix.

### Remedy 2 (widen the gate) — done, and it was worse than recorded

The bean had it as "diff-scoped ... so it reaches neither the 34 nor anything
on a push". Measured rather than reasoned, it was a **green no-op**. Both jobs
computed

    base="origin/${{ github.base_ref }}"
    files=$(git diff --name-only --diff-filter=d "$base"...HEAD -- '*.lean' | tr '\n' ' ')

and `github.base_ref` is **empty for `workflow_dispatch`**, the workflow's only
trigger. `base` became the literal `origin/`, git answered `fatal: bad revision
'origin/...HEAD'`, and `files` came back empty. `set -e` did not fire, because
the assignment's status is the pipeline's and the pipeline ends in `tr`. Every
downstream step was `if: files != ''`. **Both jobs skipped everything and
reported green, on every run they were ever capable of.**

Fixed by a `scope` input (all | changed, default all) resolved through a new
`scripts/lib/ci-lean-scope.sh`. Against this checkout the old idiom yields 0
files; the new one yields 938 siblings. Auto-triggers stay off — this widens
what a dispatch covers, it re-enables nothing.

The shared function is not there for DRY. It is there because an *unresolvable*
scope and a *genuinely empty* scope produced the same output and the caller
could not tell them apart. Now a scope that cannot be computed fails, an
unresolvable base fails, and a whole-tree scope that comes back empty fails —
the tree is never empty. `--self-test` has 11 cases; case 1 reproduces the
original defect against the old idiom, so the fix is measured against the bug.

`--fail-on` stays scope=changed only. Whole-tree is report-only: ~40
pre-existing import-order defects exist tree-wide, so a whole-tree `--fail-on`
would be red for unrelated reasons. It prints them; it does not pretend to gate.

### The same green-no-op one layer down

`scripts/lean-verify-siblings.sh` `exit 0`'d when the olean cache could not be
restored, printing only a `::warning`. Caught live: re-running the 34 through it
today, `lean-cache-restore.sh` died (`tar: Unexpected EOF in archive`) and the
script **reported success over 32 files it never opened**, in a run whose whole
purpose was to re-check them.

The neutral-skip is right — a cold runner must not false-block a PR — but
conflated with 0 it means a permanently broken cache makes the gate permanently
green and useless, silently. Now **exit 3 = VERIFIED NOTHING**, for both the
no-cache path and the every-file-neutral-skipped path. CI maps 3 to a warning,
so blocking behaviour is unchanged; an agent running it locally now sees that
nothing was verified.

### Re-measuring the 34

Direct `lean` sweep against the paper's own olean tree (the invocation that
works in this container), then the script's own stale-import disambiguation
against `scripts/data/mathlib-modules.txt` — whose rev matches the manifest
pin, so the check is valid. Per-file:
`docs/audits/2026-09-07-known-failing-siblings-recheck.tsv`.

| 2026-08-28 | 2026-09-07 |
|---|---|
| 34 FAIL | **2 deleted** from the tree |
| | **12 now compile clean** |
| | **20 unverifiable here** — imports outside this container's olean cone |
| | **0 confirmed still failing** |

**20 unverified is not 20 fixed**, and I am not claiming the residual is zero.
What the stale-import check does establish is that none of the 20 is hiding a
real defect behind a skip: every missing module genuinely exists at the pinned
Mathlib rev or in the QOU source tree, so all 20 are true cache-cone misses.
Confirming them needs the wider cone, which this container does not have.

### What is left

- **Retitle this bean.** "69 ... do not compile" is wrong by its own
  2026-08-28 measurement and is what sent me down a redundant path.
- **Verify the 20** under a full olean cone.
- **Nothing dispatches the widened workflow.** With Actions billing off, the
  practical enforcement is an agent running `scripts/lean-content-sweep.sh`
  (source-based, stronger than the cache-based CI check) — `/prepare-merge`
  already names it at step 375. That is the honest state: the gate is now
  correct *when run*, and what runs it is discipline, not CI.

### The 20 resolved — residual is ZERO

The 20 that were unverifiable an hour earlier all **PASS**:

    lean-verify-siblings: pass=20 neutral-skip=0 fail=0

They were neutral-skipped because I ran them against the *paper's* olean tree
(`folio/quantum-observable-universe/lean/.lake`), whose cone does not cover
their imports. `scripts/lean-verify-siblings.sh` uses the **root** `.lake`, and
the root cache is in fact fine here: 3480 mathlib oleans, above the ~2900
"complete" mark. Re-running `lean-cache-restore.sh` now prints *"3480 mathlib
oleans already present — skipping"* and exits 0.

So the "corrupt tarball" was never the blocker I called it. The earlier
`tar: Unexpected EOF` came from a *later* payload in the same restore; mathlib
had already extracted completely, and the run that reported it had simply not
got that far when I read the log. **The tar failure is real but it is not on
the path that matters** — which is exactly the kind of thing the new exit-3
signal is for: the script said VERIFIED NOTHING, and the right response was to
find out why, not to assume the worst.

**Final tally on the 34 recorded FAIL at 2026-08-28:**

| | |
|---|---|
| deleted from the tree | 2 |
| compile clean | **32** |
| still failing | **0** |

Per-file: `docs/audits/2026-09-07-known-failing-siblings-recheck.tsv`.

The repair backlog this bean opened with is empty. What remains is entirely the
wiring half: nothing in CI builds these, and with Actions billing off the
enforcement is an agent running `scripts/lean-content-sweep.sh` (source-based,
stronger than the cache check) — which `/prepare-merge` already names.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
