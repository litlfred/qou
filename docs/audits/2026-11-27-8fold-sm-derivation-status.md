# 8-fold / Standard Model derivation: what is proved, what is assumed

Date: 2026-11-27. Thread: "close all gaps" on the 8-fold and Standard Model
derivation. Bean: `qou-h0zz` (stays open; its conjectures are not closed).

This is a status record, not a new result. Every "proved" row below is a
sorry-free Lean declaration on `main`. Every "assumed" row is an input that
the Lean takes as a definition or hypothesis, and that no QOU axiom yet
forces.

## Proved in Lean (on main)

| Result | Lean | PR |
|---|---|---|
| One neutral lepton fixes the hypercharge mix: `Q = T₃ + αY₀` with `α = 1/6` | `QOU/EightfoldWay/NeutralLeptonFixesCharges.lean` | #9633 |
| Strand labels separate the anti-up from the down | (same arc) | #9637 |
| Fermi exchange (`f j i = -f i j`) forces Λ²5 over Sym²5; the 10 wedges split 3 colour–colour + 6 colour–isospin + 1 isospin–isospin; Sym² would add a charge-2 colour singlet | `QOU/EightfoldWay/FermiPairWedge.lean` | #9651 |
| Cubic `Y₀` trace: 5̄ = −30, Λ²5 = 30, 5 = 30, Sym²5 = 270; `a·5̄ + c·Λ²5` cancels iff `a = c` | `FermiPairWedge.lean` (`cubic_cancel_iff`) | #9651 |
| Colour triality Z/3 is the colour centre, not a flavour phase (negative: it supplies no flavour label) | colour-triplet commutant | #9669 |
| The strand slot (colour / colIso3 / colIso4 / colCol) plus a dual flag separates the 8 first-generation quark states; the dual flag equals helicity; charges at α = 1/6 match and are colour-independent | `QOU/EightfoldWay/StrandSlotSeparatesGen1.lean` | #9674 |

The last row supplies the label that `ChiralityIndependentOfCrossing.lean`
(V9) proved the braid element alone cannot supply.

## Assumed (inputs, not derived)

1. **Strand count / multiplet shape.** Why a multiplet is one strand (5̄) or
   one strand pair (Λ²5). The Lean starts from the 5 = C ⊕ V decomposition.
2. **Georgi–Glashow slot assignment.** The map from states to slots is a
   `def` in `StrandSlotSeparatesGen1.lean`. Its consequences are proved; the
   map itself is not forced.
3. **Fermi exchange.** Antisymmetry `f j i = -f i j` is a hypothesis
   (`IsFermi`), not derived from the braid structure.
4. **No vector-like 5 ⊕ 5̄.** `cubic_5_add_5bar` shows 5 ⊕ 5̄ also cancels,
   so the cubic trace does not exclude it. Nothing yet does.

## Scope note

The negatives above are scope (a): each names what one construction does not
supply. None is a structural exclusion of an ingredient.

## Next step

Any of the four assumed rows. Item 4 (excluding 5 ⊕ 5̄) is the one with a
concrete target: a Lean statement whose hypotheses are QOU-native and whose
conclusion rules out the vector-like pair.
