# Pre-registration: does photon exchange between two nucleon blocks go as Q_A·Q_B? (2026-11-22)

Thread "Settle the neutron-heavier sign". Owner 2026-11-22, on the Coulomb answer: "Do 1 2", where
option 1 is "formalize in Lean, pre-registered: the photon exchange between two nucleon blocks gives
a pair term ∝ Q_i·Q_j". Written before `np_two_block_photon_exchange_probe.py` exists or is run.
No number from it has been seen.

## Setup (fixed in advance)
- Level-2 Jimbo braiding Ř = [[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]], h = q − q⁻¹,
  K = diag(q, q⁻¹), u = bit 0, on (C²)^{⊗6}.
- Block A on strands 0–2, block B on strands 3–5. Each block is the ruled nucleon core
  V³ = (σ_iσ_{i+1}⁻¹)³ with i = 0 (A) and i = 3 (B), per ruling A (2026-11-22).
- Block charge Q = (number of u bits on the block) − 1 ∈ {−1, 0, 1, 2}; p has Q = 1, n has Q = 0.
  Π_a ⊗ Π_b projects onto block charges (a, b).
- T_X(a, b) = Tr(K^{⊗6}·(Π_a ⊗ Π_b)·V_A³·V_B³·X). K^{⊗6} and Π_a ⊗ Π_b commute with V_A³V_B³, so
  the placement of X in the word does not matter up to cyclicity.
- The exchange insertions X are the monomials of the ruled photon
  γ = 1 + φ₀σ_i + φ₁σ_{i+1} + φ₀₁σ_iσ_{i+1}⁻¹ that touch both blocks, for the photon on strands
  1–3 and on 2–4: X ∈ {σ₂, σ₁σ₂⁻¹, σ₂σ₃⁻¹}, plus σ₂⁻¹ and the second-order σ₂², σ₂⁻².
  Each is reported separately; none is preferred.
- Pair shift ΔE_X(a, b) = T_X(a, b)/T_1(a, b), where T_1 = T with X = 1 (which factorises over
  the blocks). Sectors with T_1 = 0 are reported and excluded.
- Exact arithmetic only: sympy over Q(q), checked at q = 111/100 and q = 7/5 with Fraction.

## Outcomes (one is reported per X; no prior is stated because I have none)
- **O1, Coulomb form.** ΔE_X(a, b) = c + κ·Q_a·Q_b for all valid (a, b), with κ ≠ 0.
  Then a neutral block feels nothing beyond the constant c: pn = np = nn.
- **O2, isospin form.** ΔE_X(a, b) = c + κ·W_aW_b with W = 2Q − 1. Then pp = nn ≠ pn
  (charge symmetric). This is what an su(2)-only braiding would be expected to give.
- **O3, affine-bilinear.** ΔE_X = c + α·Q_a + β·Q_b + κ·Q_aQ_b with (α, β) ≠ (0, 0) and not of
  form O2. A bilinear piece exists but a neutral block still feels the exchange.
- **O4, not bilinear.** The double-centred matrix of ΔE_X over (a, b) is not rank one along the
  charge vector.

O1 and O2 differ only by one-block terms, so they are separated by the neutral rows, not by the
double-centred matrix. Both are tested on the four nucleon pairs (pp, pn, np, nn) and on all 16
charge pairs.

## What a result means
- O1 for some X: the ruled photon gives a charge-charge pair term. That is the missing link in
  §25 of `docs/audits/2026-11-21-neutron-heavier-sign.md`, and it would be formalized in Lean.
- O2, O3 or O4 for every X: no single-photon insertion between two V³ blocks gives a Coulomb pair
  term. That is a scope-(a) negative for these insertions only; it does not exclude Coulomb from
  longer exchanges, other placements or a different trace.
- No value is compared with experiment. κ is not converted to MeV here.
