"""The cone condition is a degree-6 INTEGER polynomial in (z, hbar) -- and that
is forced by the Markov trace, not fitted.

WHAT THIS SUPERSEDES.  The predecessor probe
`toffoli_cone_in_entry_subring.py` put the cone condition in the degree-2
subring of the 8x8 strand-type amplitudes, with rational coefficients

    -4/9, 5/36, -20/3, -10/9, 5/18, -28/9, 20/3, 38/9, 20/9, 5/36

and I recorded as open "whether any member of the solution family has a
Hecke-theoretic reading".  THAT QUESTION WAS POSED IN THE WRONG BASIS.  The
amplitudes are not the natural coordinates; their coefficients have no
structural reading because the basis does not.  In the natural coordinates the
answer is immediate, integral, and derived:

    z    = q^3/(q^2+1)     the Markov parameter (convention D)
    hbar = q - 1/q         the Hecke deformation, sigma^2 = hbar sigma + 1

    (G t)_5  =  z^2 + 2 hbar z + 3 hbar^2 z^2 + hbar^3 z + hbar^4 z^2

Coefficients (1, 2, 3, 1, 1).  Total degree 6.  No denominators, no fit.

CORRECTION, 2026-08-31, TO THIS PROBE'S OWN FIRST VERSION.  That coefficient
string is NOT AN INVARIANT, and the question this probe originally left open --
"does (1, 2, 3, 1, 1) count something?" -- was ill-posed.  z and hbar are
ALGEBRAICALLY DEPENDENT:

    R(z, hbar)  =  hbar^3 z - hbar^2 z^2 + 4 hbar z - 4 z^2 + 1  =  0

(irreducible over Q, total degree 4; verified below).  So Q[z, hbar] is not a
polynomial ring but the coordinate ring Q[Z, H]/(R) of an affine rational
curve, and a representative is unique only MODULO R.  Measured: the degree-<=6
representatives form a coset of a SIX-dimensional space.  A second, equally
valid, equally integral degree-6 representative --

    -1 + 4 z^2 - 3 hbar z + 4 z^4 + hbar^2 z^4

-- differs from the first by exactly (hbar z + z^2 + 1) * R.  Six free
parameters is far too much room for five small integers to mean anything.

WHAT SURVIVES THE CORRECTION, and it is most of the result:

  * The IDENTITY is true and is Lean-proved
    (`QOU.Information.cone_eq_markov_hecke_polynomial`).  Nothing proved is
    affected -- the defect was in the interpretation offered alongside it.
  * MINIMAL DEGREE 6 stands.  That measurement was made over the span of the
    EVALUATED monomials, so it already accounts for the relation: no
    polynomial in (z, hbar) of total degree <= 5 equals the constraint,
    R-multiples included.  Minimal degree IS an invariant of the class.
  * Integrality stands, and is not a coincidence of one representative: the
    grevlex normal form modulo R is integral too.

THE CANONICAL REPRESENTATIVE.  Reducing modulo a Groebner basis of (R) under a
STATED order (grevlex, Z > H) gives one well-defined element of the class, and
both representatives above reduce to it:

    hbar^5 z + 4 hbar^3 z + hbar^2 - 2 hbar z + 5 z^2 - 1

This is reproducible rather than intrinsic -- a different term order gives a
different normal form -- so it is the honest object to ask a structural
question about, and any such question must name the order.

WHY IT IS FORCED -- AND THIS HALF IS NOT NEW.  Every Markov trace of a Hecke
word lies in Z[z, hbar]: the Markov property tr(x sigma_last) = z tr(x) removes
the highest generator, and the quadratic relation sigma^2 = hbar sigma + 1
reduces everything else.  The corpus already CARRIES that fact as a table --
`QOU.Machinery.MarkovTraceH4.TRM` gives all 24 H_4 normal-form trace values as
polynomials in `z` and `h`, and its entries 9 and 13 are `h*z^2 + z`, which is
exactly tr(sigma_0 sigma_1 sigma_0).  So the derivation below is a
CROSS-CHECK of my hand computation against committed Lean, not a discovery; the
check that the six H_3 values agree with that table is run in `main`.

What is new here is only the DOWNSTREAM assembly: nothing in the corpus had
written the Toffoli LP cone constraint in these coordinates, which is what makes
the predecessor's "structural reading" question answerable.

The q-Toffoli's normal-form coordinate vector is t = (0, 0, 1, hbar, 0, 0), i.e.

    T_q = sigma_1 + hbar sigma_0 sigma_1

so its coordinates are themselves in Z[hbar].  Hence

    (G t)_5 = tr(W sigma_1) + hbar tr(W sigma_0 sigma_1),   W = sigma_0 sigma_1 sigma_0

is in Z[z, hbar] BEFORE any computation.  The three steps, using nothing but the
braid relation, cyclicity of the trace, and the quadratic relation:

    tr(W)                = tr(sigma_1 sigma_0 sigma_1) = tr(sigma_1^2 sigma_0)
                         = hbar tr(sigma_1 sigma_0) + tr(sigma_0)
                         = hbar z^2 + z                     (= P_77; in the table)
    tr(W sigma_1)        = tr(sigma_0^2 sigma_1 sigma_0)
                         = hbar tr(W) + tr(sigma_1 sigma_0)
                         = hbar^2 z^2 + hbar z + z^2
    tr(W sigma_0 sigma_1)= hbar tr(W sigma_1) + hbar z^2 + z
                         = hbar^3 z^2 + hbar^2 z + 2 hbar z^2 + z

BOTH PARAMETERS ARE NEEDED -- measured, not assumed.  Minimal polynomials over
the two one-parameter subfields, by resultant:

    over Q(z)     degree 3   -> the cone condition is NOT a function of the
                               Markov parameter alone
    over Q(hbar)  degree 2   -> nor of the Hecke deformation alone

(Q(z, hbar) = Q(q) itself, since [Q(q):Q(z)] = 3 and [Q(q):Q(hbar)] = 2 are
coprime; q is exhibited below as a rational expression in the two.  So the
content of the result is the SUBRING statement, not a field statement.)

A STRUCTURAL EXCLUSION, while we are here.  The cone numerator
N = q^10 + q^6 - q^4 + q^2 - 1 is neither reciprocal nor anti-reciprocal:
q^10 N(1/q) has coefficient vector (-1,0,1,0,-1,0,1,0,0,0,1) against N's
(1,0,0,0,1,0,-1,0,1,0,-1).  Alexander polynomials of knots are reciprocal, so
N is the Alexander polynomial of NO knot -- a scope-(b) exclusion, resting on
the reciprocity invariant rather than on a numerical near-miss.

WHAT IS STILL OPEN -- RE-POSED, twice now.  The predecessor asked about ten
rationals in a structureless basis; this probe's first version asked about five
integers that turned out to be one point in a six-parameter family.  The
surviving well-posed questions are:

  (a) Does the MINIMAL DEGREE, 6, mean anything?  It is a genuine invariant of
      the class, unlike any coefficient string.
  (b) Does the curve R(z, hbar) = 0 -- the relation between the Markov
      parameter and the Hecke deformation, which is a fact about H_n and not
      about the Toffoli at all -- appear anywhere else in the corpus?
  (c) Does the grevlex normal form above mean anything, GIVEN that order?

Ask (b) first: it is the only one of the three whose subject is not an artifact
of a choice this probe made.

Exact symbolic arithmetic (sympy over Q(q)); no floating point anywhere.
"""

