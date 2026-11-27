#!/usr/bin/env python3
"""Route 1 test of BraidBoostInertialEquivalence (bean qou-2k68, owner choice 2026-11-25).

Definition under test (owner option 1):
    m_clock(beta) := 2 a_2 = 2 hbar_q^2 tau(reeb >> reeb),
the Reeb-clock kinetic coefficient of the categorical Lagrangian
(QOU.Core.CategoricalHamiltonianLegendre.trace_scaled_reeb_eq_lagrangianClock).
Under the Stokes hypothesis, reeb_holonomy_leftTrace_eq_functional_hol identifies
tau(reeb^2) with  casimir >> leftMul(hol w) >> frobeniusForm,  the Casimir-weighted
functional. Under a fibre functor to free modules that is the REGULAR trace of the
Hecke algebra (def:mass-identity, paragraph 3), sum_lambda f^lambda chi_lambda.

Target: m(beta) = (1+q^2)^n q^(-n-2w) tr_M(beta), tr_M the convention-D Markov trace
(z = q^3/(q^2+1)), sum_lambda y_lambda chi_lambda (def:mass-identity, braid classes).

PRE-REGISTERED PREDICTIONS (written before the first run):
  P1  ratio m_clock/m is not identically 1 as a rational function of q.
  P2  the ratio depends on beta (so no rescaling of the clock variable fixes it).
  P3  m_clock vanishes at q = 1 (double zero from hbar_q^2) while m(1) = 2^components > 0.

Exact arithmetic: sympy in Q(q); point values at the proton-pinned q0 via mpmath, 80 dps.
No float64 anywhere.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp
import mpmath as mp

mp.mp.dps = 80
q = sp.symbols("q", positive=True)
h = q - 1 / q
hbar = 1 - 1 / q
z = q**3 / (q**2 + 1)


def hecke_chars(n):
    """Irreducible characters on braid words via explicit seminormal matrices, n = 2, 3.

    Returns dict partition -> (dim f^lambda, generator matrices list)."""
    if n == 2:
        return {(2,): [sp.Matrix([[q]])], (1, 1): [sp.Matrix([[-1 / q]])]}
    if n == 3:
        # Two-dimensional irreducible of H_3 with eigenvalues q, -1/q (seminormal form).
        a = 1 / (q + 1 / q)  # = 1/[2]
        s1 = sp.Matrix([[q, 0], [0, -1 / q]])
        # s2 = conjugate seminormal: entries from axial distance 2 content
        c = 1 / (q**2 + 1 + q**-2)  # 1/[3] scaled; fixed below by verifying relations
        # Use the standard seminormal form: for axial distance d, diagonal entries
        # q^d/[d] - ... ; simpler: build s2 = P s1 P^-1 satisfying braid relation, solve.
        x, y = sp.symbols("x y")
        s2 = sp.Matrix([[x, y], [1, h - x]])  # trace h, det -1 => eigenvalues q, -1/q
        detc = sp.Eq(sp.simplify(x * (h - x) - y), -1)
        br = sp.simplify(s1 * s2 * s1 - s2 * s1 * s2)
        sol = sp.solve([detc, br[0, 0], br[0, 1]], [x, y], dict=True)
        sol = [s for s in sol if sp.simplify(s[x]) != q and sp.simplify(s[x]) != -1 / q]
        s = sol[0]
        s2 = s2.subs(s).applyfunc(sp.simplify)
        assert sp.simplify(s1 * s2 * s1 - s2 * s1 * s2) == sp.zeros(2)
        return {(3,): [sp.Matrix([[q]])] * 2, (2, 1): [s1, s2], (1, 1, 1): [sp.Matrix([[-1 / q]])] * 2}
    raise ValueError(n)


def word_char(mats, word):
    M = sp.eye(mats[0].shape[0])
    for g in word:
        i = abs(g) - 1
        M = M * (mats[i] if g > 0 else mats[i].inv())
    return sp.simplify(M.trace())


def markov_weights(n):
    """y_lambda for convention D from tr(1)=1, tr(sigma)=z (n=2); n=3 adds y_(1^3)=0
    (QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows) and tr(s1 s2)=z^2."""
    if n == 2:
        a, b = sp.symbols("a b")
        sol = sp.solve([a + b - 1, a * q - b / q - z], [a, b])
        return {(2,): sp.simplify(sol[a]), (1, 1): sp.simplify(sol[b])}
    if n == 3:
        a, b = sp.symbols("a b")
        ch = hecke_chars(3)
        # tr(1) = 1 with dims 1, 2 ; tr(s1) = z
        e1 = a * 1 + b * 2 - 1
        e2 = a * q + b * word_char(ch[(2, 1)], [1]) - z
        sol = sp.solve([e1, e2], [a, b])
        y = {(3,): sp.simplify(sol[a]), (2, 1): sp.simplify(sol[b]), (1, 1, 1): sp.Integer(0)}
        # consistency check: tr(s1 s2) = z^2 (Markov property)
        trs = y[(3,)] * q**2 + y[(2, 1)] * word_char(ch[(2, 1)], [1, 2])
        assert sp.simplify(trs - z**2) == 0, "Markov check failed"
        return y
    raise ValueError(n)


DIMS = {(2,): 1, (1, 1): 1, (3,): 1, (2, 1): 2, (1, 1, 1): 1}


def evaluate(n, word):
    ch = hecke_chars(n)
    y = markov_weights(n)
    chis = {lam: word_char(m, word) for lam, m in ch.items()}
    tr_M = sp.simplify(sum(y[l] * chis[l] for l in ch))
    tr_reg = sp.simplify(sum(DIMS[l] * chis[l] for l in ch))
    w = sum(1 if g > 0 else -1 for g in word)
    m_target = sp.simplify((1 + q**2) ** n * q ** (-n - 2 * w) * tr_M)
    m_clock = sp.simplify(2 * hbar**2 * tr_reg)
    ratio = sp.simplify(m_clock / m_target) if m_target != 0 else None
    return {"m_target": m_target, "m_clock": m_clock, "ratio": ratio, "tr_M": tr_M, "tr_reg": tr_reg}


def q0_proton():
    sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools/qou-substrate/python"))
    from qou_substrate.constants import Q_50_DIGIT_STR  # proton-pinned (owner directive 2026-08-07)
    return mp.mpf(Q_50_DIGIT_STR)


def main():
    q0 = q0_proton()
    cases = [(2, []), (2, [1]), (2, [1, 1]), (2, [1, 1, 1]), (2, [1, -1]),
             (3, [1, 2]), (3, [1, -2]), (3, [1, 2, 1]), (3, [1, -2, 1, -2, 1, -2])]
    rows, ratios = [], set()
    for n, word in cases:
        r = evaluate(n, word)
        at1 = {k: sp.limit(v, q, 1) for k, v in (("m_target", r["m_target"]), ("m_clock", r["m_clock"]))}
        num = lambda e: mp.nstr(mp.mpf(sp.N(e.subs(q, sp.Rational(str(q0))), 90)), 30)
        row = {
            "n": n, "word": word,
            "m_target": str(r["m_target"]), "m_clock": str(r["m_clock"]),
            "ratio": str(r["ratio"]),
            "m_target_at_q1": str(at1["m_target"]), "m_clock_at_q1": str(at1["m_clock"]),
            "ratio_at_q0": num(r["ratio"]) if r["ratio"] is not None else None,
        }
        rows.append(row)
        ratios.add(sp.simplify(r["ratio"]))
        print(n, word, "ratio =", row["ratio"], "| at q0:", row["ratio_at_q0"],
              "| m(1) =", row["m_target_at_q1"], "m_clock(1) =", row["m_clock_at_q1"])
    P1 = all(sp.simplify(rt - 1) != 0 for rt in ratios)
    P2 = len(ratios) > 1
    P3 = all(r["m_clock_at_q1"] == "0" and r["m_target_at_q1"] not in ("0",) for r in rows)
    print("P1 (ratio never identically 1):", P1)
    print("P2 (ratio braid-dependent):", P2, f"({len(ratios)} distinct ratios)")
    print("P3 (m_clock(1)=0, m(1)!=0):", P3)
    out = {
        "description": "qou-2k68 route 1: clock-Lagrangian inertial mass 2 hbar_q^2 tr_reg vs framed Markov mass",
        "q0Anchor": "proton", "workdps": 80, "q0Value": mp.nstr(q0, 50),
        "predictions": {"P1": P1, "P2": P2, "P3": P3},
        "rows": rows,
    }
    p = Path(__file__).with_name("braid-boost-inertial-clock.witness.json")
    p.write_text(json.dumps(out, indent=2) + "\n")
    print("wrote", p)


if __name__ == "__main__":
    main()
