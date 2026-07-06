# b0vf — markov-peel cross-check resolves the He-4 scalar tr_M (2026-06-29)

**Bean:** `b0vf` — *"chi-helium-4-h12-at-q0-50dps.witness.json only 17/77
complete (22%) — needs He4 H12 chi producer re-run."*

**TL;DR.** The *scalar* Markov trace `tr_M(β_⁴He)` is **already canonical
and complete** via the independent **markov-peel** method — no Hoefsmit
per-partition grind is needed for it. The 27/77 partial χ-sum witness is
genuinely incomplete (≈0.1 % high), but its only unique deliverable is the
**per-partition χ_λ decomposition**, not the scalar. This note records the
cross-check so no future session re-runs weeks of compute to recover a
number that already exists.

## The three He-4 objects (do not conflate them)

| witness / method | quantity | value @ q₀ | completeness | q₀ pin | cost |
|---|---|---|---|---|---|
| `markov/markov-peel-atomic-tr-m.witness.json` (He-4 row) | normalized `tr_M` | `0.055358426266783106…` | **complete** | muon `…955573347` | **96.8 s** |
| `chi-helium-4-h12-at-q0-50dps.witness.json` | normalized `tr_M` = Σ_λ y_λ χ_λ | `0.055414100884379576…` | **27/77 partial** | muon `…955573347` | 68 501 s (19 h, incomplete) |
| `chi-helium-4-h12-at-q0-50dps-matrix-m.witness.json` | raw M-matrix trace | `0.885616401506…` | 77/77 complete | **retired-proton** `…827513808` | — |

The first two are the **same observable at the same pin**, so they are
directly comparable. The third is a **different normalization at a
different pin** (the retired-proton q₀; per the bean's 2026-06-29 note its
1e-7 drift is the muon↔proton convention class, owner-gated under
`tnjb`/`z5vu` — *not* an engine or completeness defect).

## Cross-check

```
markov-peel He-4 (muon, complete, 96.8 s) : 0.055358426266783106469852…
chi-sum         (muon, 27/77 partial)     : 0.055414100884379576159189…
gap (chi − peel)                          : 0.000055674617596469689337…
relative gap                              : 1.0057e-3   (0.1006 %)
```

The 0.1 % gap is exactly the **net contribution of the 50 missing
partitions** (all ≥ 3 rows; the 7 two-row partitions that carry ~84 % of
the |contribution| mass are all in the computed 27). It is four orders of
magnitude larger than the leading-δ change (~1e-6), so the partial is not
a δ-staleness artifact — it is genuine incompleteness.

## Why the χ-sum producer is slow (and why markov-peel is not)

The per-partition producer builds the full **Hoefsmit seminormal
representation matrix** (dim_λ × dim_λ) for each λ ⊢ 12 in pure-Python
`mpmath` at 50 dps, then traces the braid word — cost ~O(dim²·|β|) per
partition. For balanced λ the dimension reaches ~5 600; one partition
(`[6,3,2,1]`, dim 5632) alone took **43 896 s ≈ 12.2 h**. The 50 missing
partitions are the *largest-dimension* balanced ones, so completing the
decomposition is a **multi-week** compute — infeasible in an ephemeral
sandbox.

markov-peel instead reduces β to **Hecke normal form** and traces, never
materializing a per-partition seminormal matrix — hence He-4 in 96.8 s.

## Correction to the dominance probe

`computations/probes/he4_partition_dominance_audit_probe.py` reports the
missing-partition tail as ≤ 5.3e-52. That bound is **circular**: its
`reported_tr_M` is the cached partial sum itself
(`source = "cached_sum / reported_tr_M"`), so it compares the 27-partition
sum to itself. The markov-peel cross-check above is the *independent*
measurement and shows the real tail is **5.6e-5**, not 1e-52. The probe's
*structural* verdict (2-row partitions dominate, ~84 %) stands; only its
tail bound is an artifact.

## Disposition (no compute, no q₀ flip)

- **Scalar tr_M(He-4):** use the markov-peel value `0.055358426…` (muon
  pin) — canonical, complete, already on `main`.
- **Per-partition χ_λ(He-4):** the 27/77 partial is flagged
  known-incomplete (≈0.1 % high vs markov-peel); it is **not** to be
  trusted as converged. A complete 77/77 per-partition table exists in the
  `-matrix-m` sibling but at the retired-proton pin — merging across pins
  is the owner-gated q₀-convention migration (`tnjb`/`z5vu`); **not done
  here**.
- No witness regenerated; no q₀ flipped; tree otherwise clean.
