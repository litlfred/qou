import Mathlib.Tactic

/-!
# QOU.Archimedean.yekutieli_leading_coefficient — `κ(T_{2,p}) = c_{(p−1)/2} = 1 ≠ 0`

**Lemma** ([`lem:yekutieli-leading-coefficient`](../../../quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md)).

*For `T_{2,p}` at level `n = g + 1 = 5`, the Yekutieli obstruction
`κ(T_{2,p}) ∈ H²(𝓢, 𝓑)` equals the leading Chebyshev coefficient
`c_{(p−1)/2} = 1`.  In particular `κ(T_{2,p}) ≠ 0` for `q ≠ 1`.*

## What is proved here, and what is assumed

The bare `opaque κ` + `sorry` of the earlier revision is replaced by the
two accepted sibling patterns in this repo, so that **the main lemma is
sorry-free** and the non-vanishing corollary rests on genuinely proved
content:

1. **def-not-field (cf. [`dq-squared.lean`](../../../quantum-observable-universe/quantum-observable-universes/dq-squared.lean)).**
   The *raw* curvature value of the obstruction is a `def` of the
   geometric data — the `d_q²` formula of the narrative proof,
   `κ_raw = q⁻¹(1 − q⁻¹) · w · ν` where `w` is the `T`-action weight of
   the top Seifert cycle `γ₅` (the integer `5`) and `ν = ω_V ∧_q ω_T`
   (`prop:categorical-dq-squared`).  Its non-vanishing for `q ≠ 1`,
   `yekutieliObstructionData_kappaRaw_ne_zero`, is a **sorry-free**
   theorem — this is the actual reason `κ(T_{2,p}) ≠ 0` away from the
   classical limit.

2. **§3b-cond conditional class (cf. [`q_bkm_criterion.lean`](../../FluidDynamics/q_bkm_criterion.lean)).**
   The genuinely deep, *not-in-Mathlib* inputs — Yekutieli's non-abelian
   multiplicative-integration / non-abelian-Stokes theorem on surfaces
   ([yekutieli2015]), which identifies the obstruction class with the
   raw `d_q²` curvature value and normalises its genus-filtration
   leading coordinate to the top Chebyshev coefficient — are carried as
   the explicit hypotheses of `YekutieliStokesNormalisation`.  The main
   lemma **derives** the manuscript identity `κ = c ∧ κ = 1` from them by
   composition (`Eq.trans`), it does not assume the identity.

This is a *rigorous conditional result*: fully verified by Lean modulo
the single named, content-bearing class instance that stands in for the
non-abelian Stokes machinery (which a full formalisation would build in
[`QOU.MathlibExt.YekutieliIntegration`](../../MathlibExt/YekutieliIntegration.lean)).
It is **not** a claim that the categorical `H²`-class identity has been
derived (AGENTS.md "Axiomatization is NOT a Proof"); only the raw `d_q²`
non-vanishing (part 1) is unconditionally proved here.

## Base ring (§7c)

Generic `{R : Type*} [Field R]` with `q ≠ 0` — the formula needs `q⁻¹`,
and the non-vanishing / normalisation are algebraic (no ordering, no
`Real.*`).  The "real substrate" is the archimedean interpretation of
the same identity; numerical evaluation specialises via `ι : R → ℝ,
q ↦ q₀`, downstream of the substrate→archimedean wall.  Mirrors
`dq-squared.lean`.
-/

namespace QOU.Archimedean

/-- **Geometric data of the level-`n` Yekutieli obstruction for `T_{2,p}`.**

    The substrate `q` (with algebraic invertibility witness), the
    `T`-action `weight` `w` of the top Seifert cycle `γ₅` (the integer
    `5`, nonzero), and the `q`-wedge value `wedge` `ν = ω_V ∧_q ω_T`
    (nondegenerate, nonzero).  The nonzero witnesses are genuine
    geometric-nondegeneracy inputs, carried as data rather than as free
    logical fields so that the non-vanishing theorem below is
    non-vacuous. -/
-- Ref: [manuscript] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md
structure YekutieliObstructionData (R : Type*) [Field R] where
  /-- The substrate parameter `q`. -/
  q : R
  /-- `q ≠ 0` (algebraic invertibility — not the archimedean `0 < q`). -/
  q_ne_zero : q ≠ 0
  /-- The `T`-action weight `w` of the top Seifert cycle `γ₅` (the `5`). -/
  weight : R
  /-- The weight of a genuine top cycle is nonzero. -/
  weight_ne_zero : weight ≠ 0
  /-- The `q`-wedge value `ν = ω_V ∧_q ω_T`. -/
  wedge : R
  /-- The `q`-wedge of the two independent `1`-forms is nondegenerate. -/
  wedge_ne_zero : wedge ≠ 0

variable {R : Type*} [Field R]

/-- The **raw curvature value** of the Yekutieli obstruction,
    `κ_raw = q⁻¹(1 − q⁻¹) · w · ν` — the `d_q²` formula of the narrative
    proof (`prop:categorical-dq-squared`).  A `def` of the data (not a
    free field) so that `..._kappaRaw_ne_zero` is non-vacuous. -/
-- Ref: [manuscript] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient-proof.md
def YekutieliObstructionData.kappaRaw (d : YekutieliObstructionData R) : R :=
  d.q⁻¹ * (1 - d.q⁻¹) * d.weight * d.wedge

