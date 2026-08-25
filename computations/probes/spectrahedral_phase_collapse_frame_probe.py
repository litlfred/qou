#!/usr/bin/env python3
"""Is the supergolden "phase collapse" a threshold, or a convention-C artefact?

`prop:spectrahedral-phase-collapse` reads `det G(u) = 0` at `u = 1/psi`
(`psi^3 - psi^2 - 1 = 0`, the supergolden ratio) as a rank drop onto a strictly
lower-dimensional face of the Hecke spectrahedron.  Its Lean sibling proves
exactly that, over `QOU.Interactions.GramMatrixH3Symbolic.gramMatrix` -- the
**convention-C** Gram (`z = sqrt(q)/(q+1)`, i.e. `u/(u^2+1)` with `u = sqrt q`).

The owner ruling of 2026-08-15 makes convention D (`z = q^3/(q^2+1)`) canonical,
and `gramMatrixD_det_eq_zero` proves the D-frame determinant vanishes for EVERY
`q`.  So the question is not whether the C theorem is true -- it is -- but
whether its *reading* survives the canonical frame.  A vanishing point is a
threshold only if the determinant is non-zero somewhere else.

Two results, both exact:

1. **The C theorem has content, and the block understates it.**  On `u > 0` the
   determinant vanishes at exactly TWO points, not one: `u = 1/psi` (multiplicity
   5) and `u = 1`, i.e. `q = 1`, the classical limit (multiplicity 1).  The other
   two real roots of the factorisation are negative and so outside the regime.
   The substrate `u_0 = sqrt(q_0) = 1.0536` sits above both, in the `1 < u`
   region where `gramMatrix_det_ne_zero` applies -- consistent, no clash.

2. **The reading does not survive D.**  `det G_D(q) = 0` identically, recovered
   here from the parsed Lean entries independently of the Lean proof.  Under the
   canonical convention the supergolden hypothesis does no work: the determinant
   is zero there because it is zero everywhere.

Everything is EXACT over Q(u) / Q(q) -- the Gram entries are rational functions,
so nothing is approximated and no float enters the mathematics.  Determinants go
through `DomainMatrix` over the fraction field; the naive `Matrix.det()` on
rational-function entries exhausts memory on this 6x6.  The entries are PARSED
out of the committed `.lean` rather than retyped, so the probe tests the artefact
under review and cannot silently drift from it.
"""

from __future__ import annotations

