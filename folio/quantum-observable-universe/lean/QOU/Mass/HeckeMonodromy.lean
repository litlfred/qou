import QOU.MathlibExt.OcneanuTrace
import QOU.Mass.HeckeStokesEigenvalues
import Mathlib.Tactic

/-!
# `HeckeMonodromy` — Step 2 of the canonical chain as a §3b conjecture class

Option **A** of `docs/audits/2026-09-06-step-2-plan-hecke-monodromy.md`. Cheat-sheet §2a records
that Step 2 (geometry → `H_n(q)`) is *stipulated*: the curvature 2-form is defined to be the Hecke
quadratic `F(σ) = σ² − (q − q⁻¹)σ − 1`, so "flatness derives the Hecke relation" is a tautology, and
the geometry it cites (`prop:hecke-spectral-sequence`) has no declaration in `content/`.

This class is the honest restatement §2a asks for. **The conjecture** (primary, §3b-tax — no other
conjecture class among its binders): *the framework's flat connection on the complement of the
discriminant locus of the colour cubic has braid-group monodromy landing in the Hecke tower that
carries the Markov trace, its generators satisfy the Hecke quadratic and the braid relations, and
its classical shadow — under a ring map `ε` to the `q = 1` target — is the Picard–Lefschetz
involution measured in `colour_cubic_branch_monodromy_probe.py`.* The fields carry exactly that
content; nothing is `True`, nothing is empty.

**The KZ model case is derived, not assumed.** For the 𝔰𝔩₂ Knizhnik–Zamolodchikov connection
on two points, the `quad` and `shadow_involution` fields are theorems:
`QOU.Mass.KohnoTwoPoint.kzExchange_quad` and `kzExchange_shadow_involution` (sorry-free; the
`braid`/`far_comm` fields are vacuous for one generator). For `n ≥ 3` the braid relation needs
holonomy over configuration space (bean `qou-9634`); and that the substrate connection *is* KZ is
open (bean `qou-d0qq`). The polynomial `F(σ)` is the eigenvalue relation of the monodromy of a
flat connection; "curvature" in older text means this.

What the file **derives** from the class (sorry-free, unconditional given the instance):

* `hecke_factor` — the generator factors as `(g − q)(g + q⁻¹) = 0` in the algebra: the two
  Stokes/Hecke eigenvalues `q, −q⁻¹` of `QOU.Mass.HeckeStokes.stokes_curvature_factors` are now a
  *consequence* of the monodromy relation rather than the definition of a curvature;
* `shadow_hecke_at_one` — the shadow satisfies the `q = 1` Hecke quadratic `(X − 1)(X + 1) = 0`;
* `shadow_kills_h` — applying `ε` to the Hecke quadratic and using the involution forces
  `ε(h • g) = 0`: the classical shadow *is* the `h = q − q⁻¹ = 0` specialisation, so the
  deformation parameter is exactly what the shadow forgets. This is the sense in which what remains
  stipulated is the deformation `1 ↦ q` and nothing else.

**What this does NOT do.** It does not construct the connection (option C) and it does not define
the forms `(α, β)` route D2 needs. `NaStokesKeystone.lean`'s docstring claim *"has curvature 2-form
`F(σ)`"* is, from here on, to be read as an instance of this class, not as a fact.

Base ring §7c: generic `Field K` for the eigenvalue algebra (division by `q`), generic
`Ring A`/`Ring B` for the tower and its shadow; nothing archimedean.

-- Ref: [leitner2026] docs/canonical-derivation-cheat-sheet.md §2a
-- Ref: [leitner2026] computations/probes/colour_cubic_branch_monodromy_probe.py
-- Ref: [kohno1987] Kohno, Ann. Inst. Fourier 37 (1987) — the model theorem (KZ monodromy factors
--      through the Hecke algebra), for option C.
-/

namespace QOU.Mass

open QOU.MathlibExt.OcneanuTrace

/-- **Conjecture (Step 2 as monodromy).** For a Markov-trace tower `T : MarkovTrace K A` with
generators `T.g i`, a parameter `q ≠ 0`, and a ring map `ε : A →+* B` to the classical target:
the generators are the monodromies of the substrate connection around the branch points of the
colour cubic, so they satisfy the Hecke quadratic with `h = q − q⁻¹`, the braid and far-commutation
relations of the braid group, and under `ε` each becomes an involution (the Picard–Lefschetz
transposition on the two colliding roots). -/
class HeckeMonodromy {K : Type*} [Field K] {A : Type*} [Ring A] [Algebra K A]
    (T : MarkovTrace K A) (q : K) {B : Type*} [Ring B] (ε : A →+* B) : Prop where
  /-- The Hecke quadratic on every generator, with `h = q − q⁻¹`. -/
  quad : ∀ i, T.g i * T.g i = (q - q⁻¹) • T.g i + 1
  /-- The braid relation between neighbours. -/
  braid : ∀ i, T.g i * T.g (i + 1) * T.g i = T.g (i + 1) * T.g i * T.g (i + 1)
  /-- Far commutation. -/
  far_comm : ∀ i j, i + 2 ≤ j → T.g i * T.g j = T.g j * T.g i
  /-- The classical shadow of every generator is an involution: the branch-point transposition. -/
  shadow_involution : ∀ i, ε (T.g i) * ε (T.g i) = 1

namespace HeckeMonodromy

variable {K : Type*} [Field K] {A : Type*} [Ring A] [Algebra K A]
variable (T : MarkovTrace K A) (q : K) {B : Type*} [Ring B] (ε : A →+* B)

