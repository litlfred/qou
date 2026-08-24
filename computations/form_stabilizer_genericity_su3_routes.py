#!/usr/bin/env python3
"""Can a degenerating 4-form reach SU(3)?  The dimension count says NO. (bean qou-8p1f)

Context
-------
After the marked-pair exclusion killed the Bring -> Klein bridge, the live
question is how else to reach a 3-dimensional fibre / colour SU(3) from the
categorical substrate.  One proposal on the table is:

    "perhaps the 4-form degenerates"

i.e. take the tetraplectic 4-form of `def:bring-cone-tetraplectic-structure`
(Foth's closed
4-form with Omega^m non-degenerate on a 4m-manifold) and let it degenerate down
the exceptional chain

    Spin(7)  ->  G_2  ->  SU(3)
    (4-form     (3-form   (SU(3)-structure
     on R^8)     on R^7)   on R^6)

which is a real chain of stabilizers, with S^7 = Spin(7)/G_2 and
S^6 = G_2/SU(3).  The last of these is already recorded in the corpus as
eightfold open-problem item 3 ("continuous G_2 completion, S^6 = G_2/SU(3)").

The test
--------
A structure "is generic" precisely when its stabilizer's GL orbit is OPEN in
the space of forms, i.e. when

    dim GL(n)  -  dim Stab  =  dim Lambda^k(R^n)*.

If the orbit is open, a *generic* form has that stabilizer and one can talk
about a form degenerating INTO the structure.  If the orbit has positive
codimension, the structure is a special stratum: a generic or arbitrary form
will never land on it, and it has to be IMPOSED rather than obtained.

This script computes those numbers exactly (they are just binomials and
Lie-algebra dimensions -- no floating point, no fitting).

Result
------
The two cases sit on opposite sides of the genericity question:

  * `G_2` on `R^7` from a 3-form: orbit is OPEN (codimension 0).  G_2 IS the
    stabilizer of a *generic* 3-form.  This is the classical fact that
    G_2-structures are "generic 3-forms in 7 dimensions".
  * `Spin(7)` on `R^8` from a 4-form: orbit has codimension 27.  Spin(7) is
    NOT the stabilizer of a generic 4-form.  Indeed dim GL(8) = 64 is already
    smaller than dim Lambda^4(R^8) = 70, so NO 4-form on R^8 has an open orbit
    -- 4-forms in dimension 8 have moduli, full stop.

Consequence for the proposal
----------------------------
**The "4-form degenerates to Spin(7), then chains to SU(3)" route does not work
by genericity.**  There is nothing for the 4-form to degenerate *into*: the
Cayley orbit is a codimension-27 stratum that an arbitrary (or tetraplectic)
4-form misses.  Reaching Spin(7) means imposing the Cayley form by hand, which
is exactly the octonionic import the route was meant to avoid -- and imposing
it one level HIGHER than the current G_2 import, since Spin(7) contains G_2.

What the same count says CONSTRUCTIVELY
---------------------------------------
The count is not purely negative.  It says the generic-form route to the
exceptional chain runs through **3-forms in dimension 7**, not 4-forms in
dimension 8.  So of the two links in `Spin(7) -> G_2 -> SU(3)`:

  * the upper link is the one that fails genericity, and
  * the lower link, `G_2 -> SU(3)` via `S^6 = G_2/SU(3)`, is untouched by this
    argument -- and is already recorded as eightfold open-problem item 3.

So the corpus's existing item 3 is on the *right* side of the genericity
question and the proposed 4-form route is on the wrong side.  If a
form-stabilizer route to SU(3) is wanted, item 3 is where the effort belongs.

Scope
-----
**scope-(b) for the specific claim "a generic/tetraplectic 4-form on an
8-manifold degenerates to a Spin(7) structure"** -- excluded by a dimension
count, which is a proved invariant.

**NOT excluded** (stated so this is not over-read):

  * imposing a Cayley form by hand.  That is consistent; it is just not a
    derivation, and it is a larger import than the status quo.
  * the lower link `G_2 -> SU(3)`.  Nothing here bears on it.
  * tetraplectic geometry generally.  This bounds one proposed USE of it; see
    bean `qou-8p1g` for the separate, and more damaging, observation that the
    Bring-cone instantiation is at `m = 1` where the tetraplectic condition is
    vacuous.
  * any route that does not go through generic-form stabilizers at all
    (Bruhat, multi-fibre groupoid).

Exact integer arithmetic only.
"""
from __future__ import annotations

import json
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
_OUT = HERE / "form-stabilizer-genericity-su3-routes.witness.json"


def dim_gl(n: int) -> int:
    """dim GL(n, R) = n^2."""
    return n * n


def lambda_dim(n: int, k: int) -> int:
    """dim of the space of alternating k-forms on R^n."""
    return comb(n, k)


# Lie-algebra dimensions of the stabilizers, standard.
DIM = {
    "G_2": 14,       # rank 2 exceptional
    "Spin(7)": 21,   # = dim so(7)
    "SU(3)": 8,      # = 3^2 - 1
    "SL(3,R)": 8,
}


def analyse(name: str, n: int, k: int, stab: str) -> dict:
    lam = lambda_dim(n, k)
    gl = dim_gl(n)
    orbit = gl - DIM[stab]
    codim = lam - orbit
    return {
        "structure": name,
        "ambient_dim": n,
        "form_degree": k,
        "dim_Lambda_k": lam,
        "dim_GL_n": gl,
        "stabilizer": stab,
        "dim_stabilizer": DIM[stab],
        "orbit_dim": orbit,
        "codim_in_forms": codim,
        "orbit_open": codim == 0,
    }


