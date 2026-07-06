# c_3 [3]_q/25 3-rung closure — cross-anchor rigidity falsification (2026-06-04)

> **⮕ This falsification is encoded in the authoritative registry**
> [`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
> (§3: c_3 = EMPIRICAL, REFUTED as real-q fibre element). Read the registry
> for the consolidated c_k / d_k status.

> **Finding**: the 3-rung `[3]_q/25` Habiro closure for `c_3` (PR #1781)
> is a **proton-anchor near-match**, NOT a genuine real-q fibre element.
> It reproduces empirical `c_3` at the proton anchor (−0.0023 %) but
> **misses by −2.97 % at the muon anchor**. This is a falsification of
> the "universal real-q fibre element" reading — and a confirmation of
> the production-honest NEAR-MATCH tier. No production change.

## What was tested

PR #1781 found `c_3(q) = -(q²+q⁻²)·(1 + ℏ_q·[3]_q/25 + ℏ_q³/[2]_q)`
reproduces empirical `c_3` to 2.65 ppm **at the proton anchor**. The
open question (AGENTS.md §"Im(q) at fibre vs observable level"): is this
a genuine fibre-level Habiro element (reproduces empirical `c_3` at
every q₀ anchor) or a coincidence at one anchor?

The discriminator: evaluate the real-q formula at both established
anchors and compare its swing to the empirical `c_3` swing.

## The established cross-anchor facts (PR #1609 infra)

| anchor | q₀ | empirical c_3 |
|--------|-----|---------------|
| proton (m_p) | 1.10997858275… | −2.0693 |
| muon (m_μ) | 1.10997859555… | −2.0097 |

Anchor separation ≈ **1.28 × 10⁻⁸**, yet empirical `c_3` swings
**−2.88 %** — `c_3` is a hyper-sensitive *extracted* quantity (the tiny
`c_3·u³` ladder term), so `dc_3/dq ≈ 4.6 × 10⁶` near the anchor.

## Result

[`probes/qbeta_c3_habiro_3rung_crossanchor_rigidity_probe.py`](../../computations/probes/qbeta_c3_habiro_3rung_crossanchor_rigidity_probe.py)

| quantity | proton | muon |
|----------|--------|------|
| formula `c_3` | −2.0693481 | −2.0693481 |
| empirical `c_3` | −2.0693 | −2.0097 |
| err vs empirical | **−0.0023 %** | **−2.97 %** |

- **formula swing**: +6.18 × 10⁻⁷ %  (rigid)
- **empirical swing**: −2.88 %
- **swing ratio (formula / empirical)**: −2.15 × 10⁻⁷ — the formula
  swings **4.7 million times less** than empirical `c_3`.

## Interpretation

A smooth real-q function cannot have `dc_3/dq ≈ 4.6 × 10⁶`, so **no
real-q `c_3 = f(q)` can track the empirical swing** — the `[3]_q/25`
form is no exception. It matches at the proton anchor by construction
(it was found there) and is rigid everywhere else.

This is exactly the distinction AGENTS.md §"Im(q) at fibre vs
observable level" draws:

- ❌ a REAL formula `c_3 = f(q_real)` matching multiple anchors — known
  to fail; **this probe is the explicit numerical demonstration for the
  `[3]_q/25` form**.
- ✓ a FIBRE Habiro element `F(q)` whose archimedean evaluation at *each*
  q₀ reproduces the `c_3` at *that* anchor — a different (complex-
  analytic / root-of-unity) object.

## Consequences

1. **Production tier unchanged.** `c_3` stays `cal-anchored`; the
   `[3]_q/25` closure stays NEAR-MATCH. This probe *confirms* that
   labelling rather than promoting it — the right Δ_λ-gate outcome.

2. **The headline `[3]_q/25` finding is real but bounded.** It is a
   clean proton-anchor structural near-match shared between m_μ V9 and
   Q_β c_3 (PR #1781). It is NOT a universal real-q fibre element. Both
   statements are true and should be stated together.

3. **Redirect for the fibre-level Composite 4 search.** Do NOT invest
   the `pyhecke` linear-combination `tr_M` infrastructure in chasing
   real-q forms. The genuine Habiro element (if one exists) must be
   **complex-analytic / evaluated at roots of unity** — the fibre level
   proper, where `c_3` is a Habiro-ring element, not a real number. The
   archimedean Composite 4 probe (PR #1795) already pointed here; this
   probe nails it quantitatively.

4. **m_μ V9 likely inherits the same status.** The m_μ closure uses the
   same `[3]_q/25` building block; a parallel cross-anchor test on the
   m_μ R9+V9 closure is the natural follow-up (though the m_μ anchor
   structure differs — m_e is the CAL-1 anchor, q₀-independent, so the
   m_μ swing analysis needs its own setup).

## Cross-refs

- m_μ V9 + Q_β c_3 closures: PR #1781
- `[3]_q/25` universal-template audit: [`2026-06-03-l2-closure-habiro-3-q-25-universal-template.md`](2026-06-03-l2-closure-habiro-3-q-25-universal-template.md)
- residue-A acceptance: [`2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md`](2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md)
- Composite 4 archimedean dead-end + fibre redirect: `qbeta/qbeta_composite4_wenzl_qpochhammer_first_probe.py` (PR #1795)
- prior cross-anchor infra: `probes/qbeta_li2q_spectral_combiner_crossanchor_probe.py` (PR #1609)
- AGENTS.md §"Critical framing — Im(q) at fibre vs observable level"
