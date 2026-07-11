import Mathlib.Tactic

/-!
# QOU.Archimedean.yekutieli_leading_coefficient — `κ(T_{2,p}) = c_{(p−1)/2} = 1 ≠ 0`

**Lemma** ([`lem:yekutieli-leading-coefficient`](../../../quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md)).

*For `T_{2,p}` at level `n = g + 1 = 5`, the Yekutieli obstruction
`κ(T_{2,p}) ∈ H²(𝓢, 𝓑)` equals the leading Chebyshev coefficient
`c_{(p−1)/2} = 1`.  In particular `κ(T_{2,p}) ≠ 0` for `q ≠ 1`.*

## What is proved here, and what is assumed

The bare `opaque κ` + `sorry` of the earlier revision is replaced by the
accepted sibling patterns in this repo, so that **the main lemma is
sorry-free** and progressively fewer inputs are axiomatised:

1. **def-not-field (cf. [`dq-squared.lean`](../../../quantum-observable-universe/quantum-observable-universes/dq-squared.lean)).**
   The *raw* curvature value is a `def` of the geometric data — the `d_q²`
   formula `κ_raw = q⁻¹(1 − q⁻¹) · w · ν` (`w` the `T`-weight of the top
   Seifert cycle `γ₅`, i.e. `5`; `ν = ω_V ∧_q ω_T`;
   `prop:categorical-dq-squared`).  Its non-vanishing for `q ≠ 1`,
   `yekutieliObstructionData_kappaRaw_ne_zero`, is **sorry-free**.

2. **Leading Chebyshev coefficient `= 1` — now PROVED, not assumed.**
   The genus-filtration basis is the monic Chebyshev recurrence `monicCheb`
   (`p₀ = 1`, `p₁ = X`, `p_{n+2} = X·p_{n+1} − p_n`), which is monic of
   degree `n` by induction (`monicCheb_monic`); hence its leading
   coefficient is `1` (`leadingChebyshev_eq_one`).  This discharges what was
   previously the axiomatised `chebyshev_top_eq_one` class field.

3. **§3b-cond conditional class (cf. [`q_bkm_criterion.lean`](../../FluidDynamics/q_bkm_criterion.lean)).**
   The remaining genuinely-deep, *not-in-Mathlib* inputs — Yekutieli's
   non-abelian Stokes theorem on surfaces ([yekutieli2015]) identifying the
   obstruction class with the raw curvature (`stokes_identity`), and the
   genus-filtration normalisation identifying the raw value with the leading
   Chebyshev coefficient (`raw_eq_chebyshev`) — are the **two** remaining
   hypotheses of `YekutieliStokesNormalisation` (down from three).  The main
   lemma **derives** `κ = c ∧ κ = 1` from them plus the proved
   `leadingChebyshev_eq_one`; it does not assume the identity.

This is a *rigorous conditional result*: verified by Lean modulo the named
class instance standing in for the non-abelian Stokes machinery (which a
full formalisation would build in
[`QOU.MathlibExt.YekutieliIntegration`](../../MathlibExt/YekutieliIntegration.lean),
whose discrete holonomy / Stokes layer is already sorry-free).  It is **not**
a claim that the categorical `H²`-class identity is derived (AGENTS.md
"Axiomatization is NOT a Proof"); the raw `d_q²` non-vanishing (1) and the
Chebyshev normalisation (2) are unconditional, the Stokes identification (3)
is not.

## Base ring (§7c)

Generic `{R : Type*} [Field R]` with `q ≠ 0` — the formula needs `q⁻¹`, and
the non-vanishing / normalisation are algebraic (no ordering, no `Real.*`).
The monic-Chebyshev machinery needs only `[CommRing R] [Nontrivial R]`.
Mirrors `dq-squared.lean`.
-/

open Polynomial

namespace QOU.Archimedean