/-- **The two Stokes/Hecke eigenvalues are a consequence.** Every generator factors as
`(g − q)(g + q⁻¹) = 0` in `A` — the algebra behind `stokes_curvature_factors`, now derived from
the monodromy hypothesis instead of stipulated as a curvature. -/
theorem hecke_factor [HeckeMonodromy T q ε] (hq : q ≠ 0) (i : ℕ) :
    (T.g i - algebraMap K A q) * (T.g i + algebraMap K A q⁻¹) = 0 := by
  have hquad := HeckeMonodromy.quad (T := T) (q := q) (ε := ε) i
  rw [Algebra.smul_def, map_sub] at hquad
  have hc : algebraMap K A q⁻¹ * T.g i = T.g i * algebraMap K A q⁻¹ := Algebra.commutes _ _
  have hinv : algebraMap K A q * algebraMap K A q⁻¹ = 1 := by
    rw [← map_mul, mul_inv_cancel₀ hq, map_one]
  calc (T.g i - algebraMap K A q) * (T.g i + algebraMap K A q⁻¹)
      = T.g i * T.g i + T.g i * algebraMap K A q⁻¹ - algebraMap K A q * T.g i
          - algebraMap K A q * algebraMap K A q⁻¹ := by noncomm_ring
    _ = ((algebraMap K A q - algebraMap K A q⁻¹) * T.g i + 1) + T.g i * algebraMap K A q⁻¹
          - algebraMap K A q * T.g i - 1 := by rw [hquad, hinv]
    _ = 0 := by rw [← hc]; noncomm_ring

/-- The classical shadow satisfies the Hecke quadratic at `q = 1`: `(X − 1)(X + 1) = 0`. -/
theorem shadow_hecke_at_one [HeckeMonodromy T q ε] (i : ℕ) : (ε (T.g i) - 1) * (ε (T.g i) + 1) = 0 := by
  have h := HeckeMonodromy.shadow_involution (T := T) (q := q) (ε := ε) i
  calc (ε (T.g i) - 1) * (ε (T.g i) + 1) = ε (T.g i) * ε (T.g i) - 1 := by noncomm_ring
    _ = 0 := by rw [h, sub_self]

/-- **The shadow forgets exactly the deformation.** Pushing the Hecke quadratic through `ε` and
using the involution gives `ε((q − q⁻¹) • g) = 0`: the classical target sees `h = 0`, i.e. the
`q = 1` specialisation. What Step 2 leaves stipulated is therefore the deformation `1 ↦ q` alone. -/
theorem shadow_kills_h [HeckeMonodromy T q ε] (i : ℕ) : ε ((q - q⁻¹) • T.g i) = 0 := by
  have hquad := HeckeMonodromy.quad (T := T) (q := q) (ε := ε) i
  have hinv := HeckeMonodromy.shadow_involution (T := T) (q := q) (ε := ε) i
  have h1 : ε (T.g i * T.g i) = ε ((q - q⁻¹) • T.g i + 1) := by rw [hquad]
  rw [map_mul, hinv, map_add, map_one] at h1
  -- h1 : 1 = ε ((q - q⁻¹) • T.g i) + 1
  have := congrArg (fun x => x - 1) h1
  simpa using this.symm

/-! ### The shadow is a Coxeter representation

The probe finds the classical monodromy group to be `S₃`, generated by transpositions. Pushing the
three relation fields through `ε` shows why that is forced by the class: the shadow generators
satisfy the Coxeter presentation of the symmetric group — involutions, braid relation, far
commutation — so `ε ∘ ϱ` factors through `S_n` and is a permutation representation. -/

/-- The shadow satisfies the braid relation. -/
theorem shadow_braid [HeckeMonodromy T q ε] (i : ℕ) :
    ε (T.g i) * ε (T.g (i + 1)) * ε (T.g i) = ε (T.g (i + 1)) * ε (T.g i) * ε (T.g (i + 1)) := by
  have h := HeckeMonodromy.braid (T := T) (q := q) (ε := ε) i
  have := congrArg ε h
  simpa only [map_mul] using this

/-- The shadow satisfies far commutation. -/
theorem shadow_far_comm [HeckeMonodromy T q ε] (i j : ℕ) (hij : i + 2 ≤ j) :
    ε (T.g i) * ε (T.g j) = ε (T.g j) * ε (T.g i) := by
  have h := HeckeMonodromy.far_comm (T := T) (q := q) (ε := ε) i j hij
  have := congrArg ε h
  simpa only [map_mul] using this

/-- Each shadow generator is a unit, its own inverse (a transposition). -/
theorem shadow_isUnit [HeckeMonodromy T q ε] (i : ℕ) : IsUnit (ε (T.g i)) :=
  ⟨⟨ε (T.g i), ε (T.g i), HeckeMonodromy.shadow_involution (T := T) (q := q) (ε := ε) i,
      HeckeMonodromy.shadow_involution (T := T) (q := q) (ε := ε) i⟩, rfl⟩

/-- **Coxeter presentation.** The three relations of `S_n` on the shadow generators, bundled:
involution, braid, far commutation. This is the content of "the classical shadow is a
permutation representation", which the probe measured as `S₃` at `n = 3`. -/
theorem shadow_coxeter [HeckeMonodromy T q ε] :
    (∀ i, ε (T.g i) * ε (T.g i) = 1) ∧
    (∀ i, ε (T.g i) * ε (T.g (i + 1)) * ε (T.g i) = ε (T.g (i + 1)) * ε (T.g i) * ε (T.g (i + 1))) ∧
    (∀ i j, i + 2 ≤ j → ε (T.g i) * ε (T.g j) = ε (T.g j) * ε (T.g i)) :=
  ⟨HeckeMonodromy.shadow_involution (T := T) (q := q) (ε := ε),
    shadow_braid T q ε, shadow_far_comm T q ε⟩

end HeckeMonodromy

end QOU.Mass
