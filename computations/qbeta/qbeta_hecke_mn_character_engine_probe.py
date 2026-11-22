#!/usr/bin/env python3
"""qou-avt2: a general-n Iwahori-Hecke character engine from the
Murnaghan-Nakayama rule, and its validation.

WHY THIS EXISTS. The corpus's per-block Hecke characters are hand-derived and
exist ONLY at n = 3 (`chi_block_3` / `chi_block_21` / `chi_block_111` in
`computations/qbeta/qbeta_utils.py`), and the one-crossing "character collapse"
identity was likewise derived by hand. There is no general-n machinery, so every
extension past H_3 has cost a fresh hand derivation.

THE RULE. Jing-Liu, `library/arxiv-2504.18825v2/` Corollary 3.4, specialised to
m = 1 (the cyclotomic Hecke algebra H_{m,n}(q,u) reduces to the Iwahori-Hecke
algebra of type A at m = 1: (2.10) gives g_1 = u_1 scalar and g_2..g_n satisfy
the braid relations). Crucially their Hecke relation is

    g_i^2 = (q - q^-1) g_i + 1

which is EXACTLY the corpus's `sigma^2 = h*sigma + 1`, h = q - 1/q. No
convention translation is needed -- and that is worth stating explicitly, since
the C/D Markov-parameter campaign has repeatedly found value-correct code under
a wrong convention label. This is the HECKE parameter q, not a Markov z; no z
enters this file at all.

Their Corollary 3.4 at m = 1 (u_1 = 1, r = 1) reads

    chi^lambda_mu = sum_nu  q^{mu_j}/(q - q^-1) * wt(lambda/nu; q^-2) * chi^nu_{mu \ mu_j}

with wt(lambda/nu; t) = (1-t)^{cc} (-t)^{ht}, summed over nu subset lambda such
that lambda/nu is a GENERALIZED ribbon (a skew diagram with no 2x2 block, NOT
necessarily connected) of size mu_j. Since 1 - q^-2 = q^-1 * h, the prefactor
collapses and the whole rule is a monomial in q times a power of h:

    chi^lambda_mu = sum_nu  q^{mu_j - cc - 2*ht} * (-1)^{ht} * h^{cc - 1} * chi^nu_{mu \ mu_j}

That form is what this file implements, and it makes the classical limit
visible: at q -> 1, h -> 0 kills every disconnected (cc >= 2) term and leaves
(-1)^{ht} over connected ribbons -- the classical Murnaghan-Nakayama rule.

ARITHMETIC. Exact throughout: sympy over Q(q). No float anywhere, per
AGENTS.md ("PROBES ARE NOT EXEMPT"). The comparisons below are symbolic
`sp.simplify(a - b) == 0`, not numerical agreement, so "exact" here is meant
literally rather than as a statement about the arithmetic's resolution.

VALIDATION -- five checks, and note what each one is independent OF:

  1. n = 2, by hand from the eigenvalues of sigma (q and -1/q).
  2. chi^lambda_{1^n} = f^lambda (number of standard Young tableaux),
     q-INDEPENDENTLY, n = 2..6. Counted by the hook-length formula, which
     shares no code with the recursion.
  3. Classical limit q -> 1 against the symmetric-group character table
     computed by a GENUINELY DIFFERENT route: the Frobenius characteristic,
     expanding p_mu in the Schur basis by linear algebra on monomial
     coefficients in n variables. Not a second copy of Murnaghan-Nakayama.
  4. Column orthogonality of that classical limit: sum_lambda chi^l_mu chi^l_nu
     = delta_{mu,nu} z_mu.
  5. The H_3 table against the two representations that are certain a priori:
     the index rep (chi = q^len) and the sign rep (chi = (-1/q)^len).

WHAT THIS DOES NOT DO. It computes characters on the STANDARD elements
T_{gamma_mu} indexed by cycle type. It does not by itself evaluate an arbitrary
braid word -- a Hecke character is not a class function on braid words -- so it
does not yet reproduce `chi_block_*`, which are characters of the specific
nucleon word difference `beta_n - beta_p`. Bridging that is separate and is NOT
claimed here.

Ref: library/arxiv-2504.18825v2/sections/sec-002-3-murnaghannakayama-rule-for-the-cyclotomic-heck.md
Ref: library/9511222v1/ (Halverson-Ram; superseded for completeness, see qou-avt2)
"""

from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

