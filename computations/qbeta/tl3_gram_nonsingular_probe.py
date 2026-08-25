#!/usr/bin/env python3
"""The TL_3 quotient form is non-singular for EVERY real q > 0 — exactly.

Bean `qou-8iru` (the TL_n compute move) / `qou-cds2` (the Gram singularity).
Formalize-first step, run BEFORE the engine work, per AGENTS.md §3.3: state
the structural claim and check whether it prunes, rather than starting from a
numerical port.

## What was blocked

Under convention D the Markov-Gram form on the H_3(q) NF basis is identically
singular: `det G = 0` over Q(q), radical spanned by the three-strand
q-antisymmetriser `v_i = (-1/q)^len(w_i)`. Consumers work around it with
`pinv` (gram.py:407), a rank-one-shift Moore-Penrose (gram.rs:339), or by
raising. `qou-cds2` names the principled repair — build the form on the
TL_3 quotient, where the radical is divided out — and costs it at 2-3 days
across the Rust engine, the Python wrapper and confinement-operator-selection.

That estimate is worth spending only if the repair actually lands on a
non-singular form. **This probe settles that first, symbolically, at zero
engine cost.**

## Result

    det G_TL  =  -(q^4 + 1)(q^2 - q + 1)^4 (q^2 + q + 1)^4 / (q^2 + 1)^10

- **Non-singular for every real q > 0, with no exceptions.** Not "generically
  in q": the numerator's bracket has all-positive coefficients, so it is
  strictly positive on q > 0 and the determinant is strictly negative there.
  Confirmed independently — the numerator has no real roots at all.
- **The exponents are the Wedderburn block dimensions squared.** `(q^4+1)`
  appears once and the two cyclotomic factors to the fourth: 1 = dim(3)^2 and
  4 = dim(2,1)^2, the two partitions of 3 with fewer than three rows. The
  three-row partition (1^3) is exactly the block convention D kills, which is
  what makes the quotient Temperley-Lieb (`qou-8iru`).
- **It agrees with the Wedderburn prediction up to a perfect square.**
  `y_(3)^1 * y_(2,1)^4` from the closed form `y_(n-k,k) = [n-2k+1]/[2]^n`
  differs from `det G_TL` by exactly `-(J^2)`, `J = (q^4+q^2+1)^2/q^4` — the
  change-of-basis law `det_B(G) = det(P)^2 det_W(G)`, since the NF basis is
  not the matrix-unit basis. A mismatch of any other shape would have meant
  one of the two is wrong.

## Scope

Scope-(b) structural, citing a proved invariant (the determinant, exactly over
Q(q)). It establishes that the TL_3 target is well-posed; it does **not**
perform the migration, and nothing here is wired to production.

Everything is exact sympy over Q(q). No float64, no q_0 evaluation, no anchor
— so the result is pin-independent and carries no muon/proton layer question.
"""
from __future__ import annotations

import sympy as sp

NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]

_CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    _CHECKS.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")


def gram_symbolic(q):
    """G[i][j] = tr_M(b_i b_j) on NF_BASIS, exact over Q(q), convention D.

    Multiplication table and TR_M transcribed from `pyhecke.gram` exactly as
    `computations/probes/gram_radical_exact_probe.py` does, and for the same
    reason: that module is float64 end to end, which is what stops it
    resolving its own degeneracy.
    """
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)          # convention D

    def hm(nf, c, d, gen):
        r = [sp.Integer(0)] * 6
        tab = ([(0, [(1, c), (0, d)]), (1, [(1, c * h), (0, c), (1, d)]),
                (2, [(3, c), (2, d)]), (3, [(3, c * h), (2, c), (3, d)]),
                (4, [(5, c), (4, d)]), (5, [(5, c * h), (4, c), (5, d)])]
               if gen == 0 else
               [(0, [(2, c), (0, d)]), (1, [(4, c), (1, d)]),
                (2, [(2, c * h), (0, c), (2, d)]), (3, [(5, c), (3, d)]),
                (4, [(4, c * h), (1, c), (4, d)]), (5, [(5, c * h), (3, c), (5, d)])])
        for si, tgts in tab:
            if nf[si] == 0:
                continue
            for ti, co in tgts:
                r[ti] += nf[si] * co
        return r

    def word_nf(w, start=None):
        nf = start if start else [sp.Integer(1)] + [sp.Integer(0)] * 5
        for g in w:
            nf = hm(nf, sp.Integer(1), sp.Integer(0), g)
        return nf

    TR_M = [sp.Integer(1), z, z, z ** 2, z ** 2, h * z ** 2 + z]
    G = sp.zeros(6, 6)
    for i, bi in enumerate(NF_BASIS):
        for j, bj in enumerate(NF_BASIS):
            nf = word_nf(bj, start=word_nf(bi))
            G[i, j] = sp.cancel(sum(nf[k] * TR_M[k] for k in range(6)))
    return G


