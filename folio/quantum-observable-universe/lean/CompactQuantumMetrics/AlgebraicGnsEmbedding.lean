import Mathlib.Tactic
import Mathlib.Analysis.InnerProductSpace.Basic

/-!
# QOU.Observations.AlgebraicGnsEmbedding

The Markov-trace GNS embedding `H_∞(q) ↪ L(H)`, encoded as a
typeclass packaging the four ingredients of the construction.

Unlike `MuArchContinuumLimit`, the GNS construction is **not
conjectural**: it is the Jones–Wenzl subfactor machinery
([jones1985], [wenzl1988]). Under convention D the trace factors through
Temperley–Lieb with loop value `[2]_q = q + q⁻¹ ≥ 2`, so positivity holds for
every real `q > 0` (Jones), including the QOU substrate `q_0 ≈ 1.11`. The old
"regime `q^{1/2} + q^{-1/2} > 2`" only excluded `q = 1`. The per-block
weights are proved positive in `QOU.SchurWeyl.ocneanuWeight_conventionD_pos_of_two_rows`.

The class fields are the *data* of the construction (positive
tracial state on the inductive system, trace ideal, Hilbert-space
completion, faithful representation). Provided an instance, the
embedding `π_GNS : H_∞(q) → L(H)` is exhibited.

## References

- [jones1985] V. F. R. Jones, *A polynomial invariant for knots via
  von Neumann algebras*, Bull. AMS 12 (1985) 103-111.
- [wenzl1988] H. Wenzl, *Hecke algebras of type A_n and subfactors*,
  Invent. Math. 92 (1988) 349-383.
-/

namespace QOU.Observations.AlgebraicGnsEmbedding

universe u v

open scoped BigOperators

/-- **Markov-trace GNS embedding data.**

A class witnessing the Jones–Wenzl GNS embedding of the inductive
limit Hecke algebra `H_∞(q)` into bounded operators on a Hilbert
space. Each field carries concrete content; no `True` placeholders.

The carrier `A` represents `H_∞(q)`, the carrier `H` represents the
GNS Hilbert space, and `repr` is the faithful representation. -/
class HasMarkovGnsEmbedding (A : Type u) (H : Type v)
    [NonUnitalNonAssocRing A] [Star A]
    [NormedAddCommGroup H] [InnerProductSpace ℝ H] [CompleteSpace H] where
  /-- The (real-valued) Markov trace. -/
  trM : A → ℝ
  /-- **Linearity** of `trM`. -/
  trM_add : ∀ (x y : A), trM (x + y) = trM x + trM y
  /-- **Traciality** (cyclicity): `tr_M(x · y) = tr_M(y · x)`. -/
  trM_cyclic : ∀ (x y : A), trM (x * y) = trM (y * x)
  /-- **Positivity** (every real `q > 0` under convention D): `tr_M(x* x) ≥ 0`. -/
  trM_pos : ∀ (x : A), 0 ≤ trM (star x * x)
  /-- **Faithfulness on the GNS quotient**:
      `tr_M(x* x) = 0 → x ∈ trace ideal`. Encoded via an explicit
      ideal predicate. -/
  traceIdeal : A → Prop
  trM_faithful : ∀ (x : A), trM (star x * x) = 0 ↔ traceIdeal x
  /-- **The GNS representation** as a function `A → (H → H)`
      (left multiplication on the GNS quotient, extended to H by
      continuity). -/
  repr : A → (H → H)
  /-- **Linearity of `repr`** in its first argument
      (so `repr (x + y) = repr x + repr y` pointwise). -/
  repr_add : ∀ (x y : A) (h : H), repr (x + y) h = repr x h + repr y h
  /-- **Multiplicativity of `repr`** (a *-homomorphism on the
      algebra-action side). -/
  repr_mul : ∀ (x y : A) (h : H), repr (x * y) h = repr x (repr y h)
  /-- **Faithfulness of `repr`**: zero representation only for
      ideal elements. -/
  repr_faithful : ∀ (x : A), (∀ h : H, repr x h = 0) → traceIdeal x


