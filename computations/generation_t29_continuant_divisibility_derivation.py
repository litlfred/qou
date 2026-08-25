#!/usr/bin/env python3
"""Route A of the three-generation question: DERIVE the primality condition.

Companion to `generation_count_t29_truncation_probe.py`, which localised
"why three generations" to the single lemma WHAT EXCLUDES T(2,9)? and
recorded that the primality condition ("odd primes") appears in the
corpus exactly once, as an underived parenthetical. That probe listed
three routes and marked **Route A (derive primality)** as "the one with
an actual payoff (3 generations, not merely <= 4)".

THIS script executes Route A on the normal-form data, with the
matching sorry-free Lean invariant in
`QOU/Archimedean/lepton_continuant_generation_exclusion.lean`.

THE CLAIM. The sigma-coefficient b_n of the Groebner-Shirshov normal
form of T(2,n) = sigma_0^n -- the Morgan-Voyce continuant of
`prop:lepton-continuant-recurrence`,

    NF(sigma_0^n) = a_n * 1 + b_n * sigma_0,
    b_0 = 0, b_1 = 1, b_{n+1} = h * b_n + b_{n-1},   h = q - 1/q

-- satisfies the Fibonacci-polynomial divisibility

    b_a  |  b_n   (as polynomials in h)   <==>   a | n.

Consequence on the genus-admissible odd windings {3,5,7,9}: 9 = 3*3 is
the UNIQUE composite, and b_3 | b_9 with the explicit harmonic cofactor
b_9 = b_3 * (h^6 + 6h^4 + 9h^2 + 1). The prime windings 3, 5, 7 are
mutually non-divisible (each leaves a unit remainder). So "n odd prime"
= "b_n does not factor through a smaller winding's coefficient" -- the
asserted parenthetical, now DERIVED at the normal-form level.

This is done in exact integer arithmetic on Z[h] (no q_0, no floats):
the divisibility is a statement about the continuant polynomials, so it
holds identically in the Hecke parameter and needs no evaluation. That
also keeps it clear of the failed net->mass validation from the sibling
probe: this derivation is entirely at the normal-form level.

HONEST SCOPE (scope-(a), not scope-(b)). This derives the
harmonic/factorisation distinction on the normal-form coefficient. It
does NOT prove T(2,9) cannot be a physical state -- T(2,9) is a genuine
prime knot of genus 4, and the map from the continuant to a physical
lepton mass is still open (the sibling probe's net->mass validation
FAILED and was not patched with a fitted scale). What is closed is the
corpus's asserted-not-derived primality parenthetical. The remaining
bridge -- "normal-form-independent winding => physical generation",
plus the mass map -- stays open (bean qou-x4qm).
"""

from __future__ import annotations

import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder  # noqa: E402


# --- exact polynomial arithmetic in Z[h]; a poly is a coeff list, index=power ---

def _mul_h(p):
    return [0] + p


def _add(p, q):
    n = max(len(p), len(q))
    r = [0] * n
    for i in range(len(p)):
        r[i] += p[i]
    for i in range(len(q)):
        r[i] += q[i]
    while len(r) > 1 and r[-1] == 0:
        r.pop()
    return r


def morgan_voyce_b(n_max: int):
    """b_0..b_{n_max} as integer coeff lists (Morgan-Voyce continuant)."""
    b = [[0], [1]]
    for _ in range(2, n_max + 1):
        b.append(_add(_mul_h(b[-1]), b[-2]))
    return b


def poly_divmod(num, den):
    """Exact division in Z[h]. Returns (quotient, remainder) or (None, None)
    if a leading coefficient is not divisible (never happens for these
    monic-in-leading continuants, but guarded)."""
    num = num[:]
    while len(num) > 1 and num[-1] == 0:
        num.pop()
    q = [0] * max(1, len(num) - len(den) + 1)
    while len(num) >= len(den) and any(num):
        if num[-1] == 0:
            num.pop()
            continue
        deg = len(num) - len(den)
        if num[-1] % den[-1] != 0:
            return None, None
        c = num[-1] // den[-1]
        q[deg] = c
        for i, dc in enumerate(den):
            num[deg + i] -= c * dc
        while len(num) > 1 and num[-1] == 0:
            num.pop()
    return q, num


