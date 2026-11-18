---
# qou-k448
title: 'Sweep: ''X = X := rfl'' + non-compiling un-sidecar''d library Lean files'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T08:35:57Z
updated_at: 2026-10-04T15:24:41Z
parent: qou-5vkl
---


Surfaced 2026-08-08 on PR #4727. `QOU/Eightfold/WeylInvarianceQDeformation.lean`
was **red on `main`** (two `No goals to be solved`) and its headline declaration
was `cartanMatrix_A2 = cartanMatrix_A2 := rfl` — a tautology with unused `q`
binders — while three `.md` blocks cited it as proving q-independence. It was
found **by accident** (opening the file to check an adjacent `native_decide`),
not by any checker.

Root cause is structural, not incidental: a standalone library `.lean` under
`content/**/lean/QOU/**` with no `<block>.qa.json` sidecar is not covered by
`lean-content-siblings.yml`, and with CI auto-triggers disabled repo-wide
nothing reads it at all. A file can be red indefinitely.

Both halves are mechanically detectable:

1. **`X = X := rfl` with unused binders.** The unused-variable linter already
   fires on these — the signal exists and nothing consumes it. Cross-check
   against `lean-vacuity-axiom-audit.ts`, which keys on `: True` but (as far as
   this session saw) not on reflexivity-on-a-constant.
2. **Does it compile at all?** `scripts/lean-verify.sh` over every
   un-sidecar'd library file, against the restored `lake-cache/qou-<slug>`
   oleans. This session verified 5 Eightfold files in a few minutes each, so a
   full pass is feasible but not free.

Suggested scope: run (2) first — a red file is strictly worse than a vacuous
one, and the count is the interesting number. Then (1) as a checker addition
rather than a one-off sweep, so it does not regress.

Related: bean `qou-8fl1` item 3 (`Sym2Gate.lean` vacuous — compiles, and the
chapter prose already labels it honestly) and item 4 (`native_decide`,
discharged on PR #4727).

---

## RESULT (2026-08-08) — partial sweep landed, tooling fixed

**The instrument was broken.** `scripts/lean-direct-cone.sh` could not survey anything:
its topo-sort does `os.walk("QOU")` and so never sees the root aggregator `lean/QOU.lean`
(a *sibling* of `QOU/`, not inside it). `ORDER` collapsed to `["QOU"]` and `lean` ran on
the ~1000-import aggregator with no deps built. The reported missing
`QuadraticIrrationalBadlyApproximable.olean` was **never a red module** — it was never
scheduled. Fixed on branch `claude/k448-library-lean-red-sweep-2026-08-08`, plus
`--all`, `--keep-going`, `--min-free-gb`, capped failure logs, and an incremental TSV.

**Counts at 1187/1622 settled (73.2 %):** `ok` 665 · `up-to-date` 471 · **`error` 38** ·
**`blocked` 13**. Genuine reds **38** (lower bound); **51** including cascade-suspects.
The 13 blocked trace to only **6** red roots. Dominant shape: **19 of 38 are
`Invalid field`** (dot-notation onto an absent field — Mathlib API drift).

**Cascades are a small fraction once the cone is built** — 13 blocked against 38 genuine.
This retro-invalidates the earlier pre-fix figure of 129 reds in 490 files, which was
almost entirely missing-olean noise and **must not be cited**.

**Honest limits:** coverage is 73.2 % and is **not a random sample** (topo-order settles
shallow cones first, so the unsurveyed 435 are systematically Mathlib-heavier — the 3.2 %
rate must NOT be extrapolated); the 471 `up-to-date` modules were **not recompiled** this
run (freshly verified = 665); per-module logs were lost to a container restart, leaving
only the TSV's truncated `error_head`; and one row (`Mathlib.HeckeAlgebra`) is
**suspect** — its captured head is a *warning*, so the confirmed count is 37–38.

Data + full writeup: `docs/audits/2026-08-08-library-lean-red-sweep-partial.md` and
`docs/audits/2026-08-08-library-lean-red-sweep.tsv` (committed).

**Remaining (bean stays open):** confirm/drop the suspect row; finish the 435 unsettled
modules (cheap now — ~1268 QOU oleans exist); fix the 6 cascade roots first (clears 13 for
the price of 6); triage the 19 `Invalid field` cases as ONE class; and close the
structural hole — a green tree today means nothing while nothing watches it.