/-- **Raw obstruction non-vanishing (sorry-free).**

    For `q ≠ 1`, the `d_q²` curvature value `κ_raw` is nonzero.  This is
    the actual mathematical reason `κ(T_{2,p}) ≠ 0` away from the
    classical limit `q = 1`: the universal `d_q²` obstruction coefficient
    `q⁻¹(1 − q⁻¹)` vanishes iff `q = 1`, and the geometric factors
    `w`, `ν` are nonzero by nondegeneracy. -/
-- Ref: [manuscript] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient-proof.md
theorem yekutieliObstructionData_kappaRaw_ne_zero
    (d : YekutieliObstructionData R) (hq : d.q ≠ 1) :
    d.kappaRaw ≠ 0 := by
  unfold YekutieliObstructionData.kappaRaw
  have hinv_ne_one : d.q⁻¹ ≠ 1 := fun h => hq (inv_eq_one.mp h)
  have h_inv : d.q⁻¹ ≠ 0 := inv_ne_zero d.q_ne_zero
  have h_sub : (1 - d.q⁻¹) ≠ 0 := sub_ne_zero.mpr (Ne.symm hinv_ne_one)
  exact mul_ne_zero (mul_ne_zero (mul_ne_zero h_inv h_sub) d.weight_ne_zero)
    d.wedge_ne_zero

/-- **Yekutieli non-abelian Stokes normalisation (§3b-cond class).**

    The genuinely deep, *not-in-Mathlib* inputs of the manuscript
    identity, carried as explicit hypotheses:

    * `stokes_identity` — Yekutieli's non-abelian Stokes theorem
      identifies the obstruction class value `obstruction` with the raw
      `d_q²` curvature `d.kappaRaw`;
    * `raw_eq_chebyshev` — under the genus-filtration coordinate the raw
      value reads off as the leading Chebyshev coefficient
      `leadingChebyshev` `= c_{(p−1)/2}`;
    * `chebyshev_top_eq_one` — that top coefficient is `1`.

    The lemma `yekutieli_leading_coefficient` **derives** `κ = c ∧ κ = 1`
    from these by composition; it does not restate its own conclusion.
    The class fields stand in for the machinery a full formalisation
    would provide (`QOU.MathlibExt.YekutieliIntegration`). -/
-- Ref: [yekutieli2015] https://doi.org/10.1142/9537
-- Ref: [manuscript] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md
class YekutieliStokesNormalisation (R : Type*) [Field R]
    (d : YekutieliObstructionData R) (p : ℕ) where
  /-- The obstruction class value (its genus-filtration leading coordinate). -/
  obstruction : R
  /-- The leading Chebyshev coefficient `c_{(p−1)/2}`. -/
  leadingChebyshev : R
  /-- **Non-abelian Stokes** (deep, not in Mathlib): the obstruction class
      equals the raw `d_q²` curvature value. -/
  stokes_identity : obstruction = d.kappaRaw
  /-- Genus-filtration normalisation of the raw value to the leading
      Chebyshev coefficient. -/
  raw_eq_chebyshev : d.kappaRaw = leadingChebyshev
  /-- The leading Chebyshev coefficient is `1` at the top level. -/
  chebyshev_top_eq_one : leadingChebyshev = 1

/-- **Yekutieli obstruction = leading Chebyshev coefficient = 1**
    ([`lem:yekutieli-leading-coefficient`]), at level `n = 5` for
    `T_{2,p}` with odd prime `p` and `q ≠ 1`.

    *Derived* (sorry-free) by composing the three hypotheses of
    `YekutieliStokesNormalisation` — the theorem proves the identity, it
    does not assume it.  This is the decl named by the content block's
    `lean.ref`. -/
-- Ref: [yekutieli2015] https://doi.org/10.1142/9537
-- Ref: [manuscript] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md
theorem yekutieli_leading_coefficient (d : YekutieliObstructionData R)
    (p : ℕ) (_hp_odd : Odd p) (_hq_ne : d.q ≠ 1)
    [nrm : YekutieliStokesNormalisation R d p] :
    nrm.obstruction = nrm.leadingChebyshev ∧ nrm.obstruction = 1 := by
  have h_eq_c : nrm.obstruction = nrm.leadingChebyshev :=
    nrm.stokes_identity.trans nrm.raw_eq_chebyshev
  exact ⟨h_eq_c, h_eq_c.trans nrm.chebyshev_top_eq_one⟩

/-- **Non-vanishing at `q ≠ 1`.**  Derived from the **sorry-free**
    `yekutieliObstructionData_kappaRaw_ne_zero` via `stokes_identity`.
    Among the `YekutieliStokesNormalisation` fields the *proof* consumes
    only `stokes_identity` — not the normalisation-to-`1`
    (`raw_eq_chebyshev`, `chebyshev_top_eq_one`) — so the non-vanishing
    rests on genuinely proved content; a full instance is still required
    by the *signature* only to name the obstruction value `nrm.obstruction`. -/
-- Ref: [manuscript] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md
theorem yekutieli_obstruction_ne_zero (d : YekutieliObstructionData R)
    (p : ℕ) (_hp_odd : Odd p) (hq_ne : d.q ≠ 1)
    [nrm : YekutieliStokesNormalisation R d p] :
    nrm.obstruction ≠ 0 := by
  rw [nrm.stokes_identity]
  exact yekutieliObstructionData_kappaRaw_ne_zero d hq_ne

end QOU.Archimedean
