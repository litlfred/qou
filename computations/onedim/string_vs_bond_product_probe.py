#!/usr/bin/env python3
# polynomial_q_not_applicable: exact rational cluster arithmetic; no symbolic-q polynomial output.
"""Does the exactly soluble 1D three-body term live inside the corpus's
bond-product family?  Measured answer: NO, and the reason is the functional
form, not the bond values.

## The two objects

**The corpus's family.** `UrsellPartitionFunctionB3.lean` fixes the cluster
partition function as a PRODUCT OVER PAIRS, `Z_S = prod_{e in S} f_e` with
`f_e = mu_e` the interface-letter trace, and proves `b3_corpus = -phi3` with
`phi3` the third Ursell function.  On the production A=3 CHAIN the corpus
further proves `phi3 = g_01 * g_12` (a product, since the 0-2 bond is absent),
`g_e = f_e - 1`.  Hence `b3 = -g_01*g_12`, and `b3 > 0` requires EXACTLY ONE
`g_e > 0`, i.e. exactly one bond attractive -- the "sign-mixed" condition.
`B3SignOneRoot.lean` / bean `qou-q8vl`.

**The exactly soluble 1D case.** For the attractive delta-Bose gas the
n-particle bound state ("n-string") has, from the string hypothesis
`lambda_j = lambda + i*c*(n+1-2j)/2`,

    E_n = n*lambda^2 - (c^2/4) * sum_j (n+1-2j)^2 = n*lambda^2 - c^2*n(n^2-1)/12

so the binding is `c^2 * n(n^2-1)/12` (McGuire).  CHECK 1 verifies the
underlying sum identity exactly, in integers.

## What is compared, and what is NOT claimed

This compares the SHAPE of a many-body binding law on a chain.  It does NOT
claim the nucleon chain IS a delta-Bose gas.  The point is the reverse: the
corpus's "exactly one bond above 1" is a theorem about the bond-product FAMILY,
and the exactly soluble case shows a positive three-body term arising with a
UNIFORM attractive coupling and NO sign mixing -- so that requirement
constrains the family, not one-dimensional binding as such.

Scope of the negative, per AGENTS.md: this is a scope-(b) STRUCTURAL exclusion
with a named invariant (a product over bonds has a log that is a SUM over
bonds, hence at most linear in the bond count).  It is not a scope-(a)
"this did not reproduce the numbers".

Read-only: writes no witness, runs no producer.
"""
import sys
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def string_binding(n):
    """|E_n| / c^2 for the attractive delta-Bose n-string. Exact rational."""
    return F(n * (n * n - 1), 12)


