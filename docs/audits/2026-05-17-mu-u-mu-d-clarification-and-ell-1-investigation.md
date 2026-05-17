# μ_u, μ_d clarification + ℓ=1 (B_3 binding) substrate investigation

**Branch**: `claude/isotope-mass-witness-data-x5lCh`
**Owner ask**: *"so we need Pair skein mass for up and down quarks?
this might not be in level 0 of the tower since the only exist in
the B_3 binding stably? if so maybe check there... clarify μ_d, μ_u
meaning / definitions"*

## TL;DR

The owner's diagnosis is **correct**.  The framework's μ_u and μ_d
are **ℓ=1 (nucleon-level) dressed quark masses** ≈ 311 MeV — not
ℓ=0 (free-quark, bare) masses ≈ 2.2 MeV.  The framework is right
to use ℓ=1 values because **free quarks do not exist stably**
(QCD confinement); they only have well-defined masses INSIDE the
B_3 Borromean binding.

The framework HARDCODES μ_u ≈ 311.10 MeV and μ_d ≈ 312.39 MeV;
it does NOT derive them from substrate.  The structural relation
to the nucleon mass (m_N/3 ≈ μ_q) is recognized but the
SUBSTRATE derivation of either:
1. The absolute mean `(μ_u + μ_d)/2 ≈ 311.745 MeV`, or
2. The difference `μ_d − μ_u ≈ 1.29 MeV`

is the open piece.

## 1. Clarification: μ_u, μ_d are ℓ=1, not ℓ=0

### The confinement-level hierarchy

Per [`confined-particle.md`](../../content/quantum-observable-universe/braids-and-knots/confined-particle.md) lines 52, 67-70:

| Particle | confinement level ℓ | strand count n_0 | Markov-trace class |
|---|---:|---:|---|
| quark | **0** | 1 | [σ_0] in H_1(q) |
| neutrino | 0 | 1 | trefoil-like |
| photon | 0 | 4 | … |
| **proton** | **1** | 3 | [B_3(uud)] in H_3(q) |
| **neutron** | **1** | 3 | [B_3(udd)] in H_3(q) |
| electron | 1 | 2 | trefoil σ_1³ |
| ⁴He | 2 | 4 nucleons | binding link |

The quark is **only conceptually defined at ℓ=0** — but per QCD
confinement (well-established physics), **free quarks do not exist
stably**.  The asymptotic-freedom + confinement structure of SU(3)
gauge theory forces quarks to appear only inside bound colour-singlet
states: at ℓ=1 (mesons, baryons), never at ℓ=0.

### Bare (ℓ=0) vs dressed (ℓ=1) quark masses

In standard particle physics:

| quantity | up-quark | down-quark | source |
|---|---:|---:|---|
| Bare / current mass (ℓ=0) | ~2.2 MeV | ~4.7 MeV | PDG, lattice QCD at MS-bar μ=2 GeV |
| **Dressed / constituent (ℓ=1)** | **~310 MeV** | **~310 MeV** | constituent quark model; ≈ m_N/3 |
| Framework's μ_u, μ_d | **311.10 MeV** | **312.39 MeV** | hard-coded in HadronicMass.lean line 327-335 |

The framework's values match the **constituent quark mass**
convention, NOT bare quark mass.  Per Lean docstring (line 327-329):

> *"Dressed quark Skein mass of the up quark (MeV).  Derived from
>  the Borromean Skein decomposition: μ_u ≈ 311.10 MeV at q = 1.1097."*

So **the framework correctly identifies μ_u, μ_d as ℓ=1 dressed
quantities** — the owner's diagnosis is correct.

### The "derived from Borromean Skein decomposition" claim

The Lean source SAYS μ_u, μ_d are "derived from the Borromean Skein
decomposition" but the actual code is:

```lean
noncomputable def dressed_mass_up : ℝ := 311.10
noncomputable def dressed_mass_down : ℝ := 312.39
```

These are **hard-coded literals**.  No actual derivation chain is
present in the source.  The pair-Skein formula
`𝒮_{ab}(q) = (q·μ_a + q⁻¹·μ_b) / (q^{1/2}+q^{-1/2})` is an
ALGEBRAIC IDENTITY that distributes the nucleon mass into three
crossing-pair contributions — it does NOT derive μ_a, μ_b from
substrate.

## 2. The numerical near-coincidence: μ_q ≈ m_N / 3

| quantity | value (MeV) |
|---|---:|
| μ_u | 311.10 |
| m_p / 3 | 312.76 |
| μ_d | 312.39 |
| m_n / 3 | 313.19 |
| (μ_u + μ_d) / 2 | 311.745 |
| (m_p + m_n) / 6 | 312.97 |

The framework's dressed quark masses are within **0.5 %** of `m_N / 3`.
This is the standard **constituent quark mass** identification from
phenomenological QCD: at low energies, an "effective" quark inside
a nucleon carries ≈ 1/3 of the nucleon's mass.

Per the framework's pair-Skein decomposition:

```
m_p = 𝒮_uu + 2·𝒮_ud
    = (q+q⁻¹)/(q^{1/2}+q^{−1/2}) · [μ_u·(1) + μ_u·(q/q-q^{-1}/q + …)]
    ≈ prefactor · 3 · μ_avg     (when μ_u ≈ μ_d)
    ≈ 1.004 · 3 · 311.745
    = 938.97 MeV  (vs CODATA 938.272, 0.07% over)
```

