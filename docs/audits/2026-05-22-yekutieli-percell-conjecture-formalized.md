# Yekutieli per-cell curvature for λ_scale — load-bearing conjecture, formalised

**Date:** 2026-05-22 (evening)
**Branch:** `claude/lambda-scale-alts-strategy-d-2026-05-22`
**Status:** Conjecture statement made falsifiable; numerical test designed; no proof.

## Context

After PR #895 settled `λ_scale := λ_A(q) = 5/2 + (3/4)·h²` (Family A,
proved theorem) as the framework's substrate value with ~3% residual
to CODATA, and after the q-dilog Tier 0 / Tier 1+ basis-extension
searches all came up negative
([af2d27ee on main](https://github.com/litlfred/qou/commit/af2d27ee52b7ecde5fddd624010a6ee59208573d) /
[PR #928](https://github.com/litlfred/qou/pull/928) /
[PR #916 commit e64b2806](https://github.com/litlfred/qou/commit/e64b2806)), the
remaining substrate-pure-research direction is the
**Yekutieli per-cell curvature** structural argument from
[`docs/audits/2026-05-18-conjecture-proof-step3-yekutieli.md`](2026-05-18-conjecture-proof-step3-yekutieli.md).

That audit ("Step 3") argues `λ_scale = 5/2 − G·h² + O(h⁴)` from
the categorical non-abelian Stokes (Yekutieli 2015) integrated over
𝓑_3's 8-fold ideal-octahedral tessellation. It is **structurally
distinct** from PR #701's falsified Wedderburn-sum search: the
trace on which Yekutieli acts is the **half-symmetric Markov trace
on the H_4 stabilization of β_Bor**, not a sum of `dim_q V_λ` over
partitions. PR #701's falsification of `5/2 − h²·G` only rules
out the *Wedderburn-sum* incarnation of that form.

## The load-bearing conjecture (formalised)

The Yekutieli audit Step 3 has one provably-true input (5/2 leading,
from Step 2 enumeration), one standard-differential-geometry input
(curvature = hyperbolic volume), one derived input (Vol(𝓑_3) = 8G
from Adams 1985), and **one load-bearing conjecture** the audit
itself flags:

**Conjecture (cell-extraction-by-half-symmetric-projection).**
*Let `Π_HS : H_4(q) → H_4(q)` be the half-symmetric Wedderburn
projection (the projection onto the (1/2)·Σ_{λ:λ=λ^t}-symmetric
sub-algebra at H_4). The non-abelian-multiplicative-integral of
the q-deformation curvature 2-form across the Borromean ribbon
surface, restricted via `Π_HS`, extracts the curvature contribution
of exactly **one** of the 8 ideal octahedral cells in the
𝓑_3-complement tessellation, in the q → 1 expansion to second
order.*

Stated symbolically:

```
τ^{(2)}_{half-sym}(β_Bor)  :=  (1/2) · d²/dq² |_{q=1} [ Π_HS ∘ τ_q ] (β_Bor)
                            =  -G   ( = -Vol(𝓑_3) / 8 )
```

with the right-hand side being the per-cell hyperbolic volume of
**one** of the 8 ideal octahedra (sign by the absorption convention
in [Yekutieli, 2015]).

## Where the conjecture comes from

The audit's structural sketch:

| Wedderburn block (λ ⊢ 4) | conj | Octahedral cell type |
|---|---|---|
| (4), (1,1,1,1) | conjugate pair | "vertex" octahedra (2 of 8) |
| (3,1), (2,1,1) | conjugate pair | "edge" octahedra (4 of 8) |
| (2,2) | self-conjugate | "center" octahedron (1 of 8, ×2 multiplicity?) |

Total: 2 + 4 + 1 = 7 (or 8 if (2,2) is counted with its
self-conjugate doubling) octahedra. Half-symmetric Π_HS sums
conjugate-pair contributions WITH A SYMMETRIC factor of (1/2);
the self-conjugate (2,2) is fixed. The conjecture is that the
weighted sum (1/2)(2 + 4) + (1·2)/2 = 1 + 2 + 1 = 4 of cells
extracts... wait, the audit text claims **ONE** cell. There is
an unresolved combinatorial step here (the audit's §5 says "the
half-symmetric projection extracts ONE conjugate-pair sum out of
the 8-fold tessellation"; the bijection in §"Concrete next R&D"
allocates the 8 cells differently).

This is exactly the "load-bearing **and** still-not-rigorous" step
the audit acknowledges.

## A falsifiable numerical test

The conjecture as stated would imply:

  `τ_{half-sym}(β_Bor)(q_0) = 5/2 − G · h²(q_0) + O(h⁴)`
  `                          ≈ 2.4599666078...`

vs the CODATA-derived closure target `2.4599527869...` (the
historical empirical match from `docs/audits/2026-05-18-lambda-scale-derivation-search.md`).

If a CONCRETE H_4 half-symmetric Markov trace operator can be
defined and `τ_{half-sym}(β_Bor)(q_0)` computed at MPFR-50dps, the
result is either:

1. **Matches `5/2 − G · h²` to within MPFR floor** ⇒ strong
   empirical support for the Yekutieli structural argument
   (proof still requires the explicit cell-↔-projection bijection
   construction the audit §"Concrete next R&D" lists).
2. **Matches `5/2 − G · h²` to within 5.6 ppm but not to MPFR
   floor** ⇒ same empirical match as the historical numerical
   coincidence — Yekutieli argument's leading-order claim is
   consistent but the h^4 corrections matter (not surprising;
   audit explicitly notes the residual is at h^4 order).
3. **Mismatches at first order** ⇒ the Yekutieli derivation has
   a load-bearing bug in either the bijection counting or the
   non-abelian Stokes identification; treat as falsified pending
   a corrected formulation.

The probe `lambda_scale_alt_i_yekutieli_halfsym_trace_test.py` (in
this commit) defines `Π_HS` as the natural conjugate-pair-symmetric
projection on the H_4 Wedderburn weights `y_λ` and computes the
resulting "half-symmetric trace" on the H_4 Markov stabilization
of β_Bor.

## What this commit does NOT do

- **No proof.** Outcome 1 above would still be empirical evidence,
  not categorical proof. The audit's §"Concrete next R&D" item 1
  (explicit cell-↔-projection bijection) is the required theory work.
- **No Lean formalisation.** Mathlib lacks the non-abelian
  multiplicative integral primitive
  ([audit §4 R&D item 4](2026-05-18-conjecture-proof-step3-yekutieli.md)
  classifies this as a long-term dependency).
- **No production wiring.** Family A (per #895) remains the
  framework's substrate λ_scale. If outcome 1 lands, a follow-up
  PR would propose updating production to `5/2 − G·h²` ONLY after
  the categorical bijection step is rigorously closed.

## Cross-references

- [`docs/audits/2026-05-18-conjecture-proof-step3-yekutieli.md`](2026-05-18-conjecture-proof-step3-yekutieli.md) — Step 3 structural argument (May 18)
- [`prop:yekutieli-stokes-mass`](../../content/quantum-observable-universe/lifting-and-descent/) — categorical Stokes block family
- [`docs/audits/2026-05-22-q-dilog-tower-spike-lambda-scale.md`](2026-05-22-q-dilog-tower-spike-lambda-scale.md) — q-dilog Tier 0 negative (af2d27ee on main)
- [PR #928](https://github.com/litlfred/qou/pull/928) — q-dilog Tier 1+ negative (|V̂_S| + Q(ζ_60) + knot vols, coeff 10³⁰)
- [`docs/agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md`](../agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md) §Recommended ordering — Yekutieli (Strategy I) is the #2 priority after the q-dilog Tier 1+ extensions (now exhausted).