/-! ### The trace ideal of a positive tracial functional is a two-sided ideal

This is the step of the GNS construction that the block's quotient
`H_∞(q)/𝒩` needs: the null set `𝒩 = {x : tr(x* x) = 0}` must be an ideal for
the quotient to be an algebra on which the representation acts.  It is proved
here from linearity, positivity and cyclicity alone, for any real
`*`-algebra; nothing about `𝒩` is assumed.

The argument is the polarisation step of Cauchy–Schwarz.  If `tr(x* x) = 0`
then `t ↦ tr((x + t y)*(x + t y)) = t·c + t²·tr(y* y)`, with
`c = tr(x* y) + tr(y* x)`, is non-negative for every real `t`, which forces
`c = 0` (`null_polar`).  Each closure property then follows by choosing `y`.
-/

section NullIdeal

variable {A : Type u} [Ring A] [StarRing A] [Algebra ℝ A] [StarModule ℝ A]

/-- **Polarisation.**  If `x` is null for a positive linear functional, then
`tr(x* y) + tr(y* x) = 0` for every `y`. -/
theorem null_polar (tr : A →ₗ[ℝ] ℝ) (hpos : ∀ a : A, 0 ≤ tr (star a * a))
    {x : A} (hx : tr (star x * x) = 0) (y : A) :
    tr (star x * y) + tr (star y * x) = 0 := by
  set c := tr (star x * y) + tr (star y * x) with hc
  set d := tr (star y * y) with hd
  have hd0 : 0 ≤ d := hpos y
  have key : ∀ t : ℝ, 0 ≤ t * c + t ^ 2 * d := by
    intro t
    have h := hpos (x + t • y)
    have e : star (x + t • y) * (x + t • y)
        = star x * x + t • (star x * y + star y * x) + (t ^ 2) • (star y * y) := by
      simp only [star_add, star_smul, star_trivial, add_mul, mul_add, smul_mul_assoc,
        mul_smul_comm, smul_add, smul_smul, pow_two]
      abel
    rw [e, map_add, map_add, map_smul, map_smul, map_add, hx, smul_eq_mul, smul_eq_mul] at h
    linarith
  have h1 := key (-c / (d + 1))
  have hd1 : 0 < d + 1 := by linarith
  have e2 : -c / (d + 1) * c + (-c / (d + 1)) ^ 2 * d = -(c ^ 2 / (d + 1) ^ 2) := by
    field_simp
    ring
  rw [e2] at h1
  have hq : 0 ≤ c ^ 2 / (d + 1) ^ 2 := by positivity
  have h0 : c ^ 2 / (d + 1) ^ 2 = 0 := le_antisymm (by linarith) hq
  have : c ^ 2 = 0 := by
    rcases div_eq_zero_iff.mp h0 with h | h
    · exact h
    · exact absurd h (by positivity)
  exact pow_eq_zero_iff (n := 2) (by norm_num) |>.mp this

