#!/usr/bin/env python3
"""Convention-slip validator — generalises the trace-convention registry guard.

THE DEFECT CLASS
----------------
A *named constant stipulated inside a definition, inconsistent with the object
the definition names*, propagating silently because nothing cross-checked the
name against the value.

The seed instance (bean ``qou-3qrv`` / ``n1dj``) was ``markov-axioms-primitive.md``
axiom 3 stipulating ``z = 1/(q^{1/2}+q^{-1/2})`` while naming the *Jones*-Markov
trace: that value is ``1/delta``, the Temperley-Lieb loop reciprocal (right for
the TL generator ``e_i``, wrong for the Hecke generator ``sigma_n`` it was
applied to). The trace-convention registry implements the *doc-vs-code*
comparison (question 3) for traces specifically. This validator implements the
two *self-consistency* questions, which need no second implementation to
compare against and therefore generalise to every channel:

  R1  RECONSTRUCTION IDENTITY.
      A stated decomposition must sum to the object it decomposes.
      Mechanical, symbolic, no reference implementation needed.
      Catches: coulomb-charge.md's strong/Coulomb split, which reconstructs
      ``p*q + m/q`` instead of ``p*q - m/q`` (multiplicities swapped between
      the cosh and sinh channels).

  R2  ALGEBRA-RELATION RESIDUAL.
      A claimed identity in ``H_n(q)`` must have zero residual in a
      representation that satisfies the Hecke relation. We use the Hoefsmit
      2-dimensional representation of ``H_3(q)``, whose Hecke relation is
      asserted first as a self-test.
      Catches: feynman-eigenbasis.md:29 asserting the balanced HOMFLY/Jones
      skein relation *is* the characteristic equation of the braiding.

  R3  FIBRE-DIMENSION INTEGRALITY.
      ``z(N) = q^N/[N]_q`` is strictly decreasing in ``N`` for ``q > 1``, hence
      injective, so a stipulated Ocneanu parameter determines a fibre dimension
      ``N_eff = -ln(1 - (q - q^-1)/z) / (2 ln q)``. A categorical trace on a
      fibre requires ``N_eff`` to be a positive integer.
      Catches the seed defect: convention C gives ``N_eff = 2.5995...``.
      Lean backing (sorry-free): ``QOU.BraidsAndKnots.ocneanu_param_eq_of_fibre_qdim``
      in ``FibreDimensionForcesTL.lean`` proves ``z*[N]_q = q^N``.

Entries with ``expect: "fail"`` are REGRESSION FIXTURES pinning a confirmed
defect. ``--strict`` exits 1 when an ``expect: "pass"`` entry regresses, or when
an ``expect: "fail"`` entry starts passing (the doc was fixed; update the
registry).

q0 is the EXPERIMENTAL / proton pin per the AGENTS.md owner directive of
2026-08-07. R1 and R2 are symbolic and pin-independent; only R3 evaluates at q0.

Usage:
    python3 docs/coordination/convention_slip_validate.py
    python3 docs/coordination/convention_slip_validate.py --strict
    python3 docs/coordination/convention_slip_validate.py --rule R1
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
REGISTRY = HERE / "convention-slip-registry.json"

# Integrality tolerance for R3. The non-integer witness in the seed defect is
# 0.5995 away from an integer, four orders of magnitude above this bound, so the
# test is not tolerance-sensitive.
N_EFF_TOL = sp.Rational(1, 10**6)


def _hoefsmit_h3(q: sp.Symbol) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    """The Hoefsmit 2-dim rep of H_3(q): sigma_2 in seminormal (symmetric) form.

    Uniquely determined by fixing the off-diagonal to b = sqrt([3]_q)/[2]_q and
    imposing trace = q - q^-1, det = -1 (the Hecke eigenvalues q, -q^-1) plus the
    braid relation. Returns (sigma, sigma_inv, identity).
    """
    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    s = sp.Matrix([[-1 / (q**3 + q), b], [b, q**3 / (q**2 + 1)]])
    return s, sp.simplify(s.inv()), sp.eye(2)


def _is_zero_matrix(m: sp.Matrix) -> bool:
    return all(sp.simplify(e) == 0 for e in m)


def check_r1(entries: list[dict]) -> list[dict]:
    """R1 — a stated decomposition must sum to the object it decomposes."""
    out = []
    for e in entries:
        syms = {n: sp.Symbol(n, positive=True) for n in e["symbols"]}
        whole = sp.sympify(e["whole"], locals=syms)
        parts = sum(sp.sympify(p, locals=syms) for p in e["parts"])
        residual = sp.simplify(whole - parts)
        passed = residual == 0
        out.append(
            {
                "id": e["id"],
                "rule": "R1",
                "channel": e.get("channel", "?"),
                "doc": e["doc"],
                "passed": passed,
                "expect": e["expect"],
                "detail": "residual 0"
                if passed
                else f"residual = {sp.simplify(residual)}  (reconstructs {sp.simplify(parts)})",
            }
        )
    return out


def check_r2(entries: list[dict]) -> list[dict]:
    """R2 — a claimed H_n(q) identity must have zero residual in a Hecke rep."""
    q = sp.Symbol("q", positive=True)
    s, si, I = _hoefsmit_h3(q)
    h = q - 1 / q

    # Self-test: the representation must satisfy the Hecke quadratic relation,
    # otherwise every downstream verdict is meaningless.
    if not _is_zero_matrix(s * s - h * s - I):
        raise AssertionError(
            "Hoefsmit self-test FAILED: rep does not satisfy sigma^2 = (q-q^-1)sigma + 1"
        )

    env = {"s": s, "si": si, "I": I, "q": q, "sqrt": sp.sqrt}
    out = []
    for e in entries:
        lhs = eval(e["lhs"], {"__builtins__": {}}, env)  # noqa: S307 - registry-controlled
        rhs = eval(e["rhs"], {"__builtins__": {}}, env)  # noqa: S307
        residual = sp.simplify(sp.Matrix(lhs) - sp.Matrix(rhs))
        passed = _is_zero_matrix(residual)
        if passed:
            detail = "residual is the zero matrix"
        else:
            q0 = sp.Float("1.1099785827513808", 30)
            num = sp.N(residual.subs(q, q0), 8)
            detail = f"nonzero residual; at q0 = {num.tolist()}"
        out.append(
            {
                "id": e["id"],
                "rule": "R2",
                "channel": e.get("channel", "?"),
                "doc": e["doc"],
                "passed": passed,
                "expect": e["expect"],
                "detail": detail,
            }
        )
    return out


def check_r3(entries: list[dict], q0_str: str) -> list[dict]:
    """R3 — a stipulated Ocneanu parameter must imply an integer fibre dim."""
    q = sp.Symbol("q", positive=True)
    q0 = sp.Float(q0_str, 40)
    out = []
    for e in entries:
        z_expr = sp.sympify(e["z"], locals={"q": q, "sqrt": sp.sqrt})
        z0 = sp.N(z_expr.subs(q, q0), 40)
        # N_eff = -ln(1 - (q - q^-1)/z) / (2 ln q), from z(N) = q^N/[N]_q.
        arg = 1 - (q0 - 1 / q0) / z0
        if arg <= 0:
            out.append(
                {
                    "id": e["id"],
                    "rule": "R3",
                    "channel": e.get("channel", "?"),
                    "doc": e["doc"],
                    "passed": False,
                    "expect": e["expect"],
                    "detail": f"no real fibre dimension: 1-(q-1/q)/z = {sp.N(arg, 8)} <= 0",
                }
            )
            continue
        n_eff = -sp.log(arg) / (2 * sp.log(q0))
        n_eff = sp.N(n_eff, 30)
        nearest = sp.Integer(sp.floor(n_eff + sp.Rational(1, 2)))
        dev = abs(n_eff - nearest)
        passed = bool(dev < N_EFF_TOL) and nearest > 0
        if passed and "expected_N" in e and nearest != e["expected_N"]:
            passed = False
            detail = f"N_eff = {sp.N(n_eff, 12)} -> {nearest}, but registry expects N = {e['expected_N']}"
        elif passed:
            detail = f"N_eff = {sp.N(n_eff, 12)} (integer, N = {nearest})"
        else:
            detail = f"N_eff = {sp.N(n_eff, 12)} — NOT an integer (deviation {sp.N(dev, 6)})"
        out.append(
            {
                "id": e["id"],
                "rule": "R3",
                "channel": e.get("channel", "?"),
                "doc": e["doc"],
                "passed": passed,
                "expect": e["expect"],
                "detail": detail,
            }
        )
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--strict", action="store_true", help="exit 1 on any surprise")
    ap.add_argument("--rule", choices=["R1", "R2", "R3"], help="run one rule only")
    args = ap.parse_args()

    reg = json.loads(REGISTRY.read_text())
    results: list[dict] = []
    if args.rule in (None, "R1"):
        results += check_r1(reg["R1_reconstruction"])
    if args.rule in (None, "R2"):
        results += check_r2(reg["R2_algebra_residual"])
    if args.rule in (None, "R3"):
        results += check_r3(reg["R3_fibre_dimension_integrality"], reg["q0"])

    surprises = []
    print(f"convention-slip validator — {len(results)} entries, q0 = {reg['q0']} ({reg['q0_pin']})\n")
    for r in results:
        actual = "pass" if r["passed"] else "fail"
        surprise = actual != r["expect"]
        mark = "!!" if surprise else ("ok" if r["passed"] else "DEFECT(known)")
        print(f"[{r['rule']}] {mark:14s} {r['id']}")
        print(f"     channel : {r['channel']}")
        print(f"     doc     : {r['doc']}")
        print(f"     {r['detail']}")
        if surprise:
            surprises.append(r)
            print(f"     >>> SURPRISE: expected {r['expect']}, got {actual}")
        print()

    n_defect = sum(1 for r in results if not r["passed"])
    print(f"summary: {len(results) - n_defect} pass, {n_defect} fail, {len(surprises)} surprise(s)")
    if surprises:
        print("\nA surprise means either a new defect landed, or a known defect was")
        print("fixed and the registry entry needs flipping to expect=pass.")
        for r in surprises:
            print(f"  - {r['id']} ({r['doc']})")
    if args.strict and surprises:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
