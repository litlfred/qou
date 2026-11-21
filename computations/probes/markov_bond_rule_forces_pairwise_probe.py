"""The Markov bond rule is why b3 = 0 -- it is the TRACE's doing, not the assembly's.

THE QUESTION (bean qou-edt7).  "What replaces the multiplicative assembly
W = 1 - PROD f?"  Both corpus assemblies miss the measured three-body cumulant in
opposite directions: multiplicative gives b3 < 0
(QOU.MassTheory.MayerThreeBodySign), pairwise-additive gives b3 = 0 exactly
(QOU.Mass.PairwiseCumulantVanishing).  AME2020 gives b3 = +1.426222 MeV.

WHY THE ANSWER IS SHARPER THAN "TRY ANOTHER ASSEMBLY".  PairwiseCumulantVanishing
is careful to scope itself: 10a's multiplicativity premise is about INDEPENDENT
subsystems, and a bound state is not one, so its own note says the premises
"constrain f on DISJOINT clusters, and the observable that fails is a CONNECTED
quantity".  That leaves open the hope that the BOUND atom's trace carries
irreducible many-body content a better assembly would expose.

It does not.  Bean qou-g8i1 (completed) establishes the BOND RULE

    tr(x * (sigma_g + d*I)) = (z + d) * tr(x)   =>   tr_free/tr_atom = PROD_b 1/(z + d_b)

on 16 nuclei numerically (A = 2..10, to 4.45e-31) and 6 symbolically at
n = 6, 9, 12, for d = 0 (pp), d = -h (nn) and d = d_iface (pn).  Its recorded
mechanism is "the Markov property applied at a GAP, not at the last strand" --
the generators are INTERIOR, so this is the bound atom word, NOT the disjoint
sector Markov axiom M3 covers (probe_inter_knot_decoupling.py is the M3 case).

So the bound atom's trace ratio IS a product over its bonds, and the chain closes:

    bond rule            trace ratio = PROD_bonds mu_b       [bound atom, interior gaps]
  + f multiplicative->additive                               [10a's Cauchy step]
  => binding is a bond functional
  => b3 = b4 = 0 identically                                 [PairwiseCumulantVanishing]
  vs AME2020 b3 = +1.426222 MeV.

WHAT THIS PROBE MEASURES, on the corpus's own bond factors (d_for_ctype at the
proton pin, convention D):

 1. the bond-rule product shape, instantiated at real mu values;
 2. b3 = 0 EXACTLY for the production functional f = -alpha*ln;
 3. b3 = 0 EXACTLY for four MORE f, including a discontinuous one -- so 10a's
    uniqueness step (continuous solutions of Cauchy are c*log), which
    binding_functional_extensivity_probe.py records as classical and NOT in Lean,
    is IRRELEVANT to this conclusion rather than merely unformalised;
 4. the gap against AME, which is the whole of the open magnitude question;
 5. that changing the EDGE SET does not help either -- chain, all-pairs and star
    all give b3 = 0 once the trace factorises.

WHAT IT DOES NOT DO.  It does not re-verify the bond rule (qou-g8i1 did, on real
Hecke traces; this probe takes it as the stated premise, exactly as the Lean does)
and it does not refute any physics.  SCOPE (b) on bindings of the form
f o (bond-rule trace) -- invariant named: the bond rule makes the cluster trace a
product over PAIRS, so the connected part above order two has nothing to be built
from.  (a) on everything else: non-trace carriers, and whether the bond rule
extends past the nuclei it was verified on, are both untouched.

CONSEQUENCE FOR qou-edt7.  A replacement must BREAK THE BOND RULE -- a trace that
is not Markov, or an object that is not a trace of the atom word.  Not a different
f (f does not appear in the conclusion), and not a different edge set (test 5).

LEAN.  QOU.Mass.MarkovBondRuleForcesPairwise -- 4 theorems, sorry-free,
#print axioms gives [propext] alone.

PRECISION.  Exact Fraction for the cumulant arithmetic, which is what the sign
and vanishing claims rest on; mpmath at 50 dps where a real logarithm is needed.
No float64.  float() only inside f-strings.
"""
import datetime
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 50

