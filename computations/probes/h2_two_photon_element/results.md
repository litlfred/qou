# Results: the H₂ bond as a two-photon element (route 4), and the γγ / neutrality filters (route 1)

Issue #8879. Pre-registration [`PREREGISTRATION.md`](PREREGISTRATION.md), commit `1ad26901e17`,
pushed before computing. Producer `h2_two_photon_element_probe.py`, witness
`h2-two-photon-element.witness.json`, 2/2 checks, 22 s. Lean
`QOU/Molecular/H2BondSelectionRoutes.lean`.

## Route 4. Outcome (iii): every element passes, so the element test selects nothing

Photon coefficients fixed by the proved factorisation `V³ = γ(0,0,qh)·γ(0,0,−q⁻¹h)`:
`a₊ = qh = 0.232052…`, `a₋ = −q⁻¹h = −0.188346…`.

| element | passes, all 4 cells | trace ratio | least character |
|---|---|---|---|
| one photon `1 + a·V_s` (4) | yes | 0.937 – 1.077 | 0.442 – 0.511 |
| two photons, one window (= `V_s³`) (2) | yes | 0.997 – 1.0 | ≈ 0.47 |
| two photons, two windows (4) | yes | 0.986 – 1.014 | ≈ 0.47 – 0.48 |

- **C1.** The one-window element equals `V_s³` to relative `6e-41` in every cell, so the
  factorisation holds in `H₁₂` through the windows.
- **C2.** The `V_s³` characters reproduce `h2-ruled-electron.witness.json` exactly (384 characters).
- **Why it cannot select.** Every element carries the identity term (the photon not absorbed)
  with coefficient `1`, and `|a| ≤ 0.23`. The bare word passes with characters near `0.47`,
  so every element passes with a wide margin, including the single photon `1 + a·V_s`, whose
  monomial `V_s` fails on its own. Reading 3 on an element is dominated by its unabsorbed term.
- **Priors.** P1 (C1 holds, `V³` passes) yes. P2 (no one-photon element passes) no.
  P3 (no two-window element passes) no.

So read as an element, the photon does not separate bonds under reading 3. The monomial
reading of `h2_ruled_electron` is the one that discriminates.

## Route 1. The γγ invariant and neutrality on the bond (Lean, no `sorry`)

- `bondWord_gammaGamma_iff`: a bond over `{σ₄, σ₅, σ₆, V₄, V₅}` is a γγ-produced word iff it
  uses only `V₄, V₅`. The invariant is the writhe: γγ words have writhe `0`
  (`writhe_eq_zero`), and a bond's writhe is its number of `σ` letters (`writhe_bondWord`).
- `sigma5_sq_not_gammaGamma`: `σ₅²` is excluded.
- `neutral_table` (by `decide`, no axioms): with the U(1) colouring of PR #8835 on the four
  junction strands, `V_s`, `V_s²`, `V_s³` are neutral at both sites; `σ₅²`, `V₅V₄`, `V₅²V₄` are not.

Read against `h2-ruled-electron.witness.json` (no new compute):

| filter on the bond | passing bonds that survive |
|---|---|
| γγ grammar | `ep`: `V₄³, V₅³, V₅²V₄`; `pe`: those and `V₅V₄` |
| U(1) neutrality of the bond's closure | `V₄³, V₅³`, all four cells |

Neutrality of the bond selects `V³` uniquely (up to the site) among the 155 bonds. Neutrality
of the whole H₂ word selects nothing, because the electron `σ₀σ₁σ₀` closes to a Hopf link and is
itself not neutral (self-writhe 1, linking 2 in each atom).

## A third filter: the bond preserves the particles

A bond is **pure** if it permutes no junction strand. Then the closure of the bonded word has
exactly the components of the bare word: no constituent is merged with or split from another.
Measured against `h2-ruled-electron.witness.json`:

- The pure bonds are 11 of the 155 (`σ₄², σ₅², σ₆²`, `V₄³`, `V₅³`, and six three-letter words
  such as `σ₄V₄σ₅`). All 11 pass reading 3 in all four cells, and they are exactly the passing
  bonds that leave the component partition of the H₂ closure unchanged.
