---
# qou-c3if
title: 'PROVE(lean): exponent of convergence <= order (Hadamard PI-4), from Mathlib Jensen + counting'
status: in-progress
type: task
priority: normal
tags:
    - lean
    - hadamard
    - mathlib-gap
    - paper-qou
    - reorg-2026-10-04
created_at: 2026-08-08T03:30:00Z
updated_at: 2026-10-04T15:22:27Z
parent: qou-t5uj
---

## Why

For `f` entire of order `rho` with zeros `a_n`, Hadamard needs
`sum_n 1/|a_n|^{rho+eps} < infinity` for every eps > 0 — the exponent of
convergence is at most the order. That is what makes the genus `p <= rho` and
the canonical product converge (PI-3, already proved).

The route is Jensen's formula: `N(r) <= T(r) + O(1)` and the growth bound gives
`T(r) = O(r^rho)`, so the zero-counting function grows at most like `r^rho`, and
a summation-by-parts turns that into summability of `1/|a_n|^{rho+eps}`.

Jensen and the counting function are ALREADY IN MATHLIB (bean qou-bp5n), so this
is a derivation, not a build.

## Do

1. Settle qou-bp5n step 1 first — what `ValueDistribution.logCounting` unfolds to.
2. State `exponentOfConvergence_le_order` against
   `QOU.Mathlib.HadamardFactorization.IsEntireOfOrderLE`.
3. Prove, or reduce to a precisely-named missing lemma.

## ROAST

**"Closing this closes PI-5."** FALSE, and this is the trap. PI-5 needs at least
three things: (a) this bound, (b) the canonical product itself has order <= rho,
(c) the quotient `f / (exp(g)·prod)` is zero-free of finite order, hence
`exp(polynomial)` — which needs Borel-Carathéodory (qou-8cwi, done) plus a
Liouville-type argument. Closing (a) closes one of three. Do not report PI-5 as
"nearly done" on the strength of it.

**"`IsEntireOfOrderLE` is the standard order-of-growth hypothesis."** NO — and
this is the sharpest hit against the whole PI chain. The definition in
HadamardFactorization.lean is

    Differentiable C f  AND  exists A C, 0 < C AND forall z, ‖f z‖ <= A exp(C ‖z‖^rho)

That is **finite type with respect to order rho**, which is STRICTLY STRONGER
than "order <= rho". The classical Hadamard theorem hypothesises order <= rho,
i.e. for every eps > 0, `‖f z‖ <= exp(‖z‖^{rho+eps})` for large `‖z‖`. A
function of order exactly rho and infinite type (e.g. maximal type) satisfies
the classical hypothesis and NOT this one.

Consequences, both real:
  * the theorem as stated is TRUE but WEAKER than Hadamard;
  * the intended application (`phiBProd`, epic qou-lbth) must be checked against
    the STRONGER hypothesis. Nobody has done that. If phiBProd is of maximal
    type at its order, the whole chain proves something that does not apply.

Also loose: no `0 < A` is required, so `A <= 0` forces `f == 0`. Harmless where
`f 0 /= 0` is assumed, but the definition is not clean.

**Action item promoted from this roast:** before investing in PI-4/PI-5, verify
that `phiBProd` satisfies `IsEntireOfOrderLE` and not merely "order <= rho". If
it does not, the definition must be relaxed to the eps-form FIRST, and every
downstream statement re-checked.

---

## 2026-08-08 — the promoted action item was run. The answer is worse than "no".

The roast above ended: "before investing in PI-4/PI-5, verify that `phiBProd`
satisfies `IsEntireOfOrderLE` and not merely order <= rho."

**It satisfies neither. `phiBProd` is not entire at all.**

`QOU.MathlibExt.PhiBProd.phiBProd` is defined as a RATIO of two infinite
products, and the `k = 0` DENOMINATOR factor vanishes at an explicit point, for
EVERY `b /= 0` — including the substrate b. Proved sorry-free in
`QOU/Mathlib/HadamardApplicability.lean`:

    denFactor_eq_zero        denFactor b ((I*b/2)*(1 + 1/b^2)) 0 = 0
    denFactor_eq_zero_shift  ... and at every dual-period translate + m*I*b

