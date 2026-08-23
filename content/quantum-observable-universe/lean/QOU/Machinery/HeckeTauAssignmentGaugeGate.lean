/-
# The gauge gate — descent-transport decision, cell-factoring master lemma, ζ₄ bar edge

Three tightening results on the orbit-invariance program, one per open
bean of the coherence phase-2 plan:

**§1 (bean qou-yvel) — the conjugation-edge monodromy question is
DECIDED, as a criterion.** `monodromyN_equivariant_iff_descent_transport`:
for a marking homomorphism sending `σₗ ↦ σₗ'`, the `q = i` monodromy is
equivariant for ALL states **iff** the homomorphism transports the
σₗ-descent condition pointwise. Sufficiency in the clean general form:
`monodromyN_equivariant_of_length_preserving` — any LENGTH-PRESERVING
marking homomorphism is monodromy-equivariant (subsumes the merged
diagram-edge theorem; also covers e.g. conjugation by the longest
element in a finite system, where `ℓ(w₀xw₀) = ℓ(x)`). Generic
conjugation edges — e.g. the A₃ 4-cycle carrying `(0,1)` to `(1,2)` —
do NOT preserve length, and the descent-transport criterion is exactly
what they must satisfy; the criterion reduces the remaining question
to finite combinatorics per edge. Scope-(a): no blanket claim either
way about generic conjugation edges is made here.

**§2 (bean qou-fc35) — the master cell-factoring lemma, the Δ_λ prune
gate.** `pairCoherent_of_cell`: EVERY functional that factors through
the six-element cell restriction is pair-coherent, in one stroke —
subsuming the assignment and trace instances and giving the gate any
future Δ_λ-candidate construction routed through marked-pair cell data
must pass: factor through the cell (automatic pass) or supply its own
coherence proof. `pairCoherent_comp` closes the class under
post-composition.

**§3 (bean qou-vegn) — the first vertical (bar) edge at ζ₄, named.**
At the monodromy point `q = i = ζ₄` the Habiro bar involution
`q ↦ q⁻¹` IS complex conjugation (`zeta4_inv_eq_star`), and the
`rho_compat` law already carried by every `TauAssignmentData` is
precisely equivariance for this ℤ/2 action
(`tauAssignment_zeta4_bar_equivariance` — a restatement with the right
name, no new proof). In the Habiro-ring-of-a-number-field picture
(Garoufalidis–Scholze–Wheeler–Zagier, arXiv:2412.04241 — uploaded at
`library/arxiv-2412.04241v2/2412.04241v2.pdf`: modules graded by `K₃(K)` whose elements
are root-of-unity-indexed series glued by Frobenius), this is the
bar-involution edge at the ζ₄ fibre; the Frobenius/Galois edges to
other fibres remain the open research half of bean qou-vegn.

HONESTY (STRICT): sorry-free, no axioms, no `decide`; general-rank.
§1 decides a criterion, it does not resolve generic conjugation edges;
§3 renames an already-proved law and claims nothing about the
root-of-unity family. Nothing wired; `1/(8π)` stays phase-4.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.HeckeTauAssignmentMonodromyEquivariance

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List Complex
open QOU.Machinery.HeckeGeneral
open scoped Classical

variable {B W : Type*} [Group W] {M : CoxeterMatrix B}
  (cs : CoxeterSystem M W)

local prefix:100 "σW" => cs.simple

/-! ## §1 — the descent-transport decision -/

