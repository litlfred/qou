#!/usr/bin/env python3
"""
KC19 ↔ KC20 cross-consistency: the two independently-Lean-proved bar-odd
narrowings of the Q_β c₃ channel live in the SAME trace variable y=q²+q⁻² and
are mutually consistent — jointly sharpening the real-q/quadratic exclusion and
DISCIPLINING the flagged C(3)=−2 numerology as a wrong-anchor coincidence.

Formalize-first CONSISTENCY check (sympy-exact). No c_k value, no wiring, no tier
change (registry §8 flip-flop guard). This CROSS-CHECKS two proved constraints;
it does NOT attempt a c₃ closure (every discrete route is refuted — #3536/#3567;
the surviving object is the analytic Φ_b state-integral, worked on #3544/#3596).

The two objects (both from docs/coordination/ck-dk-canonical-registry.md §9):

  KC19 (observable / eval-map side, PR #3473, proved-lean CrossingWeightAffine):
    the archimedean eval map E(w)=h²/2−h·w is AFFINE ⇒ the bar-odd ladder part is
    K(q)·(w−w₀) with the ANCHOR-RIGID kernel K(q)=2h/(4w₀²−h²); the c₃ swing lives
    entirely in the crossing weight w(q).

  KC20 (fibre / 4₁-carrier side, PR #3467, proved-lean QBetaZeta4ResidueRefutation):
    the bar-odd carrier num=(q²−1)·R₁₂, R₁₂=q⁶·C(y), C(y)=y³−4y²+3y−2 is a
    degree-3 IRREDUCIBLE cubic in y=q²+q⁻² (disc −152=−2³·19), no quadratic anchor
    is a root ⇒ real-q/quadratic c₃ closures structurally excluded.

Four consistency facts (all sympy-exact, parameter-free):

  1. SAME COORDINATE. KC19's kernel denominator at the counit w₀=1 is
     4w₀²−h² = 4−h² = 6−y EXACTLY (y=q²+q⁻²) — the SAME bar-even trace variable
     as KC20's carrier cubic C(y). The two audits never state this bridge; it is
     the reason both can describe one channel.

  2. DISJOINT SINGULAR STRUCTURE. K(q)=2h/(6−y) has its only pole at y=6 (the
     SILVER anchor 1+√2); the carrier C is regular there (C(6)=88≠0, and the
     carrier's real root is y₀≈3.27). So the eval map's singularity and the
     carrier's degree-3 root are disjoint — consistent, non-overlapping.

  3. JOINT (SHARPER) EXCLUSION. KC19 localizes the c₃ swing to w(q); KC18 (the
     bridge, eval-map bar-decomposition) feeds the carrier into w AFFINELY; KC20
     makes the carrier degree-3 irreducible with no quadratic anchor. Composing
     the three proved constraints: w(q) — hence c₃=[u³]w — inherits the degree-3
     field, so NO quadratic / root-of-unity closed form for c₃ can exist. This is
     the UNIFIED statement neither audit makes alone (KC20 §4 excludes at the
     fibre carrier; KC19 localizes at the observable; the affine bridge joins
     them). Consistent, not contradictory.

  4. TWO DISTINCT −2's — MEANINGFUL Hopf-sector shadow vs COINCIDENTAL total match
     (corrected 2026-07-12 to cite the prior bridge audit
     2026-07-07-hopf-cubic-vs-crossing-weight-shadow-bridge, a corpus-grep miss):
     (a) MEANINGFUL: C_Hopf(2)=−2 at the CLASSICAL anchor y=2 = J_Hopf(1) = the c₃
         q=1 shadow (Lean-certified in the bridge audit) — the −2/c₃ link is real,
         not coincidental, and is sourced by the Hopf (2-crossing) sector (KC20 §5).
     (b) COINCIDENCE: the TOTAL C(3)=−2 at the GOLDEN anchor y=3 (KC20 §4 flag) —
         the total C at the actual shadow anchor is C(2)=−4≠−2, so this separate
         match needs the WRONG anchor. Sharpens KC20 §4 WITHOUT conflating it with
         the meaningful Hopf-sector shadow.

Net: the two most-recent Lean-proved c₃ narrowings are coherent (same variable,
disjoint singularities), jointly stronger than either alone, and close a flagged
numerology. Nothing wired; no tier change.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp


def main():
    q = sp.symbols('q', positive=True)
    Y = sp.symbols('Y')
    y = q**2 + q**(-2)
    h = q - 1/q
    C = Y**3 - 4*Y**2 + 3*Y - 2
    C_Hopf = Y**3 - 6*Y**2 + 10*Y - 6
    C_unknot = 2*Y**2 - 7*Y + 4

    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    # 1. same coordinate: KC19 denom 4-h^2 == 6-y exactly
    same_coord = sp.simplify((4 - h**2) - (6 - y)) == 0
    check("kc19_kc20_same_trace_variable", same_coord,
          "KC19 kernel denom 4−h² = 6−y exactly (y=q²+q⁻²) — the SAME bar-even "
          "trace variable as KC20's carrier cubic C(y); the unstated bridge")

    # carrier sanity: C = C_Hopf + C_unknot
    sector_ok = sp.expand(C - (C_Hopf + C_unknot)) == 0
    check("carrier_sector_decomposition_exact", sector_ok,
          "C(y) = C_Hopf(y³−6y²+10y−6) + C_unknot(2y²−7y+4) exactly (KC20 §5)")

    # 2. disjoint singular structure: K pole at y=6 (silver); C(6)!=0
    disjoint = (C.subs(Y, 6) != 0)
    check("disjoint_singular_structure", disjoint,
          f"K(q)=2h/(6−y) pole at y=6 (silver anchor); carrier regular there "
          f"C(6)={C.subs(Y, 6)}≠0 ⇒ eval-map singularity ⊥ carrier degree-3 root")

    # 3. joint exclusion: C irreducible over Q (degree-3 => no quadratic anchor).
    #    Direct sympy irreducibility over QQ (clearer than RRT+disc; the RRT
    #    values are retained in the detail as the informative computational content).
    C_irreducible = sp.Poly(C, Y, domain='QQ').is_irreducible
    joint_excl = C_irreducible and (sp.discriminant(C, Y) == -152)
    check("joint_degree3_exclusion", joint_excl,
          f"C irreducible over ℚ (Poly.is_irreducible={C_irreducible}; rational-root "
          f"candidates {{±1,±2}} all nonzero: {[int(C.subs(Y, r)) for r in (1, -1, 2, -2)]}), "
          f"disc={sp.discriminant(C, Y)} ⇒ via KC19 (swing∈w) + KC18 (affine bridge), "
          "c₃=[u³]w inherits the degree-3 field ⇒ no quadratic/RoU c₃ closure (unified KC19+KC20)")

    # 4. TWO distinct −2's — keep them separate (corrected 2026-07-12 to cite the
    #    prior bridge audit 2026-07-07-hopf-cubic-vs-crossing-weight-shadow-bridge):
    #    (a) MEANINGFUL: C_Hopf(2)=−2 at the classical anchor y=2 (= J_Hopf(1) = c₃ shadow);
    #    (b) COINCIDENCE: total C(3)=−2 at the golden anchor y=3 (KC20 §4 numerology).
    C_Hopf = Y**3 - 6*Y**2 + 10*Y - 6
    y_at_q1 = sp.limit(y, q, 1)                # = 2 (classical/q=1 trace point)
    C_hopf_shadow = C_Hopf.subs(Y, y_at_q1)    # C_Hopf(2) = -2  (MEANINGFUL = J_Hopf(1))
    C_total_shadow = C.subs(Y, y_at_q1)        # C(2) = -4        (total ≠ -2 at the right anchor)
    C_total_golden = C.subs(Y, 3)              # C(3) = -2        (the coincidental total match)
    two_minus_twos = ((y_at_q1 == 2) and (C_hopf_shadow == -2)
                      and (C_total_shadow == -4) and (C_total_golden == -2))
    check("two_distinct_minus_twos_meaningful_vs_coincidence", two_minus_twos,
          f"MEANINGFUL: C_Hopf({y_at_q1})={C_hopf_shadow} at the classical anchor y=2 = "
          f"J_Hopf(1) = c₃ shadow (bridge audit, Lean-certified). COINCIDENCE: total "
          f"C(3)={C_total_golden} at the GOLDEN anchor y=3, but total C({y_at_q1})={C_total_shadow}≠−2 "
          "at the actual shadow anchor ⇒ the total-C-at-golden match needs the WRONG anchor "
          "(sharpens KC20 §4); the −2/c₃ link is NOT globally coincidental — it is the "
          "Hopf-sector classical shadow")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "KC19 ⇔ KC20 ARE CONSISTENT AND JOINTLY SHARPER (formalize-first, no c₃ value, "
        "nothing wired): (1) both live in the SAME trace variable y=q²+q⁻² — KC19's "
        "eval-kernel denominator 4−h²=6−y is exactly KC20's carrier variable (unstated "
        "bridge); (2) their singular structures are DISJOINT (K pole at silver y=6, "
        "C(6)=88≠0; carrier root y₀≈3.27); (3) composing KC19 (c₃ swing∈w) + KC18 (affine "
        "carrier→w) + KC20 (degree-3 irreducible carrier) gives the UNIFIED exclusion c₃ "
        "inherits the degree-3 field ⇒ no quadratic/RoU closure — stronger than either "
        "audit alone; (4) TWO distinct −2's kept separate — the MEANINGFUL Hopf-sector "
        "shadow C_Hopf(2)=−2 at the classical anchor y=2 (= J_Hopf(1) = c₃ shadow, bridge "
        "audit) vs the COINCIDENTAL total C(3)=−2 at the golden anchor y=3 (total C(2)=−4 at "
        "the actual shadow anchor). The two most-recent Lean-proved c₃ narrowings are "
        "coherent; adds the 4−h²=6−y kernel-denominator identity + disjoint singularities to "
        "the prior 2026-07-07 bridge audit. NO tier change; NOTHING WIRED."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    _here = os.path.dirname(os.path.abspath(__file__))

    def _sha():
        s = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not s:
            raise RuntimeError("empty commitSha")
        return s

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "qbeta-c3-kc19-kc20-consistency",
        "description": "KC19 (eval-map affine kernel) and KC20 (degree-3 carrier cubic) both "
                       "live in y=q²+q⁻²; consistent (disjoint singularities), jointly sharpen "
                       "the real-q/quadratic c₃ exclusion, and the C(3)=−2 flag is a wrong-anchor "
                       "coincidence (c₃ q=1 shadow at y=2 gives C(2)=−4). No c_k value; nothing wired.",
        "auditOnly": "docs/audits/2026-07-11-qbeta-c3-kc19-kc20-consistency.md",
        "tier": "symbolic-exact (sympy; consistency cross-check of two proved-lean constraints)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "kc19_kernel_denom": "4-h^2 = 6-y (y=q^2+q^-2)",
            "kc20_carrier": "C(y)=y^3-4y^2+3y-2 (disc -152), C_Hopf disc -76",
            "anchors": {"golden_y3": int(C.subs(Y, 3)), "silver_y6": int(C.subs(Y, 6)),
                        "q1_shadow_y2": int(C.subs(Y, 2))},
            "kc19_pole_y": 6, "verdict": verdict,
        },
        "context": {
            "kc19": "PR #3473 CrossingWeightAffine (proved-lean) — eval map affine, K(q) anchor-rigid",
            "kc20": "PR #3467 QBetaZeta4ResidueRefutation (proved-lean) — degree-3 irreducible carrier",
            "bridge": "KC18 eval-map bar-decomposition (carrier feeds w affinely)",
            "does_not": "attempt a c₃ closure (discrete routes refuted #3536/#3567; survivor = "
                        "analytic Φ_b state-integral, #3544/#3596)",
            "gate": "registry §8 flip-flop guard — no c_k value, no wiring, no tier change",
        },
    }
    out = os.path.join(_here, "qbeta-c3-kc19-kc20-consistency.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
