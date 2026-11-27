import Mathlib.Algebra.Group.Basic

/-!
# Consecutive γγ vertices telescope to one positive and one negative crossing

Bean `qou-brng`, brief C2 front C (bond-selection rule search).
Audit: `docs/audits/2026-11-27-bond-selection-rule-search.md`.

The ruled photon vertex at site `i` is `V(i) = σᵢ σᵢ₊₁⁻¹` (owner rulings 2026-11-20 and
2026-11-22, reading A). Consecutive vertices cancel in pairs:

  `V(s) V(s+1) ⋯ V(s+n) = σₛ σₛ₊ₙ₊₁⁻¹`.

So the set of words built from γγ vertices contains `σₛ σₜ⁻¹` for every `s < t`: one positive and
one negative single crossing. This is the reason the cheapest passing bond over **all** bond words
(no junction-vertex restriction) is a word such as `V2V3 = σ₂σ₄⁻¹` (A = 2) or
`V2V3V4 = σ₂σ₅⁻¹` (A = 3), whose reduced form is two single crossings rather than a vertex power.

The statement is about an arbitrary family `a : ℕ → G` in an arbitrary group, so it holds in the
braid group, in `H_n(q)ˣ`, and in any representation. No number appears in it.
-/

namespace QOU.MassTheory.GammaGammaVertexTelescope

variable {G : Type*} [Group G]

/-- The vertex `a i · (a (i+1))⁻¹`. With `a = σ` this is the ruled γγ vertex `V(i)`. -/
def vertex (a : ℕ → G) (i : ℕ) : G := a i * (a (i + 1))⁻¹

/-- The product `V(s) V(s+1) ⋯ V(s+n-1)` of `n` consecutive vertices. -/
def run (a : ℕ → G) (s : ℕ) : ℕ → G
  | 0 => 1
  | n + 1 => run a s n * vertex a (s + n)

/-- **Telescoping.** `n` consecutive vertices reduce to `a s · (a (s+n))⁻¹`. -/
theorem run_eq (a : ℕ → G) (s : ℕ) : ∀ n, run a s n = a s * (a (s + n))⁻¹
  | 0 => by simp [run]
  | n + 1 => by
      rw [run, run_eq a s n, vertex]
      have : s + (n + 1) = s + n + 1 := by omega
      rw [this, mul_assoc, inv_mul_cancel_left]

/-- Two consecutive vertices: `V(s) V(s+1) = σₛ σₛ₊₂⁻¹` (e.g. `V2V3 = σ₂σ₄⁻¹`). -/
theorem vertex_mul_vertex_succ (a : ℕ → G) (s : ℕ) :
    vertex a s * vertex a (s + 1) = a s * (a (s + 2))⁻¹ := by
  have h := run_eq a s 2
  simp only [run, one_mul] at h
  simpa using h

/-- Every word `σₛ σₜ⁻¹` with `s < t` is a product of γγ vertices. -/
theorem exists_run_of_lt (a : ℕ → G) {s t : ℕ} (hst : s < t) :
    ∃ n, 0 < n ∧ run a s n = a s * (a t)⁻¹ :=
  ⟨t - s, by omega, by rw [run_eq]; congr 3; omega⟩

/-- The telescoped product is not a vertex power in general: it equals `1` only if
`a s = a (s+n)`. (So a faithful family gives a genuine two-crossing word.) -/
theorem run_eq_one_iff (a : ℕ → G) (s n : ℕ) : run a s n = 1 ↔ a s = a (s + n) := by
  rw [run_eq, mul_inv_eq_one]

end QOU.MassTheory.GammaGammaVertexTelescope
