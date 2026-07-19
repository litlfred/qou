/-
# The braided morphism action, packaged as an endomorphism-ring datum (τ-functor law F2)

Bean `qou-msof` — a sub-piece of the Hecke braided-monoidal-category infra
(bean `qou-pbjv`). The just-landed all-rank core proves the braiding relations
in **operator / composition** form on the function module `W → R`:

* `mulStep_quadratic` / `mulSimple_quadratic` — the Hecke quadratic
  `σᵢ² = h·σᵢ + 1` at EVERY rank (the R-matrix eigenvalue / F2 quadratic);
* `braid_of_dihedral` — the braid relation `σᵢσⱼσᵢ = σⱼσᵢσⱼ` at general rank,
  conditional on a `DihedralCosetStructure` coset datum, reduced to the proved
  n = 3 cell braid `H3.braid_operator`.

But the `HeckeBraidedPresentation` class (`HeckeBraidedCategoryScaffold`) states
the F2 datum as **ring-element** relations `σ i * σ i = (q − q⁻¹) • σ i + 1`,
`σ i * σ (i+1) * σ i = …` over a ring `H` — where `*` is ring multiplication.
The proved braiding action lives one encoding away: it is a family of
endomorphisms of `W → R`, with composition, not literally an element of a named
ring. This file supplies the **missing bridge**: it packages the operator
`mulStep D h` as an honest `R`-linear endomorphism

  `braidingEnd D h : Module.End R (W → R)`,

and re-derives the F2 relations as **genuine ring relations in that
endomorphism ring** — the exact shape the `HeckeBraidedPresentation` fields
demand, with `H := Module.End R (W → R)`:

* `braidingEnd_quadratic` — `braidingEnd D h * braidingEnd D h = h • braidingEnd D h + 1`
  (the quadratic as a `Module.End` ring identity, at every rank);
* `braidingEnd_braid` — `σᵢ * σⱼ * σᵢ = σⱼ * σᵢ * σⱼ` in `Module.End`, from the
  coset datum (the braid as a `Module.End` ring identity);
* proved slices: `descentH2σ₀` (n = 2) and `descentH3σ₀/σ₁` (n = 3, braid via
  `cell_braid`);
* `braidingEnd_hecke_quadratic_field` / `braidingEnd_braid_adjacent` — the two
  packaged relations stated **exactly** in the shape of the corresponding
  `HeckeBraidedPresentation` fields (with `σ i := braidingEnd (D i) (q − q⁻¹)`),
  so a future `HeckeBraidedPresentation R q (Module.End R (W → R)) σ` instance
  would take these as its `hecke_quadratic` (unconditional) and `braid_adjacent`
  (coset-conditional) proofs.

HONESTY (STRICT, §"Axiomatization is NOT a Proof"): **no** instance of
`HeckeBraidedPresentation` or `MarkovStabilization` is declared. The class
quantifies a generator family `σ : ℕ → H` over the H_∞ inductive limit with far
commutation for `|i − j| ≥ 2` (the F1 datum) — and that, together with the
existence of a `DihedralCosetStructure` for every adjacent pair (the open
combinatorial input isolated in `HeckeDihedralBraidReduction`), is **not**
supplied here. This file bridges the *encoding* of the already-proved F2
relations into the ring the class lives in; it closes nothing new and wires
nothing to production (`1/(8π)` stays phase-4). The general-n far-commute /
tower instance stays OPEN, exactly as in the scaffold.

Base ring (§7c): `[CommRing R]` for the endomorphism, quadratic, and braid;
`[Field F]` enters only for the `q − q⁻¹` field-shape corollary (needs `q⁻¹`) —
no `ℝ`, no ordering, no archimedean construct.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/
import QOU.Machinery.HeckeDihedralBraidReduction
import Mathlib.Algebra.Module.End

namespace QOU.Machinery.HeckeGeneral

variable {W : Type*} {R : Type*} [CommRing R]

/-! ## The braiding generator as an `R`-linear endomorphism -/