So **m_p ≈ 3 · μ_avg · prefactor** is the structural identity,
modulo the small chirality correction from μ_d ≠ μ_u.

## 3. ℓ=1 substrate-candidate investigation

If μ_u, μ_d at ℓ=1 are to be substrate-derived, the natural
categorical formulation is:

> **μ_q(ℓ=1) = (B_3-binding energy contribution per quark) at substrate q_0**

Substrate quantities available at the B_3 level (3-strand
Borromean braid):

| substrate quantity | value at q_0 |
|---|---:|
| q_0 | 1.110 |
| ℏ_q = (q-1)/q | 0.0991 |
| z_0 = √q − 1/√q | 0.1044 |
| z = 1/(√q+1/√q) | 0.4993 |
| Vol(𝔅_3) = 8G | 7.328 |
| Vol(𝔅_3)/ℏ_q² | 746.27 |
| Hoefsmit d_1 = q³/(q²+1) | 0.6127 |
| Hoefsmit d_2 = −q⁻¹/(q²+1) | −0.4036 |
| Hoefsmit b = √(d_1·d_2 + 1) | 0.8676 |
| `[2]_q · z` (PL prefactor) | 1.004 |
| `[3]_q` | 3.044 |

Target: μ_u_cat = 311.10 / 0.511 = 608.81 (m_e units).

**Candidate formulas** for the dressed mass scale at ℓ=1:

| candidate | value (m_e units) | value (MeV) | residual % |
|---|---:|---:|---:|
| Vol(𝔅_3)/(3·ℏ_q²) · 1.0 | 248.76 | 127.12 | −59.1 |
| Vol(𝔅_3)/(3·ℏ_q²) · A(q₀) where A=2.46 | 611.95 | 312.71 | +0.51 |
| m_p_pred / 3 (PL-derived) | 612.27 | 312.87 | +0.56 |
| Vol(𝔅_3)/(3·ℏ_q²) · prefactor² | 250.74 | 128.13 | −58.8 |

**Best**: μ_q ≈ Vol(𝔅_3)/(3·ℏ_q²) · A(q₀) · m_e where A(q₀) is the
Picard-Lefschetz amplification factor.  This reduces μ_q substrate
derivation to **the same open problem as m_p substrate derivation**
— namely, deriving A(q₀) (currently "substrate + best-fit
integration limit").

## 4. Status

| substrate piece | status |
|---|---|
| μ_u, μ_d at ℓ=1 (dressed masses) | identified correctly as ℓ=1 by framework |
| Numerical value (μ_u, μ_d ≈ 311 MeV) | hard-coded; not derived |
| Mean μ_avg ≈ m_N/3 | structural identity, but ties to m_N |
| Difference μ_d − μ_u ≈ 1.29 MeV | best candidate (|d_1|·4) off by 2.77% |
| Substrate derivation of μ_avg | reduces to PL m_p derivation (open) |
| Substrate derivation of (μ_d − μ_u) | open; needs Hoefsmit chirality combination beyond simple entries |

## 5. Implication for ρ_K open problem

Per the C10 finding: ρ_K · m_e · |tr_M(K)| = M(K)_atomic.  For the
proton:

```
ρ_K(p) · m_e · |tr_M(p)| = m_p
                          = 𝒮_uu + 2·𝒮_ud
                          = [(q+q⁻¹)/(q^{1/2}+q^{−1/2})] · (3·μ_avg + small ε)
                          ≈ prefactor · 3 · μ_avg
```

So:

```
ρ_K(p) ≈ prefactor · 3 · μ_avg / (m_e · |tr_M(p)|)
       = 1.004 · 3 · 608.81 / 1.0653
       = 1721.8
       (vs ρ_K_CODATA = 1723.6, +0.10 %)
```

**This identifies ρ_K structurally as the dressed-quark scale
amplification factor** — and reduces ρ_K substrate derivation
to the same open question: derive μ_avg (≈ 311 MeV / m_e)
from substrate.

## 6. Recommendations

1. **Affirm the ℓ=1 identification**: the framework correctly uses
   ℓ=1 dressed quark masses (free quarks don't exist).  This is
   physical and right.

2. **Document the open derivation chain**:
   - PL m_p derivation (open: integration limit)
   - μ_u, μ_d substrate derivation (open: depends on PL m_p or
     equivalent dressed-mass-scale derivation at ℓ=1)
   - ρ_K substrate derivation (open: reduces to μ_avg)

3. **Update m_n_difference_formula.py and HadronicMass.lean**
   docstrings to clarify the calibration:
   - μ_u = 311.10 MeV is CALIBRATED (constituent quark-model
     identification ≈ m_p/3), NOT substrate-derived
   - μ_d = 312.39 MeV similarly CALIBRATED
   - The 1.29 MeV difference is CALIBRATED to CODATA Δm

4. **Research item**: derive μ_avg ≈ m_N/3 from substrate AT ℓ=1
   without using m_N as input.  Candidate forms involve
   Vol(𝔅_3), ℏ_q, and an "amplification factor" structurally
   identical to A(q₀) from the PL chain.

This audit clarifies that the framework's substrate derivation of
m_p, m_n, ρ_K, and all atomic masses **reduces to a single open
piece**: the substrate-only derivation of the ℓ=1 dressed-quark
mass scale μ_avg ≈ m_N/3 ≈ 311 MeV at q_0.
