#!/usr/bin/env python3
"""gamma_gamma_bond_markov_crosscheck_probe.py -- is the gamma-gamma probe's trace the
Markov trace at z_D, and does the overlap theorem explain its bond ratios?  (issue #8960)

## The question

`gamma_gamma_bond_is_pair_independent_probe.py` measured that the gamma-gamma bond ratio
mu = tr(W_atom)/tr(W_free) depends only on the SECOND nucleon, and its witness recorded
the mechanism as NOT established.  The block `prop:markov-trace-hecke-functional` proves,
sorry-free, for the Markov trace `towerTr z h` on the Hecke tower

    towerTr_gammaGammaBond :  tr(X * Y^3 * (V^3)^2) = tr X * tr(V^3 * Y^1),   X in H_2,

with V^3 = (sigma_0 sigma_1^-1)^3.  So mu = tr(V^3 Y^1)/tr Y, independent of the first
nucleon -- PROVIDED the probe's y_lambda-weighted H_6 trace is that Markov trace.

## What this computes

An independent Markov trace on H_6 in EXACT Fraction arithmetic at
q = Fraction(Q_50_DIGIT_STR) (proton pin), sigma^2 = h sigma + 1, h = q - 1/q,
fixed by tr 1 = 1, cyclicity and tr(x sigma_{n-1}) = z_D tr x, z_D = q^3/(q^2+1).
It is built on the T_w basis with coset representatives; it is NOT a line-by-line port
of the Lean `trWord`.  Both satisfy the Markov axioms, so they agree by
`QOU.BraidKnot.markovTrace_unique`.

It then (1) compares against the probe's own trace at 60 dps for all four pairs,
(2) checks the overlap identity mu = tr(V^3 Y^1)/tr Y EXACTLY (Fraction equality), and
(3) checks tr(W_free) = tr X * tr Y exactly.  The nucleon words are rebuilt here in
Fractions and compared letter by letter against the probe's `nucleon_block`, so the
two cannot silently drift apart.

Nothing is tuned: the words are the probe's, the trace is fixed by its axioms.
"""
import datetime
import json
import subprocess
import sys
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python",
           "computations/substrate", "computations/hecke", "computations",
           "computations/probes"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

import gamma_gamma_bond_is_pair_independent_probe as P  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

DPS = 60
mp.mp.dps = DPS
TOL = mp.mpf("1e-50")

q = F(Q_50_DIGIT_STR)
h = q - 1 / q
zD = q ** 3 / (q ** 2 + 1)
N = 6
ID = tuple(range(N))


def rmul_gen(el, i, c=F(1), d=F(0)):
    """el * (c sigma_i + d)"""
    out = {}
    for w, a in el.items():
        if d:
            out[w] = out.get(w, 0) + a*d
        ws = list(w); ws[i], ws[i+1] = ws[i+1], ws[i]; ws = tuple(ws)
        if w[i] < w[i+1]:
            out[ws] = out.get(ws, 0) + a*c
        else:
            out[ws] = out.get(ws, 0) + a*c
            out[w] = out.get(w, 0) + a*c*h
    return {k: v for k, v in out.items() if v}

def reduced_word(w):
    w = list(w); word = []
    # bubble sort from right: w = (product) ; collect s_i with w = w' s_i
    while True:
        for i in range(len(w)-1):
            if w[i] > w[i+1]:
                w[i], w[i+1] = w[i+1], w[i]; word.append(i); break
        else:
            break
    return word[::-1]   # w = s_{word[0]} ... s_{word[-1]}

@lru_cache(None)
def trT(w):
    n = len(w)
    while n > 1 and w[n-1] == n-1:
        n -= 1
    if n == 1:
        return F(1)
    w = w[:n]
    k = w.index(n-1)
    u = list(w); u.pop(k); u.append(n-1); u = tuple(u)
    # T_w = T_u s_{n-2} s_{n-3} ... s_k ; tr = z tr(Y T_u), Y = s_{n-3}..s_k
    el = {tuple(range(n)): F(1)}
    for g in range(n-3, k-1, -1):
        el = rmul_gen(el, g)
    for g in reduced_word(u):
        el = rmul_gen(el, g)
    return zD * sum(a*trT(x) for x, a in el.items())

def tr(el):
    return sum(a*trT(w) for w, a in el.items())

def word_el(word):
    el = {ID: F(1)}
    for c, d, g in word:
        el = rmul_gen(el, g, c, d)
    return el

def vertex_pow(i, k):
    w = []
    for _ in range(k):
        w += [(F(1), F(0), i), (F(1), -h, i+1)]
    return w

def nucleon(kind, off):
    g0, g1 = off, off+1; one, zero = F(1), F(0); w = []
    for _ in range(3):
        w += [(one, zero, g0), (one, -h, g1)]
    if kind == 'p':
        w += [(one, zero, g0), (one, -h/2, g0), (one, -h/2, g1)]
    else:
        w += [(one, -h/2, g0), (one, -h/2, g0), (one, -h, g1)]
    w += [(one, zero, g0), (one, zero, g0)]
    return w



def to_mpf(x: F):
    return mp.mpf(x.numerator) / x.denominator


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=_ROOT, capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        return ""


