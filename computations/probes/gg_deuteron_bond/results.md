# Results: the deuteron with a γγ-selected p-n bond

Pre-registration: [`preregistration.md`](preregistration.md), commit `a06ae62c2b2`, pushed before computing.
Producer `gg_deuteron_bond_probe.py`, witness `gg-deuteron-bond.witness.json`, 3/3 checks. mpmath 40 dps
(the `h2_one_rule` helpers), convention D, proton pin, `E₀ = m_e/(q₀(q₀−1)) = 4.18598` MeV.
Run time under 1 s.

## Calibration

- K1: the bare nucleons V³ and V⁶ pass reading 3 on three strands, as in `h2-gg-atom.witness.json`.
- K2: inserting the production-style interface letter `σ₂ + d·1` between the two nucleons gives the
  trace ratio `z_D + d` to better than 1e-30 (the Markov property), for m = 3 and m = 6.

## Rows

Free word `x = Vᵐ ⊗ Vᵐ` on six strands. Both bare words pass reading 3 at every level
(tr = 0.997126 for m = 3, 0.988547 for m = 6).

| m | bond | reading 3, every level | first failing level | ratio r | −E₀ ln r (MeV) |
|---|---|---|---|---|---|
| 3 | V(1) | fail | 4 | 0.25043 | 5.796 |
| 3 | V(1)² | fail | 3 | 0.28482 | 5.257 |
| 3 | **V(1)³** | **pass** | — | **0.998497** | **0.006296** |
| 3 | V(2) | fail | 5 | 0.24343 | 5.914 |
| 3 | V(2)² | fail | 4 | 0.27782 | 5.361 |
| 3 | **V(2)³** | **pass** | — | **0.998497** | **0.006296** |
| 6 | V(1) | fail | 4 | 0.25417 | 5.734 |
| 6 | V(1)² | fail | 3 | 0.29033 | 5.177 |
| 6 | **V(1)³** | **pass** | — | **0.998420** | **0.006620** |
| 6 | V(2) | fail | 5 | 0.24046 | 5.966 |
| 6 | V(2)² | fail | 4 | 0.27599 | 5.389 |
| 6 | **V(2)³** | **pass** | — | **0.998447** | **0.006505** |

## Outcome

**(i): a γγ bond exists, and it is V³ at either junction site, for both nucleon words.** This is the
same bond letter the H₂ probe selects. Its trace drop is tiny: the log law gives the deuteron
`B ≈ 0.0063` MeV in this cell, **−99.7 %** against AME 2.224566 MeV. The bonds that would bind by a
few MeV (V, V²) fail reading 3, so ruling B and the γγ rule exclude them. Their binding was not used.

## What this says about the +27.4 %

The +27.36 % on the production word comes from its single-crossing interface letter, whose trace
ratio is `z_D + d_pn = 0.5082`. That letter is not a γγ word, and the 2026-11-15 owner ruling covers
bond letters. In this cell the γγ rule admits only V³, whose ratio is 0.9985. So the +27 % is not a
small error on a correct input. Replacing the input by a γγ-selected bond moves the deuteron from
+27 % to −99.7 %. The +27 % was produced by the non-γγ letter.

Observation, not a claim: the V³ bond ratio 0.998497 (m = 3) is close to the Markov trace of the bare
Borromean core, |tr_M(β_Bor)| = 0.998562 (`mass_at_3A_proper.atom_braid_word_3A` docstring), but not
equal to it (difference 6.5e-5).

## Relation to the existing γγ chain result

This is **not** the first γγ deuteron. `docs/audits/2026-11-22-light-nuclei-a2-a3-gg-chain.md`
(Lean `QOU/Mass/LightNucleiGGChainSign.lean`, sorry-free) puts the same V³ bond on the
**production** proton and neutron blocks and proves that every chain unbinds at every q > 1:
²H ratio 1.000611 (pn) or 1.001058 (np), B_log −2.6 to −4.5 keV. This probe uses the
**γγ nucleons** V³ / V⁶ of `../h2_gg_atom/` instead, and the ratio falls just below 1
(0.998497), so B_log is +6.3 keV. The two cells differ only in the nucleon block, and they agree
on the point that matters: on the ruled V³ bond the deuteron's binding is of order keV, about
350× (here) to 860× (production blocks) below AME, with a sign that depends on the nucleon
block. By the 2026-11-22 ruling (closure on the right, a bond enters the newer nucleon) the
canonical site here is s = 2; s = 1 is reported for completeness and gives the same ratio at m = 3.

