"""Every evaluable binding channel gives b3 the WRONG SIGN -- the shipped one too.

THE CLOSING MEASUREMENT of the qou-brng b3 arc.  Everything before it excluded
one channel at a time: the crossing-energy count (BrunnianTripleExhaustion), the
type-weighted bond count and the colour-weighted interface
(TypeWeightedChainRatio).  Each exclusion carried the same caveat -- production
ships something else, so none of it bound production.  This removes the caveat by
testing all four evaluable channels at once, including ch1, the shipped one.

WHAT IS MEASURED.  The Ursell three-body cumulant, from each channel's own
binding:

    b2 = B(2H),   Bbar(3) = (B(3H) + B(3He))/2,   b3 = Bbar(3) - 3 b2

against the AME2020 value b3/b2 = 950815/1483044 = +0.6411239316.

RESULT -- all four NEGATIVE:

    channel                         b3/b2      vs measured
    ch1  observe-early (SHIPPED)   -1.3995        -318.3 %
    ch3  log-ratio                 -0.9679        -251.0 %
    ch4  bar-norm log              -0.9681        -251.0 %
    ch5  pairwise sum              -1.0205        -259.2 %

The three bond-additive channels cluster near -1 because on the chain they sum
one term per bond and A=3 has twice A=2's bond count -- the same ratio-of-2 that
TypeWeightedChainRatio proves pins b3/b2 to -1.  ch1 differs (-1.3995) precisely
because it is NOT additive: its trace prefactor |tr_p|^Z |tr_n|^N is exponential
in A.  So the two structural families fail SEPARATELY, not as one artefact.

WHY THIS IS THE CAPSTONE.  Combined with the exclusions above, no channel the
corpus can evaluate produces a positive b3 -- and the failure is a SIGN, which no
magnitude, normalisation, anchor or convention can repair.  It matches the t7qv
arc arriving independently: the many-body term measured directly is negative in
all eight A=3 flavour orderings, with an alpha-free ceiling short by 2.0975x.

PROVENANCE.  B/A values are the output of main's own
computations/binding_channel_taxonomy_probe.py, re-run in this container and
reproducing docs/audits/2026-08-31-binding-channel-taxonomy.md byte-for-byte.
They are printed to ~8 significant figures.  That is ample for a SIGN test and
the margins are 251-318 %, nowhere near marginal -- but it is NOT enough for a
precision claim, and none is made here.

PRECISION.  Exact Fraction over the producer's decimal strings; no float
arithmetic.  float() only inside f-strings for display.
"""
import datetime
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
from qou_substrate.witness import WitnessBuilder  # noqa: E402

# B/A, verbatim from binding_channel_taxonomy_probe (re-run 2026-09-02;
# identical to docs/audits/2026-08-31-binding-channel-taxonomy.md).
BA = {
    "ch1 observe-early (SHIPPED)": {
        "2H": "0.21770174", "3H": "0.2317105",
        "3He": "0.23285074", "4He": "0.219016"},
    "ch3 log-ratio": {
        "2H": "1.4165813", "3H": "2.2103152",
        "3He": "1.6279574", "4He": "2.1704138"},
    "ch4 bar-norm log": {
        "2H": "1.4168774", "3H": "1.9193337",
        "3He": "1.9193337", "4He": "2.1705619"},
    "ch5 pairwise sum": {
        "2H": "1.1648428", "3H": "1.5884235",
        "3He": "1.4860155", "4He": "1.7234078"},
}
NUCLEON_COUNT = {"2H": 2, "3H": 3, "3He": 3, "4He": 4}
MEASURED = F(950815, 1483044)


def cumulants(ba):
    """b2, b3 and b3/b2 from a channel's B/A table, exactly."""
    B = {k: F(v) * NUCLEON_COUNT[k] for k, v in ba.items()}
    b2 = B["2H"]
    b3 = (B["3H"] + B["3He"]) / 2 - 3 * b2
    return b2, b3, b3 / b2


