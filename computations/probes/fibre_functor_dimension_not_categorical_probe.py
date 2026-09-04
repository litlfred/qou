#!/usr/bin/env python3
"""A fibre functor changes dimensions, not fusion rules — so no fibre functor
of the single-fibre category hosts the eightfold way.

Front 2 of PR #6458 (bean `qou-yjwg`), re-posing cheat-sheet §4-A.

**The question this answers.** The eightfold programme's live surface was
recorded (2026-08-07, `qou-y7vg` / T3g) as "does QOU's braided category admit
inequivalent fibre functors?", on the reasoning that a three-dimensional
flavour object might arrive as the image of the fundamental `V` under a
different fibre functor `tau'`, with `dim tau'(V) = 3`.

**Exact facts established here, all in `QQ(q)` / `ZZ`, no floating point.**

  F1. Such fibre functors EXIST, at every dimension `n >= 2`, and at the
      substrate `q_0` they are real.  Bichon (2003) proves that for
      `E in GL_n(k)` with

          tr(E^{-1} E^t) = -q - q^{-1}

      the comodule category of the bilinear-form quantum group `B(E)` is
      monoidally equivalent to that of `O_q(SL_2)`, sending the fundamental
      of `O_q(SL_2)` (dimension 2) to the fundamental of `B(E)` (dimension
      `n`).  This probe exhibits, for `n = 3..6`, an explicit `E` over
      `QQ(q)[b]` with `b` a root of a quadratic whose discriminant is
      positive at every real `q > 0`, so `E` is real at `q_0`.  It also
      checks the `n = 2` sanity case: the standard `E_q = [[0,1],[-1/q,0]]`
      satisfies the condition, recovering `O_q(SL_2)` itself.

  F2. A fibre functor is monoidal and exact, so it carries the
      Clebsch-Gordan decomposition `V (x) V_j = V_{j+1/2} (+) V_{j-1/2}` of
      `Rep(SL_q(2))` (generic `q`) to dimensions satisfying
      `d_{k+2} = n d_{k+1} - d_k`, `d_0 = 1`, `d_1 = n`.  Under a
      3-dimensional fibre functor `V^{(x)3} = V_{3/2} (+) 2 V_{1/2}` has
      dimensions `{21, 3, 3}` -- total 27, the same total as the eightfold
      `10 + 8 + 8 + 1`, and a different split.

  F3. For NO `n >= 2` is any summand of `V^{(x)3}` one-dimensional: the
      spin-0 object is absent from `V^{(x)3}` by Clebsch-Gordan parity (a
      fact about the CATEGORY), and every other summand has dimension
      `>= n`.  Nor is any summand ever 10-dimensional unless `n = 10`, in
      which case the 10-dimensional summands are copies of `V` itself and
      the split is `{980, 10, 10}`.  So the multiset `{10, 8, 8, 1}` is not
      the image of `V^{(x)3}` under any fibre functor.

  F4. The "8" that DOES appear under a 3-dimensional fibre functor
      (`V (x) V = 1 (+) 8`, i.e. `tau'(V_1)`) is not an SU(3) octet:
      its square has dimensions `{1, 8, 55}` (`V_1 (x) V_1 = V_0 (+) V_1 (+) V_2`),
      against the octet's `8 (x) 8 = 1 + 8 + 8 + 10 + 10 + 27`.  Recorded so the
      coincidence of a dimension is not read as a coincidence of
      representation theory.

**Scope, per the (a)/(b) discipline.**  F3 is a scope-(b) structural
exclusion: the named invariant is the Clebsch-Gordan parity of
`Rep(SL_q(2))`, preserved by every monoidal equivalence and every fibre
functor.  It excludes "change the fibre functor" as a route to the eightfold
way.  It does NOT exclude the eightfold way from QOU: it relocates the
missing object from the fibre functor to the CATEGORY -- an object `W` with
`Lambda^3 W != 0` -- which is exactly what QOU axiom 5 (`Lambda^2 V = 1`,
`VolumeConstraintForcesFibreTwo.lean`) forbids for the fundamental.

**Hypotheses consumed, not proved here.**  That the single-fibre category has
the `Rep(SL_q(2))` fusion rules at `q_0` (the corpus's own
`def:quantum-gauge-group` / `ex:tannaka-krein-su2`, `H = O_q(SU(2))`), that
`q_0` is not a root of unity (real, `> 1`), and Bichon's theorem.  The Lean
sibling `QOU/Eightfold/FibreFunctorDimensionNotCategorical.lean` proves the
combinatorial half (F2, F3) unconditionally.

Cross-references:
  - docs/audits/2026-09-03-fibre-functors-do-not-change-the-category.md
  - docs/audits/2026-08-25-4a-question-imports-symmetric-theory.md  (the re-posing this corrects)
  - docs/audits/2026-08-07-eightfold-live-surface-collapse.md       (where the question was set)
  - content/.../lean/QOU/BraidsAndKnots/VolumeConstraintForcesFibreTwo.lean
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

# Path bridge (subdirectory refactor): must follow the sys.path bootstrap
# above, per _path_bridge's documented USAGE.
import _path_bridge as _bridge  # noqa: E402, F401

import sympy as sp  # noqa: E402

WITNESS_OUT = HERE / "fibre-functor-dimension-not-categorical-probe.witness.json"

q, b = sp.symbols("q b")


# ── F1: Bichon forms E of every dimension n >= 2, real at q_0 ──────


def bichon_trace(E: sp.Matrix) -> sp.Expr:
    """tr(E^{-1} E^t), the invariant Bichon's condition constrains."""
    return sp.simplify((E.inv() * E.T).trace())


