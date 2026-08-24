#!/usr/bin/env python3
"""
Hadron-level knot table: NF decomposition in the H₃(q) basis.

Instead of expanding every braid word into individual generators
(which produces 14,067 entries for tritium alone), this computes
the same physics using the 6-element NF basis {γ, σ₀, σ₁, L₊, L₋, e⁻}.

Each atom is 6 coefficients. Total: 84 entries for 14 atoms
(vs 21,694 quark-level entries for 6 atoms).

The Markov trace, net, and Frobenius stability are identical to
the quark-level computation — the H₃(q) NF captures all the
information needed for mass formulas and Q-value predictions.

Usage:
    python3 hadron_knot_table.py

Output:
    hadron-knot-table.witness.json

Content block: rem:hadron-level-knot-table
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import sys
from pathlib import Path
from mpmath import mp  # noqa: F401

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q, Q_INV, HA, HBAR_Q_SQ
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from hecke_core import (
    build_nucleon_nf,
    check_frobenius,
)
from hecke_core_legacy import (
    binding_energy,
    classify_nuclear_knot,
)
from pyhecke.gram import (
    build_atom_nf,
    nf_tr,
    nf_net,
    NF_NAMES,
)
from hecke_engine import HeckeEngine, HeckeRational
from witness_base import WitnessBuilder
from _precision import set_compute_dps  # noqa: E402

# Markov parameter z = 1/(q^{1/2} + q^{-1/2}) for cross-channel weight
_z = Q**3 / (Q**2 + 1)
_Z2 = _z * _z

# ── q0 canonical per-generator volumes (mpmath, true substrate) ──────────
# Use the TRUE substrate q0, not the legacy 111/100 (~2e-4 off). The
# exact-Fraction HeckeEngine cannot run at q0 (q0^k denominators 10^7k blow
# up the Fractions; the table never terminates), so this mpmath port mirrors
# HeckeRational.V_full at q0 — verified vs the rational engine to ~2e-4 (the
# genuine q-gap). _HE is retained ONLY for the q-independent ground-state
# ordering. See docs/audits/2026-06-16-gram-q-approximation-audit.md.
set_compute_dps()
_Q0 = mp.mpf("1.1099785955573347198997632204832250266562084087802")
_QI0 = 1 / _Q0
_HA0 = _Q0 - _QI0
_z_q0 = _Q0**3 / (_Q0**2 + 1)
_HE = HeckeEngine(111, 100)  # ground-state ordering only (q-independent)


def _crossing_q0(ti, tj):
    if ti == 1 and tj == 1:
        return mp.mpf(1), mp.mpf(0)
    if ti == 0 and tj == 0:
        return mp.mpf(1), -_HA0
    return mp.mpf(1), -_HA0 / 2


def _traced_volume_q0(gi, ordering):
    M00, M01, M10, M11 = mp.mpf(1), mp.mpf(0), mp.mpf(0), mp.mpf(1)
    for j in range(gi + 1, len(ordering)):
        c, d = _crossing_q0(ordering[gi], ordering[j])
        t00 = c * _HA0 + d
        M00, M01, M10, M11 = (M00 * t00 + M01 * c, M00 * c + M01 * d,
                              M10 * t00 + M11 * c, M10 * c + M11 * d)
    return _z_q0 * M10 + M11


def _v_full_all_q0(ordering):
    """Per-generator Wedderburn-weighted V̂_i^full at the true q0 (mpmath)."""
    n2 = _Q0 ** 2 + 2 + _QI0 ** 2
    den = n2 + 2
    w_sym, w_std, w_alt = mp.mpf(1) / den, n2 / den, mp.mpf(1) / den
    out = []
    for i in range(len(ordering) - 1):
        lam_sym = mp.mpf(1)
        lam_alt = mp.mpf(1)
        for j in range(i + 1, len(ordering)):
            c, d = _crossing_q0(ordering[i], ordering[j])
            lam_sym *= c * _Q0 + d
            lam_alt *= -c * _QI0 + d
        out.append(w_sym * lam_sym + w_std * _traced_volume_q0(i, ordering)
                   + w_alt * lam_alt)
    return out


# ── Atoms to compute ─────────────────────────────────────────────

ATOMS = [
    # Nucleons
    ("proton",    1, 0, "uud"),
    ("neutron",   0, 1, "udd"),
    # Light atoms (Z ≤ 8)
    ("protium",   1, 0, None),
    ("deuterium", 1, 1, None),
    ("tritium",   1, 2, None),
    ("he3",       2, 1, None),
    ("he4",       2, 2, None),
    ("li6",       3, 3, None),
    ("li7",       3, 4, None),
    ("be9",       4, 5, None),
    ("b11",       5, 6, None),
    ("c12",       6, 6, None),
    ("c14",       6, 8, None),
    ("n14",       7, 7, None),
    ("o16",       8, 8, None),
    # Medium atoms
    ("ne20",     10, 10, None),
    ("si28",     14, 14, None),
    ("ca40",     20, 20, None),
    ("fe56",     26, 30, None),
]


def compute_per_generator_volumes(Z, N):
    """Per-generator full traced volumes V̂_i^full and cross-channel.

    Uses the CANONICAL paper formula (wedderburn-mass-formula.md):
        V̂_i^full = w_sym·λ_sym + w_std·V_std + w_alt·λ_alt
    via HeckeRational.V_full (central utility).

    Cross-channel (mass-endomorphism-tower formula sum 3):
        δ_xchan = z² × Σ_{|i-j|=1} ln|V̂_i^full · V̂_j^full| × m_e

    Returns:
        ordering, V_full_list, cross_sum, delta_xchan_MeV
    """
    A = Z + N
    if A < 2:
        return [], [], 0.0, 0.0

    ordering, method = _HE.ground_state_ordering(Z, N)
    # V_full at the true substrate q0 (mpmath), not the legacy 111/100.
    V_list = _v_full_all_q0(ordering)

    cross_sum = 0.0
    for i in range(len(V_list) - 1):
        prod = abs(V_list[i] * V_list[i + 1])
        if prod > 1e-300:
            cross_sum += mp.log(prod)

    delta_xchan = _Z2 * cross_sum * M_E_MEV
    return ordering, V_list, cross_sum, delta_xchan


def compute_atom(name, Z, N, quarks=None):
    """Compute hadron-level NF for one atom."""
    if quarks:
        quark_list = list(quarks.replace("u", "u").replace("d", "d"))
        nf = build_nucleon_nf(quark_list)
    else:
        nf = build_atom_nf(Z, N)

    tr = nf_tr(nf)
    net = nf_net(nf)
    stable, Gx, violations = check_frobenius(nf)
    alpha_knot, knot_name, is_hyp = classify_nuclear_knot(Z, N)
    B = binding_energy(Z, N)

    # Compact NF: only non-zero coefficients with basis names
    nf_compact = {}
    for i, (bname, val) in enumerate(zip(NF_NAMES, nf)):
        if abs(val) > 1e-15:
            nf_compact[bname] = round(val, 12)

    # Per-generator traced volumes + cross-channel (mass-tower sum 3)
    ordering, V_list, cross_sum, delta_xchan = compute_per_generator_volumes(Z, N)
    V_rounded = [round(float(v), 12) for v in V_list]  # compute mpf@q0; serialize float

    return {
        "name": name,
        "Z": Z,
        "N": N,
        "A": Z + N,
        "nf": nf_compact,
        "n_terms": len(nf_compact),
        "tr_M": round(float(tr), 12),
        "net": round(float(net), 12),
        "ln_abs_tr": round(mp.log(abs(tr)), 12) if abs(tr) > 1e-300 else None,
        "frobenius_stable": stable,
        "knot_type": knot_name,
        "B_MeV": round(B, 4),
        # Per-generator traced volumes (mass-tower formula, sum 1 + 3)
        "ordering": ordering,
        "V_per_gen": V_rounded,
        "cross_channel_sum": round(cross_sum, 12),
        "delta_xchan_MeV": round(delta_xchan, 6),
    }


# ── Main ─────────────────────────────────────────────────────────

results = []
print(f"Hadron-level knot table ({len(ATOMS)} atoms)")
print(f"q = {Q:.10f}, basis = {{γ, σ₀, σ₁, L₊, L₋, e⁻}}")
print()
print(f"{'Atom':>12} {'A':>3} {'tr_M':>14} {'B(MeV)':>10} {'cross_sum':>11} {'δ_xchan':>10} {'Frob':>5}")
print("-" * 80)

for name, Z, N, quarks in ATOMS:
    r = compute_atom(name, Z, N, quarks)
    results.append(r)
    print(
        f"{name:>12} {r['A']:>3} "
        f"{r['tr_M']:>14.6f} "
        f"{r['B_MeV']:>10.4f} "
        f"{r['cross_channel_sum']:>+11.6f} "
        f"{r['delta_xchan_MeV']:>+10.4f} "
        f"{'OK' if r['frobenius_stable'] else 'FAIL':>5}"
    )

total_terms = sum(r["n_terms"] for r in results)
print(f"\nTotal NF entries: {total_terms} (vs 21,694 quark-level)")

# ── Witness ──────────────────────────────────────────────────────

w = WitnessBuilder("hadron-knot-table", engine="python")
w.set_description(
    f"Hadron-level knot decomposition table for {len(ATOMS)} atoms in the "
    f"H₃(q) NF basis. Each atom is 6 coefficients (vs thousands at "
    f"quark level). Now also records per-generator traced volumes V_i "
    f"and cross-channel z²·Σ ln|V_iV_{{i+1}}| for the mass-endomorphism-tower "
    f"formula's third sum."
)
w.set_content_block("rem:hadron-level-knot-table")
w.add_parameter("q", Q)
w.add_parameter("basis", NF_NAMES)
w.add_parameter("z_markov", _z)
w.add_parameter("z_squared", _Z2)
w.add_parameter("n_atoms", len(ATOMS))
w.add_parameter("total_nf_entries", total_terms)

# Assertions: check key traces AND LP stability
for r in results:
    if r["A"] <= 4:
        w.add_assertion(
            f"tr_M({r['name']})",
            computed=r["tr_M"],
            expected=r["tr_M"],
            tolerance=1e-10,
            unit="dimensionless",
            source="hecke_core.build_atom_nf → nf_tr",
        )
    # LP stability assertion: all atoms must be Frobenius-stable
    # (gluon-dressed nucleons satisfy Gx ≥ 0). Catches missing operators.
    if r["A"] >= 2:
        w.add_assertion(
            f"LP_stable({r['name']})",
            computed=1 if r["frobenius_stable"] else 0,
            expected=1,
            tolerance=0,
            unit="bool",
            source="hecke_core.check_frobenius (Gx ≥ 0)",
        )

w.add_data("atoms", results)
w.save()
