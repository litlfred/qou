# Pre-registration: the two measured-only items of audit §27A / §28, symbolically over Q(q)

Written and committed before `np_all_q_symbolic_probe.py` is run (owner ruling 2026-11-22, "Do all" on #9103).

Audit `docs/audits/2026-11-21-neutron-heavier-sign.md` records two identities measured exactly at a few
rational q and not proved:

1. §27A: over the whole six-strand braid image, the only reachable affine-bilinear pair term is
   c + κ(Q_aQ_b − αQ_a − βQ_b) with α + β = 1 (measured at q = 111/100 and 7/5).
2. §28: pp = nn for the Ř-compatible U_q pair Casimir (G-q, op = False) and for the KZ monodromy β_AB²
   (measured at q = 111/100, 7/5, 2 and the proton q₀).

Method: redo both computations with every entry an exact element of the rational function field Q(q)
(numerator and denominator in Q[q], normalised by gcd). No float, no numeric q. Same readout as the
numeric probes: ΔE_X = T_X/T_1, T_X(a, b) = Tr(K^{⊗6} Π_{a,b} V_A³ V_B³ X), V = σ_lo σ_{lo+1}⁻¹,
Jimbo Ř.

Predictions (stated before running):

- P1. The span of the 720 sector vectors over Q(q) has dimension 10.
- P2. The affine-bilinear solutions with κ ≠ 0 form one ray, with α(q) + β(q) = 1 as an identity in Q(q),
  and α, β not both zero, so no Coulomb form (α = β = 0, κ ≠ 0) is reachable.
- P3. pp − nn = 0 in Q(q) for G-q (op = False) and for M = β_AB². The control G-q (op = True) gives
  pp − nn ≠ 0 in Q(q).

What a result means. An identity in Q(q) holds at every q where the denominators and pivots used are
nonzero; the probe prints those polynomials so the excluded q are explicit. This is a computer-algebra
proof at n = 6 (tier "symbolic-exact"), not a Lean proof and not a statement about other n.
If a prediction fails, the failure is reported as found.
