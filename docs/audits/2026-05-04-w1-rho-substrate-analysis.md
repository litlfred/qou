# W-1 ρ_F Substrate Analysis — 2026-05-04

**Status:** partial progress — ³He error reduced 2.97% → 0.12% (C3); ³H regresses 0.16% → 2.0%.  GAP-A remains open.

---

## 1  Background

The Kashaev binding law states

$$
B(Z,N) = \rho_F \cdot m_e \cdot V_{\mathrm{hyp}}(K)
$$

The paper derives ρ_F as an **integer** from the alt-block Wedderburn
occupation rule (`rem:frobenius-packing-density`):

| condition on K | ρ_F |
|---|---|
| alt ∉ Λ(K)  (single-chirality, e.g. D) | m_e |
| alt ∈ Λ(K)  (CPT-saturated, e.g. T, ³He) | 2 m_e |

This yields ρ_F = ⌈A/2⌉ · m_e for the census atoms.  The empirical
true ρ (B_AME / (m_e · V_hyp)) deviates from the integer at the percent
level:

| atom | ρ_int | true_ρ | δρ | δρ/ρ_int |
|---|---|---|---|---|
| ²H  | 1 | 0.9892 | −0.011 | −1.1% |
| ³H  | 2 | 2.0031 | +0.003 | +0.15% |
| ³He | 2 | 2.0612 | +0.062 | **+3.1%** |

³He is the dominant outlier.  W-1 asks: can the 3.1% correction be
derived categorically, without fitting to AME data?

---

## 2  Categorical Candidates Tested

All four candidates are **zero-AME-input**.  They depend only on q₀ and
the per-atom Markov-trace values from
`markov-peel-atomic-tr-m.witness.json` (which are derived from the
Hoefsmit Hecke-algebra computation, not from nuclear data).

| label | formula | insight |
|---|---|---|
| **C0** | ρ = ⌈A/2⌉ | integer paper rule |
| **C1** | ρ = [⌈A/2⌉]_q | q-deform the ceiling; uses q₀ only |
| **C2** | ρ = ⌈A/2⌉ · (Z·tr_M_p + N·tr_M_n) / (A·tr_M_avg) | nucleon-composition weighting |
| **C3** | ρ = [⌈A/2⌉]_q · (Z·tr_M_p + N·tr_M_n) / (A·tr_M_avg) | C1 × C2 correction |

Parameters at q₀ = 1.1099785955541805:

- [2]_q = q₀ + q₀⁻¹ = **2.01090**
- tr_M(proton) = **1.06531**
- tr_M(neutron) = **0.92323**
- tr_M_avg = **(tr_M_p + tr_M_n)/2 = 0.99427**

The C2/C3 correction factor for each atom:

| atom | (Z·tr_M_p + N·tr_M_n) / (A·tr_M_avg) |
|---|---|
| ²H  | (1·1.0653 + 1·0.9232) / (2·0.9943) = 1.0000 |
| ³H  | (1·1.0653 + 2·0.9232) / (3·0.9943) = **0.9763** |
| ³He | (2·1.0653 + 1·0.9232) / (3·0.9943) = **1.0238** |

The correction distinguishes ³He from ³H (which have the same A) because
³He has more protons (higher tr_M_p) while ³H has more neutrons.

---

## 3  Results

From `rho-f-categorical-probe.witness.json`:

| atom | true_ρ | C0 err | C1 err | C2 err | **C3 err** |
|---|---|---|---|---|---|
| ²H  | 0.9892 | +1.09% | +1.09% | +1.09% | +1.09% |
| ³H  | 2.0031 | −0.16% | +0.39% | −2.53% | **−2.00%** |
| ³He | 2.0612 | −2.97% | −2.44% | −0.66% | **−0.12%** |
| mean \|err\| | — | 1.40% | 1.31% | 1.43% | **1.07%** |
| max \|err\|  | — | 2.97% | 2.44% | 2.53% | **2.00%** |

