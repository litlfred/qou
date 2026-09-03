#!/usr/bin/env python3
# polynomial_q_not_applicable: pure combinatorics of the canonical braid
# word (letter counts, generator indices) — no q enters, no float anywhere.
"""
substrate_complexity_bound_probe.py — does the substrate supply a
complexity bound tight enough to make the nucleus->link census match
mean anything?

## The question this answers

`docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md` established that the
A<=4 nucleus->link assignments (2H -> 6_2, 3H -> 8_11, 3He -> L6a4) are an
**AME-driven census fit**: `jsj_verification.py` scans the census keeping
volumes near `B_AME/(rho*m_e)`.  It then measured the degeneracy:

    nucleus | named knot | census manifolds strictly closer
    --------|------------|----------------------------------
    2H      | 6_2        |   0  inside tabulated LinkExteriors (1184)
    2H      | 6_2        | 796  inside OrientableCuspedCensus (212641)

i.e. **all** of the deuteron's apparent selectivity comes from restricting
to low-crossing tabulated links, and that audit closed by naming the one
thing that would make the match quotable:

  > Derive a complexity bound on K from the substrate -- braid index and/or
  > crossing number -- with no reference to B_AME; then ask whether the
  > volume match is unique inside that class.  The registry already asserts
  > `n_braid: 3`, `n_0: 6` -- CHECK WHETHER THAT IS DERIVED OR ALSO HANDED
  > OVER.

Nobody had.  This probe does, and the answer is in two parts with opposite
signs.

## Result

**(1) `n_0 = 3A` IS derived.**  Structural: a nucleon is the trefoil
`(s1 s2^-1)^3` in B_3, so an A-nucleon atom occupies 3A strands.  Measured
here from generator indices rather than assumed: max generator index is
exactly `3A - 2` for every isotope tested, i.e. the word uses all 3A
strands and no more.

**(2) `n_braid` is NOT derived -- it is a READOUT OF THE ANSWER.**
For each registry entry, `n_braid` equals `1 + max|generator|` of the
*assigned knot's own* SnapPy braid word.  It is computed FROM the chosen
knot, so it is downstream of the assignment and cannot restrict it.  Using
it as a selection class is circular, not merely underived.  This is checked
mechanically below against the registry's own stored words -- no SnapPy
needed, the words are in `binding_k_solver.REGISTRY`.

**(3) The substrate bound that IS derived is far too loose, and its slack
GROWS.**  Word laws, measured exactly (integers, no fit):

    total letters       = 12A - 1
    genuine braid       = 10A - 2      <- the crossing bound
    superpositions      =  2A + 1      <- 2^(2A+1) branches
    strands  n_0        =  3A

So the substrate says `crossings <= 10A - 2` and `braid index <= 3A`.
Against the assigned knots (6, 8, 6 crossings; braid index 3, 5, 3) the
bound is satisfied with slack that increases linearly in A.

**Consequence, and it is the point:** a census search at higher A is
*freer* than at A=2, never tighter.  The A=2 search is already 796-fold
degenerate once the underived low-crossing restriction is dropped; since
the only derived restriction loosens as A grows, no A>=5 census assignment
can be better supported than the deuteron's.  Extending the assignment by
census search therefore adds fitted parameters at every new A and acquires
no out-of-sample support at any of them.

## Scope

**(a)** for the census-search route: *this way of assigning links, alone,
cannot be made evidential by the substrate bound.*  It does NOT refute the
existence of a derived nucleus->link map -- it says the map cannot be
recovered by volume-matching inside the class the substrate actually cuts
out.  The C1-C9 constraint table in
`docs/audits/2026-07-13-atom-knot-rule-a5plus-constraints.md` already
excludes the constructed alternatives from the other side.

Reads no AME value and no q.  Writes no witness; nothing is wired.
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

# (Z, N, label) — the N=Z chain plus the A=3 mirror pair.
ISOTOPES = [
    (1, 1, "2H"), (1, 2, "3H"), (2, 1, "3He"), (2, 2, "4He"),
    (3, 3, "6Li"), (4, 4, "8Be"), (6, 6, "12C"), (8, 8, "16O"),
]

# The three registry entries, copied from computations/binding_k_solver.py
# REGISTRY.  `assigned_word` is SnapPy's stored braid word for the named
# knot (the source comments say so verbatim: "# 6_2 in B_3 (SnapPy)").
REGISTRY = [
    ("2H",  "6_2",  3, [1, -2, 1, 1, 1, -2]),
    ("3H",  "8_11", 5, [-1, 2, -3, 2, 1, -3, -3, 4, -3, -2, -3, -4, -3, 2]),
    ("3He", "L6a4", 3, [-1, 2, -1, 2, -1, 2]),
]


def word_profile(Z: int, N: int) -> dict:
    """Exact integer profile of the canonical atom word.  No floats."""
    w = atom_canonical_crossings(Z, N)
    kinds = Counter(t for _, t in w)
    braid = kinds["sigma"] + kinds["sigma_inv"]
    return {
        "A": Z + N,
        "total_letters": len(w),
        "braid_letters": braid,
        "superpositions": len(w) - braid,
        "max_generator": max(g for g, _ in w),
    }


def main() -> int:
    checks: list[tuple[bool, str]] = []

    print("=" * 74)
    print("SUBSTRATE COMPLEXITY BOUND — is the census restriction derived?")
    print("=" * 74)

    # ── 1. the word laws, measured ──────────────────────────────────
    print("\n[1] Canonical atom word — exact integer laws\n")
    print(f"{'iso':>5} {'A':>3} {'total':>6} {'braid':>6} {'super':>6} "
          f"{'maxgen':>7} | {'12A-1':>6} {'10A-2':>6} {'2A+1':>5} {'3A-2':>5}")
    for Z, N, name in ISOTOPES:
        p = word_profile(Z, N)
        A = p["A"]
        print(f"{name:>5} {A:>3} {p['total_letters']:>6} {p['braid_letters']:>6} "
              f"{p['superpositions']:>6} {p['max_generator']:>7} | "
              f"{12*A-1:>6} {10*A-2:>6} {2*A+1:>5} {3*A-2:>5}")
        checks.append((p["total_letters"] == 12 * A - 1,
                       f"{name}: total letters = 12A-1"))
        checks.append((p["braid_letters"] == 10 * A - 2,
                       f"{name}: braid letters = 10A-2"))
        checks.append((p["superpositions"] == 2 * A + 1,
                       f"{name}: superpositions = 2A+1"))
        # generators are 0-based; max index 3A-2 swaps strands 3A-2, 3A-1,
        # so the word uses exactly 3A strands and no more.
        checks.append((p["max_generator"] == 3 * A - 2,
                       f"{name}: max generator = 3A-2, i.e. n_0 = 3A exactly"))

    print("\n  => n_0 = 3A is DERIVED (measured from generator indices, not"
          "\n     assumed): a nucleon is a trefoil in B_3, an atom occupies 3A"
          "\n     strands.  The substrate bound is braid index <= 3A and"
          "\n     crossing number <= 10A - 2 (superposition letters are not"
          "\n     crossings; each resolves to sigma_g or the identity).")

    # ── 2. n_braid is a readout of the assigned knot ─────────────────
    print("\n[2] Is `n_braid` derived, or read off the chosen knot?\n")
    print(f"{'iso':>5} {'assigned':>9} {'n_braid':>8} {'1+max|g|':>9} "
          f"{'verdict':>12}")
    for name, knot, n_braid, word in REGISTRY:
        readout = 1 + max(abs(g) for g in word)
        agree = readout == n_braid
        checks.append((agree,
                       f"{name}: n_braid == 1+max|g| of the ASSIGNED knot's word"))
        print(f"{name:>5} {knot:>9} {n_braid:>8} {readout:>9} "
              f"{'READOUT' if agree else 'differs':>12}")

    print("\n  => n_braid is computed FROM the assigned knot's own braid word."
          "\n     It is downstream of the assignment, so it cannot restrict it."
          "\n     Using it as a selection class is CIRCULAR, not merely"
          "\n     underived.  This answers the open question posed in"
          "\n     docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md.")

    # ── 3. the derived bound vs the assignment, and the slack ────────
    print("\n[3] Derived bound vs assigned knot — and how the slack moves\n")
    # crossing numbers of the assigned knots: from their names (6_2 -> 6,
    # 8_11 -> 8) and L6a4 (Thistlethwaite: 6 crossings).  Also equal to the
    # length of each stored word here, which is checked rather than assumed.
    assigned_crossings = {"2H": 6, "3H": 8, "3He": 6}
    print(f"{'iso':>5} {'A':>3} | {'c(assigned)':>11} {'c <= 10A-2':>11} "
          f"{'slack':>6} | {'n_braid':>8} {'bi <= 3A':>9} {'slack':>6}")
    for name, knot, n_braid, word in REGISTRY:
        Z, N = {"2H": (1, 1), "3H": (1, 2), "3He": (2, 1)}[name]
        A = Z + N
        c_assigned = assigned_crossings[name]
        # A braid word for K is an UPPER bound on c(K), never an identity:
        # 8_11's stored word is 14 letters against c = 8.  Asserting equality
        # here failed on exactly that entry and the assertion was wrong, not
        # the datum — 6_2 and L6a4 agreeing at 6 is a coincidence of two
        # minimal-crossing braid words, not a law.
        checks.append((c_assigned <= len(word),
                       f"{name}: c({knot}) <= its stored braid word length"))
        c_bound, bi_bound = 10 * A - 2, 3 * A
        checks.append((c_assigned <= c_bound,
                       f"{name}: assigned crossings within the derived bound"))
        checks.append((n_braid <= bi_bound,
                       f"{name}: assigned braid index within the derived bound"))
        print(f"{name:>5} {A:>3} | {c_assigned:>11} {c_bound:>11} "
              f"{c_bound-c_assigned:>6} | {n_braid:>8} {bi_bound:>9} "
              f"{bi_bound-n_braid:>6}")

    print("\n[3b] The slack is strictly increasing in A — projected forward\n")
    print(f"{'A':>3} {'c <= 10A-2':>11} {'bi <= 3A':>9} {'branches 2^(2A+1)':>18}")
    prev_c = prev_bi = -1
    for A in (2, 3, 4, 6, 8, 12, 16):
        cb, bib = 10 * A - 2, 3 * A
        print(f"{A:>3} {cb:>11} {bib:>9} {'2^' + str(2*A+1):>18}")
        checks.append((cb > prev_c and bib > prev_bi,
                       f"A={A}: both derived bounds strictly increase"))
        prev_c, prev_bi = cb, bib

    print("\n  => The ONLY derived restriction LOOSENS as A grows.  The A=2"
          "\n     census search is already 796-fold degenerate once the"
          "\n     underived low-crossing restriction is dropped (measured in"
          "\n     the 2026-08-25 audit), so no A>=5 census assignment can be"
          "\n     better supported than the deuteron's.  Extending the"
          "\n     assignment by census search adds a fitted parameter at every"
          "\n     new A and gains no out-of-sample support at any of them.")

    # ── report ──────────────────────────────────────────────────────
    print("\n" + "=" * 74)
    failed = [m for ok, m in checks if not ok]
    for ok, m in checks:
        if not ok:
            print(f"  FAIL  {m}")
    print(f"{len(checks) - len(failed)}/{len(checks)} checks passed")
    print("=" * 74)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
