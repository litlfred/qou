#!/usr/bin/env python3
"""All THREE gates named for selecting the D-frame Habiro generator are
non-discriminating.  The class cannot be closed from internal consistency.

Bean `qou-cds1`, tranche S1.  Follows PR #6282 (merged `e2f6a1a76d`), which
established that all three legs of the C-frame instrument fail to transport to
convention D, and named three gates on any candidate generator `rho`
(the rank-1 ratio in `c_{k+1} = rho * c_k`).  Two were already retracted there:

    gate                     verdict in #6282
    -----------------------  -------------------------------------------------
    bar-parity               FILTER, not a selector -- every symmetric
                             q-integer is bar-invariant, so it admits the
                             whole family at once
    Hankel  c_2*c_4 = c_3^2  VACUOUS for rank-1 -- rank-1 gives c_3 = rho*c_2
                             and c_4 = rho^2*c_2, so it holds IDENTICALLY for
                             every rho
    C-limit reduction        "survives"   <-- THIS FILE REFUTES THAT

This file closes the third.  The C-limit gate asks that the D-frame ladder
reduce to the C-frame ladder where the two conventions agree, i.e. where

    z_C(q) = sqrt(q)/(q+1)   equals   z_D(q) = q^3/(q^2+1).

That happens at exactly ONE point, `q = 1` -- and `q = 1` is precisely where the
ladder is degenerate: `hbar_q = 0` so `u = 0`, `h = 0` so `Vhat = 1` and
`alpha = 0`, and the whole product collapses to the bare `Q_A` for EVERY
candidate.  The gate is therefore satisfied by every `rho` and discriminates
nothing.

CONSEQUENCE (scope (a), and it is the point of the file): the generator cannot
be selected by any internal-consistency condition identified so far.  Closing it
needs an EXTERNAL structural input -- not another candidate sweep.  Naming the
remaining routes is done in the bean, not asserted here.

Exact sympy; no float64; emits no witness.
"""
import sys

import sympy as sp

q = sp.symbols("q", positive=True)


def main() -> int:
    checks = []

    zC = sp.sqrt(q) / (q + 1)
    zD = q**3 / (q**2 + 1)

    # 1. The two conventions agree at exactly one point, and it is q = 1.
    sols = sp.solve(sp.Eq(zC, zD), q)
    real_pos = [s for s in sols if s.is_real and s.is_positive]
    checks.append(("z_C = z_D has exactly one positive real solution",
                   len(real_pos) == 1))
    checks.append(("and that solution is q = 1", real_pos == [sp.Integer(1)]))

    # 2. At q = 1 every ladder ingredient degenerates.
    hbar = (q - 1) / q
    h = q - 1 / q
    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    u = b * hbar**2
    VhatD = sp.simplify(zD * h + 1)
    alphaD = (zD - 1) * h / 2

    at1 = lambda e: sp.simplify(e.subs(q, 1))
    checks.append(("hbar_q(1) = 0", at1(hbar) == 0))
    checks.append(("u(1) = 0", at1(u) == 0))
    checks.append(("h(1) = 0", at1(h) == 0))
    checks.append(("Vhat_D(1) = 1", at1(VhatD) == 1))
    checks.append(("alpha_D(1) = 0", at1(alphaD) == 0))

    # 3. So the whole product collapses to 1 at q = 1, for ANY rho and ANY c_2.
    #    Ladder factor k is (1 + c_k * X^k) with X = u*Vhat_D; X(1) = 0.
    X = u * VhatD
    checks.append(("X(1) = 0, so every rung factor is 1 at q = 1", at1(X) == 0))

    rho, c2 = sp.symbols("rho c_2")
    prod = sp.prod([1 + c2 * rho ** (k - 2) * X**k for k in range(2, 8)])
    checks.append(("the whole product is 1 at q=1 for symbolic rho and c_2",
                   sp.simplify(prod.subs(q, 1)) == 1))

    # 4. And the N=1 factor too, under the sibling's derived bar-midpoint form
    #    M = cos(a_D - h^2/4) * cos(h^2/4).
    M = sp.cos(alphaD - h**2 / 4) * sp.cos(h**2 / 4)
    checks.append(("the derived N=1 factor M(1) = 1 as well", at1(M) == 1))

    print("Convention D vs C: where do they agree?  Exact sympy.\n")
    print(f"  z_C = {zC}")
    print(f"  z_D = {zD}")
    print(f"  z_C = z_D  at  q in {real_pos}   <- the ONLY positive real point\n")
    print("  numerically, away from that point they diverge fast:")
    for v in (sp.Rational(1), sp.Rational(11, 10), sp.Rational(111, 100),
              sp.Integer(2)):
        print(f"    q={float(v):.3f}   z_C={float(zC.subs(q, v)):.6f}"
              f"   z_D={float(zD.subs(q, v)):.6f}")

    print("\n  at q = 1 every ingredient degenerates:")
    for name, e in (("hbar_q", hbar), ("h", h), ("u", u),
                    ("Vhat_D", VhatD), ("alpha_D", alphaD), ("X = u*Vhat_D", X)):
        print(f"    {name:14} -> {at1(e)}")
    print("    ladder product -> 1   (symbolic rho, symbolic c_2)")
    print("    N=1 factor M   -> 1")

    print("\n--- checks ---")
    ok = True
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok = ok and bool(passed)
    print(f"\n{sum(1 for _, p in checks if p)}/{len(checks)}")

    print("""
FINDING -- the gate inventory is EXHAUSTED

  bar-parity        FILTER      admits every symmetric q-integer  (#6282)
  Hankel            VACUOUS     holds identically for rank-1      (#6282)
  C-limit reduction VACUOUS     only q=1, where the ladder is degenerate (HERE)

All three conditions named for selecting the D-frame Habiro generator are
satisfied by every candidate.  The generator is NOT determined by internal
consistency, and running a wider candidate sweep against these gates cannot
change that -- the gates do not rank candidates, they admit all of them.

This is the formalize-first prune applied to my own proposed search: the
structural argument says do NOT run the scan.

Scope (a).  A scope-limited negative about the three gates identified so far,
NOT a claim that no gate exists.  What it establishes is that closing the
generator needs an EXTERNAL structural input, and that the next move is to find
one rather than to enumerate candidates.
""")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