**C3 reduces ³He error from −2.97% to −0.12%** — better than the 0.5%
target — at zero AME input.

---

## 4  Tension: ³He vs ³H

The C3 formula cannot simultaneously fix both ³He and ³H:

- **C3** corrects ³He to −0.12% but moves ³H from −0.16% to −2.00%.
- The two atoms have opposite tr_M corrections (³He: +2.38%, ³H: −2.37%).
- A formula that fixes ³He *by proton-excess weighting* necessarily
  penalizes ³H's neutron-excess, and vice versa.

This tension signals that the residual δρ has **two independent
categorical contributions**:

| atom | primary correction | source |
|---|---|---|
| ³He | +3.1% (large, proton-excess) | C3 captures 99% of this |
| ³H  | +0.15% (small, neutron-excess) | needs a separate term |
| ²H  | −1.1% (intermediate, balanced) | neither C1/C2 nor C3 helps |

---

## 5  What Is Still Needed (GAP-A)

To bring ALL three census atoms to ≤0.5% with a single categorical formula:

1. **Explain the ²H −1.1% offset.** C0–C3 all give ²H at +1.09%.
   This is symmetric (Z=N=1) so it cannot come from proton/neutron
   asymmetry.  It likely requires a knot-topology correction (6_2
   vs Borromean geometry).

2. **Decouple ³He from ³H.** The C3 correction overshoots ³H by −2%.
   A categorical fix would need a SIGN-asymmetric formula that adds to
   ³He without subtracting from ³H (or vice versa).  Candidates:
   - Isospin I_z = (Z−N)/2 weighted correction: but I_z(³He) = +½ and
     I_z(³H) = −½ — symmetric, won't work without sign flip.
   - A **topological** distinction: 8_11 (knot, 1 component) vs
     L6a4 (link, 3 components).  The Borromean multi-component
     structure of ³He could carry an additional categorical correction
     absent for the 1-component knot 8_11 (³H).
   - **Milnor triple linking number** μ̄(³He) = 1 (Borromean),
     μ̄(³H) = 0 (knot).  A correction proportional to μ̄ would add
     only to ³He, not ³H.

3. **Probe Milnor-μ̄ correction.** The next probe should test:

   $$
   \rho_F^{(C4)}(Z,N) = \rho_F^{(C3)}(Z,N)
     + \mu\bar{}(K) \cdot \delta\rho_{\mu}(q)
   $$

   where δρ_μ(q) is a categorical q-function and μ̄(K) is the Milnor
   triple linking number of the atomic link K.  For ³He (Borromean):
   μ̄ = 1.  For ³H (8_11 knot): μ̄ = 0.  This isolates the ³He
   correction.

---

## 6  Impact on mass-table-ppb

| atom | current err (C0) | with C3 | with C4 (target) |
|---|---|---|---|
| ²H  | +1.09% | +1.09% | ≤0.5% (open) |
| ³H  | −0.16% | −2.00% | ≤0.5% (open) |
| ³He | −2.97% | **−0.12%** ✓ | ≤0.12% |
| ⁴He | +5.87% | (magic-A) | (separate) |

`mass_table_ppb.py` should be updated to use C3 for ³He once the ³H
regression is resolved.  **Not wired yet**: pending C4 Milnor-μ̄ probe.

---

## 7  Next Steps

- [ ] **W-1a** — Milnor-μ̄ correction probe: does δρ_μ(q₀) ≈ 0.062 − (C3 residual)?
- [ ] **W-1b** — If μ̄ probe succeeds, wire C4 into `mass_table_ppb.py`.
- [ ] **W-1c** — Understand ²H −1.09% offset (symmetric case; knot-topology correction?).
- [ ] **W-2** — Canonical knot assignment for A=5,6 atoms (Li family).

---

## 8  Witness File

`computations/probes/rho-f-categorical-probe.witness.json`

Computed at q₀ = 1.1099785955541805 using tr_M from
`markov-peel-atomic-tr-m.witness.json` (50 dps, Hoefsmit bridge
verified).  Zero AME input.
