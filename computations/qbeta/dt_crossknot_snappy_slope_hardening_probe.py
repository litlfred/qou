#!/usr/bin/env python3
"""dt_crossknot_snappy_slope_hardening_probe.py — D3: SnapPy-harden the
cross-knot boundary-slope data (qou-btvl / qou-52sn).

The Route-A cross-knot gate (RouteANewtonPolygonDT.lean, audit
2026-08-11-aomega-internal-derivation-attack-options.md) rests on
LITERATURE-recalled boundary-slope data: 4₁ slopes ±4, 5₂ slopes
{0, −4, −10} (Hatcher–Oertel), with the R2 refutation using
max|slope|(5₂) = 10 ∉ DT {3,4}. SnapPy was unavailable when that landed
(bean qou-52sn). This probe recomputes the slopes with SnapPy 3.3.2's
`normal_boundary_slopes()` (spun-normal surface theory, FXrays exact
rational arithmetic — integer output, no float tier) and:

  [1] HARDENS 4₁: detected slopes = {±4}, matching the Lean
      `a41_edge_slopes_pm_four` / `a41MaxAbsSlope = 4`.
  [2] HARDENS 5₂: detected |slopes| = {0, 4, 10}, max = 10 — the R2
      refutation's load-bearing datum confirmed by computation.
      CONVENTION NOTE: SnapPy returns (4,1),(10,1) where Hatcher–Oertel
      write −4, −10; the sign is the meridian/longitude orientation
      convention, the MAGNITUDE set is convention-independent and is
      what the refutation uses. Recorded as-is, not "corrected".
  [3] NEW DATA 6₁: detected slopes (0,1), (4,−1), (8,1) →
      |slopes| = {0, 4, 8}, max = 8. This is the D3 cross-knot
      extension datum. NO DT spectrum for 6₁ exists in the corpus or
      the GGM literature tables we carry (4₁/5₂ only), so no R1/R2
      comparison is made — the slopes are banked for when 6₁ DT
      integers become available. Nothing is inferred from them here.
  [4] Volume cross-checks (SnapPy float64 tier, informational): each
      manifold volume vs the corpus values (Vol(4₁) = 2.0298832…,
      Vol(5₂) = 2.8281220…, Vol(6₁) = 3.1639632…).

Spun-normal caveat (honest scope): `normal_boundary_slopes()` detects
slopes of spun-normal surfaces; for these small census knots the
detected sets coincide with the known full boundary-slope sets
(Hatcher–Oertel for 2-bridge knots), which is exactly the cross-check
wanted. The probe asserts the detected sets, not completeness.

Scope-(a) throughout; nothing wired; verdicts reported not asserted
beyond the two hardening assertions. Beans qou-btvl (D3) / qou-52sn.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402

set_compute_dps()

# Corpus volumes (50-digit corpus constants truncated to float64-safe
# comparison width; the SnapPy side is float64, so 1e-9 is the honest
# comparison tolerance — this is a cross-check, not a precision claim).
VOL_CORPUS = {
    "4_1": mp.mpf("2.029883212819307250042405108549040391679005894"),
    "5_2": mp.mpf("2.828122088330783162763898809276634942770981317"),
    "6_1": mp.mpf("3.163963228883143983991757529167384812325703962"),
}
# Literature-recalled slope data being hardened (magnitude sets).
LIT_ABS = {"4_1": {4}, "5_2": {0, 4, 10}, "6_1": None}  # 6_1: new data


def main() -> int:
    import snappy

    print("=" * 78)
    print(" D3 — SnapPy hardening of the cross-knot boundary-slope data")
    print("=" * 78)

    wb = WitnessBuilder("dt-crossknot-snappy-slope-hardening", engine="snappy")
    wb.set_description(
        "D3 (qou-btvl) + qou-52sn: recompute the Route-A cross-knot "
        "boundary slopes with SnapPy 3.3.2 normal_boundary_slopes() "
        "(spun-normal, FXrays exact integer output). Hardens the "
        "literature-recalled 4_1 {+-4} and 5_2 {0,-4,-10} (magnitude "
        "sets convention-independent; SnapPy sign convention differs "
        "from Hatcher-Oertel and is recorded as-is). New 6_1 datum "
        "|slopes| = {0,4,8}; no 6_1 DT spectrum exists in corpus or "
        "carried literature, so no R1/R2 comparison is made. Volume "
        "cross-checks are float64-tier informational. Scope-(a); "
        "nothing wired. Beans qou-btvl / qou-52sn."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    results = {}
    for name in ("4_1", "5_2", "6_1"):
        M = snappy.Manifold(name)
        slopes = M.normal_boundary_slopes()
        abs_slopes = sorted({abs(m_) if l_ in (1, -1) else None
                             for (m_, l_) in slopes} - {None})
        # slope p/q with q = +-1 for all these census knots -> |slope| = |m|
        vol = mp.mpf(repr(M.volume()))
        vol_err = mp.fabs(vol - VOL_CORPUS[name])
        results[name] = {
            "slopes_snappy": [list(s) for s in slopes],
            "abs_slopes": abs_slopes,
            "max_abs_slope": max(abs_slopes),
            "volume_snappy_f64": mp.nstr(vol, 12),
            "volume_corpus_err": mp.nstr(vol_err, 4),
        }
        print(f"\n  {name}: slopes {slopes}  |slopes| {abs_slopes}  "
              f"vol {mp.nstr(vol, 12)} (corpus err {mp.nstr(vol_err, 3)})")

    ok_41 = set(results["4_1"]["abs_slopes"]) == LIT_ABS["4_1"]
    ok_52 = set(results["5_2"]["abs_slopes"]) == LIT_ABS["5_2"]
    ok_vol = all(mp.mpf(results[n]["volume_corpus_err"]) < mp.mpf("1e-9")
                 for n in results)
    max52 = results["5_2"]["max_abs_slope"]

    print(f"\n[1] 4_1 hardening: |slopes| == {{4}}: {ok_41}")
    print(f"[2] 5_2 hardening: |slopes| == {{0,4,10}}: {ok_52} "
          f"(max {max52}; R2 refutation datum 10 not in DT {{3,4}} stands)")
    print(f"[3] 6_1 new datum: |slopes| = {results['6_1']['abs_slopes']} "
          f"(max {results['6_1']['max_abs_slope']}); no DT spectrum to compare")
    print(f"[4] volumes within 1e-9 of corpus: {ok_vol}")

    wb.add_data("knots", results)
    wb.add_data("convention_note", {
        "snappy_vs_hatcher_oertel": "sign differs (orientation convention); "
                                    "magnitude sets compared",
        "spun_normal_scope": "detected spun-normal slopes; completeness not "
                             "asserted",
    })
    wb.add_data("six_one_status", {
        "dt_spectrum": "NOT AVAILABLE (corpus + carried GGM tables cover "
                       "4_1/5_2 only); slopes banked, no reading tested"})
    wb.add_assertion("fourone_abs_slopes_match_lean",
                     computed=str(sorted(results["4_1"]["abs_slopes"])),
                     expected="[4]", tolerance="exact",
                     source="SnapPy normal_boundary_slopes vs a41MaxAbsSlope")
    wb.add_assertion("fivetwo_abs_slopes_match_literature",
                     computed=str(sorted(results["5_2"]["abs_slopes"])),
                     expected="[0, 4, 10]", tolerance="exact",
                     source="SnapPy vs Hatcher-Oertel recall {0,-4,-10} (abs)")
    wb.add_assertion("volumes_match_corpus_f64",
                     computed=str(bool(ok_vol)), expected="True",
                     tolerance="1e-9 per knot",
                     source="SnapPy float64 volume vs corpus 50-digit values")
    # q0 anchor: this probe never reads the substrate modulus. Verified by
    # transitive import cone (3 modules), not by reading this file alone —
    # nothing in the cone reaches q_parameter or qou_substrate.constants.
    # So the honest record is `independent`; stamping the standing proton
    # default would assert a pin the compute never read. Via save(extra=...)
    # and NOT add_data(), which nests under `data` where the audit reading
    # body["q0Anchor"] cannot see it. No q0Value — one here is a Q0_FLIP.
    wb.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "SnapPy cusp/slope geometry only — hyperbolic invariants of the "
            "cross-knot census, computed from the manifolds themselves. No "
            "substrate value is read; the 3-module import cone reaches "
            "neither q_parameter nor qou_substrate.constants."
        ),
    })

    ok = ok_41 and ok_52 and ok_vol
    print(f"\n  RESULT: {'HARDENED — literature recall confirmed' if ok else 'MISMATCH — see above'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
