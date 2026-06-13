# Yekutieli per-cell 1/dim H_3 normalisation — NEGATIVE

**Date:** 2026-06-13
**Branch:** `claude/research-yekutieli-mp-derivation-2026-06-13`
**Related PR:** None yet
**Triggered by:** `docs/audits/2026-06-01-yekutieli-mp-substrate-derivation-scaffolding.md` (Session B)

## Goal

Session B of the Yekutieli substrate-derivation of $m_p$: derive the $1/\dim H_3 = 1/6$ factor as the per-cell normalisation under the half-symmetric projection $\Pi_{HS}$ by attempting to use a Kashiwara-crystal projection (rather than the natural conjugation involution that was refuted previously).

## Methodology

Evaluated the normalisation factors dynamically via Kashiwara-crystal weights ($c_\lambda(q)$ via Macdonald hook-content). The test sought to extract exactly $1/6$ at $q_0$, avoiding the $1/14$ Wedderburn-block-weighted form that emerges from $H_4$ self-conjugate sums ($\sum d^2$).

## Results (Pre-stated failure signature hit)

The computed factor tied back precisely to the Wedderburn-block weighted sums ($\sum d^2$) form at the $q \to 1$ limit (approaching 14 for $H_4$ self-conjugate, or 6 for $H_3$). This matches the pre-stated failure signature defined in the scaffolding:

> Pre-stated failure signature: factor comes out as 1/Σ d² = 1/14 or some other Wedderburn-block-weighted form ⟹ the (α_em/π)/dim H_3 factor is correct numerically but NOT a per-cell Yekutieli structure.

## Implications

The result is **NEGATIVE**. While the value $1/6$ holds numerically, it originates as a purely Wedderburn-block-weighted term rather than emerging structurally as a true per-cell Yekutieli normalisation.

Together with the Session A negative result, this establishes that the 54 ppb residual correction $( \alpha_{em}/\pi ) / \dim H_3$ cannot be integrated via standard, simple injections into the ideal octahedron per-cell coupling/normalisation. The derivation requires deeper categorical machinery—such as co-simplicial crossed groupoids—bypassing the simplistic Yekutieli structural guesses.

## Deliverables
- **Probe script:** `folio-assistant/computations/yekutieli_per_cell_dim_h3_normalisation_probe.py`
- **Witness:** `folio-assistant/computations/yekutieli-per-cell-dim-h3-normalisation-probe.witness.json`
