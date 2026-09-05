#!/usr/bin/env python3
"""
Owner redirect 2026-08-15: is the c_3 refutation evidence chain still valid
after the compute-convention changes that landed since its probes ran?

The change under audit is the Markov-trace convention flip C -> D
(owner ruling 2026-08-09, trace-convention-registry.json):

    C (full-Hecke Ocneanu/Wenzl):   z = sqrt(q)/(1+q)
    D (SU(2)/Temperley-Lieb Jones): z = q^3/(q^2+1)     (+22.7% at q0)

The Q_beta c_3 extractor consumes z through the N=1 rung phase:

    alpha = (z - 1) * h / 2                    qbeta_utils.py:124-125
    Q_N1  = Q_A * cos(alpha - b*hbar^2/2)
    c_3   = (Q_beta^exp / Q_N2 - 1) / u^3

and the SAME z_C sits in the exact D-ladder core
(qbeta_ck_sseries_exact_rational.py:20,248) and in the Lean parity certificate
ZBarParity.lean (zNum/zDen with s = sqrt(q), i.e. z = sqrt(q)/(1+q)).
The trace-convention registry has channels mass / binding /
borromean-binding-single-pipeline only — THE Q_BETA CHANNEL IS NOT REGISTERED —
so this dependence was invisible to the convention audit that excised C.

WHAT THIS PROBE MEASURES (all at 60 dps, both anchors, both conventions):

  1. Regression: the C-frame extraction reproduces the committed corpus
     values c_3(proton) = -2.06934258, c_3(muon) = -2.01986031 (the muon
     target is anchor-qualified: CODATA 2022, per fca08de7d2 and qou-t39x).
  2. Exact bar parity of the two z's (sympy, exact zero):
     bar(z_C) = z_C  but  bar(z_D) = q^-4 * z_D — convention D's trace
     parameter is NOT bar-invariant; KC13's "z exactly bar-even" is a
     convention-C statement.
  3. Both conventions coincide at q = 1 (z = 1/2), so q->1 shadow gates
     (c_2 -> -1, c_3 -> -2, KC10) are convention-immune at the classical point.
  4. Re-extraction under D: c_3 moves by ~972 (to ~ -974). Every value-level
     ~ -2 near-match — (H1) c_3^even = -Vol(4_1), [3]_q/25 (2.65 ppm),
     J - hbar^2, the S_leak = c_3 + Vol(4_1) program, q*_S — is therefore
     CONDITIONAL ON CONVENTION C.
  5. The anchor-swing mechanism is convention-IMMUNE: swing_D/swing_C = 1.005.
     The "REFUTED as real-q fibre element" verdict (cross-anchor rigidity,
     dc_3/dq ~ 4.6e6, the capstone's 1/u^3 result) rests on the swing, whose
     dominant source (Q_A(q) sensitivity over u^3) is z-free. The refutation
     SURVIVES the convention change under both conventions.
  6. The ladder's rung-by-rung convergence exists in the C frame only:
     N2/N1 residual improvement 58x under C vs 1.12x under D, and the implied
     empirical c_2 = (Q/Q_N1 - 1)/u^2 is ~ -1.02 under C (the proved -1 plus
     the c_3*u term) vs ~ -9.3 under D. So the canonical rung c_2 = -1
     (Lean-proved Taylor-exact) is ALSO a statement about the C-frame ladder
     object. The C->D excision does NOT mechanically transfer to Q_beta:
     transferring it demands a re-derivation of the ladder, not a z swap.

SCOPE — scope-(a) throughout. This probe adjudicates NO convention for the
Q_beta channel; it does not show C is right (C was excised from mass/binding
by a forcing argument) nor that D applies to the beta channel (the two-row
cap argument has not been examined for the decay channel — open item, new
bean). Nothing is wired; no c_k value changes; no tier changes. The output is
provenance: which pillars of the c_3 record are convention-immune and which
are C-conditional.
"""

import datetime
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

from qbeta_utils import c3_target_at, substrate_ladder_quantities  # noqa: E402
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 60

ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
with mp.workdps(60):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))

