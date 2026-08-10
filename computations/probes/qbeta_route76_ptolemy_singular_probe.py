#!/usr/bin/env python3
"""Route 76 -- the Ptolemy variety solved LOCALLY with Singular: no Magma, no network.

Beans `qou-ptlm`, `qou-m015`.

WHY THIS EXISTS
---------------
Route 75 derives shape fields by LLL identification (`algdep`) plus exact verification,
and its measured ceiling is the IDENTIFICATION step: 11a1 (17 tetrahedra), 11a2, 12a1 all
failed to identify within budget. Garoufalidis-Goerner-Zickert (1207.6711 sec 1.3) point
at the alternative:

    "while Groebner basis computations are feasible for the Ptolemy varieties even for
     many simplices, they are usually impractical for the gluing equations even when the
     cusp equations are added. However, the monomial map mu can be used to obtain shapes
     from Ptolemy coordinates."

SnapPy ships the Ptolemy machinery, but both of its solving paths are unavailable here:

  * `retrieve_solutions()` fetches from ptolemy.unhyperbolic.org -- the agent proxy
    answers 403 (recorded in the proxy's own `recentRelayFailures`);
  * `compute_solutions()` requires **Magma**, which is proprietary, commercially licensed
    software from the University of Sydney. It is not open source, is not on GitHub, and
    cannot be installed here.

NEITHER IS NECESSARY. The Ptolemy equations are available offline from SnapPy, and the
primary decomposition they need is exactly what **Singular**'s `minAssGTZ` computes --
Singular being the engine Sage itself calls for this. `apt-get install singular` and the
route runs locally.

WHAT THIS BUYS, AND WHAT IT DOES NOT
------------------------------------
The derivation is **fully symbolic end to end**: no LLL, no height cap, no
precision-stability gate, hence none of Route 75 gate G2's lattice-artifact risk. It
starts from SnapPy's exact combinatorial data and returns exact ideals.

It does NOT establish that a triangulation is a triangulation *of* a knot complement --
that is Thurston hyperbolisation plus Mostow rigidity, unchanged from Routes 74/75.

THE OBSTRUCTION CLASS MATTERS, AND GETTING IT WRONG LOOKS LIKE A BUG
--------------------------------------------------------------------
For both 4_1 and 5_2 the obstruction class **0** variety is EMPTY -- Singular returns the
unit ideal, `dim = -1`. The geometric representation lives on class **1**. A probe that
silently used `obstruction_class=0` would conclude these manifolds have no boundary-
unipotent representations at all. Gate G2 pins this so it cannot be mistaken for a
failure of the method.
"""

import json
import pathlib
import re
import shutil
import subprocess
import tempfile
import warnings

warnings.filterwarnings("ignore")


def singular(code, timeout=900):
    with tempfile.NamedTemporaryFile("w", suffix=".sing", delete=False) as f:
        f.write(code + "\nquit;\n")
        path = f.name
    try:
        r = subprocess.run(["Singular", "-q", "--no-warn", path],
                           capture_output=True, text=True, timeout=timeout)
        return r.stdout
    finally:
        pathlib.Path(path).unlink(missing_ok=True)


def decompose(M, N=2, obstruction="all", timeout=900):
    """Primary decomposition of every obstruction class's Ptolemy variety."""
    vs = M.ptolemy_variety(N, obstruction_class=obstruction)
    if not isinstance(vs, (list, tuple)):
        vs = [vs]
    out = []
    for idx, P in enumerate(vs):
        vars_ = list(P.variables_with_non_zero_condition)
        eqs = [re.sub(r"\s+", " ", str(e)).strip()
               for e in P.equations_with_non_zero_condition]
        code = "\n".join([
            'LIB "primdec.lib";',
            f"ring R = 0,({','.join(vars_)}),dp;",
            "ideal I = " + ",\n  ".join(eqs) + ";",
            "list L = minAssGTZ(I);",
            'printf("NCOMP %s", size(L));',
            "for (int i=1; i<=size(L); i++) {",
            '  printf("COMP %s DIM %s", i, dim(std(L[i])));',
            '  printf("GENS %s", L[i]);',
            "}",
        ])
        so = singular(code, timeout=timeout)
        comps = re.findall(
            r"COMP (\d+) DIM (-?\d+)\n?GENS ([\s\S]*?)(?=COMP \d+ DIM|\Z)", so)
        out.append({
            "obstruction_index": idx,
            "num_variables": len(vars_),
            "num_equations": len(eqs),
            "components": [
                {"index": int(i), "dimension": int(d), "generators": " ".join(g.split())}
                for i, d, g in comps],
        })
    return out


