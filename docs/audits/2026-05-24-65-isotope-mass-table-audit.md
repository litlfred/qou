# 65-isotope mass table audit (2026-05-24)

**Branch:** `claude/geom-qbeta-n5-isotope-audit-2026-05-24`
**Witness:** `mass-table-comprehensive.witness.json` (2026-05-24T02:01:48)

> **Framing note (post-2026-05-23 absorption coord).** This audit pre-dates the framing correction "`λ_scale` is absorbed into `VolDensity`". Read the per-isotope +3% offsets below as the gap between the framework's current categorical `VolDensity` evaluation and the categorically-exact one — **not** as a free-parameter calibration gap. The factor that the legacy framing called `λ_scale` is what the canonical `VolDensity(K)` produces per knot/link; it is no longer treated as a separately-named constant.

## Summary

65 masses (63 stable isotopes H→Fe + p + n) computed in <1s using
Wenzl LR closed-form. All masses use:
- Current categorical `VolDensity(𝓑₃)` evaluation (Family A linking-weight, `5/2 + (3/4)h²`, PROVED via H_4 Wedderburn — the linking-weight is the **per-link** value the Geom functor produces, not a separate calibration)
- Substrate flavor-split `Δm/M_N` (PROVED)
- Rust Tier 1.A kernel (canonical-rust default)

## Mass predictions

| range | m_err (%) | count | notes |
|---|---:|---:|---|
| p, n (A=1) | +2.89 | 2 | per-nucleon VolDensity gap |
| D, T, ³He (A=2-3) | +2.99 to +3.18 | 3 | slight growth with A |
| ⁴He (A=4) | +3.65 | 1 | magic-A formula |
| A=6–12 | +3.46 to +3.73 | 6 | recursive-on-⁴He |
| A=13–58 | +3.72 to +3.86 | 53 | not-in-atlas (no braid words) |

The mass error grows monotonically from +2.89% (p) to +3.86% (⁵⁸Fe).
This growth reflects the per-nucleon `VolDensity` gap accumulating
across A nucleons. The pattern is smooth and structurally predictable.

## Binding energies

Only **10 of 65** isotopes have computed binding energies (D through ¹²C).
The remaining 55 have `B_pred = n/a` (gated on Phase-2 H_{3A} kernels
or absent from the knot atlas).

| isotope | B_pred (MeV) | B_AME (MeV) | B_err (%) |
|---|---:|---:|---:|
| D | 0.47 | 2.22 | -79 |
| T | 0.63 | 8.48 | -93 |
| ³He | 0.66 | 7.72 | -91 |
| ⁴He | 0.71 | 28.30 | -97 |
| ⁶Li–¹²C | 0.68–0.72 | 31.99–92.16 | -98 to -99 |

Binding energies are **catastrophically wrong** because:
1. The +3% mass gap propagates into the DIFFERENCE (B = ΣM_nucleon - M_atom)
2. B is ~1-100 MeV while the mass gap is ~30 MeV per nucleon
3. A 30 MeV per-nucleon error on a 2-30 MeV binding energy = -80% to -99%

This is structurally expected from the current `VolDensity(𝓑₃)`
evaluation. The binding-energy problem requires refining `VolDensity`
for the proton (and neutron) — not a per-isotope fix. There is no
separate "λ_scale" to calibrate; the per-knot Geom evaluation IS the
quantity that needs to land on its categorically-exact value.

## Methodology coverage

| tag | count | description |
|---|---:|---|
| `principled-derivation` | 2 | p, n — canonical braid words |
| `manual-historical-volume-match` | 3 | D, T, ³He — historical Vol match |
| `magic-A-formula` | 1 | ⁴He — algebraic shell closure |
| `deprecated-volume-match` | 2 | ⁶Li, ⁷Li — brute-force SnapPy |
| `recursive-on-4He` | 4 | ⁹Be–¹²C — α-particle recursion |
| `not-in-atlas` | 53 | ¹³C–⁵⁸Fe — no assigned knot/braid |

## Key observations

1. The mass table infrastructure works at scale (65 isotopes <1s).
2. All mass predictions are bounded by the current `VolDensity(𝓑₃)` per-nucleon ~+3% gap.
3. Binding energies are structurally unusable until `VolDensity` refines.
4. 53/65 isotopes have no assigned braid word ("not-in-atlas") —
   their masses are computed from pure A-counting (Z protons + N
   neutrons × per-nucleon mass), NOT from individual knot topology.
5. The growth of mass error from +2.89% to +3.86% with A suggests
   a small per-nucleon accumulation — possibly from the tower-factor
   computation at higher H_{3A} Hecke levels.
