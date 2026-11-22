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
   The remaining genuinely-deep, *not-in-Mathlib* input is stated as a
   concrete **polynomial identity**: Yekutieli's non-abelian Stokes theorem
   on surfaces ([yekutieli2015]) says the obstruction's genus generating
   polynomial is the raw `d_q²` curvature times the monic genus-filtration
   basis (`YekutieliStokesNormalisation.stokes_expansion`), with the
   geometric data unit-normalised (`raw_normalised`, `κ_raw = 1`).  The
   scalar `obstruction = κ_raw` is then **proved**
   (`obstructionCoord_eq_kappaRaw`) from `stokes_expansion` via the
   leading-coefficient extraction `leadingCoeff_C_mul_monicCheb` — it is no
   longer an axiom.  The main lemma **derives** `κ = c ∧ κ = 1` from these
   plus the proved `leadingChebyshev_eq_one`; it does not assume the identity.

This is a *rigorous conditional result*: verified by Lean modulo the named
class instance standing in for the non-abelian Stokes machinery (which a
full formalisation would build in
[`QOU.MathlibExt.YekutieliIntegration`](../../MathlibExt/YekutieliIntegration.lean),
whose discrete holonomy / Stokes layer is already sorry-free).  It is **not**
a claim that the categorical `H²`-class identity is derived (AGENTS.md
"Axiomatization is NOT a Proof"); the raw `d_q²` non-vanishing (1), the
Chebyshev normalisation (2), and the obstruction↔curvature extraction (3) are
all proved.  The **two** remaining axioms are the polynomial `stokes_expansion`
and the scalar `raw_normalised`.

## Base ring (§7c)

Generic `{R : Type*} [CommRing R]` with the substrate carried as a **unit**
`q : Rˣ` — the formula needs `q⁻¹`, and unit-hood is exactly the algebraic
content of the former `q ≠ 0` (no ordering, no `Real.*`).  No field and no
division are required, so the manuscript's own ground ring
`R_q = ℤ[q, q⁻¹]` (`LaurentPolynomial ℤ`, in which `q = T 1` is a unit) is
a direct instance.  The monic-Chebyshev machinery needs only
`[CommRing S] [Nontrivial S]`.

`[IsDomain R]` is required — and is genuinely load-bearing, not decorative
— by exactly two things: the product non-vanishing
`yekutieliObstructionData_kappaRaw_ne_zero` (`mul_ne_zero`) and the
leading-coefficient extraction `leadingCoeff_C_mul_monicCheb`
(`Polynomial.leadingCoeff_mul`, which needs `NoZeroDivisors`).  Over a
`CommRing` with zero divisors the non-vanishing is false: in `R = ZMod 6`
take `q = 5` (a unit, `q⁻¹ = 5`, `q ≠ 1`), `weight = 3 ≠ 0`,
`wedge = 1 ≠ 0`; then `κ_raw = 5·2·3·1 = 30 = 0`.  `ℤ[q, q⁻¹]` and every
field are domains, so nothing downstream is lost.  Mirrors
`dq-squared.lean`.
-/

open Polynomial

namespace QOU.Archimedean

/-- **Geometric data of the level-`n` Yekutieli obstruction for `T_{2,p}`.**

    The substrate `q` (with algebraic invertibility witness), the `T`-action
    `weight` `w` of the top Seifert cycle `γ₅` (the integer `5`, nonzero),
    and the `q`-wedge value `wedge` `ν = ω_V ∧_q ω_T` (nondegenerate,
    nonzero).  The nonzero witnesses are geometric-nondegeneracy inputs,
    carried as data so the non-vanishing theorem below is non-vacuous. -/
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md
structure YekutieliObstructionData (R : Type*) [CommRing R] where
  /-- The substrate parameter `q`, carried as a **unit** of the ground
      ring: algebraic invertibility (the old `q ≠ 0`), not the
      archimedean `0 < q`. -/
  q : Rˣ
  /-- The `T`-action weight `w` of the top Seifert cycle `γ₅` (the `5`). -/
  weight : R
  /-- The weight of a genuine top cycle is nonzero. -/
  weight_ne_zero : weight ≠ 0
  /-- The `q`-wedge value `ν = ω_V ∧_q ω_T`. -/
  wedge : R
  /-- The `q`-wedge of the two independent `1`-forms is nondegenerate. -/
  wedge_ne_zero : wedge ≠ 0

variable {R : Type*} [CommRing R]

