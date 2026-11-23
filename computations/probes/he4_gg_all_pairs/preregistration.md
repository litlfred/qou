# Pre-registration: ⁴He with γγ-selected bonds on every pair

Issue #8960, PR #8969. Written before any γγ ⁴He number is computed.

## Why

Owner, 2026-11-21: *"Are you using γγ production for this? P-n-p-n seems chosen, not
derived"*, *"Order is from GB reduction?"*. Card choice "1+2 now, then 3".
Steps 1 and 2 (`QOU/Mass/BlockRelabelConjugation.lean`,
`../he4_order_conjugation/`) showed nucleon order is a conjugation and changes no
trace, so it is not an input. This probe is step 3. It replaces the superseded
single-crossing bond letters with the γγ-selected bond.

## The word

- Nucleon blocks: the production free word `atom_braid_word_3A(Z, N, include_inter=False)`.
  These are the same 11-letter blocks the γγ pair probe uses.
- Bond: `G³ = (σ_{3j−1} σ_{3j}⁻¹)³`, the bond selected by reading 3 on the `H₆` interface
  (`QOU/Mass/GammaGammaH6Interface.lean`, `interfaceSelected_three`). For neighbours
  `j = i + 1` this is the γγ pair probe's bond exactly.
- Non-neighbours: `T_ij · G³ · T_ij⁻¹`, with `T_ij` from `TransportedPairBond.lean`. It carries
  nucleon i's last strand to `3j − 1`, so G³ touches that strand and nucleon j's first two.
  Over (positive crossings) and under (negative crossings) are both run.
- Formation routes: the same four ⁴He routes as the superseded-letter probe (D+D pairing a,
  D+D pairing b, ³H + p, ³He + n). The bond list is in route order, and each bond is placed
  after the block of its right nucleon (an equal element, as before).

## Controls

1. ²H chain with G³ reproduces μ_pn(G³) = 1.00061119140688… from
   `gamma-gamma-bond-is-pair-independent.witness.json` (tolerance 1e−40).
2. The free word reproduces `tr_m_atom_zn` tr_free.
3. A = 3: the commuted arrangement equals the appended word (≤ 1e−50).

## Reported, nothing selected

For ³H, ³He and ⁴He: the γγ chain, plus every route × {over, under}. Each row gets tr_atom,
B_log = E₀ ln(tr_free/tr_atom), B_diff = E₀(tr_free − tr_atom), and AME/B (comparison only).
No route, transport or strand choice is selected. A negative B (unbinding) is a result.

## Not covered

- Which strands a non-neighbour bond joins. The production convention, kept here, is "i's
  last strand to j's first two". Step 2 showed relabelling moves bonds onto other strand
  pairs, so this is a remaining freedom, not a derived choice.
- Gröbner–Shirshov normal forms. GS reduction names an element and does not change its trace,
  so no number here depends on it. Computing the normal forms is a separate step if wanted.
- Many-body γγ vertices (a γγ event touching three nucleons).

## Amendment (before any ⁴He number)

Control 1 tolerance is relaxed from 1e−40 to 1e−28. The reference μ_pn in the pair witness
is stored to 30 significant digits, and the first run matched it to 2.5e−30. Nothing else
changes.
