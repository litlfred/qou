"""The tetrahedral shape parameter is INDEX-BLIND, so tau_arch cannot be a
function of the algebraic seed.

`conj:shared-denominator-cusp-holonomy` asserts that the n roots q_0^{-k} of
the q-Pochhammer denominator (x; q_0)_n "address" the cusps of the hyperbolic
piece. `snappy_cusp_seeding.py` measured the distance |q_0^{-k} - z_k| to
SnapPy's converged shapes, found ~0.4-0.9, and concluded the bijection "must be
interpreted as a bijection of *labels* ... with the actual shape parameter being
a non-trivial function tau_arch(q_0^{-k}) of the algebraic seed; the shape of
that function is the subject of further work."

This probe shows there is no such function to find, and does so WITHOUT any
distance measurement, by counting.

WHAT IS MEASURED
----------------
Read from the committed `snappy-cusp-seeding.witness.json` (SnapPy is not
re-run; nothing here depends on it being installed):

  manifold   n = #roots   distinct shape VALUES   distinct tetrahedra
                                                  up to ISOMETRY
  m004            2                1                     1
  m003            2                1                     1
  L6a4            8                2                     1

The last column is the one that matters, and it is not what the witness
records. An ideal tetrahedron has THREE shape parameters -- the orbit
z -> 1/(1-z) -> (z-1)/z of relabelling which edge is distinguished -- so two
different recorded values can be one tetrahedron. They are:

    orbit(1+i) = {1+i, i, (1+i)/2}

and L6a4's two recorded values are 1+i and (1+i)/2, both with dihedral angles
{pi/4, pi/4, pi/2}. All eight of its tetrahedra are isometric. m004 and m003
are two copies of the REGULAR ideal tetrahedron, z = exp(i*pi/3), whose orbit
is a fixed point (all three parameters equal) -- that fixed-point property IS
regularity, and it is checked here rather than asserted.

Both facts are classical (Thurston): the figure-eight complement is two
regular ideal tetrahedra, and the Borromean complement is two regular ideal
octahedra, each subdividing into four copies of the {pi/4, pi/4, pi/2}
tetrahedron. The probe confirms the committed numbers agree with them; it does
not establish them.

THE ORBIT IDENTITY IS ALREADY PROVED IN THE CORPUS -- READ THIS BEFORE
TREATING ANY LINE BELOW AS A FINDING
-------------------------------------------------------------------
`QOU/MathlibExt/IdealTriangulation.lean` is **sorry-free** and already carries
the whole relabelling structure:

    param : Fin 3 -> C  =  {z, 1/(1-z), 1 - 1/z}      -- the three edge params
    rotate : IdealTetrahedron := <1/(1-z), _>          -- docstring: "The same
                                                       --  tetrahedron, relabelled"
    shape_cycle2, shape_cycle3                         -- rotate generates a 3-cycle
    rotate_angles                                      -- angles cycle, so volume is fixed
    param_prod : param 0 * param 1 * param 2 = -1

and that file's own section header states the point this probe re-measured:
*"`z -> 1/(1-z)` does not change the tetrahedron -- it changes which edge-pair
is called 'first'. ... **This is not a coincidence to be checked
numerically**."*

So the identity `(1+i)/2 in orbit(1+i)` is NOT a result of this probe. It is
`rotate` applied twice -- `rotate(1+i) = i`, `rotate(i) = (1+i)/2` -- and the
corpus proves it. The `=== the identities ===` section below is a CONSISTENCY
CHECK of this probe's arithmetic against proved Lean, kept because a probe
whose counting rests on an identity should fail loudly if its own arithmetic
disagrees with the proof. Do not cite it as evidence for the identity; cite
`shape_cycle2` / `rotate_angles`.

What is genuinely this probe's is narrower and is entirely about the DATA:
that the committed L6a4 shape values lie in ONE `rotate` orbit, that m004's
lies at the orbit's FIXED POINT, and the counting consequence below.

THE PRUNE (scope-(b), invariant = pigeonhole on a finite set)
-------------------------------------------------------------
The n roots q_0^{-k}, k = 0..n-1, are pairwise DISTINCT, since q_0 != 1. The
shapes they would map to take exactly ONE value up to isometry. So any map

    tau_arch : {algebraic seed} -> {shape parameter}

is constant on each of these manifolds, and a constant map cannot recover k.
This kills the whole hypothesis class at once -- every injective candidate
(Moebius, exponential, any reparametrisation) AND every non-constant one.
Per AGENTS.md's refutation rule this is scope-(b) and the invariant is named:
a map from an n-set onto a 1-set is not injective, and carries no information
about its argument.

SCOPE, stated narrowly. This excludes tau_arch as a function OF THE SEED
VALUE, on the three triangulations the corpus probes. It does NOT exclude the
conjecture, and it does not touch the n != c arity point below.

WHY THE CONJECTURE SURVIVES, AND WHAT TO MEASURE INSTEAD
--------------------------------------------------------
The conjecture's own displayed right-hand side is NOT about z_k. It reads

    (x; q_0)_n = 0  <=>  Hol_{mu_k}(z_k) = 1 and Hol_{lambda_k}(z_k) = 1

i.e. about HOLONOMY. A holonomy is a product of shape parameters along the
meridian's or longitude's edge path, so it is PATH-dependent and therefore
index-dependent even when every shape is equal -- exactly the property the
shapes lack. So the conjecture's equation is better than the table row
("pole of Phi_n <-> complete cusp") and better than the witness's reading: the
existing probe measured the one object in the statement that cannot carry the
index.

The measurement that would test the conjecture is the gluing/holonomy
RESIDUAL |Hol_{mu_k} - 1| evaluated at the algebraic seeds, not the distance
|q_0^{-k} - z_k|. `snappy_cusp_seeding.py`'s second caveat already says a
genuine test needs the gluing system; this probe says the first caveat's
conclusion is about the wrong object.

WHAT THE LEAN HAS, STATED NARROWLY (do not read this as "unformalised")
----------------------------------------------------------------------
`IdealTriangulation.lean` carries `SatisfiesEdgeEquations` and
`SatisfiesAngleEquations`, and a case-insensitive scan of that file for
cusp / complete / meridian / longitude returns ZERO -- so the general
triangulation file has no cusp-completeness predicate, which is a plausible
reason the probe reached for shapes. But meridian/longitude work DOES exist
elsewhere, per-knot: `QOU/Knot/FigureEightDeformedMeridianWinding.lean`,
`QOU/Mass/FiveTwoGluingFromFareyWord.lean`,
`QOU/Mass/FiveTwoAPolynomialFromFareyWord.lean`. This probe has NOT read those
closely enough to say whether one of them already supplies the holonomy
residual it asks for. Treat "the right measurement is the holonomy residual"
as a redirection, NOT as a claim that nothing in the corpus computes it --
AGENTS.md's corpus-grep checklist gates that claim and it has not been run to
completion here.

TWO SMALLER CORRECTIONS TO THE RECORDED NEGATIVE
------------------------------------------------
1. ARITY. The displayed equivalence ranges k over the n roots on the left and
   over CUSPS on the right. Measured: n != c in all three cases (2 vs 1,
   2 vs 1, 8 vs 3), so pole-index <-> cusp-index is not a bijection of sets
   at all. The conjecture's own table row already says "n ideal tetrahedra in
   JSJ piece", so the carrier is internally inconsistent: the table is
   tetrahedron-indexed and the equation is cusp-indexed. Tetrahedron-indexing
   is the consistent reading and is what the producer actually pairs against
   (`M.tetrahedra_shapes`).
2. THE 0.4-0.9 IS MOSTLY THE PROBE'S OWN KNOB. The seeds are lifted to C by a
   fixed IM_PERTURBATION = 0.1 while the true shapes have Im = sqrt(3)/2
   = 0.866 (m004/m003) or 1 and 1/2 (L6a4). Setting the perturbation to the
   true Im collapses the m004 distances from 0.8646/0.9148 to 0.4009/0.5.
   The knob-free part of the negative is the REAL part, which no choice of
   imaginary lift can move: |Re(q_0^{-k}) - Re(z_k)| >= 0.4009 on m004. That
   is the honest form, and it is STRONGER than the reported one because it
   holds for every lift.

Bean qou-3kni; conjecture carrier
folio/quantum-observable-universe/mass-theory/shared-denominator-cusp-holonomy.md.
No fit, no calibration, no q_0 derivation: q_0 enters only as the already-pinned
substrate value, and every conclusion here is a count or an exact identity.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from mpmath import almosteq, exp, j, mp, mpc, mpf, nstr, pi

mp.dps = 60

ROOT = Path(__file__).resolve().parent
WITNESS = ROOT / "snappy-cusp-seeding.witness.json"

# Tolerance for matching SnapPy's output, which the witness stores to 10
# decimal digits. Not a precision claim about this probe's arithmetic, which is
# exact: the orbit identities below are rational/algebraic and hold at 60 dps.
SNAPPY_TOL = mpf("1e-9")


def orbit(z):
    """The three shape parameters of ONE ideal tetrahedron.

    Relabelling which edge is distinguished sends z -> 1/(1-z) -> (z-1)/z.
    Two recorded values in the same orbit are the SAME tetrahedron.
    """
    return [z, 1 / (1 - z), (z - 1) / z]


def same_tetrahedron(z, w, tol=SNAPPY_TOL):
    return any(almosteq(u, w, tol) for u in orbit(z))


def isometry_classes(shapes, tol=SNAPPY_TOL):
    """Partition recorded shape values into tetrahedra up to edge relabelling."""
    reps = []
    for z in shapes:
        if not any(same_tetrahedron(r, z, tol) for r in reps):
            reps.append(z)
    return reps


def dihedral_angles(z):
    return sorted(mp.arg(w) for w in orbit(z))


def main() -> int:
    if not WITNESS.exists():
        print(f"MISSING: {WITNESS}")
        return 2
    doc = json.loads(WITNESS.read_text())

    def dig(o, key):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == key:
                    yield v
                yield from dig(v, key)
        elif isinstance(o, list):
            for v in o:
                yield from dig(v, key)

    results = next(dig(doc, "results"), None)
    if not results:
        print("no `results` block in the committed witness")
        return 2

    ok = True
    rows = []
    print("=== shapes up to ISOMETRY, not up to equality ===\n")
    for r in results:
        shapes = [mpc(mpf(str(s["real"])), mpf(str(s["imag"])))
                  for s in r["snappy_shapes"]]
        seeds = [mpc(mpf(str(s["real"])), mpf(str(s["imag"])))
                 for s in r["algebraic_seeds"]]
        n = int(r["num_tetrahedra"])
        c = int(r["num_cusps"])

        # distinct recorded VALUES
        vals = []
        for z in shapes:
            if not any(almosteq(v, z, SNAPPY_TOL) for v in vals):
                vals.append(z)
        classes = isometry_classes(shapes)

        # the seeds are pairwise distinct -- this is what makes it pigeonhole
        distinct_seeds = []
        for s in seeds:
            if not any(almosteq(v, s, SNAPPY_TOL) for v in distinct_seeds):
                distinct_seeds.append(s)

        rows.append({
            "name": r["name"],
            "n_tetrahedra": n,
            "n_cusps": c,
            "n_roots": len(seeds),
            "distinct_seeds": len(distinct_seeds),
            "distinct_shape_values": len(vals),
            "isometry_classes": len(classes),
            "angles_per_class": [
                [nstr(a / pi, 15) for a in dihedral_angles(z)] for z in classes
            ],
        })
        print(f"{r['name']:6s} n={n} tets, c={c} cusps, {len(distinct_seeds)} "
              f"distinct seeds -> {len(vals)} distinct shape values "
              f"-> {len(classes)} tetrahedra up to isometry")
        for z in classes:
            print(f"        class rep {nstr(z, 12)}  angles/pi = "
                  f"{[nstr(a / pi, 12) for a in dihedral_angles(z)]}")
        if len(distinct_seeds) != len(seeds):
            print("        UNEXPECTED: the algebraic seeds are not distinct")
            ok = False
        if len(classes) != 1:
            print("        NOTE: more than one isometry class; the prune below "
                  "weakens from constant to non-injective for this manifold")

    # --- the two exact identities the counting rests on --------------------
    print("\n=== the identities, at 60 dps ===")
    a, b = mpc(1, 1), mpc(1, 1) / 2
    id1 = same_tetrahedron(a, b, mpf("1e-50"))
    print(f"(1+i)/2 lies in orbit(1+i)                        : {id1}")
    print(f"  orbit(1+i) = {[nstr(w, 12) for w in orbit(a)]}")
    zreg = exp(j * pi / 3)
    id2 = all(almosteq(w, zreg, mpf("1e-50")) for w in orbit(zreg))
    print(f"orbit(exp(i*pi/3)) is a fixed point (= regular)   : {id2}")
    print(f"  angles/pi = {[nstr(x / pi, 12) for x in dihedral_angles(zreg)]}")
    if not (id1 and id2):
        print("  FAIL: an exact identity the prune rests on does not hold")
        ok = False

    # --- the knob: how much of 0.4-0.9 is IM_PERTURBATION = 0.1? ----------
    print("\n=== the reported distance is dominated by the probe's own lift ===")
    m004 = next(r for r in results if r["name"] == "m004")
    zs = [mpc(mpf(str(s["real"])), mpf(str(s["imag"])))
          for s in m004["snappy_shapes"]]
    re_seeds = [mpf(str(s["real"])) for s in m004["algebraic_seeds"]]
    for k, (xr, z) in enumerate(zip(re_seeds, zs)):
        d_as_recorded = abs(mpc(xr, mpf("0.1")) - z)
        d_best_lift = abs(xr - z.real)          # imaginary part matched exactly
        print(f"  seed[{k}] Re={nstr(xr, 12)}:  |recorded - z| = "
              f"{nstr(d_as_recorded, 6)}   |Re diff| (lift-free floor) = "
              f"{nstr(d_best_lift, 6)}")
    floor = min(abs(xr - z.real) for xr, z in zip(re_seeds, zs))
    print(f"  lift-free floor on m004: {nstr(floor, 10)} > 0, for EVERY "
          f"imaginary lift")

    # --- arity -------------------------------------------------------------
    print("\n=== arity: root index vs CUSP index ===")
    for row in rows:
        verdict = "equal" if row["n_roots"] == row["n_cusps"] else "NOT a bijection"
        print(f"  {row['name']:6s} {row['n_roots']} roots vs "
              f"{row['n_cusps']} cusps -> {verdict}")

    print("\n=== verdict ===")
    const = [r["name"] for r in rows if r["isometry_classes"] == 1]
    print(f"tau_arch (seed -> shape) is CONSTANT on: {', '.join(const)}")
    print("so no function of the seed value can carry the pole index k.")
    print("scope-(b); invariant = pigeonhole on a finite set.")
    print("The conjecture is NOT excluded: its own RHS is HOLONOMY, which is")
    print("path-dependent and so index-dependent even at equal shapes. The")
    print("object to measure is |Hol_mu_k - 1| at the seeds, not |seed - z_k|.")

    # NO ARTIFACT IS WRITTEN, deliberately. This probe derives no physical
    # quantity -- every output is a count or an exact identity -- so there is
    # nothing for a witness to pin and nothing a consumer would re-read. A
    # first draft wrote a `.probe.json`; that invented an artifact class the
    # corpus does not have (it was the only such file in the tree), which is
    # the kind of unilateral convention AGENTS.md's ASK-THE-OWNER rule is
    # about. If a durable record is wanted the house mechanism is
    # `WitnessBuilder`, as `snappy_cusp_seeding.py` uses -- a one-line add,
    # and the owner's call, not this probe's.
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
