---
# qou-y3bm
title: 'OPEN DERIVATION: the E_0 tower sum 1/(1-hbar_q^2) is canonical by ruling but never derived'
status: todo
type: task
priority: normal
created_at: 2026-09-12T19:04:21Z
updated_at: 2026-09-12T19:06:21Z
---

**What is wrong.** `E₀`, the Q_β energy scale, had **two live forms** in
`computations/qbeta/`, differing by `1/(1 − ℏ_q²) = 1.00991452` (**+0.9915 %**),
with no signal at either call site:

| form | value | where |
|---|---|---|
| order-zero `m_e/(q(q−1))` | 4.18598136 MeV | most call sites, incl. the dashboard |
| tower-summed `… /(1 − ℏ_q²)` | 4.22748336 MeV | `qbeta_bar_branch_refuted_probe.py:88`, annotated *"tower-summed, as ruled"* |

**Unified 2026-09-12 on owner instruction** in
[`computations/qbeta/qbeta_e0.py`](../computations/qbeta/qbeta_e0.py):
`canonical()` = `tower_summed()`, per the 2026-09-03 full-tower ruling
(*"should make use of the full tower even though what is observable is only
order zero"*). `order_zero()` is kept, named for what it is, so historical
figures stay reproducible. The dashboard routes through it.

**🛑 WHAT REMAINS OPEN — and it is the whole bean.** That the tower sum **is**
the geometric series `Σ_{k≥0} ℏ_q^{2k} = 1/(1 − ℏ_q²)` is taken from that one
precedent's annotation. **I did not find a derivation in the corpus and did not
construct one** — inventing a series to justify a factor already in use is
exactly the laundering AGENTS.md forbids. So `tower_summed` is canonical **by
ruling** and open **by proof**.

**What would close it:** derive the tower sum from the Hecke-tower structure —
which orders in `q` contribute, why the ratio is `ℏ_q²` rather than `ℏ_q` or
`h²`, and whether it terminates (the Habiro-ring element terminates at `M = 8`,
which is *not* a geometric series, so the two pictures need reconciling). Until
then, **say "assumed" wherever `E₀`'s tower factor is quoted.**

**Scale, so this is not mistaken for the Q_β problem.** `E₀` moves the row
**0.9915 %**. The convention-D functional moves it **257×** base-to-base. Two
different orders of magnitude; fixing `E₀` does not address the gap.

**Remaining call sites to route through the module** (not done — each needs
checking that it is not deliberately order-zero):
`qbeta_admissible_functionals_bracket_probe.py:164`,
`qbeta_counit_substrate_consistency.py:86`,
`qbeta_habiro_f_from_shape_collapse.py`, `qbeta_markov_trace_steps_4_5.py`.

**A guard fired during this unification and the lesson is worth keeping.**
Routing the dashboard onto the tower `E₀` **silently reverted the whole Q_β row**
to the retired `z = 1` cell: the re-score calibrates against a witness cell
computed at *order-zero* `E₀`, so the +0.99 % shift broke the comparison and the
producer correctly refused to publish. The guard worked; the calibration was
asking the wrong question (it conflated "is my trace right?" with "which `E₀` is
canonical?"). Fixed by calibrating the trace at the `E₀` the cell used, then
publishing at the canonical `E₀` — **one check per claim**. The failure mode was
a *silent revert*, not an error.

Full analysis: `docs/audits/2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md` §5(c), §6.
