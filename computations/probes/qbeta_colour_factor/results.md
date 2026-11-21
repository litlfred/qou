# Results: a colour tensor factor on the ruled Q_β cell

Pre-registration: [`PREREGISTRATION.md`](PREREGISTRATION.md) (committed `e7a96d0061` before
any number here). Lean: `QOU/QBeta/ColourFactorDeligne.lean` (`1740e55f78`). Probe:
`qbeta_colour_factor_probe.py`, witness `qbeta-colour-factor.witness.json`, **8/8 checks**.
Proton pin, mpmath 60 dps; exact Fractions at q = 2, 3; the colour-singlet line by exact sympy
linear algebra at the pin taken as a rational.

## Mechanism

Each quark strand is C² ⊠ C³ in the Deligne product of Rep U_q(sl₂) and Rep U_q(sl₃). The braid
acts by ρ₂ ⊗ ρ₃, the quantum trace uses K₂ ⊗ K₃, and the ruled T³ projections act on the
isospin factor. The trace of a Kronecker product factorises, so
ε^col_p = ε_p · F, ε^col_n = ε_n · F with one F: the colour factor is **flavour-blind** and
multiplies ε_flavour by F. This is checked by brute force on the 216-dim space (E4), not assumed.

## Lean (sorry-free; axioms propext, Classical.choice, Quot.sound)

| theorem | statement |
|---|---|
| `hecke_S0`, `hecke_S1`, `braid_S`, `S1_mul_S1inv`, `S1inv_eq` | the 2-dim (2,1) rep of H₃(q) used below is a rep |
| `chi21_V3` | χ_(2,1)(V³) = 2 − h⁴[3] (with `chiTriv_V3`, `chiSign_V3`: the 1-dim blocks give 1) |
| `weyl_sum` | Σ_λ f_λ dim_q S_λ(C^N) = [N]³ on three strands, a = q^N symbolic |
| `colourFactorV3_eq` | full colour trace on V³ / [N]³ = 1 − h⁴[N−1][N+1]/[N]² |
| `qn_pm_one` | [N−1][N+1] = [N]² − 1, so the factor is 1 − h⁴ + h⁴/[N]² |
| `colourFactorV3_lt_one` | for real 1 < q < a (rank N ≥ 2) the factor is < 1 |
| `framing_drops` | the sl_N framing σ ↦ cσ leaves V = σ₀σ₁⁻¹ unchanged |
| `singletScalar_V_pow` | on the colour singlet every V^k acts by 1 |
| `trace_kronecker_mul` | Tr(A ⊗ B) = Tr A · Tr B (Mathlib), the flavour-blindness |

## Numbers at q₀ (gl₃ and sl₃ framing identical, E5)

F_required = 0.78233341 / 0.325433929 = 2.40397.

| word | C1 full colour / [3]³ | C2 singlet / [3]³ | C3 singlet / 1 |
|---|---|---|---|
| V³ (ruled) | 0.998295963607 | 0.035464334084 | 1 |
| V⁶ | 0.993193762013 | 0.035464334084 | 1 |
| V⁹ | 0.984723060373 | 0.035464334084 | 1 |

F / F_required lies in [0.01475, 0.41598] over all 18 cells. No cell has F > 1, so every member
leaves the cell unchanged (C3) or makes it smaller. C1 on V³ is 1 − h⁴ + h⁴/[3]² exactly
(E3: exact at q = 2, 3 for N = 2, 3, 4 from the matrices; at q₀ to 1e-50).

## Verdict

**Scope (b) for this family.** The invariant is `colourFactorV3_eq` with `qn_pm_one`:
the full colour trace on V³ is 1 − h⁴(1 − 1/[N]²) < 1 for every rank N ≥ 2 and every real
q > 1, and the singlet members are 1/[N]³ or 1 (the singlet carries K-weight 1 and V acts on it by
(−q⁻¹c)(−q⁻¹c)⁻¹ = 1). A colour factor of tensor-product type cannot supply F ≈ 2.404 on the
ruled cell; the gap must come from elsewhere.

Scope limits. Only Deligne-product colour (colour as a separate tensor factor) is covered. A
colour mechanism that mixes isospin and colour in one R-matrix (e.g. a gl₆ Jimbo R on C²⊗C³),
or one that changes the word rather than the trace, is outside this family and not excluded.
Nothing was selected; nothing was mapped to MeV.