def main() -> int:
    print("=" * 74)
    print("qou-8p1f : does a degenerating 4-form reach SU(3)?")
    print("=" * 74)

    checks: dict[str, bool] = {}

    g2 = analyse("G_2 from a 3-form on R^7", 7, 3, "G_2")
    spin7 = analyse("Spin(7) from a 4-form on R^8", 8, 4, "Spin(7)")

    print("\n%-34s %8s %8s %8s %8s  %s" %
          ("structure", "dimLam", "dimGL", "orbit", "codim", "generic?"))
    print("-" * 84)
    for r in (g2, spin7):
        print("%-34s %8d %8d %8d %8d  %s" %
              (r["structure"], r["dim_Lambda_k"], r["dim_GL_n"],
               r["orbit_dim"], r["codim_in_forms"],
               "OPEN ORBIT" if r["orbit_open"] else "codim > 0 -- SPECIAL"))

    checks["G2_orbit_is_open"] = g2["orbit_open"]
    checks["Spin7_orbit_not_open"] = not spin7["orbit_open"]
    checks["Spin7_codim_27"] = spin7["codim_in_forms"] == 27

    # The blunter statement: on R^8 no 4-form can have an open orbit at all,
    # because the group is smaller than the space it acts on.
    no_open_possible = dim_gl(8) < lambda_dim(8, 4)
    checks["no_4form_on_R8_can_be_generic"] = no_open_possible
    print(f"\ndim GL(8) = {dim_gl(8)} < dim Lambda^4(R^8) = {lambda_dim(8,4)}"
          f"  =>  NO 4-form on R^8 has an open orbit : {no_open_possible}")
    print("    (4-forms in dimension 8 have moduli; 'generic 4-form' does not")
    print("     single out Spin(7), or anything else)")

    print("\ncontrast: dim GL(7) = %d >= dim Lambda^3(R^7) = %d, and the G_2"
          % (dim_gl(7), lambda_dim(7, 3)))
    print("    orbit exactly fills the space -- G_2-structures ARE generic 3-forms")

    all_ok = all(checks.values())
    print("\n" + "=" * 74)
    print(f"ALL CHECKS PASS : {all_ok}")
    print("=" * 74)
    print("""
VERDICT (bean qou-8p1f)
-----------------------
The "perhaps the 4-form degenerates" route to SU(3) does NOT work by
genericity.  There is nothing for a 4-form to degenerate INTO: on R^8 the
Cayley/Spin(7) locus is a codimension-27 stratum, and no 4-form there can be
generic because GL(8) (dim 64) is smaller than Lambda^4(R^8) (dim 70).
Reaching Spin(7) means imposing the Cayley form by hand -- the octonionic
import the route was meant to avoid, one level HIGHER than the status quo,
since Spin(7) contains G_2.

CONSTRUCTIVELY, the same count says the generic-form route runs through
3-forms in dimension 7, not 4-forms in dimension 8.  The lower link of the
chain, G_2 -> SU(3) via S^6 = G_2/SU(3), is untouched by this argument and is
already eightfold open-problem item 3.  That is where form-stabilizer effort
belongs.

SCOPE-(b) for the specific claim tested.  Does NOT exclude: imposing a Cayley
form by hand (consistent, just not a derivation); the G_2 -> SU(3) link;
tetraplectic geometry generally (see qou-8p1g for the separate m = 1 problem);
or any route not going through generic-form stabilizers.
""")

    payload = {
        "schema": "witness/v1",
        "description": (
            "Dimension count excluding the 'degenerating 4-form' route to "
            "SU(3): Spin(7) is not the stabilizer of a generic 4-form on R^8 "
            "(codim 27), and no 4-form on R^8 can be generic at all since "
            "dim GL(8) = 64 < dim Lambda^4 = 70. G_2 from a 3-form on R^7 is "
            "by contrast an open orbit. Bean qou-8p1f."
        ),
        "computation": {
            "script": "computations/form_stabilizer_genericity_su3_routes.py",
            "arithmetic": "exact integer (binomials + Lie algebra dimensions)",
        },
        "data": {
            "cases": [g2, spin7],
            "no_4form_on_R8_can_be_generic": no_open_possible,
            "verdict": (
                "the 'perhaps the 4-form degenerates' route to SU(3) fails by "
                "genericity: the Cayley/Spin(7) locus is codimension 27 and no "
                "4-form on R^8 has an open orbit, so a tetraplectic or "
                "arbitrary 4-form does not degenerate into a Spin(7) structure "
                "-- it would have to be imposed, which is a LARGER octonionic "
                "import than the status quo since Spin(7) contains G_2"
            ),
            "constructive_reading": (
                "the generic-form route runs through 3-forms in dimension 7, "
                "not 4-forms in dimension 8; the lower link G_2 -> SU(3) via "
                "S^6 = G_2/SU(3) is untouched and is already eightfold "
                "open-problem item 3, which is where form-stabilizer effort "
                "belongs"
            ),
            "scope": (
                "scope-(b) for the specific claim 'a generic/tetraplectic "
                "4-form on an 8-manifold degenerates to Spin(7)', excluded by "
                "a dimension count"
            ),
            "not_excluded": [
                "imposing a Cayley form by hand (consistent; not a derivation)",
                "the G_2 -> SU(3) link (open-problem item 3)",
                "tetraplectic geometry generally -- see qou-8p1g for the "
                "separate m = 1 vacuity observation",
                "routes not going through generic-form stabilizers (Bruhat, "
                "multi-fibre groupoid)",
            ],
            "all_checks_pass": all_ok,
            "checks": checks,
        },
    }
    _OUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {_OUT.name}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
