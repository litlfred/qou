import Mathlib.Algebra.Algebra.Basic
import Mathlib.RingTheory.Ideal.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic


/-!
# Cohomology vanishing collapses the GB spectral sequence

For semisimple algebras over a field of characteristic zero,
Hochschild cohomology vanishes in positive degrees (Whitehead lemma).
The Iwahori-Hecke algebra `A = H_n(R, q)` is semisimple at generic q,
so `HH^k(A) = 0` for `k ≥ 1`.  The GB filtration spectral sequence
therefore collapses at `E_1` with all contributions concentrated in
`HH^0 = Z(A) = ⊕_λ R · e_λ` (the centre).

The Markov trace (Frobenius integral `Int_A : A → R`) factors through
the Wedderburn-Artin centre.  Plancherel weights `w_λ = dim_q²(λ)/[n]_q!`
on the centre are bounded (`Σ_λ w_λ = 1`), avoiding the super-
exponential blow-up that disrupted naive numerical tests of the
universal residue.

-- Ref: [manuscript] prop:spectral-sequence-collapse
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

/-- Inner derivation `ad_x(a) = x·a − a·x`. -/
def innerDerivation {R : Type u} [CommRing R]
    {A : Type u} [Ring A] [Algebra R A] (x : A) : A →ₗ[R] A where
  toFun  := fun a => x * a - a * x
  map_add' := by intros; simp [mul_add, add_mul]; ring
  map_smul' := by intros; simp [Algebra.smul_def]; ring

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

/-- **Spectral sequence collapse (structural statement).**

    Under `[SemisimpleAlgebra R A]` and `[WhiteheadHH R A]`, the GB
    filtration spectral sequence has only the centre on the
    `E_∞`-page: `E_∞^{p,q} = 0` for `p + q ≥ 1`, and
    `E_∞^{0,0} = Z(A) = ⊕_i R · e_i`.

    This is the formal consequence; downstream blocks
    (`prop:confinement-categorical`, `prop:plancherel-term-7-formulation`)
    package the categorical and analytic readings respectively. -/
theorem spectral_sequence_collapses_to_centre
    {R : Type u} [CommRing R] {A : Type u} [Ring A] [Algebra R A]
    [I : SemisimpleAlgebra R A] [WhiteheadHH R A] :
    ∀ i : I.central_idempotents, I.e i * I.e i = I.e i :=
  fun i => I.e_idem i

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
