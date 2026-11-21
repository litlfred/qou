#!/usr/bin/env python3
"""qbeta_gb_ordering_reversal_probe — PREREGISTRATION Addendum 7.

Reversed orderings for the state-level reduction count of W = X·β_Bor on V^{⊗4}:
R1 generator order (σ⁻¹ leading), R2 colour order (d < u), and both. Exact over ℚ(q); proton q₀;
CODATA only in the last section; nothing is selected by it.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
_BP = _ROOT / "computations/probes/beta_pair_creation_word"
for _p in (str(_ROOT / "computations"), str(_ROOT / "tools/qou-substrate/python"), str(_BP)):
    sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

import qou_substrate.constants as C  # noqa: E402
import beta_pair_creation_word_probe as BP  # noqa: E402
from hecke_exact import KF, h, q  # noqa: E402

mp.mp.dps = 60
N = 4
Q0 = mp.mpf(C.Q_50_DIGIT_STR)
ME = mp.mpf(C.M_E_MEV_STR)
E0 = ME / (Q0 * (Q0 - 1))
QK, HK = KF(q), KF(h)
FAILED: list = []
OUT: dict = {"preregistration": "PREREGISTRATION.md (Addendum 7)", "checks": [], "A": {}, "comparison": {}}


def check(name, ok, note=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    OUT["checks"].append({"name": name, "ok": bool(ok), "note": note})
    if not ok:
        FAILED.append(name)


def V(i):
    return (i, -(i + 1) - 1)


WORDS = {"V1^3": V(1) * 3, "V0V1V0V1": V(0) + V(1) + V(0) + V(1), "V1V0V1V0": V(1) + V(0) + V(1) + V(0)}


def R(b, i, r2):
    """Ř (r2: colours exchanged) on basis b: [(image, weight, is_branch)]."""
    a, c = b[i], b[i + 1]
    br = (0, 1) if r2 else (1, 0)          # the pair that branches
    if a == c:
        return [(b, QK, 0)]
    sw = list(b); sw[i], sw[i + 1] = c, a
    if (a, c) == br:
        return [(tuple(sw), KF.one, 0), (b, HK, 1)]
    return [(tuple(sw), KF.one, 0)]


def Rinv(b, i, r2):
    """Ř⁻¹ = Ř − h, written in its own normal form (the branch term is the −h on the other pair)."""
    a, c = b[i], b[i + 1]
    br = (0, 1) if r2 else (1, 0)
    if a == c:
        return [(b, 1 / QK, 0)]
    sw = list(b); sw[i], sw[i + 1] = c, a
    if (a, c) == br:
        return [(tuple(sw), KF.one, 0)]
    return [(tuple(sw), KF.one, 0), (b, -HK, 1)]


def gen_terms(b, i, inv, r1, r2):
    if isinstance(r1, tuple):
        r1 = r1[i]
    if not r1:          # σ leading: σ = Ř, σ⁻¹ = Ř − h (the −h is a firing)
        t = R(b, i, r2)
        return t + [(b, -HK, 1)] if inv else t
    # σ⁻¹ leading: σ⁻¹ = Ř⁻¹, σ = Ř⁻¹ + h (the +h is a firing)
    t = Rinv(b, i, r2)
    return t if inv else t + [(b, HK, 1)]


def apply_marked(vec, word, r1, r2):
    for g in reversed(word):
        i, inv = (g, False) if g >= 0 else (-g - 1, True)
        out: dict = {}
        for b, poly in vec.items():
            for img, wgt, f in gen_terms(b, i, inv, r1, r2):
                d = out.setdefault(img, {})
                for k, c in poly.items():
                    d[k + f] = d.get(k + f, KF.zero) + c * wgt
        vec = {b: {k: c for k, c in p.items() if c != 0} for b, p in out.items()}
        vec = {b: p for b, p in vec.items() if p}
    return vec


def out_pos(w, labels):
    final, _ = BP.strand_track(w)
    posv = [0] * N
    for s in range(N):
        posv[final[s]] = labels[s]
    return tuple(posv)


def block(w, ins, outs, r1, r2):
    tot: dict = {}
    for ib in ins:
        img = apply_marked({ib: {0: KF.one}}, w, r1, r2)
        for ob in outs:
            for k, c in img.get(out_pos(w, ob), {}).items():
                tot[k] = tot.get(k, KF.zero) + c
    return tot


def mean_k(E):
    e1 = sum(E.values(), KF.zero)
    d1 = sum((k * c for k, c in E.items()), KF.zero)
    return (d1 / e1) if e1 != 0 else None, e1


def ev(f):
    return BP.ev_frac(f, Q0) if f != 0 else mp.mpf(0)


NIN = [nb + (0,) for nb in BP.NUC_IN]
POUT = [pb + (1,) for pb in BP.NUC_OUT]
ORD = {"standard": (False, False), "R1": (True, False), "R2": (False, True), "R1+R2": (True, True)}

Aex: dict = {}
for name, X in WORDS.items():
    W = X + BP.BETA
    _, cc, rev = BP.analyse_element(BP.word_el(W))
    ccs = sum((e for r in cc for e in r), KF.zero)
    rvs = sum((e for r in rev for e in r), KF.zero)
    OUT["A"][name] = {}
    for o, (r1, r2) in ORD.items():
        Ef, Er = block(W, NIN, POUT, r1, r2), block(W, POUT, NIN, r1, r2)
        mf, ef = mean_k(Ef)
        mr, er = mean_k(Er)
        if not r2:
            check(f"{name} {o}: amplitudes (t = 1) unchanged by the marking", ef == ccs and er == rvs)
        A = mf - mr
        Aex[(name, o)] = A
        OUT["A"][name][o] = {"A_exact": BP.fx(A) if A != 0 else "0", "A_q0": mp.nstr(ev(A), 12),
                             "A_times_E0_MeV": mp.nstr(ev(A) * E0, 12),
                             "E_f1_q0": mp.nstr(ev(ef), 12), "E_r1_q0": mp.nstr(ev(er), 12)}
        print(f"  {name:9s} {o:9s} A = {mp.nstr(ev(A), 10):>14s}  A·E0 = {mp.nstr(ev(A) * E0, 10):>14s} MeV")

print("Preregistered tests")
for o in ORD:
    vals = [Aex[(n, o)] for n in WORDS]
    OUT[f"word_independent_{o}"] = all(v == vals[0] for v in vals)
    print(f"  {o:9s} word-independent: {OUT[f'word_independent_{o}']}")
for n in WORDS:
    OUT.setdefault("R2_is_minus_A", {})[n] = Aex[(n, "R2")] == -Aex[(n, "standard")]
    OUT.setdefault("R1_changes_A", {})[n] = Aex[(n, "R1")] != Aex[(n, "standard")]
print("  R2 maps A -> -A:", OUT["R2_is_minus_A"])
print("  R1 changes A:   ", OUT["R1_changes_A"])

print("Addendum 8(a): mean over the 8 per-generator orderings (colour order u < d)")
import itertools  # noqa: E402
Abar: dict = {}
for name, X in WORDS.items():
    W = X + BP.BETA
    vals = []
    for flags in itertools.product((False, True), repeat=3):
        mf, _ = mean_k(block(W, NIN, POUT, flags, False))
        mr, _ = mean_k(block(W, POUT, NIN, flags, False))
        vals.append(mf - mr)
    ab = sum(vals, KF.zero) / 8
    Abar[name] = ab
    vq = [ev(v) for v in vals]
    OUT.setdefault("A_mean8", {})[name] = {"exact": BP.fx(ab) if ab != 0 else "0", "q0": mp.nstr(ev(ab), 12),
                                           "times_E0_MeV": mp.nstr(ev(ab) * E0, 12),
                                           "spread_times_E0_MeV": mp.nstr((max(vq) - min(vq)) * E0, 12),
                                           "all8_times_E0_MeV": [mp.nstr(v * E0, 8) for v in vq]}
    print(f"  {name:9s} mean A·E0 = {mp.nstr(ev(ab) * E0, 10):>14s} MeV, spread·E0 = {mp.nstr((max(vq) - min(vq)) * E0, 8)}")
ab = list(Abar.values())
OUT["A_mean8_word_independent"] = all(v == ab[0] for v in ab)
print("  word-independent:", OUT["A_mean8_word_independent"])

print("Addendum 8(b): writhe of each W (colour frame q^(-w/N) is the identity iff w = 0)")
for name, X in WORDS.items():
    W = X + BP.BETA
    wr = sum(1 if g >= 0 else -1 for g in W)
    check(f"{name}: writhe(W) = 0", wr == 0, str(wr))

print("Comparison with CODATA (last; nothing selected)")
mn, mpp = mp.mpf(C.M_N_MEV_STR), mp.mpf(C.M_P_MEV_STR)
Qb = mn - mpp - ME
for (n, o), A in Aex.items():
    v = ev(A) * E0
    OUT["comparison"][f"{n}|{o}"] = {"A_E0_MeV": mp.nstr(v, 12), "abs_vs_Q_beta_pct": mp.nstr(100 * (abs(v) / Qb - 1), 6)}
for n, ab_ in Abar.items():
    v = ev(ab_) * E0
    OUT["comparison"][f"{n}|mean8"] = {"A_E0_MeV": mp.nstr(v, 12), "abs_vs_Q_beta_pct": mp.nstr(100 * (abs(v) / Qb - 1), 6)}
OUT["ok"] = not FAILED
(_HERE / "qbeta-gb-ordering-reversal.witness.json").write_text(json.dumps(OUT, indent=2, ensure_ascii=False) + "\n")
print(f"{len(OUT['checks']) - len(FAILED)}/{len(OUT['checks'])} checks passed")
sys.exit(1 if FAILED else 0)
