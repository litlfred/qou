/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPerturb

set_option autoImplicit false

/-!
# Replacing every component in turn (issue #8902, C¹ bridge)

If, in any link, a component equal to `L.comp i` can be replaced by `P i` through Δ-moves, then
`L` is Δ-equivalent to the link whose components are the `P i`. The components are replaced one
after another; each replacement only needs the current component, not the others.

## What is a THEOREM here

* `PolygonalLink.deltaEquiv_of_reaches_all` — the statement above.
-/

namespace QOU.MathlibExt.PL

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

namespace PolygonalLink

/-- **Replacing every component in turn is a Δ-equivalence.** -/
theorem deltaEquiv_of_reaches_all (L : PolygonalLink E) (P : Fin L.k → Polygon E)
    (hP : ∀ (L' : PolygonalLink E) (m : Fin L'.k) (i : Fin L.k), L'.comp m = L.comp i →
      L'.Reaches m (P i))
    (L'' : PolygonalLink E) (hk : L.k = L''.k) (hc : ∀ i, L''.comp (Fin.cast hk i) = P i) :
    DeltaEquiv L L'' := by
  classical
  have key : ∀ j, j ≤ L.k → ∃ Lj : PolygonalLink E, DeltaEquiv L Lj ∧ ∃ hj : L.k = Lj.k,
      ∀ i, Lj.comp (Fin.cast hj i) = if (i : ℕ) < j then P i else L.comp i := by
    intro j
    induction j with
    | zero =>
      intro _
      exact ⟨L, Relation.EqvGen.refl _, rfl, fun i => by simp⟩
    | succ j ih =>
      intro hjk
      obtain ⟨Lj, hd, hj, hcj⟩ := ih (by omega)
      set i0 : Fin L.k := ⟨j, by omega⟩
      have hm : Lj.comp (Fin.cast hj i0) = L.comp i0 := by rw [hcj]; simp [i0]
      obtain ⟨L', hd', hk', hc'⟩ := hP Lj (Fin.cast hj i0) i0 hm
      refine ⟨L', Relation.EqvGen.trans _ _ _ hd hd', hj.trans hk', fun i => ?_⟩
      have := hc' (Fin.cast hj i)
      rw [Fin.cast_cast] at this
      rw [this]
      by_cases hi : i = i0
      · subst hi; simp [i0]
      · rw [Function.update_of_ne (fun h => hi (Fin.cast_injective _ h)), hcj]
        have hv : (i : ℕ) ≠ j := fun h => hi (Fin.ext h)
        by_cases hlt : (i : ℕ) < j
        · simp [hlt, show (i : ℕ) < j + 1 by omega]
        · simp [hlt, show ¬ (i : ℕ) < j + 1 by omega]
  obtain ⟨Lk, hd, hj, hcj⟩ := key L.k le_rfl
  have he : Lk = L'' := ext' (hj.symm.trans hk) fun i => by
    have h1 := hc (Fin.cast hj.symm i)
    rw [Fin.cast_cast] at h1
    rw [h1]
    have h2 := hcj (Fin.cast hj.symm i)
    rw [Fin.cast_cast, Fin.cast_eq_self] at h2
    rw [h2, if_pos (Fin.is_lt _)]
  exact he ▸ hd

end PolygonalLink

end QOU.MathlibExt.PL
