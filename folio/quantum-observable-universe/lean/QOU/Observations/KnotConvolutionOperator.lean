/-
# Knot convolution operators on the Peter–Weyl blocks

Thread "Derive the electron's categorical weight" (2026-11-27). Owner: "The knot convolution
operators in 𝔤 give the volume of knots implicated", then card "Convolution operator in Lean".
Audit: `docs/audits/2026-11-27-electron-categorical-weight.md` §13.

A knot `K` defines a central element of `U_q(𝔤)` (the universal invariant), so it acts on the
coend `A = O_q(SU(2)) = ⊕_N End(V_N)^*` by convolution. It acts by a scalar `c_N(K)` on the
colour-`N` Peter–Weyl block. For the normalised coloured Jones polynomial, `c_N(K) = J'_N(K)` with
`J'_N(unknot) = 1`. This file gives the algebraic part over any commutative ring or field:

* `ConvOp`, `ConvOp.act`: a family of block scalars acting on block data. `act_mul_left` and
  `act_mul_right` show it commutes with the block algebra (centrality).
* `act_comp`: composing operators multiplies the scalars. For knots,
  `J'_N(K # K') = J'_N(K) J'_N(K')`, so connected sum is composition (`ofJones_connSum`).
* `habiroJ41`: Habiro's cyclotomic sum for `4₁`,
  `J'_N(4₁; q) = Σ_{m<N} Π_{j<m} (q^N + q^{−N} − q^{j+1} − q^{−(j+1)})`.
  `habiroJ41_at_root`: at `q^N = 1` it is `Σ_{m<N} habiro41 q m`. That is the corpus Kashaev
  summand `∏(1 − q^j)(1 − q^{−j})` (`PreArchimedeanBloch.habiro41`), so the Kashaev invariant is
  this operator's scalar on the `N`-block at `q = ζ_N`.

At real `q` the scalars are Laurent polynomials and carry no volume. The volume is the growth
rate of the scalars at `q = ζ_N`. Its additivity under composition is in
`QOU.Transcendental.MassTheory.KnotConvolutionVolume`. No measured value enters.
-/
import QOU.MassTheory.PreArchimedeanBloch
import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic

namespace QOU.Observations.KnotConvolutionOperator

open QOU.Archimedean.PreArchimedeanBloch

/-- A central convolution operator: one scalar per colour `N`. -/
structure ConvOp (R : Type*) where
  c : ℕ → R

namespace ConvOp

variable {R : Type*} [CommRing R]

/-- Action on block data `f N ∈ Mat_N(R)` (matrix coefficients of the `N`-block). -/
def act (z : ConvOp R) (f : (N : ℕ) → Matrix (Fin N) (Fin N) R) :
    (N : ℕ) → Matrix (Fin N) (Fin N) R :=
  fun N => z.c N • f N

/-- Composition of convolution operators. -/
def comp (z w : ConvOp R) : ConvOp R := ⟨fun N => z.c N * w.c N⟩

/-- The identity (the unknot). -/
def one : ConvOp R := ⟨fun _ => 1⟩

theorem act_comp (z w : ConvOp R) (f : (N : ℕ) → Matrix (Fin N) (Fin N) R) :
    act (comp z w) f = act z (act w f) := by
  funext N; simp [act, comp, mul_smul]

theorem act_one (f : (N : ℕ) → Matrix (Fin N) (Fin N) R) : act one f = f := by
  funext N; simp [act, one]

theorem comp_comm (z w : ConvOp R) : comp z w = comp w z := by
  simp [comp, mul_comm]

/-- **Centrality**: the action commutes with the block algebra on both sides. -/
theorem act_mul_left (z : ConvOp R) (f g : (N : ℕ) → Matrix (Fin N) (Fin N) R) :
    act z (fun N => f N * g N) = fun N => act z f N * g N := by
  funext N; simp [act, smul_mul_assoc]

theorem act_mul_right (z : ConvOp R) (f g : (N : ℕ) → Matrix (Fin N) (Fin N) R) :
    act z (fun N => f N * g N) = fun N => f N * act z g N := by
  funext N; simp [act, mul_smul_comm]

/-- The operator of a knot from its normalised coloured Jones polynomials. -/
def ofJones (J : ℕ → R) : ConvOp R := ⟨J⟩

/-- **Connected sum is composition**: if `J'_N(K # K') = J'_N(K) J'_N(K')`, the operator of
`K # K'` is the composite. -/
theorem ofJones_connSum (J J' Jsum : ℕ → R) (h : ∀ N, Jsum N = J N * J' N) :
    ofJones Jsum = comp (ofJones J) (ofJones J') := by
  simp [ofJones, comp, funext h]

end ConvOp

variable {F : Type*} [Field F] [DecidableEq F]

/-- Habiro's cyclotomic sum for the normalised coloured Jones polynomial of `4₁`. -/
def habiroJ41 (q : F) (N : ℕ) : F :=
  ∑ m ∈ Finset.range N,
    ∏ j ∈ Finset.range m, (q ^ N + (q ^ N)⁻¹ - q ^ (j + 1) - (q ^ (j + 1))⁻¹)

/-- **At `q^N = 1` the Habiro sum is the corpus Kashaev sum `Σ_{m<N} habiro41 q m`.** -/
theorem habiroJ41_at_root (q : F) (N : ℕ) (hN : q ^ N = 1) (hq : q ≠ 0) :
    habiroJ41 q N = ∑ m ∈ Finset.range N, habiro41 q m := by
  unfold habiroJ41 habiro41
  refine Finset.sum_congr rfl fun m _ => Finset.prod_congr rfl fun j _ => ?_
  rw [hN, inv_one]
  have : q ^ (j + 1) ≠ 0 := pow_ne_zero _ hq
  field_simp
  ring

/-- `J'_1(4₁) = 1` (colour 1 is the trivial block). -/
theorem habiroJ41_one (q : F) : habiroJ41 q 1 = 1 := by
  simp [habiroJ41]

/-- `J'_2(4₁) = Q² − Q + 1 − Q⁻¹ + Q⁻²` in Habiro's variable `Q`. With `Q = q²` (the corpus
variable) the ring mass of the 4₁ word `(σ₁σ₂⁻¹)²` is `[2]` times this (probe check). -/
theorem habiroJ41_two (q : F) (hq : q ≠ 0) :
    habiroJ41 q 2 = q ^ 2 + (q ^ 2)⁻¹ - q - q⁻¹ + 1 := by
  simp [habiroJ41, Finset.sum_range_succ, Finset.prod_range_succ]
  ring

end QOU.Observations.KnotConvolutionOperator
