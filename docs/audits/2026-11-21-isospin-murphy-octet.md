# Weighted Murphy sums on the octet (2026-11-21, owner chose "hypercharge-Murphy sum")

Lean: `QOU/BraidsAndKnots/IsospinMurphyOctet.lean` (sorry-free, lean-direct exit 0; axioms propext, Classical.choice, Quot.sound).
Probe: `computations/flavour_strange_strand/murphy_octet_probe.py` (exact over Q(q); q₀ only in display lines).

Setting: Jimbo braiding on (C³)^⊗3, Jucys–Murphy elements L₁ = 1, L₂ = σ₁², L₃ = σ₂σ₁²σ₂.
Weighted sum M_w = Σ_k w(flavour on strand k)·L_k. Splitting of an isospin pair: D = tr_lo(M_w) − tr_hi(M_w).

## Lean (two strands)
- `murphy2_diag`: diagonal of L₂ = Ř² is q² on eᵢ⊗eᵢ, 1 on eᵢ⊗eⱼ (i<j), 1+h² on eᵢ⊗eⱼ (j<i), h = q−q⁻¹.
- `murphy2_pair_trace`: trace of L₂ on {eᵢ⊗eⱼ, eⱼ⊗eᵢ} is 2+h² for every pair of distinct flavours.
- `weightedMurphy2_pair_trace`: weighted trace is 2(wᵢ+wⱼ) + wᵢh². The h² term is the position-sensitive part.

## Results (exact, three strands)
| weight | functional | n−p, Σ, Ξ splittings | Coleman–Glashow Σ = N + Ξ | α₂/α₁ (first order) |
|---|---|---|---|---|
| hypercharge Y | tr M, tr V³M | **0, 0, 0** exactly | trivially | — |
| isospin I₃ | tr M, tr V³M | nonzero | **exact in q** | (2/3)(q−1) + … |
| charge Q = I₃ + Y/2 | tr M, tr V³M | same as I₃ | exact | (2/3)(q−1) + … |
| Y or I₃ or Q × isospin Cartan q^{H₁} | tr M | nonzero | broken at O((q−1)²) | Y: −2 + …; I₃: (2/3)(q−1); Q: (4/3)(q−1) |

- **Hypercharge-Murphy alone cannot split any isospin pair**: Y treats u and d alike, so the operator is U_q(sl₂)_{ud}-invariant (sketch; exact compute confirms). Derived zero, not a neglected term.
- **The charge (or isospin) Murphy sum is the first operator tested that gives α₂ ≠ 0 and keeps Coleman–Glashow exact.** α₂ comes from the q-deformation (h² term), first order in q−1.
- Its sign: α₂/α₁ > 0 for q > 1 under every flavour order tried (u<d<s, s<u<d, u<s<d, d<u<s); first-order coefficient 2/3 in all four. Not a convention choice.

## Comparison boundary (physics enters only here)
At q₀: α₂/α₁ ≈ +0.056 (tr M), +0.059 (tr V³M). Lattice QCD parts (Horsley et al.) imply α₂/α₁ ≈ −0.141.
Scope (a): this operator, alone, has the right structure (exact CG, α₂ from q-deformation) but the wrong sign and about 0.4× the size.
It is not excluded from a fuller assembly (e.g. with the electromagnetic two-term charge operators, or a sea strand).

## Open
- Lean for the three-strand statements (Y-blindness, exact CG of the I₃/Q-Murphy trace, α₂ series).
- Why the sign is positive: whether a different trace (quantum trace, two-term Lagrangian trace per the 2026-11-21 ruling) flips it.