- Lean `pure_writhe_zero_bonds` (`decide`, over all 155 bonds, `allBonds_length`): the pure bonds
  with writhe `0` are exactly `V₄³` and `V₅³`.

So **purity + writhe 0 selects `V³`** without reading 3 doing any of the selecting: every pure
bond already passes. Purity replaces the neutrality step; writhe 0 is the one premise left, and
it follows both from the γγ grammar (`writhe_eq_zero`) and from U(1) neutrality
(`writhe_eq_zero_of_neutral`, #8835). On a pure bond, neutrality is the statement that every
pairwise linking number vanishes, which is what the Borromean `V³` satisfies and the Hopf clasp
`σ₅²` does not.

## Writhe 0 from two candidate sources (2026-11-21, later)

**(A) The bond is achiral.** Lean `QOU/Molecular/H2BondMirror.lean`, sorry-free, axioms
`propext, Classical.choice, Quot.sound`:

- `mirror n : BraidGroup n →* BraidGroup n`, `σᵢ ↦ σᵢ⁻¹`, built on the Artin presentation (both
  relator families checked). In the Hecke algebra this is the bar involution on the braid part.
- `exponentSum_mirror`: the mirror negates the writhe.
- `writhe_eq_zero_of_conj_mirror`: a braid conjugate to its own mirror has writhe `0`.
- `mirror_vPow_three_conj`: `Vᵢ³ = (σᵢσᵢ₊₁⁻¹)³` is conjugate to its mirror, by
  `c = (σᵢσᵢ₊₁σᵢ)⁻¹σᵢ₊₁⁻¹` (conjugation by `Δ = σᵢσᵢ₊₁σᵢ` swaps `σᵢ` and `σᵢ₊₁`).
- `sq_not_conj_mirror`: `σᵢ²` is not.

So **pure + achiral selects `V³`**: among the 155 bonds, achiral implies writhe 0, the pure
writhe-0 bonds are exactly `V₄³, V₅³` (`pure_writhe_zero_bonds`), and both are achiral. This
replaces the γγ-grammar and neutrality premises with one that needs no particle content: the
bond has no handedness. The step from the `BondLetter` list to the braid group element is by
hand (each letter is `σ` or `V` at a fixed site); it is not a Lean bridge yet.

Status: achirality of the bond is a reading, as purity is. It is not stated as a rule in the
corpus. Its natural source is that the H₂ ground state is invariant under the bar involution
`q ↦ q⁻¹`, which the corpus uses for parity questions but has not ruled for bonds.

**(B) The two-term charge insertion cannot supply writhe 0.** This is a scope-(b) negative with
a proved invariant: `derived_insertion_closed_form` (`H2RuledElectronBond.lean`) shows the
derived insertion is a scalar on each total-weight space of `V^{⊗N}`, whichever strands carry
the leptons, and `derived_insertion_eq_of_total_eq` makes it equal across those choices. A
braid word preserves total weight, so the insertion commutes with every word and its connected
part is `0` on every bond. It therefore assigns the same value to `V³` and to `σ₅²`, and to
every bond of every writhe. It cannot constrain the writhe.

## Status of each step

- γγ grammar for the bond: a proved invariant (writhe), applied under the 2026-09-08 rule that
  canonical words are γγ-produced. Not derived for bonds specifically.
- Neutrality: the table is proved; that a bond must be neutral is the working conjecture of
  PR #8835, and its scope (bond vs. whole word) is not settled.
- Achirality (A above): proved to imply writhe 0; that a bond must be achiral is a reading.
- Purity as "the bond preserves the particles": a reading of what a bonded state of the same
  constituents is. Natural, but not stated as a rule in the corpus.
- The selection is a computation at `q₀` over at most three photons, not a proof.

## Not done

Elements with `σ` terms (`φ₀, φ₁` are fixed by nothing in the corpus); more than three photons;
other `q`; the trefoil backup electron.
