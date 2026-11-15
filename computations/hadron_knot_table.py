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
import sys
import time
from pathlib import Path
from mpmath import mp

sys.path.insert(0, str(Path(__file__).parent))

from _precision import set_compute_dps, fmt, COMPUTE_DPS  # noqa: E402

# Set the working precision BEFORE any module-level mpf is built: an mpf
# rounds to the AMBIENT dps, which is mpmath's default 15 until this runs.
set_compute_dps()

# `q_at` is anchor-aware: `q_parameter` selects the pin from this script's
# stem via `q0_anchor_manifest.json`. `hadron_knot_table` is listed under
# `physical_proton` (moved from `ideal_muon` 2026-11-15): it tabulates
# mass / binding / Q-value observables, which is neither an explicit
# proton-vs-muon comparison (E1) nor the CAL-1/2/3 calibration as
# mathematics (E2), so the owner's proton default applies.
from q_parameter import q_at  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from hecke_core_legacy import (  # noqa: E402
    binding_energy,
    classify_nuclear_knot,
)
from pyhecke.gram import (  # noqa: E402
    build_atom_nf,
    gram_matrix_mp,
    NF_NAMES,
)
from pyhecke.atom import build_nucleon_nf  # noqa: E402
from pyhecke.constants import pn_interface_offset  # noqa: E402
from hecke_engine import HeckeEngine  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# ── Substrate constants at the working precision (NO float64) ────────────
# Everything below is mpf at COMPUTE_DPS from the 70-digit anchor-aware
# `q_at`. This replaces (2026-11-15) the float64 `q_parameter.Q` that fed
# `parameters.q` / `z_markov` / `z_squared` and the 50-digit
# `Q_50_DIGIT_STR` that fed the volume port — 50 digits is BELOW the
# 60-digit OUTPUT_DPS, so `fmt` of anything built from it padded.
_Q0 = q_at(COMPUTE_DPS)
_QI0 = 1 / _Q0
_HA0 = _Q0 - _QI0
# Markov parameter, convention D: z = q³/(q² + 1).
_z_q0 = _Q0**3 / (_Q0**2 + 1)
_Z2 = _z_q0 * _z_q0
# Canonical p-n interface offset (bring_color_weighted, owner ruling R3),
# the same `D_PN` `pyhecke.atom.build_atom_nf` binds, but at the mpf q.
_D_PN0 = pn_interface_offset(_Q0)
# Markov trace on the NF basis {γ, σ₀, σ₁, L₊, L₋, e⁻}.
_TR_M0 = [mp.mpf(1), _z_q0, _z_q0, _Z2, _Z2, _HA0 * _Z2 + _z_q0]
# Gram matrix G_ij = tr_M(b_i b_j) at the same q, for Frobenius positivity.
_G0 = gram_matrix_mp(COMPUTE_DPS, q=_Q0)
# Frobenius-positivity tolerance: the value the float64 `check_frobenius`
# used, kept so a verdict is not changed by the arithmetic change alone.
_FROB_TOL = mp.mpf("1e-10")
# Cross-check bound between this mp NF and the float64 builder. The float64
# builder carries ~16 digits, compounded over up to ~1000 multiplications
# for fe56; 1e-9 relative is loose enough not to fire on that and tight
# enough to catch a CONSTRUCTION drift (a missing crossing moves a
# component by O(1), see `build_nucleon_nf_mp`'s 2288 % episode).
_XCHECK_REL = mp.mpf("1e-9")

_HE = HeckeEngine(111, 100)  # ground-state ordering only (q-independent)

# `binding_energy`'s SDP leg (`sdp_cross_channel`) needs cvxpy; without it the
# leg falls back to a scalar LP whose status is not `optimal`, and the leg is
# SILENTLY 0.0 (measured: deuterium -15.81 MeV without, +0.54 MeV with). The
# witness `environment` block does not list cvxpy, so record it here.
import importlib.util as _ilu  # noqa: E402
_HAS_CVXPY = _ilu.find_spec("cvxpy") is not None


def _hm0(nf, c, d, gen):
    """NF × (c·σ_gen + d·I) in H₃(q) at the mpf q — same structure
    constants as `pyhecke.gram.hm`, no float64, no small-coefficient skip."""
    h = _HA0
    r = [mp.mpf(0)] * 6
    if gen == 0:
        tables = [
            (0, [(1, c), (0, d)]),
            (1, [(1, c * h), (0, c), (1, d)]),
            (2, [(3, c), (2, d)]),
            (3, [(3, c * h), (2, c), (3, d)]),
            (4, [(5, c), (4, d)]),
            (5, [(5, c * h), (4, c), (5, d)]),
        ]
    else:
        tables = [
            (0, [(2, c), (0, d)]),
            (1, [(4, c), (1, d)]),
            (2, [(2, c * h), (0, c), (2, d)]),
            (3, [(5, c), (3, d)]),
            (4, [(4, c * h), (1, c), (4, d)]),
            (5, [(5, c * h), (3, c), (5, d)]),
        ]
    for si, tgts in tables:
        if nf[si] == 0:
            continue
        for ti, co in tgts:
            r[ti] += nf[si] * co
    return r


