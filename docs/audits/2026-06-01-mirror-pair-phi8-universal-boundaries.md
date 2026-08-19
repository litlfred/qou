# Mirror-pair Φ_8 boundary structure: M_first_Φ_8 = 7 AND M_first_Φ_8² = 15 are UNIVERSAL

**Date:** 2026-06-01
**Branch:** `claude/qbeta-c3-eigenphase-scaling-map-2026-06-01` (PR #1649)
**Status:** **CONFIRMED** — PR #1625's atomic-step universal M = 7 boundary extends to mirror pairs, and M_first_Φ_8² = 15 is a new universal boundary.

> **🛑 SUPERSEDED 2026-08-18 — this doc's numbers are computed on the wrong
> object; scoped, not corrected (bean `qou-0ndb`).** The mirror-pair element
> here is `Σ_m Δa_m(X − Y)·(u;u)_m`, formed by subtracting two witnesses'
> Habiro coefficients. Each witness's `a_m` expand *its own
> denominator-cleared numerator* `p = d·t`, so that sum is `d_X·t_X − d_Y·t_Y`,
> not the pair difference — and the denominators are built out of Φ₄ and Φ₈,
> the very factors being measured, to **different powers on each member of a
> pair** (⁶He: Φ₈⁴ vs ⁶Be: Φ₈⁸; ¹⁴O: Φ₈¹⁶ vs ¹⁴C: Φ₈¹²; proton: Φ₈² vs
> neutron: none). Proved sorry-free in
> [`QOU/Habiro/MirrorPairNormalisation.lean`](../../content/quantum-observable-universe/lean/QOU/Habiro/MirrorPairNormalisation.lean)
> (`coeffDiff_at_coincidence`). Differencing the traces instead gives
> `mult(Φ₈) = 2⌊(A−1)/2⌋` on **10/10** pairs with `Φ₁ = Φ₂ = 1` and `Φ₄ = A`.
> Read the tables below as a record of what was measured, not as the pair's
> cyclotomic content. Full analysis, including which specific claims here do
> not survive:
> [`2026-08-18-mirror-pair-a-m-differencing-normalisation-defect.md`](2026-08-18-mirror-pair-a-m-differencing-normalisation-defect.md).

> **This doc's two claims SURVIVE the correction.** They were computed on
> partial sums of the a_m-difference and so had to be re-measured; on the
> corrected trace difference `M_first_Φ₈ = 7` holds **9/9** and
> `M_first_Φ₈² = 15` holds **9/9**, now including ⁶He−⁶Be and ¹⁴O−¹⁴C, which
> were the two anomalies under the old differencing. The boundary structure is
> genuinely universal even though the multiplicity read off the same object was
> not. Only the `mult(Φ_8)` column below is superseded.


## TL;DR

PR #1625 found `M_first_Φ_8 = 7` for atomic-step pair-differences (D−n, ³He−D, ⁴He−³He) and observed Φ_8² appearing at M = 15 in (⁴He−³He). This probe extends both boundary checks to mirror pairs and finds:

  **`M_first_Φ_8` = 7  for all 9 mirror pairs with mult(Φ_8) > 0**
  **`M_first_Φ_8²` = 15  for all 9 mirror pairs (regardless of total multiplicity)**

The boundary structure is **universal** across pair-difference types (atomic-step AND mirror); what's pair-dependent is the multiplicity m (= number of Φ_8 factors in the full Habiro sum).

## Data

| Mirror Pair | A | M_max | mult(Φ_8) | **M_first_Φ_8** | **M_first_Φ_8²** |
|---|---|---|---|---:|---:|
| n − p | 1 | 8 | 0 | (no Φ_8) | (no Φ_8) |
| ³He − ³H | 3 | 15 | 2 | **7** | **15** |
| ⁵Li − ⁵He | 5 | 19 | 4 | **7** | **15** |
| ⁶He − ⁶Be | 6 | 21 | 2 | **7** | **15** |
| ⁷Be − ⁷Li | 7 | 23 | 6 | **7** | **15** |
| ⁸B − ⁸Li | 8 | 25 | 6 | **7** | **15** |
| ⁹B − ⁹Be | 9 | 27 | 8 | **7** | **15** |
| ¹⁰C − ¹⁰Be | 10 | 28 | 8 | **7** | **15** |
| ¹²N − ¹²B | 12 | 31 | 10 | **7** | **15** |
| ¹⁴O − ¹⁴C | 14 | 33 | 4 | **7** | **15** |

9/9 mirror pairs with Φ_8 multiplicity ≥ 0 show **M=7 first boundary** and **M=15 second boundary**, independent of A, total mult, magic structure, or anomaly status.

## Categorical interpretation

Per PR #1625's identification:

  `M_first_Φ_8 = 7 = ord(σ_i in H_n(ζ_8)) − 1`

That is: in the Iwahori-Hecke algebra at q = ζ_8 (level-2 SU(2) Verlinde Wenzl projector kernel), the generator σ_i has order 8 (since the Hecke relation `(σ_i − q)(σ_i + q⁻¹) = 0` at q = ζ_8 has eigenvalues `ζ_8` and `−ζ_8⁻¹`, with minimal polynomial of order lcm(8, 8) = 8). The M = 7 boundary is one less than that order — the first M at which the canonical level-2-Wenzl-annihilator linear relation triggers.

**M_first_Φ_8² = 15 = 2·M_first_Φ_8 + 1.** This is a clean arithmetic relation suggesting the second Wenzl-annihilator linear relation triggers at M = 2·(ord − 1) + 1 = 15. Interpretation hypothesis: the bar-conjugate annihilator `[−4]_q = 0` at q = ζ_8⁻¹ contributes its first cancellation at M = 8 (delayed by half a period?) and the SQUARED annihilator (`[4]_q · [−4]_q`) acts at M = 8 + 7 = 15.

This deserves a Lean formalization parallel to PR #1625's `(ζ_8; ζ_8)_7 = 8`, `ord(σ_i)|q=ζ_8 = 8`, `[4]_q|q=ζ_8 = 0`:

  **Conjecture (Lean target):** `M_first_Φ_8² = 2·ord(σ_i in H_n(ζ_8)) − 1 = 15`.

## Why this matters for the A=6, A=14 anomalies

The A=6 (mult=2) and A=14 (mult=4) anomalies are NOT explained by a different boundary structure — both pairs have `M_first_Φ_8 = 7` and `M_first_Φ_8² = 15` exactly like the matching pairs. The anomaly is in the TOTAL multiplicity at the upper end M_max:

- Matching pairs reach `mult(Φ_8) = A − 1` (odd A) or `2⌊(A−1)/2⌋` (even A) by accumulating Φ_8 factors at M=7, 15, 23, 31, ... (period 8).
- Anomalous pairs (A=6, A=14) hit the first 2 boundaries (M=7, M=15) but DROP from there — fewer Wenzl-annihilator relations are triggered by the pair-specific Wedderburn-block content past M=15.

This is consistent with the magic-shell hypothesis: anomalous pairs (A=6 ⁶He(Z=2)/⁶Be(N=2); A=14 ¹⁴O(Z=8)/¹⁴C(N=8)) have one magic shell per half, contracting the Wedderburn support and reducing the per-pair relations beyond M=15.

## Connection to the existing magic-shell corpus

(Per AGENTS.md §"Before declaring 'open' math" corpus-grep — user correctly recalled this exists.)

- [`prop:categorical-neutrality-saturated-shells`](../../content/quantum-observable-universe/mass-endomorphism/categorical-neutrality-saturated-shells.md): at magic n, full-twist Δ²_n acts as identity ⇒ Wedderburn support contracts to self-conjugates.
- [`conj:diagrammatic-double-magic-lr-fusion`](../../content/quantum-observable-universe/observations/diagrammatic-double-magic-lr-fusion.md): LR-fusion of two magic shells is rigid.
- [`prop:magic-numbers-from-q`](../../content/quantum-observable-universe/observations/magic-numbers-from-q.md): magic numbers emerge from substrate q₀ via Hoefsmit seminormal forms.
- MAG-1 audit (2026-05-02): all 7 magic numbers verified.

These propositions act at the **single-shell** level (the mass endomorphism Φ_n at a specific n). The mirror-pair Φ_8 multiplicity drops are the empirical signature at the **pair-difference** level — when the contraction propagates through the LR fusion to the pair Markov trace.

## Open follow-up

1. **Verify M_first_Φ_8³ = 23?** Predicts the third boundary at 8·k - 1 form: M = 7, 15, 23, 31 → period 8 starting at 7. Requires extracting Habiro coefficients to higher M for the higher-multiplicity pairs (e.g. ¹²N−¹²B with mult=10 should have Φ_8³ visible).
2. **Lean formalization** of `M_first_Φ_8 = 2·ord(σ_i)·k − 1` for the k-th Wenzl-annihilator cascade.
3. **LR-fused per-block χ_λ** evaluation at q = ζ_8 per pair — directly count which Wedderburn blocks are killed and verify the anomalous-pair mechanism.

## Probe script + witness

- [`computations/topic2_mirror_pair_phi8_boundary_scan.py`](../../computations/topic2_mirror_pair_phi8_boundary_scan.py)
- Witness: [`computations/topic2-mirror-pair-phi8-boundary-scan.witness.json`](../../computations/topic2-mirror-pair-phi8-boundary-scan.witness.json)