/-- **The braiding morphism `σ` as an honest `R`-linear endomorphism.** The
Iwahori–Hecke length-rule action `mulStep D h` (proved additive and
`R`-homogeneous) packaged as an element of the endomorphism ring
`Module.End R (W → R)`. This is the object the `HeckeBraidedPresentation` class
lives on: composition in `Module.End` is the ring multiplication in which the
F2 relations below are genuine ring identities. -/
noncomputable def braidingEnd (D : DescentStructure W) (h : R) :
    Module.End R (W → R) where
  toFun := mulStep D h
  map_add' := mulStep_add D h
  map_smul' := fun c v => mulStep_smul D h c v

@[simp] lemma braidingEnd_apply (D : DescentStructure W) (h : R) (v : W → R) :
    braidingEnd D h v = mulStep D h v := rfl

/-! ## The F2 quadratic as a ring identity in `Module.End` -/

/-- **The Hecke quadratic as a `Module.End` ring identity, at every rank.**
`braidingEnd D h * braidingEnd D h = h • braidingEnd D h + 1`, where `*` is
composition in `Module.End R (W → R)` and `1` is the identity endomorphism.
This is the ring-element form of `mulStep_quadratic` — the exact shape of the
`HeckeBraidedPresentation.hecke_quadratic` field. -/
theorem braidingEnd_quadratic (D : DescentStructure W) (h : R) :
    braidingEnd D h * braidingEnd D h = h • braidingEnd D h + 1 := by
  refine LinearMap.ext fun v => ?_
  simp only [LinearMap.mul_apply, LinearMap.add_apply, LinearMap.smul_apply,
    Module.End.one_apply, braidingEnd_apply]
  exact mulStep_quadratic D h v

/-! ## The F2 braid relation as a ring identity in `Module.End` -/

/-- **The braid relation as a `Module.End` ring identity, at general rank.**
Given a `DihedralCosetStructure` on the adjacent pair, the two induced braiding
endomorphisms satisfy `σᵢ * σⱼ * σᵢ = σⱼ * σᵢ * σⱼ` in `Module.End R (W → R)` —
the ring-element form of `braid_of_dihedral` (which reduces the general braid
to the proved n = 3 cell braid). Coset-conditional exactly as
`braid_of_dihedral`: the datum's existence for every adjacent pair is the
isolated open combinatorial input, NOT proved here. -/
theorem braidingEnd_braid (S : DihedralCosetStructure W) (h : R) :
    braidingEnd S.Di h * braidingEnd S.Dj h * braidingEnd S.Di h
      = braidingEnd S.Dj h * braidingEnd S.Di h * braidingEnd S.Dj h := by
  refine LinearMap.ext fun v => ?_
  simp only [LinearMap.mul_apply, braidingEnd_apply]
  exact S.braid_of_dihedral h v

/-! ## Proved concrete slices (n = 2, n = 3) -/

/-- The rank-one (S₂ / H₂) descent structure: step = the transposition `0↔1`,
lengths `[0,1]`. The single-generator base of the tower. -/
def descentH2σ₀ : DescentStructure (Fin 2) where
  t := ![1, 0]
  len := ![0, 1]
  t_invol := by decide
  len_ne := by decide

/-- **n = 2 quadratic slice** (proved): the single H₂ braiding endomorphism
satisfies the Hecke quadratic as a `Module.End` ring identity. The
endomorphism-framework analogue of the scaffold's diagonal-matrix slice
`heckeQuadratic_h2`. -/
theorem braidingEnd_quadratic_h2 (h : R) :
    braidingEnd descentH2σ₀ h * braidingEnd descentH2σ₀ h
      = h • braidingEnd descentH2σ₀ h + 1 :=
  braidingEnd_quadratic descentH2σ₀ h

