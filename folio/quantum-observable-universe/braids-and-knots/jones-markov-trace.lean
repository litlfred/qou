import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.List.Basic
import Mathlib.Tactic
import QOU.Machinery.HeckeH3AlgebraLaws


/-!
# QOU.Braiding.JonesMarkovTrace — Markov trace axiom (Jones, 1987)

External proof axiom encoding the existence and non-degeneracy of the
Markov trace on the Hecke algebra tower, following the Yekutieli pattern:
the result is stated as a Lean `structure` whose fields capture the three
properties from Jones (1987) Theorem 5.1 and Corollary 5.3, with the
proof taken as axiomatic.

This is the Fields Medal result on which knot eigenbasis completeness
depends. The proof occupies §3–5 of:

  V.F.R. Jones, "Hecke Algebra Representations of Braid Groups and
  Link Polynomials", Annals of Mathematics 126 (1987), 335–388.

LaTeX label: `thm:jones-markov-trace`

## References

- [jones1987] https://doi.org/10.2307/1971403
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2, Ch. XII

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Braiding

-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
-- See `QOU.Archimedean.GroundRing` for the compiled definition.
abbrev R_q := LaurentPolynomial ℤ

/-- The canonical indeterminate `q = T^1` of `R_q`. -/
noncomputable def q_param : R_q := LaurentPolynomial.T 1

/-- The formal Laurent inverse `q⁻¹ = T^{-1}` of `R_q`. -/
noncomputable def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-! ## Hecke Algebra (minimal, for self-containment) -/

/-- Minimal Hecke algebra data needed for the Markov trace axiom.
    The full structure is in `knot-eigenbasis-complete.lean`; this
    extracts only what the Jones theorem requires. -/
structure HeckeAlgebraData where
  /-- Number of strands. -/
  n : ℕ
  /-- Carrier type of H_n(q). -/
  carrier : Type*
  /-- Deformation parameter q. -/
  q : R_q
  -- q > 0.
  -- q_pos : 0 < q  -- (archimedean; not meaningful over R_q)
  /-- q ≠ 1. -/
  q_ne_one : q ≠ 1
  -- q is not a root of unity.
  -- q_not_root_of_unity : ∀ k : ℕ, k ≥ 1 → q ^ k ≠ 1  -- (archimedean; not meaningful over R_q)
  /-- Multiplication. -/
  mul : carrier → carrier → carrier
  /-- Unit element. -/
  one : carrier
  /-- Generators T_1, ..., T_{n-1}. -/
  T : Fin (n - 1) → carrier

/-! ## Jones–Markov Trace Axiom -/

/-- **Jones–Markov Trace** (Jones, 1987, Theorem 5.1 & Corollary 5.3).

    External proof axiom: for each Hecke algebra H_n(q) with q not a
    root of unity, there exists a unique trace functional satisfying
    the Markov property, which is non-degenerate on every irreducible
    summand.

    We encode this as a structure whose fields are the properties
    proved in Jones (1987). The proof is taken as axiomatic — the
    `sorry` marks where Jones's 54-page proof would go.

    **Three key properties:**
    1. **Existence & uniqueness**: a trace satisfying normalisation,
       cyclicity, and the Markov property tr(x T_n) = z tr(x); the
       negative stabilisation tr(x T_n⁻¹) = z₋ tr(x),
       z₋ = z − (q − q⁻¹), is forced by the Hecke quadratic relation.
    2. **Non-degeneracy**: the trace is nonzero on every irreducible
       H_n(q)-module S_λ.
    3. **Link invariance**: the trace value depends only on the isotopy
       class of the braid closure, yielding the Jones polynomial. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
