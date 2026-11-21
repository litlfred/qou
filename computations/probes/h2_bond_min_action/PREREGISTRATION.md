# Pre-registration: the H₂ bond by minimum action, beyond three photons

Written 2026-11-21, before any number in this directory was computed. Issue #8879.

## Why

`gg_atom_bonds` (`QOU/Molecular/H2BondSelectionRoutes.lean`, merged in #8884) shows that among
bonds of **one to three** photons, the γγ-produced bonds that keep each atom's strands closed and
do not split across the atom cut are exactly `V₄³` and `V₅³`. With more photons the same
conditions admit more words (`V⁶`, `V₄³V₅³`, …). So those conditions select `V³` only as the
**shortest** admissible bond. A rule is needed for longer bonds.

The corpus has one: the confinement **minimum-action** principle (`prop:confinement-lp`), where
the canonical operator minimises the Markov trace `tr_M` subject to the constraints, and
`rem:assembly-shortest-production`, which uses the same min-action program to pick the canonical
assembly word. This probe applies it to the bond: among the admissible bonds that pass reading 3,
take the one whose bonded H₂ word has the least `tr_M`.

Applying the min-action rule to a finite set of words rather than to an LP over an operator
basis is a reading of `prop:confinement-lp`. It is not the LP itself, and it is stated as such.

## What is fixed (taken from the corpus, not chosen)

- Everything in `h2_ruled_electron/PREREGISTRATION.md` that is not about the bond: nucleon `V^m`,
  `m ∈ {3, 6}`; electron `σ₀σ₁σ₀`; six-strand atoms with no p–e or junction letter; atom 1 `pe`,
  atom 2 `pe` or `ep` (four cells); reading 3 under convention D at the proton pin `q₀`, every
  level 1…12; mpmath 40 dps, `TOL = 1e-25`; the code of `h2_ruled_electron` / `h2_gg_atom` /
  `h2_one_rule` reused unchanged.
- `tr_M = Σ_λ y_λ χ_λ` at level 12, convention D, as computed there. The quantity reported is the
  ratio `tr_M(bonded) / tr_M(bare)`.

## The candidates

All words in the letters `V₄, V₅` (γγ-produced, `bondWord_gammaGamma_iff`) of length 1 to 6:
`2 + 4 + 8 + 16 + 32 + 64 = 126` words. Keep a word if

1. it is **atom-preserving**: its permutation of the junction strands 4…7 maps {4, 5} to itself;
2. it is **not split**: after free reduction of adjacent `σᵢ^e σᵢ^{−e}`, some letter is `σ₅^{±1}`.

These are the Python mirrors of `atomPreserving` and `!splitAcross` in the Lean file. Check C1:
for lengths ≤ 3 the kept set is exactly `{V₄³, V₅³}`, as `gg_atom_bonds` states.

## What is measured, and the hypothesis

For each kept word and each cell: reading 3 at every level, and the trace ratio.

**Hypothesis H.** In every cell, the minimum trace ratio over kept words that pass reading 3 is
attained by `V₄³` or `V₅³` (or both, tied).

Outcomes, all reported:

- (i) H holds in all four cells: min action extends the selection to six photons.
- (ii) H fails in some cell: a longer word has smaller trace. That word is reported, and the
  min-action reading does **not** select `V³` there.
- (iii) Ties with longer words: reported as ties; no tie-break is chosen.

The probe does not try any other rule if H fails, and does not change the candidate set after
seeing numbers.

## Not covered

More than six photons; words with `σ` letters (excluded by the γγ rule); other `q`; elements
rather than monomials (route 4, done in `h2_two_photon_element`).
