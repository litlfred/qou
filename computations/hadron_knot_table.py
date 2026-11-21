#!/usr/bin/env python3
"""
Hadron-level knot table: NF decomposition in the H₃(q) basis.

Instead of expanding every braid word into individual generators
(which produces 14,067 entries for tritium alone), this computes
the same physics using the 6-element NF basis {γ, σ₀, σ₁, L₊, L₋, e⁻}.

Each atom is 6 coefficients. Total: 84 entries for 14 atoms
(vs 21,694 quark-level entries for 6 atoms).

The H₃(q) NF Markov trace (`nf_tr`), net (`nf_net`), and Frobenius
stability (`check_frobenius`) are exact within the 6-dimensional H₃(q)
quotient produced by `build_atom_nf` (which projects strand generators
modulo 2 onto {σ₀, σ₁}). Note (bean `qou-zgg2`): for compound nuclei
(A ≥ 2), this H₃-projected pairing is distinct from the full-tower
H_{3A}(q) canonical atomic trace (`tr_m_atom_via_transfer.tr_m_atom_zn`
/ `markov_peel.tr_M_atomic`).

Usage:
    python3 hadron_knot_table.py

Output:
    hadron-knot-table.witness.json

Content block: rem:hadron-level-knot-table
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path
from mpmath import mp  # noqa: F401

sys.path.insert(0, str(Path(__file__).parent))

from experimental_constants import M_E_MEV
from hecke_core import (
    build_nucleon_nf,
)
from pyhecke.atom import (
    build_atom_nf_mp,
    build_nucleon_nf_mp,
    check_frobenius_mp,
)
from hecke_core_legacy import (
    binding_energy,
    classify_nuclear_knot,
)
from pyhecke.gram import (
    build_atom_nf,
    tr_m_mp,
    NF_NAMES,
)
from hecke_engine import HeckeEngine, HeckeRational
from witness_base import WitnessBuilder
from _precision import set_compute_dps, fmt  # noqa: E402


# ── q0 canonical per-generator volumes (mpmath, true substrate) ──────────
# Use the TRUE substrate q0, not the legacy 111/100 (~2e-4 off). The
# exact-Fraction HeckeEngine cannot run at q0 (q0^k denominators 10^7k blow
# up the Fractions; the table never terminates), so this mpmath port mirrors
# HeckeRational.V_full at q0 — verified vs the rational engine to ~2e-4 (the
# genuine q-gap). _HE is retained ONLY for the q-independent ground-state
# ordering. See docs/audits/2026-06-16-gram-q-approximation-audit.md.
set_compute_dps()
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
_Q0 = mp.mpf(Q_50_DIGIT_STR)
_QI0 = 1 / _Q0
_HA0 = _Q0 - _QI0
_z_q0 = _Q0**3 / (_Q0**2 + 1)
# Markov parameter z = q^3/(q^2+1) (convention D) for the cross-channel
# weight, at the 50-digit substrate q0. It was the float64 `Q**3/(Q**2+1)`.
_Z2 = _z_q0 * _z_q0
_TR_M_MP = tr_m_mp()
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



VHAT_WEIGHTS_LABEL = (
    "pre-convention-D mixture (q-Plancherel W_sym/W_std/W_alt), kept by owner "
    "ruling 2026-11-20 until the Phi_q pole (qou-2tuv) is resolved; "
    "convention-D z*a+b gives m_p/m_e = inf (PR #8590)"
)

def _v_full_all_q0(ordering):
    """Per-generator Wedderburn-weighted V̂_i^full at the true q0 (mpmath)."""
    # OWNER RULING 2026-11-20 (PR #8590): this V-hat deliberately keeps the
    # pre-convention-D W_sym/W_std/W_alt (q-Plancherel) mixture. The 11-18 ruling
    # moved pyhecke.atom to the convention-D Markov trace z*a+b, but here that puts
    # the proton V-hat (1.2824) past the Phi_q pole at q0 and m_p/m_e = inf
    # (qou-2tuv). Kept, labelled, until the pole is resolved. No number moves.
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

# Frozen roster the committed witness is expected to cover.  `_save_witness`
# compares `ATOMS` against this so that TRUNCATING `ATOMS` cannot produce a
# witness claiming `complete: true` — bean `qou-i7ju` warns in as many words
# that "truncating the ATOMS list would produce a different witness, not a
# regenerated one", and a coverage block keyed on `len(ATOMS)` alone would
# report a 2-atom run as complete.  Measured: it did, before this was added.
#
# THIS MUST BE A LITERAL, not `[a[0] for a in ATOMS]`.  Derived from `ATOMS` it
# is a comparison of a list to itself: truncating `ATOMS` truncates the
# "canonical" roster with it and the check passes vacuously.  That is the same
# self-comparison defect this file's own comment block records for the removed
# `tr_M` assertion (`computed=r["tr_M"], expected=r["tr_M"]`, bean `qou-26f2`),
# and the first version of this guard reproduced it — caught by testing the
# guard against a truncated copy rather than trusting it.
CANONICAL_ATOM_ROSTER = [
    "proton", "neutron", "protium", "deuterium", "tritium", "he3", "he4",
    "li6", "li7", "be9", "b11", "c12", "c14", "n14", "o16", "ne20",
    "si28", "ca40", "fe56",
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
        return [], [], mp.mpf(0), mp.mpf(0)

    ordering, method = _HE.ground_state_ordering(Z, N)
    # V_full at the true substrate q0 (mpmath), not the legacy 111/100.
    V_list = _v_full_all_q0(ordering)

    cross_sum = mp.mpf(0)
    for i in range(len(V_list) - 1):
        prod = abs(V_list[i] * V_list[i + 1])
        if prod > 1e-300:
            cross_sum += mp.log(prod)

    delta_xchan = _Z2 * cross_sum * M_E_MEV
    return ordering, V_list, cross_sum, delta_xchan


def compute_atom(name, Z, N, quarks=None):
    """Compute hadron-level NF for one atom, in mpmath end to end.

    The NF is built by the float64-free twins (`build_atom_nf_mp`,
    `build_nucleon_nf_mp`) at the 50-digit substrate q0; the trace, net and
    Frobenius check use the mpmath trace form. Every recorded number is an
    `mpf` serialized with `_precision.fmt`. The float64 builder is still run,
    only to assert that the two twins build the same braid word: they must
    agree to float64 resolution, or one of them has drifted (bean qou-1qsw).
    """
    if quarks:
        quark_list = list(quarks)
        nf = build_nucleon_nf_mp(quark_list)
        nf_f64 = build_nucleon_nf(quark_list)
    else:
        nf = build_atom_nf_mp(Z, N)
        nf_f64 = build_atom_nf(Z, N)
    scale = max(abs(c) for c in nf)
    twin_gap = max(abs(nf[i] - nf_f64[i]) for i in range(6)) / scale
    if twin_gap > mp.mpf("1e-10"):
        raise RuntimeError(
            f"{name}: mp and float64 NF builders disagree (rel {mp.nstr(twin_gap, 3)}); "
            "one twin has drifted from the other's braid word")

    tr = mp.fsum(nf[i] * _TR_M_MP[i] for i in range(6))
    net = mp.fsum(nf)
    stable, Gx, violations = check_frobenius_mp(nf)
    alpha_knot, knot_name, is_hyp = classify_nuclear_knot(Z, N)
    B = binding_energy(Z, N, as_mpf=True)

    # Compact NF: only non-zero coefficients with basis names
    nf_compact = {}
    for bname, val in zip(NF_NAMES, nf):
        if abs(val) > mp.mpf("1e-40") * scale:
            nf_compact[bname] = fmt(val)

    # Per-generator traced volumes + cross-channel (mass-tower sum 3)
    ordering, V_list, cross_sum, delta_xchan = compute_per_generator_volumes(Z, N)

    return {
        "name": name,
        "Z": Z,
        "N": N,
        "A": Z + N,
        "nf": nf_compact,
        "n_terms": len(nf_compact),
        "tr_M": fmt(tr),
        "net": fmt(net),
        "ln_abs_tr": fmt(mp.log(abs(tr))) if tr != 0 else None,
        "frobenius_stable": stable,
        "knot_type": knot_name,
        "B_MeV": fmt(B),
        # Per-generator traced volumes (mass-tower formula, sum 1 + 3)
        "ordering": ordering,
        "V_per_gen": [fmt(v) for v in V_list],
        "cross_channel_sum": fmt(cross_sum),
        "delta_xchan_MeV": fmt(delta_xchan),
        "_twin_gap": twin_gap,
    }


# ── Main ─────────────────────────────────────────────────────────

def _save_witness(results):
    """Write the witness from the atoms computed SO FAR.

    CHECKPOINTED (2026-09-05, bean `qou-i7ju` route 2).  This used to run
    once, after all 19 atoms — so a run that did not reach the end produced
    **nothing**, and since the table takes many hours (deuterium ~20 min,
    tritium ~26 min, and rising with A) no agent container could ever
    refresh it.  That is why `hadron-knot-table.witness.json` sat stale on
    `main`: not because the numbers were hard, but because partial progress
    was discarded.

    Calling this after every atom makes a bounded run refresh the rows it
    reached.  The cost is negligible against the per-atom compute.

    A partial witness is a DIFFERENT artifact from a complete one and is
    labelled as such: `coverage` records exactly which atoms are present and
    which are missing, and the description opens with PARTIAL/COMPLETE.  A
    reader — human or audit — can never mistake one for the other, and no
    assertion is made about an atom that was not computed.

    `coverage` records the ROSTER, not just a count, because "complete" here
    can only ever mean *reached the end of the configured `ATOMS`* — and this
    bean's own warning is that "truncating the `ATOMS` list would produce a
    different witness, not a regenerated one".  A truncated roster would
    otherwise report `complete: true` off two atoms.  Recording the names, and
    checking them against the canonical roster, makes that visible instead.
    """
    computed_names = [r["name"] for r in results]
    roster = [a[0] for a in ATOMS]
    missing = [n for n in roster if n not in computed_names]
    reached_end = len(results) == len(ATOMS)
    roster_is_canonical = roster == CANONICAL_ATOM_ROSTER
    # "complete" means the canonical table, not merely the configured one.
    complete = reached_end and roster_is_canonical
    total_terms = sum(r["n_terms"] for r in results)
    if complete:
        status = "COMPLETE"
    elif not roster_is_canonical:
        status = (f"NON-CANONICAL ROSTER — {len(results)}/{len(roster)} of a "
                  f"{len(roster)}-atom list, not the canonical "
                  f"{len(CANONICAL_ATOM_ROSTER)}")
    else:
        status = f"PARTIAL — {len(results)}/{len(ATOMS)} atoms"

    w = WitnessBuilder("hadron-knot-table", engine="python")
    w.set_description(
        f"[{status}] Hadron-level knot decomposition table in the H₃(q) NF "
        f"basis. Each atom is 6 coefficients (vs thousands at quark level). "
        f"Also records per-generator traced volumes V_i and cross-channel "
        f"z²·Σ ln|V_iV_{{i+1}}| for the mass-endomorphism-tower formula's "
        f"third sum."
        + ("" if complete else
           f" THIS IS A PARTIAL RUN: {len(missing)} atoms were not reached "
           f"and are absent from `atoms` — see `coverage`. Values present are "
           f"fully computed; nothing is extrapolated.")
    )
    w.set_content_block("rem:hadron-level-knot-table")
    w.add_parameter("q", fmt(_Q0))
    w.add_parameter("basis", NF_NAMES)
    w.add_parameter("vhat_weights", VHAT_WEIGHTS_LABEL)
    w.add_parameter("z_markov", fmt(_z_q0))
    w.add_parameter("z_squared", fmt(_Z2))
    w.add_parameter("n_atoms_expected", len(ATOMS))
    w.add_parameter("n_atoms_computed", len(results))
    w.add_parameter("total_nf_entries", total_terms)

    # Assertions: LP stability, over the computed atoms only.
    for r in results:
        w.add_assertion(
            f"mp_twin_matches_float64_builder({r['name']})",
            computed=1 if r["_twin_gap_ok"] else 0,
            expected=1,
            tolerance=0,
            unit="bool",
            source="build_atom_nf_mp / build_nucleon_nf_mp vs the float64 builder, rel gap <= 1e-10",
        )
        # The `tr_M(<atom>)` assertion that stood here read
        # `computed=r["tr_M"], expected=r["tr_M"]` under
        # `source="hecke_core.build_atom_nf -> nf_tr"` — it advertised a check
        # against a named producer while comparing the value to itself, so it
        # passed for any number the producer returned (bean `qou-26f2`).
        #
        # Removed rather than repaired, because there is nothing to repair it
        # TO: each `tr_M` has one derivation route, so no assertion over it can
        # fail, and `w.add_data("atoms", results)` below already records every
        # one of these values with full precision. The assertion was
        # contributing a guaranteed pass to `allPassed` and nothing else;
        # deleting it loses no information and removes a claim never made.
        #
        # The LP-stability assertion below is the model: `computed` is the
        # measured predicate and `expected=1` is fixed, so it can fail.
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

    w.add_data("coverage", {
        "complete": complete,
        "reached_end_of_configured_roster": reached_end,
        "roster_is_canonical": roster_is_canonical,
        "atoms_expected": len(roster),
        "atoms_canonical": len(CANONICAL_ATOM_ROSTER),
        "atoms_computed": len(results),
        "roster": roster,
        "computed": computed_names,
        "missing": missing,
    })
    w.add_data("atoms", [{k: v for k, v in r.items() if not k.startswith("_")}
                         for r in results])
    w.save()


results = []
print(f"Hadron-level knot table ({len(ATOMS)} atoms)")
print(f"q = {mp.nstr(_Q0, 17)}, basis = {{γ, σ₀, σ₁, L₊, L₋, e⁻}}")
print()
print(f"{'Atom':>12} {'A':>3} {'tr_M':>14} {'B(MeV)':>10} {'cross_sum':>11} {'δ_xchan':>10} {'Frob':>5}")
print("-" * 80)

for name, Z, N, quarks in ATOMS:
    r = compute_atom(name, Z, N, quarks)
    r["_twin_gap_ok"] = r.pop("_twin_gap") <= mp.mpf("1e-10")
    results.append(r)
    print(
        f"{name:>12} {r['A']:>3} "
        f"{mp.nstr(mp.mpf(r['tr_M']), 8):>14} "
        f"{mp.nstr(mp.mpf(r['B_MeV']), 7):>10} "
        f"{mp.nstr(mp.mpf(r['cross_channel_sum']), 7):>11} "
        f"{mp.nstr(mp.mpf(r['delta_xchan_MeV']), 6):>10} "
        f"{'OK' if r['frobenius_stable'] else 'FAIL':>5}"
    )
    # Checkpoint: a killed run keeps the rows it reached (bean `qou-i7ju`).
    _save_witness(results)

print(f"\nTotal NF entries: {sum(r['n_terms'] for r in results)} "
      f"(vs 21,694 quark-level)")
