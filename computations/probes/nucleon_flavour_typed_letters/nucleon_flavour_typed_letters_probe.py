#!/usr/bin/env python3
"""Flavour-typed letters and a second flavour factor (beans qou-myts / qou-99qc).

Pre-registration: PREREGISTRATION.md (this directory).
Lean: QOU.Nuclear.NucleonFlavourTypedLetters (typed_V_pow_tau_ratio).

Exact sympy over Q(q) on H_3; exact Fraction on n = 6 at rational q; 80 dps at the proton q0.
No float64 computation.
"""
from __future__ import annotations

import itertools
import sys
import time
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps(80)
import mpmath as mp  # noqa: E402
from mpmath import mpf  # noqa: E402

mp.mp.dps = max(mp.mp.dps, 80)
import sympy as sp  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qbeta import qbeta_e0  # noqa: E402

T0 = time.time()
FAILED: list[str] = []


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name, ok, note=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""), flush=True)
    if not ok:
        FAILED.append(name)
    return bool(ok)


# ------------------------------------------------------------------ H_3 over Q(q)
q = sp.symbols("q", positive=True)
h = q - 1 / q
R = sp.zeros(4, 4)
R[0, 0] = q; R[3, 3] = q; R[2, 1] = 1; R[1, 2] = 1; R[2, 2] = h
Ri = R.inv().applyfunc(sp.simplify)
I2 = sp.eye(2)
kp = sp.kronecker_product
PUU = sp.diag(1, 0, 0, 0); PDD = sp.diag(0, 0, 0, 1); PM = sp.diag(0, 1, 1, 0)
K = sp.diag(q, 1 / q)
K3 = kp(K, kp(K, K))


def sig(s, corr):
    f = q ** (-2 * s) if corr else 1
    return f * (R if s == 1 else Ri)


def typed(eps, corr):
    return PUU * sig(eps, corr) + PDD * sig(-eps, corr) + PM * (sig(1, corr) + sig(-1, corr)) / 2


def plain_letter(kind, corr):
    """Hand-placed quark letter: 'u' = sigma, 'd' = sigma^-1, 'm' = average (census recipe)."""
    if kind == "u":
        return sig(1, corr)
    if kind == "d":
        return sig(-1, corr)
    return (sig(1, corr) + sig(-1, corr)) / 2


def gen(g, M):
    return kp(M, I2) if g == 0 else kp(I2, M)


ND = lambda i: bin(i).count("1")  # noqa: E731
WP = [i for i in range(8) if ND(i) == 1]
WN = [i for i in range(8) if ND(i) == 2]


def ratio3(X):
    Y = K3 * X
    tp = sp.simplify(sum(Y[i, i] for i in WP))
    tn = sp.simplify(sum(Y[i, i] for i in WN))
    return sp.factor(sp.simplify(tp / tn))


def exponent_at(r, q0):
    v = mpf(sp.N(r.subs(q, sp.Rational(str(q0))), 90)) if not isinstance(r, mpf) else r
    if v <= 0:
        return None, v
    return mp.log(v) / mp.log(q0), v


def part1():
    log("1. typed gamma-gamma words V^k on H_3 (exact over Q(q))")
    rows = {}
    ok = True
    for corr in (False, True):
        V = gen(0, typed(1, corr)) * gen(1, typed(-1, corr))
        X = sp.eye(8)
        for k in range(1, 7):
            X = X * V
            r = ratio3(X)
            good = sp.simplify(r - q**2) == 0
            ok &= good
            rows[f"{'corr' if corr else 'raw'}_V^{k}"] = str(r)
    check("typed_V_pow_ratio_q2_raw_and_corrected_k1_to_6", ok)
    return rows, ok


def part1b():
    log("1b. widened gamma-gamma words (fork G2, Vbar = s0^-1 s1), measured not proved")
    V = [(0, 1), (1, -1)]
    Vb = [(0, -1), (1, 1)]
    words = {"Vbar^3": Vb * 3, "V Vbar": V + Vb, "(V Vbar)^2": (V + Vb) * 2,
             "V^2 Vbar": V * 2 + Vb, "V Vbar V": V + Vb + V}
    rows, ok = {}, True
    for name, w in words.items():
        for corr in (False, True):
            X = sp.eye(8)
            for g, e in w:
                X = X * gen(g, typed(e, corr))
            r = ratio3(X)
            ok &= sp.simplify(r - q**2) == 0
            rows[f"{name} {'corr' if corr else 'raw'}"] = str(r)
    check("widened_G2_words_ratio_q2", ok)
    return rows, ok