def standard_E_q() -> dict:
    """n = 2 sanity case: the standard q-antisymmetric form of O_q(SL_2)."""
    E = sp.Matrix([[0, 1], [-1 / q, 0]])
    tr = bichon_trace(E)
    ok = sp.simplify(tr - (-q - 1 / q)) == 0
    return {"E": str(E.tolist()), "trace": sp.sstr(tr),
            "equals_minus_q_minus_qinv": bool(ok)}


def bichon_form(n: int) -> dict:
    """E = I_{n-2} (+) [[0,1],[b,0]]: tr(E^{-1}E^t) = (n-2) + b + 1/b.

    Bichon's condition becomes b + 1/b = -(q + 1/q) - (n-2), a quadratic in
    b with discriminant ((q + 1/q) + (n-2))^2 - 4, which is > 0 for every real
    q > 0 and n >= 3 (since q + 1/q >= 2 forces the bracket >= 3 > 2).
    """
    assert n >= 3
    blocks = sp.eye(n - 2)
    E = sp.zeros(n, n)
    E[: n - 2, : n - 2] = blocks
    E[n - 2, n - 1] = 1
    E[n - 1, n - 2] = b
    tr = bichon_trace(E)
    expected = (n - 2) + b + 1 / b
    assert sp.simplify(tr - expected) == 0, (n, tr)
    # Solve the condition for b, exactly.
    cond = sp.Eq(tr, -q - 1 / q)
    sols = sp.solve(cond, b)
    assert len(sols) == 2
    disc = sp.expand((q + 1 / q + (n - 2)) ** 2 - 4)
    # Positivity of the discriminant for real q > 0: write s = q + 1/q >= 2,
    # then (s + n - 2)^2 - 4 >= (n)^2 - 4 > 0 for n >= 3.
    s = sp.symbols("s", positive=True)
    disc_in_s = sp.expand((s + (n - 2)) ** 2 - 4)
    lower_bound_at_s2 = disc_in_s.subs(s, 2)  # s >= 2 is the AM-GM floor
    assert lower_bound_at_s2 > 0, (n, lower_bound_at_s2)
    # Product of the two roots is 1 (Vieta), so both are nonzero: E invertible.
    prod = sp.simplify(sols[0] * sols[1])
    assert prod == 1, prod
    # Evaluate at the proton pin as an exact rational (17 significant digits
    # of the 50-digit pin; enough to certify the sign of b and of the
    # discriminant, which is all that is claimed).
    q0 = sp.Rational("1.1099785827513808")
    b_vals = [sp.nsimplify(sp.N(sol.subs(q, q0), 30), rational=False) for sol in sols]
    disc_q0 = sp.N(disc.subs(q, q0), 30)
    assert disc_q0 > 0
    return {
        "n": n,
        "E_block_form": "I_{n-2} (+) [[0, 1], [b, 0]]",
        "trace_E_inv_E_t": sp.sstr(tr),
        "condition": "b + 1/b = -(q + 1/q) - (n - 2)",
        "b_roots_exact": [sp.sstr(sol) for sol in sols],
        "b_root_product_vieta": sp.sstr(prod),
        "discriminant_in_q": sp.sstr(disc),
        "discriminant_lower_bound_at_q_plus_qinv_eq_2": sp.sstr(lower_bound_at_s2),
        "discriminant_at_q0_positive": bool(disc_q0 > 0),
        "b_roots_at_q0_30dps": [sp.sstr(v) for v in b_vals],
        "real_at_q0": True,
    }


