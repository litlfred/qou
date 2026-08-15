#!/usr/bin/env python3
"""volume_binding_four_point.py — the four-point volume-binding test proposed as
the next step in `docs/coordination/2026-08-07-l2-volume-binding-cluster.md` §5,
run at witness precision, and the finding that it CANNOT be completed with
existing corpus data.

BACKGROUND
    That ledger recorded a two-point observation: using pure `Vol` with zero free
    parameters, the A=3 mirror pair gives

        B(T)/B(3He) = 1.0990   vs   Vol(T)/Vol(3He) = 1.1308   ->  2.90% miss

    and flagged it honestly: "this is a TWO-POINT observation on one mirror pair;
    `~4` is a constant fitted to two numbers and means nothing until it holds
    across D / T / 3He / 4He; and it is scratch float64, NOT witness-grade."
    §5 then set the next task: redo it across all four L2 binding targets,
    ratio-only, zero free parameters -- listed as blocked on the author's
    Reading-1-vs-Reading-2 ruling.

WHAT THIS SCRIPT FINDS
    The four-point test is not blocked on the ruling. It is blocked on DATA, and
    it is unrunnable under BOTH readings:

      * Reading 1 (literal mass-braid H_9 closures) -- every closure is
        non-hyperbolic, Vol = 0 identically. Zero usable points. Already recorded
        in `he4-link-volume-braid-closure.witness.json` (3H closure is
        4-component vs 8_11's 1; 3He closure 4-component vs Borromean's 3; all
        non-geometric).

      * Reading 2 (SDP binding-link registry) -- the registry contains exactly
        THREE atoms (`n_atoms = 3`: deuteron, tritium, he3). There is no 4He
        entry: the SDP solver scope is A <= 3, and A=4 needs B_5 Hoefsmit plus
        the Clarabel backend (conj #604 / GAP-A-1). Of the three present, the
        deuteron maps to the Hopf link, which is Seifert-fibred with Vol = 0.
        => Reading 2 supplies TWO usable points, T and 3He -- exactly the mirror
        pair the two-point observation already used.

    So the ledger's own falsification criterion ("not evidence until it survives
    four points") cannot be met by either reading with data now in the corpus.
    The honest count is 2 usable points out of 4 required, and the missing two
    are missing for different and independent reasons.

WHAT IT DOES COMPUTE
    Everything the existing data does support, at 70 dps rather than scratch
    float64: the mirror-pair ratio test, the implied bond-count constant, and an
    explicit statement of what each missing point would require.

    The only 4He volume anywhere in the corpus is Vol_4 ~ 8.046, a BACK-OUT from
    the bond-count model, not a measured link volume -- and it disagrees with the
    provisional doubly-magic 2*Vol(Borromean) = 14.655 by ~1.8x. Using either as
    a fourth point would be assuming the law under test. Both are reported as
    excluded inputs, and the ratio test is run WITHOUT them.

No fit, no AME inversion, no free parameter, nothing wired to production.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))

from mpmath import mpf, nstr  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from knot_volumes import VOL_8_11_MPF, VOL_BORROMEAN_MPF  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)

set_compute_dps()

# ---------------------------------------------------------------------------
# The four L2 binding targets and their Reading-2 (SDP registry) links.
# Registry source: binding-k-solver.witness.json  data.registry  (n_atoms = 3).
# ---------------------------------------------------------------------------

TARGETS = [
    # name,  A,  B_AME,                              link,        Vol,        usable
    ("D",    2, mpf(str(AME_B_DEUTERON_MEV_VALIDATION)), "Hopf L2a1", mpf(0), False),
    ("T",    3, mpf(str(AME_B_TRITIUM_MEV_VALIDATION)),  "8_11",      VOL_8_11_MPF, True),
    ("3He",  3, mpf(str(AME_B_HE3_MEV_VALIDATION)),      "L6a4=Borr", VOL_BORROMEAN_MPF, True),
    ("4He",  4, mpf(str(AME_B_HE4_MEV_VALIDATION)),      "(none)",    None, False),
]

EXCLUSION = {
    "D": "Reading 2 assigns the Hopf link L2a1, which is Seifert-fibred: "
         "Vol = 0 exactly. The corpus's claimed deuteron match was obtained by "
         "substituting Vol(B_3) for Vol(Hopf) -- an unjustified substitution "
         "(2026-08-07 ledger §6), so it may not be used as a data point here. "
         "TWO reasons now, not one: that match was also quoted as +0.2% under "
         "trace convention C, excised by owner ruling 2026-08-09; under the "
         "canonical convention D the same computation gives -6.3% and the "
         "witness records the assertion as failing (bean qou-jdhm). So the "
         "exclusion below is if anything better founded than when written -- "
         "there is no deuteron success to exclude, only a near-miss.",
    "4He": "No SDP binding link exists. The registry stops at A = 3 (solver "
           "scope A <= 3; A = 4 needs B_5 Hoefsmit + Clarabel, conj #604 / "
           "GAP-A-1). The only 4He volume in the corpus is Vol_4 ~ 8.046, a "
           "BACK-OUT from the bond-count model (assuming the law under test), "
           "and it disagrees with the provisional doubly-magic "
           "2*Vol(Borromean) = 14.655 by ~1.8x.",
}


def main() -> None:
    dash = "-" * 74
    print("Volume-binding across the four L2 binding targets (Reading 2)\n")
    print(f"{'target':6s} {'A':>2s} {'B_AME (MeV)':>14s} {'link':>12s} "
          f"{'Vol':>14s}  usable")
    print(dash)
    for name, A, B, link, vol, usable in TARGETS:
        vs = "-" if vol is None else nstr(vol, 10)
        print(f"{name:6s} {A:2d} {nstr(B, 10):>14s} {link:>12s} {vs:>14s}  "
              f"{'yes' if usable else 'NO'}")
    print(dash)

    usable = [(n, A, B, v) for n, A, B, _l, v, u in TARGETS if u]
    print(f"\nusable points: {len(usable)} of 4 required "
          f"({', '.join(n for n, *_ in usable)})\n")
    for k, why in EXCLUSION.items():
        print(f"  {k} excluded: {why}\n")

    # ---- the two-point mirror-pair test, at witness precision --------------
    (_, _, B_T, V_T), (_, _, B_He3, V_He3) = usable
    r_B = B_T / B_He3
    r_V = V_T / V_He3
    ratio_of_ratios = r_V / r_B
    miss_pct = (ratio_of_ratios - 1) * 100

    print("Mirror-pair ratio test (zero free parameters -- the overall")
    print("constant cancels identically in the ratio):")
    print(f"    B(T)/B(3He)      = {nstr(r_B, 12)}")
    print(f"    Vol(T)/Vol(3He)  = {nstr(r_V, 12)}")
    print(f"    ratio of ratios  = {nstr(ratio_of_ratios, 12)}"
          f"   ->  {nstr(miss_pct, 6)}% miss")

    # ---- the implied bond-count constant, per point -----------------------
    print("\nImplied constant in  B = c * m_e * Vol(K)  (NOT a prediction --")
    print("this is the law inverted at each point; spread is the diagnostic):")
    me = mpf(str(M_E_MEV))
    cs = []
    for name, _A, B, V in usable:
        c = B / (me * V)
        cs.append(c)
        print(f"    {name:5s}  c = {nstr(c, 12)}")
    spread = abs(cs[0] - cs[1]) / ((cs[0] + cs[1]) / 2) * 100
    print(f"    spread = {nstr(spread, 6)}%   (identical to the ratio-test miss,")
    print("             as it must be -- these are the same two numbers)")

    print("\n" + "=" * 74)
    print("FINDING: the four-point test is blocked on DATA, not on the ruling.")
    print("Reading 1 gives 0 usable points (all closures non-hyperbolic).")
    print("Reading 2 gives 2 (T, 3He) -- the same mirror pair as before.")
    print("A ruling either way does not produce a third or fourth point.")
    print("The two-point '~4' constant therefore remains exactly as strong as")
    print("the 2026-08-07 ledger already called it: not evidence.")
    print("=" * 74)

    w = WitnessBuilder("volume-binding-four-point", engine="mpmath")
    w.add_assertion("usable_points_of_four", len(usable), 2, tolerance=0,
                    source="Reading 2 registry has n_atoms=3; deuteron->Hopf "
                           "has Vol=0; 4He has no SDP link at all.")
    w.add_assertion("deuteron_volume_is_zero", str(TARGETS[0][4]), "0.0",
                    tolerance="0",
                    source="Hopf link L2a1 is Seifert-fibred.")
    w.add_assertion("mirror_pair_ratio_of_ratios",
                    nstr(ratio_of_ratios, 30), "1.0290", tolerance="1e-3",
                    source="Reproduces the 2026-08-07 ledger's scratch-float64 "
                           "2.90% at 70 dps.")
    w.add_data("targets", [
        {"name": n, "A": A, "B_AME_MeV": str(B), "link": l,
         "volume": (None if v is None else str(v)), "usable": u}
        for n, A, B, l, v, u in TARGETS])
    w.add_data("exclusions", EXCLUSION)
    w.add_data("mirror_pair", {
        "B_ratio": str(r_B), "Vol_ratio": str(r_V),
        "ratio_of_ratios": str(ratio_of_ratios),
        "miss_percent": str(miss_pct)})
    w.add_data("implied_bondcount_constants",
               {n: str(c) for (n, *_), c in zip(usable, cs)})
    w.add_data("verdict", (
        "scope-(a). The four-point falsification the 2026-08-07 ledger set as "
        "its next task cannot be run: Reading 1 supplies zero hyperbolic points "
        "and Reading 2 supplies two. The blocker is the absence of an A=4 SDP "
        "binding link and the Vol=0 deuteron, not the pending "
        "Reading-1-vs-Reading-2 ruling. No claim is made for or against the "
        "volume law; the evidence base for it is unchanged and remains two "
        "points."))
    w.add_data("wired_to_production", False)
    w.add_data("fit_performed", False)
    w.add_caveat("Two of the four required points do not exist in the corpus. "
                 "This witness records that absence; it does not estimate the "
                 "missing volumes, and deliberately does NOT use the Vol_4 "
                 "~ 8.046 bond-count back-out as a fourth point (that would "
                 "assume the law under test).")
    path = w.save()
    print(f"\nwitness -> {path}")


if __name__ == "__main__":
    main()