def part3(q0):
    log("3. hand-placed extra typed letters on V^3")
    out = {}
    V3 = (gen(0, sig(1, False)) * gen(1, sig(-1, False))) ** 3   # writhe 0: same in both readings
    single = {}
    for corr in (False, True):
        for g in (0, 1):
            Xp = V3 * gen(g, typed(1, corr))
            r = ratio3(Xp)
            e, _ = exponent_at(r, q0)
            single[f"{'corr' if corr else 'raw'}_gen{g}"] = {"ratio": str(r), "exponent_q0": fmt(e) if e is not None else "non-positive"}
    out["single_typed_letter_after_V3"] = single
    bare = {}
    for corr in (False, True):
        r = ratio3(gen(0, typed(1, corr)))
        e, _ = exponent_at(r, q0)
        bare["corr" if corr else "raw"] = {"ratio": str(r), "exponent_q0": fmt(e)}
    out["single_typed_letter_bare"] = bare
    check("bare_typed_letter_raw_is_q4", sp.simplify(ratio3(gen(0, typed(1, False))) - q**4) == 0)
    census = {"raw": [], "corr": []}
    pk = {"p": ["u", "m", "m"], "n": ["d", "m", "m"]}
    for gens in itertools.product([0, 1], repeat=3):
        for perm in sorted(set(itertools.permutations(range(3)))):
            for corr in (False, True):
                T = {}
                for c in "pn":
                    F = sp.eye(8)
                    for k in perm:
                        F = F * gen(gens[k], plain_letter(pk[c][k], corr))
                    Y = K3 * V3 * F
                    W = WP if c == "p" else WN
                    T[c] = sp.simplify(sum(Y[i, i] for i in W))
                r = sp.simplify(T["p"] / T["n"])
                e, v = exponent_at(r, q0)
                census["corr" if corr else "raw"].append({"gens": list(gens), "order": list(perm), "exponent_q0": fmt(e) if e is not None else f"non-positive ratio {fmt(v)}"})
    for key in ("raw", "corr"):
        vals = [mpf(x["exponent_q0"]) for x in census[key] if not x["exponent_q0"].startswith("non")]
        out[f"census_{key}_exponent_min"] = fmt(min(vals))
        out[f"census_{key}_exponent_max"] = fmt(max(vals))
        out[f"census_{key}_n_distinct"] = len(set(x["exponent_q0"] for x in census[key]))
    out["census_rows"] = census
    return out


# ------------------------------------------------------------------ n = 6 exact at rational q
def ratio6(qv: Fraction, word, corr, typed_letters=True):
    hq = qv - 1 / qv

    def Rop(s):
        if s == 1:
            return {(0, 0): {(0, 0): qv}, (1, 1): {(1, 1): qv}, (0, 1): {(1, 0): Fraction(1)},
                    (1, 0): {(0, 1): Fraction(1), (1, 0): hq}}
        return {(0, 0): {(0, 0): 1 / qv}, (1, 1): {(1, 1): 1 / qv}, (1, 0): {(0, 1): Fraction(1)},
                (0, 1): {(1, 0): Fraction(1), (0, 1): -hq}}

    def sg(s):
        f = qv ** (-2 * s) if corr else Fraction(1)
        return {k: {kk: v * f for kk, v in d.items()} for k, d in Rop(s).items()}

    def T(e):
        a, b = sg(1), sg(-1)
        out = {(0, 0): sg(e)[(0, 0)], (1, 1): sg(-e)[(1, 1)]}
        for k in ((0, 1), (1, 0)):
            d = {}
            for kk, v in a[k].items():
                d[kk] = d.get(kk, 0) + v / 2
            for kk, v in b[k].items():
                d[kk] = d.get(kk, 0) + v / 2
            out[k] = d
        return out

    ops = {1: T(1), -1: T(-1)}

    def apply(op, g, vec):
        out = {}
        for st, c in vec.items():
            for (a, b), coef in op[(st[g], st[g + 1])].items():
                ns = st[:g] + (a, b) + st[g + 2:]
                out[ns] = out.get(ns, 0) + c * coef
        return out

    tau = [Fraction(0), Fraction(0)]
    for st in itertools.product([0, 1], repeat=6):
        nd = sum(st[:3])
        if nd not in (1, 2):
            continue
        vec = {st: Fraction(1)}
        for g, e in reversed(word):
            vec = apply(ops[e], g, vec)
        kw = qv ** (st.count(0) - st.count(1))
        tau[nd - 1] += kw * vec.get(st, 0)
    return tau[0] / tau[1]


