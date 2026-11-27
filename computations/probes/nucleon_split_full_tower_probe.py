#!/usr/bin/env python3
"""Nucleon split on the full tower, all strands (beans qou-myts / qou-99qc).

Pre-registration: computations/probes/nucleon_split_full_tower/PREREGISTRATION.md.
Lean: QOU.Nuclear.NucleonSplitFullTower (markov_forces_K, strandWeight_flip, ...).

1. Re-derive the K-weight by solving the Markov equations for a general 2x2 K (sympy).
2. On n = 3, 6 strands, exact over Z[q, q^-1] (Laurent polynomials with Fraction
   coefficients): tau_p, tau_n summed over every colouring of all strands, tagged nucleon
   = each block (primary) and every 3-subset (secondary). Elements: V^3, all 58 six-strand
   gamma-gamma survivors, colour-weighted two-nucleon words, seeded random words.
3. n = 9 exact in Fraction at q = 11/10 and 3/2; and at the proton q0 in mpmath.
4. MeV: E * log(tau_p / tau_n) for both E0 forms; CODATA only at the end.

No float64 computation. Long runs print progress lines.
"""
from __future__ import annotations

import itertools
import json
import random
import sys
import time
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
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
M_E = mpf(_codata.codata("electron mass energy equivalent in MeV").value_str)
M_P_EXP = mpf(_codata.codata("proton mass energy equivalent in MeV").value_str)   # comparison
M_N_EXP = mpf(_codata.codata("neutron mass energy equivalent in MeV").value_str)   # comparison
DM_NP_EXP = M_N_EXP - M_P_EXP


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


# ------------------------------------------------------------- 1. Markov forces K (sympy)
def derive_K():
    q, a, b, c, d, z = sp.symbols("q a b c d z")
    h = q - 1 / q
    R = sp.zeros(4, 4)
    R[0, 0] = q; R[3, 3] = q; R[2, 1] = 1; R[1, 2] = 1; R[2, 2] = h
    K = sp.Matrix([[a, b], [c, d]])
    I2 = sp.eye(2)

    def ptr(M):
        return sp.Matrix(2, 2, lambda i, j: sum(M[2 * i + k, 2 * j + k] for k in range(2)))
    P = ptr(sp.kronecker_product(I2, K) * R)
    P1 = ptr(sp.kronecker_product(I2, K))
    sol = sp.solve(list(P - z * P1), [b, c, d, z], dict=True)
    right = {k.name: str(v) for k, v in sol[0].items()}
    M = sp.kronecker_product(K, I2) * R
    ML = sp.kronecker_product(K, I2)
    PL = sp.Matrix(2, 2, lambda i, j: sum(M[2 * k + i, 2 * k + j] for k in range(2)))
    PL1 = sp.Matrix(2, 2, lambda i, j: sum(ML[2 * k + i, 2 * k + j] for k in range(2)))
    soll = sp.solve(list(PL - z * PL1), [b, c, d, z], dict=True)
    left = {k.name: str(v) for k, v in soll[0].items()}
    return {"right_ptr": right, "left_ptr": left}


# ------------------------------------------------------------- Laurent polys over Q
class L:
    __slots__ = ("t",)

    def __init__(self, t=None):
        self.t = {k: v for k, v in (t or {}).items() if v != 0}

    @staticmethod
    def c(x, e=0):
        return L({e: Fraction(x)})

    def __add__(self, o):
        t = dict(self.t)
        for k, v in o.t.items():
            t[k] = t.get(k, 0) + v
        return L(t)

    def __sub__(self, o):
        return self + o.scale(-1)

    def scale(self, s):
        return L({k: v * s for k, v in self.t.items()})

    def __mul__(self, o):
        t = {}
        for k1, v1 in self.t.items():
            for k2, v2 in o.t.items():
                t[k1 + k2] = t.get(k1 + k2, 0) + v1 * v2
        return L(t)

    def shift(self, e):
        return L({k + e: v for k, v in self.t.items()})

    def __eq__(self, o):
        return self.t == o.t

    def iszero(self):
        return not self.t

    def ev(self, x):
        return sum((mpf(v.numerator) / v.denominator) * x ** k for k, v in self.t.items())

    def __repr__(self):
        return " + ".join(f"({v})q^{k}" for k, v in sorted(self.t.items())) or "0"


