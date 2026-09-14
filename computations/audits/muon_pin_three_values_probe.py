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
import re
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
# WAS a hardcoded list of four witnesses "carrying B". It had gone stale: on
# 2026-09-14 `qbeta-h-frame-rungs.witness.json` held only proton and C, having
# been regenerated, so the first entry was simply wrong and the probe could not
# say so. A transcribed inventory of a MIGRATING population is a snapshot that
# ages into a lie — the same defect this file documents elsewhere.
#
# Counted live instead. `_survival_census` walks the committed witnesses and
# reports how many q0-bearing fields still carry each of A, B and C, which is
# the question the inventory was a proxy for and stays true as the migration
# moves.
# Deliberately a STRICT SUPERSET of `q0_value_drift_audit`'s field regex: that
# gate's `^(q_?0|q_?0_\d+dps|q0Value|q_zero|substrate_q)$` plus the bare `q`,
# which several anchor legs use (`data.anchors[].q`). The two scans therefore
# do NOT report the same totals, and that is intended rather than a bug —
# decomposed 2026-09-14 so nobody "reconciles" them later by narrowing one:
#
#   in this census only  89   bare `q` 54, `q_0` 22, … and 36 of them live
#                             OUTSIDE computations/, which that gate does not
#                             scan at all
#   in that gate only    45   all `q_0_50dps` / `q0_50dps`, the spellings this
#                             set was missing before this change
#
# After it, every field that gate sees is also seen here — VERIFIED, not
# asserted: 284 gate entries, 375 census entries, and the gate-only set is
# EMPTY. The residual gap is scan ROOT and the bare `q`, both of which a
# survival census should have and a drift ratchet reasonably does not.
_Q0_KEY_RE = re.compile(r"^(q|q_?0|q_?0_\d+dps|q0Value|q_zero|substrate_q)$", re.I)


def _survival_census() -> dict:
    """-> {"A": n, "B": n, "C": n, "files": {...}} over committed witnesses.

    Matched on a 16-character prefix: A and B diverge at the 13th significant
    digit, so 16 is comfortably past their separation and still short enough
    to match a truncated copy.
    """
    import subprocess  # noqa: PLC0415 -- only needed on this path
    root = HERE.parent.parent
    out = subprocess.run(["git", "ls-files", "*.witness.json"], cwd=root,
                         capture_output=True, text=True).stdout.split()
    pref = {k: mp.nstr(v, 17)[:16] for k, v in _DEFINED_PINS().items()}
    counts = {k: 0 for k in pref}
    files: dict[str, set] = {k: set() for k in pref}

    def walk(o, f):
        if isinstance(o, dict):
            for k, v in o.items():
                if _Q0_KEY_RE.match(k) and isinstance(v, (str, float, int)):
                    t = str(v)
                    for name, q in pref.items():
                        if t.startswith(q):
                            counts[name] += 1
                            files[name].add(f)
                else:
                    walk(v, f)
        elif isinstance(o, list):
            for v in o:
                walk(v, f)

    for rel in out:
        try:
            walk(json.loads((root / rel).read_text(encoding="utf-8")), rel)
        except Exception:                                   # noqa: BLE001
            continue
    return {"counts": counts,
            "files": {k: sorted(v) for k, v in files.items()}}


def _ppb(x, y) -> mp.mpf:
    """Relative separation in parts per billion, exact at the working dps."""
    return (mp.mpf(x) - mp.mpf(y)) / mp.mpf(y) * mp.mpf(10) ** 9


def _DEFINED_PINS() -> dict:
    """A, B and C from their ESTABLISHED definitions, not by discovery.

    The probe used to resolve A live and hunt B in one witness. Both bindings
    broke, in opposite ways, and neither failure was visible as itself:

      * `A = _q0_value_for_anchor("muon")` returned A when it was written.
        Since bean `qou-tekx` stage 3b that resolver DERIVES from
        `q_muon_at()`, so it now returns **C** — measured 2026-09-14,
        relative difference from C exactly 0. The probe that defines the A/B/C
        vocabulary was labelling C as A.
      * `_find_b` filtered on the prefix `1.1099785955` (the A/B family) and
        excluded anything matching the resolver's first 14 chars. Once the
        resolver moved to C that exclusion stopped excluding anything in the
        family, so the first A-or-B value found would have been returned as B.

    So the values are defined here. B and C are DERIVED — they are the same
    lepton-tower inversion at two CODATA vintages. A is a literal because A is
    not derivable from any published muon ratio, which is this probe's own
    finding (assertion `5c`) and the reason it is safe to freeze: a value
    nobody can recompute cannot drift.
    """
    vol = 2 * mp.clsin(2, mp.pi / 3)
    q0 = lambda r: 1 / (1 - mp.sqrt(vol / mp.mpf(r)))     # noqa: E731
    return {"A": mp.mpf("1.1099785955573347"),
            "B": q0("206.7682830"),                        # CODATA 2018
            "C": q0("206.7682827")}                        # CODATA 2022


