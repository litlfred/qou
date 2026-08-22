#!/usr/bin/env python3
"""The asserted ladder phase is not the eigenphase of ANY braid word on V_(2,1).

Bean `qou-pdix` (child of `qou-cds1`).  Scope-**(b)** structural exclusion, with
the invariant named and verified.

## What this closes

`qou-pdix` asks for a *derivation* of the Q_β ladder phase `α = (z−1)h/2`.  The
Lean carrier that was supposed to hold that identification asserts nothing
(`QOU.QBeta.EigenphaseCarrier.carrier_is_trivial`, proved), and its content-bearing
replacement `TransferMatrixSpectrum` states the obligation a derivation must
discharge:

    M.trace = 2·cos(eigenphase q)   ∧   M.det = 1

where `M` is the β-decay transfer matrix on the 2-dimensional irrep `V_(2,1)` of
`H₃(q)`.  This probe shows **no braid word can supply that `M`.**

## The representation, DERIVED not assumed

`σ₁ = diag(q, −q⁻¹)` on the standard tableaux `[[1,2],[3]]`, `[[1,3],[2]]` (1 and
2 share a row in the first, a column in the second).  `σ₂` is then *forced*: the
Hecke relation (trace `h`, determinant `−1`) plus the braid relation
`σ₁σ₂σ₁ = σ₂σ₁σ₂` have a unique non-diagonal solution,

    σ₂ = [[ d₂ , b ], [ c , d₁ ]],   d₂ = −1/(q(q²+1)),  d₁ = q³/(q²+1),
    b·c = d₁d₂ + 1 = (q⁴+q²+1)/(q²+1)²

`b` and `c` individually are gauge; only `b·c` is fixed.  **That product is
exactly `hoefsmitB(q)²`** — so the corpus constant `hoefsmitB = √(q⁴+q²+1)/(q²+1)`
is recovered here as the off-diagonal coupling of the seminormal form rather
than imported (assertion 2).

## The invariant

**Every character of this representation lies in ℤ[q, q⁻¹].**  `b` appears in a
trace only through `b·c`, which is rational, so the square root never survives.
Verified exhaustively on every word of length 2, 4 and 6 (17 distinct traces,
**0** exceptions) — assertion 4.

**`2cos((z−1)h/2)` is not in ℤ[q, q⁻¹].**  `(z_C−1)h/2` is a non-constant
*algebraic* function of `q` (`z_C = √q/(1+q)`), and the cosine of a non-constant
algebraic function is not algebraic — while every Laurent polynomial is.  So the
two cannot agree **as functions of q**.

**This is the load-bearing step, and it is about functional identity — not about
a numerical gap.**  Assertion 5 measures the separation at `q₀` only, and that
separation is *small* (≈2.7e-3, and the nearest trace is the trivial identity
word).  It is reported for completeness and is **not** what the exclusion rests
on: a derivation would have to establish an identity of functions, and no
Laurent polynomial is an admissible candidate.  Correspondingly, this does not
rule out a numerical coincidence at one anchor — see Scope.

## The exclusion, and why scalar normalisation does not rescue it

Let `M = λ·ρ(w)` for a scalar `λ` and any braid word `w` of length `L`.
`det ρ(σ_i^{±1}) = −1`, so `det ρ(w) = (−1)^L` and `det M = λ²(−1)^L`.  Requiring
`det M = 1` forces `L` even and `λ² = 1`, i.e. `λ = ±1`.  Then

    trace M = ±(an element of ℤ[q,q⁻¹])

and `2cos((z−1)h/2)` is not.  **So no scalar multiple of any braid word has the
asserted spectrum** — the identification is not merely underived, it is
*underivable in the stated form*.

## Scope, stated precisely

This excludes `M_β = λ·ρ(w)`, `w` a braid word in `H₃(q)`, `λ` scalar.  It does
**not** exclude:

  * an `M_β` built from a *non-scalar* normalisation (e.g. divided by a
    Markov-trace factor that is itself q-dependent and non-rational);
  * an `M_β` outside the image of the braid group — a general element of
    `H₃(q)`, or an operator on a larger space restricted to `V_(2,1)`;
  * the ladder's numerics, which are untouched.  `α`'s *value* is not in
    question here; its *identification as a braid-word eigenphase* is;
  * a **numerical coincidence at a single anchor**.  The exclusion is a
    statement about identity of functions of `q`.  At `q₀` alone the closest
    enumerated trace sits only ≈2.7e-3 away, so nothing here says a braid word
    cannot come numerically close — only that none *is* the phase.

Per AGENTS.md §"Before declaring refuted", the (b) classification is used
because a proved invariant (integrality of Hecke characters, verified) forbids
the whole class — not because a numerical search came up empty.

## Method

Exact symbolic ℚ(q) via sympy throughout; the single numerical evaluation
(assertion 5) is mpmath at 40 dps and is used only to exhibit a separation, not
to decide anything.  No float64.  AGENTS.md §"PROBES ARE NOT EXEMPT".
"""
from __future__ import annotations

