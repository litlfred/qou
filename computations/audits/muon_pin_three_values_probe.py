#!/usr/bin/env python3
"""Three different values are all called "the muon q0", spread over ~0.09 ppb.

Found while adding the `comparison` q0-anchor value (bean `qou-po7i`), by
stamping four deliberate cross-anchor probes with the muon value they ACTUALLY
computed with and letting the anchor audit check it. All four came back
Q0_FLIP. The stamp was not the defect -- the check worked, and it found this.

THE THREE VALUES
----------------
  A  canonical pin        computations/q-pinning-50-digit.witness.json, served
                          by qou_substrate.witness._q0_value_for_anchor("muon")
                          and by q_parameter under QOU_Q0_ANCHOR=ideal. FROZEN.
  B  committed in probe   the muon leg recorded inside the four cross-anchor
     witnesses            probe witnesses on main.
  C  q_muon_at() today    a LIVE derivation, q = 1/(1 - sqrt(Vol(4_1)/(m_mu/m_e)))
                          over MASS_RATIO_MU_E_STR (CODATA).

B is not a rounding of A and C is not a rounding of B. They diverge at the 13th
significant digit -- five orders of magnitude above the framework's own L1
compute target of 1 ppQ (1e-15), and inside the ~11.5 ppb muon-proton
separation that the whole two-pin vocabulary exists to keep straight.

WHAT A, B AND C ACTUALLY ARE (corrected 2026-08-21 by PR #5434)
----------------------------------------------------------------
B and C are the SAME derivation at two CODATA vintages. The lepton-tower
family derives q0 inline as hbar_q^2 = Vol(4_1)/(m_mu/m_e), q0 = 1/(1-hbar_q),
which inverts cleanly. Verified independently here (mpmath dps=60):

    Vol(4_1)/206.7682830  ->  1.10997859555418057528159407961   == B  (CODATA 2018)
    Vol(4_1)/206.7682827  ->  1.10997859564273904668179512938   == C  (CODATA 2022)

So C is not a second unexplained drift: it is B's derivation re-evaluated after
the CODATA table was updated (commit a4d9906659, which added
codata_2022_source.py). This CORRECTS the account below, which attributed B's
VALUE to the reverted change. The revert is plausibly how B got STAMPED into
the anchor field, but B's value is what that derivation returns under CODATA
2018 -- not an artifact.

A is the anomaly, and more sharply than "frozen". Inverting it the same way:

    invert A  ->  m_mu/m_e = 206.768282989315

which matches NEITHER published figure. It sits strictly BETWEEN them,
5.17e-11 relative from 2018 and 1.40e-9 from 2022. So A is not that derivation
at any CODATA vintage, and the tempting explanation -- "A is just the old
CODATA" -- is measurably false. A is not reproducible from a published muon
ratio at all.

HOW B GOT STAMPED (the original finding, still standing)
---------------------------------------------------------
B is verbatim the number recorded in `_q0_value_for_anchor`'s own docstring as
the WRONG side of a change that was made and then REVERTED on 2026-08-15:

    "measured 1.1099785955573347 computed vs 1.1099785955541805 stamped"

That revert restored the anchor SOURCE. It did not regenerate the witnesses
written while the derivation was live, so B survives on main inside every such
witness -- the revert is complete in the code and incomplete in the data.

C then moved again on top of that: q_muon_at() is a live derivation over a
CODATA input, so it drifts whenever that input is updated, while A is frozen.
Two of the three values are therefore MOVING TARGETS and one is not -- and
per the correction above, the two moving ones are the SAME derivation at
successive CODATA vintages, not two independent drifts.

WHY THIS BLOCKS THE `comparison` STAMP IT WAS FOUND BY
------------------------------------------------------
A producer that calls `q_muon_at()` is not computing at the canonical muon
anchor; it is computing at C. Stamping such a witness `q0Anchor: comparison`
with `q0Values.muon` = what it computed is HONEST and the audit correctly
reports Q0_FLIP -- which is CI-failing. So the four probes cannot be stamped
until it is ruled which of A and C a "muon-anchored" quantity should use.
Stamping the canonical constant instead would make the audit's per-leg check a
tautology and hide exactly this; that is the widen-the-checker move the
precision discipline forbids.

SCOPE
-----
Scope-(a), and this is a MEASUREMENT, not a ruling. It does not say which value
is correct, does not change any pin, and wires nothing. Deciding between A and C
is an owner/registry question (it touches what "ideal CAL-2 muon pin" means),
and regenerating the B-carrying witnesses is a separate migration.

Usage:
    python3 computations/audits/muon_pin_three_values_probe.py

Output:
    computations/audits/muon-pin-three-values.witness.json
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _pb  # noqa: E402

sys.path.insert(0, str(HERE.parents[1] / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder, _q0_value_for_anchor  # noqa: E402
from qou_substrate.constants import q_muon_at  # noqa: E402

_T0 = time.monotonic()

# Every comparison below is exact-decimal on 50-digit strings via mpmath at
# raised precision; no float64 anywhere.
mp.mp.dps = 80

#: The four witnesses whose muon leg carries value B.
_B_WITNESSES = [
    ("qbeta-h-frame-rungs.witness.json", "data/anchors[1]/q"),
    ("qbeta-c3-crossanchor-swing-provenance.witness.json", "(muon leg)"),
    ("qbeta-h-vs-u-frame-stability.witness.json", "(muon leg)"),
    ("qbeta-ladder-required-phase.witness.json", "(muon leg)"),
]


def _ppb(x, y) -> mp.mpf:
    """Relative separation in parts per billion, exact at the working dps."""
    return (mp.mpf(x) - mp.mpf(y)) / mp.mpf(y) * mp.mpf(10) ** 9


def _find_b() -> tuple[str, str] | tuple[None, None]:
    """Read value B out of the h-frame-rungs witness, whose muon leg is
    addressable without guessing at the other three layouts."""
    p = _pb.witness_path("qbeta-h-frame-rungs.witness.json",
                         prefer_dir=HERE.parent / "qbeta")
    if not p.exists():
        return None, None
    body = json.loads(p.read_text(encoding="utf-8"))
    for a in (body.get("data") or {}).get("anchors") or []:
        q = str(a.get("q") or "")
        if q.startswith("1.1099785955"):          # a muon-family value
            if not q.startswith(_q0_value_for_anchor("muon")[:14]):
                return q, str(p)
    return None, str(p)


def main() -> int:
    A = _q0_value_for_anchor("muon")
    C = mp.nstr(q_muon_at(60), 52, strip_zeros=False)
    B, bpath = _find_b()

    # CODATA reconstruction (PR #5434's refinement, verified here rather than
    # taken on trust). The lepton-tower family derives q0 inline as
    # hbar_q^2 = Vol(4_1)/(m_mu/m_e), q0 = 1/(1-hbar_q), so a published muon
    # ratio predicts a q0 forward, and a q0 inverts back to a ratio.
    VOL41 = 2 * mp.clsin(2, mp.pi / 3)      # 2*Cl_2(pi/3); NOT the 2*Lambda spelling
    R2018, R2022 = mp.mpf("206.7682830"), mp.mpf("206.7682827")

    def _q0_from_ratio(r):
        return 1 / (1 - mp.sqrt(VOL41 / r))

    def _ratio_from_q0(qs):
        q = mp.mpf(qs)
        return VOL41 / (1 - 1 / q) ** 2

    q_2018, q_2022 = _q0_from_ratio(R2018), _q0_from_ratio(R2022)
    ratio_A = _ratio_from_q0(A)

    print("=" * 74)
    print("Three values all called 'the muon q0'")
    print("=" * 74)
    print(f"  A canonical pin (q-pinning-50-digit) : {A[:30]}")
    print(f"  B committed in probe witnesses       : {(B or '<not found>')[:30]}")
    print(f"  C q_muon_at() live derivation        : {C[:30]}")
    print()

    assertions = []
    if B is None:
        assertions.append({
            "name": "0_value_B_located",
            "passed": False,
            "detail": f"could not locate value B in {bpath} — the witness layout "
                      "changed, or it has since been regenerated onto A",
        })
        all_passed = False
        pairs = {}
    else:
        ab, ac, bc = _ppb(B, A), _ppb(C, A), _ppb(C, B)
        pairs = {"B_minus_A_ppb": mp.nstr(ab, 8),
                 "C_minus_A_ppb": mp.nstr(ac, 8),
                 "C_minus_B_ppb": mp.nstr(bc, 8)}
        print(f"  B - A = {mp.nstr(ab, 8)} ppb")
        print(f"  C - A = {mp.nstr(ac, 8)} ppb")
        print(f"  C - B = {mp.nstr(bc, 8)} ppb")
        print()

        distinct = len({A[:14], B[:14], C[:14]})
        assertions += [
            {"name": "1_three_distinct_values",
             "passed": distinct == 3,
             "detail": f"{distinct} distinct values at the anchor audit's own "
                       "14-char discrimination width (_MATCH_PREFIX), which is "
                       "what it uses to tell muon from proton"},
            {"name": "2_separations_exceed_L1_target",
             "passed": bool(min(abs(ab), abs(ac), abs(bc)) > mp.mpf("1e-6")),
             "detail": "every pairwise separation exceeds the L1 compute target "
                       "of 1 ppQ = 1e-15 relative = 1e-6 ppb, so this is not "
                       "arithmetic noise"},
            {"name": "3_separations_below_mu_p_tension",
             "passed": bool(max(abs(ab), abs(ac), abs(bc)) < mp.mpf("11.5")),
             "detail": "all three sit INSIDE the ~11.5 ppb muon-proton gap, so "
                       "none of them is a mislabelled proton value — this is a "
                       "muon-vs-muon discrepancy, a class the anchor vocabulary "
                       "has no way to express",
             },
            {"name": "4_B_is_the_reverted_derivation_value",
             "passed": B.startswith("1.1099785955541805"),
             "detail": "B matches the number `_q0_value_for_anchor`'s docstring "
                       "records as the WRONG side of the 2026-08-15 revert "
                       "('1.1099785955541805 stamped'). The revert fixed the "
                       "code and left the data, so B survives on main.",
             },
            {"name": "5a_B_is_CODATA_2018",
             "passed": mp.nstr(q_2018, 28) == mp.nstr(mp.mpf(B), 28),
             "detail": f"Vol(4_1)/206.7682830 (CODATA 2018) reproduces B: "
                       f"{mp.nstr(q_2018, 28)}. So B's VALUE is not an artifact "
                       "of the revert — the revert is how it got stamped, not "
                       "what it is (PR #5434, verified here independently).",
             },
            {"name": "5b_C_is_CODATA_2022",
             "passed": mp.nstr(q_2022, 28) == mp.nstr(mp.mpf(C), 28),
             "detail": f"Vol(4_1)/206.7682827 (CODATA 2022) reproduces C: "
                       f"{mp.nstr(q_2022, 28)}. B and C are therefore the SAME "
                       "derivation at successive CODATA vintages, not two "
                       "independent drifts.",
             },
            {"name": "5c_A_matches_no_CODATA_vintage",
             "passed": bool(R2022 < ratio_A < R2018),
             "detail": f"inverting A gives m_mu/m_e = {mp.nstr(ratio_A, 16)}, "
                       "which matches NEITHER published figure and sits strictly "
                       "between them (5.17e-11 from 2018, 1.40e-9 from 2022). "
                       "So 'A is just the old CODATA' is measurably FALSE — A is "
                       "not reproducible from a published muon ratio at all.",
             },
            {"name": "5_C_is_not_B",
             "passed": C[:16] != B[:16],
             "detail": "q_muon_at() no longer returns what it returned when "
                       "these witnesses were written — it derives over a CODATA "
                       "input and drifts as that input updates, while A is "
                       "frozen. Two moving targets, one fixed.",
             },
        ]
        all_passed = all(a["passed"] for a in assertions)

    payload = {
        "computation_method": (
            "Reads A from qou_substrate.witness._q0_value_for_anchor('muon') "
            "(the committed q-pinning witness), C from "
            "qou_substrate.constants.q_muon_at(60) (the live derivation), and B "
            "from the committed muon leg of qbeta-h-frame-rungs. All "
            "separations are exact-decimal mpmath at dps=80; no float64."),
        "description": (
            "Three distinct values are all called 'the muon q0' and differ at "
            "the 13th significant digit: the frozen canonical pin, the value "
            "left inside four probe witnesses by a code change that was "
            "reverted without regenerating them, and today's live q_muon_at() "
            "derivation, which has drifted again since. All three sit inside "
            "the 11.5 ppb muon-proton gap, so this is a muon-vs-muon "
            "discrepancy the anchor vocabulary cannot currently express."),
        "audit_only": True,
        "tier": "empirical",
        "q0Anchor": "muon",
        "q0Value": A,
        "q0AnchorReason": (
            "Muon-layer throughout: every value compared is a muon q0 and the "
            "canonical muon pin is the reference. No proton quantity is read, "
            "so this is not a cross-anchor comparison and not a layer straddle."),
        "scope": (
            "scope-(a) MEASUREMENT, not a ruling. Does not say which value is "
            "correct, changes no pin, wires nothing. Choosing between A and C "
            "is an owner/registry question about what the ideal CAL-2 muon pin "
            "means; regenerating the B-carrying witnesses is a separate "
            "migration."),
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "A_canonical_pin": A,
            "B_committed_in_probe_witnesses": B,
            "C_q_muon_at_live": C,
            "separations": pairs,
            "codata_reconstruction": {
                "vol_4_1": mp.nstr(VOL41, 25),
                "q0_from_CODATA_2018": mp.nstr(q_2018, 30),
                "q0_from_CODATA_2022": mp.nstr(q_2022, 30),
                "m_mu_over_m_e_implied_by_A": mp.nstr(ratio_A, 16),
                "note": ("B = CODATA 2018, C = CODATA 2022 — the same inline "
                         "derivation q0 = 1/(1-sqrt(Vol(4_1)/(m_mu/m_e))) at two "
                         "vintages, with commit a4d9906659 (codata_2022_source.py) "
                         "the step between. A matches no vintage."),
            },
            "B_carrying_witnesses": [w for w, _ in _B_WITNESSES],
            "verdict": (
                "Three values, two of them moving. The 2026-08-15 revert of the "
                "derive-the-muon-branch change was complete in the code and "
                "incomplete in the data, and q_muon_at() has drifted again on "
                "top of that. Until it is ruled which of A and C a "
                "'muon-anchored' quantity should use, a producer that calls "
                "q_muon_at() cannot be honestly stamped against the canonical "
                "pin -- the audit correctly reports Q0_FLIP, and stamping the "
                "constant instead would make its per-leg check a tautology."),
        },
        "context": {
            "found_by": "adding the `comparison` q0 anchor value (bean qou-po7i)",
            "beans": ["qou-po7i"],
            "reverted_change": (
                "see the REVERTED note in "
                "qou_substrate.witness._q0_value_for_anchor -- it names value B"),
            "blocks": (
                "stamping qbeta_c3_crossanchor_swing_provenance_probe, "
                "qbeta_h_frame_rungs_probe, qbeta_h_vs_u_frame_stability_probe "
                "and qbeta_ladder_required_phase_probe as `comparison`"),
        },
    }

    b = WitnessBuilder.wrap_legacy(
        "muon-pin-three-values", payload,
        script_path=__file__, engine="mpmath",
        engine_version=mp.__version__, output_dir=HERE, start_time=_T0)
    out = b.save()
    print(f"witness -> {out}")
    print(f"allPassed: {all_passed}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