def main() -> int:
    _pins = _DEFINED_PINS()
    A = mp.nstr(_pins["A"], 52, strip_zeros=False)
    B = mp.nstr(_pins["B"], 52, strip_zeros=False)
    C = mp.nstr(_pins["C"], 52, strip_zeros=False)

    # What the two live doors answer TODAY. Both used to return A; both now
    # return C, and that is the migration landing rather than a defect — but
    # it has to be ASSERTED, because this probe silently mislabelled C as A
    # for as long as it took the binding to go unchecked.
    live_resolver = _q0_value_for_anchor("muon")
    live_derivation = mp.nstr(q_muon_at(60), 52, strip_zeros=False)
    census = _survival_census()

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
    _same = lambda x, y: mp.nstr(mp.mpf(x), 24) == mp.nstr(mp.mpf(y), 24)  # noqa: E731

    print("=" * 74)
    print("Three values all called 'the muon q0'")
    print("=" * 74)
    print(f"  A frozen anomaly (no CODATA vintage) : {A[:30]}")
    print(f"  B Vol(4_1)/206.7682830  CODATA 2018  : {B[:30]}")
    print(f"  C Vol(4_1)/206.7682827  CODATA 2022  : {C[:30]}")
    print(f"  live _q0_value_for_anchor('muon')    : {live_resolver[:30]}")
    print(f"  live q_muon_at(60)                   : {live_derivation[:30]}")
    print()
    print(f"  still carried in committed witnesses : "
          f"A {census['counts']['A']}   B {census['counts']['B']}   "
          f"C {census['counts']['C']}")
    print()

    assertions = []
    if True:
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
            # 5a/5b USED to compare a discovered B and a live-resolved C
            # against the two CODATA reconstructions. Both are now DEFINED by
            # those reconstructions, so that comparison is a tautology and
            # would pass however wrong the rest got. What is not a tautology,
            # and is what actually moved, is where the two live doors point.
            {"name": "5a_live_resolver_returns_C_not_A",
             "passed": _same(live_resolver, C) and not _same(live_resolver, A),
             "detail": "_q0_value_for_anchor('muon') derives from q_muon_at() "
                       "since bean qou-tekx stage 3b, so it returns C. This "
                       "probe bound its `A` to that call and therefore labelled "
                       "C as A until 2026-09-14; the binding is now a literal "
                       "and this assertion is what would catch the drift again.",
             },
            {"name": "5b_live_derivation_agrees_with_the_resolver",
             "passed": _same(live_derivation, live_resolver),
             "detail": "q_muon_at(60) and _q0_value_for_anchor('muon') are the "
                       "two doors onto 'the muon pin'. bean qou-2361 recorded "
                       "them DISAGREEING (code on C, anchor witness on A); they "
                       "now agree, so that split is closed on the read path.",
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
            "A, B and C are DEFINED, not discovered: B and C from the "
            "lepton-tower inversion q0 = 1/(1-sqrt(Vol(4_1)/(m_mu/m_e))) at "
            "CODATA 2018 and 2022, A as the literal it has to be because no "
            "published ratio reproduces it (assertion 5c). The two live doors "
            "— _q0_value_for_anchor('muon') and q_muon_at(60) — are then "
            "CHECKED against C rather than used as sources, which is the "
            "binding that silently broke. Survival counts are a live walk of "
            "the committed witnesses, replacing a hardcoded four-file "
            "inventory that had gone stale. Exact-decimal mpmath; no float64."),
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
            "survival_census": census["counts"],
            "survival_files": {k: v[:20] for k, v in census["files"].items()},
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
