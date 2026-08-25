#!/usr/bin/env python3
"""The Borromean `tau` closed form is the convention-**D** Markov trace (bean qou-cds1).

## The question this answers

The 2026-08-15 owner ruling makes convention **D** (`z_D = q^3/(q^2+1)`)
canonical and excises **C** (`z_C = sqrt(q)/(q+1)`).  Draining the C sites
raises a hazard AGENTS.md names explicitly: *migrating `z` is not migrating the
file* — a nominally-D file can still carry a **closed form that was solved
under C**, and substituting `z_D` into such a form is invalid (it is the banned
"substitute into a derived conclusion" move).

Two files in the probe/derived-tower drain bind a C-frame `z` **and** hard-code
the Borromean trace

    tau_Borr(h) = (4 + h^2 - 3h^4 - h^6)/(h^2 + 4)                        (T)

as a function of `h = q - 1/q` alone, citing `QOU.BraidsAndKnots`
`BorromeanMarkovTrace` / `QOU.MassTheory.tauBorromean`.  A Markov trace depends
on `z`, so (T) has had its `z` eliminated by *some* convention.  Which one is
not recorded anywhere in the corpus, and (T) carries **no half-integer power of
q**, so the `convention-c-producer-audit` C-specialised-closed-form detector
cannot see it either way -- that detector keys on a surviving `sqrt`.

If (T) were C-frame, migrating `z` in those files would leave a C-frame
constant beside a D-frame parameter.  This settles it.

## The computation

The Ocneanu trace on `H_3` is fixed by the Markov property
(`tr(1) = 1`, `tr(a s_2 b) = z tr(ab)` for `a, b` in `H_2`) together with the
Hecke relation `s^2 = h s + 1`.  On the six-element basis
`{1, s1, s2, s1s2, s2s1, s1s2s1}` it is

    tr(1) = 1,  tr(s_i) = z,  tr(s1s2) = tr(s2s1) = z^2,
    tr(s1s2s1) = z*(h*z + 1).

Reducing the Borromean braid word `(s1 s2^-1)^3` (with `s^-1 = s - h`) against
that basis gives, exactly,

    tr_M((s1 s2^-1)^3)  =  1 - h^4 * (1 + h*z - z^2).                     (B)

Comparing (B) with (T) collapses the whole convention question to a single
rational identity, since `1 - tau_Borr = h^4 (3 + h^2)/(h^2 + 4)`:

    tr_M == tau_Borr   <=>   z^2 - h*z == 1/(h^2 + 4).                    (*)

`h^2 + 4 = (q + 1/q)^2 = [2]_q^2`, so (*) reads `z^2 - h z = 1/[2]_q^2`.

## The result

`z_D = q^2/[2]_q` satisfies (*) identically:

    z_D^2 - h*z_D = (q^4 - h*q^2*[2]_q)/[2]_q^2 = (q^4 - (q^4 - 1))/[2]_q^2
                  = 1/[2]_q^2,          using h*[2]_q = q^2 - 1/q^2.

`z_C` does not, and cannot: `h*z_C = (q-1)/sqrt(q)` is irrational in `q` while
`z_C^2 = q/(q+1)^2` is rational, so `z_C^2 - h z_C` carries a half-integer
power of `q` that `1/[2]_q^2` has not got.

**So (T) is the convention-D Borromean Markov trace, and always was.**

## What this licenses, and what it does NOT

* It licenses migrating `z_C -> z_D` in the two Borromean files
  (`delta_lambda_borromean_ascaling.py`, `probes/borromean_per_lambda_fr_probe.py`)
  as a **repair**: those files pair a D-frame `tau` with a C-frame `z` today,
  which is a straddle.  Migrating `z` makes each file self-consistent.  This is
  a definition migration, not a substitution into a derived conclusion.
* It does **NOT** re-derive anything in the Q_beta `c_k` ladder, and says
  nothing about it.  The ladder remains C-frame and un-re-derived (`qou-cds1`).
* Scope-(a): this is a statement about one closed form (T), established by
  exact symbolic algebra.  It is not a claim that every `h`-only closed form in
  the corpus is D-frame; each must be checked the same way.

Exact throughout: `sympy` over `Q(s)` with `q = s^2`, so `sqrt(q) = s` and both
conventions are rational functions of `s`.  No floating-point arithmetic is
used anywhere in this probe.
"""
from __future__ import annotations

import sys

import sympy as sp

# q = s^2 makes sqrt(q) = s, so BOTH conventions are rational in s and every
# comparison below is an exact equality of rational functions -- no floats, and
# no reliance on sympy's radical simplification heuristics.
s = sp.symbols("s", positive=True)
z = sp.symbols("z")

Q = s**2
H = Q - 1 / Q

BASIS = [(), (1,), (2,), (1, 2), (2, 1), (1, 2, 1)]

TRACE = {
    (): sp.Integer(1),
    (1,): z,
    (2,): z,
    (1, 2): z**2,
    (2, 1): z**2,
    (1, 2, 1): z * (H * z + 1),
}


