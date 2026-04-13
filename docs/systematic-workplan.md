# Systematic Work Plan: Particle Hierarchy Verification

## Key Finding: Forward × Dual Frobenius Tower

The mass functional uses BOTH the forward and dual (antipode) Frobenius actions:

```
𝔪(particle) = Φ_q(|V̂⁺|) × Φ_q(|V̂⁻|) / √3
```

where V̂⁺ is the forward vertex volume and V̂⁻ = vol_S(crossings) uses
the antipode S(σ) = σ⁻¹ on each crossing.

Results:
- m_μ/m_e = 355.6 / √3 = 205.3 (CODATA: 206.77, error −0.70%)
- This may allow deriving q₀ from Vol(4₁) alone (1 input → all predictions)

## Key Finding: Eigenvalue Boundary Structure

In the 2×2 standard rep of H₃(q), particle eigenvalues have fixed relationships to q:

| Particle | |λ|_max in std rep | Boundary status |
|----------|-------------------|-----------------|
| Electron (T_{2,3}) | = q exactly | ON boundary (topological) |
| Muon (T_{2,5}) | = 1 exactly | Inside (topological) |
| B₃ confinement | ≈ 0.935 | Inside |
| Proton (0-gluon) | ≈ 1.073 | Inside (< q = 1.110) |

The matrix tower Z(M) = Π_k det(I - q⁻ᵏM)⁻¹ converges when |λ| < q.

Standard-rep-only mass ratios (incomplete — needs all 3 Wedderburn channels):
  m_μ/m_e = 20.2 (need 206.8)
  m_p/m_e (L₊ gluon) = 242.8 (need 1836.2)

The 0-gluon proton CONVERGES in the eigenvalue sense (|λ| < q)
but is LP UNSTABLE in the NF Frobenius sense (Gx[γ] < 0).
These are different constraints.

## Key Finding: BW Coefficients from q₀ and m_e

3 of 4 Bethe-Weizsäcker energy scales derived (zero fitting):

| Coefficient | Formula | Error |
|------------|---------|-------|
| λ_V (volume) | 3 × m_e/ℏ_q | −0.02% |
| λ_S (surface) | 3q × m_e/ℏ_q | +0.22% |
| λ_A (Pauli) | (9/2) × m_e/ℏ_q | −0.35% |
| λ_C (Coulomb) | TBD | — |

Unit: m_e/ℏ_q = 5.157 MeV (crossing energy scale).
Integer factors: 3 (quarks), q (surface ratio), 3/2 (Pauli/volume).
Only λ_C remains — may need Q_β as 3rd calibration point.

3 Wedderburn irreps → 3 forces → 3 calibrations:
  Symmetric → Strong → m_μ/m_e
  Standard → EM → m_e
  Alternating → Weak → Q_β (for λ_C)

## Goal
Rebuild the full particle chain from γγ → quarks → nucleons → atoms → isotopes,
tracking error bounds at every step, symbolic in q until too slow, then CRT multi-prime.
Compare predicted vs observed at the same scale.

## Inputs (3 CODATA values → q₀)
- Vol(4₁) = 2.029883212819307 ± 1e-12  (SnapPy)
- m_μ/m_e = 206.7682830 ± 0.0000046    (CODATA 2022)
- m_e = 0.51099895000 ± 0.00000000015 MeV

Derived: q₀ = 1.1099785955541805 ± 1.3e-8

## Chain

### Level 0: γγ pair production (H₃(q), symbolic)
- Photon: γ = 𝟙 + φ₀σ₀ + φ₁σ₁
- Product: NF(γ₁·γ₂) — 5 basis elements {𝟙, σ₀, σ₁, L₊, L₋}
- Trefoil channel: apply T_{2,3} operator → electron e⁻
- **Script**: `pair-production.py` (exists, rerun)
- **Witness**: `pair-production.witness.json` (exists, verify)

