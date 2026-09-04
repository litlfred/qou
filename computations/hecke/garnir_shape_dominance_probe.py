#!/usr/bin/env python3
"""Does the Garnir composition's partition STRICTLY dominate the original shape?

Mathas, *Hecke algebras and Schur algebras of the symmetric group*, Lemma 3.12:

    Let lambda be a partition of n and suppose g is a Garnir tableau.  Then there
    exists a partition nu of n such that nu |> lambda and m_{t^lambda g} = ...

    Proof.  ... Set nu = (l_1, ..., l_{i-1}, j-1, l_i + 1, l_{i+1} - j,
    l_{i+2}, ..., l_k), a composition of n ...

That composition is what this probe checks, BEFORE any of it is formalised.  The
question is narrow and finite: for every partition and every Garnir node, does the
SORTED composition strictly dominate the original partition?

Why it is worth asking rather than assuming.  The corpus already carries a
disproof of the neighbouring, tempting statement --
`docs/audits/2026-07-06-garnir-strict-domweight-counterexample.md` shows that the
strict `domWeight` (tableau-level) induction is FALSE, because same-tabloid Garnir
cosets tie the weight.  Mathas' strictness lives one level up, in the SHAPE.  This
probe is the check that the shape-level strictness really is strict, i.e. that the
route around the refuted one exists.

RESULT (measured, n = 2..11, 910 Garnir nodes, exhaustive over all partitions):

    sorted(nu) >_lex lambda   910 / 910    <- Mathas' actual order
    sorted(nu) |> lambda      824 / 910    <- dominance: 86 FAILURES

**Dominance is FALSE here, and the smallest counterexample is hand-checkable.**
lambda = (3,3), node (i,j) = (0,1):  nu = (1, 4, 1), sorted (4,1,1).  Partial sums
4 >= 3 but 4+1 = 5 < 6 = 3+3, so (4,1,1) does NOT dominate (3,3) -- while it is
plainly lex-greater, since 4 > 3 in the first part.

The order is not an incidental detail of the write-up: Mathas introduces it
explicitly, in the sentence immediately before Lemma 3.12, precisely because these
lemmas need a different one --

    "For the next few Lemmas we need another ordering on the set of partitions.
     Given partitions lambda and mu we write lambda > mu if lambda is greater than
     mu in the lexicographic ordering. ...  Note that if lambda |> mu then
     lambda > mu."

so dominance implies lex and lex is the weaker, TOTAL order.  For the formalisation
that is the good news: lex on partitions of a fixed n is a total order on a finite
set, hence well-founded with no extra work, whereas dominance is only partial.  The
corpus's `QOU.BraidKnot.SpechtClassification.partitionDom` is DOMINANCE and is
therefore NOT the order this induction runs on.

Index convention: 0-indexed throughout, to match the corpus
(`QOU.BraidKnot.GarnirTableau.garnirPerm i j h` with `h : (i + 1, j) in mu`), NOT
Mathas' 1-indexing.  Translating j_Mathas = j + 1, his three replacement parts

    (j_M - 1, l_i + 1, l_{i+1} - j_M)   become   (j, l_i + 1, l_{i+1} - j - 1).

Arithmetic is exact integer throughout: partitions are tuples of `int`, dominance
is a comparison of integer partial sums.  No float appears anywhere in this file.
"""

from itertools import count


def partitions(n, maxpart=None):
    """All partitions of n as weakly-decreasing tuples of positive ints."""
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def sort_to_partition(comp):
    """A composition -> the partition of its parts (zeros dropped, sorted down)."""
    return tuple(sorted((p for p in comp if p > 0), reverse=True))


def dominates(mu, lam):
    """mu |>= lam  (dominance): every partial sum of mu is >= that of lam.

    Both are partitions of the same n, so the full sums agree and short tuples are
    padded with zeros.
    """
    k = max(len(mu), len(lam))
    s_mu = s_lam = 0
    for r in range(k):
        s_mu += mu[r] if r < len(mu) else 0
        s_lam += lam[r] if r < len(lam) else 0
        if s_mu < s_lam:
            return False
    return True