def reduce_word(word):
    """Reduce a braid word in {1,2} to a linear combination of BASIS.

    Uses the Hecke relation `s_i^2 = h s_i + 1` to shorten, and the braid
    relation `121 = 212` to expose a square when the word is square-free.
    """
    out: dict[tuple, sp.Expr] = {}

    def rec(w, coeff):
        w = tuple(w)
        if w in BASIS:
            out[w] = out.get(w, 0) + coeff
            return
        for i in range(len(w) - 1):
            if w[i] == w[i + 1]:                      # s^2 = h s + 1
                pre, post = w[:i], w[i + 2:]
                rec(pre + (w[i],) + post, coeff * H)
                rec(pre + post, coeff)
                return
        for i in range(len(w) - 2):                   # 121 -> 212
            a, b, c = w[i], w[i + 1], w[i + 2]
            if a == c and a != b:
                rec(w[:i] + (b, a, b) + w[i + 3:], coeff)
                return
        raise RuntimeError(f"irreducible word not in basis: {w}")

    rec(word, sp.Integer(1))
    return out


def mul(elem, gen_terms):
    """Right-multiply `elem` (dict word -> coeff) by a linear combination."""
    new: dict[tuple, sp.Expr] = {}
    for w, c in elem.items():
        for suffix, cs in gen_terms:
            for b, cb in reduce_word(w + suffix).items():
                new[b] = new.get(b, 0) + sp.expand(c * cs * cb)
    return new


def borromean_trace():
    """tr_M((s1 s2^-1)^3) as an exact polynomial in (z, h)."""
    elem = {(): sp.Integer(1)}
    s1 = [((1,), sp.Integer(1))]
    s2_inv = [((2,), sp.Integer(1)), ((), -H)]        # s^-1 = s - h
    for _ in range(3):
        elem = mul(elem, s1)
        elem = mul(elem, s2_inv)
    return sp.expand(sum(c * TRACE[b] for b, c in elem.items()))


def main() -> int:
    failures: list[str] = []

    def check(name, cond, detail):
        mark = "ok  " if cond else "FAIL"
        print(f"  [{mark}] {name}")
        print(f"         {detail}")
        if not cond:
            failures.append(name)

    tr = borromean_trace()
    tau = (4 + H**2 - 3 * H**4 - H**6) / (H**2 + 4)

    z_C = s / (Q + 1)            # 1/(sqrt q + 1/sqrt q) = sqrt(q)/(q+1)
    z_D = Q**3 / (Q**2 + 1)      # q^3/(q^2+1) = q^2/[2]_q

    print("Borromean tau: which convention eliminated the Markov parameter?")
    print()

    # 1. the reduction really did produce the advertised polynomial (B)
    closed = 1 - H**4 * (1 + H * z - z**2)
    check(
        "1. tr_M((s1 s2^-1)^3) = 1 - h^4 (1 + h z - z^2)  [exact, in H_3]",
        sp.expand(tr - closed) == 0,
        f"tr - closed form = {sp.expand(tr - closed)}",
    )

    # 2. the unlink normalisation, as a sanity anchor on the trace itself
    check(
        "2. tau_Borr(h=0) = 1 (3-component unlink, writhe-0)",
        sp.cancel(tau.subs(s, 1)) == 1,
        f"tau at h = 0 (q = 1) = {sp.cancel(tau.subs(s, 1))}",
    )

    # 3. the comparison collapses to one rational identity
    rel = sp.cancel(sp.together((tr - tau) / H**4 - (z**2 - H * z - 1 / (H**2 + 4))))
    check(
        "3. tr_M == tau  <=>  z^2 - h z == 1/(h^2+4)  [equivalent conditions]",
        sp.cancel(rel) == 0,
        "difference of the two conditions cancels identically",
    )

    # 4./5. the two conventions against that identity
    for tag, zv in (("z_C = sqrt(q)/(q+1)", z_C), ("z_D = q^3/(q^2+1)", z_D)):
        lhs = sp.cancel(sp.together(zv**2 - H * zv))
        rhs = sp.cancel(sp.together(1 / (H**2 + 4)))
        holds = sp.cancel(lhs - rhs) == 0
        n = 4 if "z_C" in tag else 5
        want = "must FAIL" if "z_C" in tag else "must HOLD"
        check(
            f"{n}. {tag}: z^2 - h z == 1/(h^2+4) ?  ({want})",
            holds == ("z_D" in tag),
            f"z^2 - h z = {lhs} ;  1/(h^2+4) = {rhs} ;  holds = {holds}",
        )

    # 6./7. and directly against the trace, independently of step 3
    for tag, zv in (("z_C", z_C), ("z_D", z_D)):
        got = sp.cancel(sp.together(tr.subs(z, zv)))
        equal = sp.cancel(got - sp.cancel(sp.together(tau))) == 0
        n = 6 if tag == "z_C" else 7
        check(
            f"{n}. tr_M at {tag} equals tau_Borr ?  "
            f"({'must FAIL' if tag == 'z_C' else 'must HOLD'})",
            equal == (tag == "z_D"),
            f"equal = {equal}",
        )

    print()
    if failures:
        print(f"FAILED {len(failures)}/7: {', '.join(failures)}")
        return 1
    print("7/7 assertions hold (exact symbolic over Q(s), q = s^2).")
    print()
    print("CONCLUSION: tau_Borr = (4 + h^2 - 3h^4 - h^6)/(h^2 + 4) is the")
    print("convention-D Borromean Markov trace. Convention C cannot produce it:")
    print("h*z_C is irrational in q while 1/[2]_q^2 is rational.")
    print()
    print("CONSEQUENCE (scope-(a)): the two files that pair this tau with a")
    print("C-frame z are internally inconsistent TODAY. Migrating z to z_D is a")
    print("repair of that straddle, not a substitution into a derived form.")
    print("This says nothing about the Q_beta c_k ladder, which stays C-frame")
    print("and un-re-derived (qou-cds1).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
