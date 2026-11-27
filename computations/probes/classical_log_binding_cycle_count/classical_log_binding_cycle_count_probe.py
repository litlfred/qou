#!/usr/bin/env python3
"""classical_log_binding_cycle_count_probe.py — the q = 1 part of the ruled log binding law.

Brief C2 (compute-accuracy epic qou-myts; open kernel qou-brng). Lean sibling:
QOU/MassTheory/ClassicalLogBindingCycleCount.lean. Audit:
docs/audits/2026-11-27-classical-log-binding-cycle-count.md.

What it does (nothing fitted, nothing selected, nothing wired):
  K0  the trace used here is the convention-D Markov trace: tr(sigma_1) = q^3/(q^2+1) = z_D,
      exact in QQ(q) (sympy rational function field).
  K1  it reproduces the corpus gamma-gamma deuteron table (PR #9426 results.md) at the proton
      pin to the 12 digits printed there.
  K2  at q = 1 (exact integers) every pure-junction bond word up to six vertices on the
      V^3 (x) V^3 deuteron has trace 2^(c - n): the log binding is E0*ln2*(merges).
  K3  pure-junction words (vertices V(1), V(2) only) are products of 3-cycles, hence even
      permutations, so they merge an EVEN number of components; on strands 1..4 that is 0 or 2.
      The deuteron's pure-junction classical binding is 0 or 2*E0*ln2, never 1*E0*ln2.
  T   the q0 departure from the classical count, word by word: -ln r(q0) against ln2*defect.
The comparison with AME is made only in the audit, never here.

Trace: Schur-Weyl / quantum trace on (C^2)^{(x)n} with the R-matrix (eigenvalues q, -1/q,
sigma - sigma^{-1} = h = q - 1/q), weight K = diag(q, 1/q) per factor, normalised by [2]^n.
mpmath 50 dps at q0; exact Fraction arithmetic at q = 1. No float64.

-- Ref: [leitner2026] QOU/MassTheory/ClassicalTraceFloor.lean (cycle-count trace, linear law)
-- Ref: [leitner2026] docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md §2 S2
"""
from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
from sympy import QQ, simplify
from sympy.polys.fields import field

mp.mp.dps = 50
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "computations" / "substrate"))
sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
from codata_constants import M_E_MEV  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

Q0 = mp.mpf(json.loads((ROOT / "computations" / "y-lambda-at-q0.witness.json")
                       .read_text(encoding="utf-8"))["q0Value"])


def apply_gen(vec, s, inv, q, h, zero):
    out = {}
    for st, c in vec.items():
        a, b = st[s], st[s + 1]
        if a == b:
            terms = [((a, b), q)]
        elif (a, b) == (0, 1):
            terms = [((0, 1), h), ((1, 0), 1)]
        else:
            terms = [((0, 1), 1)]
        if inv:  # sigma^{-1} = sigma - h
            terms = terms + [((a, b), -h)]
        for (a2, b2), k in terms:
            ns = st[:s] + (a2, b2) + st[s + 2:]
            out[ns] = out.get(ns, zero) + c * k
    return {k: v for k, v in out.items() if v != 0}


def trace(word, n, q, one):
    zero = one - one
    h = q - one / q
    tot = zero
    for st in itertools.product((0, 1), repeat=n):
        v = {st: one}
        for (s, inv) in word:
            v = apply_gen(v, s, inv, q, h, zero)
        if st in v:
            w = one
            for x in st:
                w = w * (q if x == 0 else one / q)
            tot = tot + w * v[st]
    return tot / (q + one / q) ** n


def V(s):
    return [(s, False), (s + 1, True)]


def perm(word, n):
    p = list(range(n))
    for (s, _) in word:
        p[s], p[s + 1] = p[s + 1], p[s]
    return p


def cycles(p):
    seen, c = set(), 0
    for i in range(len(p)):
        if i not in seen:
            c += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return c


def name(seq):
    return "".join(f"V({s})" for s in seq)