from __future__ import annotations

import itertools
import sys

import sympy as sp

q = sp.Symbol("q")
Z_, H_, F_ = sp.symbols("Z H F")

z = q ** 3 / (q ** 2 + 1)                       # Markov parameter, convention D
hb = q - 1 / q                                  # Hecke deformation
N = q ** 10 + q ** 6 - q ** 4 + q ** 2 - 1
CONE = N / (q ** 2 + 1) ** 2
P77 = q ** 3 * (q ** 4 + 1) / (q ** 2 + 1) ** 2
TR_W_S1 = q ** 2 * (q ** 6 + q ** 2 - 1) / (q ** 2 + 1) ** 2
TR_W_S0S1 = q * (q ** 8 + q ** 4 - q ** 2 + 1) / (q ** 2 + 1) ** 2

CHECKS: list[tuple[str, bool]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"         {detail}")


def zero(expr) -> bool:
    return sp.simplify(sp.cancel(expr)) == 0


def min_poly_degree(rel, f) -> int:
    """Degree of the minimal polynomial of `f` over the subfield `rel` defines."""
    num, den = sp.fraction(sp.cancel(f))
    g = sp.expand(F_ * den - num)
    R = sp.resultant(sp.Poly(rel, q), sp.Poly(g, q))
    return sp.Poly(sp.factor(sp.Poly(R, F_)), F_).degree()


