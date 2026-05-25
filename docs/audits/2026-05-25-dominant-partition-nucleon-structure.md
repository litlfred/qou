# Dominant Wedderburn partition ↔ nucleon decomposition correspondence

**Date:** 2026-05-25
**Trigger:** Post-PR #1284/#1286 (α* dominant-partition analysis)
**Status:** EXPLORATORY finding — pattern observed across 4 atoms, mechanism conjectural

## Empirical observation

Per [`alpha_star_dominant_partitions.py`](../../folio-assistant/computations/alpha_star_dominant_partitions.py) (PR #1284), the Wedderburn partition forcing the smallest α* in each canonical atom-braid's PSD bisection has a structural correspondence with the atom's nucleon decomposition.

| Atom | A | dominant λ* | transpose λ*^T | rows(λ*^T) | cols(λ*^T) | Pattern |
|---|---:|---|---|---:|---:|---|
| D ²H | 2 | (3, 1, 1, 1) | (4, 1, 1) | 3 | 3 | irregular |
| T ³H | 3 | (3, 2, 2, 2) | (4, 4, 1) | 3 | 3 | irregular |
| ³He | 3 | (3, 2, 2, 2) | (4, 4, 1) | 3 | 3 | irregular |
| **⁴He** | **4** | **(4, 4, 4)** | **(3, 3, 3, 3)** | **4** | **3** | **A rows × 3 cells = 4 nucleons × 3 strands** ✓ |

## Key finding — ⁴He realises the Schur-Weyl nucleon decomposition

⁴He is the **first atom** where the dominant Wedderburn partition's transpose corresponds **exactly** to the natural nucleon decomposition: 4 rows (one per nucleon) of 3 cells (one per strand).

For the 3-strand-per-nucleon convention `atom_braid_word_3A(Z, N)` on `B_{3A}`:
- ⁴He has `n_0 = 12 = 3·4` strands → transpose `(3, 3, 3, 3)` = **4 nucleon-rows × 3 strand-cells**
- The dominant partition `(4, 4, 4)` = **3 strand-rows × 4 nucleon-cells** (Schur-Weyl dual)

## Strand-per-nucleon imprint on the max column

All 4 dominant partitions have `max(λ*) = 3` (D, T, ³He) or `max(λ*) = 4` (⁴He). The column count of the transpose:
- D / T / ³He: 3 columns = **3 strands per nucleon** (canonical recipe constant)
- ⁴He: 4 columns = **n_0 / 3 = A** (number of nucleons)

This suggests the dominant-partition transpose carries the **strand-bundle structure** as one of its dimensions.

## Conjecture (under-determined; needs more data)

For the canonical atom-braid `T_w(Z, N)`, the dominant Wedderburn partition forcing α* satisfies (one of):

(a) **Schur-Weyl form:** `λ*^T` is the A × 3 rectangle when n_0 = 3A and A ≥ 4. (Verified for ⁴He.)

(b) **Almost-rectangular form:** For A < 4 (small atom), `λ*^T` is a near-rectangle with at most one "defect" row. (Verified for T/³He as (4,4,1) — two full rows + one corner.)

(c) **Bar-involution constraint:** `λ*` and `λ*^T` are BOTH near-dominant (both in top-5 most-negative min_eig). The σ_avg bar-symmetric content populates transpose-paired irreps (Lean-proved in [`conj-atom-braid-exterior-algebra.lean`](../../content/quantum-observable-universe/braids-and-knots/conj-atom-braid-exterior-algebra.lean) PR #1286).

## Implications

If the rectangular form holds for larger atoms (A ≥ 5):
- `λ*^T` for ⁶Li (A=6, n_0=18) should be the (3, 3, 3, 3, 3, 3) hexagonal rectangle
- For ¹²C (A=12, n_0=36): (3, 3, ..., 3) with 12 rows
- These are **specific** large-dim irreps that the R5-full SDP would need to evaluate

Testing requires extending the Rust solver to higher-A atoms via the `atom_braid_word_3A` recipe + running the dominant-partition extraction probe.

## Gap-narrowing probe (3) — α* vs binding-energy gap correlation

Per [`alpha_star_vs_binding_gap.py`](../../folio-assistant/computations/alpha_star_vs_binding_gap.py), tested whether the PSD obstruction depth `(1 − α*)` per atom tracks the absolute fractional binding-energy gap `|B_pred − B_AME| / B_AME`:

| sym | α* | 1−α* | B_AME | B_pred | \|err\|/B | err_MeV |
|---|---:|---:|---:|---:|---:|---:|
| ²H | 0.193 | 0.807 | 2.225 | 2.249 | 1.09% | +0.024 |
| ³H | 0.096 | 0.904 | 8.482 | 8.469 | 0.156% | −0.013 |
| ³He | 0.091 | 0.909 | 7.718 | 7.489 | 2.97% | −0.229 |
| ⁴He | 0.048 | 0.952 | 28.296 | 29.956 | 5.87% | +1.660 |

**Spearman correlations (n=4):**
- ρ(1−α*, \|err\|/B) = **+0.80** — strong monotone, one inversion (T)
- ρ(1−α*, signed err/B) = +0.20 — signs flip across atoms; collapses
- ρ(1−α*, \|err\| MeV) = +0.80 — same as fractional

**⁴He magnitude check:** `(1 − α*)·B_AME = 26.94 MeV`, observed `|err| = 1.66 MeV` → ratio **0.062**. The obstruction depth **overpredicts** the gap by ~16×.

**Interpretation:** The dominant-partition obstruction correlates with **gap magnitude** (ρ=0.8) but the bulk of (1−α*) is cancelled across other Wedderburn blocks; only ~6% leaks into the residual gap. The cancellation includes a sign flip — the *direction* of the gap is set by which non-dominant blocks contribute. So the dominant block is the **obstruction structure** but NOT the **gap carrier** in isolation. This narrows the Gap-narrowing problem to: which secondary blocks cancel `(1 − α*)` down to the observed residual?

## Gap-narrowing probe (1) — project ⁴He mass on PSD-dominant pair

Per [`probe_1_project_4he_on_dominant.py`](../../folio-assistant/computations/probe_1_project_4he_on_dominant.py), computed `y_λ · χ^λ(T_w_⁴He)` for the PSD-dominant pair vs the trace-dominant blocks. **PSD-dominance ≠ trace-dominance** — they are orthogonal structural axes.

**Top-10 trace contributors (by |y_λ · χ^λ|) — all low-row "long-string" partitions:**

| rank | λ | d_λ | y_λ | χ^λ | y·χ | % of \|tr_M_partial\| |
|---:|---|---:|---:|---:|---:|---:|
| 1 | [9, 3] | 154 | 5.87×10⁻⁴ | 27.17 | 0.0159 | **32.0%** |
| 2 | [8, 4] | 275 | 4.31×10⁻⁴ | 30.03 | 0.0129 | **26.0%** |
| 3 | [10, 2] | 54 | 7.12×10⁻⁴ | 10.39 | 0.0074 | **14.9%** |
| 4 | [7, 5] | 297 | 2.62×10⁻⁴ | 21.59 | 0.0057 | **11.4%** |
| 5 | [11, 1] | 11 | 7.67×10⁻⁴ | 7.36 | 0.0056 | **11.3%** |

**PSD-dominant pair (the Schur-Weyl rectangle):**

| λ | d_λ | y_λ | χ^λ | y·χ | % \|tr_M\| | rank | min_eig |
|---|---:|---:|---:|---:|---:|---:|---:|
| **(4, 4, 4)** | 462 | 1.26×10⁻⁶ | −12.08 | −1.52×10⁻⁵ | **0.030%** | 12/26 | **−19.84** |
| **(3, 3, 3, 3)** | 462 | −4.65×10⁻⁹ | 23.44 | −1.09×10⁻⁷ | **0.0002%** | 18/26 | **−15.51** |

**Pair contribution to ⁴He mass:** `m_e · A · 8G · (y·χ)_pair = −2.3×10⁻⁴ MeV` — five orders of magnitude smaller than the 1.66 MeV gap.

**Structural finding (orthogonal axes):**
- **Trace-dominance** ⟹ **low-row "long-string" partitions** ([9,3], [8,4], [10,2], [11,1], [7,5]): large `y_λ` (10⁻⁴), moderate `χ`, big positive contributions
- **PSD-dominance** ⟹ **balanced rectangular partitions** ((4,4,4), (3,3,3,3)): tiny `y_λ` (10⁻⁶ to 10⁻⁹), but the rep matrix is most non-PSD
- `y_λ` varies by **5 orders of magnitude** across partitions; the rectangular Schur-Weyl block has the **smallest y_λ** in the witness

**Implication for Gap-narrowing:** The mass deficit lives in the **trace-dominant** partitions (mostly 2-row [9,3] / [8,4]), NOT in the PSD-dominant blocks. The Schur-Weyl rectangle (4,4,4) is a structural fingerprint of the nucleon decomposition but is **negligible** in the Markov-trace mass formula. Probes (2) and (4) should therefore be re-scoped: the crystal-weight Δ_(4,4,4) is unlikely to close the Gap directly, but the *mechanism* by which a low-y/high-PSD-obstruction block exists alongside a high-y/low-PSD-obstruction set may itself be the Δ_λ-gating structure to model.

## Next-probe predictions (updated after probes (3) + (1))

- ~~Probe (1) — project mass on (4,4,4) alone~~ **DONE.** Contributes 0.030% of |tr_M|. PSD-dominance ≠ trace-dominance. Gap lives in trace-dominant low-row partitions.
- **Probe (2) — crystal weight Δ_(4,4,4):** *Re-scoped.* The crystal weight of (4,4,4) won't close the Gap directly (per Probe (1)), but the Type B fold *pairing* between (4,4,4) and (3,3,3,3) — both at d_λ=462, both with comparable min_eig magnitudes (−19.8 vs −15.5), but with `y_λ` differing by 270× and opposite signs — is itself a structural feature worth deriving categorically. The crystal projection could explain why low-y "obstruction-bearing" blocks exist alongside high-y "mass-bearing" blocks.
- **Probe (4) — ⁶Li dominant partition:** under the rectangular-form conjecture, λ*^T(⁶Li) = (3,3,3,3,3,3); this would predict α*(⁶Li) by the same algebra. Falsifies the conjecture if the actual dominant partition is non-rectangular. Still worth running to confirm/falsify the rectangular conjecture, but Gap-narrowing connection is now weaker.

## Cross-references

- [`alpha_star_dominant_partitions.py`](../../folio-assistant/computations/alpha_star_dominant_partitions.py) — empirical witness (PR #1284)
- [`conj-atom-braid-exterior-algebra.lean`](../../content/quantum-observable-universe/braids-and-knots/conj-atom-braid-exterior-algebra.lean) — Lean transpose-pair theorems (PR #1286)
- [`joint-tower-sdp-rust.witness.json`](../../folio-assistant/computations/joint-tower-sdp-rust.witness.json) — per-partition eigenvalue data (PR #1283)
- [`mass_at_3A_proper.py`](../../folio-assistant/computations/mass_at_3A_proper.py) — canonical atom-braid recipe
- [`alpha_star_vs_binding_gap.py`](../../folio-assistant/computations/alpha_star_vs_binding_gap.py) — Probe (3): obstruction-vs-gap correlation (ρ=+0.80)
- [`alpha-star-vs-binding-gap.witness.json`](../../folio-assistant/computations/alpha-star-vs-binding-gap.witness.json) — per-atom data + Spearman
- [`probe_1_project_4he_on_dominant.py`](../../folio-assistant/computations/probe_1_project_4he_on_dominant.py) — Probe (1): y·χ projection on (4,4,4)/(3,3,3,3)
- [`probe-1-project-4he-on-dominant.witness.json`](../../folio-assistant/computations/probe-1-project-4he-on-dominant.witness.json) — per-block contributions to tr_M_⁴He

## What this audit does NOT do

- Does NOT propose a categorical derivation of the rectangular-transpose conjecture
- Does NOT extend the Rust solver to ⁶Li / ¹²C / heavier atoms (requires `atom_braid_word_3A` Rust registry extension + significant compute)
- Does NOT claim the pattern is exact — only 4 data points, and D's transpose (4,1,1) is irregular

## Next steps (deferred)

1. Extend the Rust registry to ⁶Li / ⁷Li canonical-3A atoms + run α* extraction
2. If transpose (3,3,3,3,3,3) holds for ⁶Li: write a Lean theorem `helium4_extends_to_lithium_rectangle`
3. Categorical proof via Schur-Weyl GL_3 ⊗ S_{3A} action on V_3^{⊗3A}