def main() -> int:
    a = []
    a.append(("tr(sigma_0) = tr(sigma_4) = z_D exactly",
              tr(word_el([(F(1), F(0), 0)])) == zD and tr(word_el([(F(1), F(0), 4)])) == zD))
    bor = tr(word_el(vertex_pow(0, 3)))
    a.append(("tr V^3 = (4 + h^2 - 3h^4 - h^6)/(h^2 + 4) exactly",
              bor == (4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4)))

    hm = mp.mpf(Q_50_DIGIT_STR) - 1 / mp.mpf(Q_50_DIGIT_STR)
    words_match = True
    for kind in "pn":
        for off in (0, 3):
            ex, pr = nucleon(kind, off), P.nucleon_block(kind, hm, off)
            words_match &= len(ex) == len(pr) and all(
                g == pg and abs(to_mpf(c) - pc) < TOL and abs(to_mpf(d) - pd) < TOL
                for (c, d, g), (pc, pd, pg) in zip(ex, pr))
    a.append(("nucleon words equal the probe's nucleon_block letter by letter", words_match))

    cache = P.BlockCacheMP(mp.mpf(Q_50_DIGIT_STR), hm)
    parts6 = [tuple(p) for p in P.partitions_of(6)]
    y6 = {tuple(k): mp.mpf(v) for k, v in P.y_lambda_su_n(6, mp.mpf(Q_50_DIGIT_STR), 2).items()}
    reps6 = {lam: P.seminormal_matrices_mp(lam, cache=cache) for lam in parts6}

    def tr_probe(w):
        return mp.fsum(y6[lam] * P.trace(P.word_image(reps6[lam][0], reps6[lam][1], w),
                                          reps6[lam][1]) for lam in parts6)

    bond_ex, bond_pr = vertex_pow(2, 3), P.vertex_pow(2, 3, hm)
    rows = {}
    worst = mp.mpf(0)
    for x in "pn":
        for y in "pn":
            wf = nucleon(x, 0) + nucleon(y, 3)
            tf, ta = tr(word_el(wf)), tr(word_el(wf + bond_ex))
            pf = tr_probe(P.nucleon_block(x, hm, 0) + P.nucleon_block(y, hm, 3))
            pa = tr_probe(P.nucleon_block(x, hm, 0) + P.nucleon_block(y, hm, 3) + bond_pr)
            df, da = abs(pf - to_mpf(tf)) / abs(to_mpf(tf)), abs(pa - to_mpf(ta)) / abs(to_mpf(ta))
            worst = max(worst, df, da)
            Y, Y1 = nucleon(y, 0), nucleon(y, 1)
            pred = tr(word_el(vertex_pow(0, 3) + Y1)) / tr(word_el(Y))
            rows[x + y] = {
                "tr_free_exact": mp.nstr(to_mpf(tf), 30),
                "tr_atom_exact": mp.nstr(to_mpf(ta), 30),
                "mu_exact": mp.nstr(to_mpf(ta / tf), 30),
                "rel_dev_probe_free": mp.nstr(df, 3),
                "rel_dev_probe_atom": mp.nstr(da, 3),
                "overlap_identity_exact": bool(pred == ta / tf),
                "free_factorizes_exact": bool(tf == tr(word_el(nucleon(x, 0))) * tr(word_el(Y))),
            }
    a.append(("probe trace = exact Markov trace at z_D (all pairs, rel < 1e-50)", worst < TOL))
    a.append(("mu = tr(V^3 Y^1)/tr Y exactly, all pairs",
              all(r["overlap_identity_exact"] for r in rows.values())))
    a.append(("tr(W_free) = tr X * tr Y exactly, all pairs",
              all(r["free_factorizes_exact"] for r in rows.values())))

    ok = True
    for name, passed in a:
        ok &= bool(passed)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
    for k, r in rows.items():
        print(f"  {k}: mu = {r['mu_exact']}  dev free/atom = {r['rel_dev_probe_free']} / {r['rel_dev_probe_atom']}")

    w = {
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "fractions+mpmath",
        "scriptFile": Path(__file__).name,
        "commitSha": _head_sha(),
        "q0Anchor": "proton",
        "q0AnchorReason": "Fraction(Q_50_DIGIT_STR); convention D (z = q^3/(q^2+1))",
        "description": (
            "Independent exact Markov trace at z_D on H_6 against the gamma-gamma probe's "
            "y_lambda-weighted trace, and an exact check of the overlap identity "
            "mu = tr(V^3 Y^1)/tr Y proved as towerTr_gammaGammaBond. Not a line-by-line "
            "port of the Lean trWord; agreement with it follows from markovTrace_unique."
        ),
        "dps": DPS,
        "q0": Q_50_DIGIT_STR,
        "tr_V3_exact": mp.nstr(to_mpf(bor), 30),
        "worst_rel_dev_probe_vs_exact": mp.nstr(worst, 3),
        "pairs": rows,
        "assertions": [{"name": n, "passed": bool(p)} for n, p in a],
        "allPassed": bool(ok),
    }
    out = Path(__file__).with_name("gamma-gamma-bond-markov-crosscheck.witness.json")
    out.write_text(json.dumps(w, indent=1) + "\n")
    print(f"  witness -> {out.relative_to(_ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
