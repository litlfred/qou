#!/usr/bin/env python3
"""binding_ceiling_q0_probe.py — does the classical merge ceiling survive the q-deformation?

Bean `qou-brng` (brief C2, epic `qou-myts`), part 2 of PR #9467. Question (open item 1 of
`docs/audits/2026-11-27-classical-log-binding-cycle-count.md`): on the six-strand deuteron with the
γγ nucleons V^3 (gens 0,1) and V^3 (gens 3,4), is

    -ln r(q0) <= ln 2 * (n - 1) = 5 ln 2      (n = 6 strands)

for every bond word that passes reading 3 at every level, and how does -ln r(q0) compare with the
classical merge count ln 2 * m, m = c(sigma_free) - c(sigma_atom)?

Population: every concatenation of vertices V(0)..V(3) of length 1..L that contains V(1) or V(2)
(5334 words for L = 6), the population of the corpus run `gg_deuteron_all_bonds_probe.py`
(PR #9426, branch claude/gg-deuteron-bond-20261125). Reading 3 is evaluated with the corpus
helpers (`../h2_one_rule`, `../h2_gg_atom`: seminormal basis, convention D, proton pin, 40 dps).
The trace ratio is computed a SECOND time with an independent Schur-Weyl trace on (C^2)^{(x)6}
(R-matrix with sigma - sigma^{-1} = h, quantum trace weight K = diag(q, 1/q), normalised by
[2]^n); the two must agree. Merges are exact integers from the underlying permutation.

Reading 3 selects. The ratio is reported, never used to select (ruling B, 2026-11-15). AME is not
read. Nothing fitted, selected against data, or wired. mpmath throughout, no float arithmetic.

-- Ref: [leitner2026] bean qou-brng; bean qou-ales; QOU.MassTheory.ClassicalLogBindingCycleCount
"""
from __future__ import annotations

import itertools
import sys
import time
from pathlib import Path

import mpmath as mp
mp.mp.dps = max(mp.mp.dps, 40)

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_one_rule"))
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
import h2_one_rule_probe as base  # noqa: E402
import h2_gg_atom_probe as gga  # noqa: E402

cf = base.cf
ONE, ZERO, TOL, y = base.ONE, base.ZERO, base.TOL, base.y
Q, H = cf.Q, cf.H
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

L = int(sys.argv[1]) if len(sys.argv) > 1 else 6
A = int(sys.argv[2]) if len(sys.argv) > 2 else 2   # nucleons; three strands each
N = 3 * A
JUNCTIONS = [{3 * j - 2, 3 * j - 1} for j in range(1, A)]   # V(s) crossing strand boundary 3j-1 | 3j
LN2 = mp.log(2)


# ---------------------------------------------------------------- corpus reading 3 (seminormal)
def corpus_letters(word):
    """word = list of (gen, inverse?) -> corpus letter list (coef, shift, gen): sigma^{-1} = sigma - h."""
    return [(ONE, -H if inv else ZERO, s) for (s, inv) in word]


def corpus_trace_and_pass(word):
    d = base.diag_of(corpus_letters(word), N)
    lc = gga.level_chars(d, N, 1)
    tr = mp.fsum(y(l) * lc[(N, l)] for l in base.two_row(N))
    ok = all(v >= -TOL for v in lc.values())
    return tr, ok


# ---------------------------------------------------------------- independent Schur-Weyl trace
def _rcheck(a, b):
    if a == b:
        return [((a, b), Q)]
    if (a, b) == (0, 1):
        return [((0, 1), H), ((1, 0), ONE)]
    return [((0, 1), ONE)]


def _apply(vec, s, inv):
    out = {}
    for st, c in vec.items():
        a, b = st[s], st[s + 1]
        terms = _rcheck(a, b)
        if inv:
            terms = terms + [((a, b), -H)]
        for (a2, b2), k in terms:
            ns = st[:s] + (a2, b2) + st[s + 2:]
            out[ns] = out.get(ns, ZERO) + c * k
    return out


def sw_trace(word):
    tot = ZERO
    for st in itertools.product((0, 1), repeat=N):
        v = {st: ONE}
        for (s, inv) in word:
            v = _apply(v, s, inv)
        if st in v:
            w = ONE
            for x in st:
                w *= Q if x == 0 else 1 / Q
            tot += w * v[st]
    return tot / (Q + 1 / Q) ** N


# ---------------------------------------------------------------- classical data
def V(s):
    return [(s, False), (s + 1, True)]


def perm(word):
    p = list(range(N))
    for (s, _) in word:
        p[s], p[s + 1] = p[s + 1], p[s]
    return p


def n_cycles(p):
    seen, c = set(), 0
    for i in range(len(p)):
        if i not in seen:
            c += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return c