`IsEntireOfOrderLE f rho` has `Differentiable C f` as its FIRST conjunct. So
`IsEntireOfOrderLE (phiBProd b) rho` is unavailable for every rho, and the
question of finite-type-vs-order-<=-rho — the whole point of the roast above —
never arises. The stronger/weaker hypothesis debate was downstream of an
assumption that fails one step earlier.

WHAT IS AND IS NOT PROVED, because the distinction matters:
  PROVED     a denominator FACTOR vanishes, explicitly, for every b /= 0.
  NOT PROVED that the denominator PRODUCT vanishes there (needs the
             multipliability hypotheses phiBProd's own theorems carry), nor that
             the numerator does not vanish to matching order and make the
             singularity removable. Neither is expected to fail; neither is
             checked. Hence the conclusion is stated as "entirety cannot be
             ASSUMED", not "phiBProd has a pole".

LIKELY REPAIR, recorded so it is not re-derived: each numFactor/denFactor is
entire in z, and for Im b^2 > 0 both products converge locally uniformly, so the
NUMERATOR and DENOMINATOR are separately entire. Hadamard applies to each of
them, not to their ratio. Whether the minimality principle survives that
reformulation is an open question, not a translation.

CONSEQUENCE FOR THIS BEAN AND FOR qou-v4if. PI-4 and PI-5 are not blocked — they
are fine theorems about entire functions — but the MOTIVATION stated at the top
of HadamardFactorization.lean does not connect them to phiBProd. Anyone
resuming should fix the motivation (or the target) BEFORE proving more of the
chain, or the chain will be finished and still not apply.

---

## 2026-08-08 (later) — the repair is PROVED, not just recorded.

The previous entry named the likely repair (Hadamard applies to the numerator
and denominator separately, each entire, never to their quotient). That is now
discharged in `QOU/Mathlib/HadamardApplicability.lean`, sorry-free:

    differentiable_tprod_one_add   entire factors + summable domination on every
                                   ball  ==>  z |-> prod' (1 + f n z) is entire
    differentiable_numProd         the numerator half is entire
    differentiable_denProd         the denominator half is entire

The general lemma stitches two Mathlib pieces that do not meet on their own:
`Summable.hasProdLocallyUniformlyOn_nat_one_add` (locally uniform multipliability
from a summable dominant) and `TendstoLocallyUniformlyOn.differentiableOn`
(holomorphy of locally uniform limits), then passes from "on every ball" to
entire, differentiability being local.

CONVERGENCE INPUT is carried as an explicit hypothesis rather than discharged.
That is not a dodge: PhiBProd.lean states the same discipline for its own
`Multipliable` inputs ("carried as explicit named hypotheses, not axiomatized and
not sorry'd") because they are the analytic geometric-bound facts for
Im b^2 > 0. The STRUCTURAL claim — that the halves are entire and the quotient is
not — is what was missing, and it is discharged.

STILL OPEN, and it is not a translation: whether the minimality principle that
motivated the chain survives being restated about the two halves instead of the
quotient. Nothing here implies it does.

## Round 70 Update (lane-e667)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Foundations/DyadicShellSummationCentralIdempotentFiberAdjointPlanarTransferPivotalMonoidality.lean`
- 80-dps mpmath probe: `computations/probes/dyadic_shell_summation_central_idempotent_fiber_adjoint_planar_transfer_pivotal_monoidality_probe.py`
- Witness: `computations/probes/dyadic-shell-summation-central-idempotent-fiber-adjoint-planar-transfer-pivotal-monoidality.witness.json` (`scriptHash = 65da05b0114c`, `scriptCommitSha = e3073696f062c7ba6a16becdc35a768b99bba3c2`)
- PR: https://github.com/litlfred/qou/pull/8382 (`eaf480ab4ed647b2e4dc199177fe5aeacf717fb8`)
