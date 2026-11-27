# Uniform bond limit (3∞) past A = 3: saturation and α decay

**Date** 2026-11-27 · **Owner card** "Component change of the closure" · **Bean** `qou-brng` (epic `qou-myts`)
**Builds on** [`2026-11-27-bond-rules-and-length-cutoff.md`](2026-11-27-bond-rules-and-length-cutoff.md) rule (3∞)
**Probe** [`uniform_bond_limit_saturation_probe.py`](../../computations/probes/uniform_bond_limit_saturation/uniform_bond_limit_saturation_probe.py), 5/5 checks, mpmath 50 dps.
**Scope** (a). This is one candidate bond rule, measured and not adopted. Bond selection stays the owner's open decision. AME appears only in comparison columns.

## 1. Result

Rule (3∞) is the uniform average over bond words of length L as L → ∞. It has the closed form r = y_(n)/tr(x), with y_(n) = [n+1]_q/[2]_q^n and n = 3A. The free-word trace factorises over nucleons (check K1: the per-nucleon log trace read from the A = 2 and A = 3 witnesses agrees to 1e-15). So B(A) = E₀(A·ln t₁ − ln y_(3A)) holds for every A, and it reproduces the source audit at A = 2 and A = 3 (K2).

| A | B (MeV) | B/A (MeV) | B / B_AME |
|---|---|---|---|
| 2 | 9.119 | 4.560 | 4.10 (²H) |
| 3 | 16.093 | 5.364 | 1.90 (³H) |
| 4 | 23.354 | 5.838 | 0.825 (⁴He) |
| 56 | 414.64 | 7.404 | |
| 208 | 1559.25 | 7.496 | |

**It saturates.** B/A increases monotonically (K4) towards 3E₀ ln(1+q⁻²) + E₀ ln t₁ = **7.5303 MeV** (K3). This is a finite plateau, which the complete-graph law cannot give (`QOU.Mass.CoordinationSaturation`).

**The light end is wrong.** The rule over-binds ²H by 4.1× and ³H by 1.9×.

**α decay.** Scoring the sign of Q_α against AME, using the CAL-3-conditional EM term: 1208 of 2373 nuclides are on the right side. The rule gets 1117 of the 1118 α-unstable nuclides right but only 91 of the 1255 stable ones, so it calls almost everything unstable.

## 2. What this does not establish

- The rule ignores the bond words entirely. It compares the free word with the fully symmetrised state. The source audit's objection stands, so the plateau is a property of y_(n), not of nuclear bonds.
- The plateau value is not a derived binding coefficient. Do not compare it with the SEMF volume term as evidence.
- Correction: a chat report earlier on 2026-11-27 gave the asymptote as 7.5364 MeV. That figure left out the E₀ ln t₁ term; 7.5303 MeV is correct.
