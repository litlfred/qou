# Pre-registration: ⁴He with every nucleon pair bonded, by formation route

**Owner ask (project thread, 2026-11-21, issue #8960):** "Why only three strands? Not all γγ
production should be on same strands. Look at how He formed."

Written and pushed **before** any number below is computed.

## Why

`QOU/Mass/StrandLayoutForcesChain.lean` proves that, with nucleon k on strands 3k..3k+2, a single
generator joins two nucleons only when they are neighbours. So the production atom word
(`atom_braid_word_3A`) can only write the chain: A − 1 bonds, 3 for ⁴He, which has 6 pairs. A bond
between non-neighbours needs a word that carries a strand past the nucleons in between.

## Word

Everything is the production word except the extra bonds. Nucleon order is the production order,
Z protons then N neutrons (⁴He = p₀ p₁ n₂ n₃). Nucleon blocks are `atom_braid_word_3A(Z, N,
include_inter=False)`, unmodified. Bond letters are the production ones, read off the production
word, by pair type: pp = σ, pn = σ − h(½ − δ/4), nn = σ − h.

**Transported bond** for nucleons i < j: `T · b · T⁻¹`, with `b` the pair-type letter on generator
3j − 1, and T carrying nucleon i's last strand (3i + 2) to position 3j − 1:

- **over:** T = σ_{3i+2} σ_{3i+3} ⋯ σ_{3j−2}
- **under:** T = σ⁻¹_{3i+2} σ⁻¹_{3i+3} ⋯ σ⁻¹_{3j−2}

For j = i + 1, T is empty and the bond is the production letter on 3i + 2. Both variants are run and
reported; neither is chosen.

**Atom word for a route** = the free word, then the route's bonds in route order.

## Routes (⁴He = p₀ p₁ n₂ n₃)

Within a stage, pairs are taken by span (j − i) ascending, then left index ascending. This rule is
fixed here, before running.

| route | stage 1 (the clusters that form first) | stage 2 (the bonds made when they fuse) |
|---|---|---|
| D + D, pairing a | D = (0,2), D = (1,3) | (0,1), (2,3), (1,2), (0,3) |
| D + D, pairing b | D = (0,3), D = (1,2) | (0,1), (2,3), (0,2), (1,3) |
| ³H + p | ³H = (1,2,3): (1,2), (2,3), (1,3) | (0,1), (0,2), (0,3) |
| ³He + n | ³He = (0,1,2): (0,1), (1,2), (0,2) | (2,3), (1,3), (0,3) |

Both D + D pairings are run; neither is chosen.

**A = 3, for growth with A:** ³H = p₀ n₁ n₂ and ³He = p₀ p₁ n₂, bonds (0,1), (1,2), (0,2).
²H has one pair and is unchanged.

**Controls.**
1. The production word itself must give the production tr_M(atom) (`tr_m_atom_zn`) exactly.
2. The chain bonds (0,1), (1,2), (2,3) appended after the free word (rather than interleaved)
   measure what appending alone does.

## Reported

For every word: tr_M(free), tr_M(atom), B_log = E₀ ln(tr_free/tr_atom) (the posited form B_sym
uses, so directly comparable with its 8.767 MeV), and B_diff = E₀(tr_free − tr_atom) (the
Frobenius-pairing form). E₀ is the dashboard's tower-summed E₀. AME 2020 appears only in a
comparison column.

## What would be read from it

Nothing is adopted. The transported bond, its over/under variant, the route rule and the
nucleon order are modelling choices written down here. **Choosing a route, a pairing or a variant
because its number is closer to AME would be selection against the target.** Every row is
reported. The result measures how much of the ⁴He gap a bonded-pairs word recovers, under this
construction alone; it does not decide which word the physics wants.