structure JonesMarkovTrace (H : HeckeAlgebraData) where
  /-- The trace functional tr_M : H_n(q) → ℝ. -/
  tr : H.carrier → R_q

  -- ### Property 1: Normalisation and trace axioms

  /-- Normalisation: tr(1) = 1. -/
  tr_one : tr H.one = 1

  /-- Trace property (cyclicity): tr(ab) = tr(ba). -/
  tr_comm : ∀ (a b : H.carrier), tr (H.mul a b) = tr (H.mul b a)

  /-- Markov-trace loop value `z = tr_M(σ_i)`. The canonical value is
      convention D, `z = q³/(q² + 1)` (owner ruling 2026-08-15), which
      is what the `.md` statement fixes. This structure leaves `z` free:
      the pin is **not** encoded here, so nothing proved from this
      structure depends on convention D. -/
  z : R_q

  /-- The Markov parameter is nonzero. -/
  z_ne_zero : z ≠ 0

  /-- **Markov property** (positive stabilisation):
      tr(x · T_{n-1}) = z · tr(x) for x ∈ H_n(q).
      This encodes vertical stabilisation in the Hecke tower. -/
  markov_pos : ∀ (hn : H.n ≥ 2) (x : H.carrier),
      let last : Fin (H.n - 1) := ⟨H.n - 2, by omega⟩
      tr (H.mul x (H.T last)) = z * tr x

  -- ### Property 2: Non-degeneracy on irreducibles

  /-- Number of irreducible summands at level n (= ⌊n/2⌋ + 1 for SU_q(2)). -/
  numIrreps : ℕ

  /-- **Non-degeneracy (weak form)**: the trace is not identically zero.
      The index `i` does not enter the body, so this field says only that
      some element has nonzero trace; it does **not** encode "nonzero on
      every irreducible `S_λ`". That stronger reading would also be false
      under convention D, where the Ocneanu weight of every shape with a
      third row vanishes. A per-`S_λ` statement needs the Wedderburn
      decomposition, which this structure does not carry. -/
  -- Ref: [jones1987] Corollary 5.3
  nondeg : ∀ (i : Fin numIrreps), ∃ (a : H.carrier), tr a ≠ 0

  -- ### Property 3: Link invariance

  /-- Negative-crossing loop value `z₋ = z − (q − q⁻¹)`.

      Forced by linearity and the Hecke quadratic relation
      σ⁻¹ = σ − (q − q⁻¹): substituting into `markov_pos` gives
      tr(x·T⁻¹) = (z − (q − q⁻¹))·tr(x). Note z₋ ≠ z for q ≠ ±1,
      and z₋ is NOT z⁻¹ — the two stabilisations do not scale by
      mutually inverse factors for any non-degenerate trace
      parameter (z·z₋ = 1 forces z ∈ {q, −q⁻¹}, the two
      one-dimensional characters). Link invariance is restored by
      the writhe prefactor outside the trace (Jones 1987 §5), not
      by ±-symmetry of the trace. -/
  z_neg : R_q

  /-- `z_neg` is pinned to its Hecke-forced value z − (q − q⁻¹). -/
  z_neg_spec : z_neg = z - (q_param - q_inv_param)

  /-- **Negative stabilisation (Markov II input)**:
      tr(x · T_{n-1}⁻¹) = z₋ · tr(x) with z₋ = z − (q − q⁻¹).
      Combined with tr_comm (Markov I), markov_pos, and the
      writhe-normalisation prefactor of Jones 1987 §5, this ensures
      the normalised invariant depends only on the isotopy class of
      the braid closure, yielding the Jones polynomial J_L(q). -/
  -- Ref: [jones1987] Theorem 5.1 + §5 (writhe normalisation)
  markov_neg : ∀ (hn : H.n ≥ 2) (x T_inv : H.carrier),
      let last : Fin (H.n - 1) := ⟨H.n - 2, by omega⟩
      -- T_inv must be the two-sided Hecke-algebra inverse of the last
      -- generator; without this constraint the field would assert the
      -- scaling for EVERY element (T_inv = 0 would force tr ≡ 0,
      -- contradicting nondeg).
      H.mul (H.T last) T_inv = H.one →
      H.mul T_inv (H.T last) = H.one →
      tr (H.mul x T_inv) = z_neg * tr x

/-! ## The former existence axiom was false

`jones_markov_trace_exists : ∀ H : HeckeAlgebraData, JonesMarkovTrace H` was
removed 2026-11-15, together with its three consequences (`markov_trace_one`,
`markov_z_ne_zero`, `all_irreps_detected`), which used nothing else.

Jones's theorem is true for the Hecke algebra, but `HeckeAlgebraData` carries
no relations: `mul`, `one` and `T` are arbitrary. On the one-point carrier,
`markov_pos` forces `z = 1` and `markov_neg` forces `z₋ = 1`, while
`z_neg_spec` says `z₋ = z − (q − q⁻¹)` with `q − q⁻¹ ≠ 0` in `ℤ[q, q⁻¹]`.
A correct statement needs the Hecke relations as fields of the data (or the
concrete `H₃` trace `QOU.Machinery.H3.trM`, which is proved); recorded as open
in bean `qou-n2un`. -/