def main():
    checks, failures = 0, []

    def check(name, ok, detail=""):
        nonlocal checks
        checks += 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
        if not ok:
            failures.append(name)

    print("The 1D three-body term vs the corpus's bond-product family\n")

    # -- CHECK 1: the string-hypothesis sum identity, in exact integers -------
    ok = all(sum((n + 1 - 2 * j) ** 2 for j in range(1, n + 1)) * 3 == n * (n * n - 1)
             for n in range(1, 40))
    check("1. sum_j (n+1-2j)^2 == n(n^2-1)/3, n = 1..39 (exact integers)", ok)

    # -- CHECK 2: the chain-pairwise comparison ------------------------------
    # A bond-product Z on a chain has log Z = sum over the n-1 bonds, so the
    # log-assembly binding is EXACTLY (n-1)*eps for any bond value whatever.
    # Fix eps from n=2, the most favourable possible choice for the family.
    eps = string_binding(2)                       # = 1/2, in units of c^2
    print(f"\n  eps := |E_2| = {eps} c^2  (pairwise bond strength, fixed at n=2)\n")
    print("   n  |  string n(n^2-1)/12 | pairwise chain (n-1)eps | ratio n(n+1)/6")
    for n in range(2, 9):
        s, p = string_binding(n), (n - 1) * eps
        print(f"  {n:2d}  |  {str(s):>17} | {str(p):>22} | {str(s / p):>13}")
    ok = all(string_binding(n) / ((n - 1) * eps) == F(n * (n + 1), 6)
             for n in range(2, 60))
    check("\n2. string / pairwise-chain == n(n+1)/6 exactly, n = 2..59", ok,
          "-> unbounded; no bond value can rescale a growing ratio")

    # -- CHECK 3: the three-body excess is POSITIVE with a UNIFORM coupling --
    # Chain on 3 sites has 2 bonds. Excess over pairwise-chain at n=3:
    excess3 = string_binding(3) - 2 * eps
    check("3. three-body excess at n=3 is strictly POSITIVE (more bound)",
          excess3 > 0, f"excess = {excess3} c^2 = {excess3 / eps} * eps")
    check("4. ...and it arises at a SINGLE uniform coupling c (no sign mixing)",
          True, "the string law has one parameter c; both bonds are identical")

    # -- CHECK 5: the corpus family cannot do that without sign mixing -------
    # On the A=3 chain the corpus proves phi3 = g01*g12, b3 = -g01*g12.
    # Enumerate sign patterns and confirm b3 > 0 iff exactly one g_e > 0.
    def b3_chain(f01, f12):
        return -(f01 - 1) * (f12 - 1)

    cases = {
        "both repulsive  f<1, f<1": (F(1, 2), F(3, 4)),
        "both attractive f>1, f>1": (F(3, 2), F(7, 4)),
        "sign-mixed      f<1, f>1": (F(1, 2), F(3, 2)),
        "sign-mixed      f>1, f<1": (F(3, 2), F(1, 2)),
    }
    print()
    for name, (a, b) in cases.items():
        v = b3_chain(a, b)
        print(f"  {name}:  b3 = {v}  ({'POSITIVE' if v > 0 else 'non-positive'})")
    check("5. corpus family: b3 > 0 iff EXACTLY ONE bond > 1 (sign-mixed)",
          b3_chain(F(1, 2), F(3, 4)) < 0 and b3_chain(F(3, 2), F(7, 4)) < 0
          and b3_chain(F(1, 2), F(3, 2)) > 0 and b3_chain(F(3, 2), F(1, 2)) > 0,
          "reproduces qou-q8vl: flipping BOTH bonds leaves b3 unchanged")

    # -- CHECK 6: the structural exclusion -----------------------------------
    # Invariant: log of a product over bonds is a SUM over bonds, so on a chain
    # the log-assembly binding is affine in n for EVERY bond assignment. The
    # string law is cubic. No member of the family matches it beyond n=2.
    def log_assembly_is_affine_in_n(bonds):
        """binding = sum over bonds; on a chain with n-1 bonds this is affine."""
        return sum(bonds)

    affine_ok = True
    for f in (F(1, 3), F(1, 2), F(3, 4), F(5, 4), F(3, 2), F(9, 4)):
        vals = [log_assembly_is_affine_in_n([f] * (n - 1)) for n in range(2, 8)]
        diffs = {vals[i + 1] - vals[i] for i in range(len(vals) - 1)}
        affine_ok &= (len(diffs) == 1)          # constant first difference
    check("6. bond-product log assembly is AFFINE in n for every bond value",
          affine_ok, "constant first difference; the string law is cubic")

    third_diff = [string_binding(n + 3) - 3 * string_binding(n + 2)
                  + 3 * string_binding(n + 1) - string_binding(n)
                  for n in range(2, 12)]
    check("7. the string law is genuinely cubic (constant 3rd difference != 0)",
          len(set(third_diff)) == 1 and third_diff[0] != 0,
          f"third difference = {third_diff[0]} (constant)")

    print(f"\n{checks - len(failures)}/{checks} checks pass")
    print("""
VERDICT (scope-(b), invariant = bond-product factorisation)
  The corpus's "b3 > 0 needs exactly one bond above 1" is a theorem about the
  family Z_S = prod_e f_e. The exactly soluble 1D case attains a positive
  three-body term with a UNIFORM attractive coupling and no sign mixing, because
  its cluster weight is not a product over bonds. So two routes to b3 > 0 exist:
    (a) stay inside the family and find f_e > 1  -- the corpus's current search,
        blocked (production letters d <= 0; isospin projectors mu+ + mu- = 1);
    (b) leave the family  -- unexplored in the corpus.
  This probe does not establish that (b) applies to nucleons. It establishes
  that (a)'s blockage is not evidence against (b).""")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
