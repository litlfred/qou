# qou-awpk: per-winding Stokes constants of 4₁ — extraction, certification, and the effective A at the observed ϑ sheets

**Date:** 2026-07-31 · **Axis:** ϑ_K gap (`qou-qnnq`, route 2 `qou-awpk`) · **Tier:** structural + measurement (scope-(a)).
**No c_k wired; nothing fitted; T4 ϑ values consumed as fixed inputs, not re-fitted.**
**Probe:** [`qbeta_awpk_perwinding_stokes_41_probe.py`](../../computations/probes/qbeta_awpk_perwinding_stokes_41_probe.py)
· witness [`qbeta-awpk-perwinding-stokes-41.witness.json`](../../computations/probes/qbeta-awpk-perwinding-stokes-41.witness.json).

## Route

The landed T4/T5 chain (`qbeta_t4_stokes3_crux_probe.py`; T5 assembly
`S_K = A_ω·κ·(ln²q₀ − ϑ_K²)`) carries a **constant** Stokes coefficient
A_ω = 3. GGM's peacock-pattern structure (arXiv 2012.00062) says Stokes
constants form a **lattice-indexed integer family** — one per
(winding m, descendant ℓ) — and the proven-for-4₁ dictionary
(GGM 2007.10190 eq 5/80; Conjecture-4 eq 21 of 2012.00062, proven for 4₁)
x-refines the geometric Stokes entry by the winding number e:

$$
S^+_{\sigma_1\sigma_1}(w;\tilde q) \;=\; \sum_{e\in\mathbb{Z}} I_{4_1}(0,e)(\tilde q)\, w^{e},
\qquad
S^+_{\sigma_1\sigma_1}(1;\tilde q) = 1 - 8\tilde q - 9\tilde q^2 + 18\tilde q^3 + 46\tilde q^4 + \dots
$$

so the per-winding Stokes data over ι = Vol(4₁)/π are exactly the
3d-index coefficients I(0,e), and the observed sheet enters as the
meridian holonomy w = e^𝔲 (corpus 𝔲-coordinate; `qou-qnnq`:
𝔲 = ln q₀ + i·ϑ_K, and the NZ coordinate u = 2 log m).

## Finding 1 — the per-winding integer family, extracted and certified exactly

Per-winding I(0,e) computed on the validated DGG eq (4.18) flux-sum engine
(`qbeta_g3_fourone_index_assembly_corrected`, tranche-1 exact I_Δ):

| e \ q̃-power | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | −2 | −3 | 2 | 8 | 18 | 18 | 14 | −12 | −52 | −106 |
| ±1 | 0 | −2 | −2 | 2 | 8 | 16 | 16 | 10 | −14 | −52 | −102 |
| ±2 | 0 | −1 | −1 | 3 | 6 | 12 | 9 | 3 | −19 | −50 | −88 |
| ±3 | 0 | 0 | 0 | 2 | 4 | 6 | 2 | −4 | −20 | −42 | −64 |
| ±4 | 0 | 0 | 0 | 1 | 1 | 2 | −2 | −6 | −16 | −27 | −35 |
| ±5 | 0 | 0 | 0 | 0 | 0 | 0 | −2 | −4 | −8 | −12 | −12 |
| ±6 | 0 | 0 | 0 | 0 | 0 | 0 | −1 | −1 | −2 | −3 | 0 |
| ±7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| ±8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |

- **Closes the deferred item** of
  [`qbeta-g3-fourone-index-assembly-corrected`](../../computations/probes/qbeta_g3_fourone_index_assembly_corrected.py)
  ("e-sum numerical reproduction deferred"): the e-sum reproduces the
  printed rotated index `1 −8q̃ −9q̃² +18q̃³ +46q̃⁴ +90q̃⁵ +62q̃⁶`
  **exactly**, e-window stable (E = 14 vs 11), internal x-order 96.
  Spot check at q̃¹⁰: −106 − 2·(102+88+64+35+12+0−2−1) = −702 = the deep
  tower coefficient. ✓
- **Amphichirality per winding** is exact: I(0,e) = I(0,−e) at full
  order (e = 1,2,3 checked; DGG eq 4.19).
- Reading: the −8 at q̃¹ splits as −2|₀ − 2·2|₁ − 1·2|₂; each column is
  the winding-resolved integer decomposition of one descendant Stokes
  constant — the (e,ℓ) lattice family of the bean's framing.

## Finding 2 — a convergence-guard bug class (the `else-40` sentinel)

The first run of this probe evaluated the substrate layer at q̃-order 400
and reported "[40 stable digits]" on values that were **pre-asymptotic
garbage** (I(0,0) ≈ −4869 at an order where the series has not begun to
converge; index coefficients grow ~e^{c√k}, so at q̃ = 1/q₀ ≈ 0.9009 the
tail only turns over near q̃-order ~600). Root cause: the guard pattern

```python
conf = int(-mp.log10(conv)) if 0 < conv < 1 else 40
```

maps a truncation difference **≥ 1** — i.e. gross non-convergence — to
the same "40 digits" as an exact match. The same pattern ships in the
merged [`qbeta_g3_ggm_stokes_41.py`](../../computations/probes/qbeta_g3_ggm_stokes_41.py)
V4 guard, and its witness records `"S11_at_substrate": 0.2584…` with
`"stable_digits": 40` — **the sentinel value**, so that datum is
unverified pending re-evaluation (this probe's deep e-sum supplies the
honest number; see Finding 3). This probe now uses a multi-cut
certificate (partial sums at 4 cut points, diff ≥ 1 → 0 digits).

## Finding 3 — substrate values and the effective A at the observed sheets

<!-- FILL: deep-run results -->

## Verdict

<!-- FILL: after deep run -->

## Cross-references

- Bean: `qou-awpk` (route 2 of `qou-qnnq`); siblings `qou-offl`,
  `qou-mcus`, `qou-rdmr`.
- T4 chain: `computations/qbeta/qbeta_t4_stokes3_crux_probe.py`;
  T5 assembly `S = A_ω·κ·(ln²q₀ − ϑ²)` (merged #4415).
- Target audit: [`2026-07-11-qbeta-c3-pole-cusp-phase-tractability.md`](2026-07-11-qbeta-c3-pole-cusp-phase-tractability.md)
  (S(muon) = +0.00968298, S(proton) = −0.03945936, ratio −4.0751).
- Anti-numerology flag on 2·Vol(4₁) ≈ 4.0598 vs |ratio| 4.0751:
  recorded in `qbeta-g3-fourone-index-assembly-corrected.witness.json`,
  still **not wired**.
- AGENTS.md §"Before declaring refuted (a)/(b)"; §"Im(q) at fibre vs
  observable level".
