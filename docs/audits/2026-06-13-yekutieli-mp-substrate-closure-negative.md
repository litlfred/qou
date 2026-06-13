# Yekutieli substrate closure + cross-anchor verification — NEGATIVE

**Date:** 2026-06-13
**Branch:** `claude/research-yekutieli-mp-derivation-2026-06-13`
**Related PR:** None yet
**Triggered by:** `docs/audits/2026-06-01-yekutieli-mp-substrate-derivation-scaffolding.md` (Session C)

## Goal

Session C of the Yekutieli substrate-derivation of $m_p$: stitch Sessions A + B into a closed-form per-cell contribution, verify the sum over the 8 octahedra reproduces the 54 ppb correction, and check cross-anchor stability at both $q_{proton}$ and $q_{muon}$.

## Methodology

The probe evaluates the required structural term $k_{req}$ at both substrate anchors (proton and muon). The target correction was hypothesized to be $8 \times (\alpha_{em}/\pi)/6 = \frac{4}{3} (\alpha_{em}/\pi)$ based on the Session A + B synthesis attempt. We checked if the derived formula maintained exact stability across both anchors.

## Results (Pre-stated failure signature hit)

- **$k_{req}(q_{proton})$:** exactly 12.0000000
- **$k_{req}(q_{muon})$:** 11.9995553
- **Expected offset:** $\approx 0.000387$ ($(\alpha_{em}/\pi)/6$) vs actual gap at muon $\approx 0.000444$

The probe hit the pre-stated failure signature perfectly: the derivation closes (or near-closes) at $q_{proton}$ but fails to maintain the correct residual at $q_{muon}$. 

## Implications

The result is **NEGATIVE**. This confirms that stitching simple per-cell terms (like the Kashiwara-crystal weight or Bring-zero-mode analog) does not yield cross-anchor structural invariants. 

As predicted in the scaffold guards, the divergence at the muon anchor indicates that a fibre-level Habiro element is required (mirroring the parallel $\alpha_{EM}$ PR #1511 pattern). The structural derivation of the 54 ppb $m_p$ correction cannot rely on flat Yekutieli cell integration; it MUST incorporate the full co-simplicial crossed-groupoid structure and the Habiro elements that provide anchor-independent closures.

## Deliverables
- **Probe script:** `folio-assistant/computations/yekutieli_mp_substrate_closure_probe.py`
- **Witness:** `folio-assistant/computations/yekutieli-mp-substrate-closure-probe.witness.json`
