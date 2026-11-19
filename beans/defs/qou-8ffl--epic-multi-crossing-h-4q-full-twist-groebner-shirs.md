---
# qou-8ffl
title: 'EPIC: Multi-Crossing H_4(q) Full-Twist + Groebner-Shirshov Nuclear Compute & Paper/Lean Derivations (^4He, ^12C, ^56Fe..^238U) & Retirement of alpha_cluster_recursion.py'
status: in-progress
type: epic
priority: high
created_at: 2026-11-19T09:36:33Z
updated_at: 2026-11-19T09:36:33Z
parent: qou-10v9
---

Owner directive (2026-11-19): **"work both"** — execute BOTH the multi-crossing `H_4(q_2t)` / Gröbner–Shirshov **Compute** AND the **Paper + Lean Derivations** across light, medium, and heavy nuclei (`^4He`, `^12C`, `^56Fe -> ^208Pb -> ^238U`), while retiring the non-Lean dead-exploratory script `computations/alpha/alpha_cluster_recursion.py` (`64 m_e G + Vol(7^2_1)`).

## Deduplication & Cross-Links Against Existing Beans

- **Parent Milestone / Epic:** `qou-10v9` (cross-linked with `qou-v2om` *close the low-isotope binding defect*, `qou-rtxm` *Lean / Mathlib foundations*, `qou-br4t` *4x4 Hankel/Cauchy SU(4) q-Plancherel*, `qou-xsmr` *General-K GPMT cumulants*, `qou-brng` *saturated binding fraction kernel*).
- **`qou-n0so` & `qou-yd54`:** `qou-n0so` established the 1-crossing 3D tetrahedral `alpha`-simplex complex `K_A` (`f_1 = 3A - 6`) and Pauli excess attachment regimes (`AlphaSimplexCoordinationDerivation.lean`), and `qou-yd54` tracks downstream Z=0..118 isotope atlas wiring. Single-crossing `K_4` edges (`b2_log_D = 2.051 MeV`, `b2_log_gg = 2.834 MeV`) give `13.92..18.62 MeV` on `^4He` vs `28.30 MeV` AME because an intra-`alpha` 4-strand full twist `Delta_4^2 = (sigma_1 sigma_2 sigma_3)^4` has length `12 = 2 * C(4,2)` (multi-crossing per pair) coupled to the Convention-D + GPMT modified trace.
- **`qou-usft`, `qou-mumr`, `qou-4waf`:** Already established and closed the EM/geometry boundary diagnosis: derived `alpha_EM` is wired; `A^(1/3)` and the `3/5` uniform-sphere factor have no continuum position-space `rho(r)` counterpart in QOU (`ell_P = hbar_q * t_P = 1` is dimensionless Reeb step count; Connes spectral distance on `(A, H, D_grad)` is the discrete step-count dual); and `delta(q)` cancels out of mirror differences in the `p-n`-only bond (`mirror_split_eq_L_diff`). Child `N2` respects those proved boundaries without re-litigating closed EM steps.

## Strict Anti-Fitting & Anti-Numerology Rules

1. **Zero fitting** to AME2020 binding energies or separation energies (`S_sep` from AME rejected per `qou-usft`).
2. **Zero knot-volume hunting**: never revive `alpha_cluster_recursion.py`'s `B(n alpha) = n * 64 m_e G + C(n,2) m_e Vol(7^2_1)`.
3. **80-dps pure-`mpmath` compute** (`0` float64 in probes and witnesses; evaluated at both `q_0` and `q_2t`).
4. **Genuine Lean 4 proofs** (`0 sorry`, `0 axiom`, `0` borrowed names, `0` collapsed definitions).

## Child Lanes (`N1..N6`)

| Child Bean | Lane | Status | Scope Summary |
|---|---|---|---|
| `qou-ki22` | **N1: `H_4(q)` Full-Twist + Inductive GS Light/Medium Compute & Lean** | `in-progress` | `QOU/Nuclear/H4FullTwistAlphaCellAndGroebnerBridge.lean` + `h4_fulltwist_alpha_and_carbon12_groebner_probe.py` & `.witness.json` (`^2H..^40Ca`, `^8Be` vs `2*^4He`, `^12C`, `H_12(q)` 80-dps comparison) |
| `qou-rhfk` | **N2: Heavy Nuclei `^56Fe -> ^208Pb -> ^238U` Saturation & Pauli Asymmetry** | `todo` | Multi-crossing simplicial saturation + 4-row `SU(4)` `(9/4)(N-Z)^2/A` content-sum penalty + discrete step-graph vs CAL-3 Coulomb audit (deduplicated with `qou-n0so`, `qou-usft`, `qou-mumr`, `qou-4waf`) |
| `qou-pg2f` | **N3: Retire `alpha_cluster_recursion.py` & Rewire Live Importers** | `todo` | Excise dead-exploratory `64 m_e G + Vol(7^2_1)` recursion & rewire `b_over_a_v5_unified.py` / isotope atlas / dashboards (coordinated with `qou-yd54`) |
| `qou-2lwj` | **N4: Paper + Monograph Derivation Blocks (`nuclear-interactions/`, `predicted-spectra/`)** | `todo` | Replace `magic A*8G` / `Vol(7^2_1)` prose with Lean-backed `H_4(q)` full-twist, GPMT & inductive transfer-matrix Gröbner–Shirshov derivations in Voice A |
| `qou-ozdk` | **N5: Higher-Order GPMT `(z - z_D)^m` & `H_12(q)` Cabled `(3^4)` Bridge** | `todo` | Formalize 2nd-order GPMT modified trace on `(3,3,3,3)` (`m = 2` zero at `z_D`) & bridge `H_12(q) supset H_3(q)^4` to `H_4(q)` (`0 sorry`, 80 dps) |
| `qou-wxey` | **N6: `1 <= A <= 238` Valley of Stability, Magic Closures & Drip-Line Sweep** | `todo` | 80-dps parameter-free isobar & transfer-matrix Groebner-Shirshov demand sweep across `Z=0..118` (coordinated with `qou-yd54`) |
