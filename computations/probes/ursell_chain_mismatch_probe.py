"""The additive channels' b3 = -b2 is the Ursell INVERSION, not a three-body term.

REFRAMES A RESULT OF MY OWN.  all_channels_b3_sign_probe measured b3/b2 < 0 for
all four evaluable binding channels and read the three bond-additive ones
clustering at ~ -1 as a shared physical failure.  For those three it is
arithmetic, and this probe is the arithmetic.  (That probe's own docstring
already named the mechanism in prose -- "A=3 has twice A=2's bond count".  What
is new here is that it is exact, and that it does not depend on the chain.)

THE MISMATCH.  The Ursell inversion

    b3 = Bbar(3) - 3 b2

subtracts C(3,2) = 3 pair terms, because three objects have three pairs.  The
bond set is a CHAIN with A-1 bonds -- and QOU.Mass.StrandLayoutForcesChain proves
that is forced by the strand layout rather than chosen.  The counts agree at
A = 2 (1 = 1) and diverge from A = 3 (3 vs 2), which is exactly where b3 lives.

For a chain-additive model with uniform bond value b, B(A) = (A-1)b:

    b2 = b ,   b3 = 2b - 3b = -b ,   b3/b2 = -1     identically, for every b.

THE GENERALISATION -- and this is the part worth having.  Changing the bond set
does not help.  For any binding additive over a bond set with a UNIFORM bond
value the value cancels and only the counts survive:

    b3/b2 = n(3)/n(2) - 3 .

Two bound nucleons have exactly one bond, so n(2) = 1; a simple bond set on three
nucleons has at most C(3,2) = 3 of them.  Hence

    b3/b2 = n(3) - 3 <= 0   for EVERY uniform pairwise-bond model,

with the chain (n(3) = 2) at -1 and all-pairs (n(3) = 3) at exactly 0.  The
measured value is +0.6411239316.  So the chain is not the culprit -- the
uniformity is.

SURVIVING ESCAPE, stated because it is the next direction and this probe does
NOT close it: non-uniformity.  If the A=3 bonds are stronger than the deuteron
bond then b3/b2 = 3w/w_d - 3 > 0 whenever w > w_d.  Nothing here touches that.

NOT AFFECTED.  ch1 = -1.3995, the SHIPPED channel, is not bond-additive -- its
trace prefactor |tr_p|^Z |tr_n|^N is exponential in A -- and fails for its own
reasons.  This probe measures how far each channel sits from -1 precisely to
separate the three that the identity explains from the one it does not.  The AME
b3/b2 = 950815/1483044 is data; no inversion convention alters it.

SCOPE.  (b) on uniform pairwise-bond-additive binding models, invariant named:
the bond count on three nodes is capped at C(3,2) = 3 while the inversion
subtracts three pair terms.  (a) on everything else -- this excludes no channel,
refutes no physics, and says nothing about ch1, about non-uniform bond weights,
or about non-pairwise carriers.

LEAN.  QOU.Mass.UrsellChainMismatch, 12 declarations, sorry-free, axioms only
[propext, Classical.choice, Quot.sound].

PRECISION.  Exact Fraction throughout; the channel b3/b2 values are read back
verbatim from all-channels-b3-sign.witness.json as rationals.  float() only
inside f-strings for display.
"""
import datetime
import json
import sys
from fractions import Fraction as F
from math import comb
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
from qou_substrate.witness import WitnessBuilder  # noqa: E402

# AME2020 measured Ursell ratio, as carried by CarrierCrossingQuantisation
# (Lean `rMeasured`) and by all_channels_b3_sign_probe.
R_MEASURED = F(950815, 1483044)


def pair_count(A: int) -> int:
    """Pairs among A objects -- what the Ursell inversion charges for."""
    return comb(A, 2)


def chain_bond_count(A: int) -> int:
    """Bonds in a chain on A nucleons -- what the forced layout supplies."""
    return A - 1


def chain_binding(b: F, A: int) -> F:
    """Bond-additive binding on the chain with uniform bond value b."""
    return F(A - 1) * b


def ursell_b3_over_b2(b2: F, b3bar: F) -> F:
    """b3/b2 with b3 = Bbar(3) - 3 b2."""
    return (b3bar - 3 * b2) / b2


def b_ratio_of_bond_counts(n2: int, n3: int) -> F:
    """b3/b2 for a uniform bond-additive model, from the counts alone."""
    return F(n3, n2) - 3


