#!/usr/bin/env python3
"""he4_bond_both_nucleons_probe.py -- gamma-gamma bonds that enter BOTH nucleons
(issue #8960, item 3).  Preregistration: preregistration.md (written first).

The proved cases (MarkovTraceHeckeFunctional.lean): a bond on its own generators
gives a pair-independent factor (towerTr_interfaceWord); a bond overlapping only
the second nucleon gives mu = tr(B Y^1)/tr Y, so mu depends only on the second
nucleon (towerTr_overlapBond / towerTr_gammaGammaBond).  The remaining case is a
bond whose generators meet both {0,1} (nucleon 1) and {3,4} (nucleon 2).

Class: every product of 1..3 vertices sigma_i sigma_{i+1}^-1, i in {0,1,2,3}
(84 words, <= 6 letters).  All are computed; the "both" subclass is flagged.
For each word and each pair (pp, pn, np, nn): mu = tr(X Y^(3) B) / tr(X Y^(3)),
exact Fraction arithmetic, Markov trace at z_D = q^3/(q^2+1).

Evaluated at the proton pin q = Fraction(Q_50_DIGIT_STR) and at q = 1.
No float anywhere; mpmath only for printing.
"""
import datetime
import itertools
import json
import subprocess
import sys
import time
from fractions import Fraction as F
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
for _p in ("tools/qou-substrate/python", "computations"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 40
N = 6
ID = tuple(range(N))
NUC1, NUC2 = {0, 1}, {3, 4}


class Markov:
    """Exact Markov trace on H_N(q) at z_D (same construction as
    gamma_gamma_bond_markov_crosscheck_probe.py, parameterised by q)."""

    def __init__(self, q):
        self.q = q
        self.h = q - 1 / q
        self.z = q ** 3 / (q ** 2 + 1)
        self.cache = {}

    def rmul_gen(self, el, i, c=F(1), d=F(0)):
        out = {}
        h = self.h
        for w, a in el.items():
            if d:
                out[w] = out.get(w, 0) + a * d
            ws = list(w); ws[i], ws[i + 1] = ws[i + 1], ws[i]; ws = tuple(ws)
            out[ws] = out.get(ws, 0) + a * c
            if w[i] > w[i + 1]:
                out[w] = out.get(w, 0) + a * c * h
        return {k: v for k, v in out.items() if v}

    @staticmethod
    def reduced_word(w):
        w = list(w); word = []
        while True:
            for i in range(len(w) - 1):
                if w[i] > w[i + 1]:
                    w[i], w[i + 1] = w[i + 1], w[i]; word.append(i); break
            else:
                break
        return word[::-1]

    def trT(self, w):
        if w in self.cache:
            return self.cache[w]
        key = w
        n = len(w)
        while n > 1 and w[n - 1] == n - 1:
            n -= 1
        if n == 1:
            self.cache[key] = F(1)
            return F(1)
        w = w[:n]
        k = w.index(n - 1)
        u = list(w); u.pop(k); u.append(n - 1); u = tuple(u)
        el = {tuple(range(n)): F(1)}
        for g in range(n - 3, k - 1, -1):
            el = self.rmul_gen(el, g)
        for g in self.reduced_word(u):
            el = self.rmul_gen(el, g)
        val = self.z * sum(a * self.trT(x) for x, a in el.items())
        self.cache[key] = val
        return val

    def tr_word(self, word):
        el = {ID: F(1)}
        for c, d, g in word:
            el = self.rmul_gen(el, g, c, d)
        return sum(a * self.trT(w) for w, a in el.items())

    def nucleon(self, kind, off):
        """nucleon_block of gamma_gamma_bond_is_pair_independent_probe.py."""
        h = self.h
        g0, g1 = off, off + 1; one, zero = F(1), F(0); w = []
        for _ in range(3):
            w += [(one, zero, g0), (one, -h, g1)]
        if kind == "p":
            w += [(one, zero, g0), (one, -h / 2, g0), (one, -h / 2, g1)]
        else:
            w += [(one, -h / 2, g0), (one, -h / 2, g0), (one, -h, g1)]
        w += [(one, zero, g0), (one, zero, g0)]
        return w

    def bond(self, verts):
        w = []
        for i in verts:
            w += [(F(1), F(0), i), (F(1), -self.h, i + 1)]  # sigma_i sigma_{i+1}^-1
        return w


def gens(verts):
    return {g for i in verts for g in (i, i + 1)}


def classify(verts):
    s = gens(verts)
    a, b = bool(s & NUC1), bool(s & NUC2)
    return "both" if a and b else ("nuc1_only" if a else ("nuc2_only" if b else "interface_only"))


def pattern(mu):
    one = 1
    strong = mu["pn"] < one and mu["np"] < one and mu["pp"] > one and mu["nn"] > one
    weak = (mu["pn"] < one or mu["np"] < one) and mu["pp"] > one and mu["nn"] > one
    return strong, weak


def nstr(x):
    return mp.nstr(mp.mpf(x.numerator) / x.denominator, 15)


def run(q, label):
    M = Markov(q)
    t0 = time.time()
    free = {}
    for x, y in itertools.product("pn", repeat=2):
        free[x + y] = M.tr_word(M.nucleon(x, 0) + M.nucleon(y, 3))
    words = [v for k in (1, 2, 3) for v in itertools.product(range(4), repeat=k)]
    rows = []
    for idx, verts in enumerate(words):
        B = M.bond(verts)
        mu = {}
        for x, y in itertools.product("pn", repeat=2):
            ta = M.tr_word(M.nucleon(x, 0) + M.nucleon(y, 3) + B)
            mu[x + y] = ta / free[x + y]
        strong, weak = pattern(mu)
        rows.append({"verts": list(verts), "gens": sorted(gens(verts)),
                     "n_gap_letters": sum((i == 2) + (i + 1 == 2) for i in verts),
                     "class": classify(verts), "mu": mu,
                     "pattern": strong, "pattern_weak": weak})
        if idx % 10 == 0:
            print(f"  [{label}] word {idx+1}/84  elapsed {time.time()-t0:.1f}s", flush=True)
    return M, free, rows


def _head_sha():
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=_ROOT, capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        return ""


def main():
    q0 = F(Q_50_DIGIT_STR)
    _, free0, rows0 = run(q0, "q0")
    _, free1, rows1 = run(F(1), "q=1")

    checks = []
    # q = 1: all four mu equal for every word (p and n words coincide at h = 0)
    checks.append(("q=1: mu_pp = mu_pn = mu_np = mu_nn for every word",
                   all(len(set(r["mu"].values())) == 1 for r in rows1)))
    checks.append(("q=1: pattern holds for no word", not any(r["pattern_weak"] for r in rows1)))
    # Controls against the proved theorems at q0
    def factor(r):  # mu depends only on second nucleon?
        m = r["mu"]; return m["pp"] == m["np"] and m["pn"] == m["nn"]
    def factor1(r):  # depends only on first nucleon?
        m = r["mu"]; return m["pp"] == m["pn"] and m["np"] == m["nn"]
    checks.append(("q0: nuc2_only words: mu depends only on nucleon 2 (overlap theorem)",
                   all(factor(r) for r in rows0 if r["class"] == "nuc2_only")))
    checks.append(("q0: nuc1_only words: mu depends only on nucleon 1 (mirror control)",
                   all(factor1(r) for r in rows0 if r["class"] == "nuc1_only")))

    both0 = [r for r in rows0 if r["class"] == "both"]
    def cross(r):
        m = r["mu"]; return m["pp"] * m["nn"] == m["pn"] * m["np"]
    gap = [r for r in both0 if 2 not in r["gens"]]
    usesgap = [r for r in both0 if 2 in r["gens"]]
    checks.append(("q0: 'both' words avoiding generator 2: mu_pp*mu_nn = mu_pn*mu_np exactly "
                   "(towerTr_gapBond_crossRatio)", bool(gap) and all(cross(r) for r in gap)))
    n_cross_usesgap = sum(cross(r) for r in usesgap)
    single = [r for r in usesgap if r["n_gap_letters"] == 1]
    checks.append(("q0: 'both' words with ONE gap letter: cross-ratio identity exactly "
                   "(towerTr_singleGapBond_crossRatio)", bool(single) and all(cross(r) for r in single)))
    checks.append(("q0: every mu > 0 (so mu < 1 / mu > 1 is the binding test)",
                   all(v > 0 for r in rows0 for v in r["mu"].values())))
    nonfact = [r for r in usesgap if not cross(r)]
    for r in nonfact:
        r["cross_ratio_fails"] = True
    print("  words where the cross-ratio identity FAILS:",
          [(r["verts"], r["n_gap_letters"]) for r in nonfact])
    print(f"  'both' words using generator 2: {len(usesgap)}; cross-ratio identity holds for "
          f"{n_cross_usesgap}")
    n_strong = sum(r["pattern"] for r in both0)
    n_weak = sum(r["pattern_weak"] for r in both0)
    n_strong_all = sum(r["pattern"] for r in rows0)
    print(f"\n  'both' words: {len(both0)}; strong pattern {n_strong}; weak {n_weak}; "
          f"strong among all 84: {n_strong_all}")
    print("  verts         gens        mu_pp            mu_pn            mu_np            mu_nn")
    for r in both0:
        m = r["mu"]
        print(f"  {str(r['verts']):13s} {str(r['gens']):11s} " +
              " ".join(f"{nstr(m[k]):16s}" for k in ("pp", "pn", "np", "nn")) +
              ("  PATTERN" if r["pattern"] else ("  weak" if r["pattern_weak"] else "")))
    for n, p in checks:
        print(f"  [{'PASS' if p else 'FAIL'}] {n}")

    def ser(rows):
        return [{**{k: v for k, v in r.items() if k != "mu"},
                 "mu": {k: nstr(v) for k, v in r["mu"].items()},
                 "mu_gt_1": {k: bool(v > 1) for k, v in r["mu"].items()}} for r in rows]

    w = {
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "fractions",
        "scriptFile": Path(__file__).name,
        "commitSha": _head_sha(),
        "q0Anchor": "proton",
        "q0AnchorReason": "Fraction(Q_50_DIGIT_STR); convention D (z = q^3/(q^2+1))",
        "q0": Q_50_DIGIT_STR,
        "description": ("gamma-gamma bonds (products of 1..3 vertices sigma_i sigma_{i+1}^-1, "
                        "i in 0..3, 84 words) appended to X Y^(3) in H_6; mu = tr(atom)/tr(free) "
                        "for pp,pn,np,nn, exact Markov trace at z_D. Pattern = pn,np < 1 and "
                        "pp,nn > 1. Preregistered in preregistration.md."),
        "class_counts": {c: sum(r["class"] == c for r in rows0)
                         for c in ("both", "nuc1_only", "nuc2_only", "interface_only")},
        "pattern_count_both": n_strong,
        "pattern_weak_count_both": n_weak,
        "pattern_count_all": n_strong_all,
        "both_avoiding_gen2": len(gap),
        "both_using_gen2": len(usesgap),
        "cross_ratio_holds_among_using_gen2": n_cross_usesgap,
        "lean": ["QOU.BraidKnot.HeckeFunctional.towerTr_gapBond",
                 "QOU.BraidKnot.HeckeFunctional.towerTr_gapBond_crossRatio",
                 "QOU.BraidKnot.HeckeFunctional.towerTr_free_crossRatio",
                 "QOU.BraidKnot.HeckeFunctional.towerTr_singleGapBond",
                 "QOU.BraidKnot.HeckeFunctional.towerTr_singleGapBond_crossRatio",
                 "QOU.BraidKnot.HeckeFunctional.not_both_lt_one_of_crossRatio"],
        "non_factorising_words": [r["verts"] for r in nonfact],
        "tr_free_q0": {k: nstr(v) for k, v in free0.items()},
        "rows_q0": ser(rows0),
        "rows_q1": ser(rows1),
        "assertions": [{"name": n, "passed": bool(p)} for n, p in checks],
        "allPassed": all(p for _, p in checks),
    }
    out = Path(__file__).with_name("he4-bond-both-nucleons.witness.json")
    out.write_text(json.dumps(w, indent=1) + "\n")
    print(f"  witness -> {out}")
    return 0 if w["allPassed"] else 1


if __name__ == "__main__":
    sys.exit(main())
