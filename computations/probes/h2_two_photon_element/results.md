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

## Status of each step

- γγ grammar for the bond: a proved invariant (writhe), applied under the 2026-09-08 rule that
  canonical words are γγ-produced. Not derived for bonds specifically.
- Neutrality: the table is proved; that a bond must be neutral is the working conjecture of
  PR #8835, and its scope (bond vs. whole word) is not settled.
- The selection is a computation at `q₀` over at most three photons, not a proof.

## Not done

Elements with `σ` terms (`φ₀, φ₁` are fixed by nothing in the corpus); more than three photons;
other `q`; the trefoil backup electron.