def part2():
    log("2. tower n = 6, leftmost block tagged (exact Fraction)")
    V3a = [(0, 1), (1, -1)] * 3
    V3b = [(3, 1), (4, -1)] * 3
    words = {
        "V3 (x) V3": V3a + V3b,
        "V3 s2 V3": V3a + [(2, 1)] + V3b,
        "V3 s2^-1 V3": V3a + [(2, -1)] + V3b,
        "V3 V(2,3) V3": V3a + [(2, 1), (3, -1)] + V3b,
    }
    rows = {}
    disjoint_ok = True
    for qs in ("11/10", "3/2"):
        qv = Fraction(qs)
        for name, w in words.items():
            for corr in (False, True):
                r = ratio6(qv, w, corr)
                e = mp.log(mpf(r.numerator) / mpf(r.denominator)) / mp.log(mpf(qv.numerator) / mpf(qv.denominator)) if r > 0 else None
                rows[f"q={qs} {name} {'corr' if corr else 'raw'}"] = {"ratio": f"{r.numerator}/{r.denominator}", "exponent": fmt(e) if e is not None else "non-positive"}
                if name == "V3 (x) V3":
                    disjoint_ok &= (r == qv ** 2)
    check("tower_n6_disjoint_typed_V3xV3_leftmost_q2", disjoint_ok)
    return rows, disjoint_ok


def main():
    q0 = mpf(q_at())
    M_E = mpf(_codata.codata("electron mass energy equivalent in MeV").value_str)
    E_ord0 = qbeta_e0.order_zero(q=q0, m_e=M_E)
    E_twr = qbeta_e0.canonical(q=q0, m_e=M_E)
    r1, ok1 = part1()
    r1b, ok1b = part1b()
    r2, ok2 = part2()
    r3 = part3(q0)
    lq = mp.log(q0)
    corr_single = mpf(r3["single_typed_letter_after_V3"]["corr_gen0"]["exponent_q0"])
    mev = {
        "cell_2E0logq_ord0": fmt(2 * E_ord0 * lq), "cell_2E0logq_tower": fmt(2 * E_twr * lq),
        "raw_single_letter_4E0logq_ord0": fmt(4 * E_ord0 * lq),
        "corr_single_letter_total_ord0": fmt(corr_single * E_ord0 * lq),
    }
    # comparison boundary (data enters only here)
    dm = mpf(_codata.codata("neutron mass energy equivalent in MeV").value_str) - mpf(_codata.codata("proton mass energy equivalent in MeV").value_str)
    comp = {"codata_mn_minus_mp": fmt(dm),
            "literature_quark_mass_part_GLR_2008.05806": "1.87(16)",
            "literature_quark_mass_part_BMW_1406.4088": "2.52"}
    for k, v in mev.items():
        log(f"  {k} = {mp.nstr(mpf(v), 10)} MeV")
    wb = WitnessBuilder("nucleon-flavour-typed-letters", engine="mpmath")
    wb.set_description("Flavour-typed letters (NucleonFlavourIsDetermined rule) on the gamma-gamma nucleon word, raw and framing-corrected traces: no second flavour factor.")
    wb.add_assertion("typed_V_pow_ratio_q2_raw_and_corrected", computed=bool(ok1), expected=True)
    wb.add_assertion("tower_n6_disjoint_typed_leftmost_q2", computed=bool(ok2), expected=True)
    wb.add_data("lean_module", "QOU.Nuclear.NucleonFlavourTypedLetters")
    wb.add_data("beans_referenced", ["qou-myts", "qou-99qc"])
    wb.add_data("q0_proton", fmt(q0))
    wb.add_data("E0_ord0", fmt(E_ord0)); wb.add_data("E0_tower", fmt(E_twr))
    wb.add_data("part1_typed_V_pow_ratios", r1)
    wb.add_data("part1b_widened_G2_words_measured", r1b)
    wb.add_data("part2_tower_n6", r2)
    wb.add_data("part3_hand_placed_letters", r3)
    wb.add_data("mev_proton_q0", mev)
    wb.add_data("comparison_only", comp)
    path = wb.save({"q0Anchor": "proton"})
    log(f"witness: {path}")
    log(f"FAILED: {FAILED}" if FAILED else "all checks passed")
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(main())