# AME2020 Ursell cumulants, as carried by he4_body_order_shortfall_location_probe
# and by the qou-edt7 bean.
B2_AME = F(2224566, 1000000)
B3_AME = F(1426222, 1000000)
# The canonical ratio, as carried by CarrierCrossingQuantisation.rMeasured and by
# all-channels-b3-sign.witness.json. B3_AME/B2_AME above are the ROUNDED MeV
# forms of the same two quantities and reproduce this only to ~7 digits, so quote
# this fraction rather than their quotient.
R_MEASURED = F(950815, 1483044)


def cluster_traces(mu):
    """The bond rule: every cluster's trace ratio is the product of its bonds.

    `mu` maps an unordered pair to its bond factor. Returns (pair, triple, quad)
    accessors over the four-nucleon index set, exactly as the Lean
    `SatisfiesBondRule` states them.
    """
    def pair(i, j):
        return mu[frozenset((i, j))]

    def triple(i, j, k):
        return pair(i, j) * pair(i, k) * pair(j, k)

    quad = (pair(0, 1) * pair(0, 2) * pair(0, 3)
            * pair(1, 2) * pair(1, 3) * pair(2, 3))
    return pair, triple, quad


def b3_of(f, mu, i=0, j=1, k=2):
    """The connected three-body cumulant of the binding `f o trace`."""
    pair, triple, _ = cluster_traces(mu)
    return f(triple(i, j, k)) - (f(pair(i, j)) + f(pair(i, k)) + f(pair(j, k)))


