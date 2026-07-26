/-
# The bar-even / bar-odd split of the deuteron binding is the **partition-conjugation parity** of the
# H₆ Wedderburn sum

The canonical categorical deuteron object is the Frobenius-paired Markov trace over the Wedderburn
blocks of `H₆(q)` (`build_markov_trace_assembly_deuteron_chain.py`):

```
tr_M(β_D) = Σ_{λ ⊢ 6} w_λ(q) · χ^λ_q(β_D),   (the Δ_λ-dressed form B = m_e Σ_λ w_λ χ^λ Δ_λ is the binding)
```

The bar involution `q ↦ q⁻¹` acts on the index set of partitions by **conjugation** `λ ↦ λ'`
(transpose of the Young diagram): `w_{λ'}(q) = w_λ(q⁻¹)` and `χ^{λ'}(q) = ±χ^λ(q⁻¹)`. For `n = 6` the
11 partitions form **5 conjugate pairs** `{(6),(1⁶)}, {(5,1),(2,1⁴)}, {(4,2),(2²,1²)},
{(4,1,1),(3,1³)}, {(3,3),(2,2,2)}` plus the **single self-conjugate** partition `(3,2,1)' = (3,2,1)`.

This file formalises, as a pure `CommRing` identity, the structural claim that determines the
*parity* of the deuteron's binding correction (independently of the unknown `Δ_λ` magnitudes — the
Track-A gate): a Wedderburn-indexed quantity splits under conjugation into a bar-even part (symmetric
under `λ ↔ λ'`) and a bar-odd part (antisymmetric), and

**the self-conjugate partition `(3,2,1)` contributes *only* to the bar-even channel** — its character
feeds the bar-even coefficient `g₂`, never the bar-odd impurity `t`.

Model: an index type `I` (the partitions), an involution `c : I → I` (conjugation, `c∘c = id`), and a
Wedderburn quantity `g : I → R` (the per-block `w_λ·χ^λ·Δ_λ` contribution at fixed `q`). The bar image
of `g` is `g ∘ c`. This file proves the parity backbone; it does **not** compute the `Δ_λ` magnitudes.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

namespace QOU.MassTheory.ConjugationParity

variable {I : Type*} {R : Type*} [CommRing R]

/-- The bar-**odd** part of a Wedderburn quantity `g` under conjugation `c` (unnormalised):
`g p − g (c p)`. This is the antisymmetric channel that carries the bar-odd impurity `t`. -/
def barOdd (c : I → I) (g : I → R) (p : I) : R := g p - g (c p)

/-- The bar-**even** part (unnormalised): `g p + g (c p)` — the symmetric channel carrying `g₂`. -/
def barEven (c : I → I) (g : I → R) (p : I) : R := g p + g (c p)

/-- **Decomposition:** twice the quantity is the sum of its bar-even and bar-odd parts. -/
theorem two_mul_eq (c : I → I) (g : I → R) (p : I) :
    2 * g p = barEven c g p + barOdd c g p := by
  unfold barEven barOdd; ring

/-- **Conjugation antisymmetry of the bar-odd part:** `barOdd` at `c p` is minus `barOdd` at `p`,
provided `c` is an involution (`c (c p) = p`). So conjugate pairs `{p, p'}` cancel in the bar-odd
channel. -/
theorem barOdd_conj (c : I → I) (g : I → R) (p : I) (hc : c (c p) = p) :
    barOdd c g (c p) = - barOdd c g p := by
  unfold barOdd; rw [hc]; ring

/-- **Conjugation symmetry of the bar-even part.** -/
theorem barEven_conj (c : I → I) (g : I → R) (p : I) (hc : c (c p) = p) :
    barEven c g (c p) = barEven c g p := by
  unfold barEven; rw [hc]; ring

/-- **The key categorical fact — a self-conjugate partition contributes nothing to the bar-odd
channel.** If `c p = p` (e.g. `p = (3,2,1)` for `n = 6`) then `barOdd c g p = 0`: its Wedderburn
contribution is purely bar-even, so it feeds `g₂` and never the bar-odd impurity `t`. -/
theorem barOdd_selfConj_zero (c : I → I) (g : I → R) (p : I) (hself : c p = p) :
    barOdd c g p = 0 := by
  unfold barOdd; rw [hself]; ring

/-- For a self-conjugate `p`, the bar-even part is just twice the raw contribution. -/
theorem barEven_selfConj (c : I → I) (g : I → R) (p : I) (hself : c p = p) :
    barEven c g p = 2 * g p := by
  unfold barEven; rw [hself]; ring

/-! ## Pairwise cancellation over a conjugate pair

For a conjugate pair `{p, c p}` with `c` an involution, the two bar-odd contributions sum to zero —
the antisymmetric channel is supported entirely on the *asymmetry between* paired partitions, never
on their sum. -/

theorem barOdd_pair_sum_zero (c : I → I) (g : I → R) (p : I) (hc : c (c p) = p) :
    barOdd c g p + barOdd c g (c p) = 0 := by
  rw [barOdd_conj c g p hc]; ring

end QOU.MassTheory.ConjugationParity
