# qou-awpk: per-winding Stokes constants of 4₁ — extraction, certification, and the effective A at the observed ϑ sheets

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


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
V4 guard, and its witness recorded `"S11_at_substrate": 0.2584…` with
`"stable_digits": 40` — **the sentinel value**. **Fixed on this PR:** the
g3 guard now reports 0 digits on a diff ≥ 1, its deep order was raised
to the honest range (q̃-order 1600), and the regenerated witness
self-corrects to `0.42764420131745803633 [13 stable digits]` — agreeing
with this probe's independent ladder evaluation (Finding 3a) to 13+
digits. This probe uses the same honest guard discipline throughout.

## Finding 3 — substrate values, the honest tower, and the convergence annulus

Per-winding substrate values (exact-int canonical-chamber engine,
internal-order ladder 1600/2400/3200, ≥ 26 agree-digits each), q̃ = 1/q₀:

| e | I(0,e)(q̃) | e | I(0,e)(q̃) |
|---|---|---|---|
| 0 | +0.581410712237 | 8 | +0.041106402381 |
| 1 | −0.300207905140 | 15 | +0.056408932091 |
| 2 | +0.142274900685 | 16 | −0.085107294974 |
| 3 | +0.243725283769 | 25 | +0.113447381680 |
| 4 | −0.140964056760 | 28 | −0.083163701621 |

(full table in the witness).

**3a — the honest deep tower.** S⁺₁₁(q̃_sub) evaluated at q̃-order 1600 via
the certified sandwich exemplar, honest ladder guard (800/1200/1600, 13
agree-digits):

$$
S^+_{\sigma_1\sigma_1}(1;\tilde q_{\mathrm{sub}}) = 0.4276442013174\ldots
$$

— **superseding the g3 witness value 0.2584** (Finding 2). The per-winding
e-sum oscillates toward it (Σ_{|e|≤8} = 0.864, Σ_{|e|≤28} = 0.3995, residual
−0.028): the two summation orders agree at x = 1.

**3b — the winding sum has empirical radius of convergence 1.** The values
|I(0,e)(q̃_sub)| do **not** decay in e (0.041 at e=8, 0.085 at e=16, 0.113 at
e=25): |I(0,e)|^{1/e} → 1. Therefore Σ_e I(0,e)·wᵉ converges only on the unit
circle |w| = 1 (conditionally), and **every radial sheet is outside the
convergence annulus** — including the corpus sheet w = e^𝔲 with |w| = q₀ =
1.1100, which even exceeds the natural index-annulus boundary q̃^{−1/2} =
1.0535. Empirical confirmation: the radial partial sums are unstable in the
e-window (muon-sheet Im flips +0.073 → −0.569 from E=8 to E=28; the q₀²
convention reaches |A_eff|/A ≈ 27). Radial-sheet rows in the witness are
**divergent-partial-sum exhibits**, not evaluations; the E=28 q₀²-row
"Im-ratio 4.013" near |S_p/S_μ| = 4.075 is such an artifact (wrong sign, no
flip, window-unstable) and is **not wired**.

**3c — on the convergent domain the winding-refined Stokes is exactly
bar-even.** Amphichirality (I(0,e) = I(0,−e), certified) forces
Im A_eff ≡ 0 for |w| = 1 — verified to 1e-51. The effective coefficient
**does** vary with ϑ on the unit sheet (A_eff(ϑ_μ)/A_eff(0) ≈ 1.24,
A_eff(ϑ_p)/A_eff(0) ≈ 2.41 at E=28, e-window-slow), so the constant-A_ω
picture is not supported once winding is resolved — but no choice of ϑ
produces a bar-odd part by naive summation.

## Verdict

- **Extraction: done, exact.** The per-(e,ℓ) integer Stokes family of 4₁
  is in the corpus (Finding 1), the deferred e-sum item is closed, and the
  honest tower value at the substrate is 0.42764420 (Finding 3a).