_ONE, _ZERO = mp.mpf(1), mp.mpf(0)


def _nucleon_block0(nf, kind):
    """One nucleon's 11 crossings, in the order of
    `pyhecke.atom.build_atom_nf` / `build_nucleon_nf`."""
    h, half_h = _HA0, _HA0 / 2
    for _ in range(3):                      # B₃ = (σ₀ σ₁⁻¹)³
        nf = _hm0(nf, _ONE, _ZERO, 0)
        nf = _hm0(nf, _ONE, -h, 1)
    if kind == "uud":                       # proton quark crossings
        nf = _hm0(nf, _ONE, _ZERO, 0)       # (0,1) uu
        nf = _hm0(nf, _ONE, -half_h, 0)     # (0,2) ud
        nf = _hm0(nf, _ONE, -half_h, 1)     # (1,2) ud
    elif kind == "udd":                     # neutron quark crossings
        nf = _hm0(nf, _ONE, -half_h, 0)     # (0,1) ud
        nf = _hm0(nf, _ONE, -half_h, 0)     # (0,2) ud
        nf = _hm0(nf, _ONE, -h, 1)          # (1,2) dd
    else:
        raise ValueError(f"unknown nucleon quark content {kind!r}")
    nf = _hm0(nf, _ONE, _ZERO, 0)           # gluon 1
    nf = _hm0(nf, _ONE, _ZERO, 0)           # gluon 2
    return nf


def _build_nucleon_nf0(quarks):
    return _nucleon_block0([_ONE] + [_ZERO] * 5, quarks)


def _build_atom_nf0(Z, N):
    """mpf twin of `pyhecke.atom.build_atom_nf` (interleaved ground state,
    all-pairs inter-nucleon crossings with the colour-weighted p-n offset,
    one σ₁⁻¹ per electron)."""
    A = Z + N
    nf = [_ONE] + [_ZERO] * 5
    if A == 0:
        return nf
    ordering, pc, nc = [], 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append("p")
            pc += 1
        else:
            ordering.append("n")
            nc += 1
    for k in range(A):
        nf = _nucleon_block0(nf, "uud" if ordering[k] == "p" else "udd")
        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == "p" and tj == "p":
                nf = _hm0(nf, _ONE, _ZERO, 0)      # pp: σ₀
            elif ti == "n" and tj == "n":
                nf = _hm0(nf, _ONE, -_HA0, 0)      # nn: σ₀⁻¹
            else:
                nf = _hm0(nf, _ONE, _D_PN0, 0)     # pn: colour-weighted
    for _ in range(Z):
        nf = _hm0(nf, _ONE, -_HA0, 1)              # pe: σ₁⁻¹
    return nf


def _xcheck_vs_float_builder(nf_mp, nf_f64, what):
    """Refuse to publish if the mp twin and the float64 builder disagree
    beyond float64 accumulation — a construction drift, not rounding."""
    scale = max(abs(mp.mpf(v)) for v in nf_mp) or _ONE
    worst = max(abs(a - mp.mpf(float(b))) for a, b in zip(nf_mp, nf_f64))
    if worst / scale > _XCHECK_REL:
        raise RuntimeError(
            f"{what}: mpf NF twin disagrees with the float64 builder by "
            f"{mp.nstr(worst / scale, 5)} relative (> {_XCHECK_REL}); the "
            f"two constructions have drifted apart — fix before publishing")
    return worst / scale