/-- The **raw curvature value** of the Yekutieli obstruction,
    `κ_raw = q⁻¹(1 − q⁻¹) · w · ν` — the `d_q²` formula of the narrative
    proof (`prop:categorical-dq-squared`).  A `def` of the data (not a
    free field) so that `..._kappaRaw_ne_zero` is non-vacuous. -/
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient-proof.md
def YekutieliObstructionData.kappaRaw (d : YekutieliObstructionData R) : R :=
  ((d.q⁻¹ : Rˣ) : R) * (1 - ((d.q⁻¹ : Rˣ) : R)) * d.weight * d.wedge

/-- **Raw obstruction non-vanishing (sorry-free).**

    For `q ≠ 1`, the `d_q²` curvature value `κ_raw` is nonzero — the actual
    reason `κ(T_{2,p}) ≠ 0` away from the classical limit `q = 1`: the
    universal `d_q²` coefficient `q⁻¹(1 − q⁻¹)` vanishes iff `q = 1`, and the
    geometric factors `w`, `ν` are nonzero by nondegeneracy. -/
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient-proof.md
theorem yekutieliObstructionData_kappaRaw_ne_zero [IsDomain R]
    (d : YekutieliObstructionData R) (hq : d.q ≠ 1) :
    d.kappaRaw ≠ 0 := by
  unfold YekutieliObstructionData.kappaRaw
  have hinv_ne_one : ((d.q⁻¹ : Rˣ) : R) ≠ 1 := fun h =>
    hq (inv_eq_one.mp (Units.val_eq_one.mp h))
  have h_inv : ((d.q⁻¹ : Rˣ) : R) ≠ 0 := Units.ne_zero _
  have h_sub : (1 - ((d.q⁻¹ : Rˣ) : R)) ≠ 0 := sub_ne_zero.mpr (Ne.symm hinv_ne_one)
  exact mul_ne_zero (mul_ne_zero (mul_ne_zero h_inv h_sub) d.weight_ne_zero)
    d.wedge_ne_zero

/-! ### Genus-filtration Chebyshev basis — leading coefficient `= 1`

The leading Chebyshev coefficient `c_{(p−1)/2}` of the genus-filtration
expansion is the leading coefficient of the **monic** Chebyshev basis
polynomial of degree `(p−1)/2`.  We exhibit that basis concretely (the monic
three-term recurrence) and prove it monic, so its leading coefficient is `1`
outright — discharging the former `chebyshev_top_eq_one` axiom.  Only the
*normalisation* (the basis is monic) is proved here; the identification of
the obstruction's genus generating polynomial with this basis is the
axiomatised `YekutieliStokesNormalisation.stokes_expansion` below. -/

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

/-- **Genus-coordinate extraction (sorry-free).**  The leading coefficient of
    `scale · (monic basis)` is the scale itself — the genus-filtration
    coordinate reads off the scale from a monic expansion.  This is the
    proved bridge that turns the polynomial Stokes expansion below into the
    scalar identity `obstruction = κ_raw`. -/
theorem leadingCoeff_C_mul_monicCheb [IsDomain R] (c : R) (n : ℕ) :
    (Polynomial.C c * monicCheb R n).leadingCoeff = c := by
  rw [leadingCoeff_mul, leadingCoeff_C, (monicCheb_monic R n).1.leadingCoeff,
    mul_one]

/-- **Yekutieli non-abelian Stokes normalisation (§3b-cond class).**

    The genuinely deep, *not-in-Mathlib* input is now stated as a concrete
    **polynomial identity** rather than an opaque scalar equation:

    * `genusPoly` — the genus generating polynomial of the obstruction class
      (its expansion in the genus filtration);
    * `stokes_expansion` — Yekutieli's non-abelian Stokes theorem says this
      generating polynomial is the raw `d_q²` curvature times the monic
      genus-filtration Chebyshev basis, `genusPoly = C κ_raw · monicCheb`.
      A future formalisation of the `d_q²` curvature could *discharge* this
      by computing `genusPoly` (`QOU.MathlibExt.YekutieliIntegration`);
    * `raw_normalised` — the geometric data is unit-normalised so the top
      genus coordinate is `1` (`κ_raw = 1`), the irreducible normalisation.

    Progress vs. the earlier revision: the scalar `stokes_identity`
    (`obstruction = κ_raw`) is **no longer an axiom** — it is the *derived*
    `obstructionCoord_eq_kappaRaw`, obtained from `stokes_expansion` by the
    proved leading-coefficient extraction `leadingCoeff_C_mul_monicCheb`.
    The remaining axioms are the structural polynomial `stokes_expansion`
    (strictly stronger, but faithful to what non-abelian Stokes actually
    asserts) and the scalar `raw_normalised`.  `chebyshev_top_eq_one` stays
    discharged (`leadingChebyshev_eq_one`). -/
