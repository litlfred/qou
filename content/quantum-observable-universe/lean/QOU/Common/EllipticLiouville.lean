import Mathlib.Analysis.Complex.Liouville
import Mathlib.Tactic

/-!
# Elliptic Liouville — a doubly-periodic entire function is constant

The isolated classical step named as the residual gap of the G3 Stokes-constant
keystone: `PentagonRigidity.uniqueUpToScalar`
(`QOU/QBeta/CyclicDilogPentagon.lean`) reduces, once **both** periods of the
inter-solution ambiguity are proved (`ratio_ib_periodic` + `ratio_ibinv_periodic`,
lattice `⟨ib, i/b⟩`), to "a doubly-periodic entire function is constant". This
file supplies that theorem, sorry-free.

**What this does and does NOT close (anti-laundering, explicit).** This is a
standalone complex-analysis theorem with **no** dependency on `FaddeevPhi` or any
QOU object. It does **not** by itself discharge `uniqueUpToScalar`: that still
requires (i) endowing `FaddeevPhi` with holomorphicity of `Φ_b` (the class
currently axiomatizes only the two difference equations — the contour-integral
`Φ_b` and its analyticity are open input) and (ii) proving the *ratio* `Φ₁/Φ₂` of
two solutions is entire (poles cancel). Given (i)+(ii), `hf` and the two
periodicities feed this lemma to force the ratio constant. Those two hypotheses
remain open; this file removes only the "elliptic Liouville" excuse.

Proof: continuity on the compact fundamental parallelogram bounds `f` there;
lattice periodicity (integer shifts) extends the bound to all of `ℂ`; Mathlib's
Liouville theorem (`Differentiable.exists_const_forall_eq_of_bounded`) concludes.

Verified `lean`-direct against pinned Mathlib (exit 0).

Ref: [manuscript] docs/audits/2026-07-18-g3-stokes-keystone-evidence-base.md §6
-/

open Complex Set

namespace QOU.Common

/-- **Elliptic Liouville.** An entire function `f : ℂ → ℂ` periodic with respect
to two periods `ω₁, ω₂` that ℝ-span `ℂ` (a lattice basis) is constant. -/
theorem doublyPeriodic_entire_const
    (f : ℂ → ℂ) (ω₁ ω₂ : ℂ)
    (hf : Differentiable ℂ f)
    (h1 : ∀ z, f (z + ω₁) = f z)
    (h2 : ∀ z, f (z + ω₂) = f z)
    (hspan : ∀ z : ℂ, ∃ a b : ℝ, z = a • ω₁ + b • ω₂) :
    ∃ c, ∀ z, f z = c := by
  -- integer periodicity in ω₁ (zsmul)
  have hz1 : ∀ (z : ℂ) (n : ℤ), f (z + n • ω₁) = f z := by
    intro z n
    induction n using Int.induction_on with
    | zero => simp
    | succ k ih =>
        have e : z + ((k : ℤ) + 1) • ω₁ = (z + (k : ℤ) • ω₁) + ω₁ := by
          rw [add_zsmul, one_zsmul]; abel
        rw [e, h1, ih]
    | pred k ih =>
        have hsub : ∀ w, f (w - ω₁) = f w := by
          intro w; have h := h1 (w - ω₁); rw [sub_add_cancel] at h; exact h.symm
        have e : z + (-(k : ℤ) - 1) • ω₁ = (z + (-(k : ℤ)) • ω₁) - ω₁ := by
          rw [sub_zsmul, one_zsmul]; abel
        rw [e, hsub, ih]
  -- integer periodicity in ω₂ (zsmul)
  have hz2 : ∀ (z : ℂ) (n : ℤ), f (z + n • ω₂) = f z := by
    intro z n
    induction n using Int.induction_on with
    | zero => simp
    | succ k ih =>
        have e : z + ((k : ℤ) + 1) • ω₂ = (z + (k : ℤ) • ω₂) + ω₂ := by
          rw [add_zsmul, one_zsmul]; abel
        rw [e, h2, ih]
    | pred k ih =>
        have hsub : ∀ w, f (w - ω₂) = f w := by
          intro w; have h := h2 (w - ω₂); rw [sub_add_cancel] at h; exact h.symm
        have e : z + (-(k : ℤ) - 1) • ω₂ = (z + (-(k : ℤ)) • ω₂) - ω₂ := by
          rw [sub_zsmul, one_zsmul]; abel
        rw [e, hsub, ih]
  -- combined lattice periodicity
  have hlat : ∀ (w : ℂ) (n m : ℤ), f (w + n • ω₁ + m • ω₂) = f w := by
    intro w n m
    have e : w + n • ω₁ + m • ω₂ = (w + m • ω₂) + n • ω₁ := by abel
    rw [e, hz1, hz2]
  -- f bounded on the compact fundamental box
  have hgcont : Continuous (fun p : ℝ × ℝ => p.1 • ω₁ + p.2 • ω₂) := by fun_prop
  have hKcompact : IsCompact
      ((fun p : ℝ × ℝ => p.1 • ω₁ + p.2 • ω₂) '' (Icc (0:ℝ) 1 ×ˢ Icc (0:ℝ) 1)) :=
    (isCompact_Icc.prod isCompact_Icc).image hgcont
  obtain ⟨C, hC⟩ := hKcompact.exists_bound_of_continuousOn hf.continuous.continuousOn
  -- every z reduces to a box point via floor/fract
  have hbound : ∀ z : ℂ, ‖f z‖ ≤ C := by
    intro z
    obtain ⟨a, b, rfl⟩ := hspan z
    have e1 : Int.fract a • ω₁ + (⌊a⌋ : ℤ) • ω₁ = a • ω₁ := by
      rw [← Int.cast_smul_eq_zsmul ℝ ⌊a⌋ ω₁, ← add_smul, Int.fract_add_floor]
    have e2 : Int.fract b • ω₂ + (⌊b⌋ : ℤ) • ω₂ = b • ω₂ := by
      rw [← Int.cast_smul_eq_zsmul ℝ ⌊b⌋ ω₂, ← add_smul, Int.fract_add_floor]
    have hval : f (a • ω₁ + b • ω₂)
        = f (Int.fract a • ω₁ + Int.fract b • ω₂) := by
      have e : a • ω₁ + b • ω₂
          = (Int.fract a • ω₁ + Int.fract b • ω₂) + ⌊a⌋ • ω₁ + ⌊b⌋ • ω₂ := by
        rw [← e1, ← e2]; abel
      rw [e, hlat]
    rw [hval]
    refine hC _ ⟨(Int.fract a, Int.fract b), ⟨?_, ?_⟩, rfl⟩
    · exact ⟨Int.fract_nonneg a, le_of_lt (Int.fract_lt_one a)⟩
    · exact ⟨Int.fract_nonneg b, le_of_lt (Int.fract_lt_one b)⟩
  -- Liouville
  have hbdd : Bornology.IsBounded (range f) := by
    rw [isBounded_iff_forall_norm_le]
    exact ⟨C, by rintro _ ⟨z, rfl⟩; exact hbound z⟩
  exact hf.exists_const_forall_eq_of_bounded hbdd

end QOU.Common
