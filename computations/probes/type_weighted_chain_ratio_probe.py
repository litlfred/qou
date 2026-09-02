"""Weighting bonds by TYPE does not escape the b3 exclusion -- and the relocation.

TWO QUESTIONS, both from the merged BrunnianTripleExhaustion.

(1) RELOCATION.  That file excludes the CROSSING-ENERGY channel.  Which of the
seven live binding channels is that?  Answer: NONE of the four evaluable ones.
docs/audits/2026-08-31-binding-channel-taxonomy.md scores four TRACE-RATIO
channels (observe-early, log-ratio, bar-norm log, pairwise sum); production ships
ch1, which is neither extensive nor bond-additive.  So the exhaustion does NOT by
itself bind production, and saying so is a scope correction I owe.

(2) THE ESCAPE.  That file names the one free ingredient: def:crossing-energy
gives EVERY crossing the same weight, which is what makes mu a bare count.  The
obvious escape is a bond-dependent weight.  PRODUCTION ALREADY DOES THAT --
canonical_braid_crossings.d_for_ctype maps sigma -> 0 (pp), averaged -> -h/2
(pn), sigma_inv -> -h (nn).  This probe tests whether it helps.  It does not.

WHAT IS MEASURED, exactly (Fraction, weights in units of h):

  chain bond set, FORCED by the strand layout (QOU.Mass.StrandLayoutForcesChain,
  8421cd4163) -- A-1 adjacent bonds, not a modelling choice.

  per-isotope mu IS arrangement-dependent:  3H is -3h/2 as p-n-n but -h as n-p-n.
  the ISOSPIN AVERAGE is NOT, exactly on the arithmetic-mean locus

      w_pp + w_nn = 2 w_pn

  which production satisfies EXACTLY (0 + (-1) = 2*(-1/2)).  Note this is
  STRICTLY WEAKER than ChainBondOrderDependence.orderIndependent_iff's
  L_pp = L_pn = L_nn, which production FAILS -- so Bbar(3) is well-defined even
  though neither isotope's chain is.  I claimed mid-analysis that b3 was
  undefined without an ordering; computing both orderings showed otherwise, and
  the cancellation is the reason.

  and on that locus mu_triple/mu_pair = 2 IDENTICALLY, so

      b3/b2 = 2 - 3 = -1     for EVERY type weighting on the locus

  against the measured +0.6411239316: wrong sign, 256% off, and h CANCELS in the
  ratio so no q0 or convention choice moves it.  That is the same -1 the UNIFORM
  chain gives -- weighting by type turns mu from a count into a weighted count
  and leaves the one number b3 can see exactly where it was.

NO FREE PARAMETERS.  AME2020 plus production's own d_for_ctype values.

PRECISION.  Exact Fraction end to end; every serialized number an exact rational
string.  float() only inside f-strings for display.

LEAN.  QOU/Mass/TypeWeightedChainRatio.lean, 5 declarations, sorry-free,
lean-direct exit 0, standard three axioms.
"""
import datetime
import itertools
import json
import sys
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401

AME = {"D": F("2.224566"), "3H": F("8.481798"), "3He": F("7.718043")}

# production, canonical_braid_crossings.d_for_ctype, in units of h
W = {"pp": F(0), "pn": F(-1, 2), "nn": F(-1)}


def bonds(order):
    """Chain bond types for a nucleon ordering (A-1 adjacent bonds)."""
    return [("pn" if {order[i], order[i + 1]} == {"p", "n"}
             else order[i] * 2) for i in range(len(order) - 1)]


def mu(order):
    return sum(W[b] for b in bonds(order))


