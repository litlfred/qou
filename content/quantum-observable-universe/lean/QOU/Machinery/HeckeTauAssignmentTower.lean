/-
# The τ-assignment tower square — ι₃₄ naturality at the H₃ → H₄ rung

The tower leg of the `TauRhoHodgeLift` program: the H3-rung τ-assignment
(merged #4102: `tauAssignmentH3`, coker(N)-exact, CW(3,1)-matched) is
extended one rung up the Hecke tower and the ι₃₄ compatibility square is
PROVED:

* **`descentH4σ₀`** — the σ₀ right-multiplication descent structure on
  the 24-element S₄ NF basis, extracted from the preflight-pinned
  `H4.mulσ₀` table (`h4_mulσ₀_eq_mulStep` certifies the extraction —
  the same pattern as the merged `h4_mulσ₂_eq_mulStep`). Its 6-element
  prefix IS the H3 cell: `t`-prefix `[1,0,3,2,5,4]` and `len`-prefix
  `[0,1,1,2,2,3]` equal `descentH3σ₀`'s tables, because the 24-basis is
  ordered with the H₃ basis first (the merged `iota34` convention).
* **`iota34_monodromyN`** — the DOMAIN square: the tower inclusion
  intertwines the nilpotents, `ι₃₄ ∘ N₃ = N₄ ∘ ι₃₄`. The monodromy
  weight structure is a tower-natural datum, not a per-rung accident.
* **`tauAssignmentH4`** — the H4-rung assignment: the same three
  H3-prefix coker-dual functionals, now on the 24-dimensional module;
  all four `TauAssignmentData` laws re-proved at the new rung.
* **`tauAssignment_tower_natural` / `_bar`** — the ASSIGNMENT square:
  `toFun₄ ∘ ι₃₄ = toFun₃` (and the ρ-partner square). Together with the
  domain square and the merged trace stabilization
  (`trM4_iota34_stabilizes`), the rung-to-rung data now commute at
  every level: action, nilpotent, trace, assignment.
* **`tauAssignmentH4_surjective`** — surjectivity onto the 3-dim
  isotypic slot TRANSPORTS up the tower through the square (witnesses
  pushed forward by `ι₃₄`).

HONESTY (STRICT): kernel-exactness is an H3-rung (tower-base) feature
and is NOT claimed at H4 — `coker N₄` is 12-dimensional while the
geometric target stays the fixed genus-4 `H^{1,0}`, so the H4 assignment
factors through its coker without being injective on it; only the
H3-block survives, which is exactly what the naturality square says.
The all-rungs functor (naturality for every `n`, and the tower limit)
remains open. Nothing wired; `1/(8π)` stays phase-4.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/
import QOU.Machinery.HeckeTauAssignmentH3
import QOU.Machinery.HeckeH4StabilizationRung

namespace QOU.Machinery.HeckeGeneral

open Complex

/-- The σ₀ right-multiplication descent structure on the 24-element S₄
NF basis, extracted from the preflight-pinned `H4.mulσ₀` table. The
6-element prefix is the H3 cell (`descentH3σ₀`). -/
def descentH4σ₀ : DescentStructure (Fin 24) where
  t := ![1, 0, 3, 2, 5, 4, 8, 11, 6, 14, 15, 7, 18, 19, 9, 10, 21, 22,
    12, 13, 23, 16, 17, 20]
  len := ![0, 1, 1, 2, 2, 3, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
    5, 5, 5, 6]
  t_invol := by decide
  len_ne := by decide

/-- The extraction certificate: the pinned `H4.mulσ₀` table IS `mulStep`
of `descentH4σ₀` (the σ₀ analogue of the merged `h4_mulσ₂_eq_mulStep`). -/
theorem h4_mulσ₀_eq_mulStep {R : Type*} [CommRing R] (h : R) (v : Fin 24 → R) :
    H4.mulσ₀ h v = mulStep descentH4σ₀ h v := by
  funext u
  fin_cases u <;> simp [H4.mulσ₀, mulStep, descentH4σ₀]

/-- **The domain square**: the tower inclusion intertwines the
nilpotents, `ι₃₄ ∘ N₃ = N₄ ∘ ι₃₄` — the monodromy weight structure is
tower-natural. -/
theorem iota34_monodromyN (v : Fin 6 → ℂ) :
    H4.iota34 (monodromyN descentH3σ₀ v)
      = monodromyN descentH4σ₀ (H4.iota34 v) := by
  funext u
  fin_cases u <;>
    simp [H4.iota34, monodromyN, mulStep, descentH3σ₀, descentH4σ₀,
      Pi.sub_apply, Pi.smul_apply, smul_eq_mul]

/-- **The H4-rung τ-assignment**: the three H3-prefix coker-dual
functionals on the 24-dimensional module, into the 3-dim isotypic slot
of the genus-4 `H^{1,0}` model. -/
noncomputable def tauAssignmentH4 : TauAssignmentData descentH4σ₀ where
  toFun v := ![v 0 + I * v 1, v 2 + I * v 3, v 4 + I * v 5, 0]
  toFunBar w := ![w 0 - I * w 1, w 2 - I * w 3, w 4 - I * w 5, 0]
  map_add v v' := by
    funext u
    fin_cases u <;> simp [Pi.add_apply] <;> try ring
  kills_nilpotent v := by
    funext u
    fin_cases u <;>
      simp [monodromyN, mulStep, descentH4σ₀, Pi.sub_apply, Pi.smul_apply,
        smul_eq_mul] <;>
      first
      | linear_combination (v 1) * I_mul_I
      | linear_combination (v 3) * I_mul_I
      | linear_combination (v 5) * I_mul_I
  rho_compat v u := by
    fin_cases u <;>
      simp [Complex.star_def, Complex.conj_I] <;>
      try ring

/-- **THE ι₃₄ COMPATIBILITY SQUARE**: the H4-rung assignment restricted
along the tower inclusion IS the H3-rung assignment. -/
theorem tauAssignment_tower_natural (v : Fin 6 → ℂ) :
    tauAssignmentH4.toFun (H4.iota34 v) = tauAssignmentH3.toFun v := by
  funext u
  fin_cases u <;> simp [tauAssignmentH4, tauAssignmentH3, H4.iota34]

/-- The ρ-partner square. -/
theorem tauAssignment_tower_natural_bar (w : Fin 6 → ℂ) :
    tauAssignmentH4.toFunBar (H4.iota34 w) = tauAssignmentH3.toFunBar w := by
  funext u
  fin_cases u <;> simp [tauAssignmentH4, tauAssignmentH3, H4.iota34]

/-- Surjectivity onto the isotypic slot transports up the tower through
the square: the H4 assignment is onto, witnessed by `ι₃₄`-pushforwards
of the H3 witnesses. -/
theorem tauAssignmentH4_surjective (c : Fin 3 → ℂ) :
    ∃ v : Fin 24 → ℂ, tauAssignmentH4.toFun v = ![c 0, c 1, c 2, 0] := by
  obtain ⟨v, hv⟩ := tauAssignmentH3_surjective c
  exact ⟨H4.iota34 v, by rw [tauAssignment_tower_natural, hv]⟩

end QOU.Machinery.HeckeGeneral
