import QOU.Machinery.SpectralSequenceBasic

/-!
# `E2Degenerates` is a page property; `KLRSpectralSequenceAtE2` is vacuous

**`E2Degenerates` (parameter property, not a debt).** It says every
differential `d_r` with `r ≥ 2` vanishes on the page structure `S` that is
passed in. `SpectralSequencePage` is bare data (no `d ∘ d = 0`, no
`E_{r+1} = H(E_r, d_r)`), so the class is a property of that data:
* `e2Degenerates_d1Page` — a concrete page on `ℤ` whose `d₁` is the identity
  (nonzero) and whose higher differentials vanish satisfies it;
* the source file already proves `not_e2Degenerates_of_d2_ne_zero`, and
  `not_e2Degenerates_d2Page` instantiates it on a concrete page.
So it is neither universally true nor universally false. The open item it
names (degeneration of the KLR / Hochschild spectral sequence of the residue-A
setting) needs that spectral sequence to be *constructed* first; the class
cannot express it until `S` is.

**`KLRSpectralSequenceAtE2` (VACUOUS — defect).** Its only field is
`e2_is_canonical_basis : True`. `klr_vacuous` records that every page
satisfies it. It asserts nothing and should be either deleted or given a real
field; that is an owner decision and is not done here. It should not be
counted as Mathlib debt.

-- Ref: [leitner2026] QOU.Machinery.SpectralSequenceBasic; [mccleary2001]
-- J. McCleary, A User's Guide to Spectral Sequences, 2nd ed., Def. 2.1
-- (pages and differentials) and §1.2 (degeneration at E₂).
-/

namespace QOU.Machinery.Instances

open QOU.Machinery

/-- A page on `ℤ` with `d₁ = id` and all other differentials zero. -/
def d1Page : SpectralSequencePage where
  E := fun _ _ _ => ℤ
  d := fun r _ _ x => if r = 1 then x else 0

instance (r : ℕ) (p q : ℤ) : Zero (d1Page.E r p q) := inferInstanceAs (Zero ℤ)

/-- A page on `ℤ` with `d₂ = id` and all other differentials zero. -/
def d2Page : SpectralSequencePage where
  E := fun _ _ _ => ℤ
  d := fun r _ _ x => if r = 2 then x else 0

instance (r : ℕ) (p q : ℤ) : Zero (d2Page.E r p q) := inferInstanceAs (Zero ℤ)

/-- `d1Page` degenerates at `E₂` although its `d₁` is nonzero. -/
theorem e2Degenerates_d1Page : E2Degenerates d1Page where
  d_vanishes_above_two r hr _ _ x := by
    show (if r = 1 then x else 0) = 0
    rw [if_neg (by omega)]

/-- `d1Page`'s `d₁` is not zero, so the instance above is not the all-zero page. -/
theorem d1Page_d1_ne_zero : d1Page.d 1 0 0 (1 : ℤ) ≠ 0 := by
  show (if (1 : ℕ) = 1 then (1 : ℤ) else 0) ≠ 0
  simp

/-- `d2Page` does not degenerate at `E₂`. -/
theorem not_e2Degenerates_d2Page : ¬ E2Degenerates d2Page :=
  not_e2Degenerates_of_d2_ne_zero d2Page (p := 0) (q := 0) (1 : ℤ)
    (by show (if (2 : ℕ) = 2 then (1 : ℤ) else 0) ≠ 0; simp)

/-- **Vacuity record**: every page satisfies `KLRSpectralSequenceAtE2`
because its only field is `True`. This is a defect report, not a result. -/
theorem klr_vacuous (S : SpectralSequencePage) : KLRSpectralSequenceAtE2 S :=
  ⟨trivial⟩

end QOU.Machinery.Instances