def main() -> int:
    q = sp.symbols("q", positive=True)
    G = gram_symbolic(q)

    # --- the blocked state, restated exactly -------------------------------
    check("H3_gram_is_identically_singular_over_Q(q)",
          sp.simplify(sp.cancel(G.det())) == 0,
          "det G = 0 identically — not a q_0 artefact")

    v = sp.Matrix([sp.Integer(-1) ** len(w) / q ** len(w) for w in NF_BASIS])
    Gv = sp.simplify(sp.cancel(G * v))
    check("radical_is_the_q_antisymmetriser",
          all(x == 0 for x in Gv),
          "G.v = 0 for v_i = (-1/q)^len(w_i), identically in q")

    # --- the repair: descend to the 5-dimensional TL_3 quotient ------------
    # The pairing descends to H_3/rad (QOU.QBeta.MarkovGramDegenerate.
    # pairing_descends), and v has a nonzero coefficient on every NF element,
    # so any five of the six cosets form a basis. Take the first five.
    G_TL = G[:5, :5]
    det_TL = sp.cancel(sp.factor(G_TL.det()))

    expected = sp.cancel(-(q ** 4 + 1) * (q ** 2 - q + 1) ** 4
                         * (q ** 2 + q + 1) ** 4 / (q ** 2 + 1) ** 10)
    check("TL3_determinant_closed_form",
          sp.simplify(det_TL - expected) == 0,
          "det G_TL = -(q^4+1)(q^2-q+1)^4(q^2+q+1)^4 / (q^2+1)^10")

    check("TL3_form_is_not_identically_singular",
          sp.simplify(det_TL) != 0,
          "the quotient form is non-degenerate over Q(q)")

    # Strictly non-singular on the WHOLE real substrate regime, not merely
    # generically: no real roots at all.
    num = sp.numer(sp.together(det_TL))
    real_roots = [r for r in sp.solve(sp.Eq(num, 0), q) if r.is_real]
    check("TL3_determinant_has_no_real_roots",
          real_roots == [],
          f"real roots: {real_roots or 'NONE'} ⇒ non-singular for EVERY real q > 0")

    # --- the exponents are the surviving block dimensions, squared ---------
    # Partitions of 3 with < 3 rows survive under D (qou-8iru): (3) dim 1,
    # (2,1) dim 2. Their squares are the multiplicities in the determinant.
    poly = sp.factor_list(sp.cancel(num))
    mults = sorted(m for _f, m in poly[1])
    check("TL3_determinant_exponents_are_block_dims_squared",
          mults == [1, 4, 4],
          f"factor multiplicities {mults} = dim(3)^2 = 1 and dim(2,1)^2 = 4 (twice)")

    # --- independent route: the Wedderburn product -------------------------
    def qint(m):
        return (q ** m - q ** (-m)) / (q - q ** (-1))

    y3 = sp.cancel(qint(4) / qint(2) ** 3)     # y_(3)   = [4]/[2]^3
    y21 = sp.cancel(qint(2) / qint(2) ** 3)    # y_(2,1) = [2]/[2]^3
    pred = sp.cancel(y3 ** 1 * y21 ** 4)
    J = (q ** 4 + q ** 2 + 1) ** 2 / q ** 4
    check("TL3_determinant_matches_wedderburn_up_to_a_perfect_square",
          sp.simplify(sp.cancel(-(J ** 2) * pred) - det_TL) == 0,
          "det_B(G) = det(P)^2 det_W(G): NF basis is not the matrix-unit basis")

    n_fail = sum(1 for _n, p, _d in _CHECKS if not p)
    print()
    print("=== TL_3 quotient form: non-singular, exactly ===")
    print(f"VERDICT: {len(_CHECKS) - n_fail}/{len(_CHECKS)} PASS. The TL_3 target of "
          f"qou-cds2's named repair is WELL-POSED: the quotient form is "
          f"non-singular for every real q > 0, its determinant is closed-form, and "
          f"its factor multiplicities reproduce the surviving Wedderburn block "
          f"dimensions squared. Scope-(b) structural. This does NOT perform the "
          f"migration and wires nothing; it removes the risk that the 2-3 day "
          f"engine move lands on a form that is still degenerate.")
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
