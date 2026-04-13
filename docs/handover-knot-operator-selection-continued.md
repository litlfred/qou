# Session Handover: Knot Operator Selection (continued)

## Branch: `claude/docs-handover-knot-operator-k3XxB`

## What was accomplished

### 1. Content blocks (Ch 11 §9): 11 new + 3 updated
- Branching Q-value framework: per-nucleon channel decomposition,
  spectator normalization, branching factorization, parity regime
  selection, positron correction, tritium symbolic Q-value,
  Frobenius positivity filter
- 3 remarks: mass ordering corrected, categorical quantity map,
  B₃ local minimum
- Updated: confinement-lp, q-value-transition, markov-trace-product,
  categorical-proton, categorical-neutron, mass-endomorphism-tower,
  atomic-braid-mass

### 2. Corrected tr_M(e⁻) = z³ (not hz²+z)
- Fixed in 9 computation scripts
- Reran 15 witnesses from scratch
- Recomputed Gram matrix (now 5+ 1- indefinite)

### 3. Integer LP derivation of gluon count
- 9-crossing proton (B₃ + quarks) is LP UNSTABLE: Gx[γ] < 0
- Integer LP over {σ₀, σ₁, L₊, L₋}: optimal = σ₀→σ₀ (2 crossings)
- Neutron: deeper instability, needs L₊→L₋ (4 crossings)
- The gluon is DERIVED, not assumed

### 4. Proton stability boundary (symbolic in q)
- 9-cross proton stable ⟺ P(q²) ≥ 0 where
  P(u) = u⁶-3u⁵+5u⁴-8u³+5u²-3u+1
- Critical q ≈ 1.104: stable below, unstable above
- Our q₀ = 1.110 is just above → gluon barely needed

### 5. Per-irrep vector action engine (hecke-irrep)
- --vector mode: O(dim) per crossing
- --confine mode: min-eigenvalue confinement eigenvector
- --knots mode: all 6 operators × all irreps
- ⁶He all 10 irreps (including dim=13260) in 90 seconds

### 6. Q-values (zero fitting, 3 CODATA inputs)
| Quantity | Predicted | Observed | Error |
|----------|-----------|----------|-------|
| Q(n→p) | 0.7816 MeV | 0.7823 MeV | −0.10% |
| Q(³H→³He) | 0.0179 MeV | 0.0186 MeV | −3.6% |
| Q(⁶He→⁶Li) | 3.637 MeV | 3.508 MeV | +3.7% |

### 7. Mass tower eigenvalue structure
- Electron eigenvalues in std rep: (−q, q⁻¹) — ON convergence boundary
- Muon eigenvalues: (−1, +1) — exactly ±1 for all q
- Brane tower has pole at k = n (crossing number) in sym channel
- The pole is the mass resonance; regularization across all channels
  gives the mass

## What was NOT accomplished (rediscovered instead)

The mass formula is ALREADY in the paper:
- **m_p via Borromean volume × color-tube amplification: 0.0006% error**
  (baryon-period-conjecture.md)
- **m_μ/m_e via jet-prolonged Seiberg-Witten integral**
  (lepton-mass-integrals.md, generation-dependent-sw.md)
- **Atomic masses Z=1-20 via Wedderburn 3-channel: 0.074% mean error**
  (atomic-braid-mass.md)

I spent significant time trying to derive the muon mass from
Φ_q towers and dual Frobenius actions when the paper already
has the correct framework (SW period integrals at jet degree k).

## What SHOULD be done next

1. **Connect the integer LP gluon derivation to the existing
   mass framework.** The LP stability requirement (gluon needed
   for q₀ ≈ 1.110) should connect to the Picard-Lefschetz
   thimble structure — the gluon is the topological defect at
   the discriminant pole.

2. **Recompute the baryon period integral with corrected
   tr_M(e⁻) = z³.** The existing computation may use the old
   trace value.

3. **Run the even-A Frobenius filter for ⁶He from scratch.**
   Currently using handover value (3.637 MeV). Need individual
   G_P(c), G_N(c) channel values.

4. **Extend Q-value predictions to ¹⁴C, ⁶⁰Co, ⁹⁰Sr, ¹³⁷Cs, ²¹⁰Bi**
   using the branching factorization + CRT engine.

5. **The mass functional question is SETTLED by the existing paper:**
   Mass = SW period integral (not Φ_q tower directly).
   The Φ_q tower is the transient component of the categorical
   mass decomposition, but the full mass uses the Picard-Lefschetz
   thimble integration over the color-tube cubic.
