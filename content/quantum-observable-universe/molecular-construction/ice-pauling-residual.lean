import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic

/-!
# QOU.Molecular.IcePauling — Pauling residual entropy of ice (combinatorial core)

Each water in ice `I_h` is tetrahedrally coordinated to four neighbours by
hydrogen bonds, two as **donor** (its two H's) and two as **acceptor** (its
two lone pairs) — the "ice rules." This file proves the combinatorial core
of Pauling's residual-entropy estimate (1935): per molecule there are
`C(4,2) = 6` ways to assign the two donated H's among the four bonds, and
each of the molecule's two bonds is shared with a neighbour and holds
exactly one H with the independent-estimate probability `1/2`, giving a
per-molecule multiplicity

    W₁ = C(4,2) · (1/2)² = 6/4 = 3/2,

thus the molar residual entropy is `S = R·ln(3/2) ≈ 3.37 J mol⁻¹ K⁻¹`. The
multiplicity `3/2` is the exact, axiom-free content; `S = R ln W₁` is the
archimedean evaluation.

## References
- [manuscript] Ch. 12, Proposition: Pauling residual entropy of ice
-/

namespace QOU.Molecular

/-- Number of ways a water assigns its two donated H's among its four
hydrogen bonds: `C(4,2) = 6`. -/
theorem ice_orientations : Nat.choose 4 2 = 6 := by decide

/-- **Pauling per-molecule multiplicity.** `C(4,2)·(1/2)² = 3/2`: the six
H-orientations, each of the two shared bonds holding exactly one H with the
independent-estimate probability `1/2`. The molar residual entropy is then
`S = R·ln(3/2)`. -/
theorem pauling_multiplicity :
    (Nat.choose 4 2 : ℚ) * (1 / 2) ^ 2 = 3 / 2 := by
  rw [ice_orientations]; norm_num

end QOU.Molecular
