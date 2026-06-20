"""Shared utilities for the h⁴-residual structural-derivation hunt (PR #1629).

Centralizes the three substrate utility functions used by both
`h4_form_AB_cross_anchor_stability.py` and
`h4_residual_higher_precision_pslq.py` per Gemini review on PR #1629.

The CODATA constants are re-exported from the canonical
`codata_2022_source` registry (M_E_MEV, M_MU_MEV, M_P_MEV); ALPHA_EM
is currently NOT in the central registry and is defined here as a
single source of truth pending a separate cleanup PR.

## Cross-references

- merged PR #1617 ocneanu_54ppb_residual_exploration.py (the f-target)
- coord ledger 2026-06-01-h4-residual-derivation.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import mpmath as mp

# Acknowledged-anchor constants from the central registries
# (consistent with repo convention; see AGENTS.md §Acknowledged-anchor
# banner). Masses use the mpf-typed codata_2022_source registry (more
# recent CODATA 2022 values + includes muon). α_em uses
# experimental_constants.ALPHA_EM_INV (which has the canonical CODATA
# 2018 fine-structure constant; experimental_constants lacks muon).
from codata_2022_source import M_E_MEV, M_MU_MEV, M_P_MEV  # noqa: F401
import experimental_constants as _ec  # noqa: E402

ALPHA_EM = mp.mpf(1) / mp.mpf(repr(_ec.ALPHA_EM_INV))


def trM_borromean_closed(q):
    """Lean-proved closed form: tr_M(β_Bor, q) = (4+h²−3h⁴−h⁶)/(h²+4)."""
    h = q - 1 / q
    h2 = h * h
    return (4 + h2 - 3 * h2 ** 2 - h2 ** 3) / (h2 + 4)


def qint(k, q):
    """q-integer [k]_q = (q^k − q^(−k)) / (q − q^(−1))."""
    return (q ** k - q ** (-k)) / (q - 1 / q)


def qfact(k, q):
    """q-factorial [k]_q! = Π_{i=1}^k [i]_q."""
    out = mp.mpf(1)
    for i in range(1, k + 1):
        out *= qint(i, q)
    return out
