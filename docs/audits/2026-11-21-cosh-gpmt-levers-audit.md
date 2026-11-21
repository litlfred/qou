# Audit: the cosh and GPMT levers of the pdix → cds1 bridge probe

Date: 2026-11-21. Beans `qou-cds1`, `qou-pdix`. Issue #8793, PR #8794.
Subject: `computations/qbeta/qbeta_pdix_cds1_cosh_gpmt_bridge_probe.py`
(owner commit `48f446490c`). Its witness is left unchanged.
Probe: `computations/qbeta/qbeta_cosh_gpmt_levers_on_v3_audit_probe.py` (6/6).

## Summary

Neither lever closes the Q_β gap on the base the dashboard scores today, the
γγ V³ base (0.325433928735 MeV, conditional on C1-C3). Both reported
near-closures are on census words, and on those words each lever was picked
from a menu of options by its residual.

| lever | on the bridge probe's cell | on V³ (scored) |
|---|---|---|
| A, as written: base·cosh(6 ln q) | nuc11: 0.7838 MeV, F = 0.998 | 0.3913 MeV, F = **1.999** |
| A, full twist inserted into the trace | nuc11: ×1.7427 → about 1.136 MeV, **+45 %** | 0.4200 MeV, F = **1.863** |
| B, GPMT (1³) term | nuc11_gen_grouped: +0.53 % | **0**: no (1³) block exists |

## Lever A: the cosh factor is not what the full twist does

Δ² = (σ₁σ₂σ₁)² is central in H₃(q), so it multiplies each block's character by
a scalar: q⁶ on (3), 1 on (2,1), q⁻⁶ on (1³). The bridge probe instead
multiplies the whole trace by (q⁶ + q⁻⁶)/2. That mixes in the (1³) eigenvalue,
but under convention D the (1³) block has weight w₍₁³₎(z_D) = 0, and the (2,1)
block, which does carry weight, has eigenvalue 1. On the probe's own nuc11
cell, actually inserting the twist multiplies the base by 1.7427, not by
cosh 6u = 1.2025, which overshoots CODATA by about 45 %. On V³ the weight
spaces carry only (3) ⊕ (2,1): the Δ² spectrum is {q⁶, 1, 1}, which the probe
asserts.

The value k = 6 is chosen from the table k ∈ {0, 1, 2, 3, 6}, and only k = 6
crosses F = 1. Calling the factor a "6-crossing core length" match is a reading
offered after the fact, not a derivation. Under §NO FITTING this is selection
against the target.

## Lever B: there is no (1³) block for GPMT to restore on V³

GPMT adds d_D(S^(1³))·χ₍₁³₎ in one of two signs. The modified dimension is
negative, d = −1/([2][3]). The "GPMT+" branch flips that sign to +|d|, and of
the 2 signs × 4 words × 2 E₀ forms, only GPMT+ on `nuc11_gen_grouped` lands
near CODATA. On the V³ weight-space trace the 3-dimensional weight spaces
contain no (1³) summand at all, so the correction is zero by construction.

## Scope

These are scope-(a) negatives: they are about these levers as constructed,
not about Δ² or GPMT traces in general. The census words `nuc11_*` were
rejected by the 2026-09-13 whole-element SDP ruling and replaced by V³.
Nothing in this audit changes a witness or the dashboard.

## Also found (not changed)

The dashboard's Q_β row has `source_witness` text that still says
"c_2 = -1 PROVED". Per AGENTS.md the defensible word is "structural". That text
is written by `per_observable_100x_status.py`, so fixing it means re-running
the dashboard producer. It is left for a separate change.
