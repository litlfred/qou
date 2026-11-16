---
# qou-quv8
title: 'D: bar-parity split — μ₀∝(q−q⁻¹) is bar-odd; add bar-even 2nd-order term (mirrors Q_β c_k); cross-check A'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-19T17:54:15Z
updated_at: 2026-11-16T19:19:00Z
parent: qou-wp3h
---

## Progress Update (2026-11-16 — PR #8164)
- **PR:** [`litlfred/qou#8164`](https://github.com/litlfred/qou/pull/8164) (`47da262e4f487a8f51de58f3577a63d5b17e6d6a`)
- **Resolution:**
  - Formalized in `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/BorromeanChiPerRep.lean` (`0` `sorry`, `0` self-assuming audit hits) the bar-parity split of the higher-order NA-Stokes counit expansion $\mu_{\text{eff}}(h) = \mu_{\text{odd}}(h) + \mu_{\text{even}}(h)$ under $h = q - q^{-1} \mapsto -h$:
    - `naStokesMuOdd c1 c3 h := c1 * h + c3 * h^3` (`naStokesMuOdd_neg`)
    - `naStokesMuEven c2 c4 h := c2 * h^2 + c4 * h^4` (`naStokesMuEven_neg`)
    - `naStokesMuEff_bar_parity_split`: proves $\mu_{\text{eff}}(h) + \mu_{\text{eff}}(-h) = 2 \mu_{\text{even}}(h)$ and $\mu_{\text{eff}}(h) - \mu_{\text{eff}}(-h) = 2 \mu_{\text{odd}}(h)$.
  - Verified to 50+ dps (`< 1e-72` residual) at $q_0$ in `computations/probes/na_stokes_bar_parity_local_bond_probe.py` (`na-stokes-bar-parity-local-bond.witness.json`).
  - Status kept at `in-progress` pending PR #8164 merge and owner verification.