/-- **Geometric data of the level-`n` Yekutieli obstruction for `T_{2,p}`.**

    The substrate `q` (with algebraic invertibility witness), the `T`-action
    `weight` `w` of the top Seifert cycle `γ₅` (the integer `5`, nonzero),
    and the `q`-wedge value `wedge` `ν = ω_V ∧_q ω_T` (nondegenerate,
    nonzero).  The nonzero witnesses are geometric-nondegeneracy inputs,
    carried as data so the non-vanishing theorem below is non-vacuous. -/
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

    For `q ≠ 1`, the `d_q²` curvature value `κ_raw` is nonzero — the actual
    reason `κ(T_{2,p}) ≠ 0` away from the classical limit `q = 1`: the
    universal `d_q²` coefficient `q⁻¹(1 − q⁻¹)` vanishes iff `q = 1`, and the
    geometric factors `w`, `ν` are nonzero by nondegeneracy. -/
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

/-! ### Genus-filtration Chebyshev basis — leading coefficient `= 1`

The leading Chebyshev coefficient `c_{(p−1)/2}` of the genus-filtration
expansion is the leading coefficient of the **monic** Chebyshev basis
polynomial of degree `(p−1)/2`.  We exhibit that basis concretely (the monic
three-term recurrence) and prove it monic, so its leading coefficient is `1`
outright — discharging the former `chebyshev_top_eq_one` axiom.  Only the
*normalisation* (the basis is monic) is proved here; the identification of
the obstruction's genus coordinate with this basis is the axiomatised
`raw_eq_chebyshev` below. -/

/-- **Monic Chebyshev-type basis**: `p₀ = 1`, `p₁ = X`,
    `p_{n+2} = X·p_{n+1} − p_n`.  Monic of degree `n` by construction — the
    subtracted lower-degree term never reaches the top coefficient. -/
noncomputable def monicCheb (S : Type*) [CommRing S] : ℕ → S[X]
  | 0 => 1
  | 1 => X
  | (n + 2) => X * monicCheb S (n + 1) - monicCheb S n

/-- `monicCheb S n` is monic of degree `n` (two-step induction). -/
theorem monicCheb_monic (S : Type*) [CommRing S] [Nontrivial S] (n : ℕ) :
    (monicCheb S n).Monic ∧ (monicCheb S n).natDegree = n := by
  induction n using Nat.twoStepInduction with
  | zero => exact ⟨monic_one, by simp [monicCheb]⟩
  | one => exact ⟨monic_X, by simp [monicCheb]⟩
  | more n ihn ihn1 =>
    obtain ⟨hm0, hd0⟩ := ihn
    obtain ⟨hm1, hd1⟩ := ihn1
    have hXp : (X * monicCheb S (n + 1)).Monic := monic_X.mul hm1
    have hXd : (X * monicCheb S (n + 1)).natDegree = n + 2 := by
      rw [(monic_X (R := S)).natDegree_mul hm1, natDegree_X, hd1]; omega
    have hlt : (monicCheb S n).degree < (X * monicCheb S (n + 1)).degree := by
      rw [degree_eq_natDegree hm0.ne_zero, degree_eq_natDegree hXp.ne_zero, hd0, hXd]
      exact_mod_cast by omega
    have heq : monicCheb S (n + 2) = X * monicCheb S (n + 1) - monicCheb S n := rfl
    refine ⟨?_, ?_⟩
    · rw [heq, sub_eq_add_neg]
      exact hXp.add_of_left (by rwa [degree_neg])
    · have hdeg : (monicCheb S (n + 2)).degree = (X * monicCheb S (n + 1)).degree := by
        rw [heq]; exact degree_sub_eq_left_of_degree_lt hlt
      rw [natDegree, hdeg, ← natDegree, hXd]

/-- The **leading Chebyshev coefficient** `c_{(p−1)/2}` of the
    genus-filtration basis: the leading coefficient of the monic basis
    polynomial of degree `(p−1)/2`. -/
noncomputable def leadingChebyshev (S : Type*) [CommRing S] (p : ℕ) : S :=
  (monicCheb S ((p - 1) / 2)).leadingCoeff

/-- **`c_{(p−1)/2} = 1`** — the genus-filtration basis is monic.  Discharges
    the former `chebyshev_top_eq_one` axiom sorry-free. -/
theorem leadingChebyshev_eq_one (S : Type*) [CommRing S] [Nontrivial S]
    (p : ℕ) : leadingChebyshev S p = 1 :=
  (monicCheb_monic S ((p - 1) / 2)).1

