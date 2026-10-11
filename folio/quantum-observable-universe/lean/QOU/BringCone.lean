import Mathlib.Algebra.Quaternion
import Mathlib.Tactic.Ring

/-!
# Tetraplectic geometry of the Bring cone — the Reeb quaternionic twist

The affine cone of Bring's curve is a real 4-manifold; its 3-dimensional link
carries a 3-Sasakian (degenerate quaternionic-contact) structure whose Reeb
triad is modelled here on the quaternion algebra `Quaternion R`.

We take the three Reeb operators to be **right-multiplication** by the
imaginary units `i, j, k`.  Right-multiplication is used (rather than left) so
that the operators generate the correct `𝔰𝔲(2)` bracket with a `+2` structure
constant:

`[M_i, M_j] p = (p·i)·j − (p·j)·i = p·(ij) − p·(ji) = p·k − p·(−k) = 2·(p·k)`.

The three `reeb_twist_*` lemmas below discharge exactly this bracket
(`[M_i,M_j] = 2·M_k` and cyclic).  These are **pure quaternion-algebra
identities** — no ordering, radical, or other archimedean construct is used —
so per the §7c base-ring convention they are stated over a generic
`{R : Type*} [CommRing R]`, with `BringCone` naming the geometric object.  The
archimedean specialization `Quaternion ℝ` for the actual quaternionic-contact
geometry is left to the consumer; nothing here forces `Mathlib.Data.Real.Basic`
into the dependency cone.

Reference for the geometric interpretation (Reeb quaternionic twist on the
quaternionic-contact link): [manuscript] `lem:bring-cone-reeb-quaternionic-twist`
(brings-surface §Spectral resolvents and gauge structures), with the SU(2)
reading and its scope limits in `rem:tetraplectic-su2-gauge-reading`.
-/

namespace QOU.Tetraplectic

variable {R : Type*} [CommRing R]

/-- The tetraplectic Bring cone, modelled on the quaternions over `R`. -/
abbrev BringCone (R : Type*) [CommRing R] := Quaternion R

/-- Reeb operator `M_i` — right-multiplication by the quaternionic unit `i`. -/
def reebM_i (p : BringCone R) : BringCone R := p * ⟨0, 1, 0, 0⟩
/-- Reeb operator `M_j` — right-multiplication by the quaternionic unit `j`. -/
def reebM_j (p : BringCone R) : BringCone R := p * ⟨0, 0, 1, 0⟩
/-- Reeb operator `M_k` — right-multiplication by the quaternionic unit `k`. -/
def reebM_k (p : BringCone R) : BringCone R := p * ⟨0, 0, 0, 1⟩

/-- Quaternionic twist `[M_i, M_j] = 2·M_k`. -/
theorem reeb_twist_ij (p : BringCone R) :
    reebM_j (reebM_i p) - reebM_i (reebM_j p) = (2 : R) • reebM_k p := by
  dsimp [reebM_i, reebM_j, reebM_k]
  ext <;> simp <;> ring

/-- Quaternionic twist `[M_j, M_k] = 2·M_i`. -/
theorem reeb_twist_jk (p : BringCone R) :
    reebM_k (reebM_j p) - reebM_j (reebM_k p) = (2 : R) • reebM_i p := by
  dsimp [reebM_i, reebM_j, reebM_k]
  ext <;> simp <;> ring

/-- Quaternionic twist `[M_k, M_i] = 2·M_j`. -/
theorem reeb_twist_ki (p : BringCone R) :
    reebM_i (reebM_k p) - reebM_k (reebM_i p) = (2 : R) • reebM_j p := by
  dsimp [reebM_i, reebM_j, reebM_k]
  ext <;> simp <;> ring

/-! ## The square of a Reeb operator is negation — a candidate for `ι`

