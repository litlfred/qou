/-
# μ₂ is FORCED, μ₃ is FREE — the well-posedness contrast for the A=3 magnitude target

Red-team (ROUTE 5) companion to `QOU.MassTheory.AdditiveResidualSimplex` (#4320).

The additive residual is decomposed on the coordination simplex `K_A`,
`M(A) = μ₂·C(A,2) + μ₃·C(A,3) + μ₄·C(A,4)`, and the three points A = 2,3,4 pin
`(μ₂,μ₃,μ₄)` by the UNIT-triangular counts matrix `[[1,0,0],[3,1,0],[6,4,1]]`.
The back-substitution is `μ₂ = m₂`, `μ₃ = m₃ − 3·m₂`, `μ₄ = m₄ − 6·m₂ − 4·μ₃`,
where `mₐ = M(A)` are the residual targets.

The audit question (ROUTE 5): is the A=3 magnitude target `μ₃ ≈ +0.4708` a
FORCED structural constant (like `μ₂`), or a FREE coordinate whose value merely
mirrors its AME input?  The lemmas below make the distinction precise and
sorry-free over a generic commutative ring (base ring §7c — no archimedean
construct is used):

* `mu2_pinned_cannot_reach_one` — under the DERIVED deuteron self-reference
  `M(2) = 0` the recovered `μ₂` equals `0` no matter what the A=3,4 AME targets
  are, so it can NEVER equal `1` (or any nonzero value).  `μ₂` is *pinned* by a
  structural constraint, independent of the data — a genuine invariant.
* `mu3_surjective_in_target` — `μ₃`, by contrast, ranges over the WHOLE ring as
  its A=3 target `m₃` varies: for every `v` there is an AME input making
  `μ₃ = v`.  Nothing structural pins its value.
* `mu3_eq_A3_target_of_deuteron` — under `M(2)=0` the triangle coefficient is
  *identically* the A=3 residual, `μ₃ = m₃`.  The "3-body moment" label is a
  coordinate name for a SINGLE isotope's residual — no averaging, no
  over-determination, no statistical-moment freedom.

Reading: `μ₂ = 0` is FORCED (a real constraint the residual must satisfy); the
*sign* and *order of magnitude* of `μ₃` are constrained elsewhere in the corpus
(`μ₃ > 0`, non-monotone ⇒ not a damping — #4300), but its precise VALUE is a free
coordinate — consistent with the companion probe's finding that `μ₃ ≈ 0.4708` is
a condition-number-≈8 residual carrying no 3-sig-fig structural meaning.
NOTHING here derives or wires a value.
-/
import Mathlib.Tactic

namespace QOU.MassTheory.Mu3WellPosedness

/-- The A=2 (edge) simplex coefficient recovered from the residual targets by the
unit-triangular back-substitution: `μ₂ = m₂`.  Written as a function of all three
targets to make "independence from the A=3,4 data" a statement about arguments. -/
def solMu2 {R : Type*} [CommRing R] (m₂ _m₃ _m₄ : R) : R := m₂

/-- The A=3 (triangle) simplex coefficient: `μ₃ = m₃ − 3·m₂`. -/
def solMu3 {R : Type*} [CommRing R] (m₂ m₃ _m₄ : R) : R := m₃ - 3 * m₂

/-- **`μ₂` is FORCED — it is pinned to `0` and cannot reach `1`.**  Under the
derived deuteron self-reference `M(2) = 0`, the recovered edge coefficient is `0`
for EVERY choice of the A=3,4 residual targets `m₃ m₄`.  Hence there is a value
(`1`) the pinned `μ₂` can never attain: it is genuinely constrained by structure,
not by fitting.  (Requires `R` nontrivial so `0 ≠ 1`.) -/
theorem mu2_pinned_cannot_reach_one {R : Type*} [CommRing R] [Nontrivial R] :
    ∃ v : R, ∀ m₃ m₄ : R, solMu2 (0 : R) m₃ m₄ ≠ v := by
  refine ⟨1, fun m₃ m₄ => ?_⟩
  simp only [solMu2]
  exact zero_ne_one

/-- **`μ₃` is FREE — a surjection onto the ring.**  With the deuteron edge target
fixed at `m₂ = 0`, for EVERY value `v` there is an A=3 residual target `m₃` making
`μ₃ = v` (namely `m₃ = v`).  So no structural constraint pins `μ₃`'s value: it is
a free coordinate of the residual.  (Contrast `mu2_pinned_cannot_reach_one`: the
edge coefficient misses `1`, the triangle coefficient hits everything.) -/
theorem mu3_surjective_in_target {R : Type*} [CommRing R] (v m₄ : R) :
    ∃ m₃ : R, solMu3 (0 : R) m₃ m₄ = v := by
  refine ⟨v, ?_⟩
  simp only [solMu3, mul_zero, sub_zero]

/-- **`μ₃` collapses to the raw A=3 target when `μ₂ = 0`.**  Under the forced
deuteron constraint the triangle coefficient is *identically* the A=3 residual:
`μ₃ = m₃`.  Hence the "3-body moment" is a coordinate name for a single isotope's
residual — there is no averaging and no statistical-moment method freedom. -/
theorem mu3_eq_A3_target_of_deuteron {R : Type*} [CommRing R] (m₃ m₄ : R) :
    solMu3 (0 : R) m₃ m₄ = m₃ := by
  simp only [solMu3, mul_zero, sub_zero]

/-- **The forced/free contrast, packaged.**  Simultaneously, over any nontrivial
commutative ring: the pinned edge coefficient `μ₂` (under `M(2)=0`) misses the
value `1`, while the triangle coefficient `μ₃` attains any prescribed `v`.  One
statement separating the structural invariant (`μ₂` forced) from the free
coordinate (`μ₃`). -/
theorem forced_free_contrast {R : Type*} [CommRing R] [Nontrivial R] (v m₄ : R) :
    (∀ m₃ m₄' : R, solMu2 (0 : R) m₃ m₄' ≠ (1 : R)) ∧
      (∃ m₃ : R, solMu3 (0 : R) m₃ m₄ = v) := by
  refine ⟨fun m₃ m₄' => ?_, v, ?_⟩
  · simp only [solMu2]; exact zero_ne_one
  · simp only [solMu3, mul_zero, sub_zero]

/-- **Exact reconstruction of the A=3 residual target `m₃` from `(solMu2, solMu3)` (`qou-p2d5`).**
For any residual targets `(m₂, m₃, m₄)` over a commutative ring `R`,
`solMu3 m₂ m₃ m₄ + 3 * solMu2 m₂ m₃ m₄ = m₃`. -/
theorem solMu3_add_three_solMu2 {R : Type*} [CommRing R] (m₂ m₃ m₄ : R) :
    solMu3 m₂ m₃ m₄ + 3 * solMu2 m₂ m₃ m₄ = m₃ := by
  have h2 : solMu2 m₂ m₃ m₄ = m₂ := rfl
  dsimp [solMu3]
  rw [h2]
  ring

end QOU.MassTheory.Mu3WellPosedness