/-- **The trace ideal is a two-sided ideal** ([`prop:algebraic-gns-embedding`],
the quotient step).  For a linear functional `tr` on a real `*`-algebra that is
positive (`tr(a* a) ≥ 0`) and tracial (`tr(ab) = tr(ba)`), the null set
`𝒩 = {x : tr(x* x) = 0}` contains `0`, is closed under addition, and is closed
under multiplication by any element on either side.  So `A/𝒩` is an algebra
and `tr` descends to a faithful positive trace on it. -/
theorem markov_gns_null_ideal (tr : A →ₗ[ℝ] ℝ)
    (hpos : ∀ a : A, 0 ≤ tr (star a * a))
    (hcyc : ∀ a b : A, tr (a * b) = tr (b * a)) :
    tr (star (0 : A) * 0) = 0 ∧
    (∀ x y : A, tr (star x * x) = 0 → tr (star y * y) = 0 →
        tr (star (x + y) * (x + y)) = 0) ∧
    (∀ a x : A, tr (star x * x) = 0 → tr (star (a * x) * (a * x)) = 0) ∧
    (∀ x a : A, tr (star x * x) = 0 → tr (star (x * a) * (x * a)) = 0) := by
  refine ⟨by simp, ?_, ?_, ?_⟩
  · intro x y hx hy
    have h := null_polar tr hpos hx y
    have e : star (x + y) * (x + y) = star x * x + (star x * y + star y * x) + star y * y := by
      simp only [star_add, add_mul, mul_add]; abel
    rw [e, map_add, map_add, map_add, hx, hy]
    linarith
  · intro a x hx
    -- take `y = a* a x`; both polar terms equal `tr(x* a* a x)`
    have h := null_polar tr hpos hx (star a * a * x)
    have e1 : star x * (star a * a * x) = star (a * x) * (a * x) := by
      simp only [star_mul]; noncomm_ring
    have e2 : star (star a * a * x) * x = star (a * x) * (a * x) := by
      simp only [star_mul, star_star]; noncomm_ring
    rw [e1, e2] at h
    linarith
  · intro x a hx
    -- `tr((xa)*(xa)) = tr(x* x a a*)` by cyclicity; take `y = x a a*`
    have h := null_polar tr hpos hx (x * a * star a)
    have hc1 : tr (star (x * a) * (x * a)) = tr (star x * (x * a * star a)) := by
      rw [star_mul, show star a * star x * (x * a) = star a * (star x * x * a) by noncomm_ring,
        hcyc, show star x * x * a * star a = star x * (x * a * star a) by noncomm_ring]
    have hc2 : tr (star (x * a * star a) * x) = tr (star x * (x * a * star a)) := by
      rw [show star (x * a * star a) * x = (a * star a) * (star x * x) by
          simp only [star_mul, star_star]; noncomm_ring,
        hcyc, show star x * x * (a * star a) = star x * (x * a * star a) by noncomm_ring]
    rw [hc2] at h
    rw [hc1]
    linarith

end NullIdeal

/-! ### The pre-Hilbert space `A/𝒩` and the left-regular action

With the null set an ideal, the GNS construction needs four more facts, all on
representatives: the form `⟨[x], [y]⟩ = tr(x* y)` is well defined on `A/𝒩`; it
is definite there (`[x] = 0` iff `⟨[x], [x]⟩ = 0`, which is the definition of
`𝒩`, and iff `[x]` pairs to zero with everything); left multiplication descends
to `A/𝒩`; and it is a `*`-action, `⟨[a x], [y]⟩ = ⟨[x], [a* y]⟩`.  For a unital
algebra the action is faithful on the quotient: `a` acts as zero on `A/𝒩`
exactly when `a ∈ 𝒩`.

One more hypothesis is used: `tr` is hermitian, `tr(a*) = tr(a)`.  Over `ℝ` this
is not implied by positivity, and it is what makes `tr(x* y)` symmetric.  The
Hilbert-space completion of `A/𝒩` is not constructed here.
-/

section PreHilbert

variable {A : Type u} [Ring A] [StarRing A] [Algebra ℝ A] [StarModule ℝ A]

/-- A null vector pairs to zero with everything, on both sides. -/
theorem null_pair_eq_zero (tr : A →ₗ[ℝ] ℝ) (hpos : ∀ a : A, 0 ≤ tr (star a * a))
    (hherm : ∀ a : A, tr (star a) = tr a) {x : A} (hx : tr (star x * x) = 0) (y : A) :
    tr (star x * y) = 0 ∧ tr (star y * x) = 0 := by
  have h := null_polar tr hpos hx y
  have hs : tr (star y * x) = tr (star x * y) := by
    rw [← hherm (star x * y), star_mul, star_star]
  constructor <;> linarith