def main() -> int:
    m_e = mp.mpf(str(M_E_MEV))
    hbar = 1 - 1 / Q
    E0_tower = m_e / (Q * (Q - 1) * (1 - hbar ** 2))
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        print(f"[{'PASS' if ok else 'FAIL'}] {name}", flush=True)

    x = [(s + 3 * a, i) for a in range(A) for (s, i) in V(0) * 3]
    trx_c, okx = corpus_trace_and_pass(x)
    trx_s = sw_trace(x)
    c_free = n_cycles(perm(x))
    check("K0_free_word_passes_and_traces_agree", okx and abs(trx_c - trx_s) < TOL and c_free == N,
          "corpus seminormal trace vs independent Schur-Weyl trace; V^3 is classically trivial")

    words = [w for n in range(1, L + 1) for w in itertools.product(range(N - 2), repeat=n)
             if all(J & set(w) for J in JUNCTIONS)]
    total = len(words)
    print(f"L={L}: {total} bond words", flush=True)
    t0, step = time.time(), max(1, total // 20)
    passing, max_dev = [], ZERO
    for k, w in enumerate(words, 1):
        K = [lt for s in w for lt in V(s)]
        tr_c, ok = corpus_trace_and_pass(x + K)
        if k % step == 0:
            el = time.time() - t0
            print(f"  {k}/{total} elapsed {el:.0f}s ETA {el / k * (total - k):.0f}s", flush=True)
        if not ok:
            continue
        tr_s = sw_trace(x + K)
        max_dev = max(max_dev, abs(tr_c - tr_s))
        r = tr_c / trx_c
        merges = c_free - n_cycles(perm(x + K))
        passing.append({"word": "".join(f"V{s}" for s in w), "length": len(w),
                        "pure_junction": set(w) <= set().union(*JUNCTIONS), "merges": merges,
                        "ratio": r, "minus_ln_r": -mp.log(r) if r > 0 else None})

    n_pass = len(passing)
    n_pure = sum(p["pure_junction"] for p in passing)
    check("K1_independent_trace_agrees_on_every_passing_word", max_dev < TOL,
          f"max |seminormal - Schur-Weyl| = {mp.nstr(max_dev, 5)}")
    if L == 6 and A == 2:
        check("K2_reproduces_corpus_count_408_of_5334_and_14_pure", (total, n_pass, n_pure) == (5334, 408, 14),
              "PR #9426 results.md Phase A table, V^3 row")
    check("K3_all_passing_ratios_positive", all(p["ratio"] > 0 for p in passing), "log law defined")

    ceiling = LN2 * (N - 1)
    by_m = {}
    for p in passing:
        by_m.setdefault(p["merges"], []).append(p)
    rows = {}
    for m_, ps in sorted(by_m.items()):
        vals = [p["minus_ln_r"] for p in ps]
        lo, hi = min(vals), max(vals)
        rows[m_] = {"n_words": len(ps), "n_pure_junction": sum(p["pure_junction"] for p in ps),
                    "classical_ln2_m": mp.nstr(LN2 * m_, 15),
                    "minus_ln_r_min": mp.nstr(lo, 15), "minus_ln_r_max": mp.nstr(hi, 15),
                    "min_word": min(ps, key=lambda p: p["minus_ln_r"])["word"],
                    "max_word": max(ps, key=lambda p: p["minus_ln_r"])["word"],
                    "n_above_classical": sum(v > LN2 * m_ for v in vals),
                    "n_above_ceiling": sum(v > ceiling for v in vals)}
        print(f"merges={m_}: {rows[m_]}", flush=True)
    n_over = sum(r["n_above_ceiling"] for r in rows.values())
    gmax = max(passing, key=lambda p: p["minus_ln_r"]) if passing else {"minus_ln_r": None, "word": None}
    print(f"max -ln r = {mp.nstr(gmax['minus_ln_r'], 15) if passing else None} ({gmax['word']}), "
          f"ceiling (n-1) ln2 = {mp.nstr(ceiling, 15)}; {n_over} passing words above the ceiling", flush=True)

    wb = (WitnessBuilder("binding-ceiling-q0" if A == 2 else f"binding-ceiling-q0-A{A}", engine="mpmath")
          .set_description(
              "PROBE (bean qou-brng, brief C2): the classical merge ceiling ln2*(n-1) of "
              "ClassicalLogBindingCycleCount tested at the proton-pin q0 on every gamma-gamma bond word of "
              f"1..{L} vertices on the {N}-strand A={A} word with V^3 nucleons (every junction bonded). Reading 3 selects (corpus "
              "seminormal helpers); the trace is recomputed with an independent Schur-Weyl trace. Ratio "
              "reported, never used to select. AME not read. Nothing fitted or wired.")
          .set_audit_only("docs/audits/2026-11-27-binding-ceiling-at-q0.md")
          .add_parameter("L", L).add_parameter("A", A).add_parameter("n_strands", N)
          .add_parameter("E0_tower_MeV", mp.nstr(E0_tower, 20))
          .add_data("summary", {"n_words": total, "n_pass": n_pass, "n_pure_junction_pass": n_pure,
                                "ceiling_ln2_n_minus_1": mp.nstr(ceiling, 20),
                                "max_minus_ln_r": mp.nstr(gmax["minus_ln_r"], 20) if passing else None, "max_word": gmax["word"],
                                "n_pass_above_ceiling": n_over,
                                "max_seminormal_vs_schur_weyl_dev": mp.nstr(max_dev, 5)})
          .add_data("by_merges", {str(k): v for k, v in rows.items()})
          .add_data("passing", [{**p, "ratio": mp.nstr(p["ratio"], 25),
                                 "minus_ln_r": mp.nstr(p["minus_ln_r"], 25)} for p in passing]))
    for name, ok, src in checks:
        wb.add_assertion(name, computed=ok, expected=True, tolerance=0, source=src)
    wb.save({"q0Anchor": "proton", "q0Value": mp.nstr(Q, 50),
             "q0AnchorReason": "q0 enters through cf.Q (committed y-lambda-at-q0 witness, proton pin)"})
    return 0 if all(ok for _, ok, _ in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