def main() -> int:
    checks = []

    def chk(name: str, ok: bool, detail: str) -> None:
        checks.append({"name": name, "passed": bool(ok), "detail": detail})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")

    print(__doc__.splitlines()[0])
    print()

    # -- 1. The two counts, and where they diverge ------------------------
    print("1. pair count vs chain bond count")
    table = []
    for A in (2, 3, 4, 5):
        pc, bc = pair_count(A), chain_bond_count(A)
        table.append({"A": A, "pairs": pc, "chain_bonds": bc,
                      "deficit": pc - bc})
        print(f"     A={A}  pairs={pc}  chain bonds={bc}  deficit={pc - bc}")

    chk("counts_agree_at_two",
        pair_count(2) == chain_bond_count(2),
        f"C(2,2)=1 and 2-1=1 -- the deuteron is the one place they agree")
    chk("pair_deficit_at_three",
        pair_count(3) - chain_bond_count(3) == 1,
        "3 pairs vs 2 chain bonds: a deficit of exactly ONE pair, which is "
        "the whole of the -b2 below")
    chk("deficit_widens",
        pair_count(4) - chain_bond_count(4) == 3,
        "A=4: 6 vs 3, deficit 3 -- not a small-A accident")

    # -- 2. The identity, for arbitrary bond values ----------------------
    print()
    print("2. chain-additive b3/b2, for a spread of bond values")
    ratios = []
    for b in (F(1), F(-1), F(2224566, 1000000), F(-7, 3), F(1, 1000000)):
        b2 = chain_binding(b, 2)
        b3bar = chain_binding(b, 3)
        r = ursell_b3_over_b2(b2, b3bar)
        ratios.append(r)
        print(f"     b={str(b):>16}  b2={str(b2):>16}  Bbar(3)={str(b3bar):>16}"
              f"  b3/b2={r}")
    chk("chain_ratio_is_minus_one_identically",
        all(r == -1 for r in ratios),
        f"all {len(ratios)} bond values give exactly -1 -- the bond value "
        "cancels, so this carries no physics")

    # -- 3. The generalisation: bond counts alone ------------------------
    print()
    print("3. any uniform pairwise-bond model, from the counts alone")
    rows = []
    for n3 in range(0, pair_count(3) + 1):
        r = b_ratio_of_bond_counts(1, n3)
        rows.append({"n3": n3, "b3_over_b2": str(r)})
        tag = ("  <- chain" if n3 == 2 else
               "  <- all-pairs (the MAXIMUM)" if n3 == 3 else "")
        print(f"     n(2)=1  n(3)={n3}  b3/b2={r}{tag}")

    chk("chain_row_is_minus_one",
        b_ratio_of_bond_counts(1, 2) == -1,
        "n(3)=2 reproduces the chain identity from counts alone")
    chk("all_pairs_row_is_zero",
        b_ratio_of_bond_counts(1, 3) == 0,
        "n(3)=3 gives exactly 0 -- the all-pairs bond set is the boundary "
        "case, and it is still not positive")
    chk("every_uniform_bond_model_nonpositive",
        all(b_ratio_of_bond_counts(1, n3) <= 0
            for n3 in range(0, pair_count(3) + 1)),
        f"b3/b2 = n(3) - 3 <= 0 for every n(3) <= C(3,2) = {pair_count(3)}; "
        f"measured is +{float(R_MEASURED):.10f} > 0, so NO uniform pairwise-"
        "bond model reaches it")

    # the escape, measured rather than asserted
    print()
    print("4. the surviving escape: NON-uniform bond value")
    w_over_wd_needed = (R_MEASURED + 3) / 3
    r_at_needed = 3 * w_over_wd_needed - 3
    print(f"     all-pairs with A=3 bond w and deuteron bond w_d:")
    print(f"       b3/b2 = 3 w/w_d - 3 , positive iff w/w_d > 1")
    print(f"     to hit the measured value needs w/w_d = {w_over_wd_needed} "
          f"= {float(w_over_wd_needed):.10f}")
    chk("nonuniform_escape_is_open",
        r_at_needed == R_MEASURED and w_over_wd_needed > 1,
        f"w/w_d = {float(w_over_wd_needed):.6f} (> 1) reproduces the measured "
        "value exactly -- so non-uniformity is NOT excluded here, and is the "
        "next direction")

    # -- 5. Which measured channels the identity explains ----------------
    print()
    print("5. distance from -1 for each measured channel")
    src = _HERE / "all-channels-b3-sign.witness.json"
    chan = json.loads(src.read_text())["channels"]
    dists = {}
    for c in chan:
        r = F(c["b3_over_b2"])
        d = abs(r + 1)
        dists[c["channel"]] = d
        print(f"     {c['channel']:<30} b3/b2={float(r):>10.6f}  "
              f"|r+1|={float(d):.6f}")

    additive = [v for k, v in dists.items() if not k.startswith("ch1")]
    ch1 = [v for k, v in dists.items() if k.startswith("ch1")][0]
    chk("three_additive_channels_sit_at_minus_one",
        all(d < F(1, 10) for d in additive) and ch1 > F(1, 10),
        f"ch3/ch4/ch5 all within {float(max(additive)):.4f} of -1 (the "
        f"identity), while ch1 -- the SHIPPED, non-additive channel -- is "
        f"{float(ch1):.4f} away and is NOT explained by it")

    ok = all(c["passed"] for c in checks)
    print()
    print(f"  {sum(c['passed'] for c in checks)}/{len(checks)} checks passed")

    witness = {
        "computation": "ursell-chain-mismatch",
        "scriptFile": "computations/probes/ursell_chain_mismatch_probe.py",
        "computedAt": datetime.datetime.now(
            datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
        "description": (
            "The three bond-additive channels' b3/b2 ~ -1 is the Ursell "
            "inversion meeting a bond set, not a three-body finding. "
            "Generalised: b3/b2 = n(3)/n(2) - 3 <= 0 for EVERY uniform "
            "pairwise-bond model, since n(2) = 1 and n(3) <= C(3,2) = 3."),
        "measured_b3_over_b2": str(R_MEASURED),
        "count_table": table,
        "bond_count_rows": rows,
        "chain_ratio": "-1",
        "all_pairs_ratio": "0",
        "nonuniform_w_over_wd_needed": str(w_over_wd_needed),
        "channel_distance_from_minus_one": {
            k: str(v) for k, v in dists.items()},
        "assertions": checks,
        "allPassed": ok,
        "lean": "QOU.Mass.UrsellChainMismatch",
        "scope": (
            "(b) on UNIFORM pairwise-bond-additive binding models, invariant "
            "named: the bond count on three nodes is capped at C(3,2) = 3 "
            "while the Ursell inversion subtracts three pair terms. (a) on "
            "everything else."),
        "caveats": [
            "This EXCLUDES NO CHANNEL and refutes no physics. It reclassifies "
            "why three already-measured channels failed; the measurement "
            "itself is unchanged.",
            "ch1, the SHIPPED channel, is NOT explained by this -- it is not "
            "bond-additive (trace prefactor exponential in A) and fails for "
            "its own reasons. Check 5 measures that separation rather than "
            "assuming it.",
            "NON-UNIFORM bond values are NOT excluded. w/w_d = "
            f"{float(w_over_wd_needed):.6f} reproduces the measured value "
            "exactly, and that is the surviving direction.",
            "The cap n(3) <= 3 assumes a SIMPLE pairwise bond set. A carrier "
            "with genuine 3-body terms, or with multiplicity on a bond, is "
            "outside this argument entirely.",
            "The channel b3/b2 values are read verbatim from "
            "all-channels-b3-sign.witness.json; their own ~8-significant-"
            "figure provenance caveat carries over. Check 5 is a "
            "distance-from--1 comparison with margins > 1.3, nowhere near "
            "that resolution.",
        ],
        "related": [
            "probes/all-channels-b3-sign.witness.json",
            "probes/type-weighted-chain-ratio.witness.json",
            "probes/brunnian-triple-exhaustion.witness.json",
        ],
        "source": "AME2020; all-channels-b3-sign.witness.json",
    }
    # P30: stamp WitnessBuilder provenance (scriptHash / commitSha / engine)
    # so the staleness machinery can track this witness. Raw json below
    # because the payload is the flat assertions/allPassed shape.
    # q0_anchor=False: nothing here evaluates at q0 -- the arithmetic is
    # exact rational over integers and AME literals.
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python", q0_anchor=False)

    out = _HERE / "ursell-chain-mismatch.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(_COMP.parent)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
