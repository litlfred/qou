---
# qou-aspz
title: 'NOT-LEAN-PROVED: Rademacher Phi((RL)^n)=0 rests on three agreeing computations'
status: completed
type: task
priority: normal
created_at: 2026-08-07T17:10:11Z
updated_at: 2026-08-07T17:10:11Z
---

NOT LEAN-PROVED. Established by compute only (PR #4513,
computations/probes/qbeta_rdmr_rademacher_winding_probe.py).

CLAIM: for the canonical 3-braid closures (sigma1 sigma2^-1)^n, whose SL(2,Z)
image is (RL)^n, the Rademacher function vanishes: Phi((RL)^n) = 0.

CURRENT EVIDENCE: three independent numerical/symbolic methods agree —
the Dedekind-sum formula in exact `Fraction` arithmetic, the RL-word count
(Phi = sum a_i - sum b_i), and homogeneity Phi(A^n) = n*Phi(A). This is the
basis of the scope-(a) refutation of the Rademacher route for theta_K.

WHY IT MATTERS: the refutation is durable and load-bearing (qou-rdmr is closed
on it). A Lean proof would make it permanent rather than resting on three
agreeing computations.

WHAT A PROOF NEEDS: the substantive content is the homogeneity / word-count
characterisation of the Rademacher function on hyperbolic conjugacy classes.
A bare `Phi := #R - #L` definition plus "balanced words give 0" would be
DEFINITIONAL and near-vacuous — do NOT ship that and call it a proof; the
vacuity audit would be right to flag it. The real target is the agreement of
the Dedekind-sum formula with the word count.

DIFFICULTY: medium. Dedekind sums exist in Mathlib
(`Mathlib.NumberTheory.DedekindSum`?  verify); the reciprocity law is the
likely lever.

---

## CLOSED 2026-08-08 (PR #4513) — proved sorry-free, by a different route

`QOU/Knot/RademacherReversible.lean`. `Phi((RL)^n) = 0` is now Lean-proved for
EVERY n, without Dedekind sums, without the word count, and without reciprocity.

**THE BEAN'S PROPOSED LEVER DOES NOT EXIST.** This bean guessed "Dedekind sums
exist in Mathlib (`Mathlib.NumberTheory.DedekindSum`? verify); the reciprocity
law is the likely lever" and rated the difficulty medium. Verified: there is no
Dedekind sum in Mathlib. The only relevant module is
`NumberTheory/ModularForms/DedekindEta` (the eta FUNCTION — product definition,
non-vanishing, differentiability); there is no eta transformation law, no
multiplier system, and no Rademacher function. `KummerDedekind`,
`DedekindDomain` and `DedekindZeta` are unrelated ring theory / L-functions.
That route means building the theory from scratch, so the difficulty was
materially underestimated.

**THE ROUTE TAKEN.** `RL` is REVERSIBLE — conjugate to its own inverse:

    S * RL * S^-1 = (RL)^-1,      S = [[0,1],[-1,0]]

and conjugation is a homomorphism, so the SAME S reverses every power at once
(`Reversible.pow`). Any conjugation-invariant, inversion-antisymmetric function
vanishes on a reversible element (`eq_zero_of_reversible`: invariance moves
Phi(g) to Phi(g^-1), antisymmetry turns that into -Phi(g)). Antisymmetry is free
from homogeneity at n = -1 (`homogeneous_inv`), so a caller with the usual
packaging of the Rademacher function needs only conjugation-invariance.

**WHY THIS IS STRONGER THAN WHAT WAS ASKED.**
  - Uniform in n; the compute checked finitely many.
  - It EXPLAINS the probe's observation. Phi vanished at both anchors and
    "could not even distinguish them" — not an accident: both anchors are
    (RL)^n closures, hence both reversible, hence both pinned to 0
    (`rademacher_cannot_distinguish`).
  - It closes the route against ALL quasimorphism-flavoured invariants at once,
    not just Rademacher's Phi — no such invariant can rescue it.

**THE VACUITY TRAP THIS BEAN WARNED ABOUT IS AVOIDED.** The warning was that a
bare `Phi := #R - #L` plus "balanced words give 0" would be definitional. No
word count appears here. Checks run: all three capstones survive the triviality
ladder (aesop fails on each), and the CONTROL `Sm_not_conj_Rm` proves the SAME
conjugation is FALSE for the parabolic R — so `Sm_conj_RL` is a fact about RL,
not a formality any matrix satisfies. Honest limit recorded in the file: that
control says THIS conjugator fails for R, not that R is non-reversible (true in
SL(2,Z), but needs an argument over all conjugators; not attempted).

**HONESTY BOUNDARY.** Conjugation-invariance and antisymmetry of Phi are
carried as EXPLICIT HYPOTHESES, not proved. They are standard for homogeneous
quasimorphisms. The theorem DERIVES its conclusion from them (§3b-cond shape);
no class carries the conclusion. `decide` is used only on 2x2 integer matrix
equality — a genuinely finite decidable computation, not `native_decide`.

Scope (a): nothing refutes the Rademacher function; what is shown is that the
Rademacher route cannot supply theta_K, for a structural reason.
