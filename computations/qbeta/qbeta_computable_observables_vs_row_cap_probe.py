#!/usr/bin/env python3
"""Does a COMPUTABLE observable escape the row cap? Two answers, and they differ.

The owner's steer (2026-09-02), in full, because both halves matter:

    "there may be more than one observable that's really in play. some may be at
     n=2 some maybe higher, but still need to take trace. some observables are
     not really direct observables of n=2, but 'computable' observables --
     operators acting at higher orders, observable at order 0 only by
     subtraction. A higher-tower operator projected down is not obviously a
     convex combination of the two crossings, which is precisely the property
     needed."

This probe was written BEFORE caveating four content surfaces with "the route is
closed", because if computable observables escaped the row cap that caveat would
be wrong on all four at once.

*** PART 1 -- THE TOWER IS RICHER THAN CROSSING MIXTURES. NOT SPECULATIVE. ***

The owner's needed property holds, and it is the Hecke quadratic relation
itself. Write an element of H_2 in the TWO-CROSSING basis, x = a.sigma +
b.sigma^-1. Since sigma^-1 = sigma - h,

    a.sigma + b.sigma^-1 = (a+b).sigma - bh
    so for x = c_1.1 + c_sigma.sigma :   b = -c_1/h ,  a = c_sigma + c_1/h

Now sigma^2 = h.sigma + 1 gives c_1 = 1, c_sigma = h, hence

    b = -1/h  <  0        for q > 1

**Two crossings compose to something OUTSIDE the segment between the two
crossings.** The convex hull of {sigma, sigma^-1} is not closed under
multiplication -- the algebra it generates is 2-dimensional, but its CONVEX
structure is not preserved. Every sigma^k, k >= 2, is outside the cone.

That is exactly the property the steer asks for, and it is elementary. So a
higher-tower operator genuinely carries structure no classical mixture of
crossings reproduces, and reading it by subtraction is a real move rather than
a re-labelling of something order 0 already had.

Measured here on the corpus's own object: `atom_braid_word_3A` returns letters
(c, d, g) denoting c.sigma_g + d.1, and EVERY letter is a convex combination of
the two crossings -- 11 pure sigma (a=1,b=0), 7 pure sigma^-1 (a=0,b=1) and 5
averaged (a=b=1/2) for the deuteron, weights >= 0 summing to 1 in every case.
So beta_atom is a convex combination of 2^5 signed braid words. Its projection
to order 0 is NOT a convex combination of the two crossings.

*** PART 2 -- BUT SUBTRACTION DOES NOT ESCAPE THE ROW CAP, BY LINEARITY ***

This is the half that decides the caveat, and it goes the other way.

A computable observable is a DIFFERENCE OF MARKOV TRACES:

    tr_M(Delta_bind) = tr_M(beta_atom) - tr_M(beta_free)

and tr_M = sum_lambda y_lambda chi_lambda with y_lambda = 0 for l(lambda) > 2 at
N = 2 (`qou-fvzm`: the row cap IS the weight vanishing, y_(1^3) = 0 because the
content-(-2) cell contributes [N-2]_q = [0]_q = 0). Subtraction is linear. A
linear combination of functionals that are blind to the tall blocks is blind to
the tall blocks. **Being computable rather than directly observed buys exactly
nothing against the row cap.**

*** THE DISTINCTION THAT SURVIVES, AND IT IS NOT A RESCUE ***

What does see the tall blocks is reading a SPECTRUM instead of a trace: the
eigenvalues of rho_lambda(Delta_bind) for l(lambda) > 2 are not weighted by
y_lambda -- they are just eigenvalues of a matrix. Measured below: for the
deuteron, rho_(3,2,1)(Delta_bind) is NONZERO while its contribution to
tr_M(Delta_bind) is exactly zero.

That is the precise sense in which the tower "carries information the trace
cannot see" -- and the precise sense in which reading it is not physical, since
the block carries no states at N = 2. It is the Path B defect (`qou-4qno`)
restated as a general principle rather than an incident.

So the caveat the four surfaces should carry is unconditional after all, but
for a reason worth stating exactly: not "the number is unverified", and not
"subtraction cannot reach it", but **every route from a >2-row block to a
physical number is either a trace (which the row cap zeroes) or a spectrum
(which has no states)**.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp
import pyhecke_native as ph

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "computations"))

DPS = 40
mp.mp.dps = DPS
Q0_STR = "1.1099785827513808075916690956107688798744991218736"
Q0 = mp.mpf(Q0_STR)
H = Q0 - 1 / Q0
Z = Q0**3 / (Q0**2 + 1)          # convention D
N_FIBRE = 2


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def two_crossing_coords(c_1, c_sigma):
    """x = c_1.1 + c_sigma.sigma  ->  x = a.sigma + b.sigma^-1."""
    b = -c_1 / H
    a = c_sigma + c_1 / H
    return a, b


def classify(a, b, tol=mp.mpf(10) ** (-(DPS - 8))):
    """Where does a.sigma + b.sigma^-1 sit relative to the two crossings?"""
    in_cone = (a > -tol) and (b > -tol)
    is_convex = in_cone and abs(a + b - 1) < tol
    return in_cone, is_convex


def tr_M_signed(signed_word, n):
    """Exact-MPFR Markov trace of a signed braid word."""
    if not signed_word:
        return mp.mpf(1)
    s = ph.tr_m_atomic_mpfr(list(signed_word), n, Q0_STR, DPS)
    return mp.mpf(s)


def letter_to_crossings(c, d):
    """(c.sigma + d.1) -> weights (a on sigma, b on sigma^-1)."""
    b = -d / H
    a = c + d / H
    return a, b


def expand_to_signed(letters):
    """Multilinear expansion into (weight, signed_word) over the two crossings."""
    terms = [(mp.mpf(1), [])]
    for (c, d, g) in letters:
        a, b = letter_to_crossings(mp.mpf(c), mp.mpf(d))
        nxt = []
        for (w, word) in terms:
            if abs(a) > mp.mpf(10) ** (-(DPS - 5)):
                nxt.append((w * a, word + [(1, int(g))]))
            if abs(b) > mp.mpf(10) ** (-(DPS - 5)):
                nxt.append((w * b, word + [(-1, int(g))]))
        terms = nxt
    return terms


def project_to_H2(terms, n):
    """Markov-orthogonal projection onto H_2 = span{1, sigma_1} <= H_n.

    E(x) = c_1.1 + c_sigma.sigma_1 is fixed by  tr_M(E(x).y) = tr_M(x.y)  for
    y in {1, sigma_1}.  The 2x2 Gram is [[tr(1), tr(s)], [tr(s), tr(s^2)]] =
    [[1, z], [z, hz+1]].
    """
    T0 = sum((w * tr_M_signed(word, n) for (w, word) in terms), mp.mpf(0))
    T1 = sum((w * tr_M_signed(word + [(1, 0)], n) for (w, word) in terms), mp.mpf(0))
    G = mp.matrix([[mp.mpf(1), Z], [Z, H * Z + 1]])
    sol = mp.lu_solve(G, mp.matrix([T0, T1]))
    return sol[0], sol[1], T0, T1


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    print("=" * 70)
    print("PART 1 — sigma^k leaves the convex hull of the two crossings")
    print("=" * 70)
    # sigma^{k+1} = h.sigma^k + sigma^{k-1}, in coords (c_1, c_sigma).
    powers = {1: (mp.mpf(0), mp.mpf(1))}
    powers[0] = (mp.mpf(1), mp.mpf(0))
    rows = []
    for k in range(2, 9):
        c1p, csp = powers[k - 1]
        c1pp, cspp = powers[k - 2]
        powers[k] = (H * c1p + c1pp, H * csp + cspp)
        aa, bb = two_crossing_coords(*powers[k])
        ic, cx = classify(aa, bb)
        rows.append({"k": k, "a": mp.nstr(aa, 12), "b": mp.nstr(bb, 12),
                     "in_cone": bool(ic), "is_convex": bool(cx)})
        print(f"  sigma^{k}:  a = {mp.nstr(aa,12):>16}   b = {mp.nstr(bb,12):>16}"
              f"   in_cone={ic}")
    ok &= chk("sigma_squared_b_coefficient_is_minus_one_over_h",
              abs(two_crossing_coords(*powers[2])[1] + 1 / H) < mp.mpf(10) ** (-30),
              True, "sigma^2 = h.sigma + 1 gives b = -1/h < 0 exactly")
    ok &= chk("no_power_k_ge_2_is_in_the_crossing_cone",
              [r["k"] for r in rows if r["in_cone"]], [],
              "composing crossings leaves the segment between them")

    print("\n" + "=" * 70)
    print("PART 2 — every atom LETTER is a convex combination of the crossings")
    print("=" * 70)
    from mass_at_3A_proper import atom_braid_word_3A
    letters_atom = atom_braid_word_3A(1, 1, include_inter=True, q=Q0)
    letters_free = atom_braid_word_3A(1, 1, include_inter=False, q=Q0)
    n_str = 6
    bad = []
    for tag, L in (("atom", letters_atom), ("free", letters_free)):
        for i, (c, d, g) in enumerate(L):
            aa, bb = letter_to_crossings(mp.mpf(c), mp.mpf(d))
            ic, cx = classify(aa, bb)
            if not cx:
                bad.append({"word": tag, "i": i, "a": mp.nstr(aa, 10),
                            "b": mp.nstr(bb, 10)})
    print(f"  atom: {len(letters_atom)} letters, free: {len(letters_free)} letters")
    print(f"  letters that are NOT convex combinations of the two crossings: {len(bad)}")
    ok &= chk("every_atom_letter_is_a_convex_combination", bad, [],
              "so the atom operator is a convex combination of signed braid words")

    print("\n" + "=" * 70)
    print("PART 3 — but the ORDER-0 PROJECTION is not")
    print("=" * 70)
    ta = expand_to_signed(letters_atom)
    tf = expand_to_signed(letters_free)
    print(f"  expansion: atom -> {len(ta)} signed words, free -> {len(tf)}")
    proj = {}
    for tag, terms in (("atom", ta), ("free", tf)):
        c1, cs, T0, T1 = project_to_H2(terms, n_str)
        aa, bb = two_crossing_coords(c1, cs)
        ic, cx = classify(aa, bb)
        proj[tag] = {"c_1": mp.nstr(c1, 14), "c_sigma": mp.nstr(cs, 14),
                     "a": mp.nstr(aa, 14), "b": mp.nstr(bb, 14),
                     "tr_M": mp.nstr(T0, 20), "in_cone": bool(ic),
                     "is_convex": bool(cx)}
        print(f"  E_2({tag:>4}):  a = {mp.nstr(aa,12):>16}  b = {mp.nstr(bb,12):>16}"
              f"  in_cone={ic}  convex={cx}")
    # Delta_bind = atom - free, and E_2 is linear.
    dterms = ta + [(-w, word) for (w, word) in tf]
    c1d, csd, T0d, T1d = project_to_H2(dterms, n_str)
    ad, bd = two_crossing_coords(c1d, csd)
    icd, cxd = classify(ad, bd)
    print(f"  E_2(Delta):  a = {mp.nstr(ad,12):>16}  b = {mp.nstr(bd,12):>16}"
          f"  in_cone={icd}  convex={cxd}")
    ok &= chk("binding_operator_projects_outside_the_crossing_cone", bool(icd), False,
              "Delta_bind's order-0 shadow is not a positive mixture of crossings")

    # Linearity of the computable observable, checked rather than assumed.
    T0a = sum((w * tr_M_signed(word, n_str) for (w, word) in ta), mp.mpf(0))
    T0f = sum((w * tr_M_signed(word, n_str) for (w, word) in tf), mp.mpf(0))
    lin_err = abs(T0d - (T0a - T0f))
    print(f"\n  tr_M(atom)  = {mp.nstr(T0a, 20)}")
    print(f"  tr_M(free)  = {mp.nstr(T0f, 20)}")
    print(f"  tr_M(Delta) = {mp.nstr(T0d, 20)}   (linearity residual {mp.nstr(lin_err,4)})")
    ok &= chk("subtraction_is_linear_in_the_markov_trace",
              lin_err < mp.mpf(10) ** (-25), True,
              "so a computable observable is itself a Markov trace")

    print("\n" + "=" * 70)
    print("PART 4 — the tall block is nonzero as an OPERATOR, zero as a TRACE")
    print("=" * 70)

    def rho(lmbda, letters):
        mats = ph.seminormal_matrices_mpfr(list(lmbda), Q0_STR, DPS)
        gens = []
        for m in mats:
            d = len(m)
            M = mp.zeros(d, d)
            for i, row in enumerate(m):
                for (j, s) in row:
                    M[i, j] = mp.mpf(s)
            gens.append(M)
        d = gens[0].rows
        acc = mp.eye(d)
        for (c, dd, g) in letters:
            acc = acc * (mp.mpf(c) * gens[int(g)] + mp.mpf(dd) * mp.eye(d))
        return acc

    tall = [3, 2, 1]
    Ra, Rf = rho(tall, letters_atom), rho(tall, letters_free)
    Rd = Ra - Rf
    nrm = max(abs(Rd[i, j]) for i in range(Rd.rows) for j in range(Rd.cols))
    y = ph.trace_weights_n(n_str, float(Q0))          # float64-ok: weight is 0/nonzero only
    parts = ph.partitions_of(n_str)
    idx = [i for i, p in enumerate(parts) if list(p) == tall][0]
    y_tall = abs(y[idx])
    print(f"  dim rho_(3,2,1) = {Rd.rows}")
    print(f"  max |rho_(3,2,1)(Delta_bind)| = {mp.nstr(nrm, 12)}")
    print(f"  Ocneanu weight |y_(3,2,1)|     = {y_tall:.6e}")
    ok &= chk("tall_block_operator_is_nonzero", nrm > mp.mpf("1e-6"), True)
    ok &= chk("tall_block_trace_weight_is_zero", y_tall < 1e-12, True,
              "so the tall block contributes exactly nothing to tr_M(Delta_bind)")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-computable-observables-vs-row-cap",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": Q0_STR, "dps": DPS, "fibre_dimension_N": N_FIBRE,
                       "trace_convention": "D (SU(2)/Temperley-Lieb)",
                       "atom": "deuteron Z=N=1, A=2, 3A=6 strands"},
        "data": {
            "sigma_powers_two_crossing_coords": rows,
            "projection": proj,
            "delta_bind_projection": {
                "c_1": mp.nstr(c1d, 14), "c_sigma": mp.nstr(csd, 14),
                "a": mp.nstr(ad, 14), "b": mp.nstr(bd, 14),
                "in_cone": bool(icd), "is_convex": bool(cxd)},
            "traces": {"atom": mp.nstr(T0a, 25), "free": mp.nstr(T0f, 25),
                       "delta": mp.nstr(T0d, 25),
                       "linearity_residual": mp.nstr(lin_err, 6)},
            "tall_block": {"partition": tall, "dim": Rd.rows,
                           "max_abs_operator_entry": mp.nstr(nrm, 12),
                           "ocneanu_weight_abs": f"{y_tall:.6e}"},
        },
        "context": {
            "axis": "does a COMPUTABLE observable -- one reached only by "
                    "subtraction -- escape the Schur-Weyl row cap?",
            "answer": "No, and the two halves of the question separate. The "
                      "tower IS richer than crossing mixtures (sigma^2 = h.sigma "
                      "+ 1 puts b = -1/h < 0, so composing two crossings leaves "
                      "the segment between them) and the binding operator's "
                      "order-0 shadow is outside the cone -- the owner's needed "
                      "property holds and is elementary. But a computable "
                      "observable is a DIFFERENCE OF MARKOV TRACES, tr_M is "
                      "linear, and every y_lambda with l(lambda) > 2 is zero at "
                      "N = 2. Subtraction buys nothing against the row cap.",
            "what_survives": "Reading a SPECTRUM rather than a trace does see the "
                             "tall blocks -- rho_(3,2,1)(Delta_bind) is nonzero "
                             "while its trace contribution is exactly zero. That "
                             "is not a rescue: the block carries no states at "
                             "N = 2. Every route from a >2-row block to a "
                             "physical number is either a trace (zeroed) or a "
                             "spectrum (stateless).",
            "scope": "Scope-(a). No content block is edited here.",
        },
        "gitCommit": _head_sha(),
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-computable-observables-vs-row-cap.witness.json"
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    with open(out_p, "w") as f:
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="proton (experimental pin)", q0_value=Q0_STR)
        # ensure_ascii=False: the corpus convention is UTF-8 witnesses, and
        # `witness_shape_guard` flags a witness that gains \uXXXX escapes.
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
