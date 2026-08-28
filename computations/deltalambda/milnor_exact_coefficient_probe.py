#!/usr/bin/env python3
"""milnor_exact_coefficient_probe.py — Route C of #4480.

Extend #4471's TWO exact-order data points (A=3 proved, A=4 measured) to FOUR by
computing the A=5 and A=6 iterated-commutator Brunnian trace-deficit leading
orders + leading coefficients, and EXTRACT the leading-coefficient sequence
mubar_A (A=3..6), then check whether it encodes the 1.585x "missing structure" the
A=3 magnitude bracketing (#4364/#4376/#4392/#4472) flagged.

Two trace conventions are computed side by side (both from the SAME Hoefsmit
characters chi_lambda and canonical Wenzl weights y_lambda):

  * SIGNED  tr_M(w) = sum_lambda y_lambda * chi_lambda(w)   -- the genuine CYCLIC
                                              Markov trace (convention C / Wenzl).
  * ABS     g(w)    = sum_lambda y_lambda * |chi_lambda(w)| -- the NON-cyclic
                                              perblock functional (#4364/#4378).

Deficit D_A(h) = 1 - trace(w_A)/trace(unlink), h = q - q^-1.  w_A is the
left-normed iterated commutator of pure-braid band generators (Brunnian, verified
by the strand-forgetting map d_k -> identity, as in a4_h12_brunnian_deficit_measure).

  w3 = [A01,A12]
  w4 = [[A01,A12],A23]
  w5 = [[[A01,A12],A23],A34]
  w6 = [[[[A01,A12],A23],A34],A45]

For each A and each convention: leading h-order (log-log slope) and leading
coefficient mubar_A (even-polynomial fit of D_A/h^{2(A-1)} -> constant as h->0),
with a rational-reconstruction attempt.

STRICT anti-fit: 0 free params; words fixed by the topological Brunnian
constraint (delete-strand=identity, verified); mubar_A EXTRACTED, never fit to any
target; the 1.585x check is reported honestly with no tuning.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_COMP = _Path(__file__).resolve().parent.parent
for _d in ("hecke", "habiro", "substrate"):
    _p = str(_COMP / _d)
    if _p not in _sys.path:
        _sys.path.insert(0, _p)
_sys.path.insert(0, str(_COMP))
import _path_bridge  # noqa: E402, F401

import json  # noqa: E402
import time  # noqa: E402
import hashlib  # noqa: E402
import subprocess  # noqa: E402
from fractions import Fraction  # noqa: E402
from datetime import datetime, timezone  # noqa: E402

import mpmath as mp  # noqa: E402
import pyhecke_native  # noqa: E402

from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

DPS = 50
set_compute_dps(DPS)
mp.mp.dps = DPS
HERE = _Path(__file__).resolve().parent
_T0 = time.time()


def _log(m):
    print(f"[{time.time()-_T0:7.1f}s] {m}", flush=True)


# -- band / braid machinery (identical convention to a4 probe) -----------------
def sig(g):
    return [(+1, g)]


def sig_inv(g):
    return [(-1, g)]


def word_inv(word):
    return [(-s, g) for (s, g) in reversed(word)]


def band_to_sigma(i, j, e):
    assert i < j
    pre = []
    for k in range(j - 1, i, -1):
        pre += sig(k)
    core = sig(i) + sig(i)
    post = []
    for k in range(i + 1, j):
        post += sig_inv(k)
    w = pre + core + post
    return w if e > 0 else word_inv(w)


def band_word_to_sigma(bw):
    out = []
    for (i, j, e) in bw:
        out += band_to_sigma(i, j, e)
    return out


def band_inv(bw):
    return [(i, j, -e) for (i, j, e) in reversed(bw)]


def band_comm(a, b):
    return list(a) + list(b) + band_inv(a) + band_inv(b)


def delete_strand_band(bw, k):
    out = []
    for (i, j, e) in bw:
        if i == k or j == k:
            continue
        ii = i - 1 if i > k else i
        jj = j - 1 if j > k else j
        out.append((ii, jj, e))
    return out


def brunnian_word(A):
    """Left-normed band commutator on A strands: w_A = [[..[A01,A12]..],A_{A-2,A-1}]."""
    bands = [[(i, i + 1, +1)] for i in range(A - 1)]
    w = bands[0]
    for b in bands[1:]:
        w = band_comm(w, b)
    return w


# -- traces via mpfr Hoefsmit characters + canonical Wenzl weights -------------
def to_hecke_mpfr(sigma_word, h):
    """sig_g=(1,0,g); sig_g^-1=sig_g - h*I=(1,-h,g). Return (c_str,d_str,g+1) triples."""
    out = []
    one = mp.nstr(mp.mpf(1), DPS, strip_zeros=False)
    zero = mp.nstr(mp.mpf(0), DPS, strip_zeros=False)
    for (s, g) in sigma_word:
        if s > 0:
            out.append((one, zero, g + 1))
        else:
            out.append((one, mp.nstr(-h, DPS, strip_zeros=False), g + 1))
    return out


_YCACHE = {}


def y_weights(n, qv):
    key = (n, mp.nstr(qv, 30))
    if key not in _YCACHE:
        _YCACHE[key] = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
                        for k, v in y_lambda_at(n, qv).items()}
    return _YCACHE[key]


def traces(n, sigma_word, qv, h):
    Y = y_weights(n, qv)
    facs = to_hecke_mpfr(sigma_word, h)
    cp = pyhecke_native.chi_q_atomic_all_partitions_mpfr(n, facs, mp.nstr(qv, DPS), DPS)
    tr_s = mp.mpf(0)
    g_a = mp.mpf(0)
    for s, chi_str in cp:
        t = tuple(s)
        if t in Y:
            chi = mp.mpf(chi_str)
            tr_s += Y[t] * chi
            g_a += Y[t] * abs(chi)
    return tr_s, g_a


def deficits(n, sigma_word, qv):
    h = qv - 1 / qv
    tr_link, g_link = traces(n, sigma_word, qv, h)
    tr_un, g_un = traces(n, [], qv, h)
    d_signed = 1 - tr_link / tr_un
    d_abs = 1 - g_link / g_un
    return d_signed, d_abs, h


# -- leading order + leading coefficient extraction ----------------------------
_QGRID = [mp.mpf(s) for s in ("1.006", "1.010", "1.017", "1.028", "1.047", "1.079")]
# small-h grid for the Richardson refinement (q -> 1; leading-order regime)
_QSMALL = [mp.mpf(s) for s in ("1.002", "1.001", "1.0005", "1.00025")]


def fit_order_and_coeff(A, n, sigma_word, which):
    """Return (order_est, mubar_refined, mubar_raw). order via small-h log-log
    slope; mubar via Richardson (D/h^{2(A-1)} extrapolated h->0, error ~ a*h)."""
    idx = 0 if which == "signed" else 1
    k = 2 * (A - 1)
    small = [(deficits(n, sigma_word, qv)) for qv in _QSMALL]
    hs = [d[2] for d in small]
    Ds = [d[idx] for d in small]
    # leading order: log-log slope on the two smallest h
    order = mp.log(abs(Ds[-1]) / abs(Ds[-2])) / mp.log(hs[-1] / hs[-2])
    # mubar raw at smallest h, and linear-in-h Richardson on two smallest
    g = [Ds[i] / hs[i] ** k for i in range(len(small))]
    mubar_raw = g[-1]
    mubar_ref = (g[-1] * hs[-2] - g[-2] * hs[-1]) / (hs[-2] - hs[-1])
    return order, mubar_ref, mubar_raw


def rational_guess(x):
    for dmax in (2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128):
        fr = Fraction(float(x)).limit_denominator(dmax)
        if fr.denominator and abs(mp.mpf(fr.numerator) / fr.denominator - x) < mp.mpf('1e-10'):
            return f"{fr.numerator}/{fr.denominator}"
    return None


def main():
    print("=" * 90)
    print("Route C -- A=3..6 Brunnian trace-deficit leading order + leading coeff mubar_A")
    print(f"  dps={DPS}  (signed cyclic Markov tr_M  vs  abs perblock g)")
    print("=" * 90)

    results = {}
    mubar_signed = {}
    mubar_abs = {}
    for A in (3, 4, 5, 6):
        n = A
        w = brunnian_word(A)
        sw = band_word_to_sigma(w)
        _log(f"A={A}: band factors={len(w)}, sigma-word len={len(sw)}, n={n}")
        sub = {}
        brunnian_ok = True
        for kk in range(A):
            dbw = delete_strand_band(w, kk)
            ssw = band_word_to_sigma(dbw)
            if ssw:
                ds, da, _ = deficits(n - 1, ssw, mp.mpf("1.05"))
                sub[f"drop_{kk}"] = mp.nstr(ds, 6)
                if abs(ds) > mp.mpf("1e-30"):
                    brunnian_ok = False
            else:
                sub[f"drop_{kk}"] = "0"
        _log(f"  Brunnian delete-strand (signed, must be ~0): {sub}  ok={brunnian_ok}")

        o_s, c_s, raw_s = fit_order_and_coeff(A, n, sw, "signed")
        o_a, c_a, raw_a = fit_order_and_coeff(A, n, sw, "abs")
        expected = 2 * (A - 1)
        cand = mp.mpf(3) / 4 * (-2) ** (A - 3)   # candidate closed form
        rg_s = rational_guess(c_s)
        rg_a = rational_guess(c_a)
        mubar_signed[A] = c_s
        mubar_abs[A] = c_a
        relerr_s = abs(c_s - cand) / abs(cand)
        _log(f"  SIGNED tr_M : order~{mp.nstr(o_s,8)} (expect {expected})  "
             f"mubar_{A}={mp.nstr(c_s,12)}  ratl~{rg_s}  vs (3/4)(-2)^(A-3)"
             f"={mp.nstr(cand,6)} relerr={mp.nstr(relerr_s,3)}")
        _log(f"  ABS perblock: order~{mp.nstr(o_a,8)} (expect {expected})  "
             f"mubar_{A}={mp.nstr(c_a,12)}  ratl~{rg_a}")
        results[f"A{A}"] = {
            "n": n, "sigma_word_len": len(sw), "expected_order": expected,
            "brunnian_verified": bool(brunnian_ok),
            "delete_strand_signed": sub,
            "candidate_closed_form": "(3/4)*(-2)^(A-3)",
            "candidate_value": mp.nstr(cand, 12),
            "signed": {"order": mp.nstr(o_s, 8), "mubar_richardson": mp.nstr(c_s, 16),
                       "mubar_raw_smallest_h": mp.nstr(raw_s, 16),
                       "relerr_vs_candidate": mp.nstr(relerr_s, 6), "rational_guess": rg_s},
            "abs": {"order": mp.nstr(o_a, 8), "mubar_richardson": mp.nstr(c_a, 16),
                    "mubar_raw_smallest_h": mp.nstr(raw_a, 16), "rational_guess": rg_a},
        }

    print("\n" + "-" * 90)
    print("1.585x bridge check (honest yes/no, 0-fit):")
    TARGET = mp.mpf("1.585")
    bridge = {"target": "1.585 (~ log2(3))", "signed": {}, "abs": {}}
    for tag, mb in (("signed", mubar_signed), ("abs", mubar_abs)):
        ratios = {}
        hits = []
        for A in (4, 5, 6):
            if mb[A - 1] != 0:
                r = mb[A] / mb[A - 1]
                ratios[f"mubar{A}/mubar{A-1}"] = mp.nstr(r, 10)
                for name, val in (("r", r), ("|r|", abs(r)),
                                  ("1/r", 1 / r if r != 0 else mp.nan),
                                  ("1/|r|", 1 / abs(r) if r != 0 else mp.nan)):
                    if val == val and abs(abs(val) - TARGET) < mp.mpf("0.05"):
                        hits.append(f"A={A}:{name}={mp.nstr(val,8)}")
        info = {"consecutive_ratios": ratios, "near_1585_hits": hits,
                "verdict": ("no clean 1.585x encoding" if not hits
                            else "candidate near-1.585 ratio(s): " + "; ".join(hits))}
        bridge[tag] = info
        print(f"  [{tag}] consecutive mubar ratios: {ratios}")
        print(f"  [{tag}] near-1.585 hits: {hits or 'NONE'}")

    witness = {
        "schema": "witness/v1",
        "producer": "computations/deltalambda/milnor_exact_coefficient_probe.py",
        "computation": "milnor-exact-coefficient",
        "description": (
            "Route C of #4480: A=3..6 iterated-commutator Brunnian trace-deficit "
            "leading ORDER + leading COEFFICIENT mubar_A, in two trace conventions "
            "from the same Hoefsmit chi_lambda and canonical Wenzl y_lambda: SIGNED "
            "tr_M=sum y_lambda chi_lambda (genuine cyclic Markov trace / conv C) and "
            "ABS g=sum y_lambda|chi_lambda| (non-cyclic perblock, #4364/#4378). "
            "Deficit D_A=1-trace(w_A)/trace(unlink), h=q-q^-1; w_A = left-normed band "
            "commutator, Brunnian-verified by strand-forgetting d_k->identity. Leading "
            "order via log-log slope; mubar_A via even-poly fit of D_A/h^{2(A-1)} -> "
            "constant, with rational reconstruction. Also the 1.585x bridge check "
            "(honest yes/no). STRICT anti-fit: 0 free params, words fixed by the "
            "topological Brunnian constraint, mubar_A extracted not fit, nothing wired."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"free_parameters": 0, "dps": DPS,
                       "convention_note": "SIGNED = cyclic Markov (conv C); ABS = "
                                          "non-cyclic perblock (#4364/#4378)."},
        "results": {"per_A": results, "bridge_1585": bridge,
                    "mubar_signed": {str(A): mp.nstr(mubar_signed[A], 16) for A in (3, 4, 5, 6)},
                    "mubar_abs": {str(A): mp.nstr(mubar_abs[A], 16) for A in (3, 4, 5, 6)}},
        "scriptHash": hashlib.sha256(_Path(__file__).read_bytes()).hexdigest()[:16],
    }
    try:
        witness["scriptCommitSha"] = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", __file__], cwd=HERE, text=True).strip() or "uncommitted"
    except Exception:
        witness["scriptCommitSha"] = "uncommitted"
    out = HERE / "milnor-exact-coefficient.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    _log(f"witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