import sympy as sp

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/qou-substrate/python", "computations"):
    _s = str(_ROOT / _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

q = sp.Symbol("q", positive=True)
h = q - 1 / q

Partition = tuple[int, ...]


# ---------------------------------------------------------------- partitions

@lru_cache(maxsize=None)
def partitions_of(n: int) -> tuple[Partition, ...]:
    """All partitions of n, weakly decreasing."""
    if n == 0:
        return ((),)
    out: list[Partition] = []

    def gen(rem: int, mx: int, acc: tuple[int, ...]) -> None:
        if rem == 0:
            out.append(acc)
            return
        for part in range(min(rem, mx), 0, -1):
            gen(rem - part, part, acc + (part,))

    gen(n, n, ())
    return tuple(out)


def cells(lam: Partition) -> set[tuple[int, int]]:
    return {(i, j) for i, row in enumerate(lam) for j in range(row)}


@lru_cache(maxsize=None)
def contained_in(lam: Partition) -> tuple[Partition, ...]:
    """Every partition nu with nu subset lambda (as Young diagrams)."""
    ranges = [range(0, part + 1) for part in lam]
    out = []
    for cand in itertools.product(*ranges):
        # must stay weakly decreasing to be a partition
        if all(cand[i] >= cand[i + 1] for i in range(len(cand) - 1)):
            out.append(tuple(x for x in cand if x > 0))
    return tuple(sorted(set(out)))


# ------------------------------------------------------- generalized ribbons

def generalized_ribbon_data(lam: Partition, nu: Partition):
    """Return (cc, ht) if lambda/nu is a generalized ribbon, else None.

    A generalized ribbon is a skew diagram containing no 2x2 block. It need NOT
    be connected -- that is exactly the difference from the classical rule, and
    it is where the h^{cc-1} factor comes from.
    """
    skew = cells(lam) - cells(nu)
    if not skew:
        return None
    for (i, j) in skew:
        if {(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)} <= skew:
            return None  # a 2x2 block

    # connected components under edge-adjacency
    unseen = set(skew)
    comps: list[set[tuple[int, int]]] = []
    while unseen:
        seed = unseen.pop()
        comp = {seed}
        stack = [seed]
        while stack:
            (i, j) = stack.pop()
            for nb in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if nb in unseen:
                    unseen.discard(nb)
                    comp.add(nb)
                    stack.append(nb)
        comps.append(comp)

    ht = sum(len({i for (i, _) in comp}) - 1 for comp in comps)
    return len(comps), ht


# ------------------------------------------------------------ the MN engine

@lru_cache(maxsize=None)
def mn_char(lam: Partition, mu: Partition) -> sp.Expr:
    """chi^lambda(T_{gamma_mu}) for the Iwahori-Hecke algebra H_n(q).

    Jing-Liu Corollary 3.4 at m = 1, in the collapsed form derived in the
    module docstring.
    """
    if sum(lam) != sum(mu):
        raise ValueError(f"size mismatch: {lam} vs {mu}")
    if not mu:
        return sp.Integer(1)

    k = mu[0]                      # strip the FIRST part (any j is valid)
    rest = tuple(mu[1:])
    total = sp.Integer(0)
    for nu in contained_in(lam):
        if sum(lam) - sum(nu) != k:
            continue
        data = generalized_ribbon_data(lam, nu)
        if data is None:
            continue
        cc, ht = data
        weight = q ** (k - cc - 2 * ht) * sp.Integer(-1) ** ht * h ** (cc - 1)
        total += weight * mn_char(nu, rest)
    return sp.simplify(sp.together(total))


def character_table(n: int) -> dict[tuple[Partition, Partition], sp.Expr]:
    return {(lam, mu): mn_char(lam, mu)
            for lam in partitions_of(n) for mu in partitions_of(n)}


# ----------------------------- independent classical route (validation only)

def _hook_length_syt_count(lam: Partition) -> int:
    """f^lambda by the hook-length formula. Shares no code with mn_char."""
    n = sum(lam)
    conj = [sum(1 for part in lam if part > j) for j in range(lam[0])] if lam else []
    num = 1
    for i in range(2, n + 1):
        num *= i
    den = 1
    for i, row in enumerate(lam):
        for j in range(row):
            den *= (row - j) + (conj[j] - i) - 1
    assert num % den == 0
    return num // den


def _schur_via_ssyt(lam: Partition, nvars: int, xs) -> sp.Expr:
    """s_lambda(x_1..x_N) as an explicit polynomial, by summing over SSYT."""
    rows = len(lam)
    if rows > nvars:
        return sp.Integer(0)
    total = sp.Integer(0)

    def fill(i: int, tableau: list[list[int]]):
        nonlocal total
        if i == rows:
            mono = sp.Integer(1)
            for row in tableau:
                for v in row:
                    mono *= xs[v]
            total += mono
            return
        width = lam[i]
        row: list[int] = []

        def place(j: int):
            lo = row[j - 1] if j > 0 else 0
            if i > 0:
                lo = max(lo, tableau[i - 1][j] + 1)
            for v in range(lo, nvars):
                row.append(v)
                if j + 1 == width:
                    fill(i + 1, tableau + [list(row)])
                else:
                    place(j + 1)
                row.pop()

        if width == 0:
            fill(i + 1, tableau + [[]])
        else:
            place(0)

    fill(0, [])
    return sp.expand(total)


def classical_table_via_frobenius(n: int) -> dict[tuple[Partition, Partition], int]:
    """chi^lambda_mu for S_n by expanding p_mu in the Schur basis.

    Deliberately a different algorithm from Murnaghan-Nakayama: it solves
    p_mu = sum_lambda chi^lambda_mu s_lambda as a linear system on monomial
    coefficients in n variables.
    """
    xs = sp.symbols(f"x0:{n}")
    lams = partitions_of(n)
    schur = {lam: _schur_via_ssyt(lam, n, xs) for lam in lams}

    monos: list[tuple[int, ...]] = []
    seen = set()
    for poly in schur.values():
        for mono in sp.Poly(poly, *xs).monoms() if poly != 0 else []:
            if mono not in seen:
                seen.add(mono)
                monos.append(mono)

    def coeffs(poly) -> list[Fraction]:
        if poly == 0:
            return [Fraction(0)] * len(monos)
        p = sp.Poly(poly, *xs)
        d = dict(zip(p.monoms(), p.coeffs()))
        return [Fraction(int(d.get(m, 0))) for m in monos]

    A = sp.Matrix([coeffs(schur[lam]) for lam in lams]).T
    out: dict[tuple[Partition, Partition], int] = {}
    for mu in partitions_of(n):
        pmu = sp.Integer(1)
        for part in mu:
            pmu *= sum(x ** part for x in xs)
        b = sp.Matrix(coeffs(sp.expand(pmu)))
        sol = A.solve_least_squares(b)
        for lam, val in zip(lams, sol):
            v = sp.nsimplify(val)
            assert v == sp.Integer(int(v)), f"non-integer character {v}"
            out[(lam, mu)] = int(v)
    return out


def _z_mu(mu: Partition) -> int:
    from collections import Counter
    z = 1
    for part, mult in Counter(mu).items():
        z *= (part ** mult)
        for i in range(2, mult + 1):
            z *= i
    return z


# ------------------------------------------------------------------- checks

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


def main() -> int:
    print(__doc__.split("\n")[0])
    print()

    # ---- 1. n = 2, from the eigenvalues of sigma ---------------------------
    print("CHECK 1 — H_2(q), against the eigenvalues q and -1/q of sigma")
    check("n2_trivial_on_sigma_is_q",
          sp.simplify(mn_char((2,), (2,)) - q) == 0,
          f"chi^(2)_(2) = {sp.simplify(mn_char((2,), (2,)))}")
    check("n2_sign_on_sigma_is_minus_qinv",
          sp.simplify(mn_char((1, 1), (2,)) + 1 / q) == 0,
          f"chi^(1,1)_(2) = {sp.simplify(mn_char((1, 1), (2,)))}")
    print()

    # ---- 2. dimensions, q-independently -----------------------------------
    print("CHECK 2 — chi^lambda_{1^n} = f^lambda, symbolically in q, n = 2..6")
    dim_ok = True
    for n in range(2, 7):
        for lam in partitions_of(n):
            got = sp.simplify(mn_char(lam, tuple([1] * n)))
            want = _hook_length_syt_count(lam)
            if sp.simplify(got - want) != 0:
                dim_ok = False
                print(f"      {lam}: got {got}, hook-length says {want}")
    check("dimension_is_syt_count_q_independent", dim_ok,
          "n = 2..6, all partitions")
    print()

    # ---- 3. classical limit vs an independent route ------------------------
    print("CHECK 3 — q -> 1 against S_n characters via the Frobenius route")
    cls_ok = True
    for n in range(2, 6):
        indep = classical_table_via_frobenius(n)
        for lam in partitions_of(n):
            for mu in partitions_of(n):
                lim = sp.limit(mn_char(lam, mu), q, 1)
                if sp.simplify(lim - indep[(lam, mu)]) != 0:
                    cls_ok = False
                    print(f"      n={n} {lam}/{mu}: MN->{lim}, Frobenius->{indep[(lam, mu)]}")
    check("classical_limit_matches_frobenius_route", cls_ok, "n = 2..5, full tables")
    print()

    # ---- 4. column orthogonality of the classical limit --------------------
    print("CHECK 4 — column orthogonality at q = 1")
    orth_ok = True
    for n in range(2, 6):
        tbl = classical_table_via_frobenius(n)
        for mu in partitions_of(n):
            for nu in partitions_of(n):
                s = sum(tbl[(lam, mu)] * tbl[(lam, nu)] for lam in partitions_of(n))
                want = _z_mu(mu) if mu == nu else 0
                if s != want:
                    orth_ok = False
                    print(f"      n={n} {mu}/{nu}: {s} != {want}")
    check("column_orthogonality_q1", orth_ok, "n = 2..5")
    print()

    # ---- 5. H_3 table, index and sign reps ---------------------------------
    print("CHECK 5 — H_3(q): index rep q^len and sign rep (-1/q)^len")
    lengths = {(1, 1, 1): 0, (2, 1): 1, (3,): 2}
    idx_ok = all(sp.simplify(mn_char((3,), mu) - q ** L) == 0
                 for mu, L in lengths.items())
    sgn_ok = all(sp.simplify(mn_char((1, 1, 1), mu) - (-1 / q) ** L) == 0
                 for mu, L in lengths.items())
    check("h3_index_rep_is_q_to_the_length", idx_ok)
    check("h3_sign_rep_is_minus_qinv_to_the_length", sgn_ok)
    print()

    # ---- the tables themselves --------------------------------------------
    tables: dict[str, dict[str, str]] = {}
    for n in (2, 3, 4):
        print(f"H_{n}(q) character table on standard elements:")
        tn: dict[str, str] = {}
        for lam in partitions_of(n):
            for mu in partitions_of(n):
                val = sp.simplify(sp.factor(mn_char(lam, mu)))
                tn[f"{lam}|{mu}"] = sp.srepr(val) if False else str(val)
                print(f"    chi^{lam}_{mu} = {val}")
        tables[f"H_{n}"] = tn
        print()

    ok = all(r[1] for r in RESULTS)
    print(f"{sum(1 for r in RESULTS if r[1])}/{len(RESULTS)} checks passed")

    try:
        from qou_substrate.witness import WitnessBuilder
        wb = WitnessBuilder("qbeta-hecke-mn-character-engine", _script_path=__file__)
        wb.set_description(
            "General-n Iwahori-Hecke character engine from the Jing-Liu "
            "Murnaghan-Nakayama rule (m=1), with five independent validations. "
            "Exact sympy over Q(q); no float, no Markov parameter."
        )
        wb.add_data("hecke_relation", "g^2 = (q - 1/q) g + 1  (matches the corpus sigma convention)")
        wb.add_data("markov_convention", "not applicable — no z enters this computation")
        # AGENTS.md asks every new witness to say which q0 pin it used. This one
        # uses NEITHER: q is a free sympy symbol throughout and no numerical
        # evaluation happens anywhere, so the q0-anchor audit's
        # Q0_ANCHOR_MISSING on this stem is correct and deliberate, not an
        # omission a later reader should "fix".
        wb.add_data("q0_anchor", "none — symbolic in q, never evaluated numerically")
        wb.add_data("character_tables", tables)
        wb.add_caveat(
            "Characters are on the STANDARD elements T_{gamma_mu} indexed by cycle "
            "type. This does NOT evaluate an arbitrary braid word, so it does not "
            "reproduce chi_block_*, which are characters of the nucleon word "
            "difference beta_n - beta_p. That bridge is not claimed here."
        )
        # add_assertion is (name, computed, expected, tolerance) -- a boolean
        # check is encoded as 1 vs 1, as STRINGS to keep it out of float64.
        # Passing (name, passed, detail) instead silently stamps the witness
        # FAILURES on an all-green run; that happened on the first run here.
        for name, passed, detail in RESULTS:
            wb.add_assertion(name, "1" if passed else "0", "1", "0",
                             source=detail or None)
        wb.save()
        print("witness written")
    except Exception as exc:  # pragma: no cover
        print(f"witness NOT written ({exc.__class__.__name__}: {exc})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
