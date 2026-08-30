#!/usr/bin/env python3
"""The Pieri corner identity in node coordinates — the six facts behind PR #6098.

`y_lambda_pieri_step_probe.py` reduced the Macdonald telescope's Pieri step (P) to
ONE identity in one variable,

    (P1)   Sum_r  Q^r * prod_{h in arm u leg(r)} (1 - Q^h)/(1 - Q^{h+1})  =  1

and recorded it as the open remainder. This probe changes the coordinates and the
identity becomes provable: it is a Lagrange node sum, with no partition in it.

`QOU.Mathlib.sum_prod_qratio_corner` (sorry-free, axiom-clean, generic `[Field F]`)
is fact 5 below. Facts 1-4 are the change of coordinates that carries (P1) to it;
fact 6 is the negative that makes the Lean hypothesis `v b = 1` load-bearing rather
than decorative. Fact 2 is the one piece still unproved, and the corpus already
names it as the open input to `sum_eq_bracket_mul_of_qratio_scaling`.

Coordinates. Pad `lam` with empty rows to length `k`, set the beta-numbers
`beta_i = lam_i + (k-1-i)` and the nodes `b_i = q^{beta_i}`. The padded bottom row
has `beta = 0`, hence the node `b = 1` that fact 6 shows is essential.

1. **The classical beta formula**, `prodHooks(lam) = prod_i beta_i! / prod_{j<l}(beta_j - beta_l)`,
   holds at every padding length. Its Lean counterpart is proved on the list layer:
   `QOU.Mathlib.SYTHookFormulaGeneral.prodHooks_mul_betaProdGap`.

2. **The q-analogue**, sign-free and power-free and also k-independent:

       prod_{c in lam} (1 - q^{h(c)})  =  prod_i (q;q)_{beta_i} / prod_{j<l} (1 - q^{beta_j - beta_l})

   This is the q-deformed Frame-Robinson-Thrall hook identity. **It IS proved in the
   corpus** -- `SYTBetaGapVandermonde.prodHooksF_one_sub_pow_pair`, sorry-free, as the
   `f n = 1 - Q^n` case of a per-row identity proved over an arbitrary commutative
   monoid. An earlier version of this docstring said it was open, on the strength of
   `LagrangeCoeffSum`'s docstring, which is stale (its bean `qou-j7ln` is completed).
   A source file's status note is not authoritative; that rule covers docstrings too.
   Measured here as an independent check of the Lean, not as evidence for an open item.

3. **The row-index weight `Q^r` in (P1) is forced, not chosen.** It is exactly the
   `q^{sum_l l*beta_l}` normalisation that converts the sign-free form of fact 2 into
   the node-gap form. Concretely

       Q^i * A(lam)/A(lam + box in row i)  =  1/(1 - q*b_i) * prod_{j != i}(q*b_i - b_j)/(b_i - b_j)

   where `A(nu) = prod_{c in nu} (1 - q^{h(c)})`. Nothing was fitted to make the
   weight appear; it falls out of the coordinate change.

4. **(P1) becomes a node sum**, and the sum may run over ALL rows of the padded shape,
   not only the addable ones: a non-addable row `i` has `beta_{i-1} = beta_i + 1`, so
   the factor `(q*b_i - b_{i-1})` vanishes and the term is 0 on its own.

5. **The node sum is GENERIC** — it holds for arbitrary distinct `b_i`, one of which
   is `1`, with no reference to any partition. This is what the Lean proves.

6. **It FAILS without the node at 1.** With free nodes and no padding row the k=2 sum
   is a genuine rational function. So the addable corner in the new bottom row is not
   an edge case to be tidied away: the identity is about shapes permitted to grow a row.

Precision: EXACT throughout — sympy symbolic over Q(q, b_0, ...), with `cancel`
deciding equality. No float appears anywhere, so the NO-FLOAT64 discipline
(AGENTS.md "PROBES ARE NOT EXEMPT") is satisfied by construction rather than by
tolerance. No witness is emitted: every output is a symbolic identity that
re-derives in seconds, and there is no measured number to record.
"""

from sympy import cancel, factorial, prod, simplify, symbols

q = symbols("q")

SHAPES = [[1], [2], [1, 1], [2, 1], [3, 1], [2, 2], [3, 2, 1], [4, 2, 1],
          [3, 3, 2], [4, 3, 1, 1], [5, 2, 2, 1], [4, 4], [5, 3, 1]]


def hook(lam, i, j):
    """Hook length of cell (i, j): arm + leg + 1."""
    arm = lam[i] - j - 1
    leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
    return arm + leg + 1


def cells(lam):
    return [(i, j) for i in range(len(lam)) for j in range(lam[i])]


def prod_hooks(lam):
    return prod([hook(lam, i, j) for (i, j) in cells(lam)])


def A(lam):
    """prod_{c in lam} (1 - q^{h(c)}) -- the un-normalised q-hook product."""
    return prod([1 - q ** hook(lam, i, j) for (i, j) in cells(lam)])