/-- **n = 3 quadratic slices** (proved): both H₃ braiding generators satisfy
the Hecke quadratic in `Module.End`. -/
theorem braidingEnd_quadratic_h3σ₀ (h : R) :
    braidingEnd descentH3σ₀ h * braidingEnd descentH3σ₀ h
      = h • braidingEnd descentH3σ₀ h + 1 :=
  braidingEnd_quadratic descentH3σ₀ h

theorem braidingEnd_quadratic_h3σ₁ (h : R) :
    braidingEnd descentH3σ₁ h * braidingEnd descentH3σ₁ h
      = h • braidingEnd descentH3σ₁ h + 1 :=
  braidingEnd_quadratic descentH3σ₁ h

/-- **n = 3 braid slice** (proved, unconditional): the two concrete H₃ braiding
generators satisfy `σ₀ * σ₁ * σ₀ = σ₁ * σ₀ * σ₁` in `Module.End R (Fin 6 → R)`.
Discharged directly by the proved n = 3 cell braid `cell_braid` (the transport
of `H3.braid_operator`), so no coset datum is needed at this concrete rung. -/
theorem braidingEnd_braid_h3 (h : R) :
    braidingEnd descentH3σ₀ h * braidingEnd descentH3σ₁ h * braidingEnd descentH3σ₀ h
      = braidingEnd descentH3σ₁ h * braidingEnd descentH3σ₀ h * braidingEnd descentH3σ₁ h := by
  refine LinearMap.ext fun v => ?_
  simp only [LinearMap.mul_apply, braidingEnd_apply]
  exact DihedralCosetStructure.cell_braid h v

/-! ## The two packaged `HeckeBraidedPresentation` field shapes

These state the proved relations in the exact shape of the class fields, with
the generator family `σ i := braidingEnd (D i) (q − q⁻¹)` and
`H := Module.End R (W → R)`. A future `HeckeBraidedPresentation` instance on the
endomorphism ring would take `braidingEnd_hecke_quadratic_field` as its
`hecke_quadratic` proof (unconditional, every rank) and
`braidingEnd_braid_adjacent` as its `braid_adjacent` proof (coset-conditional).
The remaining `far_commute` field (F1) and the H_∞ tower are NOT supplied. -/

section Field
variable {F : Type*} [Field F]

/-- **Packaged `hecke_quadratic` field content** (unconditional, every rank):
for `h = q − q⁻¹`, the endomorphism family `i ↦ braidingEnd (D i) (q − q⁻¹)`
satisfies `σ i * σ i = (q − q⁻¹) • σ i + 1` — literally the
`HeckeBraidedPresentation.hecke_quadratic` field with `H := Module.End F (W → F)`. -/
theorem braidingEnd_hecke_quadratic_field
    (D : ℕ → DescentStructure W) (q : F) (i : ℕ) :
    braidingEnd (D i) (q - q⁻¹) * braidingEnd (D i) (q - q⁻¹)
      = (q - q⁻¹) • braidingEnd (D i) (q - q⁻¹) + 1 :=
  braidingEnd_quadratic (D i) (q - q⁻¹)

end Field

/-- **Packaged `braid_adjacent` field content** (coset-conditional): for an
adjacent index pair `(i, i+1)` whose braiding generators are the induced
descent structures of a `DihedralCosetStructure`, the family satisfies
`σ i * σ (i+1) * σ i = σ (i+1) * σ i * σ (i+1)` — the
`HeckeBraidedPresentation.braid_adjacent` field, conditional on the adjacent
pair carrying the coset datum (the open combinatorial input). -/
theorem braidingEnd_braid_adjacent
    (D : ℕ → DescentStructure W) (h : R) (i : ℕ) (S : DihedralCosetStructure W)
    (hi : S.Di = D i) (hj : S.Dj = D (i + 1)) :
    braidingEnd (D i) h * braidingEnd (D (i + 1)) h * braidingEnd (D i) h
      = braidingEnd (D (i + 1)) h * braidingEnd (D i) h * braidingEnd (D (i + 1)) h := by
  rw [← hi, ← hj]
  exact braidingEnd_braid S h

end QOU.Machinery.HeckeGeneral
