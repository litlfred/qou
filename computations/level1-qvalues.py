#!/usr/bin/env python3
"""
Level 1 (quark-level) Q-value computation for all 6 verification nuclei.

Level 0: A strands (1 per nucleon), binom(A,2) crossings
Level 1: 3A strands (3 quarks per nucleon), binom(3A,2) crossings

The hecke_engine works at Level 1 WITHOUT code changes — we just
expand the ordering from nucleon-level to quark-level:
  proton (1) → [1, 1, 0]  (u, u, d)
  neutron (0) → [1, 0, 0]  (u, d, d)

The crossing types are:
  u-u (1,1) → positive crossing (weight q)    [= p-p at Level 0]
  d-d (0,0) → negative crossing (weight q⁻¹)  [= n-n at Level 0]
  u-d (1,0) → mixed crossing                   [= p-n at Level 0]

Run from repo root:
    python3 computations/level1-qvalues.py

Output:
    computations/level1-qvalues.witness.json
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mp

sys.path.insert(0, str(Path(__file__).parent.parent))
from hecke.hecke_engine import HeckeRational  # repo-root `hecke/` package, not `computations.`

# ── Quark-level ordering expansion ───────────────────────────────

def expand_to_quarks(nucleon_ordering):
    """Expand nucleon ordering to quark ordering.

    proton (1) → [1, 1, 0]  (u, u, d)
    neutron (0) → [1, 0, 0]  (u, d, d)
    """
    quark_ordering = []
    for nucleon in nucleon_ordering:
        if nucleon == 1:  # proton = uud
            quark_ordering.extend([1, 1, 0])
        else:             # neutron = udd
            quark_ordering.extend([1, 0, 0])
    return quark_ordering


def find_converting_quarks(ord_par_quarks, ord_dau_quarks):
    """Find the 3 quark positions where d→u conversion occurs."""
    converting = []
    for i in range(len(ord_par_quarks)):
        if ord_par_quarks[i] != ord_dau_quarks[i]:
            converting.append(i)
    return converting


# ── Nuclei ───────────────────────────────────────────────────────

nuclei = [
    {"name": "³H",    "p": 1,  "n": 2,  "Q_exp_MeV": 0.0186},
    {"name": "¹⁴C",   "p": 6,  "n": 8,  "Q_exp_MeV": 0.156},
    {"name": "⁶⁰Co",  "p": 27, "n": 33, "Q_exp_MeV": 0.318},
    {"name": "⁹⁰Sr",  "p": 38, "n": 52, "Q_exp_MeV": 0.546},
    {"name": "¹³⁷Cs", "p": 55, "n": 82, "Q_exp_MeV": 0.514},
    {"name": "²¹⁰Bi", "p": 83, "n": 127,"Q_exp_MeV": 1.163},
]

# ── Engine ───────────────────────────────────────────────────────

from fractions import Fraction
from q_parameter import Q_MP, HBAR_Q_SQ_MP
from qou_substrate.precision import COMPUTE_DPS, fmt
mp.dps = COMPUTE_DPS
# The engine needs an exact rational q. It used Q_RAT_NUM/Q_RAT_DEN =
# 11099786/10^7, a 7-digit truncation of q0 that moved Q_q by 1e-7..2e-6
# relative (owner, 2026-11-15). Use q0 (Q_MP) to LEVEL1_Q_DIGITS digits.
import os as _os_q  # noqa: E402
_Q_DIGITS = int(_os_q.environ.get("LEVEL1_Q_DIGITS", "40"))
_q_frac = Fraction(mp.nstr(Q_MP, _Q_DIGITS, strip_zeros=False))
qr = HeckeRational(_q_frac.numerator, _q_frac.denominator)
# NO-FLOAT64 (owner, 2026-11-15): hbar_q^2 as mpf, and each log ratio
# taken on the exact rational V_par/V_dau, never on a float cast.
hbar_q_sq = HBAR_Q_SQ_MP


def _log_abs_ratio(vp, vd):
    """log|vp/vd| for exact Fractions, evaluated at mp.dps."""
    r = vp / vd
    return mp.log(abs(mp.mpf(r.numerator) / mp.mpf(r.denominator)))


import multiprocessing as _mproc  # noqa: E402
_W_ctx = None


def _eval_site(site):
    """Q_q for converting the neutron at nucleon index `site` (exact volumes)."""
    nucleon_par, quark_par, vp_all, n_gens = _W_ctx
    nucleon_dau = list(nucleon_par)
    nucleon_dau[site] = 1
    quark_dau = expand_to_quarks(nucleon_dau)
    converting = find_converting_quarks(quark_par, quark_dau)
    vd_all = qr.traced_volumes_all(quark_dau)
    lr_sum = mp.mpf(0)
    aff = 0
    for i in range(n_gens):
        vp = vp_all[i]
        vd = vd_all[i]
        if vp != 0 and vd != 0 and vp != vd:
            lr_sum += _log_abs_ratio(vp, vd)
            aff += 1
    Q_trial = lr_sum / hbar_q_sq if hbar_q_sq != 0 else 0
    return Q_trial, aff, converting, quark_dau

print("=" * 60)
print("Level 1 (quark-level) Q-value computation")
print("=" * 60)
print(f"q = {float(qr.q)}")
print(f"ℏ_q² = {mp.nstr(hbar_q_sq, 15)}")
print()

results = []

# Resume support (bean qou-l1zd). The heavy nuclei run for hours
# (137Cs ~80 min, 210Bi ~9 h), longer than a cloud job may live, so
# each finished nucleus can be checkpointed and reused on restart.
#   LEVEL1_CHECKPOINT=<path>  per-nucleus results, keyed by q and z
#   LEVEL1_SKIP=<name,...>    record these nuclei as status "pending"
import os as _os_ck  # noqa: E402
_CK_PATH = _os_ck.environ.get("LEVEL1_CHECKPOINT")
_SKIP = {s.strip() for s in _os_ck.environ.get("LEVEL1_SKIP", "").split(",") if s.strip()}
_CK_KEY = f"q={qr.q};z={qr.z}"
_ck = {}
if _CK_PATH and Path(_CK_PATH).exists():
    _loaded = json.loads(Path(_CK_PATH).read_text())
    if _loaded.get("key") == _CK_KEY:
        _ck = _loaded.get("nuclei", {})
    else:
        print(f"Checkpoint key mismatch ({_loaded.get('key')}); ignoring it.")

for nuc in nuclei:
    p, n = nuc["p"], nuc["n"]
    A = p + n
    if nuc["name"] in _ck:
        print(f"{nuc['name']}: reused from checkpoint")
        results.append(_ck[nuc["name"]])
        continue
    if nuc["name"] in _SKIP:
        print(f"{nuc['name']}: skipped (LEVEL1_SKIP), recorded as pending")
        results.append({
            "name": nuc["name"], "A": A, "p": p, "n": n,
            "Q_exp_MeV": nuc["Q_exp_MeV"],
            "status": "pending",
            "pending_reason": (
                "not yet computed on the convention-D engine; estimated "
                "~9 h wall, longer than the cloud job limit (bean qou-l1zd)"),
        })
        continue
    strands_L1 = 3 * A
    crossings_L1 = strands_L1 * (strands_L1 - 1) // 2

    print(f"{'─' * 50}")
    print(f"{nuc['name']}: N({p},{n}), A={A}")
    print(f"  Level 0: {A} strands, {A*(A-1)//2} crossings")
    print(f"  Level 1: {strands_L1} strands, {crossings_L1} crossings")

    t0 = time.time()

    # For heavy nuclei (A > 14), use alternating nucleon ordering
    # which approximates the ground state. For light nuclei, use
    # block ordering (exact ground-state search at quark level is
    # infeasible: binom(3A, total_u) is astronomical).
    if A <= 14:
        nucleon_par = [1] * p + [0] * n
        method = "block"
    else:
        # Alternating ordering: interleave protons and neutrons
        nucleon_par = []
        pi, ni = 0, 0
        for k in range(A):
            if pi < p and (ni >= n or k % 2 == 0):
                nucleon_par.append(1)
                pi += 1
            else:
                nucleon_par.append(0)
                ni += 1
        method = "alternating"

    # Expand parent to quark level
    quark_par = expand_to_quarks(nucleon_par)

    # Try ALL neutron positions as conversion site.
    # The physical beta decay converts the neutron whose conversion
    # gives the smallest |Q_q| with Q_q < 0 (daughter less bound).
    # This avoids the wrong-sign problem from picking an arbitrary site.
    neutron_positions = [k for k in range(A) if nucleon_par[k] == 0]

    best_Q = None
    best_site = None
    best_converting = None
    best_quark_dau = None
    best_affected = 0

    # Parent volumes do not depend on the conversion site: compute once.
    # traced_volumes_all gives the same exact rationals as per-generator
    # traced_volume calls, in one O(A) sweep (bean qou-l1zd).
    _vp_all = qr.traced_volumes_all(quark_par)

    # Every site is independent and exact, so evaluate them in parallel
    # (fork start method; LEVEL1_PROCS, default = all cores). The
    # selection below runs serially in site order, so the result is the
    # same as the serial loop.
    _W_ctx = (nucleon_par, quark_par, _vp_all, strands_L1 - 1)
    _procs = int(_os_ck.environ.get("LEVEL1_PROCS", str(_mproc.cpu_count())))
    if _procs > 1 and len(neutron_positions) > 1:
        with _mproc.get_context("fork").Pool(_procs) as _pool:
            _evals = dict(zip(neutron_positions,
                              _pool.map(_eval_site, neutron_positions, chunksize=1)))
    else:
        _evals = {site: _eval_site(site) for site in neutron_positions}

    def _pick(require_negative):
        nonlocal_best = None
        for site in neutron_positions:
            Q_trial, aff, converting_trial, quark_dau_trial = _evals[site]
            if require_negative and not Q_trial < 0:
                continue
            if nonlocal_best is None or abs(Q_trial) < abs(nonlocal_best[0]):
                nonlocal_best = (Q_trial, site, converting_trial, quark_dau_trial, aff)
        return nonlocal_best

    # Select the conversion site with negative Q_q closest to zero;
    # if none is negative, take the smallest magnitude overall.
    _best = _pick(True) or _pick(False)
    if _best is not None:
        best_Q, best_site, best_converting, best_quark_dau, best_affected = _best

    log_ratio_sum = best_Q * hbar_q_sq if best_Q else 0
    Q_q = best_Q if best_Q else 0
    converting = best_converting if best_converting else []
    affected_count = best_affected
    quark_dau = best_quark_dau if best_quark_dau else quark_par

    elapsed = time.time() - t0

    print(f"  Conversion site: nucleon {best_site} (of {n} neutrons tested)")
    print(f"  Converting positions: {converting}")
    print(f"  Affected generators: {affected_count} / {strands_L1 - 1}")
    print(f"  Σ log|V_par/V_dau| = {float(log_ratio_sum):.6f}")
    print(f"  Q_q (Skein units) = {float(Q_q):.4f}")
    print(f"  Q_exp (MeV) = {nuc['Q_exp_MeV']}")
    print(f"  Time: {elapsed:.2f}s")

    result = {
        "name": nuc["name"], "A": A, "p": p, "n": n,
        "strands_L1": strands_L1, "crossings_L1": crossings_L1,
        "ordering_method": method,
        "converting_positions": converting,
        "affected_generators": affected_count,
        "log_ratio_sum": fmt(log_ratio_sum),
        "Q_q_skein_units": fmt(Q_q),
        "Q_exp_MeV": nuc["Q_exp_MeV"],
        "elapsed_s": elapsed,
        "status": "computed",
    }
    result["conversion_site"] = best_site
    result["n_sites_tested"] = n
    results.append(result)
    if _CK_PATH:
        _ck[nuc["name"]] = result
        Path(_CK_PATH).write_text(json.dumps({"key": _CK_KEY, "nuclei": _ck}, indent=2))
    print()

# ── Assemble witness ─────────────────────────────────────────────
from codata_constants import M_E_MEV as _M_E_MEV_L1  # noqa: E402
import two_term_qtrace_weighting as _ttq  # noqa: E402
_q_l1 = Q_MP
_q2_l1 = _q_l1 ** 2
_me_l1 = mp.mpf(str(_M_E_MEV_L1))
_alpha_bind_l1 = _me_l1 * 8 * mp.catalan
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
_e0_n0_l1 = _qbeta_e0.order_zero_scaled(_me_l1, _q_l1)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
_e0_full_l1 = _e0_n0_l1 / (1 - hbar_q_sq)
_tr_v3_l1 = (-_q2_l1**6 + 3*_q2_l1**5 - 3*_q2_l1**4 + 5*_q2_l1**3 - 3*_q2_l1**2 + 3*_q2_l1 - 1) / (_q2_l1**3)
_tr_e21_l1 = -(_q2_l1**2 - _q2_l1 + 1) * (_q2_l1**4 - 2*_q2_l1**3 - 2*_q2_l1 + 1) / (_q2_l1**3)
_d_qcd_v3_l1 = (_q_l1 - 1 / _q_l1) * _tr_v3_l1
_d_qcd_e21_l1 = (_q_l1 - 1 / _q_l1) * _tr_e21_l1
_denom_e21_qadj_l1 = 9 * (_q2_l1**3) * (_q2_l1**2 + _q2_l1 + 1)
_tr_e21_qadjp_l1 = -2 * ((_q_l1 - 1)**2) * ((_q_l1 + 1)**2) * (_q2_l1**6 - _q2_l1**3 + 1) / _denom_e21_qadj_l1
_tr_e21_qadjn_l1 = (
    4*_q2_l1**8 - 11*_q2_l1**7 + 13*_q2_l1**6 - 22*_q2_l1**5
    + 20*_q2_l1**4 - 22*_q2_l1**3 + 13*_q2_l1**2 - 11*_q2_l1 + 4
) / _denom_e21_qadj_l1
_tr_e21_qadj_diff_l1 = (
    2*_q2_l1**8 - 5*_q2_l1**7 + 5*_q2_l1**6 - 8*_q2_l1**5
    + 8*_q2_l1**4 - 8*_q2_l1**3 + 5*_q2_l1**2 - 5*_q2_l1 + 2
) / (3 * (_q2_l1**3) * (_q2_l1**2 + _q2_l1 + 1))
_tr_conn_p_l1 = -2 * ((_q2_l1 - 1)**4) * (_q2_l1**2 + _q2_l1 + 1) / (27 * (_q2_l1**3))
_tr_conn_n_l1 = ((_q2_l1 - 1)**4) * (2*_q2_l1**2 - _q2_l1 + 2) / (27 * (_q2_l1**3))
_tr_conn_diff_l1 = ((_q2_l1 - 1)**4) * (4*_q2_l1**2 + _q2_l1 + 4) / (27 * (_q2_l1**3))

borromean_v3_two_term_diagnostics = {
    "lean_ref": "QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm",
    "tr_V3": fmt(_tr_v3_l1),
    "tr_e3_V3": fmt(mp.mpf(1)),
    "tr_e21_V3": fmt(_tr_e21_l1),
    "Delta_tr_QCD_V3": fmt(_d_qcd_v3_l1),
    "Delta_tr_QCD_e21_V3": fmt(_d_qcd_e21_l1),
    "Delta_m_QCD_V3_alpha_bind_MeV": fmt(_alpha_bind_l1 * _d_qcd_v3_l1),
    "Delta_m_QCD_e21_E0_full_MeV": fmt(_e0_full_l1 * _d_qcd_e21_l1),
    "Delta_m_QCD_e21_E0_N0_MeV": fmt(_e0_n0_l1 * _d_qcd_e21_l1),
    "Delta_m_QCD_e21_alpha_bind_MeV": fmt(_alpha_bind_l1 * _d_qcd_e21_l1),
    "tr_e21_QAdjp_V3": fmt(_tr_e21_qadjp_l1),
    "tr_e21_QAdjn_V3": fmt(_tr_e21_qadjn_l1),
    "Delta_tr_e21_QAdj_V3": fmt(_tr_e21_qadj_diff_l1),
    "Delta_m_QED_e21_me_MeV": fmt(_me_l1 * _tr_e21_qadj_diff_l1),
    "tr_conn_p_V3": fmt(_tr_conn_p_l1),
    "tr_conn_n_V3": fmt(_tr_conn_n_l1),
    "Delta_tr_conn_V3": fmt(_tr_conn_diff_l1),
    "weighting_canonical": "derived Tr(K^{⊗3}·)/[2]_q³ (qou-99qc); M_p/Delta_m without _derived are the historical 1/3-normalised 'plain' entries",
    "M_p_QED_conn_derived_MeV": fmt(_ttq.m_p_qed_conn_mev(_q_l1, _me_l1, "derived")),
    "Delta_m_QED_conn_derived_MeV": fmt(_ttq.delta_m_qed_conn_mev(_q_l1, _me_l1, "derived")),
    "M_p_QED_conn_MeV": fmt(_me_l1 * abs(_tr_conn_p_l1)),
    "Delta_m_QED_conn_MeV": fmt(-_me_l1 * _tr_conn_diff_l1),
}

witness = {
    "computation": "level1-qvalues",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "description": (
        "Level 1 (quark-level) Q-value computation. "
        "Each nucleon expanded to 3 quark strands (u,u,d or u,d,d). "
        "All n neutron positions tested as conversion sites; "
        "the site giving negative Q_q with smallest magnitude is selected."
    ),
    "q": str(qr.q),
    "q_digits": _Q_DIGITS,
    "hbar_q_sq": fmt(hbar_q_sq),
    "nuclei": results,
    "borromean_v3_two_term_diagnostics": borromean_v3_two_term_diagnostics,
    "notes": [
        "Block ordering [protons first] is NOT the ground state for Level 1.",
        "Ground-state search at Level 1 has binom(3A, total_u) orderings.",
        "For A=3: binom(9,5) = 126 orderings — feasible.",
        "For A=14: binom(42,20) ~ 10^11 — needs heuristic.",
        "The Q_q values here are UPPER BOUNDS (block ordering overestimates).",
    ],
}

out_path = Path(__file__).parent / "level1-qvalues.witness.json"
with open(out_path, "w") as f:
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    json.dump(witness, f, indent=2)

print(f"Witness written to {out_path}")