## Scope

Scope (a): this family (bonds V(s)ᵏ, s ∈ {1, 2}, k ≤ 3), the three-strand γγ nucleons V³ and V⁶,
convention D at the proton pin, order-zero E₀. In this cell the proton and the neutron are the same
word, so it cannot distinguish the deuteron from the diproton or dineutron. Flavour needs more
strands or a non-γγ letter (`../h2_gg_atom/results.md`). Longer γγ bonds (more than one vertex
pattern, or vertices on more than two generators) are outside the enumeration.

## Addendum 1, Phase A: every γγ bond word on all six strands

Producer `gg_deuteron_all_bonds_probe.py`, witness `gg-deuteron-all-bonds.witness.json`, L = 6.
**Correction to the addendum:** it listed vertices `V(0)…V(4)`. On six strands the generators are
0–4, so `V(i) = σᵢσᵢ₊₁⁻¹` exists only for i ≤ 3. The run uses `V(0)…V(3)` (5334 words containing
`V(1)` or `V(2)`), not the 19530 the addendum counted. Nothing else changed.

| nucleon | bond words | pass reading 3 | pure junction (V(1), V(2) only) | touching a nucleon (V(0) or V(3)) |
|---|---|---|---|---|
| V³ | 5334 | 408 | 14 | 394 |
| V⁶ | 5334 | 422 | 15 | 407 |

`B` over the passing set: −0.16 to +7.67 MeV. No passing word, in either set, lies within 5 % of AME.

Pure-junction passers (V³ nucleon; V⁶ is similar):

| length | word | ratio | B (MeV) |
|---|---|---|---|
| 3 | V(1)³, V(2)³ | 0.998497 | 0.0063 |
| 4 | V(1)V(2)V(1)V(2) | 1.035874 | −0.148 |
| 4 | V(2)V(1)V(2)V(1) | 1.032898 | −0.135 |
| 6 | V(1)⁶, V(2)⁶ | 0.99414 | 0.025 |
| 6 | V(1)³V(2)³ and four reorderings | 0.99692–0.99694 | 0.0128–0.0129 |
| 6 | V(1)V(2)²V(1)V(2)² | 0.454088 | 3.305 |
| 6 | V(2)²V(1)V(2)²V(1) | 0.444397 | 3.395 |

With the V⁶ nucleon, two further length-6 words reach 5.851 MeV. The cheapest passing bond by
crossing count (the corpus `FrobeniusSelected` rule) is V(1)³ / V(2)³, the bond of the first run.
Words that touch a nucleon cluster near 5.6–5.7 MeV (median), mostly because they rewrite a
nucleon's own word, e.g. V(2)V(3) = σ₂σ₄⁻¹.

Owner card 2026-11-25: which of these sets counts as the p–n bond is decided after this table
(card 1, answer C). Nothing here selects.

## Selection under owner card 1 (2026-11-25)

Owner, after this table: *"go"*, taken as acceptance of the recommendation on card 1 (A): a p–n
bond is a pure-junction γγ word (vertices V(1), V(2) only), and among those that pass reading 3 the
bond is the cheapest by crossing count. That is the corpus selection rule `FrobeniusSelected`
(`QOU/Mass/GammaGammaFrobeniusSelection.lean`), the same rule that picks the nucleon V³ = β_Bor on
three strands. The nucleon is therefore V³ as well (cheapest passing γγ nucleon), and by the
2026-11-22 ruling (a bond enters the newer nucleon) the site is s = 2.

**Selected deuteron in this cell:** nucleons V³ ⊗ V³, bond V(2)³ = (σ₂σ₃⁻¹)³.
Trace ratio 0.998497160633, `B = −E₀ ln r = 0.006296` MeV at order-zero E₀ (0.006358 MeV at the
ruled brane-tower E₀ = 4.227483, owner card 4), against AME 2.224566 MeV: **−99.7 %.**

So under the γγ rule, reading 3 and the corpus selection rule, the deuteron is bound by about
6 keV, not 2.2 MeV. This agrees in magnitude with the 2026-11-22 result on production blocks
(unbound by 3–4 keV). The +27.4 % of the superseded interface letter is replaced by −99.7 %. The
selection was made by the rule, not by the binding: the bonds that bind by MeV are either not pure
junction or not cheapest. Scope (a): three-strand γγ nucleons (p = n), bonds up to six vertices,
convention D, proton pin. The flavoured four-strand cell (Phase B) is running separately.
