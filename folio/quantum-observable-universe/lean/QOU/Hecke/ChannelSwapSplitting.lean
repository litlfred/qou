import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Tactic.Ring

/-!
# Swapping the carriers of a two-channel letter changes the trace only through the carriers' traces

Setting (bean `qou-ulj0`, stepping stone 4 of `qou-slz5`).  A two-nucleon bond that is
graded by spin *and* isospin is built from two carriers `c₁` (isospin) and `c₂` (spin), each
dressed by a letter of degree at most one: `a • 1 + b • c`.  The two Pauli-allowed S-wave
channels, `(S, T) = (1, 0)` (deuteron) and `(0, 1)` (singlet), use the same two letters with
the carriers exchanged.

For any cyclic linear functional `tr` (a trace), the difference between the two channels is

  `tr(f(c₁) g(c₂)) - tr(g(c₁) f(c₂)) = (a₁ b₂ - a₂ b₁) (tr c₂ - tr c₁)`.

So the two channels are split **only** when the carriers have different traces.  In particular
any Markov trace, for which `tr σᵢ = z` for every generator, cannot separate the deuteron from
the singlet when spin and isospin each ride on a single Hecke generator — adjacent or far apart.

This is a structural exclusion (scope (b)): the invariant is `tr c₁ = tr c₂`.  It narrows the
spin⊗isospin route to carriers with unequal traces (e.g. a generator against a conjugate of a
generator by another, `σ₂ σ₃ σ₂`, whose trace is `z + h z²`).

The base ring is generic: `[CommRing R] [Ring A] [Algebra R A]`.
-/

namespace QOU.Hecke.ChannelSwapSplitting

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- A letter of degree at most one in a carrier `c`. -/
def letter (a b : R) (c : A) : A := a • (1 : A) + b • c

/-- **Channel-swap splitting.**  For a trace `tr`, exchanging the two carriers changes the
trace of a product of two degree-one letters by `(a₁ b₂ - a₂ b₁) (tr c₂ - tr c₁)`. -/
theorem tr_swap_sub (tr : A →ₗ[R] R) (hcyc : ∀ x y : A, tr (x * y) = tr (y * x))
    (a₁ b₁ a₂ b₂ : R) (c₁ c₂ : A) :
    tr (letter a₁ b₁ c₁ * letter a₂ b₂ c₂) - tr (letter a₂ b₂ c₁ * letter a₁ b₁ c₂)
      = (a₁ * b₂ - a₂ * b₁) * (tr c₂ - tr c₁) := by
  have h12 := hcyc c₁ c₂
  simp only [letter, mul_add, add_mul, one_mul, mul_one, smul_mul_assoc,
    mul_smul_comm, map_add, map_smul, smul_eq_mul] at *
  rw [h12]
  ring

/-- **No splitting from equal-trace carriers.**  If the two carriers have the same trace, the
two channels have the same trace, whatever the letters. -/
theorem tr_swap_eq_of_tr_eq (tr : A →ₗ[R] R) (hcyc : ∀ x y : A, tr (x * y) = tr (y * x))
    (a₁ b₁ a₂ b₂ : R) {c₁ c₂ : A} (htr : tr c₁ = tr c₂) :
    tr (letter a₁ b₁ c₁ * letter a₂ b₂ c₂) = tr (letter a₂ b₂ c₁ * letter a₁ b₁ c₂) := by
  have := tr_swap_sub tr hcyc a₁ b₁ a₂ b₂ c₁ c₂
  rw [htr, sub_self, mul_zero] at this
  exact sub_eq_zero.mp this

/-- **Converse.**  Over a domain, when the letters are independent (`a₁ b₂ ≠ a₂ b₁`), the two
channels have the same trace only if the carriers have the same trace. -/
theorem tr_eq_of_tr_swap_eq [IsDomain R] (tr : A →ₗ[R] R)
    (hcyc : ∀ x y : A, tr (x * y) = tr (y * x))
    {a₁ b₁ a₂ b₂ : R} (hind : a₁ * b₂ - a₂ * b₁ ≠ 0) {c₁ c₂ : A}
    (hswap : tr (letter a₁ b₁ c₁ * letter a₂ b₂ c₂) = tr (letter a₂ b₂ c₁ * letter a₁ b₁ c₂)) :
    tr c₁ = tr c₂ := by
  have := tr_swap_sub tr hcyc a₁ b₁ a₂ b₂ c₁ c₂
  rw [hswap, sub_self] at this
  rcases mul_eq_zero.mp this.symm with h | h
  · exact absurd h hind
  · exact (sub_eq_zero.mp h).symm

end QOU.Hecke.ChannelSwapSplitting
