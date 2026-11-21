import Mathlib.Algebra.Algebra.Basic
import Mathlib.RingTheory.Ideal.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.NoncommRing
import QOU.MathlibExt.UniversalDifferentials


/-!
# Cohomology vanishing collapses the GB spectral sequence

For separable algebras (e.g. semisimple over a field of characteristic
zero), Hochschild cohomology vanishes in positive degrees (Hochschild 1945,
the associative analogue of Whitehead's lemma).
The Iwahori-Hecke algebra `A = H_n(R, q)` is semisimple at generic q,
so `HH^k(A) = 0` for `k ≥ 1`.  The limit page of the GB filtration
spectral sequence is therefore concentrated in `HH^0 = Z(A) = ⊕_λ R · e_λ`
(the centre).  That does not imply collapse at `E_1` (corrected
2026-11-16).

The Markov trace (Frobenius integral `Int_A : A → R`) factors through
the Wedderburn-Artin centre.  Plancherel weights `w_λ = dim_q²(λ)/[n]_q!`
on the centre are bounded (but `Σ_λ w_λ(q) ≠ 1` at `q ≠ 1`; only the
classical `w_λ(1)` sums to 1), avoiding the super-
exponential blow-up that disrupted naive numerical tests of the
universal residue.

-- Ref: [leitner2026] prop:spectral-sequence-collapse
-/

namespace QOU.WedderburnMass

universe u

/-- **Semisimple algebra with explicit Wedderburn data.**

    Records the central-idempotent decomposition `A = ⊕_i e_i · A · e_i`
    of a semisimple algebra over `R`.  This is the structural data that
    survives the GB-filtration spectral sequence's collapse.

    For `A = H_n(R, q)` at generic `q`, the index type
    `central_idempotents` is the set of partitions `λ ⊢ n`. -/
class SemisimpleAlgebra (R : Type u) [CommRing R]
    (A : Type u) [Ring A] [Algebra R A] where
  central_idempotents : Type u
  e : central_idempotents → A
  e_central : ∀ i (a : A), e i * a = a * e i
  e_idem : ∀ i, e i * e i = e i
  e_orthogonal : ∀ i j, i ≠ j → e i * e j = 0

/-- `R`-linear derivation `d : A → A` satisfying Leibniz. -/
structure Derivation (R : Type u) [CommRing R]
    (A : Type u) [Ring A] [Algebra R A] where
  d : A →ₗ[R] A
  leibniz : ∀ a b : A, d (a * b) = d a * b + a * d b

open QOU.MathlibExt.UniversalDifferentials in
/-- **Every derivation factors uniquely through `Ω¹(A)`.**  For a
    derivation `D : A → A`, there is exactly one map `φ : Ω¹(A) → A` that is
    a map of `A`-bimodules and satisfies `φ ∘ d = D`.  Here `Ω¹(A) = ker μ`
    is the universal noncommutative calculus of
    `QOU.MathlibExt.UniversalDifferentials`, the same `Ω¹` that the field
    `QuantumUniverse.differentialForms` realises in `C`.

    So derivations of `A` into itself are the same thing as bimodule maps
    `Ω¹(A) → A`.  `WhiteheadHH` below is therefore a statement about maps out
    of `Ω¹(A)`.

    `Derivation` here is defined locally, not taken from Mathlib, because
    Mathlib's `Derivation` needs a commutative algebra and the Hecke algebra
    is not commutative. -/
theorem Derivation.existsUnique_factor_Ω1
    {R : Type u} [CommRing R] {A : Type u} [Ring A] [Algebra R A]
    (D : Derivation R A) :
    ∃! φ : Ω1 R A →ₗ[R] A,
      (∀ a ω, φ (lsmul a ω) = a * φ ω) ∧
      (∀ b ω, φ (rsmul b ω) = φ ω * b) ∧
      ∀ a, φ (QOU.MathlibExt.UniversalDifferentials.d R A a) = D.d a := by
  have hD : ∀ a b, D.d (a * b) = a • D.d b + MulOpposite.op b • D.d a := by
    intro a b
    rw [D.leibniz, smul_eq_mul, op_smul_eq_mul, add_comm]
  refine ⟨lift D.d, ⟨fun a ω => lift_lsmul D.d a ω, fun b ω => ?_,
    fun a => lift_d D.d hD a⟩, fun φ ⟨h1, _, h3⟩ => lift_unique D.d φ h1 h3⟩
  rw [lift_rsmul D.d hD, op_smul_eq_mul]

/-- Inner derivation `ad_x(a) = x·a − a·x`. -/
def innerDerivation {R : Type u} [CommRing R]
    {A : Type u} [Ring A] [Algebra R A] (x : A) : A →ₗ[R] A where
  toFun  := fun a => x * a - a * x
  map_add' := by intros; noncomm_ring
  map_smul' := by
    intros r a
    simp only [RingHom.id_apply, Algebra.smul_def, mul_sub, ← mul_assoc,
      Algebra.commutes r x]

/-- **Whitehead lemma (semisimple HH¹ vanishing, axiom form).**

    For a semisimple algebra `A` over a field of characteristic zero,
    every derivation is inner.  Equivalently, `HH^1(A, A) = 0`.

    Recorded as conjectural-class data because Mathlib does not yet
    have a Hochschild-cohomology framework. -/
class WhiteheadHH (R : Type u) [CommRing R]
    (A : Type u) [Ring A] [Algebra R A] : Prop where
  inner_of_derivation : ∀ (D : Derivation R A), ∃ x : A, D.d = innerDerivation x
  -- Ref: [cartan1956] Cartan-Eilenberg 1956, Ch. IX §7 (Whitehead's lemma);
  --      [weibel1994] Weibel 1994, §9.

/-- **The central idempotents are idempotent.**  A re-export of the
    `SemisimpleAlgebra.e_idem` class field.

    **This does NOT establish the spectral-sequence collapse**, and it was
    named as though it did until 2026-08-26.  Read the type: the conclusion is
    `e * e = e`.  It says nothing about `E_∞`, nothing about a filtration, and
    it does not use the `[WhiteheadHH R A]` instance at all — the hypothesis
    the collapse is supposed to turn on.  The instance is kept in the signature
    only so the rename is behaviour-preserving for any call site that supplies
    it; it is unused, deliberately, and that is the point.

    History, because this defect was found twice: the QA drain of 2026-06-07
    reported *"Lean only proves `e*e=e` idempotency"*, and the 2026-06-12 drain
    closed it as stale under a heading reading "do NOT re-file", on the grounds
    that the file had since gained `SemisimpleAlgebra`, `WhiteheadHH`, a real
    `innerDerivation` and a theorem *named* `spectral_sequence_collapses_to_centre`.
    All true; none of it changed what the theorem proves.  Corrected in
    `docs/audits/2026-06-12-qa-drain-r5r6-findings.md`; rediscovered
    independently in `docs/audits/2026-08-25-spectral-sequence-is-a-no-go-not-a-tool.md`.
    `docs/audits/lean-triviality.json` had it flagged `"closed": false` throughout. -/
theorem centralIdempotent_idem
    {R : Type u} [CommRing R] {A : Type u} [Ring A] [Algebra R A]
    [I : SemisimpleAlgebra R A] [WhiteheadHH R A] :
    ∀ i : I.central_idempotents, I.e i * I.e i = I.e i :=
  fun i => I.e_idem i

/-
GAP: the collapse itself is NOT stated in Lean, and cannot honestly be stated
here yet.  Two things are missing, and neither is a matter of effort:

1. **There is no defined filtration to collapse.**  All three objects the
   corpus calls `J^•` are excluded — the ideal-power reading is provably `⊥`
   above degree 0 (`QOU.BraidKnot.WordFiltration.map_pow_eq_bot`), the
   Coxeter-length reading fails a dimension count at `n ≤ 3`, and the
   rewrite-depth reading is identically zero once `def:hecke-normal-form` fixes
   `T_w` as the unique normal-form basis.  See
   `docs/audits/2026-08-16-three-gb-filtrations-one-name.md`.  A spectral
   sequence needs a filtration; there is no agreed one.

2. **Mathlib has no Hochschild-cohomology framework**, so `E_∞` has no type to
   be stated over.  `WhiteheadHH` is the conjecture carrier standing in for it.

The mathematics of the underlying claim is not in doubt for the FINITE Hecke
algebra: `H_n(R,q)` is semisimple at generic `q`, so Whitehead's lemma gives
`HH^k = 0` for `k ≥ 1`.  What is missing is a Lean statement of that fact, and
writing one requires (1) and (2) first.  Do not close this by renaming a
different theorem back.
-- Ref: [cartan1956] Cartan-Eilenberg 1956, Ch. IX §7 (Whitehead's lemma)
-/

/-- **q-deformed Wedderburn-block weight on λ.**
    `tilde w_λ := dim_q²(λ) / [n]_q!`.  Bounded but `Σ_λ tilde w_λ ≠ 1`
    at q ≠ 1 in general; the classical Plancherel measure
    `w_λ := (dim V_λ)² / n!` (which does sum to 1 exactly) is the
    distinct family — see `prop:plancherel-weight-boundedness`.
    Generic over a commutative ring `R`. -/
def wedderburnWeight {R : Type u} [CommRing R] (dim_q_lam : R) (n_q_fac_inv : R) : R :=
  dim_q_lam * dim_q_lam * n_q_fac_inv

/-- Backward-compat alias: the legacy name `plancherelWeight` is kept
    so older downstream code keeps compiling.  Prefer `wedderburnWeight`
    in new code, since the quantity is the q-deformed Wedderburn-block
    weight, **not** the (distinct) classical Plancherel measure. -/
def plancherelWeight {R : Type u} [CommRing R] (dim_q_lam : R) (n_q_fac_inv : R) : R :=
  wedderburnWeight dim_q_lam n_q_fac_inv

/-- q-deformed Wedderburn-block weights are R-linear in `dim_q²`. -/
theorem wedderburnWeight_smul {R : Type u} [CommRing R]
    (c d_lam n_inv : R) :
    wedderburnWeight (c * d_lam) n_inv = c * c * wedderburnWeight d_lam n_inv := by
  unfold wedderburnWeight
  ring

end QOU.WedderburnMass