/-- `q ≠ q⁻¹` in `R_q = ℤ[q, q⁻¹]`. -/
theorem q_param_ne_q_inv_param : q_param ≠ q_inv_param := by
  intro h
  have h' : (Finsupp.single (1:ℤ) (1:ℤ) : ℤ →₀ ℤ) = Finsupp.single (-1) 1 := h
  have := (Finsupp.single_left_inj one_ne_zero).mp h'
  omega

/-- **No Jones–Markov trace exists on unconstrained `HeckeAlgebraData`.** -/
-- Ref: [jones1987] §3 (The Markov trace), Theorem 5.1
theorem not_forall_jonesMarkovTrace :
    ¬ ∀ H : HeckeAlgebraData.{0}, Nonempty (JonesMarkovTrace H) := by
  intro hall
  let H : HeckeAlgebraData :=
    { n := 2, carrier := Unit, q := 0, q_ne_one := zero_ne_one, mul := fun _ _ => (),
      one := (), T := fun _ => () }
  obtain ⟨J⟩ := hall H
  have h1 : J.tr () = 1 := J.tr_one
  have hp := J.markov_pos le_rfl ()
  have hn := J.markov_neg le_rfl () () rfl rfl
  have hs := J.z_neg_spec
  simp only [H, h1, mul_one] at hp hn
  have hT : q_param - q_inv_param = 0 := by
    have : J.z_neg = J.z := by rw [← hn, ← hp]
    rw [hs] at this; linear_combination -this
  exact q_param_ne_q_inv_param (sub_eq_zero.mp hT)


/-! ## Repaired form at n = 3 (option B, 2026-11-15)

The removed axiom quantified over `HeckeAlgebraData`, which has no Hecke
relations. On the concrete normal-form model of `H₃(q)`
(`QOU.Machinery.H3`, where the Hecke quadratic and braid relation are proved)
the Jones–Markov properties hold. The statement below is over a generic
commutative ring, with `h = q − q⁻¹` and a free Markov parameter `z`.

The Markov property is stated for `x ∈ H₂` (the NF vectors supported on
`γ, σ₀`), as in Jones's theorem. The removed `markov_pos` field quantified
over all of `H_n`, which is too strong: it forces `z` to be a root of
`z² − h z − 1`, i.e. one of the two one-dimensional characters. -/

section H3Repair

open QOU.Machinery.H3

variable {R : Type*} [CommRing R]

/-- `x · σ₁⁻¹` on the NF module, using `σ₁⁻¹ = σ₁ − h`. -/
def mulσ₁Inv (h : R) (v : Fin 6 → R) : Fin 6 → R := mulσ₁ h v - h • v

/-- `σ₁⁻¹ = σ₁ − h` is a right inverse of `σ₁`: `(x σ₁⁻¹) σ₁ = x`. -/
theorem mulσ₁_mulσ₁Inv (h : R) (v : Fin 6 → R) : mulσ₁ h (mulσ₁Inv h v) = v := by
  funext i
  fin_cases i <;> simp [mulσ₁Inv, mulσ₁] <;> ring

/-- **Jones–Markov trace on `H₃(q)`** (repaired form, sorry-free):
    normalisation, cyclicity, the Markov property on `H₂`, and the negative
    stabilisation with `z₋ = z − h`. -/
-- Ref: [jones1987] Theorem 5.1
theorem jonesMarkov_H3 (z h : R) :
    trM z h unitNF = 1 ∧
    (∀ u v, trM z h (mulNF h u v) = trM z h (mulNF h v u)) ∧
    (∀ v : Fin 6 → R, v 2 = 0 → v 3 = 0 → v 4 = 0 → v 5 = 0 →
      trM z h (mulσ₁ h v) = z * trM z h v) ∧
    (∀ v : Fin 6 → R, v 2 = 0 → v 3 = 0 → v 4 = 0 → v 5 = 0 →
      trM z h (mulσ₁Inv h v) = (z - h) * trM z h v) := by
  refine ⟨?_, trM_cyclic z h, fun v h2 h3 h4 h5 => trM_markov_σ₁ z h v h2 h3 h4 h5, ?_⟩
  · simp [trM, unitNF, TRM, Fin.sum_univ_six]
  · intro v h2 h3 h4 h5
    have hs : trM z h (h • v) = h * trM z h v := trM_smul z h h v
    have ha := trM_add z h (mulσ₁Inv h v) (h • v)
    rw [mulσ₁Inv, sub_add_cancel, trM_markov_σ₁ z h v h2 h3 h4 h5, hs] at ha
    rw [mulσ₁Inv]
    linear_combination -ha

end H3Repair

end QOU.Braiding