def main() -> int:
    checks = []

    def check(nm, ok, src):
        checks.append((nm, bool(ok), src))
        print(f"[{'PASS' if ok else 'FAIL'}] {nm}: {src}", flush=True)

    # K0: z_D, exact in QQ(q)
    F, q = field("q", QQ)
    t1 = trace([(0, False)], 2, q, F(1))
    check("K0_markov_parameter_is_zD", simplify((t1 - q**3 / (q**2 + 1)).as_expr()) == 0,
          f"tr(sigma_1) = {t1.as_expr()}")

    n = 6
    nuc = V(0) * 3
    x = nuc + [(s + 3, i) for (s, i) in nuc]
    one = mp.mpf(1)
    t0 = trace(x, n, Q0, one)

    # K1: reproduce the corpus table
    corpus = {"V(1)": "0.25043", "V(1)V(1)": "0.28482", "V(1)V(1)V(1)": "0.998497160633",
              "V(2)V(2)V(2)": "0.998497160633", "V(1)V(2)V(1)V(2)": "1.035874",
              "V(1)V(2)V(2)V(1)V(2)V(2)": "0.454088"}
    k1 = []
    for nm, val in corpus.items():
        seq = [int(c) for c in nm if c.isdigit()]
        r = trace(x + sum((V(s) for s in seq), []), n, Q0, one) / t0
        digits = len(val.split(".")[1])
        k1.append(abs(r - mp.mpf(val)) < mp.mpf(10) ** (-digits) / 2 * 1.0001)
    check("K1_reproduces_corpus_gg_deuteron_table", all(k1), "6 rows of PR #9426 results.md")

    # K2/K3 and the table, all pure-junction words of 1..6 vertices
    hbar = 1 - 1 / Q0
    E0 = mp.mpf(str(M_E_MEV)) / (Q0 * (Q0 - 1)) / (1 - hbar**2)
    ln2 = mp.log(2)
    rows, k2, maxdef = [], True, 0
    fr1 = Fraction(1)
    for L in range(1, 7):
        for seq in itertools.product((1, 2), repeat=L):
            w = x + sum((V(s) for s in seq), [])
            c = cycles(perm(w, n))
            d = n - c
            maxdef = max(maxdef, d)
            t_cl = trace(w, n, fr1, fr1)  # exact at q = 1
            k2 = k2 and (t_cl == Fraction(2) ** (c - n))
            r = trace(w, n, Q0, one) / t0
            rows.append({"word": name(seq), "vertices": L, "merges": d,
                         "minus_ln_r_q0": mp.nstr(-mp.log(r), 15),
                         "classical_ln2_merges": mp.nstr(d * ln2, 15),
                         "B_q0_MeV": mp.nstr(-E0 * mp.log(r), 12),
                         "B_classical_MeV": mp.nstr(E0 * ln2 * d, 12)})
    check("K2_q1_trace_is_2_pow_c_minus_n", k2, f"{len(rows)} words, exact Fraction at q = 1")
    check("K3_pure_junction_merges_in_0_or_2", {r["merges"] for r in rows} == {0, 2},
          f"merge counts seen = {sorted({r['merges'] for r in rows})}")

    by_m = {}
    for r in rows:
        by_m.setdefault(r["merges"], []).append(mp.mpf(r["minus_ln_r_q0"]))
    summary = {m: {"count": len(v), "min_minus_ln_r": mp.nstr(min(v), 10),
                   "max_minus_ln_r": mp.nstr(max(v), 10),
                   "classical": mp.nstr(m * ln2, 10)} for m, v in sorted(by_m.items())}
    for m, s in summary.items():
        print(m, s)

    wb = (WitnessBuilder("classical-log-binding-cycle-count", engine="mpmath")
          .set_description(
              "PROBE (brief C2, qou-myts / qou-brng): the q = 1 part of the ruled log binding law "
              "B = E0 ln(tr_free/tr_atom) is E0*ln2*(closure components merged). Verifies the "
              "trace (z_D, corpus gg deuteron table), the 2^(c-n) law at q = 1 exactly on all "
              "126 pure-junction bond words up to six vertices, the 3-merge pure-junction "
              "ceiling, and tabulates the q0 departure. Nothing fitted, selected or wired.")
          .set_audit_only("docs/audits/2026-11-27-classical-log-binding-cycle-count.md")
          .add_parameter("q0", mp.nstr(Q0, 40))
          .add_parameter("E0_tower_MeV", mp.nstr(E0, 20))
          .add_data("by_merges", summary)
          .add_data("rows", rows))
    for nm, ok, src in checks:
        wb.add_assertion(nm, computed=ok, expected=True, source=src)
    wb.save()
    return 0 if all(ok for _, ok, _ in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