def divides(b, a: int, n: int) -> bool:
    _, rem = poly_divmod(b[n], b[a])
    return rem == [0]


def _fmt(p) -> str:
    terms = []
    for i, c in enumerate(p):
        if c == 0:
            continue
        if i == 0:
            terms.append(f"{c}")
        elif i == 1:
            terms.append(f"{c}h")
        else:
            terms.append(f"{c}h^{i}")
    return " + ".join(reversed(terms)) if terms else "0"


def main() -> None:
    N = 11
    b = morgan_voyce_b(N)
    odd = [3, 5, 7, 9, 11]

    # (1) The general divisibility b_a | b_n <=> a | n, verified over the range.
    div_table = {}
    equivalence_holds = True
    for a in odd:
        for n in odd:
            got = divides(b, a, n)
            want = (n % a == 0)
            div_table[f"b_{a}|b_{n}"] = {"divides": got, "a_divides_n": want}
            if got != want:
                equivalence_holds = False

    # (2) The harmonic cofactor for the unique composite in {3,5,7,9}.
    cof, rem9 = poly_divmod(b[9], b[3])
    harmonic_ok = (rem9 == [0])

    # (3) Prime windings leave a unit (+-1) remainder mod b_3.
    unit_remainders = {}
    for n in (5, 7):
        _, rem = poly_divmod(b[n], b[3])
        unit_remainders[f"b_{n} mod b_3"] = {
            "remainder": _fmt(rem),
            "is_unit_pm1": rem in ([1], [-1]),
        }

    # Among {3,5,7,9}: exactly one winding (9) factors through a smaller
    # ODD winding in the set; that winding is the unique composite.
    composite_in_window = [n for n in (3, 5, 7, 9)
                           if any(a < n and n % a == 0 for a in (3, 5, 7))]
    factoring_windings = [n for n in (3, 5, 7, 9)
                          if any(a in (3, 5, 7) and a < n and divides(b, a, n)
                                 for a in (3, 5, 7))]

    wb = WitnessBuilder("generation-t29-continuant-divisibility", engine="python-int")
    wb.set_description(
        "Route A of the three-generation question (bean qou-x4qm): DERIVES "
        "the asserted 'odd primes' condition at the normal-form level. The "
        "Morgan-Voyce continuant b_n (the sigma-coefficient of the GS "
        "normal form of T(2,n), prop:lepton-continuant-recurrence) "
        "satisfies the Fibonacci-polynomial divisibility b_a | b_n <=> "
        "a | n over Z[h]. Among the genus-admissible odd windings "
        "{3,5,7,9}, 9=3*3 is the unique composite and b_9 = b_3 * "
        "(h^6+6h^4+9h^2+1); 3,5,7 are prime and mutually non-divisible. "
        "This is the precise, exact-arithmetic form of 'sigma^9=(sigma^3)^3 "
        "is a harmonic of generation 1'. Sorry-free Lean twin: "
        "QOU/Archimedean/lepton_continuant_generation_exclusion.lean. "
        "SCOPE-(a): derives the factorisation distinction, NOT that T(2,9) "
        "is unphysical (prime knot, genus 4); the net->mass map stays open "
        "(sibling witness generation-count-t29-truncation, validation "
        "FAILED, not patched).")
    wb.add_data("continuant_closed_forms", {
        f"b_{n}": _fmt(b[n]) for n in (3, 5, 7, 9)
    })
    wb.add_data("fibonacci_polynomial_divisibility", {
        "claim": "b_a | b_n  <==>  a | n   (over Z[h])",
        "verified_range": "a, n in {3,5,7,9,11}",
        "equivalence_holds": equivalence_holds,
        "table": div_table,
    })
    wb.add_data("harmonic_factorisation_of_T29", {
        "b_9 = b_3 * cofactor": harmonic_ok,
        "cofactor": _fmt(cof),
        "reading": ("winding 9's normal-form coefficient is a multiple of "
                    "winding 3's -- the exact form of the 'harmonic of "
                    "generation 1' hypothesis; b_3 | b_9."),
    })
    wb.add_data("prime_windings_are_nonharmonic", {
        "unit_remainders": unit_remainders,
        "reading": ("b_5, b_7 leave a +-1 (unit) remainder mod b_3, so b_3 "
                    "-- degree 2, not a unit of Z[h] -- cannot divide them. "
                    "3, 5, 7 are prime: no proper odd divisor > 1, hence "
                    "mutually non-divisible."),
    })
    wb.add_data("consequence_three_generations", {
        "genus_admissible_odd_windings": [3, 5, 7, 9],
        "unique_composite_in_window": composite_in_window,
        "windings_factoring_through_a_smaller_one": factoring_windings,
        "derived_statement": ("the generation windings are exactly the odd "
                              "windings whose continuant coefficient does "
                              "NOT factor through a smaller one, i.e. the "
                              "odd primes {3,5,7}; T(2,9) is the unique "
                              "harmonic and is excluded. This DERIVES the "
                              "dictionary's asserted '(odd primes)'."),
    })
    wb.add_data("honest_residual_gap", {
        "what_is_closed": ("the corpus's asserted-not-derived primality "
                           "parenthetical, now a normal-form theorem."),
        "what_stays_open": ("the physical bridge 'normal-form-independent "
                            "winding => physical generation', and the "
                            "net->mass map (sibling probe validation "
                            "FAILED). Scope-(a): this does not exclude "
                            "T(2,9) as a knot/state (bean qou-x4qm)."),
    })

    wb.add_assertion(
        name="fibonacci_polynomial_divisibility_equivalence",
        computed=int(equivalence_holds), expected=1, tolerance=0, unit="bool",
        source=("b_a | b_n <=> a | n verified exactly over a,n in "
                "{3,5,7,9,11} in Z[h] (integer polynomial division, "
                "remainder zero iff a|n)."))
    wb.add_assertion(
        name="b3_divides_b9_harmonic",
        computed=int(divides(b, 3, 9)), expected=1, tolerance=0, unit="bool",
        source=("b_9 = b_3 * (h^6+6h^4+9h^2+1): winding 9 factors through "
                "winding 3 (the harmonic of generation 1)."))
    wb.add_assertion(
        name="b3_does_not_divide_b5",
        computed=int(divides(b, 3, 5)), expected=0, tolerance=0, unit="bool",
        source="Prime winding 5 is non-harmonic (unit remainder -1 mod b_3).")
    wb.add_assertion(
        name="b3_does_not_divide_b7",
        computed=int(divides(b, 3, 7)), expected=0, tolerance=0, unit="bool",
        source="Prime winding 7 is non-harmonic (unit remainder -1 mod b_3).")
    wb.add_assertion(
        name="unique_harmonic_in_genus_window_is_T29",
        computed=len(factoring_windings), expected=1, tolerance=0, unit="count",
        source=("Exactly one of {3,5,7,9} factors through a smaller odd "
                "winding in the set -- n=9, the unique composite -- so the "
                "generation count 3 is derived from the genus bound plus "
                "the continuant divisibility."))
    out = wb.save()

    print("ROUTE A: DERIVE THE PRIMALITY CONDITION (normal-form level)")
    print("  continuant closed forms:")
    for n in (3, 5, 7, 9):
        print(f"    b_{n} = {_fmt(b[n])}")
    print(f"\n  Fibonacci-polynomial divisibility b_a|b_n <=> a|n : "
          f"{equivalence_holds}")
    print(f"  b_9 = b_3 * ({_fmt(cof)})   [b_3 | b_9]  : {harmonic_ok}")
    print("  prime windings 5,7 leave unit remainder mod b_3 (non-harmonic)")
    print(f"\n  genus-admissible odd windings : {[3,5,7,9]}")
    print(f"  unique composite / harmonic    : {factoring_windings}  (= T(2,9))")
    print("  => 3 generations DERIVED from genus bound + continuant "
          "divisibility (scope-(a); net->mass map still open)")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