def _check_frobenius0(nf):
    """Frobenius positivity G·x ≥ 0 at the mpf q. (stable, Gx, violations)."""
    Gx = [mp.fsum(_G0[i][j] * nf[j] for j in range(6)) for i in range(6)]
    violations = [(NF_NAMES[i], Gx[i]) for i in range(6) if Gx[i] < -_FROB_TOL]
    return len(violations) == 0, Gx, violations


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

    Cross-channel (mass-endomorphism-tower formula sum 3):
        δ_xchan = z² × Σ_{|i-j|=1} ln|V̂_i^full · V̂_j^full| × m_e

    All mpf at COMPUTE_DPS.

    Returns:
        ordering, V_full_list, cross_sum, delta_xchan_MeV
    """
    A = Z + N
    if A < 2:
        return [], [], mp.mpf(0), mp.mpf(0)

    ordering, method = _HE.ground_state_ordering(Z, N)
    V_list = _v_full_all_q0(ordering)

    cross_sum = mp.mpf(0)
    for i in range(len(V_list) - 1):
        prod = abs(V_list[i] * V_list[i + 1])
        if prod != 0:
            cross_sum += mp.log(prod)

    delta_xchan = _Z2 * cross_sum * mp.mpf(M_E_MEV)
    return ordering, V_list, cross_sum, delta_xchan


def compute_atom(name, Z, N, quarks=None):
    """Compute hadron-level NF for one atom.

    Every published number is computed in mpf at COMPUTE_DPS and serialized
    with `fmt` (2026-11-15). The float64 builders are still called, but ONLY
    as a cross-check of the mpf twin's construction (`_xcheck_vs_float_builder`).
    The one float64 value left is `B_MeV`: `binding_energy` returns `float`
    by contract and its SDP leg is a float64 conic solve — see
    `B_MeV_precision_note` in the witness.
    """
    if quarks:
        nf = _build_nucleon_nf0(quarks)
        nf_f64 = build_nucleon_nf(list(quarks))
    else:
        nf = _build_atom_nf0(Z, N)
        nf_f64 = build_atom_nf(Z, N)
    xcheck = _xcheck_vs_float_builder(nf, nf_f64, name)

    tr = mp.fsum(nf[i] * _TR_M0[i] for i in range(6))
    net = mp.fsum(nf)
    stable, Gx, violations = _check_frobenius0(nf)
    alpha_knot, knot_name, is_hyp = classify_nuclear_knot(Z, N)
    B = binding_energy(Z, N)

    # Compact NF: the non-zero coefficients with basis names (exact zero
    # test — the coefficients are mpf, so there is no float64 noise floor
    # to threshold against).
    nf_compact = {bname: fmt(val) for bname, val in zip(NF_NAMES, nf)
                  if val != 0}

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
        "frobenius_min_Gx": fmt(min(Gx)),
        "nf_float64_builder_max_rel_dev": mp.nstr(xcheck, 3),
        "knot_type": knot_name,
        "B_MeV": float(B),
        # Per-generator traced volumes (mass-tower formula, sum 1 + 3)
        "ordering": ordering,
        "V_per_gen": [fmt(v) for v in V_list],
        "cross_channel_sum": fmt(cross_sum),
        "delta_xchan_MeV": fmt(delta_xchan),
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
    w.add_parameter("z_markov", fmt(_z_q0))
    w.add_parameter("z_markov_convention", "D: z = q^3/(q^2+1)")
    w.add_parameter("z_squared", fmt(_Z2))
    w.add_parameter("pn_interface_offset", fmt(_D_PN0))
    w.add_parameter("frobenius_tolerance", mp.nstr(_FROB_TOL, 3))
    w.add_parameter("cvxpy_available", _HAS_CVXPY)
    w.add_parameter("n_atoms_expected", len(ATOMS))
    w.add_parameter("n_atoms_computed", len(results))
    w.add_parameter("total_nf_entries", total_terms)

    # Assertions: LP stability, over the computed atoms only.
    for r in results:
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
    w.add_data("B_MeV_precision_note", (
        "B_MeV is the only float64 field per atom. "
        "hecke_core_legacy.binding_energy returns float by public contract "
        "(bean qou-sv7h) and its sdp_cross_channel_contribution leg is a "
        "float64 conic solve, so no exact source exists to carry; it is "
        "left a float rather than padded. It also depends on whether cvxpy "
        "is installed (the SDP leg is 0.0 without it), which the "
        "environment block does not record — see parameters.cvxpy_available."))
    w.add_data("atoms", results)
    w.save()


results = []
print(f"Hadron-level knot table ({len(ATOMS)} atoms)")
if not _HAS_CVXPY:
    print("⚠ cvxpy not installed: binding_energy's SDP leg will be 0.0 "
          "(scalar-LP fallback); B_MeV is then the degraded branch.")
print(f"q = {mp.nstr(_Q0, 20)}, basis = {{γ, σ₀, σ₁, L₊, L₋, e⁻}}")
print()
print(f"{'Atom':>12} {'A':>3} {'tr_M':>14} {'B(MeV)':>10} {'cross_sum':>11} {'δ_xchan':>10} {'Frob':>5}")
print("-" * 80)

_t_run = time.monotonic()
for name, Z, N, quarks in ATOMS:
    _t_atom = time.monotonic()
    r = compute_atom(name, Z, N, quarks)
    results.append(r)
    print(
        f"{name:>12} {r['A']:>3} "
        f"{mp.nstr(mp.mpf(r['tr_M']), 8):>14} "
        f"{r['B_MeV']:>10.4f} "
        f"{mp.nstr(mp.mpf(r['cross_channel_sum']), 7):>11} "
        f"{mp.nstr(mp.mpf(r['delta_xchan_MeV']), 6):>10} "
        f"{'OK' if r['frobenius_stable'] else 'FAIL':>5}"
    )
    print(f"    [{name}: {time.monotonic() - _t_atom:.1f} s, "
          f"run {time.monotonic() - _t_run:.1f} s, "
          f"{len(results)}/{len(ATOMS)} atoms]", flush=True)
    # Checkpoint: a killed run keeps the rows it reached (bean `qou-i7ju`).
    _save_witness(results)

print(f"\nTotal NF entries: {sum(r['n_terms'] for r in results)} "
      f"(vs 21,694 quark-level)")