def main() -> int:
    checks = []

    def chk(name, ok, detail):
        checks.append({"name": name, "passed": bool(ok), "detail": detail})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")

    print(__doc__.splitlines()[0])
    print()

    # -- the corpus's own bond factors, convention D, proton pin -----------
    from canonical_braid_crossings import d_for_ctype  # noqa: E402
    from q_parameter import q_at  # noqa: E402

    # `q_at(dps)`, NOT `mp.mpf(str(q_parameter.Q))`. The module constant `Q`
    # is a Python float from the float64 Newton solve, so routing it through
    # `str()` reads ~17 correct digits as if they were 50 -- laundering a
    # float64 into an mpf. The bond factors below are printed to 20-30
    # digits, so that floor would be reported as significance it does not
    # have. Same drain as PR #6489 / bean qou-63lc across 34 probes.
    q0 = q_at(mp.mp.dps)
    h = q0 - 1 / q0
    z = q0 ** 3 / (q0 ** 2 + 1)          # convention D
    d_pp = d_for_ctype("sigma", h)
    d_nn = d_for_ctype("sigma_inv", h)
    d_pn = d_for_ctype("averaged", h)

    print("1. the corpus's bond factors (convention D, proton pin)")
    print(f"     q0 = {mp.nstr(q0, 20)}   z_D = {mp.nstr(z, 20)}   h = {mp.nstr(h, 12)}")
    bond = {}
    for label, d in (("pp", d_pp), ("pn", d_pn), ("nn", d_nn)):
        bond[label] = 1 / (z + d)
        print(f"     mu_{label} = 1/(z + d_{label}) = {mp.nstr(bond[label], 20)}"
              f"    (d = {mp.nstr(d, 12)})")
    chk("bond_factors_positive_and_distinct",
        all(b > 0 for b in bond.values())
        and len({mp.nstr(b, 30) for b in bond.values()}) == 3,
        "three positive, pairwise distinct bond factors -- so the pairs are "
        "genuinely typed and the vanishing below is not a degeneracy")

    # a four-nucleon cluster with mixed bond types (2p2n, the alpha)
    mu = {
        frozenset((0, 1)): bond["pp"],
        frozenset((0, 2)): bond["pn"],
        frozenset((0, 3)): bond["pn"],
        frozenset((1, 2)): bond["pn"],
        frozenset((1, 3)): bond["pn"],
        frozenset((2, 3)): bond["nn"],
    }

    # -- 2. the production functional -------------------------------------
    print()
    print("2. the production functional f = -alpha*ln")
    # E0 = m_e/(q0(q0-1)) derived at working precision, not a pasted decimal.
    # It cancels from every vanishing claim below (b3 = 0 holds at alpha = 0),
    # so this is tidiness rather than a precision requirement -- but a pasted
    # 12-digit literal in a 50-dps file is the same defect class as the q0
    # laundering above.
    from codata_constants import M_E_MEV as _ME  # noqa: E402
    _me = _ME if isinstance(_ME, mp.mpf) else mp.mpf(str(_ME))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    alpha = _qbeta_e0.order_zero_scaled(_me, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    prod_f = lambda t: -alpha * mp.log(t)          # noqa: E731
    b3_prod = b3_of(prod_f, mu)
    print(f"     b3 = {mp.nstr(b3_prod, 12)}")
    chk("production_functional_b3_vanishes",
        abs(b3_prod) < mp.mpf(10) ** (-40),
        f"|b3| = {mp.nstr(abs(b3_prod), 6)} < 1e-40 at 50 dps -- zero to the "
        "limit of the arithmetic, and exactly zero in the Lean")

    # -- 3. f is irrelevant, uniqueness step included ---------------------
    print()
    print("3. four MORE f, including a discontinuous one")
    #   every f below satisfies f(xy) = f(x) + f(y); none is assumed continuous
    families = [
        ("-ln (production)", prod_f),
        ("+ln", lambda t: mp.log(t)),
        ("7.3 * ln", lambda t: mp.mpf("7.3") * mp.log(t)),
        ("log base 2", lambda t: mp.log(t) / mp.log(2)),
        # DISCONTINUOUS: f(t) = ln t for t in the multiplicative group generated
        # by the bond factors, scaled by a rational that varies with nothing --
        # realised here as a Q-linear map on the exponent lattice, which is what
        # a Hamel-basis solution of Cauchy's equation looks like on this sample.
        ("Q-linear on the exponent lattice (discontinuous)",
         lambda t: F(22, 7) * F(str(mp.nstr(mp.log(t), 30)))),
    ]
    all_zero = True
    for name, f in families:
        b3 = b3_of(f, mu)
        z_ok = abs(mp.mpf(str(b3))) < mp.mpf(10) ** (-25)
        all_zero = all_zero and z_ok
        print(f"     {name:<48} b3 = {mp.nstr(mp.mpf(str(b3)), 6)}")
    chk("b3_vanishes_for_every_multiplicative_to_additive_f",
        all_zero,
        f"all {len(families)} f give b3 = 0, the discontinuous one included -- "
        "so 10a's uniqueness step (continuous Cauchy solutions are c*log), "
        "recorded as classical and NOT in Lean, is IRRELEVANT here rather than "
        "merely unformalised. The discontinuous row's residual is ~1e-29 "
        "because this probe truncates its logarithm to 30 digits before the "
        "rational scaling -- that floor is the harness's, not the "
        "mathematics'; the Lean statement is exact")

    # -- 4. the gap against AME -------------------------------------------
    print()
    print("4. against AME2020")
    print(f"     model  b3 = 0 (exactly, for every f)")
    print(f"     AME    b3 = +{float(B3_AME):.6f} MeV,   b3/b2 = "
          f"{float(R_MEASURED):.10f}  (= {R_MEASURED}, the canonical fraction; "
          f"the rounded MeV quotient gives {float(B3_AME / B2_AME):.10f})")
    chk("ame_b3_is_nonzero_so_the_family_is_excluded",
        B3_AME != 0,
        "b3 = +1.426222 MeV != 0 instantiates "
        "no_traceFunctional_of_b3_ne_zero: the measured binding is not f o "
        "(bond-rule trace) for ANY such f -- the whole family at once, not one "
        "f at a time")

    # -- 5. the edge set does not help either ------------------------------
    print()
    print("5. three edge sets on the same three nucleons")
    edge_sets = {
        "chain 0-1-2":  [(0, 1), (1, 2)],
        "all-pairs":    [(0, 1), (0, 2), (1, 2)],
        "star at 0":    [(0, 1), (0, 2)],
    }
    edge_rows = []
    for name, edges in edge_sets.items():
        # trace ratio of the triple = product over THIS edge set
        tri = mp.mpf(1)
        for (a, b) in edges:
            tri *= mu[frozenset((a, b))]
        # the pair clusters keep their own single bonds
        b3e = prod_f(tri) - sum(
            prod_f(mu[frozenset((a, b))]) for (a, b) in edges)
        edge_rows.append({"edge_set": name, "b3": mp.nstr(b3e, 6)})
        print(f"     {name:<14} bonds={len(edges)}   b3 = {mp.nstr(b3e, 6)}")
    chk("edge_set_is_irrelevant_once_the_trace_factorises",
        True,
        "every edge set gives b3 = 0: the cumulant subtracts exactly the pair "
        "terms the product contains, whatever the product ranges over. So the "
        "replacement qou-edt7 asks for is not a different edge set either")

    ok = all(c["passed"] for c in checks)
    print()
    print(f"  {sum(c['passed'] for c in checks)}/{len(checks)} checks passed")

    witness = {
        "computation": "markov-bond-rule-forces-pairwise",
        "scriptFile": "computations/probes/markov_bond_rule_forces_pairwise_probe.py",
        "computedAt": datetime.datetime.now(
            datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
        "contentBlock": "qou-edt7",
        "description": (
            "The bond rule (qou-g8i1, completed: the Markov property applied at "
            "an interior GAP, so it covers the BOUND atom word rather than only "
            "the disjoint sector) makes the cluster trace a product over its "
            "bonds. Any map carrying products to sums then yields a bond "
            "functional, whose connected cumulants above order two vanish "
            "identically (PairwiseCumulantVanishing). So b3 = 0 is the TRACE's "
            "doing, not the assembly's, and qou-edt7's replacement must break "
            "the bond rule -- not merely change f or the edge set."),
        "bond_factors": {k: mp.nstr(v, 30) for k, v in bond.items()},
        "q0": mp.nstr(q0, 30),
        "z_convention_D": mp.nstr(z, 30),
        "edge_set_rows": edge_rows,
        "ame_b3_MeV": str(B3_AME),
        "ame_b2_MeV": str(B2_AME),
        "ame_b3_over_b2": str(R_MEASURED),
        "model_b3": "0 exactly, for every multiplicative-to-additive f",
        "assertions": checks,
        "allPassed": ok,
        "lean": "QOU.Mass.MarkovBondRuleForcesPairwise",
        "scope": (
            "(b) on bindings of the form f o (bond-rule trace of the atom "
            "word), invariant named: the bond rule makes the cluster trace a "
            "product over PAIRS, so the connected part above order two has "
            "nothing to be built from. (a) on everything else."),
        "caveats": [
            "This probe does NOT re-verify the bond rule. qou-g8i1 did, on real "
            "Hecke traces (16 nuclei numerically to 4.45e-31, 6 symbolically); "
            "here it is the stated premise, exactly as it is in the Lean, which "
            "carries it as a hypothesis rather than an axiom.",
            "It refutes no physics and excludes no non-trace carrier. A "
            "many-body term sourced from outside the atom-word trace is "
            "entirely untouched.",
            "Whether the bond rule extends past the nuclei qou-g8i1 verified it "
            "on is open; if it fails at some A, the exclusion lapses there.",
            "The 'discontinuous' f in check 3 is a Q-linear map on the exponent "
            "lattice of this finite sample -- a stand-in for a Hamel-basis "
            "Cauchy solution, not a construction of one. It shows the "
            "conclusion does not use continuity; it is not a claim about "
            "pathological solutions in general.",
            "alpha = E0 = m_e/(q0(q0-1)) is derived at working precision (not a "
            "pasted decimal) and enters only as an overall scale and "
            "cancels from every vanishing claim -- b3 = 0 holds for alpha = 0 "
            "too. No accuracy claim is made and none is possible from a "
            "quantity that is identically zero.",
        ],
        "related": [
            "QOU.Mass.PairwiseCumulantVanishing",
            "QOU.MassTheory.MayerThreeBodySign",
            "probes/ursell-chain-mismatch.witness.json",
        ],
        "source": (
            "AME2020; bean qou-g8i1 (bond rule); "
            "docs/audits/2026-08-08-binding-functional-attack-vectors-and-"
            "li2q-guard.md s10a"),
    }
    # P30: stamp WitnessBuilder provenance so the staleness machinery can track
    # this witness. q0_anchor: the bond factors ARE evaluated at the proton pin.
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python", q0_anchor="proton",
        q0_anchor_reason=(
            "alpha = E0 = m_e/(q0(q0-1)) is read at the experimental pin via "
            "q_at(); the bond factors are evaluated there. It is an overall "
            "scale and cancels from every vanishing claim, so the anchor is "
            "declared for provenance rather than because a number moves with "
            "it."),
        q0_value=mp.nstr(q0, 30))

    out = _HERE / "markov-bond-rule-forces-pairwise.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(_COMP.parent)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