- **Bean question ("does the effective A at the observed ϑ sheet differ
  from 3?"): scope-(a) answer.** On the σ₁σ₁ channel the winding-resolved
  effective coefficient is strongly ϑ-dependent (×1.2–2.4 across the T4
  sheets on the convergent domain) — the constant-A_ω simplification is
  not what the peacock structure gives. BUT:
- **The observed sheet is outside the naive-summation domain.** |w| = q₀
  exceeds the empirical convergence annulus (radius 1; even the index
  annulus bound q̃^{−1/2} = 1.054). The winding-refined S⁺_{σ₁σ₁} at the
  corpus sheet is only defined by **analytic continuation / lateral
  (Stokes) data**, not by the sum — and on the domain where the sum does
  converge it is exactly bar-even. This independently re-derives, from the
  winding side, the corpus's standing conclusion that a genuine bar-odd S
  must be lateral/Stokes (B1/#3923 lineage), and gives it a precise
  region-of-validity mechanism.
- **Scope-(a) negative for route 2's naive form:** per-winding refinement
  with naive summation does not reproduce the S sign flip or the −4.08
  ratio at the T4 sheets. The surviving form of route 2 is the *continued*
  x-refined Stokes matrix (GGM state-integral / lateral resummation at
  |x| > 1) — follow-up bean. Nothing refuted at scope-(b); nothing wired.


## Correction (2026-08-01, PR #4447) — Finding 3b was pre-asymptotic; the winding GF is ENTIRE on ℂ*

Finding 3b's "radius of convergence 1" and the verdict's "observed sheet is
outside the naive-summation domain" were **artifacts of the e ≤ 28 window**,
which sits entirely on the pre-asymptotic plateau. The leading q̃-power of
I(0,e) grows quadratically (lead(e) = T(⌈e/2⌉) ≈ e²/8), which forces the
substrate values to decay **super-exponentially** once past the hump —
measured on the exact engine (adaptive internal order, ladder-certified):

| e | I(0,e)(q̃_sub) | bare q̃^lead |
|---|---|---|
| 40 | 1.975·10⁻⁵ | 3.05·10⁻¹⁰ |
| 60 | −2.062·10⁻¹⁶ | 8.5·10⁻²² |
| 80 | −3.511·10⁻³² | 7.0·10⁻³⁸ |
| 100 | 1.927·10⁻⁵³ | 1.7·10⁻⁵⁸ |

Consequences (Lean-proved in
[`WindingGFTransform.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/WindingGFTransform.lean):
`summable_winding_of_sq_dominated`, `gf_three_term_of_sq_dominated`):

- **The winding generating function is entire on ℂ***: Σ_e I(0,e)wᵉ
  converges absolutely at EVERY w ≠ 0. The corpus sheet needs **no
  analytic continuation** — direct two-sided summation converges there
  (terms fall below 10⁻¹⁰ by e ≈ 55–60 at |w| = q₀²).
- **3c stands, sharpened**: on |w| = 1 the sum is exactly bar-even
  (amphichirality; Lean `pairedWindowSum_unit_sheet_im_zero`); off |w| = 1
  a bar-odd part CAN arise — the "bar-odd must be lateral/Stokes"
  re-derivation in the verdict was conditioned on the empty-domain
  reading and is **withdrawn as stated**; the honest evaluation at the
  corpus sheet is W2 (`qbeta_3bp8_w2_direct_sheet_probe.py`).
- The E = 28 radial rows remain window-unstable exhibits (that part of 3b
  was correct — the window straddled the hump); the "Im-ratio 4.013"
  anti-numerology flag stays.
- The W1 A2 failures (probe `qbeta_3bp8_annihilator_continuation_probe.py`)
  are explained by the same hump analysis: at |w| = 0.3 the negative-side
  hump reaches ~10¹⁷ (needs dps ≥ 80); at |w| ≈ 0.8 it peaks at ~0.26 —
  the re-specced A2 runs there.

Corrected per AGENTS.md §Before declaring refuted: the numerical results
stand; the scope of the 3b claim was wrong (scope-(a) re-scope, not a
deletion). Bean: `qou-ovph`.

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
