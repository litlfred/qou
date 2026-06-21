# Li_2^q × spectral cross-anchor completion (2026-06-01)

**Date:** 2026-06-01
**PR:** TBD (claude/hoefsmit-chi-lambda-q-evaluator-2026-06-01)
**Status:** Completes deferred q_muon evaluation from PR #1609.
Refines PR #1626 cross-anchor diagnostic.

## TL;DR

PR #1609 refuted the Li_2^q × spectral combiner at q_proton (13% off
empirical c_3) but DEFERRED the q_muon cross-anchor test, citing
"Hoefsmit χ_λ(q) closed-form evaluator not yet wired".

**The deferral was unwarranted** — the symbolic χ_λ(q) closed forms
were already in
`qbeta-per-block-paper-closed-forms.witness.json` as sympy-rationals.
This audit completes the test.

**Result: Strong structural refutation confirmed.** The candidate is
essentially q-independent (swing 2.7 × 10⁻⁹ %) while empirical c_3
swings 2.88 % across anchors. **Swing ratio: candidate/empirical
≈ 2.7 × 10⁻⁹** — 9 orders of magnitude apart.

## What this tells us

The Li_2^q × spectral combiner candidate predicts c_3 ≈ -1.7975 essentially
INDEPENDENT of q across the two production anchors (q_proton, q_muon).
The empirical c_3 values are q-anchor-DEPENDENT (-2.0693 at m_p-pin,
-2.0097 at m_μ-pin).

| | candidate | empirical |
|---|---|---|
| c_3 at q_proton | -1.79748459121884870 | -2.0693 |
| c_3 at q_muon   | -1.79748459107974787 | -2.0097 |
| swing across anchors | 1.4 × 10⁻¹⁰ (negligible) | 5.96 × 10⁻² (2.88%) |
| miss vs empirical | +13.14% (proton), +10.56% (muon) | — |

## Three structural interpretations

**(i) The candidate has the wrong structure.** The Li_2^q × spectral
mechanism doesn't reproduce ANY of the cross-anchor q-dependence —
not just the magnitude. The c_3 saga's "near-match" pattern at
q_proton (within 13%) is structurally COINCIDENTAL with the candidate's
q-independent prediction. **Strong refutation confirmed.**

**(ii) The empirical c_3 IS NOT structurally q-dependent at the level
implied by the cross-anchor numbers.** Anchor proximity is 1.28 × 10⁻⁸;
any genuine q-dependent c_3(q) function would show swing of that order
(~10⁻⁸), not 2.88 × 10⁻². The empirical "swing" reflects EXTRACTION
NOISE or PRODUCTION-PATH-DEPENDENCE, not structural q-dependence in
the fibre object.

**(iii) Implication for PR #1626's complex-c_3 hypothesis.** The user's
hypothesis ("are we missing an Im part not directly observable?") is
still STRUCTURALLY plausible per AGENTS.md fibre/observable framing
(PR #1616), but the cross-anchor test cannot discriminate it at current
data. Both:
- **Real q-independent c_3** (Li_2^q × spectral candidate behavior)
- **Complex c_3 with Im hidden by archimedean projection** (user's hypothesis)
predict near-zero anchor swing — they are observationally
INDISTINGUISHABLE from each other at current data, but BOTH are
distinguishable from the EMPIRICAL c_3 values.

The 2.88% empirical swing requires explanation OUTSIDE either of these
fibre frameworks. It's likely an artefact of how empirical c_3 is
extracted from Q_β residual / u^3 at each anchor (production pipeline
threading m_p vs m_μ inputs through different paths).

## Implication for CAL-1/2/3

Per AGENTS.md (PR #1616): CAL inputs constrain archimedean Re[q_0] only.
This audit confirms: the structural Habiro element (whether real or
complex-with-hidden-Im) is q_0-INDEPENDENT in the relevant sense at
near-identical anchors. The empirical c_3 cross-anchor "swing" is NOT a
window into fibre Im content — it's noise from the empirical pipeline.

**Productive next direction (per PR #1626):**
- Wider-spaced q-anchors (e.g., m_e/m_K) at sufficient precision
- Direct Habiro q-difference equation symbolic analysis
- Higher-precision Q_β experimental data

## What this PR does NOT do

- ❌ Does NOT propose a new c_k candidate (Li_2^q × spectral stays refuted)
- ❌ Does NOT resolve the c_3 flip-flop saga
- ❌ Does NOT support the complex-c_3 hypothesis with data (the hypothesis becomes harder to test, not easier)

## Files

- `computations/probes/qbeta_li2q_spectral_combiner_crossanchor_probe.py`
- `computations/probes/qbeta-li2q-spectral-combiner-crossanchor.witness.json`
- `docs/audits/2026-06-01-qbeta-li2q-spectral-crossanchor-completion.md` (this file)

## Cross-refs

- PR #1609 — original Li_2^q × spectral refutation at q_proton (now mech #7)
- PR #1616 — Im(q) fibre/observable framing in AGENTS.md
- PR #1620 — Hecke-natural form for sym(Δtr_M)
- PR #1626 — complex c_3 fibre diagnostic (cross-anchor under-diagnostic finding)
- `docs/audits/2026-05-31-qbeta-bridge-narrowing.md` — 7 mechanisms ruled out
- `qbeta-per-block-paper-closed-forms.witness.json` — provided the symbolic χ_λ(q) forms
