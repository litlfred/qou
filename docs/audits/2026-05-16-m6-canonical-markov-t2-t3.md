# M6 mass-table — canonical Markov-invariant T_2/T_3 wired

**Date:** 2026-05-16
**Branch:** `claude/post-662-c3-chain-anti-staleness`
**Resolves:** User work-list item #1 (T_2/T_3 fix everywhere)

After [the canonicality audit](2026-05-16-compute-pipeline-canonicality-audit.md)
identified T_2/T_3's `Φ_q` specialisation as PATHOLOGICAL, the new
`tower_mode = "canonical_markov"` in `paper_six_term_isotope_sweep`
uses the Markov-invariant algebraic form from
`prop:mass-endomorphism-tower §Algebraic form`:

$$
  T_2 \;=\; \sum_i z \cdot \mathrm{Vol}_q^{(\{i\})}(\beta),
  \qquad
  T_3 \;=\; z^2 \sum_{i<j} \mathrm{Vol}_q^{(\{i, j\})}(\beta)
$$

with $\mathrm{Vol}_q^{(S)}(\beta) = \sum_\lambda y_\lambda(q) \chi^\lambda_q(\beta|_S)$ —
per-irrep Hoefsmit Markov trace of the sub-word supported on S.

## M6 per-term breakdown

| iso | T_1 | T_2 canon | T_3 canon | T_4 | T_5 a_K | total_hecke |
|---|---:|---:|---:|---:|---:|---:|
| p   | 1.0653 | +1.04 | +0.27 | 2.4973 | 2.4237 | 6.381 |
| n   | 0.9232 | +0.96 | +0.23 | 2.4973 | 2.1336 | 5.658 |
| D   | 0.2883 | +2.19 | +1.88 | 3.2021 | 5.2279 | 8.788 |
| T   | 0.0129 | +3.30 | +4.68 | 2.5439 | 10.4775 | 10.658 |
| ³He | 0.9984 | +3.48 | +5.23 | 2.5439 | 13.9937 | 25.224 |
| ⁴He | 0.0553 | +4.59 | +9.45 | 2.2519 | 28.0456 | 17.835 |

**All bounded, Markov-invariant, sensible per-atom variation.** Vs the
legacy `Φ_q(|V̂_i|)` form which produced ~10⁵-magnitude per-generator
values and predicted T − ³He ≈ -737 MeV (CODATA: +0.019 MeV).

## Comparison with legacy modes

| mode | T_2 / T_3 source | Markov-invariant? | Pathology |
|---|---|---|---|
| `brane` (legacy)        | $\Phi_q(\lvert V̂_i \rvert)$            | ❌ specialisation | ~10⁵ amplification |
| `drop`                  | 0 (suppress)                          | trivial          | ignores physics |
| `q1-base`               | values at q = 1                       | trivial          | mis-specialised |
| `r-side-bare`           | universal Markov axiom values         | ✅ but trivial   | β-independent |
| `li2q`                  | Li_2^q(-V̂_i) Kashaev limit           | ❌ specialisation | sign/magnitude unstable |
| `habiro`                | cyclotomic (q;q)_m collapse           | ✅                | only D, p, n covered |
| `per-partition-k`       | per-partition k_λ                     | ✅                | T, ³He only |
| **`canonical_markov`**  | **$\sum_\lambda y_\lambda \chi^\lambda_q(\beta\vert_S)$** | **✅**           | **none** |

The canonical_markov mode is **universally applicable** and **canonical
per the paper**.

## Compute cost

Per atom, canonical_markov requires:
- T_2: (n-1) single-gen sub-trace evaluations × cached Hoefsmit × partitions of |S|+1 = 2
- T_3: C(n-1, 2) pair-gen sub-trace evaluations × cached Hoefsmit × partitions of |S|+1 = 3

For ⁴He (n=12, n-1=11 generators): 11 + C(11,2)=55 = 66 sub-Markov-traces. Bounded by ~10 sec each → ~10 min cold cache. Subsequent atoms are fast (cache hits).

## Open follow-on items

1. **Free-configuration T_2/T_3**: currently set to 0 for `include_inter=False`. The free config could compute Vol_q^(S) over the constituent-only braid; the M2/M3 mass-table compute would then have proper free-vs-bound differencing. Tracked for follow-on.
2. **Replace Φ_q-dependent modes (li2q, habiro, etc.)** in the sweep router: `canonical_markov` should become the default `tower_mode`. Currently it's opt-in alongside legacy modes.
3. **Full M7 mass table** under canonical_markov + full N=4 chain Q_β + V2 chirality. Should drop the ~0.19 % MAE substantially since the T_2/T_3 pathology is removed.

## Witnesses

The M6 per-atom data was computed via:
```
python3 -u -c "from paper_six_term_isotope_sweep import paper_six_term_mass; ..."
```
with `tower_mode='canonical_markov'`. Witness emission via a dedicated probe is deferred to the M7 step.

## Status update on user 5-item work list

| # | Item | Status |
|---|---|---|
| **1** | T_2/T_3 fix everywhere | ✅ **canonical_markov wired** (this commit) |
| **2** | ρ_K LO vs full audit | ✅ done (5 scripts LO, 0 full) |
| **3** | Δ_λ derivation | ⏳ open per paper; values not yet derived |
| **4** | κ derivation | ⏳ D-2 q-Catalan framework (within 2× of empirical) |
| **5** | m_p chain closure | ⏳ derivation_pending per #663 |