def main():
    ok = True
    assertions = []

    def check(name, cond, detail):
        nonlocal ok
        ok = ok and bool(cond)
        assertions.append({"name": name, "passed": bool(cond), "detail": detail})
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}\n         {detail}")

    print("Ursell b3 across every evaluable binding channel\n")
    print(f"  measured b3/b2 = {MEASURED} = +{float(MEASURED):.10f}\n")
    print(f"  {'channel':28} {'b2':>10} {'b3':>11} {'b3/b2':>9} {'rel err':>10}")

    rows = []
    for ch, ba in BA.items():
        b2, b3, ratio = cumulants(ba)
        rows.append({"channel": ch, "b2": str(b2), "b3": str(b3),
                     "b3_over_b2": str(ratio),
                     "rel_err_fraction": str((ratio - MEASURED) / MEASURED)})
        print(f"  {ch:28} {float(b2):10.5f} {float(b3):11.5f} "
              f"{float(ratio):9.4f} {float((ratio - MEASURED) / MEASURED) * 100:9.1f}%")
    print()

    ratios = {r["channel"]: F(r["b3_over_b2"]) for r in rows}

    check("EVERY evaluable channel gives b3 the WRONG SIGN",
          all(v < 0 for v in ratios.values()),
          "all four are negative against a measured +0.6411239316; margins "
          "251-318%, so the producer's ~8 significant figures are ample for a "
          "sign test")

    check("the SHIPPED channel is among them",
          ratios["ch1 observe-early (SHIPPED)"] < 0,
          f"ch1 = {float(ratios['ch1 observe-early (SHIPPED)']):.4f}. This is "
          "the channel binding_canonical actually ships, and the one none of "
          "the earlier exclusions in this arc could reach")

    additive = [v for k, v in ratios.items() if not k.startswith("ch1")]
    check("the three bond-additive channels cluster near -1",
          all(abs(v - F(-1)) < F(1, 20) for v in additive),
          f"ch3, ch4, ch5 = {[round(float(v), 4) for v in additive]}. On the "
          "chain they sum one term per bond and A=3 has twice A=2's bond count "
          "-- the same ratio-of-2 that TypeWeightedChainRatio proves pins "
          "b3/b2 to -1")

    check("ch1 differs BECAUSE it is not additive -- two families, two failures",
          abs(ratios["ch1 observe-early (SHIPPED)"] - F(-1)) > F(1, 4),
          f"ch1 = {float(ratios['ch1 observe-early (SHIPPED)']):.4f}, away from "
          "the additive cluster. Its trace prefactor |tr_p|^Z|tr_n|^N is "
          "exponential in A, so it fails SEPARATELY rather than as one shared "
          "artefact -- which makes the joint negative harder to blame on a "
          "single modelling choice")

    check("the failure is a SIGN, so no magnitude repair reaches it",
          all(v < 0 for v in ratios.values()) and MEASURED > 0,
          "no normalisation, anchor, convention or overall scale changes the "
          "sign of b3/b2; a positive measured value against four negative "
          "models is qualitative")

    witness = {
        "computation": "all-channels-b3-sign",
        "scriptFile": "probes/all_channels_b3_sign_probe.py",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "contentBlock": "qou-brng",
        "description": (
            "All four evaluable binding channels -- including ch1, the one "
            "binding_canonical ships -- give the Ursell three-body cumulant "
            "ratio b3/b2 a NEGATIVE value, against a measured +0.6411239316. "
            "The three bond-additive channels cluster near -1 for the reason "
            "TypeWeightedChainRatio proves; ch1 sits at -1.3995 because it is "
            "not additive, so the two structural families fail separately. "
            "Closes the qou-brng b3 arc: no channel the corpus can evaluate "
            "produces a positive b3, and a sign is not repairable by magnitude."),
        "measured_b3_over_b2": str(MEASURED),
        "channels": rows,
        "assertions": assertions,
        "allPassed": ok,
        "scope": (
            "(b) on the four EVALUABLE channels of the seven-channel taxonomy, "
            "invariant named: the sign of b3. (a) on the three not evaluated "
            "there (ch2 needs per-partition characters and is self-marked "
            "refuted; ch6 needs Vol(K_bind), which the corpus has only for "
            "A <= 3 and which is 0 for the deuteron; ch7 is a deprecation "
            "candidate carrying acknowledged-anchor constants). Nothing here "
            "says the framework cannot have a positive b3 -- it says none of "
            "the four channels that can currently be computed produces one."),
        "caveats": [
            "PRECISION. The B/A inputs are the taxonomy producer's printed "
            "output at ~8 significant figures. Ample for a SIGN test with "
            "251-318% margins; NOT enough for a precision claim, and none is "
            "made. A high-dps re-derivation would change no digit that matters "
            "here.",
            "This uses the CHAIN bond set, which StrandLayoutForcesChain proves "
            "is forced by the strand layout rather than chosen -- so the shared "
            "negative is not an artefact of a bond-set choice.",
            "b4 is not tested. The A=4 row is carried in the table but the "
            "quad cumulant needs the A=4 carrier's six pairs, which is a "
            "different object and untouched by this arc.",
            "ch2/ch6/ch7 are classified from source in the taxonomy, not "
            "re-evaluated there or here. Calling the arc closed over ALL seven "
            "would overstate what was measured.",
        ],
        "provenance": (
            "computations/binding_channel_taxonomy_probe.py, re-run in this "
            "container 2026-09-02, reproducing "
            "docs/audits/2026-08-31-binding-channel-taxonomy.md"),
        "related": [
            "probes/type-weighted-chain-ratio.witness.json",
            "probes/brunnian-triple-exhaustion.witness.json",
        ],
        "source": "AME2020; binding_channel_taxonomy_probe B/A output",
    }
    # P30: stamp WitnessBuilder provenance (scriptHash / commitSha /
    # engine) so the staleness machinery can track this witness. Written
    # with raw json below because the payload carries a flat
    # assertions/allPassed shape, which is what stamp_staleness_metadata
    # is for; wrap_legacy().save() would reshape it.
    # q0_anchor=False: nothing here evaluates at q0 -- the arithmetic is
    # exact rational over AME literals and integers -- so stamping an
    # anchor would assert a dependence this probe does not have.
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python", q0_anchor=False)

    out = _HERE / "all-channels-b3-sign.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(_COMP.parent)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
