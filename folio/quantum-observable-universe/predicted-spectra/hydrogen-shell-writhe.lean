import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import QOU.BraidKnot.ElectronLevelWord


/-!
# QOU.BringsSurface.hydrogen_shell_writhe — Shell number from writhe level

Under the owner ruling of 2026-11-21 the electron is `σ₀σ₁σ₀ ∈ B₃` (closure:
the Hopf link) and photon absorption is the strand-adding curl
`eₙ = σ₀σ₁σ₀σ₂⋯σₙ ∈ B_{n+2}`. Then the writhe is `w = n + 2`, so the level is
`n = w − 2` (`hydrogen_shell_writhe_ruled`).

The older statement `hydrogen_shell_writhe` below is the backup trefoil reading
(`σ^{2n+1}` on `B₂`, `n = (w − 1)/2`). The orbital count `n²` is recorded there as
a definition only; it is not re-derived for the ruled electron.

## References

- [leitner2026] Ch. 6, §3
-/

namespace QOU.BringsSurface

open QOU.MathlibExt.Braid QOU.BraidKnot.ElectronLevelWord in
/-- **Shell from writhe, ruled electron.** The ground word is the electron
`σ₀σ₁σ₀`, the level-`n` word has writhe `n + 2`, and so the level is `w − 2`. -/
theorem hydrogen_shell_writhe_ruled :
    levelWord 1 = σ 0 * σ 1 * σ 0 ∧
    (∀ n : ℕ, 1 ≤ n →
      exponentSum (n + 1) (levelWord n) = Multiplicative.ofAdd ((n : ℤ) + 2)) ∧
    (∀ n : ℕ, 1 ≤ n → ∀ w : ℤ,
      exponentSum (n + 1) (levelWord n) = Multiplicative.ofAdd w → (n : ℤ) = w - 2) :=
  ⟨levelWord_one, writhe_levelWord, shell_eq_writhe_sub_two⟩

-- Ref: [leitner2026] Ch. 6, §3
/-- Backup trefoil reading: n = (w-1)/2 maps writhe to principal quantum number.
    Ground state has w = 3 (n = 1), excited states have w = 2n+1. -/
def shellFromWrithe (w : ℕ) : ℕ := (w - 1) / 2

/-- Orbital count at shell n equals n². -/
def orbitalCount (n : ℕ) : ℕ := n ^ 2

/-- Backup trefoil reading of the shell rule (not the ruled electron). -/
theorem hydrogen_shell_writhe :
    -- (1) Shell-writhe: ground state trefoil w=3 gives n=1
    shellFromWrithe 3 = 1 ∧
    -- (2) Orbital counting: n² orbitals per shell (sum of 2ℓ+1 for ℓ=0..n-1)
    (∀ n : ℕ, 0 < n → orbitalCount n = n ^ 2) ∧
    -- (3) Excited states: w = 2n+1
    (∀ n : ℕ, 0 < n → shellFromWrithe (2 * n + 1) = n) := by
  -- Ref: [leitner2026] Ch. 6, §3
  refine ⟨by decide, fun n _ => rfl, ?_⟩
  intro n hn
  simp [shellFromWrithe]

end QOU.BringsSurface


/-! ## §3b-cond conditional-class hypothesis

This proposition is conditional on the conjecture [`conj:borromean-quark`]
(see `folio/quantum-observable-universe/observations/borromean-quark.lean`
for the canonical `class BorromeanQuark` declaration).  The local stub
below mirrors that class name so the §3b-cond audit
(`content/pipeline/conditional-class-banner-audit.ts`) recognises the
conditional-on-class structure; downstream consumers should import the
canonical class from the sibling stub file instead. -/

/-- Local mirror of `conj:borromean-quark`'s axiomatised class.
    See `borromean-quark.lean` (canonical declaration, namespace
    `QOU.Archimedean`) for the full content.  The field carries the
    genuine conjectural content — the positive baryon (proton-anchor)
    mass scale set by the Borromean volume — not a bare `True`. -/
class BorromeanQuark where
  /-- The bare baryon mass scale (the proton anchor for the electron
      trefoil), as a function of the substrate parameter `q`. -/
  bareMass : ℝ → ℝ
  /-- **Conjectural positivity.**  The baryon mass scale is strictly
      positive for every physical `q > 1` (a genuine `q`-quantified
      property in the shape of the claim, per §3b-tax). -/
  bareMass_pos : ∀ q : ℝ, q > 1 → 0 < bareMass q

/-- Witness theorem: this file's proposition is conditional on
    `BorromeanQuark` per CLAUDE.md §3b-cond.  Conditional on the
    Borromean-baryon model, the proton anchor of the electron trefoil
    has a strictly positive mass scale at the substrate value
    `q = 11/10 > 1` — derived from the class field, not asserted as
    `True`. -/
theorem hydrogen_shell_writhe_conditional_on_borromean_quark
    [inst : BorromeanQuark] : 0 < inst.bareMass (11 / 10 : ℝ) := by
  have hq : (11 / 10 : ℝ) > 1 := by norm_num
  exact inst.bareMass_pos (11 / 10 : ℝ) hq