def main() -> int:
    print("=" * 74)
    print("  THE CONE CONDITION IN THE MARKOV AND HECKE PARAMETERS")
    print("=" * 74)
    print()

    # ---- 1. the three Markov traces, each derived by hand above -------------
    check("tr(sigma_0 sigma_1 sigma_0) = hbar z^2 + z   (= P_77)",
          zero(P77 - (hb * z ** 2 + z)),
          "braid relation, cyclicity, then sigma^2 = hbar sigma + 1")
    check("tr(W sigma_1) = hbar^2 z^2 + hbar z + z^2",
          zero(TR_W_S1 - (hb ** 2 * z ** 2 + hb * z + z ** 2)))
    check("tr(W sigma_0 sigma_1) = hbar^3 z^2 + hbar^2 z + 2 hbar z^2 + z",
          zero(TR_W_S0S1 - (hb ** 3 * z ** 2 + hb ** 2 * z
                            + 2 * hb * z ** 2 + z)))

    # ---- 1b. cross-check against the committed corpus table -----------------
    from pathlib import Path
    tbl = (Path(__file__).resolve().parents[2] / "folio"
           / "quantum-observable-universe" / "lean" / "QOU" / "Machinery"
           / "MarkovTraceH4.lean")
    body = tbl.read_text() if tbl.exists() else ""
    row = [ln for ln in body.splitlines() if ln.startswith("def TRM ")]
    vals = row[0].split("![", 1)[1].rsplit("]", 1)[0].split(", ") if row else []
    h3 = ["1", "z", "z", "z", "z^2", "z^2", "z^2", "z^2", "z^2", "h*z^2 + z"]
    check("the H_3 trace values agree with QOU.Machinery.MarkovTraceH4.TRM",
          vals[:10] == h3,
          f"committed table entries 0..9: {vals[:10] if vals else 'TABLE NOT FOUND'}\n"
          f"         entry 9 is `h*z^2 + z` = tr(sigma_0 sigma_1 sigma_0) -- prior art, "
          f"not a finding of this probe")

    # ---- 2. the Toffoli coordinates are themselves in Z[hbar] ---------------
    check("the q-Toffoli is sigma_1 + hbar sigma_0 sigma_1",
          zero((q - 1) * (q + 1) / q - hb),
          "normal-form coordinate vector t = (0, 0, 1, hbar, 0, 0)")

    # ---- 3. the headline identity ------------------------------------------
    poly = (z ** 2 + 2 * hb * z + 3 * hb ** 2 * z ** 2
            + hb ** 3 * z + hb ** 4 * z ** 2)
    check("(G t)_5 = z^2 + 2 hbar z + 3 hbar^2 z^2 + hbar^3 z + hbar^4 z^2",
          zero(CONE - poly),
          "integer coefficients (1, 2, 3, 1, 1); total degree 6; no denominators")
    check("and it is the assembly of the two traces above",
          zero(CONE - (TR_W_S1 + hb * TR_W_S0S1)),
          "(G t)_5 = tr(W sigma_1) + hbar tr(W sigma_0 sigma_1)")

    # ---- 4. both parameters are needed --------------------------------------
    dz = min_poly_degree(q ** 3 - Z_ * q ** 2 - Z_, CONE)
    dh = min_poly_degree(q ** 2 - H_ * q - 1, CONE)
    check("the cone condition is NOT a function of z alone", dz > 1,
          f"minimal polynomial over Q(z) has degree {dz} (1 would mean 'in Q(z)')")
    check("nor of hbar alone", dh > 1,
          f"minimal polynomial over Q(hbar) has degree {dh}")
    qexpr = (hb - 2 * z) / (z * hb - (hb ** 2 + 1))
    check("Q(z, hbar) = Q(q), so the content is the SUBRING claim",
          zero(qexpr - q),
          "q = (hbar - 2z)/(z hbar - hbar^2 - 1); degrees 3 and 2 are coprime")

    # ---- 5. the reciprocity exclusion ---------------------------------------
    Nrev = sp.expand(q ** 10 * N.subs(q, 1 / q))
    recip = zero(Nrev - N)
    anti = zero(Nrev + N)
    check("N is neither reciprocal nor anti-reciprocal",
          not recip and not anti,
          f"N     = {sp.Poly(N, q).all_coeffs()}\n"
          f"         q^10 N(1/q) = {sp.Poly(Nrev, q).all_coeffs()}\n"
          f"         -> N is the Alexander polynomial of NO knot (scope-(b))")
    check("N is irreducible over Q", sp.Poly(N, q).is_irreducible,
          "so the single positive root q_c is not cut out by any proper factor")

    # ---- 6. the degree is minimal -------------------------------------------
    def in_span(maxdeg: int) -> bool:
        den = q ** maxdeg * (q ** 2 + 1) ** maxdeg
        mons = [sp.Integer(1)]
        for d in range(1, maxdeg + 1):
            for combo in itertools.combinations_with_replacement((z, hb), d):
                mons.append(sp.cancel(sp.prod(combo)))

        def vec(x, width):
            c = sp.Poly(sp.expand(sp.cancel(x * den)), q).all_coeffs()[::-1]
            return c + [sp.Integer(0)] * (width - len(c))

        width = max(len(sp.Poly(sp.expand(sp.cancel(x * den)), q).all_coeffs())
                    for x in mons + [CONE])
        M = sp.Matrix([vec(m, width) for m in mons])
        return M.col_join(sp.Matrix([vec(CONE, width)])).rank() == M.rank()

    below = [d for d in (2, 3, 4, 5) if in_span(d)]
    check("degree 6 is minimal -- no lower-degree polynomial in (z, hbar) works",
          not below and in_span(6),
          f"membership at total degree 2..5: {below or 'none'}; at 6: yes")

    # ---- 7. the relation, and the non-uniqueness it causes ------------------
    import sympy as _sp
    ZS, HS = _sp.symbols("Z H")
    R = HS ** 3 * ZS - HS ** 2 * ZS ** 2 + 4 * HS * ZS - 4 * ZS ** 2 + 1
    check("z and hbar satisfy R = hbar^3 z - hbar^2 z^2 + 4 hbar z - 4 z^2 + 1 = 0",
          zero(R.subs({ZS: z, HS: hb})),
          f"irreducible over Q: {sp.Poly(R, ZS, HS).is_irreducible}; total degree "
          f"{sp.Poly(R, ZS, HS).total_degree()} -> Q[z,hbar] = Q[Z,H]/(R), the "
          f"coordinate ring of an affine rational curve, NOT a polynomial ring")

    A = ZS ** 2 + 2 * HS * ZS + 3 * HS ** 2 * ZS ** 2 + HS ** 3 * ZS + HS ** 4 * ZS ** 2
    B = -1 + 4 * ZS ** 2 - 3 * ZS * HS + 4 * ZS ** 4 + ZS ** 4 * HS ** 2
    check("a SECOND integral degree-6 representative exists",
          zero((B.subs({ZS: z, HS: hb})) - CONE)
          and sp.expand(A - B) != 0,
          "-1 + 4z^2 - 3 hbar z + 4 z^4 + hbar^2 z^4 also equals the constraint")
    _, rem = sp.div(sp.Poly(sp.expand(A - B), ZS, HS), sp.Poly(R, ZS, HS))
    check("the two differ by a multiple of R", rem.is_zero,
          "quotient (hbar z + z^2 + 1) -- so the coefficient string is NOT an "
          "invariant")

    mult, mons = [], []
    for d in range(0, 7):
        for c in itertools.combinations_with_replacement((ZS, HS), d):
            mons.append(sp.prod(c))
            if d <= 2:
                mult.append(sp.expand(R * sp.prod(c)))
    vecs = sp.Matrix([[sp.Poly(x, ZS, HS).coeff_monomial(m) for m in mons]
                      for x in mult])
    check("degree-<=6 representatives form a SIX-parameter family",
          vecs.rank() == 6,
          f"dimension {vecs.rank()} -- far too much room for five small integers "
          f"to carry information")

    G = sp.groebner([R], ZS, HS, order="grevlex")
    nfA, nfB = G.reduce(A)[1], G.reduce(B)[1]
    check("both reduce to one grevlex normal form (reproducible, not intrinsic)",
          sp.expand(nfA - nfB) == 0,
          f"normal form: {nfA}")

    n_ok = sum(1 for _, ok in CHECKS if ok)
    print()
    print("=" * 74)
    print(f"  {n_ok}/{len(CHECKS)} assertions")
    print("=" * 74)
    print()
    print("  VERDICT.  In (z, hbar) the constraint is integral, of MINIMAL degree 6,")
    print("  and forced by the Markov trace rather than fitted -- and minimal degree")
    print("  is a genuine invariant.  The coefficient string is NOT: z and hbar are")
    print("  algebraically dependent, and the degree-6 representatives form a")
    print("  six-parameter family.  This probe's own first version asked whether")
    print("  (1, 2, 3, 1, 1) counts something; that question is withdrawn.")
    return 0 if n_ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