# Committed corpus values for the C-frame extraction (registry section 9f
# window endpoints; qbeta-c3-barodd-sleak.witness.json).
#
# THE MUON TARGET IS ANCHOR-QUALIFIED, AND THAT IS NOT DECORATION (qou-t39x).
# There is no single "muon c_3": the extractor returns a different value at each
# muon pin in use, and they differ in the FOURTH significant figure --
#
#     frozen pin       (...5557...)   -2.02018813
#     CODATA-2018      (...5554...)   -2.02020024   <- what this probe targeted
#     CODATA-2022      (...5642...)   -2.01986031   <- what q_muon_at() returns
#
# This probe calls `q_muon_at()`, which `fca08de7d2` (2026-08-22, owner ruling)
# moved to CODATA 2022. The target below stayed on CODATA 2018, so from that
# commit the assertion compared a 2022 computation against a 2018 literal and
# failed by 3.4e-4 -- read in `qou-cds1` as "a third value" of unknown origin.
# It was neither a third value nor a defect in the extractor: attribution is
# 99.9985 % the edition step 206.7682830 -> 206.7682827, with the 5.0e-9
# residual being this literal's own rounding to the 9 figures it quotes
# (probe: qbeta_c3_muon_anchor_codata_edition_attribution).
#
# The superseded value is KEPT, named, and asserted-against below, so a silent
# slide back onto the 2018 anchor is caught rather than re-diagnosed.
#
# SCALE, so the 1e-6 below is not misread: it is a REPRODUCIBILITY tolerance,
# not a physics one. Propagated through the CAL-1/2/3 published uncertainties
# this target is -2.0199 +- 1.26 (Q_beta-dominated, via 1/u^3 = 1.6e6) -- 0.2
# supported significant figures against the 9 quoted. What is experimentally
# resolved here is the cross-anchor SWING (9.5 sigma), not either absolute.
CORPUS_C3_PROTON = mp.mpf("-2.06934258")
CORPUS_C3_MUON = mp.mpf("-2.01986031")            # muon pin @ CODATA 2022
CORPUS_C3_MUON_CODATA2018 = mp.mpf("-2.02020024")  # SUPERSEDED — do not target


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def z_of(q: mp.mpf, conv: str) -> mp.mpf:
    """The Markov parameter under trace convention C or D
    (docs/coordination/trace-convention-registry.json)."""
    if conv == "C":
        return mp.sqrt(q) / (1 + q)
    return q ** 3 / (q ** 2 + 1)


def ladder(q: mp.mpf, conv: str) -> dict:
    """The Q_beta precision ladder with the N=1 phase built on z(conv).

    Mirrors qbeta_utils.substrate_ladder_quantities + c3_target_at exactly,
    except that z is parameterised by convention. conv="C" MUST reproduce
    qbeta_utils (assertion 1 checks this via the public API too).
    """
    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2
    z = z_of(q, conv)
    alpha = (z - 1) * h / 2
    q_a = ME * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    q_n1 = q_a * mp.cos(alpha - b * hbar ** 2 / 2)
    q_n2 = q_n1 * (1 - u ** 2)
    return {
        "z": z, "alpha": alpha, "u": u,
        "Q_N1": q_n1, "Q_N2": q_n2,
        "n1_res": QCOD / q_n1 - 1,
        "n2_res": QCOD / q_n2 - 1,
        "c2_implied": (QCOD / q_n1 - 1) / u ** 2,
        "c3": (QCOD / q_n2 - 1) / u ** 3,
    }


