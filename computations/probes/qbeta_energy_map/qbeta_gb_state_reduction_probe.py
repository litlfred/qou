#!/usr/bin/env python3
"""qbeta_gb_state_reduction_probe — PREREGISTRATION Addendum 6/6b.

State-level reduction counts for β-decay words W = X·β_Bor on V^{⊗4} (Jimbo Ř), placements B and C,
for the three G ∧ CC ∧ R3 words X ∈ {V₁³, V₀V₁V₀V₁, V₁V₀V₁V₀}; plus the element-level M1/M2/ΔM/M3
of Addenda 4–5 for each. Exact over ℚ(q); numbers by mpmath at the proton q₀. CODATA only in the
last section, as a comparison; nothing is selected by it.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
_BP = _ROOT / "computations/probes/beta_pair_creation_word"
for _p in (str(_ROOT / "computations"), str(_ROOT / "tools/qou-substrate/python"), str(_BP), str(_HERE)):
    sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

import qou_substrate.constants as C  # noqa: E402
import beta_pair_creation_word_probe as BP  # noqa: E402
from hecke_exact import H, KF, ONE, ZERO, RING, h, q  # noqa: E402

mp.mp.dps = 60
N = 4
Q0 = mp.mpf(C.Q_50_DIGIT_STR)
ME = mp.mpf(C.M_E_MEV_STR)
E0 = ME / (Q0 * (Q0 - 1))
QK, HK = KF(q), KF(h)
FAILED: list = []
OUT: dict = {"preregistration": "PREREGISTRATION.md (Addenda 6, 6b)", "checks": [], "words": {}, "comparison": {}}


def check(name, ok, note=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    OUT["checks"].append({"name": name, "ok": bool(ok), "note": note})
    if not ok:
        FAILED.append(name)


def V(i):
    return (i, -(i + 1) - 1)          # σ_i σ_{i+1}⁻¹


WORDS = {"V1^3": V(1) * 3, "V0V1V0V1": V(0) + V(1) + V(0) + V(1), "V1V0V1V0": V(1) + V(0) + V(1) + V(0)}


# ---------------------------------------------------------------- marked Jimbo action
def gen_terms(b, i, inv):
    """[(image, weight, firings)] for Ř_i (inv: Ř_i − h) on basis b."""
    a, bb = b[i], b[i + 1]
    if a == bb:
        t = [(b, QK, 0)]
    elif (a, bb) == (0, 1):
        sw = list(b); sw[i], sw[i + 1] = 1, 0
        t = [(tuple(sw), KF.one, 0)]
    else:
        sw = list(b); sw[i], sw[i + 1] = 0, 1
        t = [(tuple(sw), KF.one, 0), (b, HK, 1)]
    if inv:
        t.append((b, -HK, 1))
    return t


def apply_marked(vec, word):
    """vec: {basis: {deg: coeff}}; word applied right to left."""
    for g in reversed(word):
        i, inv = (g, False) if g >= 0 else (-g - 1, True)
        out: dict = {}
        for b, poly in vec.items():
            for img, wgt, f in gen_terms(b, i, inv):
                d = out.setdefault(img, {})
                for k, c in poly.items():
                    d[k + f] = d.get(k + f, KF.zero) + c * wgt
        vec = {b: {k: c for k, c in p.items() if c != 0} for b, p in out.items()}
        vec = {b: p for b, p in vec.items() if p}
    return vec


def apply_paths(vec, word):
    """Unweighted path counting: vec {basis: {deg: count}} over nonzero-weight edges."""
    for g in reversed(word):
        i, inv = (g, False) if g >= 0 else (-g - 1, True)
        out: dict = {}
        for b, poly in vec.items():
            for img, _w, f in gen_terms(b, i, inv):
                d = out.setdefault(img, {})
                for k, c in poly.items():
                    d[k + f] = d.get(k + f, 0) + c
        vec = out
    return vec


def out_pos(w, labels):
    final, _ = BP.strand_track(w)
    posv = [0] * N
    for s in range(N):
        posv[final[s]] = labels[s]
    return tuple(posv)


def block(w, ins, outs, marked=True):
    tot: dict = {}
    for ib in ins:
        img = (apply_marked if marked else apply_paths)({ib: {0: KF.one if marked else 1}}, w)
        for ob in outs:
            for k, c in img.get(out_pos(w, ob), {}).items():
                tot[k] = tot.get(k, KF.zero if marked else 0) + c
    return tot


def mean_k(E):
    e1 = sum(E.values(), KF.zero)
    d1 = sum((k * c for k, c in E.items()), KF.zero)
    return (d1 / e1) if e1 != 0 else None, e1


NIN_C = [nb + (0,) for nb in BP.NUC_IN]                      # n ⊗ ν, ν = u
NIN_B = [nb + (c,) for nb in BP.NUC_IN for c in (0, 1)]      # n ⊗ (either colour)
POUT = [pb + (1,) for pb in BP.NUC_OUT]                      # p ⊗ e⁻
NOUT_C = [nb + (0,) for nb in BP.NUC_IN]

# ---------------------------------------------------------------- element-level (Addenda 4–5)
HH = RING(h)


def plen(w):
    return sum(1 for a in range(len(w)) for b in range(a + 1, len(w)) if w[a] > w[b])


def reduce_count(word, left):
    fires, wt = 0, KF.zero
    x = H.one(N)
    seq = list(reversed(word)) if left else list(word)
    for g in seq:
        i, inv = (g, False) if g >= 0 else (-g - 1, True)
        d: dict = {}
        for w, v in x.c.items():
            if left:
                pi, pj = w.index(i), w.index(i + 1)
                ws = list(w); ws[pi], ws[pj] = i + 1, i
                desc = pi > pj
            else:
                ws = list(w); ws[i], ws[i + 1] = ws[i + 1], ws[i]
                desc = w[i] > w[i + 1]
            ws = tuple(ws)
            if inv:
                fires += 1; wt += 1 / QK ** (plen(w) + 1)
                d[w] = d.get(w, ZERO) - v * HH
            if desc:
                fires += 1; wt += 1 / QK ** (plen(w) + 1)
                d[w] = d.get(w, ZERO) + v * HH
            d[ws] = d.get(ws, ZERO) + v
        x = H(N, d)
    return x, fires, wt


def ev(f):
    return BP.ev_frac(f, Q0) if f != 0 else mp.mpf(0)


ROWS: dict = {}
for name, X in WORDS.items():
    print(f"== X = {name}")
    W = X + BP.BETA
    rec: dict = {"W": BP.word_str(W)}
    nf1, f1, w1 = reduce_count(W, False)
    nf2, f2, w2 = reduce_count(W, True)
    check(f"{name}: NF strategy-independent and equals reference",
          nf1.c == nf2.c == H.one(N).rmul_word(list(W)).c, f"{len(nf1.c)} terms")
    el = {}
    for tag, left in (("S1", False), ("S2", True)):
        _, fw, ww = reduce_count(W, left)
        _, fb, wb = reduce_count(BP.BETA, left)
        _, fx_, wx = reduce_count(X, left)
        el[tag] = {"M1": fw, "M2_q0": mp.nstr(ev(ww), 12), "dM1": fw - fb - fx_,
                   "dM2_exact": BP.fx(ww - wb - wx), "dM2_q0": mp.nstr(ev(ww - wb - wx), 12)}
        ROWS[f"{name}|{tag}|dM2xE0"] = ev(ww - wb - wx) * E0
        ROWS[f"{name}|{tag}|dM1xE0"] = (fw - fb - fx_) * E0
    rec["element"] = el
    _, cc, rev = BP.analyse_element(BP.word_el(W))
    # state level
    st = {}
    Ef = block(W, NIN_C, POUT)
    Er = block(W, POUT, NOUT_C)
    Ed = block(W, NIN_C, NOUT_C)
    EfB = block(W, NIN_B, POUT)
    check(f"{name}: E_f(1) equals analyse_element CC block sum",
          sum(Ef.values(), KF.zero) == sum((e for r in cc for e in r), KF.zero))
    check(f"{name}: E_r(1) equals analyse_element reverse block sum",
          sum(Er.values(), KF.zero) == sum((e for r in rev for e in r), KF.zero))
    for tag, E in (("C_forward", Ef), ("C_reverse", Er), ("C_diagonal", Ed), ("B_forward", EfB)):
        mk, e1 = mean_k(E)
        st[tag] = {"E1_exact": BP.fx(e1) if e1 != 0 else "0", "E1_q0": mp.nstr(ev(e1), 12),
                   "mean_k_exact": BP.fx(mk) if mk is not None else None,
                   "mean_k_q0": mp.nstr(ev(mk), 12) if mk is not None else None}
        if mk is not None:
            ROWS[f"{name}|{tag}|<k>xE0"] = ev(mk) * E0
        print(f"   {tag:11s} E(1) = {mp.nstr(ev(e1), 10):>14s}  <k> = {st[tag]['mean_k_q0']}")
    mf, _ = mean_k(Ef)
    mr, _ = mean_k(Er)
    if mf is not None and mr is not None:
        A = mf - mr
        st["A_exact"] = BP.fx(A) if A != 0 else "0"
        st["A_q0"] = mp.nstr(ev(A), 12)
        ROWS[f"{name}|C|AxE0"] = ev(A) * E0
        print(f"   asymmetry A = <k>_f - <k>_r = {st['A_q0']}  -> A*E0 = {mp.nstr(ev(A) * E0, 10)} MeV")
    for tag, ins, outs in (("C_forward", NIN_C, POUT), ("C_reverse", POUT, NOUT_C), ("B_forward", NIN_B, POUT)):
        P = block(W, ins, outs, marked=False)
        npaths = sum(P.values())
        F = sum(k * c for k, c in P.items())
        st[tag]["paths"] = npaths
        st[tag]["firings_over_paths"] = F
        if npaths:
            ROWS[f"{name}|{tag}|F/PxE0"] = mp.mpf(F) / npaths * E0
        print(f"   {tag:11s} paths = {npaths}, firings = {F}, F/P = {mp.nstr(mp.mpf(F) / npaths, 8) if npaths else '-'}")
    rec["state"] = st
    OUT["words"][name] = rec

# ---------------------------------------------------------------- comparison (last; nothing selected)
print("Comparison with CODATA (last; nothing selected)")
mn, mpp = mp.mpf(C.M_N_MEV_STR), mp.mpf(C.M_P_MEV_STR)
Qb, dnp = mn - mpp - ME, mn - mpp
cell = 2 * E0 * mp.log(Q0)
OUT["comparison"]["B_bound_cell_minus_me_MeV"] = mp.nstr(cell - ME, 12)
for k, v in ROWS.items():
    a, b = 100 * (v / Qb - 1), 100 * (v / dnp - 1)
    OUT["comparison"][k] = {"MeV": mp.nstr(v, 12), "vs_Q_beta_pct": mp.nstr(a, 6), "vs_mn_minus_mp_pct": mp.nstr(b, 6)}
    print(f"  {k:30s} {mp.nstr(v, 9):>14s} MeV  vs Q_β {mp.nstr(a, 5):>9s} %")
print(f"  B bound (cell - m_e) = {mp.nstr(cell - ME, 9)} MeV")
OUT["ok"] = not FAILED
(_HERE / "qbeta-gb-state-reduction.witness.json").write_text(json.dumps(OUT, indent=2, ensure_ascii=False) + "\n")
print(f"{len(OUT['checks']) - len(FAILED)}/{len(OUT['checks'])} checks passed")
sys.exit(1 if FAILED else 0)
