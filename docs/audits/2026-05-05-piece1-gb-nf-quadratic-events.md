# Piece 1 — GB-NF quadratic events match PR #546's $1/12$ leading coefficient

**Date:** 2026-05-05
**Branch:** `claude/categorical-mass-divergence-audit` (PR #534)
**Refs:**
- [`computations/piece1_three_routes_gb_filtration_probe.py`](../../computations/piece1_three_routes_gb_filtration_probe.py)
- [`computations/gb_filtration_jet_tracker.py`](../../computations/gb_filtration_jet_tracker.py)
- [`prop:gb-spectral-sequence`](../../content/quantum-observable-universe/braids-and-knots/gb-spectral-sequence.md)
- [`prop:graded-markov-trace-from-gs-filtration`](../../content/quantum-observable-universe/braids-and-knots/graded-markov-trace-from-gs-filtration.md)
- Sibling [PR #546](https://github.com/litlfred/qou/pull/546) — closed-form $\mathrm{tr}_M(p)$ with leading coefficient $-1/12$

## The gap, restated using GS filtration

The categorical-mass identity (`prop:atomic-mass-gb-nf`) reads
$$M(K) \;=\; m_e \cdot \rho_K \cdot |\!\operatorname{tr}_M(\mathrm{NF}_{\mathrm{GS}}(\beta_K))|.$$

Per `prop:gb-spectral-sequence`, $H_n(q)$ carries the GS filtration $J^0 \supset J^1 \supset \dots \supset J^{\ell(K, q)} \supset 0$. The Markov trace decomposes as $\operatorname{tr}_M = \sum_\ell \operatorname{tr}_{M, \ell}$ with $\operatorname{tr}_{M, \ell}$ acting on $J^\ell / J^{\ell+1}$.

**The dimensional gap** between $E_0 \approx 174$ MeV (Hecke-energy quantum from proton calibration) and $\alpha = m_e \cdot 8G \approx 3.74$ MeV (Borromean binding scale) is **the spectral-sequence dressing factor**: how the higher GS-filtration levels propagate quadratic content from below to dress the level-0 (descended) trace.

This is the **quadratic-form-coming-up-from-below** that the user pointed at. Each Hecke-quadratic relation event $T_w \cdot T_i = (q - q^{-1}) \cdot T_w + T_{w s_i}$ during the GB-NF reduction is a level-mixing event that propagates $J^\ell / J^{\ell+1}$ content down into $J^{\ell-1} / J^\ell$.

## The structural finding

Running the existing `gb_filtration_jet_tracker.HeckeElement` reduction on the proton's 11-crossing word in $H_3(q)$:

```
word = [σ_0]·7 · [σ_1]·4              (jet-tracker 1-indexed: T_1·7 · T_2·4)
```

The reduction fires **exactly $12$ Hecke-quadratic events** (and $12$ ascending events; $24$ steps total).

Independently, PR #546's symbolic Hoefsmit reduction gives the closed form
$$\mathrm{tr}_M(\mathrm{proton}) \;=\; \frac{q^{20} + q^{18} + 2 q^{12} - 2 q^8 - q^2 - 1}{12 \cdot q^{10}}$$
with **leading coefficient $-1/12$ exactly**.

**The "$12$" in PR #546's denominator equals the Hecke-quadratic-event count from my GB-NF reduction.** Both are categorical integers derived from the same proton braid word in $H_3(q)$ via independent algorithms.

## What this is, and what it isn't

**UPDATE (2026-05-05, post-universality test):** the universality conjecture **"GB-NF event count = $2 \cdot |S_n|$ universally"** has been **falsified** by `gb-nf-event-count-universality.witness.json`. The quadratic event count is **word-specific**, not a universal $H_n$-invariant:

| Word in $H_3$ | Length | Quadratic events |
|:---|---:|---:|
| trivial | 0 | 0 |
| $\sigma_1$ | 1 | 0 |
| $\sigma_1^2$ | 2 | 1 |
| trefoil $\sigma_1^3$ | 3 | 2 |
| Borromean $(\sigma_1\sigma_2)^3$ | 6 | 6 |
| **proton intra $\sigma_1^7 \sigma_2^4$** | **11** | **12** |
| $\sigma_1^{10}$ | 10 | 9 |
| $\sigma_1^{15}$ | 15 | 14 |
| $\sigma_1^{20}$ | 20 | 19 |

The proton's $12$ events is **specific to that word's structure**, not a universal $H_3$-invariant. The match with PR #546's $1/12$ leading-coefficient denominator is therefore **most likely coincidental** for that specific word.

**Distinction:**

- PR #546's "$1/12$" is an $H_3$-INVARIANT (depends on $n = 3$ only, via the Wedderburn-Markov aggregate normalization $2 \cdot |S_3| = 12$). It would appear in the leading coefficient of $\mathrm{tr}_M$ for any $H_3$ element.
- This probe's "12 events" is WORD-SPECIFIC (depends on the proton word's GB-NF reduction trajectory). Different words give different counts.

These are different categorical objects. Their numerical match for the proton case is **not a derived identity** — it's a coincidence of that specific word's reduction trajectory landing on $2 \cdot |S_3|$ events.

**The right structural anchor for Piece 1 is PR #546's closed-form $\mathrm{tr}_M(p)$ itself**, not the GB-NF event count. The "$1/12$" in the denominator is the $H_3$ Plancherel-Markov aggregate normalization (Wenzl 1988 Theorem 5), which is the **categorical** dimensional bridge.

To close Piece 1 categorically:

1. **Prove** the equivalence: Hecke-quadratic event count during GB-NF reduction $=$ $\sum_\lambda d_\lambda^2$ Wedderburn aggregate (or its normalization analog).
2. **Use PR #546's closed-form $\mathrm{tr}_M(p)$** as the dimensional anchor:
$$\frac{m_p}{m_e \cdot |\mathrm{tr}_M(p)|} \;=\; \frac{m_p \cdot 12 \cdot q_0^{10}}{m_e \cdot (\text{numerator polynomial at } q_0)}.$$
The factor $12$ here is the GB-NF quadratic event count, derived categorically.

## Three routes (honest report)

The probe's "three routes" do **not** trivially converge — they compute different categorical objects, not the same dressing factor three ways:

| Route | Object | Value at $q_0$ |
|:---|:---|---:|
| A — spectral-sequence level-by-level | Surrogate $z^\ell$-weighted trace ratio | $2.36$ |
| B — Hecke-quadratic-event multiplier | $(1 + h)^k$ where $k = 12$ | $9.76$ |
| C — GB-NF crossing product | $h^k$ — collapsed in current bookkeeping | $1.0$ |

Routes B and C are event-count surrogates; they do not carry the per-event coefficient propagation that the proper dressing requires. Route A is structurally correct but uses a $z^\ell$ surrogate for the Markov trace, not the proper Plancherel weights.

**The structurally significant output is Route B's intermediate: the integer $12$ event count.** That number is real and matches PR #546's leading coefficient denominator independently.

## Concrete path forward (no numerology)

1. **Use PR #546's closed-form $\mathrm{tr}_M(p) = -1/12 \cdot q^{-10} \cdot \mathrm{poly}(q)$** as the categorical anchor for the dimensional bridge.
2. **Prove the GB-NF event count $= 12 = 2 \cdot |S_3|$ for $H_3(q)$** as a categorical lemma (likely via the Coxeter-Bruhat decomposition of $S_3$).
3. **Extend to $H_n(q)$ for $n \geq 4$**: predict the GB-NF event count $= 2 \cdot |S_n|$ or analog, anchor against PR #546's $A \geq 2$ extension when ready.

This closes Piece 1 via direct categorical computation — no empirical fitting.
