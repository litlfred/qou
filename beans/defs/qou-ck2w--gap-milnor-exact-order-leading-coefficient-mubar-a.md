---
# qou-ck2w
title: 'GAP: Milnor exact-order leading coefficient mubar_A != 0 (exact law order(D_A)=2(A-1)) is OPEN'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T19:16:41Z
updated_at: 2026-11-20T16:06:50Z
parent: b9cj
---


## What is open

The EXACT Milnor order law `order(D_A) = 2(A−1)` for the A-component Brunnian
trace deficit `D_A = 1 − τ_A` — equivalently the length-A Milnor invariant
μ̄(12…A) ≠ 0 (nonzero leading coefficient). #4471 proved only the **lower bound**
`order ≥ 2(A−1)` and left this as `MilnorExactOrderConjecture` (instance-less).

## What was tried (#4480, 2026-08-01)

- **Route B (inductive leading-coefficient tracking) — PROVED SUB-WALL.** #4471's
  order engine `iterCommTower` is a *Lie* (ring) commutator; any cyclic Markov
  trace kills it (`cyclic_trace_kills_iterCommTower`, sorry-free in
  `MilnorExactCoefficient.lean`). So the leading coefficient is provably NOT
  extractable from the Lie tower via the trace — Route B as stated is dead.
- **Route C (compute) — 4 data points.** Measured μ̄_A = (3/4)(−2)^{A−3} =
  {3/4,−3/2,3,−6} for A=3..6, orders exactly 2(A−1). Clean but MEASURED, not
  derived. The (−2)^{A−3} is the trace normalization; the true Milnor part is ±1.

## Surviving route (Route A — needs machinery Lean lacks)

The exact law = the Milnor = leading-Vassiliev-invariant bridge (Bar-Natan;
Habegger–Masbaum; Meilhan–Yasuhara): the first non-vanishing Vassiliev invariant
of the Jones trace at degree 2(A−1) is ±μ̄(12…A) = ±1. **Mathlib has no
finite-type / Vassiliev theory.** Next honest step: either (i) formalize enough
finite-type invariant theory to state μ̄(12…A) = ±1 (large), or (ii) derive the
measured closed form μ̄_A = (3/4)(−2)^{A−3} symbolically (exact Markov trace of
w_A in q; sympy Hoefsmit) and PROVE the A=5/A=6 tight slices like #4471's
`borromean_tight_slice` — that upgrades "measured" to "proved" per A but does not
give the all-A law.

Do NOT fabricate a `MilnorExactOrderConjecture` instance.

ROUTE ASSESSED AND DECLINED 2026-08-29 (session 01JBMtTn): 'measure the Milnor cofactor growth to convert the scope-(a) order-law mismatch into scope-(b)' does NOT work, and should not be attempted as framed.

A multi-angle sweep proposed exactly that: the measured cumulant profile (u2=2.2246, u3=1.4262, u4=9.2434; u3/u2=0.6411, u4/u3=6.4810) is flat-to-growing against a per-body-order suppression of h^2, a 14.7-65.3x mismatch at the first step, and the suggestion was that the known cofactors (3/4 at A=3, -96 at A=4) might compensate, so measuring their growth would settle it.