# ── F2/F3: the dimension recursion and what it can never produce ────


def cg_spins(k: int) -> list[int]:
    """Twice-spins 2j of the simple summands of V^{(x)k}, with multiplicity."""
    spins = [0]
    for _ in range(k):
        nxt = []
        for s in spins:
            nxt.extend([1] if s == 0 else [s - 1, s + 1])
        spins = nxt
    return sorted(nxt if k else spins, reverse=True)


def dim_seq(n: int, k: int) -> int:
    d = [1, n]
    while len(d) <= k:
        d.append(n * d[-1] - d[-2])
    return d[k]


def cube_dims(n: int) -> list[int]:
    return [dim_seq(n, s) for s in cg_spins(3)]


def f2_f3() -> dict:
    spins3 = cg_spins(3)
    assert spins3 == [3, 1, 1], spins3
    assert 0 not in spins3
    # Parity invariant, checked out to k = 12.
    for k in range(13):
        for s in cg_spins(k):
            assert s % 2 == k % 2, (k, s)
    table = {}
    for n in (2, 3, 4, 5, 8, 10):
        dims = cube_dims(n)
        assert sum(dims) == n ** 3, (n, dims)
        assert dims[0] == n ** 3 - 2 * n
        table[str(n)] = dims
    assert table["3"] == [21, 3, 3]
    assert table["10"] == [980, 10, 10]
    eightfold = sorted([10, 8, 8, 1], reverse=True)
    # F3: no n in 2..10^4 gives a 1-dim summand, and no n gives the eightfold multiset.
    N_MAX = 10_000
    no_singlet = all(1 not in cube_dims(n) for n in range(2, N_MAX + 1))
    no_eightfold = all(sorted(cube_dims(n), reverse=True) != eightfold
                       for n in range(2, N_MAX + 1))
    # Exact, not sampled: n^3 - 2n = 10 and = 8 have no integer root.
    nn = sp.symbols("n", integer=True)
    roots10 = sp.solve(sp.Eq(nn ** 3 - 2 * nn, 10), nn)
    roots8 = sp.solve(sp.Eq(nn ** 3 - 2 * nn, 8), nn)
    assert all(not r.is_integer for r in roots10), roots10
    assert all(not r.is_integer for r in roots8), roots8
    assert no_singlet and no_eightfold
    return {
        "cg_twice_spins_of_cube": spins3,
        "spin_zero_absent_from_cube": True,
        "parity_invariant_checked_to_k": 12,
        "cube_dims_by_fibre_dimension": table,
        "cube_total_is_n_cubed": True,
        "no_one_dim_summand_n_2_to_N": N_MAX,
        "no_eightfold_multiset_n_2_to_N": N_MAX,
        "n3_minus_2n_eq_10_integer_roots": [sp.sstr(r) for r in roots10 if r.is_integer],
        "n3_minus_2n_eq_8_integer_roots": [sp.sstr(r) for r in roots8 if r.is_integer],
    }


# ── F4: the 8 that appears is not the octet ────────────────────────


def f4() -> dict:
    # V (x) V at n = 3: spins {2, 0} -> dims {8, 1}.
    vv = sorted([dim_seq(3, s) for s in cg_spins(2)], reverse=True)
    assert vv == [8, 1], vv
    # V_1 (x) V_1 = V_0 (+) V_1 (+) V_2 (Clebsch-Gordan for spins 1, 1): twice-spins 0, 2, 4.
    sq8 = sorted([dim_seq(3, s) for s in (0, 2, 4)], reverse=True)
    assert sq8 == [55, 8, 1], sq8
    assert sum(sq8) == 64
    octet_sq = sorted([27, 10, 10, 8, 8, 1], reverse=True)
    assert sum(octet_sq) == 64 and sq8 != octet_sq
    return {
        "V_tensor_V_dims_at_n3": vv,
        "tau_V1_is_8_dimensional": True,
        "square_of_that_8": sq8,
        "square_of_su3_octet": octet_sq,
        "same_total": True,
        "same_multiset": False,
    }