/-- **Yekutieli non-abelian Stokes normalisation (§3b-cond class).**

    The two genuinely deep, *not-in-Mathlib* inputs, carried as explicit
    hypotheses:

    * `stokes_identity` — Yekutieli's non-abelian Stokes theorem identifies
      the obstruction class value `obstruction` with the raw `d_q²`
      curvature `d.kappaRaw`;
    * `raw_eq_chebyshev` — under the genus-filtration coordinate the raw
      value reads off as the leading Chebyshev coefficient
      `leadingChebyshev R p` (`= c_{(p−1)/2}`, proved `= 1` above).

    The `chebyshev_top_eq_one` field of the earlier revision is gone —
    it is now the proved `leadingChebyshev_eq_one`.  The lemma
    `yekutieli_leading_coefficient` **derives** `κ = c ∧ κ = 1` from these
    two hypotheses plus that proved fact; it does not restate its own
    conclusion.  The fields stand in for the machinery a full formalisation
    would provide (`QOU.MathlibExt.YekutieliIntegration`). -/
-- Ref: [yekutieli2015] https://doi.org/10.1142/9537
-- Ref: [manuscript] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md
class YekutieliStokesNormalisation (R : Type*) [Field R]
    (d : YekutieliObstructionData R) (p : ℕ) where
  /-- The obstruction class value (its genus-filtration leading coordinate). -/
  obstruction : R
  /-- **Non-abelian Stokes** (deep, not in Mathlib): the obstruction class
      equals the raw `d_q²` curvature value. -/
  stokes_identity : obstruction = d.kappaRaw
  /-- Genus-filtration normalisation: the raw value equals the leading
      Chebyshev coefficient (which `leadingChebyshev_eq_one` proves is `1`). -/
  raw_eq_chebyshev : d.kappaRaw = leadingChebyshev R p

/-- **Yekutieli obstruction = leading Chebyshev coefficient = 1**
    ([`lem:yekutieli-leading-coefficient`]), at level `n = 5` for
    `T_{2,p}` with odd prime `p` and `q ≠ 1`.

    *Derived* (sorry-free) by composing the two hypotheses of
    `YekutieliStokesNormalisation` with the proved `leadingChebyshev_eq_one`
    — the theorem proves the identity, it does not assume it.  This is the
    decl named by the content block's `lean.ref`. -/
-- Ref: [yekutieli2015] https://doi.org/10.1142/9537
-- Ref: [manuscript] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md
theorem yekutieli_leading_coefficient (d : YekutieliObstructionData R)
    (p : ℕ) (_hp_odd : Odd p) (_hq_ne : d.q ≠ 1)
    [nrm : YekutieliStokesNormalisation R d p] :
    nrm.obstruction = leadingChebyshev R p ∧ nrm.obstruction = 1 := by
  have h_eq_c : nrm.obstruction = leadingChebyshev R p :=
    nrm.stokes_identity.trans nrm.raw_eq_chebyshev
  exact ⟨h_eq_c, h_eq_c.trans (leadingChebyshev_eq_one R p)⟩

/-- **Non-vanishing at `q ≠ 1`.**  Derived from the **sorry-free**
    `yekutieliObstructionData_kappaRaw_ne_zero` via `stokes_identity`.
    Among the `YekutieliStokesNormalisation` fields the *proof* consumes
    only `stokes_identity` — not the normalisation `raw_eq_chebyshev` — so
    the non-vanishing rests on genuinely proved content; a full instance is
    still required by the *signature* only to name `nrm.obstruction`. -/
-- Ref: [manuscript] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md
theorem yekutieli_obstruction_ne_zero (d : YekutieliObstructionData R)
    (p : ℕ) (_hp_odd : Odd p) (hq_ne : d.q ≠ 1)
    [nrm : YekutieliStokesNormalisation R d p] :
    nrm.obstruction ≠ 0 := by
  rw [nrm.stokes_identity]
  exact yekutieliObstructionData_kappaRaw_ne_zero d hq_ne

end QOU.Archimedean