### Level 1: Electron e⁻ = trefoil T_{2,3} (symbolic)
- NF(e⁻) = σ₀σ₁σ₀ in H₃(q)
- Markov trace: tr_M(e⁻) = z³ (CORRECTED, not hz²+z)
- **Verify**: recompute tr_M symbolically, confirm z³
- **LP check**: electron channel is unconditional for T_{2,3}

### Level 2: Quarks (typed crossings, symbolic)
- Up quark (𝔲): positive crossing, eigenvalue +q
- Down quark (𝔡): negative crossing, eigenvalue -q⁻¹
- Mixed (𝔲𝔡): half-shift eigenvalue ½(q - q⁻¹)
- **Script**: `breit-wheeler-nucleon-nf.py` (exists, rerun)

### Level 3: Nucleons (Borromean + typed crossings, symbolic)
- Proton 𝔭 = B₃(𝔲,𝔲,𝔡): full 6-element NF
- Neutron 𝔫 = B₃(𝔲,𝔡,𝔡): full 6-element NF
- Δnet = net(𝔫) - net(𝔭) → energy scale E₀
- **LP duality**: verify B₃ minimizes categorical action
- **Script**: `breit-wheeler-nucleon-nf.py` (exists, rerun)
- **Witness**: `breit-wheeler-nucleon-nf.witness.json` (exists, verify)

### Level 4: Atoms (Gröbner NF, CRT for A > 10)
- H (Z=1, N=0): proton + electron Hopf link
- D (Z=1, N=1): proton + neutron + electron
- He-4 (Z=2, N=2): 2p + 2n + 2e
- He-6 (Z=2, N=4): 2p + 4n + 2e (for beta decay)
- Li-6 (Z=3, N=3): 3p + 3n + 3e (daughter of He-6)
- **For A ≤ 10**: symbolic Python (minutes)
- **For A > 10**: Rust CRT engine (hecke-crt binary)
- **Reuse**: existing certificates, pick up where left off

### Level 5: Beta-decay Q-values (branching factorization)
- n → p: (A=1, odd) Q = (SΔ+1)×m_e
- ³H → ³He: (A=3, odd) Q = |SΔ|×m_e
- ⁶He → ⁶Li: (A=6, even) Q = (Σ_FP+1)×m_e
- All symbolic in q, then evaluate at q₀
- **Script**: NEW (branching-qvalue-chain.py)

### Level 6: Comparison table
- All quantities in MeV with ±δ (propagated from q₀ uncertainty)
- Observed values with CODATA/NNDC uncertainties
- Same scale: both in MeV, both with error bars
- Columns: Quantity | Predicted | δ_pred | Observed | δ_obs | Δ/σ

## Scripts to run (in order)

| # | Script | Reuse witness? | Time est. | Output |
|---|--------|---------------|-----------|--------|
| 1 | `q_parameter.py` | N/A (constants) | <1s | print q₀ ± δ |
| 2 | `pair-production.py` | verify existing | <10s | pair-production.witness.json |
| 3 | `breit-wheeler-nucleon-nf.py` | verify existing | <30s | nucleon NF witness |
| 4 | NEW: `lp-duality-check.py` | — | <10s | LP verification |
| 5 | NEW: `branching-qvalue-chain.py` | loads nucleon NF | <60s | Q-values + comparison |
| 6 | `hecke-crt` (Rust) | reuse certificates | 1-5min | atom certificates |
| 7 | NEW: `comparison-table.py` | loads all witnesses | <10s | final table |

## CRT Multi-Prime Strategy
- 4 primes: 10⁹+7, 10⁹+9, 998244353, 985661441
- Product ≈ 10³⁶ (sufficient for A ≤ 40)
- For A > 30: extend to 8 primes
- Reuse existing certificates: check witness dir before computing
- Checkpoint: each (Z,N) pair writes its own certificate file

## Error Bound Propagation
- q₀ uncertainty: δq = 1.3e-8 (from m_μ/m_e CODATA)
- All derived quantities: δX = |dX/dq| × δq
- Numerical derivatives where symbolic too complex
- Report: absolute δ (MeV) and relative δ/X (%)