import pathlib
import re
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
COMP = REPO / "computations"
for _p in (str(COMP), str(COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from witness_base import WitnessBuilder  # noqa: E402

LEAN_REL = (
    "content/quantum-observable-universe/lean/QOU/Interactions/GramMatrixH3Symbolic.lean"
)
ENTRY_RE = re.compile(r"^\s*\|\s*(\d)\s*,\s*(\d)\s*=>\s*(.+?)\s*$")


def parse_gram(text: str, defname: str, var: sp.Symbol) -> dict:
    """Read a `noncomputable def <defname> (v : R) : Fin 6 -> Fin 6 -> R` table."""
    lines = text.splitlines()
    start = next(
        i for i, l in enumerate(lines) if l.startswith(f"noncomputable def {defname} ")
    )
    cells: dict[tuple[int, int], sp.Expr] = {}
    buf = ""

    def flush(b: str) -> None:
        m = ENTRY_RE.match(b)
        cells[(int(m.group(1)), int(m.group(2)))] = sp.sympify(
            m.group(3).replace("^", "**"), locals={str(var): var}
        )

    for line in lines[start + 1 :]:
        if line.strip() and not line.startswith((" ", "\t", "|")):
            break
        if ENTRY_RE.match(line):
            if buf:
                flush(buf)
            buf = line
        elif buf and line.strip():
            buf += " " + line.strip()          # wrapped entry
        elif buf and not line.strip():
            flush(buf)
            buf = ""
    if buf:
        flush(buf)
    if len(cells) != 36:
        raise SystemExit(f"{defname}: parsed {len(cells)}/36 entries -- parser is wrong")
    return cells


def exact_det(cells: dict, var: sp.Symbol) -> sp.Expr:
    K = sp.QQ.frac_field(var)
    M = DomainMatrix(
        [[K.from_sympy(cells[(i, j)]) for j in range(6)] for i in range(6)], (6, 6), K
    )
    return sp.cancel(K.to_sympy(M.det()))


def main() -> int:
    text = (REPO / LEAN_REL).read_text(encoding="utf-8")
    u, q = sp.symbols("u q", positive=True)

    det_C = exact_det(parse_gram(text, "gramEntry", u), u)
    det_D = exact_det(parse_gram(text, "gramEntryD", q), q)

    num_C = sp.factor(sp.numer(sp.together(det_C)))
    supergolden = sp.Poly(u**3 + u - 1, u)          # u = 1/psi
    _, rem = sp.div(sp.Poly(sp.expand(sp.numer(sp.together(det_C))), u), supergolden, u)

    # Every positive real zero of the C determinant, from the factorisation.
    pos_zeros = sorted(
        {
            r
            for f, _m in sp.factor_list(num_C)[1]
            for r in sp.real_roots(sp.Poly(f, u))
            if sp.simplify(r > 0) == sp.true
        },
        key=float,
    )
    mults = {
        str(f.as_expr()): m
        for f, m in sp.factor_list(num_C)[1]
    }

    root_sg = sp.real_roots(u**3 + u - 1)[0]
    c_nonzero = sp.simplify(det_C) != 0
    d_zero = sp.simplify(det_D) == 0

    checks = [
        ("C_det_not_identically_zero", bool(c_nonzero), True,
         "a vanishing locus means something only if det is not always 0"),
        ("C_supergolden_divides_numerator", bool(rem.is_zero), True,
         "u^3 + u - 1 divides numer(det G_C) exactly -- the block's claim"),
        ("C_det_zero_at_supergolden_root", sp.simplify(det_C.subs(u, root_sg)) == 0, True,
         "cross-check by exact algebraic evaluation at the root itself"),
        ("C_supergolden_below_ne_zero_hypothesis",
         sp.simplify(root_sg < 1) == sp.true, True,
         "gramMatrix_det_ne_zero assumes 1 < u, so 1/psi < 1 means no clash"),
        ("C_has_exactly_two_positive_zeros", len(pos_zeros) == 2, True,
         "1/psi AND u = 1 (q = 1, classical limit) -- the block names only one"),
        ("D_det_identically_zero", bool(d_zero), True,
         "recovers QOU...gramMatrixD_det_eq_zero from the parsed entries"),
        ("phase_transition_reading_survives_D",
         bool(c_nonzero) and not bool(d_zero), False,
         "EXPECTED FALSE -- under D there is no distinguished point"),
    ]

    payload = {
        "description": (
            "Exact determinant of the H_3 Gram in both conventions, parsed from "
            "the committed Lean. Settles whether the supergolden 'phase collapse' "
            "is a real threshold (convention C: yes, and there is a second one at "
            "q = 1) or an artefact of a non-canonical frame (convention D: the "
            "determinant vanishes identically, so nothing is distinguished)."
        ),
        "conventionC": {
            "markov_weight": "z = u/(u^2 + 1),  u = sqrt(q)",
            "det_factored": sp.srepr(sp.factor(det_C)),
            "det_pretty": str(sp.factor(det_C)),
            "numerator_factor_multiplicities": mults,
            "positive_real_zeros": [str(sp.nsimplify(r)) for r in pos_zeros],
            "positive_real_zeros_note": (
                "u = 1/psi (supergolden, multiplicity 5) and u = 1 (q = 1, the "
                "classical limit, multiplicity 1). The factor (u^3 + u^2 + 1)^5 "
                "also has a real root, u = -psi, but it is negative and so lies "
                "outside the q > 0 regime."
            ),
        },
        "conventionD": {
            "markov_weight": "z = q^3/(q^2 + 1)",
            "det": str(det_D),
            "identically_zero": bool(d_zero),
        },
        "assertions": [
            {"name": n, "value": bool(got), "expected": bool(want), "passed": bool(got) is want,
             "note": note}
            for n, got, want, note in checks
        ],
        "allPassed": all(bool(got) is want for _n, got, want, _note in checks),
        "context": {
            "block": "prop:spectrahedral-phase-collapse",
            "lean": LEAN_REL,
            "bean": "qou-zf9n",
            "scope": (
                "(a) scope-limited per AGENTS.md: this shows the supergolden "
                "threshold is a convention-C feature and does not survive D. It "
                "does NOT exclude a phase transition in the canonical frame by "
                "some other route -- only this determinant reading of one."
            ),
            "arithmetic": "exact over Q(u) and Q(q); no float64 anywhere",
        },
    }

    out = WitnessBuilder.wrap_legacy(
        "spectrahedral-phase-collapse-frame-probe", payload,
        script_path=__file__, engine="python+sympy(exact over Q(u), Q(q))",
    ).save()

    print("=== Spectrahedral phase collapse: does the threshold survive convention D? ===")
    print()
    print("Convention C  (z = u/(u^2+1), u = sqrt q) -- the frame the block uses")
    print(f"  det G_C(u) = {sp.factor(det_C)}")
    print(f"  positive real zeros: {[float(r) for r in pos_zeros]}")
    print("    u = 0.68232780  = 1/psi   (supergolden, multiplicity 5)")
    print("    u = 1.00000000  = q = 1   (classical limit, multiplicity 1)  <- not in the block")
    print()
    print("Convention D  (z = q^3/(q^2+1)) -- canonical, owner ruling 2026-08-15")
    print(f"  det G_D(q) = {det_D}   (identically zero, all q)")
    print()
    for n, got, want, note in checks:
        good = bool(got) is want
        print(f"  [{'PASS' if good else 'FAIL'}] {n:<40} = {bool(got)!s:<5} ({note})")
    print()
    print("VERDICT: the C-frame theorem is true and non-vacuous, and understates")
    print("itself -- there are two degeneracies on u > 0, not one. Under canonical")
    print("D the determinant vanishes everywhere, so the supergolden point is not")
    print("distinguished and the phase-transition READING does not survive. Scope")
    print("the block to C; keep the theorem, do not restate it of the canonical Gram.")
    print()
    print(f"  witness -> {out}")
    return 0 if payload["allPassed"] else 1


if __name__ == "__main__":
    sys.exit(main())
