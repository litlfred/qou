import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Group.List

/-!
# QOU.Molecular.symmetric_block_domain_weight — trivial-rep domain weight = q^(word length)

On the **symmetric (trivial) representation** of the braid monoid — the
1-dimensional Wedderburn block that a molecule's `C_{nv}` assembly projector
selects (the `S_n`-symmetric channel, `rem:h2o-c2v-from-projector`) — every
generator acts as the scalar `q`. Hence an electron domain represented by a
braid word `w` of length `ℓ` has VSEPR weight `q^ℓ`.

The canonical lone pair is `e⁻ = σ₀σ₁σ₀` (length 3) and the `σ`-bond is length
1, so the lone/bond weight ratio is `q³ / q = q²` — a ratio of Hecke
eigenvalues, derived (no fit) and independent of the repulsion kernel. Plugged
into the weighted VSEPR with the per-molecule domain counts this reproduces the
second-row hydride angles `CH₄ 109.47° / NH₃ 106.88° / H₂O 104.72°` within
`0.22°` (`molecular_angle_symmetric_block_general.py`).

## References
- [manuscript] Ch. 12, Proposition: symmetric-block domain weight
-/

namespace QOU.Molecular

variable {R : Type*} [CommMonoid R] {ι : Type*}

/-- **Symmetric-block domain weight.** On the trivial representation (every
generator `↦ q`), a domain given by a braid word `w` has weight `q ^ w.length`:
the product of the per-generator scalars `q` over the word. Proved by induction
on `w` (bedrock `List.prod_cons` / `pow_succ`). -/
theorem symmetric_block_domain_weight (q : R) (w : List ι) :
    (w.map (fun _ => q)).prod = q ^ w.length := by
  induction w with
  | nil => simp
  | cons _ xs ih => simp [ih, pow_succ, mul_comm]

/-- **Lone/bond ratio `= q²`.** The lone pair `e⁻ = σ₀σ₁σ₀` (length 3) has
weight `q³`, the `σ`-bond (length 1) has weight `q`, so the lone-pair weight is
`q²` times the bond weight: `q³ = q² · q`. -/
theorem lone_bond_ratio_q_squared (q : R) : q ^ 3 = q ^ 2 * q := by
  rw [pow_succ]

end QOU.Molecular
