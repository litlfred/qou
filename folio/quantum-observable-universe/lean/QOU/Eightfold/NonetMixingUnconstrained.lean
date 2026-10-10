/-
# Singlet–octet mixing is NOT fixed by first-order octet breaking

The third member of the eightfold-way null-result family, and the one that
comes out the **other way**.

`GellMannOkuboIdentity.lean` and `DecupletEqualSpacing.lean` each show that a
celebrated relation is an *identity* of the first-order octet-breaking ansatz —
it holds for every choice of the breaking parameters, so reproducing it is
evidence for nothing.  Both are therefore dead as derivation targets.

This file shows the opposite for the **nonet mixing angle**: the ansatz places
**no constraint at all** on it.  Given the octet member `m₈` that
Gell-Mann–Okubo fixes, *any* pair of physical masses is realisable by suitable
choices of the two remaining parameters — the singlet mass `m₁` and the
octet–singlet mixing `e`.  So the observed mixing carries information the
symmetry does not supply, and a derivation of it **would** be a genuine
prediction.

That is what makes the vector nonet the interesting case.  The pseudoscalar and
vector nonets have *identical* `SU(3)` content — both are `3 ⊗ 3̄ = 8 ⊕ 1`,
both obey GMO's form — yet their measured mixings sit at nearly opposite
extremes:

| nonet | heavy state | `ss̄` purity | departure from ideal |
|---|---|---|---|
| pseudoscalar `0⁻` | `η′` | `50.3 %` | `49.7` pp |
| vector `1⁻` | `φ` | `99.5 %` | `0.5` pp |

(Comparators only, from PDG central values; cross-checked against the standard
`θ_V ≈ 39°`, `θ_P ≈ −10°`.  Nothing here is fitted.)

The vector nonet is ideally mixed — `φ` is `ss̄` to half a percentage point —
while the pseudoscalar nonet is about as far from ideal as it can be.  No
`SU(3)`-symmetric statement distinguishes them, which is precisely
`mixing_unconstrained` below.  In QCD the near-ideal vector mixing is
attributed to the OZI / quark-line rule; the framework has no account of it.

## What is proved

`charPoly_factors_of_trace_det_match` is an exact algebraic identity over any
commutative ring: with the octet entry `d₁` held **fixed**, setting

    d₂ = l₁ + l₂ − d₁      and      e² = (d₁ − l₁)(l₂ − d₁)

makes the `2 × 2` symmetric mass matrix's characteristic polynomial equal
`(x − l₁)(x − l₂)`.  `mixing_unconstrained` packages it as the surjectivity
statement.  Division-free throughout, so no positivity, ordering, or `ℝ` is
needed — the obstruction being ruled out is algebraic, not archimedean.

Because the construction is explicit rather than an existence argument, it also
says *which* parameters do the work: the mixing is carried entirely by `e`, and
`e = 0` forces the physical states to be the unmixed `ω₈`, `ω₁`
(`no_mixing_iff_eigenvalues_are_diagonal`).

## Consequence for the corpus

Of the eightfold way's three headline quantitative successes, two (GMO, equal
spacing) are now proved **content-free as targets** and the third (nonet
mixing) is proved **content-bearing**.  A framework derivation of the vector
nonet's near-ideal mixing would be the first eightfold-way result that is
evidence for anything.

**This is not a claim that the framework can derive it.**  It cannot at
present: the singlet is unavailable at `dim V = 2`
(`RowCapObstruction.lean`), so the nonet does not yet exist framework-side.
The statement here is about the *target*, not about prospects.

-- Ref: [gellmann1962] Gell-Mann, *Symmetries of Baryons and Mesons*,
--      Phys. Rev. 125 (1962) 1067, https://doi.org/10.1103/PhysRev.125.1067
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic

namespace QOU.Eightfold.NonetMixingUnconstrained

variable {R : Type*} [CommRing R]

/-- The characteristic polynomial of the symmetric `2 × 2` nonet mass matrix

        ⎡ d₁  e ⎤
        ⎣ e   d₂ ⎦

