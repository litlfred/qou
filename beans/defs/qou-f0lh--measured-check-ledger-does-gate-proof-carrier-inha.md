---
# qou-f0lh
title: 'MEASURED: --check-ledger DOES gate proof-carrier-inhabited-by-probe (qou-jr5r leg refuted)'
status: completed
type: task
priority: normal
created_at: 2026-08-30T10:03:23Z
updated_at: 2026-08-30T10:03:49Z
---

Cross-refs bean `qou-jr5r` (sibling), PR #6162 comment thread.

## Claim under test

A sibling reported a THIRD ledger hazard: `--check-ledger` "does not gate the
`proof-carrier-inhabited-by-probe` category at all", evidenced by the string
`carrier-inhabited-by-probe` appearing 0 times in the audit's output JSON and
having no row in the per-category console summary, with a worked case
(`QOU.AlgebraicSubstrate.BlowupYekutieli`) whose ledger `file_sha`
`3f4362244eaf` was said to be stale against a live `4d855ce423f8`.

## Measured on main — two of three legs do not hold

**1. The category IS gated. Settled by FAULT INJECTION, not by reading.**
Corrupted the `file_sha` on that exact entry in a ledger copy and re-ran:

    real ledger      -> 3 candidates lack a fresh verdict
    corrupted copy   -> 4, the extra being
      ConditionalClasses.lean:203
      [proof-carrier-inhabited-by-probe/lean-inhabited-no-hypotheses]
      QOU.AlgebraicSubstrate.BlowupYekutieli

**Where the inference went wrong.** The evidence is about the FINDINGS array;
the gate iterates the CANDIDATES array. `seedProbeInhabitedCandidates` pushes
directly into `candidates` at `lean-vacuity-axiom-audit.ts:2985`, inside the
`if (reviewLedger || checkLedger)` block at :2943 — so probe-seeded candidates
never traverse the scanner's findings pipeline. Their absence from the output
JSON and from the summary is CORRECT and says nothing about gating.

**2. Count is 21, not 5** — `genuine` 17, `legit` 4.

**3. The worked case is FRESH on main** — ledger `3f4362244eaf` == live
`3f4362244eaf`, and `git diff origin/main -- ConditionalClasses.lean` is empty.
All 21 in the category: fresh 21, stale 0, missing 0. The `4d855ce423f8` is
presumably that file as modified on the sibling's own branch.

## What I could NOT reproduce, and did not claim against them

They report `--check-ledger` exit 0. On main it exits **1**, on three
`proof-dependent-conjecture-not-conditional` candidates in files byte-identical
to main (inherited, not from #6162). A DIFFERENT hazard would explain an exit 0
and is worth separating in `qou-jr5r`: if a probe-inhabited candidate stops
being SEEDED (decl renamed, or the probe baseline no longer proving it
inhabitable), it drops out of `candidates` and is never asked about again. That
is a real gap with a different fix from "the category is not gated".

## TRAP for the taxonomy

Absence from a detector's OUTPUT is not evidence about that detector's GATE
when the two iterate different arrays. Same family as the arity conflation:
the measurement was sound; the thing measured was not the thing claimed.

## Side effect worth knowing

Running the audit REWRITES `docs/audits/2026-06-17-lean-vacuity-axiom-audit.json`
(+410/-37 vs main on a fresh run). Restore it after any investigative run or it
lands in an unrelated PR.