# ------------------------------------------------------------- generic ring ops
class Ring:
    """Coefficient ring: Laurent (exact in q) or a field value at a fixed q."""

    def __init__(self, kind, qv=None):
        self.kind = kind
        if kind == "laurent":
            self.zero, self.one = L(), L.c(1)
            self.q, self.qi = L.c(1, 1), L.c(1, -1)
        else:
            self.zero, self.one = (Fraction(0), Fraction(1)) if kind == "frac" else (mpf(0), mpf(1))
            self.q, self.qi = qv, 1 / qv
        self.h = self.q - self.qi

    def mul(self, a, b):
        return a * b

    def add(self, a, b):
        return a + b

    def iszero(self, a):
        return a.iszero() if self.kind == "laurent" else a == 0


def apply_letter(R, vec, gen, sign, lin=None):
    """vec: dict basis(tuple of 0/1) -> coeff. Letter sigma_gen^sign, or lin=(c,d) for c*sigma+d*1."""
    out = {}

    def put(b, v):
        if b in out:
            out[b] = R.add(out[b], v)
        else:
            out[b] = v
    for b, v in vec.items():
        x, y = b[gen], b[gen + 1]
        sw = b[:gen] + (y, x) + b[gen + 2:]
        if lin is not None:
            cc, dd = lin
            # c*sigma + d
            for bb, w in sigma_action(R, b, sw, x, y, 1):
                put(bb, R.mul(R.mul(v, w), cc))
            put(b, R.mul(v, dd))
            continue
        for bb, w in sigma_action(R, b, sw, x, y, sign):
            put(bb, R.mul(v, w))
    return {k: v for k, v in out.items() if not R.iszero(v)}


def sigma_action(R, b, sw, x, y, sign):
    if x == y:
        return [(b, R.q if sign > 0 else R.qi)]
    if sign > 0:
        if (x, y) == (0, 1):          # R(u d) = d u
            return [(sw, R.one)]
        return [(sw, R.one), (b, R.h)]  # R(d u) = u d + h d u
    if (x, y) == (0, 1):              # R^-1 = R - h: (u d) -> d u - h u d
        return [(sw, R.one), (b, R.zero - R.h)]
    return [(sw, R.one)]              # (d u) -> u d


def diag_entries(R, n, word):
    """<b|W|b> for every colouring b; word letters applied right to left."""
    res = {}
    for b in itertools.product((0, 1), repeat=n):
        vec = {b: R.one}
        for let in reversed(word):
            if let[0] == "lin":
                vec = apply_letter(R, vec, let[1], 1, lin=(let[2], let[3]))
            else:
                vec = apply_letter(R, vec, let[0], let[1])
            if not vec:
                break
        res[b] = vec.get(b, R.zero)
    return res


def kweight(R, b):
    """Forced K = q * diag(1, q^-2) = diag(q, q^-1)."""
    w = R.one
    for s in b:
        w = R.mul(w, R.q if s == 0 else R.qi)
    return w


def taus(R, n, diag, triples):
    """Per triple: tau_p, tau_n summed over every colouring of all n strands."""
    out = []
    for T in triples:
        tp, tn = R.zero, R.zero
        for b, v in diag.items():
            if R.iszero(v):
                continue
            nu = sum(1 for i in T if b[i] == 0)
            if nu == 2:
                tp = R.add(tp, R.mul(kweight(R, b), v))
            elif nu == 1:
                tn = R.add(tn, R.mul(kweight(R, b), v))
        out.append((T, tp, tn))
    return out