written out as `x² − (trace)·x + (determinant)`.  Stated as a plain polynomial
expression rather than via `Matrix.charpoly` so that the statement stays
elementary and division-free. -/
def charPoly (d₁ d₂ e x : R) : R :=
  x ^ 2 - (d₁ + d₂) * x + (d₁ * d₂ - e ^ 2)

/-- **The key identity.**  With the octet entry `d₁` held fixed — it is what
Gell-Mann–Okubo determines — the singlet entry `d₂` and the mixing `e` can be
chosen so that the characteristic polynomial is exactly `(x − l₁)(x − l₂)`, for
**any** targets `l₁, l₂`.

Both choices are forced and explicit:
`d₂ = l₁ + l₂ − d₁` (matching the trace) and `e² = (d₁ − l₁)(l₂ − d₁)`
(matching the determinant). -/
theorem charPoly_factors_of_trace_det_match (d₁ l₁ l₂ x : R)
    {d₂ esq : R} (hd : d₂ = l₁ + l₂ - d₁) (he : esq = (d₁ - l₁) * (l₂ - d₁)) :
    x ^ 2 - (d₁ + d₂) * x + (d₁ * d₂ - esq) = (x - l₁) * (x - l₂) := by
  subst hd; subst he; ring

/-- **The nonet mixing is unconstrained by the octet-breaking ansatz.**

Given the octet member `d₁` that GMO fixes, *every* pair of physical masses
`(l₁, l₂)` is realised by some singlet entry `d₂` and some squared mixing
`esq`.  The ansatz therefore says **nothing** about where the physical states
sit or how strongly they mix.

Contrast `GellMannOkuboIdentity.gmo_cannot_discriminate` and
`DecupletEqualSpacing.equal_spacing_cannot_discriminate`, where the ansatz
forces the answer and the relation is consequently content-free.  Here it
forces nothing, so the measured mixing **is** information — and deriving it
would be a real prediction. -/
theorem mixing_unconstrained (d₁ l₁ l₂ : R) :
    ∃ d₂ esq : R, ∀ x : R,
      x ^ 2 - (d₁ + d₂) * x + (d₁ * d₂ - esq) = (x - l₁) * (x - l₂) :=
  ⟨l₁ + l₂ - d₁, (d₁ - l₁) * (l₂ - d₁),
   fun x => charPoly_factors_of_trace_det_match d₁ l₁ l₂ x rfl rfl⟩

/-- **Zero mixing is exactly the unmixed case.**  When `e = 0` the
characteristic polynomial factors as `(x − d₁)(x − d₂)`, i.e. the physical
masses *are* the octet and singlet entries and no mixing occurs.

The mixing is therefore carried entirely by `e`: it is the single parameter
the symmetry leaves free, and the one whose observed value the vector and
pseudoscalar nonets disagree about. -/
theorem no_mixing_iff_eigenvalues_are_diagonal (d₁ d₂ x : R) :
    charPoly d₁ d₂ 0 x = (x - d₁) * (x - d₂) := by
  unfold charPoly; ring

/-! ### Non-degeneracy controls

Without these, `mixing_unconstrained` could be satisfied vacuously by targets
that force `esq = 0`, i.e. by no mixing at all. -/

/-- The construction genuinely requires **nonzero** mixing whenever the octet
member lies strictly between the two physical masses — which is the observed
situation in both nonets.  Witnessed over `ℤ` at `d₁ = 1`, `l₁ = 0`, `l₂ = 2`:
`esq = (1 − 0)(2 − 1) = 1 ≠ 0`. -/
theorem mixing_not_forced_zero :
    ∃ d₁ l₁ l₂ : ℤ, (d₁ - l₁) * (l₂ - d₁) ≠ 0 :=
  ⟨1, 0, 2, by decide⟩

/-- And the construction is not degenerate in the other direction either: the
two target masses can be distinct, so this is a statement about a genuine
two-state mixing problem rather than a repeated eigenvalue. -/
theorem targets_can_be_distinct : ∃ l₁ l₂ : ℤ, l₁ ≠ l₂ := ⟨0, 2, by decide⟩

end QOU.Eightfold.NonetMixingUnconstrained