import itertools
import sys

import mpmath as mp
import sympy as sp

q = sp.symbols("q", positive=True)


def build_rep():
    """Return (σ₁, σ₂) in the seminormal form, with σ₂ FORCED by the relations."""
    h = q - 1 / q
    s1 = sp.Matrix([[q, 0], [0, -1 / q]])
    a, b, c = sp.symbols("a b c")
    s2 = sp.Matrix([[a, b], [c, h - a]])          # trace = h imposed
    braid = sp.expand(s1 * s2 * s1 - s2 * s1 * s2)
    eqs = [sp.Eq(braid[i, j], 0) for i in range(2) for j in range(2)]
    eqs.append(sp.Eq(sp.simplify(s2.det()), -1))  # det = -1
    sols = sp.solve(eqs, [a, b, c], dict=True)
    nondiag = [S for S in sols if sp.simplify(S.get(b, b)) != 0]
    return s1, sols, nondiag


def main() -> int:
    failures: list[str] = []

    def check(name: str, ok: bool, detail: str) -> None:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        if not ok:
            failures.append(name)

    print("Assertions (exact symbolic ℚ(q) unless stated):")

    s1, sols, nondiag = build_rep()
    check(
        "1. braid + Hecke relations force sigma_2 up to gauge",
        len(nondiag) == 1,
        f"{len(sols)} solution(s), {len(nondiag)} non-diagonal (the irrep)",
    )

    S = nondiag[0]
    a_, b_, c_ = sp.symbols("a b c")
    d2 = sp.simplify(S[a_])
    d1 = sp.simplify((q - 1 / q) - d2)
    bc = sp.simplify(sp.simplify(S[b_]) * c_)     # b solved in terms of c
    hoefsmit_sq = (q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2
    check(
        "2. b*c equals hoefsmitB^2 (the corpus constant is DERIVED here)",
        sp.simplify(bc - hoefsmit_sq) == 0
        and sp.simplify(d2 + 1 / (q * (q ** 2 + 1))) == 0
        and sp.simplify(d1 - q ** 3 / (q ** 2 + 1)) == 0,
        f"d2={d2}, d1={d1}, b*c={sp.simplify(bc)}",
    )

    # Concrete symmetric-gauge rep for the enumeration.
    B = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
    s2 = sp.Matrix([[-1 / (q * (q ** 2 + 1)), B], [B, q ** 3 / (q ** 2 + 1)]])
    h = q - 1 / q
    rel_ok = all(
        sp.simplify(M * M - h * M - sp.eye(2)) == sp.zeros(2, 2) for M in (s1, s2)
    )
    braid_ok = sp.simplify(sp.expand(s1 * s2 * s1 - s2 * s1 * s2)) == sp.zeros(2, 2)
    check(
        "3. the explicit rep satisfies Hecke + braid, det(sigma_i) = -1",
        rel_ok and braid_ok
        and sp.simplify(s1.det() + 1) == 0 and sp.simplify(s2.det() + 1) == 0,
        f"Hecke={rel_ok}, braid={braid_ok}",
    )

    # ---- 4. every character is an integral Laurent polynomial ----
    gens = {"1": s1, "2": s2, "1'": s1.inv(), "2'": s2.inv()}
    traces: dict[str, sp.Expr] = {}
    non_laurent: list[str] = []
    for L in (2, 4, 6):
        for w in itertools.product(gens, repeat=L):
            M = sp.eye(2)
            for g in w:
                M = M * gens[g]
            tr = sp.simplify(sp.expand(sp.trace(M)))
            traces.setdefault(sp.srepr(tr), tr)
            cleared = sp.simplify(sp.expand(tr * q ** (2 * L)))
            if not cleared.is_polynomial(q):
                non_laurent.append("".join(w))
                continue
            poly = sp.Poly(cleared, q)
            if not all(co.is_integer for co in poly.all_coeffs()):
                non_laurent.append("".join(w))
    check(
        "4. every character of the rep lies in Z[q,q^-1]",
        len(non_laurent) == 0,
        f"{len(traces)} distinct traces over words of length 2,4,6; "
        f"{len(non_laurent)} outside Z[q,q^-1]",
    )

    # ---- 5. the target is not among them (numerical separation only) ----
    mp.mp.dps = 40
    q0 = mp.mpf("1.1099785827513808")
    hh = q0 - 1 / q0
    zc = mp.sqrt(q0) / (1 + q0)
    target = 2 * mp.cos((zc - 1) * hh / 2)
    # Report the closest NON-TRIVIAL elliptic trace: the identity word has
    # trace 2 exactly and is not a candidate for anything.
    best, best_w = None, None
    for key, tr in traces.items():
        if sp.simplify(tr - 2) == 0:            # identity word
            continue
        val = mp.mpf(str(sp.N(tr.subs(q, sp.Rational(11099785827513808, 10 ** 16)), 30)))
        if abs(val) <= 2:
            d = abs(val - target)
            if best is None or d < best:
                best, best_w = d, (tr, val)
    check(
        "5. no enumerated character equals 2cos((z-1)h/2)  [WEAK: see docstring]",
        best is not None and best > 0,
        f"target={mp.nstr(target,14)}; closest NON-TRIVIAL elliptic trace "
        f"{best_w[0]} = {mp.nstr(best_w[1],12)}, gap {mp.nstr(best,6)} "
        f"-- small, and deliberately NOT the basis of the exclusion",
    )

    # ---- 6. scalar normalisation cannot rescue it ----
    # det(lambda*rho(w)) = lambda^2 (-1)^L = 1  =>  L even and lambda = +-1.
    check(
        "6. scalar normalisation forces lambda = +-1, so trace stays in +-Z[q,q^-1]",
        sp.simplify(s1.det() + 1) == 0 and sp.simplify(s2.det() + 1) == 0,
        "det(rho(sigma_i^{+-1})) = -1, so det(rho(w)) = (-1)^L; det = 1 pins lambda^2 = 1",
    )

    print()
    if failures:
        print(f"FAILED {len(failures)}/6: {', '.join(failures)}")
        return 1
    print("6/6 assertions hold.")
    print()
    print("EXCLUSION (scope-(b), invariant named): for M = lambda*rho(w) with w a")
    print("braid word and lambda scalar, det M = 1 forces lambda = +-1, so")
    print("trace M lies in +-Z[q,q^-1] -- while 2cos((z-1)h/2) does not. The asserted")
    print("eigenphase is therefore not merely underived but UNDERIVABLE in that form.")
    print("Does NOT exclude a non-scalar normalisation, or an M outside the braid image.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
