#!/usr/bin/env python3
"""qbeta_d_frame_required_markov_parameter_probe.py — the decay trace is ONE
affine scalar in z, so the Markov parameter the CODATA Q-value wants is
computable exactly. This computes it.

BEAN `qou-cds1`. Four routes to the convention-D correction are now closed:
the parameter-free multiplicative correction on either admissible base
(2026-08-29), the additive/cos resummation (Step 8 — under D the bar-invariant
moves with q, so there is no fixed centre), the z=1 return (the admissibility
leak is 7.6x too small to be the correction), and block re-weighting (Step 9 —
chi^(2,1)(Delta_S) = 0, so only ONE block carries the decay).

THE REDUCTION THIS PROBE USES. Step 9 proved

    tr(Delta_S)(z) = (y_3(z) - y_(1^3)(z)) * chi^(3)(Delta_S)   for all z

and chi^(3)(Delta_S) is a FIXED rational function of q -- a property of the
decay element, not of the Markov parameter. So all of the z-dependence lives in
one scalar, and that scalar is affine:

    g(z) := y_3(z) - y_(1^3)(z) = (2qz - q^2 + 1)/(q^2 + 1)
    g(z) * chi^(3)(Delta_S) = h^2/2 - h*z          (exact, verified below)
    g(z_D) = (q^4+1)/(q^2+1)^2                     (= y_3(z_D), since y_111 = 0)

Affine and invertible, so ASKING WHAT z THE DATA WANTS IS AN EXACT QUESTION,
not a fit: there is exactly one z reproducing any given Q, and no freedom.

WHY THIS COORDINATE AND NOT F OR alpha. The phase alpha was shown to be a bad
coordinate (a square-root branch point 0.062 % above q0, manufactured by writing
a smooth correction as a cosine). F = Q/Q_A is smooth but is a ratio of two
things that both move. z is the object the Lean admissibility theorem is stated
about (`admissible_markov_param_iff`: roots exactly {q, z_D}), so a required
value of z can be compared DIRECTLY against a proved constraint rather than
against a basket of candidate forms.

SCOPE. Scope-(a) measurement. It derives nothing, proposes nothing, and
readmits nothing -- in particular a z landing near an inadmissible point is a
statement of TENSION, not permission to use that point. `one_not_root` stands.

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

# From qbeta-d-frame-admissible-base-correction-search.witness.json (2026-08-29).
F_REQUIRED_TRM = mp.mpf("1.75923699054610623")
F_REQUIRED_AUG = mp.mpf("0.88912581036021176")


def main() -> int:
    ok = True
    checks = []

    def check(name, passed, detail=""):
        nonlocal ok
        ok = ok and bool(passed)
        checks.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))

    q, z, G = sp.symbols("q z G", positive=True)
    h = q - 1 / q
    D = (q ** 2 + 1) * (q ** 2 - q + 1) * (q ** 2 + q + 1)
    y3 = (q * z + 1) * (q ** 3 * z + q * z + 1) / D
    y111 = q ** 2 * (z - q) * ((q ** 2 + 1) * z - q ** 3) / D
    g = sp.cancel(sp.simplify(y3 - y111))
    chi3S = sp.simplify(h ** 2 / 2 - h * q)
    zD = q ** 3 / (q ** 2 + 1)

    check("g(z) = (2qz - q^2 + 1)/(q^2+1)",
          sp.simplify(g - (2 * q * z - q ** 2 + 1) / (q ** 2 + 1)) == 0)
    check("g(z) * chi^(3)(Delta_S) = h^2/2 - h z, exactly, for all z",
          sp.simplify(g * chi3S - (h ** 2 / 2 - h * z)) == 0)
    check("g is AFFINE in z (so the inversion is unique, not a fit)",
          sp.degree(sp.numer(sp.cancel(g)), z) == 1)
    gD = sp.cancel(sp.simplify(g.subs(z, zD)))
    check("g(z_D) = (q^4+1)/(q^2+1)^2",
          sp.simplify(gD - (q ** 4 + 1) / (q ** 2 + 1) ** 2) == 0)

    z_of_g = sp.solve(sp.Eq(g, G), z)[0]
    print(f"\n[1] the reduction")
    print(f"    g(z)     = {sp.factor(g)}")
    print(f"    z(G)     = {sp.factor(sp.simplify(z_of_g))}")

    # ---- the required z, at the pin ----
    q0 = q_at(55)
    f_g = sp.lambdify(q, gD, "mpmath")
    f_z = sp.lambdify((q, G), z_of_g, "mpmath")
    gD_n = f_g(q0)
    zD_n = q0 ** 3 / (q0 ** 2 + 1)
    zC_n = mp.sqrt(q0) / (q0 + 1)

    rows = {}
    for nm, F in (("tr_M base", F_REQUIRED_TRM), ("augmentation base", F_REQUIRED_AUG)):
        # the augmentation base is g at z=q; the tr_M base is g at z_D
        gbase = f_g(q0) if nm == "tr_M base" else sp.lambdify(q, g.subs(z, q), "mpmath")(q0)
        zr = f_z(q0, gbase * F)
        rows[nm] = {"g_base": mp.nstr(gbase, 16), "F": mp.nstr(F, 16),
                    "g_required": mp.nstr(gbase * F, 16), "z_required": mp.nstr(zr, 16)}

    print(f"\n[2] the Markov parameter the CODATA Q-value requires")
    print(f"    {'via':<20} {'g_required':>20} {'z_required':>20}")
    for nm, r in rows.items():
        print(f"    {nm:<20} {r['g_required']:>20} {r['z_required']:>20}")
    print(f"\n    reference points at this pin:")
    for nm, v in (("z = 1 (coordinate sum, EXCLUDED)", mp.mpf(1)),
                  ("z_D = q^3/(q^2+1)  (admissible)", zD_n),
                  ("z = q             (admissible)", q0),
                  ("z_C (excised convention)", zC_n)):
        print(f"      {nm:<36} {mp.nstr(v, 16)}")

    # ---- distances: the whole point ----
    dist = {}
    print(f"\n[3] where z_required sits")
    for nm, r in rows.items():
        zr = mp.mpf(r["z_required"])
        d = {"to_z_eq_1": mp.nstr(abs(zr - 1), 8),
             "to_z_D": mp.nstr(abs(zr - zD_n), 8),
             "to_z_eq_q": mp.nstr(abs(zr - q0), 8),
             "to_z_C": mp.nstr(abs(zr - zC_n), 8)}
        d["rel_to_z_eq_1_pct"] = mp.nstr(abs(zr - 1) * 100, 6)
        d["closer_to_1_than_zD_by"] = mp.nstr(abs(zr - zD_n) / abs(zr - 1), 6) \
            if abs(zr - 1) else "inf"
        dist[nm] = d
        print(f"    {nm}:  z_req = {mp.nstr(zr,14)}")
        print(f"        |z_req - 1|   = {d['to_z_eq_1']}   ({d['rel_to_z_eq_1_pct']} %)")
        print(f"        |z_req - z_D| = {d['to_z_D']}")
        print(f"        |z_req - q|   = {d['to_z_eq_q']}")
        print(f"        nearer to z=1 than z_D is, by a factor "
              f"{d['closer_to_1_than_zD_by']}")

    zr_trm = mp.mpf(rows["tr_M base"]["z_required"])
    near_one = abs(zr_trm - 1) < mp.mpf("0.01")
    check("z_required is NOT an admissible root (one_not_root territory)",
          abs(zr_trm - zD_n) > mp.mpf("1e-6") and abs(zr_trm - q0) > mp.mpf("1e-6"))

    verdict = (
        "SCOPE-(a) TENSION, stated in the coordinate the Lean constraint is about. "
        f"The decay trace is one affine scalar g(z), so the required Markov "
        f"parameter is EXACT and unique: z_required = {mp.nstr(zr_trm, 12)}. That is "
        f"{mp.nstr(abs(zr_trm-1)*100, 4)} % from z = 1 -- the coordinate-sum point that "
        "QOU.QBeta.AdmissibleRoots.one_not_root PROVES inadmissible -- and "
        f"{mp.nstr(abs(zr_trm-zD_n)/abs(zr_trm-1), 4)}x nearer to it than the admissible "
        "z_D is. The data wants a z the theory forbids, and the gap is now a single "
        "number rather than a chain of corrections. This does NOT readmit z=1: the "
        "leak there is 7.6x too small to be the correction (measured separately), so "
        "'nearly z=1' is a description of the tension, not a mechanism."
        if near_one else
        f"SCOPE-(a): z_required = {mp.nstr(zr_trm, 12)}, not near any distinguished point.")
    print(f"\n[4] {verdict}")

    wb = WitnessBuilder("qbeta-d-frame-required-markov-parameter", engine="sympy+mpmath")
    wb.set_description(
        "Step 9 proved tr(Delta_S)(z) = (y_3 - y_(1^3))(z) * chi^(3)(Delta_S) with "
        "chi^(3) fixed, so the whole z-dependence is one AFFINE scalar g(z) = "
        "(2qz - q^2 + 1)/(q^2+1). That makes 'what Markov parameter does the CODATA "
        "Q-value require' an exact, unique question rather than a fit. This computes "
        "it and locates it against the admissible set {q, z_D} and the proved-"
        "inadmissible z=1. Derives nothing; readmits nothing.")
    wb.add_data("g_symbolic", str(sp.factor(g)))
    wb.add_data("z_of_g_symbolic", str(sp.factor(sp.simplify(z_of_g))))
    wb.add_data("chi3_deltaS_symbolic", str(sp.factor(chi3S)))
    wb.add_data("required", rows)
    wb.add_data("distances", dist)
    wb.add_data("reference_points",
                {"z_eq_1": "1", "z_D": mp.nstr(zD_n, 20), "z_eq_q": mp.nstr(q0, 20),
                 "z_C_excised": mp.nstr(zC_n, 20)})
    wb.add_data("free_parameters", 0)
    wb.add_data("verdict", verdict)
    wb.add_data("scope", "(a) measured tension; one_not_root stands exactly as proved")
    wb.add_data("what_is_unconditional_vs_ruling_conditional", {
        "UNCONDITIONAL (any z, any convention)": [
            "chi^(2,1)(Delta_S) = 0 exactly (Lean: DecayBlockCarrier.chi21_deltaS)",
            "tr(Delta_S)(z) = g(z) * chi^(3)(Delta_S) with g affine",
            "the decay channel's entire z-content is ONE affine scalar",
            "z_required = 0.998500302563, exact and unique given base ~ tr_M(Delta_S)",
        ],
        "CONDITIONAL ON THE RULING (that the decay channel is convention D)": [
            "'under D the carrier is a single block'",
            "'block re-weighting cannot source the correction' (Step 9)",
            "the inadmissibility of z_required",
            "the four closed correction routes",
        ],
        "why": (
            "AdmissibleRoots proves admissible <=> y_(1^3) = 0 <=> z in {q, z_D}. That is a "
            "theorem ABOUT the condition. That the DECAY channel must satisfy it is settled "
            "by the 2026-08-15 owner ruling (convention D), and the trace-convention registry "
            "explicitly preserves the prior analysis: 'superseded AS A STATUS, NOT AS "
            "ANALYSIS: its finding that neither convention was DERIVED for this channel "
            "stands'. MarkovZFullBarCondition's own docstring says the same -- 'Which horn is "
            "the decay channel's is NOT decided here: no corpus block derives the decay "
            "fibre'. So the block is a RULING, not a proved impossibility."),
        "consequence_for_the_open_problem": (
            "The D re-derivation is not blocked by an impossibility. The decay trace is one "
            "affine scalar; the data fixes it exactly at z = 0.99850; the ruling fixes it at "
            "z_D = 0.61269. Closing the gap means DERIVING THE DECAY FIBRE -- which the "
            "registry names as the open item -- not finding another correction. The thing "
            "missing is not a form."),
    })
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