def blocks(n):
    return [tuple(range(3 * i, 3 * i + 3)) for i in range(n // 3)]


def core(off):
    return [(off, 1), (off + 1, -1)] * 3


def colour_letter(R, gen):
    """bring_color_weighted p-n interface: sigma - h(1/2 - delta/4), delta = flavor_split_leading."""
    q, qi = R.q, R.qi
    if R.kind == "laurent":
        delta = (q - R.one) * (q - R.one) * (R.one - qi * qi * qi * qi)
        delta = delta.scale(Fraction(1, 3))
        coef = R.h * (R.one.scale(Fraction(1, 2)) - delta.scale(Fraction(1, 4)))
        return ("lin", gen, R.one, R.zero - coef)
    delta = (q - 1) ** 2 * (1 - qi ** 4) / 3
    return ("lin", gen, R.one, -(R.h * (R.one / 2 - delta / 4)))


def check_word(R, n, word, label):
    diag = diag_entries(R, n, word)
    q2 = R.q * R.q
    prim = taus(R, n, diag, blocks(n))
    allT = taus(R, n, diag, list(itertools.combinations(range(n), 3)))

    def eqq2(tp, tn):
        return R.iszero(tp - q2 * tn)
    sp_, sn_ = R.zero, R.zero
    for _, tp, tn in prim:
        sp_, sn_ = sp_ + tp, sn_ + tn
    ap_, an_ = R.zero, R.zero
    for _, tp, tn in allT:
        ap_, an_ = ap_ + tp, an_ + tn
    per_block_ok = all(eqq2(tp, tn) for _, tp, tn in prim)
    per_triple = [eqq2(tp, tn) for _, tp, tn in allT]
    bad = [list(T) for (T, tp, tn), ok in zip(allT, per_triple) if not ok]
    return {
        "label": label, "n": n,
        "primary_sum_ratio_is_q2": eqq2(sp_, sn_), "primary_tau_n_zero": R.iszero(sn_),
        "every_block_ratio_is_q2": per_block_ok,
        "leftmost_block_ratio_is_q2": eqq2(prim[0][1], prim[0][2]),
        "per_block_ratio_is_q2": [eqq2(tp, tn) for _, tp, tn in prim],
        "all_triples_sum_ratio_is_q2": eqq2(ap_, an_),
        "triples_ratio_q2": sum(per_triple), "triples_total": len(per_triple),
        "triples_not_q2": bad[:20],
        "_sums": (sp_, sn_, ap_, an_),
    }


def main():
    out = {"K_derivation": derive_K()}
    log(f"Markov forces K: {out['K_derivation']}")
    kr, kl = out["K_derivation"]["right_ptr"], out["K_derivation"]["left_ptr"]
    ok = kr.get("d") == "a/q**2" and kr.get("z") == "q**3/(q**2 + 1)" and kl.get("d") == "a*q**2"

    surv = json.loads((HERE / "gg_six_strand" / "six-strand-neutral-selection.witness.json").read_text())
    surv = [[tuple(x) for x in r["reduced"]] for r in surv["rows"] if r["reading3_q0"]]
    rng = random.Random(20261127)

    def rand_word(n, L_):
        return [(rng.randrange(n - 1), rng.choice((1, -1))) for _ in range(L_)]

    RL = Ring("laurent")
    results = []
    # n = 3
    results.append(check_word(RL, 3, core(0), "V3"))
    for k in range(5):
        results.append(check_word(RL, 3, rand_word(3, 10), f"random3_{k}"))
    log("n=3 done")
    # n = 6
    results.append(check_word(RL, 6, core(0), "V3 (x) 1_3 spectators"))
    results.append(check_word(RL, 6, core(0) + core(3), "V3 (x) V3"))
    results.append(check_word(RL, 6, core(0) + [(2, 1)] + core(3), "V3 s2 V3 (pp-type interface)"))
    results.append(check_word(RL, 6, core(0) + [(2, -1)] + core(3), "V3 s2^-1 V3 (nn-type interface)"))
    results.append(check_word(RL, 6, core(0) + [colour_letter(RL, 2)] + core(3),
                              "V3 (s2 - h(1/2-delta/4)) V3 (colour-weighted pn interface)"))
    for i, w in enumerate(surv):
        results.append(check_word(RL, 6, w, f"six_strand_survivor_{i}"))
        if (i + 1) % 10 == 0:
            log(f"n=6 survivors {i + 1}/{len(surv)}")
    for k in range(5):
        results.append(check_word(RL, 6, rand_word(6, 14), f"random6_{k}"))
    log("n=6 done (exact over Z[q,q^-1])")

    # n = 9: exact at rational q, and at q0 in mpmath
    q0 = mpf(q_at())
    w9 = {
        "V3 V3 V3": core(0) + core(3) + core(6),
        "V3 s2 V3 s5^-1 V3": core(0) + [(2, 1)] + core(3) + [(5, -1)] + core(6),
        "random9_0": rand_word(9, 16),
        "random9_1": rand_word(9, 16),
    }
    n9 = []
    for qv, kind in ((Fraction(11, 10), "frac"), (Fraction(3, 2), "frac"), (q0, "mp")):
        R = Ring(kind, qv)
        for lab, w in w9.items():
            r = check_word(R, 9, w, f"{lab} @ q={qv if kind == 'frac' else 'q0'}")
            if kind == "mp":   # numeric: compare with tolerance at 80 dps
                sp_, sn_, ap_, an_ = r["_sums"]
                r["primary_sum_ratio_is_q2"] = bool(abs(sp_ / sn_ - q0 ** 2) < mpf(10) ** -60)
                r["all_triples_sum_ratio_is_q2"] = bool(abs(ap_ / an_ - q0 ** 2) < mpf(10) ** -60)
                r["every_block_ratio_is_q2"] = None
                r["triples_ratio_q2"] = None
                r["triples_not_q2"] = None
                r["ratio_minus_q2_primary"] = fmt(sp_ / sn_ - q0 ** 2)
            n9.append(r)
            log(f"n=9 {r['label']}: primary={r['primary_sum_ratio_is_q2']} "
                f"allT={r['all_triples_sum_ratio_is_q2']} triples_q2={r['triples_ratio_q2']}")

    # summary
    exact = results + [r for r in n9 if "q0" not in r["label"]]
    left_ok = all(r["leftmost_block_ratio_is_q2"] for r in exact)
    prim_ok = all(r["primary_sum_ratio_is_q2"] for r in results + n9)
    block_ok = all(r["every_block_ratio_is_q2"] for r in exact)
    allT_ok = all(r["all_triples_sum_ratio_is_q2"] for r in results + n9)
    nonq2_triple_words = [r["label"] for r in exact if r["triples_ratio_q2"] != r["triples_total"]]
    nonprim = [r["label"] for r in results + n9 if not r["primary_sum_ratio_is_q2"]]
    log(f"leftmost block ratio q^2 on every exact word: {left_ok}")
    log(f"primary (sum over blocks) q^2 on every word: {prim_ok} (fails on {len(nonprim)})")
    log(f"every block q^2: {block_ok}; all-triples sum q^2: {allT_ok}")
    log(f"words with some non-block triple != q^2: {len(nonq2_triple_words)}")
    ok &= left_ok

    # MeV at proton q0
    E_ord0 = qbeta_e0.order_zero(q=q0, m_e=M_E)
    E_twr = qbeta_e0.canonical(q=q0, m_e=M_E)
    lr = mp.log(q0 ** 2)
    mev = {
        "q0": fmt(q0), "E0_ord0": fmt(E_ord0), "E0_tower": fmt(E_twr),
        "split_ord0": fmt(E_ord0 * lr), "split_tower": fmt(E_twr * lr),
        "codata_dm_np_comparison_only": fmt(DM_NP_EXP),
        "gap_ord0": fmt(E_ord0 * lr / DM_NP_EXP - 1), "gap_tower": fmt(E_twr * lr / DM_NP_EXP - 1),
        "diagnostic_only_exponent_needed_ord0": fmt(DM_NP_EXP / (E_ord0 * mp.log(q0))),
        "diagnostic_only_exponent_needed_tower": fmt(DM_NP_EXP / (E_twr * mp.log(q0))),
    }
    for k, v in mev.items():
        log(f"{k} = {v[:20] if isinstance(v, str) else v}")

    # pre-registered primary observable per word at q0 (where it is not q^2)
    per_word = []
    for r in results + n9:
        if r["primary_sum_ratio_is_q2"]:
            continue
        sp_, sn_ = r["_sums"][0], r["_sums"][1]
        if "q0" in r["label"]:
            rat = sp_ / sn_
        elif "@" in r["label"]:
            continue
        else:
            rat = sp_.ev(q0) / sn_.ev(q0)
        row = {"label": r["label"], "n": r["n"], "tau_ratio_q0": fmt(rat),
               "effective_exponent": fmt(mp.log(abs(rat)) / mp.log(q0)) if rat != 0 else None,
               "ratio_positive": bool(rat > 0)}
        if rat > 0:
            row["split_ord0_MeV"] = fmt(E_ord0 * mp.log(rat))
            row["split_tower_MeV"] = fmt(E_twr * mp.log(rat))
        per_word.append(row)
    npos = sum(1 for r in per_word if r["ratio_positive"])
    exps = [mpf(r["effective_exponent"]) for r in per_word if r["ratio_positive"]]
    log(f"primary != q^2: {len(per_word)} words, ratio>0 on {npos}; effective exponent range "
        f"{mp.nstr(min(exps), 6) if exps else '-'} .. {mp.nstr(max(exps), 6) if exps else '-'}")
    for r in per_word:
        log(f"  {r['label'][:48]:48s} ratio={r['tau_ratio_q0'][:14]} exp={str(r['effective_exponent'])[:10]}")

    # V3 exact sums as a record
    v3 = results[0]["_sums"]
    for r in results + n9:
        r.pop("_sums", None)

    wb = WitnessBuilder("nucleon-split-full-tower", engine="mpmath")
    wb.set_description("Nucleon split on the full tower, all strands: Markov-forced K-weight; "
                       "tau_p/tau_n = q^2 at n = 3, 6 (exact over Z[q,q^-1]) and 9 (exact at "
                       "rational q, 80 dps at q0); Gibbs MeV for both E0 forms.")
    wb.add_assertion("markov_right_forces_K_zD_left_forces_inverse", computed=bool(kr.get("d") == "a/q**2" and kl.get("d") == "a*q**2"), expected=True)
    wb.add_assertion("leftmost_block_ratio_q2_every_exact_word", computed=bool(left_ok), expected=True)
    wb.add_data("primary_sum_over_blocks_ratio_q2_on_every_word", prim_ok)
    wb.add_data("every_block_ratio_q2_on_every_word", block_ok)
    wb.add_data("primary_not_q2_per_word_q0", per_word)
    wb.add_data("lean_module", "QOU.Nuclear.NucleonSplitFullTower")
    wb.add_data("beans_referenced", ["qou-myts", "qou-99qc"])
    wb.add_data("K_derivation_sympy", out["K_derivation"])
    wb.add_data("V3_tau_p_tau_n_n3", [repr(v3[0]), repr(v3[1])])
    wb.add_data("rows_exact_laurent", results)
    wb.add_data("rows_n9", n9)
    wb.add_data("all_triples_sum_ratio_q2", allT_ok)
    wb.add_data("words_with_a_non_block_triple_not_q2", nonq2_triple_words)
    wb.add_data("mev_proton_q0", mev)
    path = wb.save({"q0Anchor": "proton"})
    log(f"witness: {path}  ALL CHECKS {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