Bean `qou-wqto`. `brings-surface/archimedean-chirality.md` states that chirality
sits in the ±-eigenspaces of **the Reeb involution `ξ ↦ −ξ`**, and
`QOU/StandardModel/ChiralityGradingConstruction.lean` (V10) proves that a
globally `ι`-odd grading exists **iff `ι` is fixed-point free**
(`free_of_reeb_odd_grading`). What the corpus does not state is any concrete
involution to put there — V10 parameterises over `reeb : State → State` and
nothing instantiates it.

The operators above supply one, as algebra. Right-multiplication by a
quaternionic unit has order four, and its **square is negation** — literally the
`ξ ↦ −ξ` of the content block:

    reebM_i (reebM_i p) = p * i * i = p * (-1) = -p

Negation is an involution, and its fixed points are exactly the solutions of
`2p = 0`: on a `BringCone R` where `2` is not a zero divisor that is the origin
alone, so **negation is fixed-point free on the punctured cone** — precisely
V10's hypothesis.

🛑 **This is a CANDIDATE, not a derivation, and the gap is named.** Proved below
is the *algebra*: that the square of each Reeb operator is negation, that
negation is involutive, and exactly when it is free. **Not** proved, and not
proved anywhere in the corpus: that the Bring cone is the physical state space,
or that the involution the Reeb field induces on physical states is this
negation. That identification is the CR-geometry step
`archimedean-chirality.md` asserts in one paragraph and nothing derives; the
whole V10/V11 tower remains conditional on it. Nothing here is wired and no
observable is predicted.
-/

/-- **`M_i² = −id`.**  Right-multiplication by `i` twice is negation, since
`i² = −1`. -/
theorem reebM_i_sq (p : BringCone R) : reebM_i (reebM_i p) = -p := by
  dsimp [reebM_i]
  ext <;> simp

/-- **`M_j² = −id`.** -/
theorem reebM_j_sq (p : BringCone R) : reebM_j (reebM_j p) = -p := by
  dsimp [reebM_j]
  ext <;> simp

/-- **`M_k² = −id`.** -/
theorem reebM_k_sq (p : BringCone R) : reebM_k (reebM_k p) = -p := by
  dsimp [reebM_k]
  ext <;> simp

/-- Each Reeb operator has **order four**, not two: its square is negation and
its fourth power is the identity. So `M_i` itself is not the involution — its
square is. -/
theorem reebM_i_quartic (p : BringCone R) :
    reebM_i (reebM_i (reebM_i (reebM_i p))) = p := by
  rw [reebM_i_sq, reebM_i_sq, neg_neg]

/-- **Negation on the cone is an involution** — the `ξ ↦ −ξ` of
`archimedean-chirality`, as a map on the cone. -/
theorem neg_involutive_cone (p : BringCone R) : -(-p) = p := neg_neg p

/-- **A fixed point of negation is exactly a solution of `p + p = 0`.**  Stated
as an iff so the next lemma's hypothesis is visibly the only thing needed. -/
theorem neg_fixed_iff_add_self_eq_zero (p : BringCone R) :
    -p = p ↔ p + p = 0 := neg_eq_iff_add_eq_zero

/-- **Negation is fixed-point free away from the origin**, whenever `2` is
cancellable on the cone — which is exactly V10's `free_of_reeb_odd_grading`
hypothesis, so a globally odd chirality grading exists on the punctured cone.

The hypothesis is an explicit cancellation property rather than a typeclass, so
the lemma stays over generic `[CommRing R]` per §7c. It holds in any `R` of
characteristic `≠ 2` without zero divisors, and in particular in `ℝ` for the
archimedean specialisation. -/
theorem neg_free_of_ne_zero {p : BringCone R}
    (h2 : ∀ x : BringCone R, x + x = 0 → x = 0) (hp : p ≠ 0) : -p ≠ p :=
  fun h => hp (h2 p ((neg_fixed_iff_add_self_eq_zero p).mp h))

end QOU.Tetraplectic
