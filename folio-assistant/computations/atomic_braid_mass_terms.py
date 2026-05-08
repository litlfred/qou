"""Shared utilities for the atomic-braid mass-table family of scripts.

Per Gemini PR #548 medium-priority feedback (consolidate `t4_raw`,
`t6_canonical_MeV` previously duplicated between
`atomic_braid_mass_table.py` and `atomic_braid_mass_table_modes_sweep.py`).

All routines preserve the 50-dps precision floor set by the caller's
`mp.mp.dps = 50`; computations use mpmath end-to-end (no SymPy →
mpmath casts).

Dimensionality conventions:
  * Hecke-unit terms (T1, T2, T3, T4) are returned in cat units —
    they get scaled by E_0 (MeV/cat-unit) at the assembly site.
  * T6 is returned in MeV directly; **do not** multiply by E_0 again
    at the assembly site.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from schur_weyl_symbolic import partitions_of, hook_lengths

HERE = Path(__file__).parent


def t4_raw(A: int, q0_mp: mp.mpf) -> mp.mpf:
    """Term 4 in cat units (without `m_e` scaling): τ(C_dim_q).

    Returns Σ_{λ ⊢ 3A} 1/dim_q(λ) at q = q0_mp.  Caller scales by
    `m_e_hecke` to get the full Term 4 contribution.

    All arithmetic in mpmath; q-factorial computed by direct product
    `[n]_q! = ∏_{k=1..n} (q^k − q^{−k}) / (q − q^{−1})` to preserve
    precision.
    """
    if A < 1:
        return mp.mpf(0)
    n = 3 * A
    denom = q0_mp - 1 / q0_mp
    nfac_val = mp.mpf(1)
    for k in range(1, n + 1):
        nfac_val *= (q0_mp ** k - 1 / q0_mp ** k) / denom
    total = mp.mpf(0)
    for lam in partitions_of(n):
        dim_q = nfac_val
        for h in hook_lengths(lam):
            qh = (q0_mp ** h - 1 / q0_mp ** h) / denom
            dim_q = dim_q / qh
        total += 1 / dim_q
    return total


def t6_canonical_MeV(A: int) -> mp.mpf:
    """Canonical T6 cyclotomic residue tail in **MeV** (per-A from
    Habiro witness `term6-habiro-residue-mpfr-50dps.witness.json`).

    The result is in MeV directly — the assembly site adds it to
    `E_0 · total_hecke` without further E_0 scaling.

    AUDIT FLAG (added 2026-05-08, see AUDIT-DEEP-2026-05.md §3.3a):
    -----------------------------------------------------------------
    The Habiro witness file `term6-habiro-residue-mpfr-50dps.witness.json`
    does NOT exist on the current branch.  This function therefore
    silently returns 0 for every A, meaning T6 contributes zero to
    every mass prediction in the current `atomic_braid_mass_table.py`
    pipeline.

    The canonical Markov-peel witness `term6-residues-at-roots.witness.json`
    DOES exist and emits per-atom values
    `data.results[].term6_at_q0_real` (dimensionless tr_M units, not
    MeV).  Wiring it requires resolving a unit-convention question
    (cat-unit additive into `total_hecke` vs MeV-scaled separately)
    and the apparent magnitude mismatch (canonical values are
    O(10⁶) for ⁴He and would dominate the mass formula if added
    raw).  See AUDIT-DEEP-2026-05.md §3.3a / §7 P4′.  Until the
    convention is confirmed by the repo owner, this function is
    LEFT in its silently-zero state — making the gap explicit
    rather than fabricating values.

    Missing witness or missing-A → returns 0 MeV.
    """
    path = HERE / "term6-habiro-residue-mpfr-50dps.witness.json"
    if not path.exists():
        # Silently zero — see AUDIT FLAG above.  Once the unit
        # convention is confirmed, this branch should consume
        # `term6-residues-at-roots.witness.json` instead.
        return mp.mpf(0)
    try:
        d = json.loads(path.read_text())
    except json.JSONDecodeError:
        return mp.mpf(0)
    for r in d.get("results_by_atom", []):
        try:
            entry_A = int(r["atom"].split("=")[1])
            if entry_A == A:
                return mp.mpf(r["term6_b_pred_mev_50dps"])
        except (KeyError, IndexError, ValueError):
            continue
    return mp.mpf(0)