It cannot, for a reason the corpus states in as many words:

 * order(D_A) >= 2(A-1) is PROVED, but only as a LOWER BOUND.
 * order(D_3) = 4 is proved exactly (cofactor(0) = 3/4 != 0).
 * order(D_4) = 6 is MEASURED, NOT PROVED (tauL4MeasuredOrder, #4378).
 * The exact law for all A is MilnorExactOrderConjecture — instance-less by design.

So the only two points available are A=3 (proved) and A=4 (measured), and MilnorOrderLawGeneral.lean says directly that 'fabricating an instance of MilnorExactOrderConjecture would launder the two-point pattern into a universal claim (anti-laundering discipline)'. Two further files record the same refusal: MilnorExactCoefficient.lean ('No new instance ... is fabricated here') and MilnorMagnusCoefficient.lean ('left instance-less'). Verified: zero instances anywhere in the Lean tree.

A cofactor-growth trend fitted through two points, one of which is itself only measured, IS the two-point pattern those three files refuse to launder. Reporting it as evidence for or against a growth law would be the same move under a different name.

CONSEQUENCE FOR THIS BEAN. The scope-(a) -> scope-(b) upgrade is not gated on a measurement at all; it is gated on THIS bean — the leading-coefficient conjecture. Anyone who wants the upgrade needs mubar_A != 0 for general A (Route-A finite-type theory, cited in MilnorExactCoefficient.lean:66 as Mathlib-inaccessible), not more numerics at A=3,4. Do not re-derive the cofactor ratio expecting it to decide anything.

## 2026-08-31 — SUPERSEDED at the math level by the recursion proof (qou-v7ro, #6217)

The exact-order law this bean calls OPEN — order(D_A)=2(A−1) ∀A ⟺ leading μ̄ coefficient ≠ 0 ∀A —
is now PROVED MATHEMATICALLY, by a DIFFERENT route than the leading-coefficient-tracking (Route B)
described above. The convention-D deficit recursion D_{A+1}=−h²(h²+2)D_A is proved ∀A by TL
structural induction (#6217, certified; probe milnor_recursion_forall_A_proof_probe.py all_verified;
audit docs/audits/2026-08-30-milnor-recursion-forall-A-PROVED.md). Its closed-form solution from the
proved A=3 base is D_A=(−1)^{A−3}h^{2(A−1)}(h²+2)^{A−3}(h²+3)/(h²+4), whose leading coefficient is
(3/4)(−2)^{A−3} ≠ 0 ∀A — exactly the nonvanishing this bean needed. Lean tight_slice_of_recursion
(merged) proves [BrunnianDeficitRecursion D] ⇒ the ∀A tight slice, so the recursion closes the ∀A
nonvanishing.

So the MATH GAP is closed; do NOT re-attack it via Route B (leading-coefficient tracking) — that
route hit the cyclic-trace-kills-commutator sub-wall and is superseded. The ONLY residual is the
LEAN INSTANCE (formalize the TL Markov-trace representation on tensor powers to discharge
BrunnianDeficitRecursion), which is DEFERRED with a documented feasibility roast: bricks 1-2 landed
(#6268, #6326), brick 3 roasted #6334 (docs/audits/2026-08-31-milnor-brick3-roast.md) — the instance
stays unfabricated (anti-laundering). Track the Lean side under qou-v7ro.


## Round 82 Execution Note (2026-11-17T10:13:44Z)

- **Status**: `in-progress` (PR awaiting merge; no unilateral closure).
- **PR**: [`litlfred/qou#8294`](https://github.com/litlfred/qou/pull/8294) (`feat/qou-b9cj-ck2w-k5r5-ndt5-x3iv-x631`, HEAD `22907bca8b5dd626221c15ea2658a1f14545c5be`).
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/PretzelSymmetryAdaptedGradingAndSubstrateBranchBrick.lean` (wired into `QOU.lean`, compiled with Lean 4.24.0, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/pretzel_symmetry_adapted_grading_and_substrate_branch_brick_probe.py` & `computations/probes/pretzel-symmetry-adapted-grading-and-substrate-branch-brick.witness.json` (`scriptCommitSha = caec3a2639d9338bfaf9aa9d455a0ab97b427071`, `scriptHash = 428700c5c7bd`, `outputHash = 27ee54e84b99cf035202cc1272490bd167d1f4ad8e861ae3bd043848cca760e3`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8294, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-08-31: "beans(qou-ck2w): cross-ref the recursion proof — math gap CLOSED, only Lean instance remains"). The work may be partly or fully done. Read the bean before you close it.