/-- **The GNS form is well defined on `A/𝒩`.** -/
theorem gns_form_well_defined (tr : A →ₗ[ℝ] ℝ) (hpos : ∀ a : A, 0 ≤ tr (star a * a))
    (hherm : ∀ a : A, tr (star a) = tr a) {x x' y y' : A}
    (hx : tr (star (x - x') * (x - x')) = 0) (hy : tr (star (y - y') * (y - y')) = 0) :
    tr (star x * y) = tr (star x' * y') := by
  have h1 := (null_pair_eq_zero tr hpos hherm hx y).2
  have h2 := (null_pair_eq_zero tr hpos hherm hy x').2
  have e1 : star y * (x - x') = star y * x - star y * x' := mul_sub _ _ _
  have e2 : star x' * (y - y') = star x' * y - star x' * y' := mul_sub _ _ _
  rw [e1, map_sub] at h1
  rw [e2, map_sub] at h2
  have s1 : tr (star y * x) = tr (star x * y) := by rw [← hherm, star_mul, star_star]
  have s2 : tr (star y * x') = tr (star x' * y) := by rw [← hherm, star_mul, star_star]
  linarith

/-- **The GNS form is definite on `A/𝒩`**: `x` is null iff it pairs to zero
with every `y`. -/
theorem gns_form_definite (tr : A →ₗ[ℝ] ℝ) (hpos : ∀ a : A, 0 ≤ tr (star a * a))
    (hherm : ∀ a : A, tr (star a) = tr a) (x : A) :
    tr (star x * x) = 0 ↔ ∀ y : A, tr (star y * x) = 0 :=
  ⟨fun hx y => (null_pair_eq_zero tr hpos hherm hx y).2, fun h => h x⟩

/-- **Left multiplication descends to `A/𝒩`.** -/
theorem gns_action_well_defined (tr : A →ₗ[ℝ] ℝ) (hpos : ∀ a : A, 0 ≤ tr (star a * a))
    (hcyc : ∀ a b : A, tr (a * b) = tr (b * a)) (a : A) {x x' : A}
    (hx : tr (star (x - x') * (x - x')) = 0) :
    tr (star (a * x - a * x') * (a * x - a * x')) = 0 := by
  rw [← mul_sub]
  exact (markov_gns_null_ideal tr hpos hcyc).2.2.1 a _ hx

omit [StarModule ℝ A] in
/-- **The action is a `*`-action**: `⟨a x, y⟩ = ⟨x, a* y⟩`. -/
theorem gns_action_adjoint (tr : A →ₗ[ℝ] ℝ) (a x y : A) :
    tr (star (a * x) * y) = tr (star x * (star a * y)) := by
  rw [star_mul, mul_assoc]

/-- **The action is faithful on `A/𝒩`**: `a` sends every class to `0` iff
`a ∈ 𝒩`. -/
theorem gns_action_faithful (tr : A →ₗ[ℝ] ℝ) (hpos : ∀ a : A, 0 ≤ tr (star a * a))
    (hcyc : ∀ a b : A, tr (a * b) = tr (b * a)) (a : A) :
    (∀ b : A, tr (star (a * b) * (a * b)) = 0) ↔ tr (star a * a) = 0 := by
  refine ⟨fun h => by simpa using h 1, fun ha b => ?_⟩
  exact (markov_gns_null_ideal tr hpos hcyc).2.2.2 a b ha

end PreHilbert

/-! ### Removed 2026-08-30 — self-assuming projections

- `markov_gns_embedding` — body was `⟨inst.repr, inst.repr_add, inst.repr_mul, inst.repr_faithful⟩`: the conclusion was the
  projected field verbatim, so the declaration restated its own hypothesis.

**Why removal.** The content stays in the class field each declaration
projected, asserting the same proposition under the same hypotheses; only the
restatement goes. That is the vacuity ledger's recorded disposition for this
category — *"drop the pseudo-theorem and project the field at use sites"* — and
there were no use sites: each had **zero references anywhere in the corpus**.
Bean `qou-z9ws`.
-/

end QOU.Observations.AlgebraicGnsEmbedding