/-- Any LENGTH-PRESERVING marking homomorphism is monodromy-
equivariant. Subsumes the diagram-edge theorem and covers
longest-element conjugation in finite systems. -/
theorem monodromyN_equivariant_of_length_preserving (φ : W →* W)
    {l l' : B} (hl : φ (σW l) = σW l')
    (hlen : ∀ w, cs.length (φ w) = cs.length w) (v : W → ℂ) (u : W) :
    monodromyN (descentRight cs l') v (φ u)
      = monodromyN (descentRight cs l) (fun x => v (φ x)) u := by
  unfold monodromyN mulStep descentRight
  simp only [Pi.sub_apply, Pi.smul_apply, smul_eq_mul]
  have ht : φ u * σW l' = φ (u * σW l) := by rw [map_mul, hl]
  simp only [ht, hlen]

/-- **The decision**: monodromy equivariance along a marking
homomorphism holds for all states iff the homomorphism transports the
descent condition pointwise. Reduces the conjugation-edge question to
finite combinatorics per edge. -/
theorem monodromyN_equivariant_iff_descent_transport (φ : W →* W)
    {l l' : B} (hl : φ (σW l) = σW l') :
    (∀ (v : W → ℂ) (u : W),
        monodromyN (descentRight cs l') v (φ u)
          = monodromyN (descentRight cs l) (fun x => v (φ x)) u)
      ↔ ∀ u : W,
          (cs.length (φ u * σW l') < cs.length (φ u)
            ↔ cs.length (u * σW l) < cs.length u) := by
  have ht : ∀ u : W, φ u * σW l' = φ (u * σW l) := by
    intro u
    rw [map_mul, hl]
  constructor
  · intro h u
    have hne1 : φ u * σW l' ≠ φ u := by
      intro hcontra
      have h1 : φ u * σW l' = φ u * 1 := by rw [mul_one]; exact hcontra
      exact simple_ne_one' cs l' (mul_left_cancel h1)
    have hspec := h (fun x => if x = φ u then (1 : ℂ) else 0) u
    unfold monodromyN mulStep descentRight at hspec
    simp only [Pi.sub_apply, Pi.smul_apply, smul_eq_mul, ← ht,
      if_neg hne1, if_true, mul_one] at hspec
    by_cases hc' : cs.length (φ u * σW l') < cs.length (φ u) <;>
      by_cases hc : cs.length (u * σW l) < cs.length u
    · exact iff_of_true hc' hc
    · rw [if_pos hc', if_neg hc] at hspec
      have h2I : (2 * I : ℂ) = 0 := by linear_combination hspec
      exact absurd h2I (mul_ne_zero two_ne_zero Complex.I_ne_zero)
    · rw [if_neg hc', if_pos hc] at hspec
      have h2I : (2 * I : ℂ) = 0 := by linear_combination -hspec
      exact absurd h2I (mul_ne_zero two_ne_zero Complex.I_ne_zero)
    · exact iff_of_false hc' hc
  · intro h v u
    unfold monodromyN mulStep descentRight
    simp only [Pi.sub_apply, Pi.smul_apply, smul_eq_mul, ← ht]
    rw [if_congr (h u) rfl rfl]

/-! ## §2 — the cell-factoring master lemma (the Δ_λ prune gate) -/

/-- **Master sufficient condition**: every functional factoring through
the cell restriction is pair-coherent. Subsumes the assignment and
trace instances; the gate a Δ_λ candidate routed through marked-pair
cell data must pass. -/
theorem pairCoherent_of_cell {α : Type*} (G : (Fin 6 → ℂ) → α) :
    PairCoherent cs (fun p v => G (cellRestrict cs p.i p.j v)) := by
  intro p p' f v
  have hcell : cellRestrict cs p'.i p'.j v
      = cellRestrict cs p.i p.j (fun x => v (f.hom x)) := by
    funext k
    show v (cellElem3 cs p'.i p'.j k)
      = v (f.hom (cellElem3 cs p.i p.j k))
    rw [cellElem3_hom cs f.hom f.map_i f.map_j k]
  exact congrArg G hcell

/-- Pair-coherence is closed under post-composition. -/
theorem pairCoherent_comp {α β : Type*} (g : α → β)
    {F : MarkedPair cs → (W → ℂ) → α} (hF : PairCoherent cs F) :
    PairCoherent cs (fun p v => g (F p v)) :=
  fun f v => congrArg g (hF f v)

/-! ## §3 — the ζ₄ bar edge -/

/-- At `ζ₄ = i` the Habiro bar involution `q ↦ q⁻¹` is complex
conjugation. -/
lemma zeta4_inv_eq_star : (I : ℂ)⁻¹ = star I := by
  rw [Complex.inv_I, Complex.star_def, Complex.conj_I]

/-- **The first vertical edge, named**: `rho_compat` is exactly
ℤ/2-equivariance of the assignment for the bar involution at the ζ₄
fibre — already proved as a law of every `TauAssignmentData`; this
restatement gives it its Habiro-facing name. -/
theorem tauAssignment_zeta4_bar_equivariance {i j : B}
    (hm : M i j = 3) (hne : σW i ≠ σW j) (v : W → ℂ) (u : Fin 4) :
    star ((tauAssignmentAtRank cs i j hm hne).toFun v u)
      = (tauAssignmentAtRank cs i j hm hne).toFunBar
          (fun x => star (v x)) u :=
  (tauAssignmentAtRank cs i j hm hne).rho_compat v u

end QOU.Machinery.CoxeterParabolic