def qpoch(n):
    """(q;q)_n = prod_{m=1..n} (1 - q^m)."""
    return prod([1 - q ** m for m in range(1, n + 1)])


def beta(lam, k):
    """Beta-numbers of lam padded with empty rows to length k."""
    p = list(lam) + [0] * (k - len(lam))
    return [p[i] + (k - 1 - i) for i in range(k)]


def addable(lam, k):
    p = list(lam) + [0] * (k - len(lam))
    return [i for i in range(k) if i == 0 or p[i] < p[i - 1]]


def add_box(lam, k, i):
    p = list(lam) + [0] * (k - len(lam))
    p[i] += 1
    return [x for x in p if x > 0]


def fact1_classical_beta_formula():
    bad = []
    for lam in SHAPES:
        for k in range(len(lam), len(lam) + 3):
            b = beta(lam, k)
            gap = prod([b[j] - b[l] for j in range(k) for l in range(j + 1, k)])
            if prod([factorial(x) for x in b]) / gap != prod_hooks(lam):
                bad.append((lam, k))
    return bad


def fact2_q_beta_formula():
    bad = []
    for lam in SHAPES:
        for k in range(len(lam), len(lam) + 3):
            b = beta(lam, k)
            den = prod([1 - q ** (b[j] - b[l])
                        for j in range(k) for l in range(j + 1, k)])
            if cancel(prod([qpoch(x) for x in b]) / den / A(lam)) != 1:
                bad.append((lam, k))
    return bad


def fact3_weight_is_forced():
    bad = []
    for lam in SHAPES:
        k = len(lam) + 1
        b = beta(lam, k)
        bb = [q ** x for x in b]
        for i in addable(lam, k):
            lhs = q ** i * A(lam) / A(add_box(lam, k, i))
            rhs = (1 / (1 - q * bb[i])
                   * prod([(q * bb[i] - bb[j]) / (bb[i] - bb[j])
                           for j in range(k) if j != i]))
            if cancel(lhs - rhs) != 0:
                bad.append((lam, i))
    return bad


def fact4_node_sum_over_all_rows():
    bad = []
    for lam in SHAPES:
        k = len(lam) + 1
        bb = [q ** x for x in beta(lam, k)]
        s = sum((1 - q) / (1 - q * bb[i])
                * prod([(q * bb[i] - bb[j]) / (bb[i] - bb[j])
                        for j in range(k) if j != i])
                for i in range(k))
        if cancel(s - 1) != 0:
            bad.append((lam, cancel(s)))
    return bad


def fact5_generic_with_unit_node():
    out = []
    for k in (2, 3, 4, 5):
        bs = list(symbols(f"b0:{k}"))
        bs[k - 1] = 1
        s = sum((1 - q) / (1 - q * bs[i])
                * prod([(q * bs[i] - bs[j]) / (bs[i] - bs[j])
                        for j in range(k) if j != i])
                for i in range(k))
        out.append((k, cancel(s)))
    return out


def fact6_fails_without_unit_node():
    out = []
    for k in (2, 3):
        bs = list(symbols(f"b0:{k}"))
        s = sum((1 - q) / (1 - q * bs[i])
                * prod([(q * bs[i] - bs[j]) / (bs[i] - bs[j])
                        for j in range(k) if j != i])
                for i in range(k))
        out.append((k, cancel(simplify(s))))
    return out


def main():
    ok = True

    bad = fact1_classical_beta_formula()
    print(f"1. classical beta formula, {len(SHAPES)} shapes x 3 paddings: "
          f"{'OK (k-independent)' if not bad else f'FAILED {bad}'}")
    ok &= not bad

    bad = fact2_q_beta_formula()
    print(f"2. q-beta formula (the OPEN bridge), same sample:               "
          f"{'OK (k-independent)' if not bad else f'FAILED {bad}'}")
    ok &= not bad

    bad = fact3_weight_is_forced()
    print(f"3. the Q^r weight is the q^{{sum l*beta_l}} normalisation:        "
          f"{'OK (forced, not chosen)' if not bad else f'FAILED {bad}'}")
    ok &= not bad

    bad = fact4_node_sum_over_all_rows()
    print(f"4. (P1) as a node sum over ALL rows:                            "
          f"{'OK (non-addable rows self-cancel)' if not bad else f'FAILED {bad}'}")
    ok &= not bad

    res = fact5_generic_with_unit_node()
    good5 = all(v == 1 for _, v in res)
    print(f"5. GENERIC nodes, one equal to 1 (this is the Lean theorem):    "
          f"{'OK, = 1 at k=' + ','.join(str(k) for k, _ in res) if good5 else f'FAILED {res}'}")
    ok &= good5

    res = fact6_fails_without_unit_node()
    good6 = all(v != 1 for _, v in res)
    print("6. WITHOUT a node at 1 the identity is FALSE — so `v b = 1` is")
    print("   load-bearing, and the new-bottom-row corner cannot be dropped:")
    for k, v in res:
        print(f"     k={k}: {v}")
    ok &= good6

    print()
    print(f"all exact: {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
