# α via an archimedean Li_2^q convergent expansion (2026-06-29)

**Branch:** `claude/flavor-split-alpha-dilog-derivation-2026-06-29`
**Follows:** the partial derivation (`2026-06-29-flavor-split-partial-derivation.md`) —
the flavor split is `leading·(1 + α·leading)` (second-order structure proven), α
the single open O(1) coefficient. This probes whether α has a convergent
archimedean `Li_2^q` expansion we can calculate.

Probe: `computations/probes/flavor_split_alpha_dilog_expansion_probe.py` (+ witness).
`Li_2^q(z) = Σ_{n≥1} z^n/(n·[n]_q)` is the archimedean realization evaluator
(`_li_2_q_util.li_2_q`). Tested principled correction factors `C` (full = leading·C)
at **both** anchors (proton-q₀, muon-q₀).

| form C (full = leading·C) | implied α | split err vs CODATA |
|---|---|---|
| geometric `1/(1−leading)` (self-energy) | 1.0014 | **0.0098%** |
| q-deformed `Σ leadingⁿ/[n]_q` | 1.0007 | 0.0098% |
| `exp(leading)` | 1.0007 | 0.0098% |
| `−log(1−leading)/leading` | 0.500 | −0.059% |
| `Li_2^q(leading)/leading` | 0.249 | −0.094% |
| **experimental** `α_true = (C_true−1)/leading` | **0.9293** | 0 (def) |

## Findings

1. **The geometric / q-dilog self-energy is a genuine derivable, convergent,
   parameter-free archimedean form: α = 1, accuracy 0.0098%** — better than the
   deprecated posited `(1+ℏ_q³)` (0.0305%) and 13× better than leading-only
   (0.128%). It IS a "convergent expansion we can calculate."

2. **Your q-dilog-softening hypothesis is numerically ruled out for the
   residual.** The idea — that the `[n]_q` denominators soften the classical
   geometric α=1 down to the experimental 0.929 — fails because at the small
   argument `leading ≈ 0.00138`, `[n]_q ≈ n` to ~0.1%. So q-geom (α=1.0007) is
   indistinguishable from classical geom (α=1.0014): the whole α≈1 family
   collapses to the same 0.0098% split error. The q-deformation supplies ~0.1%,
   not the **7.8%** softening needed to reach 0.929.

3. **α_true = 0.9293 is anchor-stable to 5.8e-8** — a real O(1) constant. It
   sits between the geometric (≈1) and the dilog-of-`leading` (0.25–0.50)
   values, closest to but ~7.8% below the geometric.

## Honest scope + next direction

- **Derivable now:** the geometric/q-dilog self-energy `leading/(1−leading)`,
  α = 1, 0.0098%. This supersedes `(1+ℏ_q³)` and is the archimedean
  parameter-free prediction.
- **Open:** the exact α = 0.9293 (a 7.8% softening below the geometric). This is
  **not** a q-dilog effect at the `leading` argument. The principled next target
  is the **archimedean bond energy itself** — `E = E_0·log(1/f_pn)` with the
  `Li_2^q(−|V̂|)` spectral corrections (`T2`/`T3` in `_li_2_q_util`), whose
  arguments are O(1) crossing weights `z ≈ 0.5`, `h ≈ 0.21` — where the dilog
  *does* contribute at O(1). Computing the flavor split directly from that
  trace-energy expansion (rather than guessing a closed form for α) is the
  genuine derivation. **We deliberately do NOT fit 0.929 to a dilog of z/h**
  (the c_k-flip-flop trap); a derivation must produce it from the trace
  normalization.

## Can α improve Q_β? — NO (and α is closed as non-critical)

Probe: `flavor_split_alpha_qbeta_amplification_probe.py` (+ witness). Identity
`Q_β = (m_n−m_p) − m_e = M_N·split − m_e` suggests a better flavor split could
sharpen Q_β (which misses its L2 target by 160×). It cannot:

`Q_β ≈ 0.782` is the small *difference* of `Δm ≈ 1.293` and `m_e ≈ 0.511`, so a
relative error in Δm is **amplified by Δm/Q_β ≈ 1.65×** into Q_β. The best
*derivable* flavor split (geometric α=1, 0.0098% on Δm) gives Q_β at
**~1.6e5 ppb** — ~128× **worse** than the production **Habiro** Q_β path
(~1248 ppb), which is already the dedicated route.

**α closure (critical-distance).** α is a clean structural result, but it has
no critical-path use:

| intended use | verdict |
|---|---|
| color-weighting δ (trace crossing) | de-wired to proven leading — α not used |
| Q_β | NO — amplification, 128× worse than Habiro |
| Δm_pn | NO — already 7e-7 via Q_β/Path C |

So α is **closed** as understood-but-non-critical: the second-order structure
is proven, the geometric self-energy (α=1) is the derivable archimedean form
(0.0098%), and the exact 0.929 remains open R&D with **no observable that
needs it**. Recorded so it is not re-chased.

## Reproduce
```bash
python3 computations/probes/flavor_split_alpha_dilog_expansion_probe.py
python3 computations/probes/flavor_split_alpha_qbeta_amplification_probe.py
```