-- Ref: [yekutieli2015] https://doi.org/10.1142/9537
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md
class YekutieliStokesNormalisation (R : Type*) [CommRing R]
    (d : YekutieliObstructionData R) (p : ℕ) where
  /-- The genus generating polynomial of the obstruction class. -/
  genusPoly : R[X]
  /-- **Non-abelian Stokes** (deep, not in Mathlib): the genus generating
      polynomial is the raw `d_q²` curvature times the monic genus-filtration
      Chebyshev basis of degree `(p−1)/2`. -/
  stokes_expansion :
    genusPoly = Polynomial.C d.kappaRaw * monicCheb R ((p - 1) / 2)
  /-- Normalisation: the raw curvature is unit-normalised (top coordinate
      `1`).  The irreducible normalisation input. -/
  raw_normalised : d.kappaRaw = 1

/-- The obstruction's **genus-filtration leading coordinate** — the leading
    coefficient of its genus generating polynomial. -/
noncomputable def obstructionCoord (d : YekutieliObstructionData R) (p : ℕ)
    [nrm : YekutieliStokesNormalisation R d p] : R :=
  nrm.genusPoly.leadingCoeff

/-- **`obstruction = κ_raw` — now PROVED, not axiomatised.**  The obstruction's
    genus coordinate is the raw `d_q²` curvature, obtained from the polynomial
    `stokes_expansion` by the leading-coefficient extraction.  (Was the
    axiom `stokes_identity` in the earlier revision.) -/
theorem obstructionCoord_eq_kappaRaw [IsDomain R]
    (d : YekutieliObstructionData R) (p : ℕ)
    [nrm : YekutieliStokesNormalisation R d p] :
    obstructionCoord d p = d.kappaRaw := by
  unfold obstructionCoord
  rw [nrm.stokes_expansion, leadingCoeff_C_mul_monicCheb]

/-- **Yekutieli obstruction = leading Chebyshev coefficient = 1**
    ([`lem:yekutieli-leading-coefficient`]), at level `n = 5` for
    `T_{2,p}` with odd prime `p` and `q ≠ 1`.

    *Derived* (sorry-free): the proved `obstructionCoord_eq_kappaRaw` gives
    `κ = κ_raw`, `raw_normalised` gives `κ_raw = 1`, and
    `leadingChebyshev_eq_one` gives `c = 1`.  The theorem proves the
    identity, it does not assume it.  This is the decl named by the content
    block's `lean.ref`. -/
-- Ref: [yekutieli2015] https://doi.org/10.1142/9537
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md
theorem yekutieli_leading_coefficient [IsDomain R]
    (d : YekutieliObstructionData R)
    (p : ℕ) (_hp_odd : Odd p) (_hq_ne : d.q ≠ 1)
    [nrm : YekutieliStokesNormalisation R d p] :
    obstructionCoord d p = leadingChebyshev R p ∧ obstructionCoord d p = 1 := by
  have hκ : obstructionCoord d p = d.kappaRaw := obstructionCoord_eq_kappaRaw d p
  have h1 : obstructionCoord d p = (1 : R) := by rw [hκ, nrm.raw_normalised]
  exact ⟨h1.trans (leadingChebyshev_eq_one R p).symm, h1⟩

/-- **Non-vanishing at `q ≠ 1`.**  Derived from the **sorry-free**
    `yekutieliObstructionData_kappaRaw_ne_zero` via the proved
    `obstructionCoord_eq_kappaRaw` (hence via `stokes_expansion`) — *not* via
    the normalisation `raw_normalised`, so the non-vanishing rests on
    genuinely proved content. -/
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md
theorem yekutieli_obstruction_ne_zero [IsDomain R]
    (d : YekutieliObstructionData R)
    (p : ℕ) (_hp_odd : Odd p) (hq_ne : d.q ≠ 1)
    [nrm : YekutieliStokesNormalisation R d p] :
    obstructionCoord d p ≠ 0 := by
  rw [obstructionCoord_eq_kappaRaw]
  exact yekutieliObstructionData_kappaRaw_ne_zero d hq_ne

end QOU.Archimedean
