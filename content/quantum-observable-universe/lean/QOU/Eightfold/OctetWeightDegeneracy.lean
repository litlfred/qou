/-
# The baryon octet's weight diagram is degenerate — and that is content

The mixed channel `λ = (2,1)` of the Schur–Weyl decomposition
`V^{⊗3} ≅ V_{(3)} ⊗ S^{(3)} ⊕ V_{(2,1)} ⊗ S^{(2,1)} ⊕ V_{(1³)} ⊗ S^{(1³)}`
carries the eight-dimensional baryon octet: `p, n, Σ⁺, Σ⁰, Σ⁻, Λ, Ξ⁰, Ξ⁻`.

This file records the one structural fact about that octet which is **not** a
null result.  The three headline eightfold relations formalised alongside it —
`GellMannOkuboIdentity`, `DecupletEqualSpacing`, `ColemanGlashowIdentity` — are
identities of their first-order ansatz and so discriminate among no mechanisms.
The statement here is the opposite kind: it is falsifiable, it is falsified by
experiment, and what it rules out is a whole class of mass formulae.

## The claim

The weight `(2I₃, Y)` is a **complete** label for the decuplet and an
**incomplete** label for the octet.  Doubling `I₃` keeps everything in `ℤ`.

| | states | distinct weights |
|---|---|---|
| decuplet `(3)` | 10 | 10 — `decuplet_weights_nodup` |
| octet `(2,1)` | 8 | 7 — `octet_weights_not_nodup` |

The single collision is `Λ` against `Σ⁰`, both at the origin `(0, 0)`
(`lambda_sigma0_same_weight`).  Every other octet state sits alone.

## Why it is falsifiable, and falsified

A mass formula that is a function of the weight alone cannot separate two
states sharing a weight, so it predicts `m_Λ = m_Σ⁰` — that is
`weight_function_cannot_separate_lambda_sigma0`, and it holds for *every*
`f : ℤ × ℤ → R`, over any commutative ring.  Experiment gives
`m_Λ ≈ 1115.7` MeV against `m_Σ⁰ ≈ 1192.6` MeV: a `77` MeV gap, about `7 %`,
which is two orders larger than the `≈ 0.8 %` Coleman–Glashow residual.  The
whole class is therefore excluded, not merely disfavoured.

This is a **scope-(b) structural exclusion** in the sense of `AGENTS.md`, and
the invariant justifying it is stated and proved here: non-injectivity of the
weight map on the octet.  Any framework — this one included — must supply a
label beyond `(2I₃, Y)` for the octet.  The physical label is isospin `I`
(`Λ` has `I = 0`, `Σ⁰` has `I = 1`), which is not a function of the weight
(`isospin_not_a_function_of_weight`).

The decuplet carries no such obligation (`decuplet_weight_function_separates`),
which is exactly why the equal-spacing rule needs only `Y` while
Gell-Mann–Okubo needs the isospin Casimir as well.

## What this does not say

The multiplicity `dim S^{(2,1)} = 2` — the reason `V^{⊗3}` contains *two*
copies of the octet — is a **different** doubling and must not be conflated
with the `Λ`/`Σ⁰` degeneracy recorded here.  The former counts copies of the
whole eight-dimensional flavour irrep inside the cube; the latter is a
coincidence of two weights *within a single* copy.  The channel arithmetic
`27 = 10·1 + 8·2 + 1·1` is checked in `schur_weyl_cube_arithmetic` so that the
two twos are visibly separate: the multiplicity two is a Hecke-module
dimension, the degeneracy two is a fibre count over one lattice point.

Everything here is conditional on `N = 3`, which the framework does not supply
(`RowCapObstruction.lean`).  At `N = 2` there is no octet to have a weight
diagram.  Numbers are comparators; nothing is fitted and nothing is wired.

Conventions: generic `[CommRing R]` per `AGENTS.md` §7c — the statements are
about a finite integer lattice and a formal mass function, and need no
ordering, no `ℝ`, and no archimedean content.

-- Ref: [gellmann1962] Gell-Mann, *Symmetries of Baryons and Mesons*,
--      Phys. Rev. 125 (1962) 1067, https://doi.org/10.1103/PhysRev.125.1067
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic

namespace QOU.Eightfold.OctetWeightDegeneracy

variable {R : Type*} [CommRing R]

/-! ### Weights

A weight is the pair `(2I₃, Y)`.  Isospin is doubled so that every entry is an
integer; the doubling is a relabelling and changes no statement below. -/

abbrev Weight : Type := ℤ × ℤ

/-! ### The decuplet, `λ = (3)` -/

/-- The ten decuplet weights `(2I₃, Y)`, in the order
`Δ⁺⁺ Δ⁺ Δ⁰ Δ⁻ Σ*⁺ Σ*⁰ Σ*⁻ Ξ*⁰ Ξ*⁻ Ω⁻`. -/
def decupletWeights : List Weight :=
  [(3, 1), (1, 1), (-1, 1), (-3, 1),
   (2, 0), (0, 0), (-2, 0),
   (1, -1), (-1, -1),
   (0, -2)]

/-- **The decuplet weight is a complete label.**  All ten weights are
pairwise distinct, so `(2I₃, Y)` names a decuplet state uniquely. -/
theorem decuplet_weights_nodup : decupletWeights.Nodup := by decide

theorem decuplet_card : decupletWeights.length = 10 := by decide

/-! ### The octet, `λ = (2,1)` -/

/-- The eight octet weights `(2I₃, Y)`, in the order
`p n Σ⁺ Σ⁰ Λ Σ⁻ Ξ⁰ Ξ⁻`.  `Σ⁰` and `Λ` are adjacent and share `(0, 0)`. -/
def octetWeights : List Weight :=
  [(1, 1), (-1, 1),
   (2, 0), (0, 0), (0, 0), (-2, 0),
   (1, -1), (-1, -1)]