def main():
    ok = True
    assertions = []

    def check(name, cond, detail):
        nonlocal ok
        ok = ok and bool(cond)
        assertions.append({"name": name, "passed": bool(cond), "detail": detail})
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}\n         {detail}")

    b2 = AME["D"]
    r = ((AME["3H"] + AME["3He"]) / 2 - 3 * b2) / b2

    print("Type-weighted chain: relocation, and whether non-uniformity escapes\n")
    print(f"  production weights (units of h): {dict((k, str(v)) for k, v in W.items())}")
    print(f"  measured b3/b2 = {r} = {float(r):.10f}\n")

    check("production's weights are NOT uniform -- mu is a WEIGHTED count",
          len(set(W.values())) == 3,
          "d_for_ctype: sigma -> 0 (pp), averaged -> -h/2 (pn), sigma_inv -> -h "
          "(nn). So mu ∝ c does not describe production, and the exhaustion's "
          "free ingredient is already relaxed there -- one axis over")

    # per-isotope arrangement dependence
    orders = {}
    for lbl, comp in (("3H", "pnn"), ("3He", "ppn")):
        orders[lbl] = {"".join(o): mu("".join(o))
                       for o in set(itertools.permutations(comp))}
        for o, m in sorted(orders[lbl].items()):
            print(f"    {lbl:4} {o:5} bonds={str(bonds(o)):22} mu={m}")
    print()

    check("per-isotope mu IS arrangement-dependent",
          len(set(orders["3H"].values())) > 1
          and len(set(orders["3He"].values())) > 1,
          f"3H spans {sorted(set(map(str, orders['3H'].values())))}, "
          f"3He spans {sorted(set(map(str, orders['3He'].values())))} -- which "
          "nucleon sits in the middle changes the bond multiset")

    # isospin average, both extremes
    avg = {}
    for name, (o3H, o3He) in {"middle-heavy": ("pnn", "ppn"),
                              "middle-light": ("npn", "pnp")}.items():
        mt = (mu(o3H) + mu(o3He)) / 2
        avg[name] = mt
        print(f"  {name:13} 3H={o3H} 3He={o3He}  mu_t={mt}  "
              f"b3/b2={mt / mu('pn') - 3}")

    check("but the ISOSPIN AVERAGE is arrangement-INDEPENDENT",
          len(set(avg.values())) == 1,
          f"both extremes give mu_t = {list(avg.values())[0]}; the 3H and 3He "
          "arrangement shifts cancel against each other. I claimed mid-analysis "
          "that b3 was undefined without an ordering -- computing both showed "
          "otherwise, and this cancellation is why")

    check("the cancellation condition is the ARITHMETIC-MEAN locus, "
          "which production satisfies exactly",
          W["pp"] + W["nn"] == 2 * W["pn"],
          f"w_pp + w_nn = {W['pp'] + W['nn']} = 2 w_pn = {2 * W['pn']}. "
          "STRICTLY WEAKER than ChainBondOrderDependence.orderIndependent_iff's "
          "L_pp = L_pn = L_nn, which production FAILS (0, -1/2, -1 all differ) "
          "-- so Bbar(3) is well-defined though neither isotope's chain is")

    ratio = avg["middle-heavy"] / mu("pn")
    b3b2 = ratio - 3
    check("on that locus the triple/pair ratio is 2 IDENTICALLY",
          ratio == 2,
          "mu_t = 2 w_pn and mu_p = w_pn, so the ratio is 2 with no dependence "
          "on the weights and none on h (Lean ratio_eq_two_of_mean)")

    check("hence b3/b2 = -1 -- wrong sign, and h cannot move it",
          b3b2 == -1,
          f"model {b3b2} vs measured {float(r):+.10f}, "
          f"rel err {float((b3b2 - r) / r) * 100:.1f}%. h CANCELS in the ratio, "
          "so no q0 pin, convention or normalisation changes it")

    check("and it is the SAME -1 the uniform chain gives",
          b3b2 == F(-1),
          "CarrierCrossingQuantisation's 'chain / coordination z = A-1' row is "
          "also -1. Weighting by type turns mu from a count into a weighted "
          "count and leaves the one number b3 can see exactly where it was -- "
          "so this is not an escape from the exhaustion, it is inside it")

    witness = {
        "computation": "type-weighted-chain-ratio",
        "scriptFile": "probes/type_weighted_chain_ratio_probe.py",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "contentBlock": "qou-brng",
        "description": (
            "Production weights inter-nucleon bonds by TYPE (d_for_ctype: pp 0, "
            "pn -h/2, nn -h), so the uniformity that BrunnianTripleExhaustion "
            "named as its free ingredient is already relaxed. It does not help: "
            "on the arithmetic-mean locus w_pp + w_nn = 2 w_pn, which production "
            "satisfies exactly, the triple/pair ratio is 2 identically and "
            "b3/b2 = -1 -- the same value the uniform chain gives, wrong sign, "
            "with h cancelling. Also relocates the exhaustion: it excludes the "
            "crossing-energy channel, which is none of the four evaluable "
            "channels in the seven-channel taxonomy."),
        "production_weights_units_of_h": {k: str(v) for k, v in W.items()},
        "measured_b3_over_b2": str(r),
        "model_b3_over_b2": str(b3b2),
        "rel_err_fraction": str((b3b2 - r) / r),
        "per_isotope_arrangements": {
            lbl: {o: str(m) for o, m in sorted(d.items())}
            for lbl, d in orders.items()
        },
        "isospin_average": {k: str(v) for k, v in avg.items()},
        "mean_locus": {
            "condition": "w_pp + w_nn = 2 w_pn",
            "production_lhs": str(W["pp"] + W["nn"]),
            "production_rhs": str(2 * W["pn"]),
            "holds": W["pp"] + W["nn"] == 2 * W["pn"],
            "vs_orderIndependent_iff": (
                "ChainBondOrderDependence requires L_pp = L_pn = L_nn, which "
                "production FAILS; the mean locus is strictly weaker and is "
                "what the isospin average actually needs"),
        },
        "assertions": assertions,
        "allPassed": ok,
        "scope": (
            "(b) on type-weighted chain carriers, invariant named: on the "
            "arithmetic-mean locus the triple/pair ratio is 2, so b3/b2 = -1 "
            "for every such weighting. (a) elsewhere -- a weighting OFF that "
            "locus is not excluded here, but it buys an arrangement-dependent "
            "Bbar(3), which is a defect of its own since a nucleus has no "
            "middle."),
        "caveats": [
            "RELOCATION, and it limits what the exhaustion binds: the excluded "
            "channel is the CROSSING-ENERGY one, which is not among the four "
            "evaluable channels of the seven-channel taxonomy. Production ships "
            "a trace-ratio channel that is neither extensive nor bond-additive. "
            "So neither the exhaustion nor this file binds the shipped channel.",
            "The chain bond set is FORCED (StrandLayoutForcesChain), so this is "
            "not a choice of bond set. A different bond set is not available in "
            "this producer.",
            "A=3 only. b4 and the A=4 carrier are untouched.",
            "The weights are read from production's d_for_ctype in units of h. "
            "The colour-weighted 'averaged_weighted' ctype is NOT covered -- it "
            "carries a flavour split delta and may sit off the mean locus; that "
            "is the one type weighting this file does not exclude.",
        ],
        "lean": ("QOU/Mass/TypeWeightedChainRatio.lean "
                 "(5 declarations, sorry-free, lean-direct exit 0)"),
        "related": [
            "probes/brunnian-triple-exhaustion.witness.json",
            "probes/carrier-crossing-quantisation.witness.json",
        ],
        "source": "AME2020; canonical_braid_crossings.d_for_ctype",
    }
    out = _HERE / "type-weighted-chain-ratio.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(_COMP.parent)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