def main() -> int:
    t0 = time.monotonic()
    q_p = mp.mpf(str(q_at()))
    q_m = mp.mpf(str(q_muon_at()))

    print("=" * 78)
    print(" c_3 refutation chain vs the C->D trace-convention flip (owner redirect)")
    print("=" * 78)

    # ---- exact bar-parity facts (sympy) --------------------------------
    qs = sp.Symbol("q", positive=True)
    zC_sym = sp.sqrt(qs) / (1 + qs)
    zD_sym = qs ** 3 / (qs ** 2 + 1)
    zC_bar_diff = sp.simplify(zC_sym.subs(qs, 1 / qs) - zC_sym)
    zD_twist_diff = sp.simplify(zD_sym.subs(qs, 1 / qs) - zD_sym / qs ** 4)
    zD_bar_diff = sp.simplify(zD_sym.subs(qs, 1 / qs) - zD_sym)
    zC_at1 = sp.simplify(zC_sym.subs(qs, 1))
    zD_at1 = sp.simplify(zD_sym.subs(qs, 1))
    print("\n  exact (sympy):")
    print(f"    bar(z_C) - z_C            = {zC_bar_diff}   (z_C bar-EVEN)")
    print(f"    bar(z_D) - q^-4 z_D       = {zD_twist_diff}   (z_D bar-twist q^-4)")
    print(f"    bar(z_D) - z_D            = {zD_bar_diff}   (NOT bar-invariant)")
    print(f"    z_C(1) = {zC_at1},  z_D(1) = {zD_at1}   (conventions coincide at q=1)")

    # ---- the four ladder runs ------------------------------------------
    runs = {}
    for conv in ("C", "D"):
        for name, q in (("proton", q_p), ("muon", q_m)):
            runs[(conv, name)] = ladder(q, conv)
    # public-API cross-check for the C frame
    c3_api_p = c3_target_at(q_p, QCOD, ME)
    c3_api_m = c3_target_at(q_m, QCOD, ME)

    print("\n  conv anchor   z              c_3                N1 residual   N2 residual")
    for (conv, name), r in runs.items():
        print(f"   {conv}   {name:7s} {mp.nstr(r['z'], 10):14s} "
              f"{mp.nstr(r['c3'], 12):18s} {mp.nstr(r['n1_res'], 5):13s} "
              f"{mp.nstr(r['n2_res'], 5)}")

    swing_c = runs[("C", "muon")]["c3"] - runs[("C", "proton")]["c3"]
    swing_d = runs[("D", "muon")]["c3"] - runs[("D", "proton")]["c3"]
    swing_ratio = swing_d / swing_c
    shift_p = runs[("D", "proton")]["c3"] - runs[("C", "proton")]["c3"]
    shift_m = runs[("D", "muon")]["c3"] - runs[("C", "muon")]["c3"]
    h1_dist_D_p = abs(runs[("D", "proton")]["c3"] + VOL41)
    h1_dist_D_m = abs(runs[("D", "muon")]["c3"] + VOL41)
    conv_ratio_C = runs[("C", "proton")]["n2_res"] / runs[("C", "proton")]["n1_res"]
    conv_ratio_D = runs[("D", "proton")]["n2_res"] / runs[("D", "proton")]["n1_res"]

    print(f"\n  swing  C: {mp.nstr(swing_c, 10)}   D: {mp.nstr(swing_d, 10)}"
          f"   ratio D/C = {mp.nstr(swing_ratio, 8)}")
    print(f"  extraction shift D - C: proton {mp.nstr(shift_p, 8)}, "
          f"muon {mp.nstr(shift_m, 8)}")
    print(f"  |c_3_D + Vol(4_1)|: proton {mp.nstr(h1_dist_D_p, 8)}, "
          f"muon {mp.nstr(h1_dist_D_m, 8)}   (C frame: 0.0395 / 0.0097)")
    print(f"  implied c_2: C {mp.nstr(runs[('C', 'proton')]['c2_implied'], 8)}"
          f"   D {mp.nstr(runs[('D', 'proton')]['c2_implied'], 8)}   (proved: -1, C frame)")
    print(f"  N2/N1 residual ratio: C {mp.nstr(conv_ratio_C, 6)} (58x improvement)"
          f"   D {mp.nstr(conv_ratio_D, 6)} (no rung convergence)")

    assertions = [
        {"name": "C_frame_regression_matches_committed_corpus_values",
         "passed": bool(abs(runs[("C", "proton")]["c3"] - CORPUS_C3_PROTON) < mp.mpf("1e-6")
                        and abs(runs[("C", "muon")]["c3"] - CORPUS_C3_MUON) < mp.mpf("1e-6")
                        and abs(runs[("C", "proton")]["c3"] - c3_api_p) < mp.mpf("1e-40")
                        and abs(runs[("C", "muon")]["c3"] - c3_api_m) < mp.mpf("1e-40")),
         "detail": "probe's C ladder == qbeta_utils.c3_target_at == registry values "
                   "(muon target anchor-qualified: CODATA 2022)"},
        {"name": "muon_anchor_has_not_slid_back_to_codata_2018",
         "passed": bool(abs(runs[("C", "muon")]["c3"] - CORPUS_C3_MUON_CODATA2018)
                        > mp.mpf("1e-4")),
         "detail": f"distance from the SUPERSEDED 2018 target = "
                   f"{mp.nstr(abs(runs[('C', 'muon')]['c3'] - CORPUS_C3_MUON_CODATA2018), 6)}"
                   " — guards the straddle that produced qou-cds1 Finding B"},
        {"name": "zC_bar_even_exact",
         "passed": bool(zC_bar_diff == 0)},
        {"name": "zD_bar_twist_is_q_minus_4_exact_and_not_invariant",
         "passed": bool(zD_twist_diff == 0 and zD_bar_diff != 0),
         "detail": "bar(z_D) = q^-4 z_D exactly; KC13's bar-even z is z_C only"},
        {"name": "conventions_coincide_at_q1_shadow_immune",
         "passed": bool(zC_at1 == sp.Rational(1, 2) and zD_at1 == sp.Rational(1, 2))},
        {"name": "D_reextraction_shifts_c3_by_more_than_100",
         "passed": bool(abs(shift_p) > 100 and abs(shift_m) > 100),
         "detail": f"shift ~ {mp.nstr(shift_p, 6)} — all ~ -2 near-matches are C-conditional"},
        {"name": "h1_volume_proximity_does_not_survive_D_reextraction",
         "passed": bool(h1_dist_D_p > 100 and h1_dist_D_m > 100),
         "detail": "|c_3_D + Vol(4_1)| ~ 972 vs C-frame 0.0097-0.0395"},
        {"name": "anchor_swing_mechanism_convention_immune",
         "passed": bool(mp.mpf("0.5") < swing_ratio < mp.mpf("2")),
         "detail": f"swing_D/swing_C = {mp.nstr(swing_ratio, 8)} — the REFUTED-as-real-q "
                   "pillar (cross-anchor rigidity / 1/u^3) stands under BOTH conventions"},
        {"name": "implied_c2_is_minus1_in_C_frame_only",
         "passed": bool(abs(runs[("C", "proton")]["c2_implied"] + 1) < mp.mpf("0.05")
                        and abs(runs[("D", "proton")]["c2_implied"] + 1) > 1),
         "detail": "c_2 = -1 (proved) is a C-frame ladder statement; D implies ~ -9.3"},
        {"name": "ladder_rung_convergence_C_frame_only",
         "passed": bool(abs(conv_ratio_C) < mp.mpf("0.05")
                        and abs(conv_ratio_D) > mp.mpf("0.5")),
         "detail": "N2 improves N1 58x under C, 1.12x under D — the ladder is C-built"},
    ]
    all_passed = all(a["passed"] for a in assertions)

    print("\n" + "=" * 78)
    print(" ASSERTIONS")
    print("=" * 78)
    for a in assertions:
        print(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
    print(f"\n  allPassed: {all_passed}")

    with open(os.path.abspath(__file__), "rb") as f:
        src = f.read()

    witness = {
        "computation": "qbeta-c3-ladder-trace-convention-sensitivity",
        "description": (
            "Validity audit of the c_3 refutation chain against the 2026-08-09 "
            "C->D Markov-trace convention flip. The Q_beta N=1 rung consumes "
            "z through alpha=(z-1)h/2 (qbeta_utils.py:124-125); the Q_beta "
            "channel is NOT registered in trace-convention-registry.json. "
            "Measured: the C-frame extraction reproduces the committed c_3 "
            "values; re-extracting with z_D shifts c_3 by ~972 (to ~ -974), so "
            "every ~ -2 value-level near-match ((H1) -Vol(4_1), [3]_q/25, "
            "J-hbar^2, S_leak, q*_S) is conditional on convention C; the "
            "anchor swing is convention-immune (ratio 1.005), so the REFUTED-"
            "as-real-q verdict SURVIVES; bar(z_D) = q^-4 z_D exactly, so "
            "KC13's bar-even z is convention-C-scoped; the implied c_2 under D "
            "is ~ -9.3 and the rung convergence disappears, so c_2 = -1 "
            "(Taylor-exact) is likewise a C-frame statement and the C->D "
            "excision does not mechanically transfer to the Q_beta channel. "
            "Scope-(a): adjudicates no convention; wires nothing."),
        "audit_only": True,
        "tier": "convention-provenance audit (exact symbolic + 60-dps measurement; no fit)",
        "q0Anchor": "proton",
        "q0Value": mp.nstr(q_p, 25),
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath+sympy",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "z_at_q0": {"C": mp.nstr(runs[("C", "proton")]["z"], 20),
                        "D": mp.nstr(runs[("D", "proton")]["z"], 20)},
            "c3": {conv + "_" + name: mp.nstr(runs[(conv, name)]["c3"], 16)
                   for conv in ("C", "D") for name in ("proton", "muon")},
            "n1_residual": {conv: mp.nstr(runs[(conv, "proton")]["n1_res"], 8)
                            for conv in ("C", "D")},
            "n2_residual": {conv: mp.nstr(runs[(conv, "proton")]["n2_res"], 8)
                            for conv in ("C", "D")},
            "c2_implied": {conv: mp.nstr(runs[(conv, "proton")]["c2_implied"], 10)
                           for conv in ("C", "D")},
            "swing": {"C": mp.nstr(swing_c, 12), "D": mp.nstr(swing_d, 12),
                      "ratio_D_over_C": mp.nstr(swing_ratio, 12)},
            "extraction_shift_D_minus_C": {"proton": mp.nstr(shift_p, 12),
                                           "muon": mp.nstr(shift_m, 12)},
            "h1_distance_under_D": {"proton": mp.nstr(h1_dist_D_p, 12),
                                    "muon": mp.nstr(h1_dist_D_m, 12)},
            "vol_4_1": mp.nstr(VOL41, 16),
            "bar_parity_exact": {
                "zC_bar_minus_zC": str(zC_bar_diff),
                "zD_bar_minus_qminus4_zD": str(zD_twist_diff),
                "zD_bar_minus_zD_simplified": str(zD_bar_diff),
            },
        },
        "context": {
            "axis": "c_3 refutation-chain validity vs post-probe convention changes",
            "convention_sites": [
                "computations/qbeta/qbeta_utils.py:124-125 (z_C in alpha; the extractor)",
                "computations/qbeta/qbeta_ck_sseries_exact_rational.py:20,248 "
                "(z_C in the KC21/KC22 D-ladder core)",
                "content/quantum-observable-universe/lean/QOU/QBeta/ZBarParity.lean:59-79 "
                "(KC13 bar-even z is z_C = s/(1+s^2), s = sqrt(q))",
                "docs/coordination/trace-convention-registry.json (channels: mass, "
                "binding, borromean only — Q_beta channel MISSING)",
            ],
            "convention_immune_pillars": [
                "cross-anchor swing / dc_3/dq ~ 4.6e6 / capstone 1/u^3 (measured: "
                "swing ratio D/C = 1.005)",
                "P4 entropy bound (sigma(c_3) = sigma(Q_beta)/(Q_N2 u^3); Q_N2 moves "
                "6e-4 relative under D)",
                "q->1 shadows (z_C(1) = z_D(1) = 1/2, exact)",
                "KC20 zeta_4/cubic certificate (Delta_net numerator is z-free: even "
                "powers of q only)",
            ],
            "scope": (
                "Scope-(a). No convention is adjudicated for the Q_beta channel; "
                "C's excision from mass/binding (owner 2026-08-09) is untouched; "
                "whether the two-row forcing transfers to the decay channel is an "
                "OPEN item (new bean). No c_k wired; no tier change."),
        },
        # int ms, not float sec: a float64 duration is the one raw-float64
        # ratchet hit this witness had (NO-FLOAT64 discipline; WitnessBuilder
        # convention is integer durationMs, masked as ephemeral meta).
        "durationMs": int((time.monotonic() - t0) * 1000),
    }

    out = HERE / "qbeta-c3-ladder-trace-convention-sensitivity.witness.json"
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, f, indent=2)
        f.write("\n")
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"\n  witness -> {out.relative_to(ROOT)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
