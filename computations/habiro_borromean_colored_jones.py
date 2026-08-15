#!/usr/bin/env python3
"""Habiro's cyclotomic formula for the colored Jones of the Borromean
rings — first corpus transcription.  Bean n920 (was deferred on PDF
access; source landed 2026-07-06 as library/arxiv-math-0508100v6/0508100v6.pdf).

Source (do NOT cite from memory — this is the verified transcription):
  Garoufalidis-Le, "Asymptotics of the colored Jones function of a
  knot", Geom. Topol. 15 (2011) 2135-2180, arXiv:math/0508100 v6,
  Appendix A (p. 26), quoting Habiro [Hab00 = RIMS Kokyuroku 1172;
  Hab08].  With {j} := q^{j/2} - q^{-j/2} and all three components
  colored n (normalized J_{B,1} = 1):

      J_{B,n}(q) = sum_{l=0}^{n-1} (-1)^l {n}^2
                   * ( prod_{j=1}^{l} {n+j}{n-j} )^3
                   / ( prod_{j=l+1}^{2l+1} {j} )^2

  The SQUARED denominator is confirmed by the appendix's own zero-count
  argument ("the denominator has 2 factors {n}" when 2l+1 > n).

Correctness anchors (all exact sympy, no fit):
  A1  J_{B,1} = 1.
  A2  bar-symmetry J_{B,n}(q) = J_{B,n}(q^{-1}) for n = 1..NMAX — the
      polynomial-level signature of the Borromean rings' amphichirality
      (same structural test the corpus's 4_1 transcription used).
  A3  independent cross-check at n = 2: J_{B,2} must equal the
      normalized Jones polynomial of the Borromean rings computed here
      from scratch via the Kauffman bracket / Temperley-Lieb algebra
      TL_3 on the 3-braid (sigma_1 sigma_2^{-1})^3 (writhe 0).  The TL
      computation shares NO code or formula with the Habiro sum.
  A4  each J_{B,n} is a genuine Laurent polynomial in q^{1/2} (the
      division is exact — sympy cancel leaves no denominator).

Context: the AJ conjecture for links is formulated-only (Sawabe 2024,
Hopf+Whitehead); NO Borromean recurrence ideal is published (see
docs/audits/2026-07-06-borromean-aj-literature-status.md).  This tower
is the input a future qZeilberger-style recurrence hunt needs.

Audit-only; no wiring.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

s = sp.symbols("s", positive=True)  # s = q^{1/2}


def brk(j: int):
    """{j} = s^j - s^{-j}."""
    return s**j - s ** (-j)


def habiro_borromean(n: int):
    """J_{B,n}(q) as a Laurent polynomial in s = q^{1/2} (exact)."""
    total = sp.Integer(0)
    for l in range(0, n):
        num = brk(n) ** 2 * sp.prod(
            [brk(n + j) * brk(n - j) for j in range(1, l + 1)]
        ) ** 3
        den = sp.prod([brk(j) for j in range(l + 1, 2 * l + 2)]) ** 2
        total += (-1) ** l * sp.cancel(sp.together(num / den))
    return sp.expand(sp.cancel(sp.together(total)))


# ── A3: independent TL_3 / Kauffman-bracket Jones of the Borromean rings ──
def jones_borromean_tl(A=None):
    """Normalized Jones polynomial of the closure of (s1 s2^{-1})^3 in B_3
    via the Temperley-Lieb algebra TL_3 (Kauffman bracket), writhe 0.

    TL_3 basis: {1, e1, e2, e1e2, e2e1} with e_i^2 = d e_i,
    e1 e2 e1 = e1, e2 e1 e2 = e2, d = -A^2 - A^{-2}.
    Braid generator: rho(s_i) = A + A^{-1} e_i (Kauffman).
    Markov closure trace on TL_3 basis elements: tr(x) = d^{c(x)-1}
    where c(x) = number of loops in the closure of the basis diagram:
    c(1) = 3, c(e1) = c(e2) = 2, c(e1e2) = c(e2e1) = 1 (closure of e_i
    in TL_3 gives 2 loops, closure of e1e2/e2e1 gives 1 loop).
    Normalized (divide by d^2 -> unknot = 1); Jones via A = q^{-1/4}
    (bar-ambiguity irrelevant here: the Borromean Jones is
    bar-symmetric, which A2' asserts explicitly).
    """
    if A is None:
        A = sp.symbols("A")
    d = -A**2 - A ** (-2)
    # basis order: 1, e1, e2, e12 (=e1e2), e21 (=e2e1)
    # multiplication table: left-multiply basis element by e1 / e2
    # e1*1=e1; e1*e1=d e1; e1*e2=e12; e1*e12=d e12; e1*e21=e1
    # e2*1=e2; e2*e1=e21; e2*e2=d e2; e2*e12=e2; e2*e21=d e21
    def lmul_e(i, vec):
        one, e1, e2, e12, e21 = vec
        if i == 1:
            return (
                sp.Integer(0),
                one + d * e1 + e21,
                sp.Integer(0),
                e2 + d * e12,
                sp.Integer(0),
            )
        return (
            sp.Integer(0),
            sp.Integer(0),
            one + d * e2 + e12,
            sp.Integer(0),
            e1 + d * e21,
        )

    def lmul_braid(i, inverse, vec):
        # rho(s_i) = A + A^{-1} e_i ; rho(s_i^{-1}) = A^{-1} + A e_i
        a, b = (A, 1 / A) if not inverse else (1 / A, A)
        evec = lmul_e(i, vec)
        return tuple(sp.expand(a * v + b * w) for v, w in zip(vec, evec))

    vec = (sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0),
           sp.Integer(0))
    for _ in range(3):  # (s1 s2^{-1})^3, applied left-to-right
        vec = lmul_braid(1, False, vec)
        vec = lmul_braid(2, True, vec)
    # closure trace: loop counts c = (3, 2, 2, 1, 1)  [n-strand closure of
    # identity = 3 loops; e_i closure = 2; e1e2 / e2e1 closure = 1]
    loops = (3, 2, 2, 1, 1)
    bracket = sum(v * d ** (c - 1) for v, c in zip(vec, loops))
    # writhe of (s1 s2^{-1})^3 is 0 => no framing factor.
    # normalize: divide by the 3-component unlink bracket... the closure
    # trace above already uses d^{c-1}; the UNKNOT (1-strand) normalizes
    # to 1, so the link invariant here is the Kauffman bracket normalized
    # so unknot = 1 (i.e. J~/[2]-style).  Habiro's J_{B,2} has the same
    # normalization (J~_L(2,2,2)/[2] with unknot -> 1).
    return sp.expand(sp.cancel(bracket))


def main() -> int:
    NMAX = 6
    print("\n  Habiro Borromean colored Jones (GL2011 Appendix A) — transcription\n")
    J = {n: habiro_borromean(n) for n in range(1, NMAX + 1)}

    # A1
    a1 = sp.simplify(J[1] - 1) == 0
    print(f"  [A1] J_B,1 = 1?  {a1}")

    # A2: bar symmetry (amphichirality)
    a2 = all(sp.simplify(J[n] - J[n].subs(s, 1 / s)) == 0
             for n in range(1, NMAX + 1))
    print(f"  [A2] J_B,n(q) = J_B,n(1/q) for n=1..{NMAX} (amphichiral)?  {a2}")

    # A4: Laurent polynomiality (division exact)
    a4 = all(sp.denom(sp.together(J[n])).as_base_exp()[0] in (s, sp.Integer(1))
             for n in range(1, NMAX + 1))
    print(f"  [A4] every J_B,n is Laurent in s (denominator a power of s)?  {a4}")

    # A3: TL_3 cross-check at n = 2 (fully independent computation)
    A = sp.symbols("A")
    V_tl = jones_borromean_tl(A)
    # Kauffman variable A = q^{-1/4} = s^{-1/2} (s is positive, so the
    # fractional powers of s simplify directly).
    V_in_s = sp.expand(sp.cancel(sp.together(V_tl.subs(A, s ** sp.Rational(-1, 2)))))
    diff = sp.cancel(sp.together(J[2] - V_in_s))
    a3 = diff.equals(0)
    # bar-ambiguity fallback: also try the mirror convention A -> s^{1/2}
    if not a3:
        V_in_s_m = sp.expand(sp.cancel(sp.together(V_tl.subs(A, s ** sp.Rational(1, 2)))))
        diff_m = sp.cancel(sp.together(J[2] - V_in_s_m))
        a3 = diff_m.equals(0)
    print(f"  [A3] J_B,2 == TL_3 Kauffman-bracket Jones of (s1 s2^-1)^3 closure?  {a3}")
    if not a3:
        print(f"       diff (direct convention): {diff}")

    print(f"\n  J_B,2 = {J[2]}")

    ok = a1 and a2 and a3 and a4
    script_path = Path(__file__)
    witness = {
        "engine": f"python {sys.version.split()[0]} / sympy {sp.__version__}",
        "scriptFile": f"computations/{script_path.name}",
        "commitSha": subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True,
            cwd=script_path.parent).stdout.strip(),
        "scriptHash": hashlib.sha256(
            script_path.read_bytes()).hexdigest()[:12],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Habiro cyclotomic formula for the Borromean colored Jones "
            "(diagonal colors), transcribed from GL2011 (arXiv:math/0508100 v6) "
            "Appendix A; anchored by exactness at n=1, bar-symmetry n<=6 "
            "(amphichirality), Laurent polynomiality, and an independent "
            "TL_3 Kauffman-bracket cross-check at n=2"
        ),
        "computation": "habiro-borromean-colored-jones",
        "audit_only": True,
        "source": {
            "pdf": "library/arxiv-math-0508100v6/0508100v6.pdf",
            "location": "Appendix A, p. 26 (Theorem A.1 proof)",
            "references": ["garoufalidis-le-2011", "habiro2000"],
        },
        "formula": (
            "J_{B,n}(q) = sum_{l=0}^{n-1} (-1)^l {n}^2 "
            "(prod_{j=1}^{l} {n+j}{n-j})^3 / (prod_{j=l+1}^{2l+1} {j})^2, "
            "{j} = q^{j/2} - q^{-j/2}"
        ),
        "assertions": {
            "A1_J1_eq_1": bool(a1),
            "A2_bar_symmetric_n_le_6": bool(a2),
            "A3_TL3_cross_check_n2": bool(a3),
            "A4_laurent_polynomial": bool(a4),
        },
        "J_B_2": str(J[2]),
        "all_ok": bool(ok),
    }
    out = Path(__file__).with_name("habiro-borromean-colored-jones.witness.json")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness → {out.name}\n  ALL OK: {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