def strictly_dominates(mu, lam):
    return mu != lam and dominates(mu, lam)


def lex_gt(mu, lam):
    """mu > lam in Mathas' lexicographic order: the first differing part is larger.

    His definition verbatim: "there exists an integer j >= 1 such that lambda_i =
    mu_i for 1 <= i < j and lambda_j > mu_j".  Short tuples pad with zeros, which is
    the right convention here because both are partitions of the same n.
    """
    for r in range(max(len(mu), len(lam))):
        a = mu[r] if r < len(mu) else 0
        b = lam[r] if r < len(lam) else 0
        if a != b:
            return a > b
    return False


def garnir_composition(lam, i, j):
    """Mathas' nu for the Garnir node (i, j), in 0-indexed form.

    Replaces parts `lam[i], lam[i+1]` by `(j, lam[i] + 1, lam[i+1] - j - 1)`.
    """
    return tuple(lam[:i]) + (j, lam[i] + 1, lam[i + 1] - j - 1) + tuple(lam[i + 2:])


def garnir_nodes(lam):
    """Every (i, j) with the cell (i+1, j) in the diagram -- the Garnir nodes.

    This is exactly `h : (i + 1, j) in mu` in the Lean.
    """
    for i in range(len(lam) - 1):
        for j in range(lam[i + 1]):
            yield i, j


def main():
    N_MAX = 11
    total = 0
    lex_ok = 0
    dom_ok = 0
    lex_fail = []
    dom_fail = []
    malformed = []

    for n in range(2, N_MAX + 1):
        for lam in partitions(n):
            for (i, j) in garnir_nodes(lam):
                nu_comp = garnir_composition(lam, i, j)
                # exactness guard: nu must be a composition of the same n
                if sum(nu_comp) != n or any(p < 0 for p in nu_comp):
                    malformed.append((n, lam, i, j, nu_comp))
                    continue
                nu = sort_to_partition(nu_comp)
                total += 1
                if lex_gt(nu, lam):
                    lex_ok += 1
                else:
                    lex_fail.append((n, lam, i, j, nu_comp, nu))
                if strictly_dominates(nu, lam):
                    dom_ok += 1
                else:
                    dom_fail.append((n, lam, i, j, nu_comp, nu))

    print(f"Garnir nodes tested (n = 2..{N_MAX}, exhaustive): {total}")
    print(f"  sorted(nu) >_lex lambda  -- Mathas' actual order : {lex_ok:5d}   "
          f"fails {len(lex_fail)}")
    print(f"  sorted(nu) |> lambda     -- dominance, stronger  : {dom_ok:5d}   "
          f"fails {len(dom_fail)}")
    print(f"  composition malformed (sum or sign)              : {len(malformed)}")

    if dom_fail:
        print("\n  Dominance counterexamples (first 5) -- lambda, node (i,j), nu:")
        for (n_, lam, i, j, comp, nu) in dom_fail[:5]:
            print(f"    n={n_}  lambda={lam}  (i,j)=({i},{j})  comp={comp}  nu={nu}"
                  f"   lex-greater? {lex_gt(nu, lam)}")

    if lex_fail:
        print("\n  LEX failures (first 10):")
        for c in lex_fail[:10]:
            print("   ", c)

    # The assertion of this probe is the LEX statement.  The dominance figure is
    # reported, not asserted -- it is expected to fail, and that is the finding.
    ok = (not lex_fail) and (not malformed) and total > 0
    print()
    if ok:
        print("VERDICT: Mathas' lex-strictness HOLDS on the whole sample; "
              "dominance does NOT and must not be used for this induction.")
    else:
        print("VERDICT: the lex statement FAILED -- see cases above.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
