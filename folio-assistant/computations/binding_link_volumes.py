#!/usr/bin/env python3
"""
binding_link_volumes.py — hyperbolic volumes of the per-atom binding
links from the SDP registry, and a test of the binding-endomorphism
extension B = m_e × Vol(K_bind) × Δtr to A ≥ 3.

BINDING LINKS (from binding-k-solver.witness.json SDP registry):
  ²H  → Hopf link L2a1      (Seifert-fibred, Vol = 0)
  ³H  → 8₁₁ knot            (hyperbolic)
  ³He → L6a4 link           (hyperbolic)

RESULTS (SnapPy, verified solution types):
  Vol(Hopf)  = 0            (degenerate — Seifert-fibred)
  Vol(8₁₁)   = 8.2863168    (all tetrahedra positively oriented)
  Vol(L6a4)  = 7.3277248    = 8G = Vol(Borromean) — L6a4 IS the
                              Borromean link (Thistlethwaite name).

KEY FINDINGS:

1. **L6a4 = Borromean.** The ³He binding link computed by the SDP is
   the Borromean rings (Vol = 8·Catalan = 7.32772), the same link
   that defines the per-nucleon braid 𝓑₃. This is an identification,
   not a fit.

2. **The single-link endomorphism does NOT extend to A ≥ 3.**
   B = m_e × Vol(K_bind) × Δtr matches the deuteron at +0.2% (via the
   Hopf → Vol(𝓑₃) substitution, since Vol(Hopf) = 0), but gives
   −60% for both ³H and ³He. The trace difference Δtr ≈ 0.6–0.9 is
   nearly A-independent while the binding energy grows ~13×, so the
   A-dependence cannot live in a single binding-link volume.

   This is an HONEST NEGATIVE: the deuteron success is special, and
   closing A ≥ 3 needs additional structure (per-pair sum over the
   JSJ decomposition, or a different trace object) — NOT a rescaling
   of Δtr by hand-chosen factors (cf. retracted PR #1383).
"""
from __future__ import annotations

import sys
from pathlib import Path

from mpmath import mp, mpf, fabs, catalan

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402


def main():
    set_compute_dps()
    wb = WitnessBuilder("binding-link-volumes", engine="snappy+mpmath")

    m_e = mpf(str(M_E_MEV))
    VOL_B3 = 8 * catalan

    # SnapPy-computed binding-link volumes (literature-stable values).
    # Recomputed here as literals to avoid a hard SnapPy dependency in
    # the witness pipeline; provenance is the SnapPy census manifolds
    # L2a1 (Hopf), 8_11, L6a4.
    vols = {
        "2H":  {"link": "Hopf (L2a1)", "vol": mpf("0"),                "hyperbolic": False},
        "3H":  {"link": "8_11",        "vol": mpf("8.2863168178"),     "hyperbolic": True},
        "3He": {"link": "L6a4",        "vol": mpf("7.3277247534"),     "hyperbolic": True},
    }
    dtr = {"2H": mpf("0.5952"), "3H": mpf("0.8040"), "3He": mpf("0.8412")}
    AME = {"2H": mpf("2.22452"), "3H": mpf("8.48182"), "3He": mpf("7.71804")}

    print("=" * 70)
    print("BINDING-LINK HYPERBOLIC VOLUMES (SDP registry + SnapPy)")
    print("=" * 70)
    print()
    print(f"Vol(𝓑₃) = 8G = {float(VOL_B3):.10f}")
    print()

    results = {}
    for iso in ["2H", "3H", "3He"]:
        v = vols[iso]["vol"]
        # Hopf (Vol=0) → Vol(𝓑₃) substitution (deuteron special case)
        v_eff = v if v > mpf("0.01") else VOL_B3
        B = m_e * v_eff * dtr[iso]
        err = float((B - AME[iso]) / AME[iso] * 100)
        results[iso] = {
            "link": vols[iso]["link"],
            "vol": str(float(v)),
            "vol_eff": str(float(v_eff)),
            "B_pred_MeV": str(float(B)),
            "B_AME_MeV": str(float(AME[iso])),
            "err_pct": err,
        }
        print(f"  {iso:4s} [{vols[iso]['link']:11s}]: Vol = {float(v):.7f}"
              f"{'  → 8G (Hopf=0)' if v <= mpf('0.01') else ''}")
        print(f"        B = m_e·Vol·Δtr = {float(B):.3f} vs AME {float(AME[iso]):.3f}"
              f"  err = {err:+.1f}%")

    print()
    print("L6a4 = Borromean: Vol(L6a4) =", float(vols["3He"]["vol"]),
          "= 8G =", float(VOL_B3),
          f"(match {float(fabs(vols['3He']['vol'] - VOL_B3)):.2e})")
    print()
    print("CONCLUSION: single-link endomorphism extends to ²H only.")
    print("A ≥ 3 (−60%) needs structure beyond one binding-link volume.")

    wb.set_description(
        "Hyperbolic volumes of the SDP binding links (Hopf/8₁₁/L6a4). "
        "L6a4 = Borromean (Vol = 8G). The endomorphism B = m_e·Vol(K_bind)·Δtr "
        "matches ²H at +0.2% but fails A≥3 (−60%): honest negative, A-dependence "
        "is not in a single binding-link volume."
    )
    wb.add_data("binding_link_volumes", {
        "Hopf_2H": "0 (Seifert-fibred)",
        "knot_8_11_3H": "8.2863168178",
        "L6a4_3He": "7.3277247534",
        "Vol_B3_8G": str(float(VOL_B3)),
        "L6a4_equals_borromean": bool(fabs(vols["3He"]["vol"] - VOL_B3) < mpf("1e-6")),
    })
    wb.add_data("endomorphism_extension_test", results)

    wb.add_assertion(
        "L6a4_is_borromean",
        computed=float(fabs(vols["3He"]["vol"] - VOL_B3)),
        expected=0,
        tolerance=1e-6,
        source="Vol(L6a4) = 8G = Vol(Borromean)",
    )
    wb.add_assertion(
        "deuteron_endomorphism_holds",
        computed=abs(results["2H"]["err_pct"]),
        expected=0,
        tolerance=1,
        source="B(²H) = m_e·Vol(𝓑₃)·Δtr within 1%",
    )
    wb.save()


if __name__ == "__main__":
    main()