def main() -> int:
    f1 = {"n2_standard_form": standard_E_q(),
          "forms": [bichon_form(n) for n in (3, 4, 5, 6)]}
    assert f1["n2_standard_form"]["equals_minus_q_minus_qinv"]
    f23 = f2_f3()
    f4r = f4()

    print("F1  Bichon forms E with tr(E^-1 E^t) = -q - 1/q")
    print(f"      n=2 standard E_q satisfies the condition: "
          f"{f1['n2_standard_form']['equals_minus_q_minus_qinv']}")
    for row in f1["forms"]:
        print(f"      n={row['n']}: b roots at q0 = {row['b_roots_at_q0_30dps']}, "
              f"disc>0: {row['discriminant_at_q0_positive']}")
    print("\nF2  dims of V^(x)3 under a fibre functor of dimension n")
    for n, dims in f23["cube_dims_by_fibre_dimension"].items():
        print(f"      n={n:>2}: {dims}   (sum {sum(dims)})")
    print("\nF3  no one-dimensional summand of V^(x)3 for any n >= 2 (checked to "
          f"n={f23['no_one_dim_summand_n_2_to_N']}; spin 0 absent by parity, exact)")
    print(f"      n^3-2n = 10 integer roots: {f23['n3_minus_2n_eq_10_integer_roots']}; "
          f"= 8: {f23['n3_minus_2n_eq_8_integer_roots']}")
    print("\nF4  the 8 at n=3 is tau'(V_1); its square is "
          f"{f4r['square_of_that_8']} vs octet {f4r['square_of_su3_octet']}")
    print("\nVERDICT")
    print("   fibre functors of every dimension n >= 2 exist (Bichon 2003; real at q0);")
    print("   none of them puts a singlet into V^(x)3 -- the eightfold 10+8+8+1 is not")
    print("   the image of V^(x)3 under any fibre functor. Scope-(b): Clebsch-Gordan")
    print("   parity of Rep(SL_q(2)) is the invariant. The missing object is in the")
    print("   CATEGORY (Lambda^3 W != 0), which axiom 5 forbids for the fundamental.")

    out = {
        "schemaVersion": "1.0.0",
        "description": (
            "A fibre functor changes dimensions, not fusion rules: Bichon "
            "bilinear-form fibre functors of every dimension n >= 2 exist on "
            "Rep(SL_q(2)) and are real at q0, yet none puts a one-dimensional "
            "summand into V^(x)3, so the eightfold 10+8+8+1 is not the image of "
            "V^(x)3 under any fibre functor of the single-fibre category."
        ),
        "computation": {
            "script": "computations/probes/fibre_functor_dimension_not_categorical_probe.py",
            "arithmetic": "exact: sympy over QQ(q)[b] and ZZ; the only numerical "
                          "evaluation is the sign of b and of a discriminant at "
                          "the proton pin, at 30 dps, and only their signs are claimed",
        },
        "facts": {"F1_bichon_forms": f1, "F2_F3_dimensions": f23, "F4_not_the_octet": f4r},
        "summary": {
            "inequivalent_fibre_functors_exist": True,
            "three_dimensional_fibre_functor_exists_real_at_q0": True,
            "eightfold_multiset_reachable_by_fibre_functor": False,
            "scope": "(b) structural exclusion of the fibre-functor route; invariant: "
                     "Clebsch-Gordan parity of Rep(SL_q(2)), preserved by every fibre functor",
            "relocates_missing_object_to": "the category: an object W with Lambda^3 W != 0, "
                                          "forbidden for the fundamental by axiom 5",
            "lean": "QOU/Eightfold/FibreFunctorDimensionNotCategorical.lean",
        },
    }
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(out, script_path=__file__, engine="python")
    out["scriptFile"] = os.path.basename(__file__)
    WITNESS_OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\nWrote: {WITNESS_OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
