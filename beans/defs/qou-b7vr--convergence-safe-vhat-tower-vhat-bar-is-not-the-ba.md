---
# qou-b7vr
title: 'convergence_safe_vhat_tower: vhat_bar is not the bar image — chain keeps the unbarred h'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T07:36:35Z
updated_at: 2026-11-17T10:49:00Z
parent: qou-v2om
---

Found while working `qou-dhbr` on PR #5750. **This is not the naming issue
`qou-dhbr` describes — it is the reason that issue looked real.**

## The defect

`computations/convergence_safe_vhat_tower.py` builds the bar image as

    pg0, pg1 = nucleon_chains(("u","u","d"), h)      # chain built with +h
    ...
    z_bar = _markov_z(qi)
    vhat_bar = _std_vhat(pg0, qi, q, z_bar, qi - q)  # recurrence given -h

The crossing chain's `(c, d)` entries carry `d = -h` (for `sigma^-1 = sigma - h`)
and `-h/2`, built from the **unbarred** `h`. The recurrence is then handed
`qi - q = -h`. So a single evaluation carries `h` at **both signs**, and the
result is not the bar image of anything.

PR #5622 fixed `z_bar` — the Markov parameter — and that fix is correct. It was
only **half** the bar image; the chain was never barred.

## Measured at q0 (70 dps, mpmath end to end)

    vhat_bar(q) - vhat(1/q)           = -0.18083       <- should be 0
    gm(q)   = sqrt(|vhat|*|vhat_bar|) =  0.5561440948168445630758605
    gm(1/q)                           =  0.3111671166808308712169974
    gm(q) - gm(1/q)                   =  0.24498       <- should be 0

Rebuilding the chain with the barred `h` (`nucleon_chains(quarks, qi - q)`)
makes **both** differences **exactly 0.0**, and `gm` becomes
`0.27820062359787614354` at both `q` and `1/q`. So the fix is known and
one-line; it is the consequences that need a decision.

## Why it was NOT fixed on PR 5750

Fixing it moves the `cand3_bar_sym` committed p/n signal, currently
`+0.00994787345445912347545185569480548842428628224346213121885145`
(+0.995 %) in `computations/convergence-safe-vhat-tower.witness.json`. That
figure backs a **recorded refutation** of candidate 3 —
`docs/audits/2026-06-01-vhat-tower-im-cancellation.md:17` reads
"Phi_q / reciprocal / bar-sym refuted". So the refutation of candidate 3 rests
on numbers computed from a non-bar-image, and correcting the bar image may
change that verdict. That is a research decision, not a cleanup.

## The name `cand3_bar_sym` is CORRECT — do not rename it

`qou-dhbr` proposes renaming it to `cand3_bar_image` because "under convention D
that object is not bar-symmetric". The object is not bar-symmetric, but the
cause is this defect, not convention D. The module header defines candidate 3 as
"Bar-symmetrization (q to 1/q) of the argument", and the geometric-mean
construction **is** exactly bar-symmetric on a correct bar image (measured
above, difference 0.0). Renaming would relabel a bug as the intent, and would
move a key that is serialised into the witness at three places. A comment
recording all of this is now at the `z_bar` site.

## Next honest step

Decide whether to (a) fix the bar chain and re-run, accepting that candidate 3's
recorded refutation must be re-adjudicated against the new numbers, or (b) leave
it and re-scope the audit doc's "bar-sym refuted" line to say the candidate was
never evaluated on its intended argument. Either way the audit doc needs an
edit; (a) additionally regenerates the witness.

## Round 85 Progress (`litlfred/qou#8312`)
- **Lean 4.24.0 Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/SurrealGradeSqueezeAndBarChainTorsionBrick.lean` (`0` `sorry`, `0` `axiom`, `0` warnings; `0` CRITICAL, `0` major, `0` advisory across all 7 static audits).
- **80-dps Probe & Witness**: `computations/probes/surreal_grade_squeeze_and_bar_chain_torsion_brick_probe.py` & `computations/probes/surreal-grade-squeeze-and-bar-chain-torsion-brick.witness.json` (`scriptCommitSha = 97adfc3139b01f6834713637c8c180e84b157659`, HEAD `788d96d10c679066e399232d2279c6981861a63b`, `allPassed = true`).

