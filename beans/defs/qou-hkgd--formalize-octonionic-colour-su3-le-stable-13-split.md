---
# qou-hkgd
title: Formalize Octonionic Colour SU(3) Le-Stable 1+3 Splitting (C + C^3) & 6D Colour Triplet Restriction
status: completed
type: task
priority: high
created_at: 2026-11-18T22:15:54Z
updated_at: 2026-11-24T03:35:25Z
parent: qou-rgj8
---

Formalize QOU/StandardModel/OctonionColourTripletSplitting.lean (0 sorry, 0 axiom) extending QOU.MathlibExt.OctonionComplexStructure and OctonionSU3RankSix: (1) Define the 2D trivial singlet projection P_singlet onto span(e_0, e_1) and the 6D colour triplet projection P_triplet = id - P_singlet onto span(e_2,...,e_7) in O = (Fin 8 -> Q); (2) Prove P_singlet^2 = P_singlet, P_triplet^2 = P_triplet, P_singlet o P_triplet = 0, and prove that both P_singlet and P_triplet commute with the complex structure Le (Le^2 = -id); (3) Prove that every derivation D in su3(stdIm) annihilates the 2D singlet subspace (D e_0 = 0 and D e_1 = 0, so D o P_singlet = 0 and P_singlet o D = 0) and restricts to a faithful, Le-commuting (C-linear), bracket-preserving action on the 6-dimensional (3_C-dimensional) colour triplet subspace range(P_triplet).

Verified 100% merged on origin/main (48f446490cc / PR #8525 917b6939954, OctonionColourTripletSplitting.lean, 0 sorry) and cross-checked over Q^64 in Batch 7 witness (8dc5481929b).
