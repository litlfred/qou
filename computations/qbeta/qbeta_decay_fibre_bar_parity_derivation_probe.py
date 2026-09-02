#!/usr/bin/env python3
"""qbeta_decay_fibre_bar_parity_derivation_probe.py — the decay fibre, derived
from bar-parity alone, WITHOUT the two-row cap.

BEAN `qou-cds1`. The registry names the open item: "neither convention was
DERIVED for this channel". The two-row cap (`y_(1^3) = 0`, giving the admissible
set `{q, z_D}` via `QOU.QBeta.AdmissibleRoots`) is the MASS channel's forcing,
imported into the decay channel by the 2026-08-15 owner ruling -- a decision,
not a derivation. So an exclusion resting only on the cap rests on a ruling.

THIS PROBE SUPPLIES AN INDEPENDENT ONE.

Step 9 (Lean, sorry-free, `QOU.QBeta.DecayBlockCarrier`) reduced the decay trace
to a single scalar times a fixed character:

    tr(Delta_S)(z) = g(z) * chi^(3)(Delta_S),   g(z) = (2qz - q^2 + 1)/(q^2 + 1)

Both factors have exactly computable behaviour under the fibre bar involution
`q -> 1/q`, and the result is a clean iff:

  1. chi^(3)(Delta_S) is bar-ODD                      bar(chi)/chi = -1 exactly
  2. g is bar-EVEN  <=>  bar(z) = z - h               the FULL-BAR condition
  3. g is bar-ODD   <=>  never                        NO SOLUTION
  4. therefore tr(Delta_S) has DEFINITE bar-parity <=> z is full-bar,
     and where it does, the parity is ODD.

Point 4 is unconditional -- a fact about the decay element, involving no claim
about what the physics requires. Its APPLICATION does need one mild premise,
stated separately below rather than smuggled in.

WHAT IT EXCLUDES, AND WHY THAT IS NOT THE CAP.

    z = q       full-bar YES  ->  tr is bar-ODD
    z_D         full-bar YES  ->  tr is bar-ODD
    z = 1       full-bar NO   ->  tr has NO definite bar-parity
    z_C         full-bar NO   ->  tr has NO definite bar-parity

So `z = 1` -- the coordinate-sum point the data wants (`z_required = 0.99850`,
0.15 % away) -- is excluded a SECOND time, by bar-parity, with no appeal to the
two-row cap and hence no appeal to the ruling.

It also explains the corpus's own mutual-exclusivity theorem
(`decayLadder_zC_threeRow_ne_zero`): `z_C` is bar-EVEN, which is a DIFFERENT
condition from full-bar, so the C-frame ladder cannot carry a bar-odd decay
trace at all. The two conditions have been adjacent in the corpus for weeks;
what is new here is that they are not the same one, and which one the decay
channel needs.

THE PREMISE, STATED NOT SMUGGLED. Turning point 4 into an exclusion needs:
"the decay trace must have definite bar-parity". That is weaker than the cap and
is the corpus's own standing structure -- `fig8Trace_im_odd` (the carrier S is
bar-odd, Lean-proved), `ZBarParity` (KC13), and Step 1's
`eigenphase_barOdd_of_barEven` / `eigenphase_bar_defect_of_fullBar`. It is NOT
proved here, and this probe does not claim it is.

SCOPE. Scope-(a) plus a derived structural iff. Nothing is wired. No c_k is
proposed. `z = 1` is not readmitted and z_D is not re-derived as unique: the
full-bar family is `z_D + (any bar-even function)`, and `z = q` is in it too, so
bar-parity NARROWS to full-bar, it does not pin a single z.

Anchor: experimental (proton) pin, per the 2026-08-07 owner directive.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp
from mpmath import mp

_COMP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(_COMP / "qbeta"), str(_COMP), str(_COMP / "substrate")]
import _path_bridge  # noqa: F401,E402

from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 60


def main() -> int:
    ok = True
    checks = []

    def check(name, passed, detail=""):
        nonlocal ok
        ok = ok and bool(passed)
        checks.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))

    q, z, w = sp.symbols("q z w", positive=True)
    h = q - 1 / q
    g = (2 * q * z - q ** 2 + 1) / (q ** 2 + 1)
    chi3S = sp.simplify(h ** 2 / 2 - h * q)
    bar = lambda e: sp.simplify(e.subs(q, 1 / q))

    # ---- 1. the fixed character is bar-odd ----
    ratio = sp.simplify(bar(chi3S) / chi3S)
    check("chi^(3)(Delta_S) is bar-ODD (bar/chi = -1 exactly)", ratio == -1,
          f"ratio = {ratio}")

    # ---- 2/3. when is the scalar bar-covariant? ----
    even_sol = sp.solve(sp.Eq(sp.simplify(g.subs({q: 1 / q, z: w})), g), w)
    odd_sol = sp.solve(sp.Eq(sp.simplify(g.subs({q: 1 / q, z: w})), -g), w)
    check("g is bar-EVEN exactly on the FULL-BAR condition bar(z) = z - h",
          bool(even_sol) and sp.simplify(even_sol[0] - (z - h)) == 0,
          f"bar(z) = {sp.simplify(even_sol[0]) if even_sol else 'none'}")
    check("g can NEVER be bar-ODD (no solution)", not odd_sol)

    print(f"\n[1] the two factors")
    print(f"    g(z)              = {sp.factor(g)}")
    print(f"    chi^(3)(Delta_S)  = {sp.factor(chi3S)}   [bar-ODD]")
    print(f"    full-bar condition: bar(z) = z - h,   h = q - 1/q")

    # ---- 4. the decay trace's parity, per z ----
    CAND = (("z = q (admissible, augmentation)", q),
            ("z_D = q^3/(q^2+1) (admissible)", q ** 3 / (q ** 2 + 1)),
            ("z = 1 (coordinate sum)", sp.Integer(1)),
            ("z_C = sqrt(q)/(q+1) (excised)", sp.sqrt(q) / (q + 1)))
    rows = {}
    print(f"\n[2] bar-parity of tr(Delta_S) = g(z)*chi^(3), by Markov parameter")
    print(f"    {'z':<38} {'full-bar':<9} {'bar-even':<9} {'tr parity'}")
    for nm, zz in CAND:
        fullbar = sp.simplify(bar(zz) - (zz - h)) == 0
        bareven = sp.simplify(bar(zz) - zz) == 0
        tr = sp.simplify(g.subs(z, zz) * chi3S)
        r = sp.simplify(bar(tr) / tr) if sp.simplify(tr) != 0 else None
        par = ("bar-ODD" if r == -1 else "bar-EVEN" if r == 1 else "NO definite parity")
        rows[nm] = {"full_bar": bool(fullbar), "bar_even": bool(bareven),
                    "trace_parity": par, "bar_ratio": str(sp.factor(r)) if r is not None else None}
        print(f"    {nm:<38} {str(fullbar):<9} {str(bareven):<9} {par}")
        # the iff, checked per candidate rather than asserted once
        check(f"definite parity <=> full-bar, at {nm}",
              (par == "bar-ODD") == bool(fullbar))

    # ---- the full-bar family is not a single z ----
    #    if f is bar-even then z + f is full-bar whenever z is: bar(z+f) = (z+f) - h
    f_even = sp.Symbol("f_even")           # stand-in for an arbitrary bar-even function
    check("the FULL-BAR family is affine over bar-even functions (so it does "
          "NOT pin a unique z)",
          sp.simplify((bar(q ** 3 / (q ** 2 + 1)) + f_even)
                      - ((q ** 3 / (q ** 2 + 1) + f_even) - h)) == 0)

    q0 = q_at(55)
    verdict = (
        "DERIVED (structural iff, no two-row cap): tr(Delta_S)(z) has DEFINITE "
        "bar-parity if and only if z satisfies the FULL-BAR condition "
        "bar(z) = z - h, and where it does the parity is ODD. chi^(3)(Delta_S) is "
        "bar-odd exactly; g is bar-even exactly on full-bar and can never be "
        "bar-odd. CONSEQUENCE: z = 1 and z_C are excluded a SECOND time, by "
        "bar-parity, with no appeal to the cap and hence none to the owner ruling. "
        "This CORRECTS this session's own Step 10 framing ('the block is a ruling, "
        "not an impossibility') -- that is right about the CAP and wrong as a "
        "statement about the exclusion as a whole. It also explains "
        "decayLadder_zC_threeRow_ne_zero: z_C is bar-EVEN, a DIFFERENT condition "
        "from full-bar. PREMISE for the application, stated not smuggled: 'the "
        "decay trace must have definite bar-parity', which is corpus-standard "
        "(fig8Trace_im_odd, ZBarParity) but is NOT proved here. LIMIT: the full-bar "
        "family is z_D + (any bar-even function) and contains z = q too, so this "
        "narrows the fibre to full-bar -- it does not pin a unique z.")
    print(f"\n[3] {verdict}")

    wb = WitnessBuilder("qbeta-decay-fibre-bar-parity-derivation", engine="sympy+mpmath")
    wb.set_description(
        "Derives a decay-fibre constraint from bar-parity alone, independently of "
        "the two-row cap: tr(Delta_S) has definite bar-parity iff z satisfies the "
        "full-bar condition bar(z) = z - h, and then it is ODD. Excludes z = 1 and "
        "z_C without appeal to the owner ruling. Narrows the fibre; does not pin a "
        "unique z. Nothing wired, no c_k proposed.")
    wb.add_data("g_symbolic", str(sp.factor(g)))
    wb.add_data("chi3_deltaS_symbolic", str(sp.factor(chi3S)))
    wb.add_data("chi3_bar_ratio", str(ratio))
    wb.add_data("g_bar_even_condition", str(sp.simplify(even_sol[0])) if even_sol else None)
    wb.add_data("g_bar_odd_condition", "NO SOLUTION" if not odd_sol else str(odd_sol[0]))
    wb.add_data("parity_by_markov_parameter", rows)
    wb.add_data("premise_not_proved_here",
                "the decay trace must have definite bar-parity (fig8Trace_im_odd, "
                "ZBarParity, eigenphase_barOdd_of_barEven) -- corpus-standard, cited "
                "not proved")
    wb.add_data("limit",
                "the full-bar family is z_D + (any bar-even function) and contains "
                "z = q; bar-parity narrows the fibre, it does not pin a unique z")
    wb.add_data("corrects",
                "this session's Step 10 framing 'the block is a ruling, not an "
                "impossibility' — right about the CAP, wrong about the exclusion as "
                "a whole, since bar-parity excludes z=1 independently")
    wb.add_data("free_parameters", 0)
    wb.add_data("verdict", verdict)
    wb.add_data("scope", "(a) + a derived structural iff; z=1 NOT readmitted")
    wb.add_data("q0Anchor", "proton")
    wb.add_data("q0Value", mp.nstr(q0, 50))
    for c in checks:
        wb.add_assertion(c["name"],
                         computed=mp.mpf(1) if c["passed"] else mp.mpf(0),
                         expected=mp.mpf(1), tolerance=mp.mpf("0.5"), unit="bool")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
