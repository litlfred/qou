---
# qou-r4ya
title: 'Balanced D-function theta-limit: derive the balanced lattice CLASS (not the extension — see scope note)'
status: in-progress
pr: 8217
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T21:33:57Z
updated_at: 2026-10-04T15:11:58Z
parent: qou-r9ih
---

Run the recentring + theta-limit machinery of
[`AwZeroLocalization`](../folio/quantum-observable-universe/lean/QOU/Archimedean/AwZeroLocalization.lean)
/ [`2026-08-01-awzero-asymptotics.md`](../docs/audits/2026-08-01-awzero-asymptotics.md)
on the **balanced** family's D-function, to link the balanced extremal
supports to the balanced tropical roots. Combined with the exact E-transport
(`TropicalClassTransport`), that would make the balanced extremal class
`φ₁ = frac(log_q̃ E)` — the `u ≡ 1` class — a *derived* statement rather than
a measured one.

**SCOPE CORRECTION (2026-08-01).** This bean was originally titled "close the
fibre leg outright." **That was an overstatement and is corrected here.**
Friedrichs and Krein occupy *complementary sublattices of the same* `u ≡ 1`
class (per `2026-08-01-ksel2id-u1-promotion.md`: "Krein odd, Friedrichs even
q-sublattice", "complementary q-sublattices of the one u ≡ 1"). A class-level
result therefore fixes the **coset**, not the **extension** — so even a fully
successful balanced theta-limit leaves the conjecture's actual closing
question (*which* self-adjoint extension is distinguished) open.

**What this bean can and cannot deliver:**

- CAN: balanced extremal class = `φ₁`, derived — removing the last measured
  step in the class chain.
- CANNOT: select Friedrichs vs Krein. That needs a different kind of input —
  an operator-level or substrate-level principle, not a lattice argument.
  Note KSel-3 already found that two natural covariance strengthenings pick
  *different* unique members, so "the substrate does not select" is a live
  possibility and would itself be a result.

**Acceptable outcomes.** Either the theta limit transfers (with an explicit
n₀ and constant, ideally at the pins), or the Jackson factor obstructs the
triple-product structure and the obstruction is characterized precisely. An
honest negative is a good outcome; do not manufacture a positive.

Follow-on bean to open once this resolves: the Friedrichs-vs-Krein selection
principle (needs owner framing — candidate routes are minimal-form/Friedrichs
distinguished, a dual-mode positivity/entropy criterion, or accepting
non-selection as physical).



## Reclassified 2026-09-05 — not an owner ruling, and never was

Triaged into the owner-gated Cluster 7 as a "Friedrichs-vs-Krein framing"
call. Re-read: this bean asks nobody to decide anything. It proposes running the
recentring + theta-limit machinery on the balanced family's D-function, and it
already carries its own **scope correction** stating exactly what that can and
cannot deliver (the class-level result fixes the *coset*, not the *extension*,
so the conjecture's closing question stays open either way).

That is open research, which the **2026-07-11 general reversal** put in scope
for all agents with no per-item sign-off. Off the owner-gated queue; open as
work.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Progress Update (2026-11-16T22:04:01Z)
- Implemented machine-checked Lean 4 theorem in `folio/quantum-observable-universe/lean/QOU/QBeta/SteepestDescentEulerMaclaurinAndFrobeniusDiagonal.lean` and 80-dps `mpmath` / exact rational witness `computations/probes/steepest-descent-euler-maclaurin-and-frobenius-diagonal.witness.json`.
- Opened PR https://github.com/litlfred/qou/pull/8217 (`f4d145a08828886b4eba631166b3e61717adc12d`); keeping `status: in-progress` until PR merges.