theorem octet_card : octetWeights.length = 8 := by decide

/-- **The octet weight is an incomplete label.**  The eight weights are *not*
pairwise distinct. -/
theorem octet_weights_not_nodup : ¬ octetWeights.Nodup := by decide

/-- The collision is exactly one, at the origin: `Λ` and `Σ⁰` carry the same
`(2I₃, Y) = (0, 0)`.  Deduplicating leaves seven. -/
theorem lambda_sigma0_same_weight :
    octetWeights.count (0, 0) = 2 ∧ octetWeights.dedup.length = 7 := by
  constructor <;> decide

/-- Every octet weight other than the origin is carried by a single state, so
the degeneracy is isolated rather than pervasive. -/
theorem octet_degeneracy_only_at_origin :
    ∀ w ∈ octetWeights, w ≠ (0, 0) → octetWeights.count w = 1 := by decide

/-! ### The consequence for mass formulae -/

/-- **No function of the weight can separate `Λ` from `Σ⁰`.**  There is no
cleverness available, because the two states hand `f` the same argument — so
the statement needs no structure on the target at all, not even a ring — hence
the local `{S : Type*}` rather than the file's `[CommRing R]`.  Weakening the
hypothesis is the point: no target structure can rescue the class.

A mass formula depending only on `(2I₃, Y)` therefore predicts
`m_Λ = m_Σ⁰`.  Experiment gives `1115.7` against `1192.6` MeV, so the entire
class is excluded. -/
theorem weight_function_cannot_separate_lambda_sigma0 {S : Type*} (f : Weight → S) :
    ∀ wLam wSig : Weight, wLam = (0, 0) → wSig = (0, 0) → f wLam = f wSig := by
  rintro wLam wSig rfl rfl; rfl

/-- The same statement in the form that is actually used: a mass assignment
built from the weight is constant on the degenerate fibre. -/
theorem weight_only_mass_is_degenerate (mass : Weight → R)
    (mLam mSig : R) (hLam : mLam = mass (0, 0)) (hSig : mSig = mass (0, 0)) :
    mLam - mSig = 0 := by
  subst hLam; subst hSig; ring

/-- **The decuplet carries no such obligation.**  Because its weights are
distinct, a weight-only function can take a different value on each state; the
obstruction above is specific to the octet.

Witnessed by exhibiting a weight-only function that separates two decuplet
states — `Δ⁺⁺` at `(3, 1)` from `Ω⁻` at `(0, -2)`. -/
theorem decuplet_weight_function_separates :
    ∃ f : Weight → ℤ, f (3, 1) ≠ f (0, -2) :=
  ⟨fun w => w.1, by decide⟩

/-! ### What supplies the missing label -/

/-- Octet isospin, doubled, in the same state order as `octetWeights`:
`p n Σ⁺ Σ⁰ Λ Σ⁻ Ξ⁰ Ξ⁻` has `I = ½ ½ 1 1 0 1 ½ ½`. -/
def octetTwoIsospin : List ℤ := [1, 1, 2, 2, 0, 2, 1, 1]

/-- **Isospin is not a function of the weight.**  Two octet states share the
weight `(0, 0)` while carrying `I = 1` and `I = 0`, so no map
`Weight → ℤ` reproduces the isospin column.  This is what the octet needs and
the weight cannot give.

Stated as the failure of the defining property: assuming such an `f` existed,
`2 = f (0,0) = 0`. -/
theorem isospin_not_a_function_of_weight :
    ¬ ∃ f : Weight → ℤ,
        ∀ i : Fin 8, ∀ hw : i.val < octetWeights.length,
          ∀ hI : i.val < octetTwoIsospin.length,
            f (octetWeights.get ⟨i.val, hw⟩) = octetTwoIsospin.get ⟨i.val, hI⟩ := by
  rintro ⟨f, hf⟩
  have h3 := hf 3 (by decide) (by decide)
  have h4 := hf 4 (by decide) (by decide)
  simp only [octetWeights, octetTwoIsospin, List.get] at h3 h4
  omega

/-- The two states at the origin are the ones that differ, and they differ by
a full unit of doubled isospin. -/
theorem sigma0_lambda_isospin_differ :
    octetTwoIsospin.get ⟨3, by decide⟩ ≠ octetTwoIsospin.get ⟨4, by decide⟩ := by
  decide

/-! ### Channel arithmetic — keeping the two "twos" apart -/

/-- The Schur–Weyl channel count at `N = 3`, `n = 3`:
`27 = 10·1 + 8·2 + 1·1`.

The `2` here is `dim S^{(2,1)}`, the Hecke-module **multiplicity** of the octet
inside `V^{⊗3}`.  It is *not* the `Λ`/`Σ⁰` degeneracy of
`lambda_sigma0_same_weight`, which is a count of states over one lattice point
within a single octet.  The two facts are stated in the same file so that the
distinction is visible, not so that they can be merged. -/
theorem schur_weyl_cube_arithmetic :
    10 * 1 + 8 * 2 + 1 * 1 = 3 ^ 3 := by decide

/-- The octet's eight states spread over seven lattice points; the decuplet's
ten spread over ten.  The deficit is the degeneracy, and it is one. -/
theorem octet_deficit_is_one :
    octetWeights.length - octetWeights.dedup.length = 1 ∧
      decupletWeights.length - decupletWeights.dedup.length = 0 := by
  constructor <;> decide

end QOU.Eightfold.OctetWeightDegeneracy
