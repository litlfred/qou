#!/usr/bin/env python3
"""The nucleon gluon segment by the γγ rule: diagnostics on CORE·TAIL·V^k.

Pre-registration: computations/probes/gg_gluon_segment/preregistration.md
(step 1 a341245311, step 2 a9ca10d266). Bean parent qou-99qc.

The γγ rule (qou-ales; GammaGammaWordSelection.vertex) applied to the gluon slot
on three strands gives the family V^k, V = σ0σ1⁻¹ (the corpus gluonUnit). The
step-2 space is k ∈ {0,1,2,3}; the only filter is whole-word reading 3. Every
member is reported. Nothing is ranked by bar parity, Q_β or any residual.

Exact sympy over Q(q) for every verdict; the proton pin enters as an exact
rational of Q_50_DIGIT_STR; mpmath at 60 dps for display only. No float64.
No dashboard re-score (qou-iagg); per_observable_100x_status is not touched.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
import os
import subprocess
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python", "tools/pyhecke/python"):
    _s = os.path.join(ROOT, _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
import qbeta_e0  # noqa: E402
from codata_constants import Q_BETA_MEV  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "_census", os.path.join(ROOT, "computations", "qbeta", "qbeta_delta_candidate_census_probe.py"))
_census = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_census)
hm, h = _census.hm, _census.h

mp.mp.dps = 60

q = sp.symbols("q", positive=True)
H = q - 1 / q
ZD = q ** 3 / (q ** 2 + 1)
Q0 = sp.Rational(Q_50_DIGIT_STR)

CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
    return ok


def zero(e):
    return sp.simplify(sp.together(e)) == 0


def bar(e):
    return sp.together(sp.sympify(e).subs(q, 1 / q))


def at_q0(e):
    """Exact rational substitution, then an mpmath readout (display only)."""
    v = sp.Rational(sp.simplify(sp.sympify(e).subs(q, Q0)))
    num, den = v.p, v.q
    return mp.mpf(int(num)) / mp.mpf(int(den))


def s(x, n=12):
    return mp.nstr(x, n)


# ------------------------------------------------------------------ letters
U = lambda g: (sp.Integer(1), sp.Integer(0), g)          # σ_g
D = lambda g: (sp.Integer(1), -h, g)                      # σ_g⁻¹ = σ_g − h
UD = lambda g: (sp.Integer(1), -h / 2, g)                 # averaged ud letter
V = [U(0), D(1)]                                          # γγ vertex 0 = gluonUnit
CORE = V * 3
SIGMA0_PAIR = [U(0), U(0)]                                # census gluon pair
TAIL = {"p": [U(0), UD(0), UD(1)], "n": [UD(0), UD(0), D(1)]}
# n − p telescoping (positions 1 and 3 of the tail differ by −h/2 each)
T1, T2 = [UD(0), D(1)], [U(0), UD(0)]


def bar_letters(ls):
    return [(c, sp.expand(-c * h + d.subs(h, -h)), g) for c, d, g in ls]


def nf_of(letters):
    nf = [sp.Integer(1)] + [sp.Integer(0)] * 5
    for c, d, g in letters:
        nf = hm(nf, c, d, g)
    return nf


def tr(letters, zz=ZD):
    nf = nf_of(letters)
    hz = h * zz + 1
    basis = [sp.Integer(1), zz, zz, zz ** 2, zz ** 2, zz * hz]
    return sp.factor(sp.together(sp.expand(sum(c * t for c, t in zip(nf, basis))).subs(h, H)))


# ------------------------------------------------------- reading 3 machinery
Y21 = sp.factor((q - ZD) / (q + 1 / q))
Y3 = sp.factor(1 - 2 * Y21)


def chi3(letters):
    return sp.factor(sp.prod([(c * q + d).subs(h, H) for c, d, _ in letters]))


def chi21(letters):
    return sp.factor((tr(letters) - Y3 * chi3(letters)) / Y21)


def det21(letters):
    return sp.factor(sp.prod([((c * q + d) * (d - c / q)).subs(h, H) for c, d, _ in letters]))


def chi111(letters):
    return sp.factor(sp.prod([(d - c / q).subs(h, H) for c, d, _ in letters]))


# independent route: explicit seminormal 2x2 (2,1) representation
_A = H / (1 - q ** -4)
_A2 = H / (1 - q ** 4)
S0 = sp.Matrix([[q, 0], [0, -1 / q]])
S1 = sp.Matrix([[_A, 1], [_A * _A2 + 1, _A2]])
if not zero((S0 * S1 * S0 - S1 * S0 * S1).norm()):
    S1 = sp.Matrix([[_A2, 1], [_A * _A2 + 1, _A]])


def chi21_matrix(letters):
    M = sp.eye(2)
    for c, d, g in letters:
        M = M * (c * (S0 if g == 0 else S1) + d.subs(h, H) * sp.eye(2))
    return sp.factor(sp.together(M.trace()))


# ------------------------------------------------------------ diagnostics
def g_of(gluon):
    return sp.factor(-(tr(CORE + T1 + gluon) + tr(CORE + T2 + gluon)) / 2)


def diagnostics(gluon, E0):
    wp, wn = CORE + TAIL["p"] + gluon, CORE + TAIL["n"] + gluon
    f = sp.factor(tr(wn) - tr(wp))
    g = g_of(gluon)
    g_odd = sp.factor((g - bar(g)) / 2)
    out = {"f": f, "g": g, "g_odd": g_odd, "f_eq_hg": zero(f - H * g)}
    for x, w in (("p", wp), ("n", wn)):
        out[f"chi3_{x}"] = chi3(w)
        out[f"chi21_{x}"] = chi21(w)
        out[f"det21_{x}"] = det21(w)
        out[f"chi111_{x}"] = chi111(w)
        out[f"chi21_matrix_agrees_{x}"] = zero(chi21_matrix(w) - out[f"chi21_{x}"])
    dtr = at_q0(f)
    out["delta_tr_q0"] = dtr
    out["Q_beta_MeV"] = abs(dtr) * E0
    out["Q_beta_pct"] = (abs(dtr) * E0 - mp.mpf(str(Q_BETA_MEV))) / mp.mpf(str(Q_BETA_MEV)) * 100
    out["reading3_p"] = bool(at_q0(out["chi3_p"]) >= 0 and at_q0(out["chi21_p"]) >= 0)
    out["reading3_n"] = bool(at_q0(out["chi3_n"]) >= 0 and at_q0(out["chi21_n"]) >= 0)
    return out


def localise(gluon):
    """R5-style Möbius split of g_odd into core / tail / gluon contributions."""
    def g_sub(sub):
        c = bar_letters(CORE) if "core" in sub else CORE
        gl = bar_letters(gluon) if "gluon" in sub else gluon
        t1 = bar_letters(T1) if "tail" in sub else T1
        t2 = bar_letters(T2) if "tail" in sub else T2
        return sp.factor(-(tr(c + t1 + gl) + tr(c + t2 + gl)) / 2)
    segs = ("core", "tail", "gluon")
    G = {t: g_sub(set(t)) for r in range(4) for t in itertools.combinations(segs, r)}
    eff = {}
    for r in range(1, 4):
        for t in itertools.combinations(segs, r):
            m = sum((-1) ** (r - k) * G[u] for k in range(r + 1) for u in itertools.combinations(t, k))
            eff["x".join(t)] = sp.factor(-m / 2)
    return eff


def _find(relpath, key):
    """First value stored under `key` anywhere in a committed witness (no literal copies)."""
    def walk(o):
        if isinstance(o, dict):
            if key in o:
                return o[key]
            for v in o.values():
                r_ = walk(v)
                if r_ is not None:
                    return r_
        elif isinstance(o, list):
            for v in o:
                r_ = walk(v)
                if r_ is not None:
                    return r_
        return None
    with open(os.path.join(ROOT, relpath)) as fh:
        val = walk(json.load(fh))
    if val is None:
        raise KeyError(f"{key} not in {relpath}")
    return mp.mpf(str(val))


def main() -> int:
    E0 = qbeta_e0.canonical()
    REF_DTR = _find("computations/qbeta/qbeta-qbeta-scores-a-difference.witness.json", "recorded_tr_conv_D")
    REF_E0 = _find("computations/qbeta/qbeta-e0-is-derived.witness.json", "E_0_tower_summed")
    # nuc11_interleaved was the scored Q_beta cell until the owner ruling D1 = A
    # (2026-11-20, bean qou-99qc); the scorecard now keeps it as an unscored history
    # cell. Calibrate against that cell, not against the first Q_beta_MeV, which is
    # now |eps_flavour(V^3)|*E0 (a different element and functional).
    with open(os.path.join(ROOT, "computations/per-observable-100x-status.witness.json")) as fh:
        _hist = json.load(fh)["data"]["qbeta_ruled_base"]["unscored_history_cells"]
    _nuc11 = [v for k, v in _hist.items() if k.startswith("nuc11_interleaved")]
    if len(_nuc11) != 1:
        raise KeyError("nuc11_interleaved history cell not found exactly once")
    REF_QB = mp.mpf(str(_nuc11[0]["Q_beta_MeV"]))

    print("C1  rerun the bar-parity-split probe")
    r = subprocess.run([sys.executable, os.path.join(ROOT, "computations/qbeta/qbeta_bar_parity_split_gap_probe.py")],
                       capture_output=True, text=True)
    check("C1_bar_parity_split_probe_24_of_24", r.returncode == 0 and "24/24 checks pass" in r.stdout)

    print("\nC2/C3/C4  calibration on nuc11_interleaved (gluon = σ0σ0)")
    P12 = 2*q**12 - 6*q**10 + 3*q**8 - 6*q**6 + 5*q**4 - 5*q**2 + 2
    ref = diagnostics(SIGMA0_PAIR, E0)
    check("C2_f_closed_form", zero(ref["f"] - (q**2 - 1)*(q**4 + 1)*P12/(4*q**7*(q**2 + 1)**2)))
    check("C2_f_eq_h_g", ref["f_eq_hg"])
    check("C2_g_odd_closed_form", zero(ref["g_odd"] + H*(q + 1/q)*(q**2 + q**-2)/8), str(ref["g_odd"]))
    check("C3_delta_tr", abs(ref["delta_tr_q0"] - REF_DTR) < mp.mpf("1e-24"),
          s(ref["delta_tr_q0"], 25))
    check("C3_E0_canonical", abs(E0 - REF_E0) < mp.mpf("1e-18"), s(E0, 15))
    check("C3_Q_beta_nuc11_history_cell", abs(ref["Q_beta_MeV"] - REF_QB) < mp.mpf("1e-18"),
          s(ref["Q_beta_MeV"], 12))
    check("C4_y_normalisation", zero(Y3 + 2*Y21 - 1))
    check("C4_y21_value", abs(at_q0(Y21) - mp.mpf("0.2473")) < mp.mpf("5e-5"), s(at_q0(Y21), 10))
    check("C4_y111_zero_at_zD", zero(tr([]) - (Y3 + 2*Y21)) and zero(ZD - (Y3*q + Y21*H)))
    check("C4_chi21_identity_is_2", zero(chi21([]) - 2))
    check("C4_chi3_of_V^k_is_1", all(zero(chi3(V * k) - 1) for k in range(7)))
    check("C4_chi21_V3_core_admitted", abs(at_q0(chi21(V * 3)) - mp.mpf("1.9942")) < mp.mpf("5e-5"),
          s(at_q0(chi21(V * 3)), 10))
    rec = {"chi3_p": "1.38249446339", "chi3_n": "1.1221068216", "chi21_p": "-0.2805933509",
           "chi21_n": "-0.3719563247", "det21_p": "-1.02197249381", "det21_n": "-1.02197249381",
           "chi111_p": "-0.739223570776", "chi111_n": "-0.910762214553"}
    for k_, v in rec.items():
        val = at_q0(ref[k_])
        check(f"C4_{k_}", abs(val - mp.mpf(v)) < mp.mpf(10) ** (-(len(v.split('.')[1]) - 1)), s(val, 13))
    check("C5_seminormal_braid_relation", zero((S0 * S1 * S0 - S1 * S0 * S1).norm()))
    check("C5_seminormal_hecke_relation", zero((S1 * S1 - H * S1 - sp.eye(2)).norm()))
    check("C5_chi21_matrix_route_on_nuc11", ref["chi21_matrix_agrees_p"] and ref["chi21_matrix_agrees_n"])

    print("\nStep 2  elements CORE · TAIL_x · V^k, k = 0..3 (all reported, no ranking)")
    rows = []
    for k in range(4):
        gl = V * k
        d = diagnostics(gl, E0)
        # P1: cyclic equivalence with V^(3+k)·TAIL
        p1 = all(zero(tr(V * (3 + k) + TAIL[x]) - tr(CORE + TAIL[x] + gl))
                 and zero(chi21(V * (3 + k) + TAIL[x]) - d[f"chi21_{x}"]) for x in "pn")
        check(f"P1_k{k}_equals_V^{3+k}_TAIL", p1)
        check(f"C5_k{k}_matrix_route", d["chi21_matrix_agrees_p"] and d["chi21_matrix_agrees_n"])
        check(f"k{k}_f_eq_h_g", d["f_eq_hg"])
        loc = localise(gl) if k > 0 else {}
        row = {
            "k": k, "gluon_segment": "(σ0σ1⁻¹)^%d" % k, "letters": 9 + 2 * k,
            "g_odd": str(d["g_odd"]), "g_odd_is_zero": zero(d["g_odd"]),
            "g_odd_q0": s(at_q0(d["g_odd"]), 15),
            "chi3_p_q0": s(at_q0(d["chi3_p"]), 13), "chi3_n_q0": s(at_q0(d["chi3_n"]), 13),
            "chi21_p": str(d["chi21_p"]), "chi21_n": str(d["chi21_n"]),
            "chi21_p_q0": s(at_q0(d["chi21_p"]), 13), "chi21_n_q0": s(at_q0(d["chi21_n"]), 13),
            "det21_p_q0": s(at_q0(d["det21_p"]), 13), "det21_n_q0": s(at_q0(d["det21_n"]), 13),
            "chi111_p_q0": s(at_q0(d["chi111_p"]), 13), "chi111_n_q0": s(at_q0(d["chi111_n"]), 13),
            "reading3_p": d["reading3_p"], "reading3_n": d["reading3_n"],
            "reading3_both": d["reading3_p"] and d["reading3_n"],
            "delta_tr_q0": s(d["delta_tr_q0"], 20),
            "Q_beta_MeV": s(d["Q_beta_MeV"], 12), "Q_beta_pct_vs_codata": s(d["Q_beta_pct"], 8),
            "g_odd_localisation": {kk: str(vv) for kk, vv in loc.items()},
        }
        rows.append(row)
        print(f"  k={k}: g_odd={row['g_odd']}\n        chi21 p={row['chi21_p_q0']} n={row['chi21_n_q0']}"
              f"  reading3 p={row['reading3_p']} n={row['reading3_n']}  Q_beta={row['Q_beta_MeV']} MeV"
              f" ({row['Q_beta_pct_vs_codata']} %)")
        for kk, vv in loc.items():
            print(f"        g_odd part {kk}: {vv}")

    ref_row = {
        "gluon_segment": "σ0σ0 (census, nuc11_interleaved; reference only)",
        "g_odd": str(ref["g_odd"]), "g_odd_q0": s(at_q0(ref["g_odd"]), 15),
        "chi21_p_q0": s(at_q0(ref["chi21_p"]), 13), "chi21_n_q0": s(at_q0(ref["chi21_n"]), 13),
        "reading3_p": ref["reading3_p"], "reading3_n": ref["reading3_n"],
        "Q_beta_MeV": s(ref["Q_beta_MeV"], 12), "Q_beta_pct_vs_codata": s(ref["Q_beta_pct"], 8),
    }
    survivors = [r_["k"] for r_ in rows if r_["reading3_both"]]
    print(f"\n  reading-3 survivors (both nucleons): k in {survivors}  ({len(survivors)} of 4)")

    nfail = sum(1 for _, ok, _ in CHECKS if not ok)
    out = {
        "scriptFile": "computations/probes/gg_gluon_segment/gg_gluon_segment_probe.py",
        "engine": "sympy exact over Q(q) + mpmath 60 dps display",
        "commitSha": subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip(),
        "recipe": "computations/probes/gg_gluon_segment/preregistration.md (a341245311 step 1, a9ca10d266 step 2)",
        "bean_parent": "qou-99qc",
        "q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR,
        "convention": "D, z = q^3/(q^2+1)",
        "E0": {"function": "qbeta_e0.canonical() (tower_summed)", "value_MeV": s(E0, 15)},
        "Q_beta_codata_MeV": str(Q_BETA_MEV),
        "reference_nuc11_interleaved": ref_row,
        "rows": rows,
        "reading3_survivors_k": survivors,
        "checks": {n: ok for n, ok, _ in CHECKS},
        "checks_passed": f"{len(CHECKS) - nfail}/{len(CHECKS)}",
        "scope": "diagnostics only; no element selected; dashboard not re-scored (qou-iagg)",
    }
    with open(os.path.join(HERE, "gg-gluon-segment.witness.json"), "w") as fh:
        fh.write(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"\n{len(CHECKS) - nfail}/{len(CHECKS)} checks pass")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