def main() -> int:
    import snappy

    if not shutil.which("Singular"):
        print("Singular not installed -- `apt-get install singular`"); return 1

    gates = []

    # ---- G1: calibration against the two fields the corpus already PROVED in Lean ----
    # 4_1 -> x^2 - x + 1  (QOU/Knot/FigureEightTriangulation.lean, `w_sq_sub`)
    # 5_2 -> z^3 - z^2 + 1 (QOU/Archimedean/BlochWignerLobachevsky.lean,
    #                       `fiveTwoShapeCubic` -- the LANDEN IMAGE of the saddle cubic
    #                       y^3-2y^2+3y-1, related by `landen_root`)
    # Decompose ONCE per knot and reuse across gates.  Computing it per gate made this
    # probe take ~10 minutes for no reason: minAssGTZ is the expensive step, and G1 and
    # G2 read different facts off the same decomposition.
    cache = {name: decompose(snappy.Manifold(name)) for name in ("4_1", "5_2")}

    calib, calib_ok = [], True
    for name, expect in [("4_1", "c_0101_0^2-c_0101_0+1"),
                         ("5_2", "c_0101_0^3-c_0101_0^2+1")]:
        res = cache[name]
        gens = " ".join(c["generators"] for r in res for c in r["components"])
        found = expect in gens.replace(" ", "")
        calib_ok = calib_ok and found
        calib.append({"knot": name, "expected_generator": expect, "found": found,
                      "decomposition": res})
    gates.append({
        "gate": "G1",
        "claim": "CALIBRATION, no Magma and no network. Singular's minAssGTZ on the "
                 "Ptolemy variety reproduces the two shape fields the corpus has ALREADY "
                 "PROVED in Lean: 4_1's x^2-x+1 (FigureEightTriangulation.w_sq_sub) and "
                 "5_2's z^3-z^2+1 (BlochWignerLobachevsky.fiveTwoShapeCubic, the Landen "
                 "image of the saddle cubic, related by `landen_root`)",
        "calibration": calib,
        "pass": bool(calib_ok),
    })

    # ---- G2: the obstruction class is not optional --------------------------------
    obstruction = []
    for name in ["4_1", "5_2"]:
        res = cache[name]
        rows = [{"obstruction_index": r["obstruction_index"],
                 "dimensions": [c["dimension"] for c in r["components"]]} for r in res]
        obstruction.append({"knot": name, "classes": rows})
    empty_zero = all(r["classes"][0]["dimensions"] == [-1] for r in obstruction)
    gates.append({
        "gate": "G2",
        "claim": "THE OBSTRUCTION CLASS IS NOT OPTIONAL, and getting it wrong looks like a "
                 "failure of the method rather than a mis-set flag. For BOTH 4_1 and 5_2 "
                 "the class-0 Ptolemy variety is EMPTY -- Singular returns the unit ideal, "
                 "dim = -1 -- and the geometric representation lives on class 1. A probe "
                 "defaulting to obstruction_class=0 would report that these manifolds have "
                 "no boundary-unipotent representations at all",
        "class_zero_is_empty_for_both": bool(empty_zero),
        "detail": obstruction,
        "pass": bool(empty_zero),
    })

    # ---- G3: what made this runnable ----------------------------------------------
    gates.append({
        "gate": "G3",
        "claim": "HOW THIS RUNS WITHOUT MAGMA OR NETWORK. SnapPy's two solving paths are "
                 "both unavailable here -- retrieve_solutions() gets a 403 from the agent "
                 "proxy against ptolemy.unhyperbolic.org, and compute_solutions() needs "
                 "Magma, which is proprietary licensed software, not open source, not on "
                 "GitHub, and not installable. Neither is necessary: the equations come "
                 "out of SnapPy offline and the primary decomposition is exactly Singular's "
                 "minAssGTZ, the same engine Sage calls",
        "magma_required": False,
        "network_required": False,
        "engine": "Singular " + (subprocess.run(["Singular", "--version"],
                                                capture_output=True, text=True)
                                 .stdout.split("version")[-1].split()[0]
                                 if shutil.which("Singular") else "?"),
        "fully_symbolic": True,
        "no_lll_no_height_gate": "unlike Route 75, so Route 75 gate G2's lattice-artifact "
                                 "risk does not arise here at all",
        "pass": True,
    })

    # ---- G4: scope -----------------------------------------------------------------
    gates.append({
        "gate": "G4",
        "claim": "SCOPE, UNCHANGED FROM ROUTES 74 AND 75. Solving the Ptolemy variety does "
                 "NOT establish that a triangulation is a triangulation OF a knot "
                 "complement -- that is Thurston hyperbolisation plus Mostow rigidity, "
                 "needing hyperbolic 3-manifolds that neither Mathlib nor QOU has. No "
                 "volume conjecture is touched. And none of this mathematics is new: the "
                 "Ptolemy variety and its decomposition are Garoufalidis-Goerner-Zickert",
        "is_triangulation_of_the_manifold": "not statable in Lean today",
        "vol_conjecture_formalized": False,
        "mathematics_is_new": False,
        "pass": True,
    })

    out = {
        "probe": "qbeta_route76_ptolemy_singular",
        "beans": ["qou-ptlm", "qou-m015"],
        "snappy_version": snappy.version(),
        "gates": gates,
        "verdict": {
            "method": "Ptolemy variety primary decomposition via Singular minAssGTZ",
            "magma_required": False,
            "network_required": False,
            "reproduces": "4_1 x^2-x+1 and 5_2 z^3-z^2+1, both already proved in Lean",
            "not_established": "that any triangulation is a triangulation of a manifold",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-route76-ptolemy-singular.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:70]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "the Ptolemy route runs LOCALLY with Singular -- no Magma, no network -- and "
        "reproduces both shape fields the corpus has already proved in Lean."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
