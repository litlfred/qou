# Yekutieli per-cell α_em weight derivation — NEGATIVE

**Date:** 2026-06-13
**Branch:** `claude/research-yekutieli-mp-derivation-2026-06-13`
**Related PR:** None yet
**Triggered by:** `docs/audits/2026-06-01-yekutieli-mp-substrate-derivation-scaffolding.md` (Session A)

## Goal

Session A of the Yekutieli substrate-derivation of $m_p$: derive the $\alpha_{em}/\pi$ factor as the per-cell coupling weight of one of the 8 ideal octahedra under the $q$-deformed Yekutieli connection $\tau_q$. This probe acts as a checkpoint for the Bring-zero-mode analog assumption.

## Methodology

Implemented the Reading-A geometrised scaffold (from PR #1628). The non-abelian multiplicative integration of the curvature 2-form over the surviving ideal octahedron yields a coupling weight. According to the Bring-zero-mode analog hypothesis, this weight should match the $\alpha_{em}/\pi$ factor needed to resolve the 54 ppb residual.

The probe (`yekutieli_per_cell_alpha_em_derivation_probe.py`) computes this weight exactly: the pure geometric extraction gives $G$ (Catalan's constant) at $h^2$ order, stemming from the $[ \alpha, \beta ] = \pm 1$ commutator structure. The hypothesized target was $\alpha_{em}/\pi \approx 0.00232$.

## Results (Pre-stated failure signature hit)

- **Computed weight:** $\approx 0.915965$ ($G$)
- **Target weight:** $\approx 0.002322$ ($\alpha_{em}/\pi$)
- **Ratio:** $\approx 394.33$

The probe hit the pre-stated failure signature precisely: the per-cell weight comes out as a rational times $G$ (specifically, exactly $1 \cdot G$) without any $\alpha_{em}$ factor.

## Implications

The result is **NEGATIVE**. This establishes that $\alpha_{em}$ is **NOT** the direct per-cell coupling extracted by the standard $\tau_q$ connection integration over the ideal-octahedron tessellation. The $\alpha_{em}/\pi$ contribution requires a different categorical input.

Following the scaffold's anti-pattern guards, we must reconsider the Bring-zero-mode analog assumption's direct injection into the per-cell volume. The categorical structure likely requires deferring to the co-simplicial crossed-groupoid (`prop:cosimplicial-crossed-groupoid`) or Yekutieli triple structure, rather than a simplistic scalar weighting on the base tessellation.

## Deliverables
- **Probe script:** `folio-assistant/computations/yekutieli_per_cell_alpha_em_derivation_probe.py`
- **Witness:** `folio-assistant/computations/yekutieli-per-cell-alpha-em-derivation-probe.witness.json`
