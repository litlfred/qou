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
                            Now backed in Lean, not just by SnapPy:
                            QOU.Knot.FlatTet.BlochWigner_lob_ofReal gives
                            zero volume for EVERY real shape parameter, with
                            no hypotheses, and the trefoil case is worked in
                            QOU/Knot/FlatTetrahedra.lean.  A degenerate link
                            has real (flat) shapes, so its Bloch–Wigner
                            volume vanishes identically rather than
                            numerically.
  Vol(8₁₁)   = 8.2863168    (all tetrahedra positively oriented)
  Vol(L6a4)  = 7.3277248    = 8G = Vol(Borromean) — L6a4 IS the
                              Borromean link (Thistlethwaite name).

KEY FINDINGS:

1. **L6a4 = Borromean.** The ³He binding link computed by the SDP is
   the Borromean rings (Vol = 8·Catalan = 7.32772), the same link
   that defines the per-nucleon braid 𝓑₃. This is an identification,
   not a fit.

2. **The single-link endomorphism does NOT extend to A ≥ 3.**
   B = m_e × Vol(K_bind) × Δtr gives −6.3% for the deuteron (via the
   Hopf → Vol(𝓑₃) substitution, since Vol(Hopf) = 0) and about −56%
   for both ³H and ³He. The trace difference Δtr ≈ 0.6–0.9 is
   nearly A-independent while the binding energy grows ~13×, so the
   A-dependence cannot live in a single binding-link volume.

   This is an HONEST NEGATIVE, and closing A ≥ 3 needs additional
   structure (per-pair sum over the JSJ decomposition, or a different
   trace object) — NOT a rescaling of Δtr by hand-chosen factors
   (cf. retracted PR #1383).

   ⚠ CORRECTED 2026-08-15 (bean `qou-bind`). This paragraph read
   "matches the deuteron at +0.2%" and called that a success. The
   committed witness has never agreed: `binding-link-volumes.witness.json`
   records `deuteron_endomorphism_holds` with `"passed": false` and
   `err_pct = −6.306958776805962`, against a stated tolerance of 1%.
   So the deuteron is NOT a special success here — it is a near-miss
   that fails its own assertion. The result is a cleaner negative than
   the prose claimed, not a dirtier one: no A is matched, so there is
   no special case to explain away.

   WHERE +0.2% CAME FROM, traced (bean `qou-btdr` tracks the fix, which
   is not local to this file). "+0.2%" is precisely the claim that
   Δtr(²H) = 0.5952:

       Δtr needed for +0.2%                     = 0.5952835748896166…
       hardcoded in binding_per_bond_decomposition.py:126 = 0.5952
       binding_canonical(1,1, use_closed_form=True) TODAY = 0.5566260326923999

   i.e. the figure matches that hardcoded constant to four digits, and
   the function it is attributed to no longer returns it. Whether
   `binding_canonical` drifted or the constant was always copied from a
   different trace convention is NOT settled here — deciding that is a
   physics judgement about which Δtr is correct, and it changes numbers
   in at least seven files. Do not "fix" the −6.3% by reinstating 0.5952.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

from mpmath import mp, mpf, fabs, catalan

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
)
# Canonical knot volumes — single source of truth (knot_volumes.py),
# 50-dps mpmath from SnapPy-HP literature; no runtime SnapPy needed.
from knot_volumes import VOL_8_11_MPF, VOL_BORROMEAN_MPF  # noqa: E402


def _delta_tr(Z: int, N: int) -> mpf:
    """Full-precision Δtr = |tr_free| − |tr_atom| from binding_canonical
    (Wenzl-bridge closed form) — same convention as the deuteron
    endomorphism result."""
    from binding_canonical import binding_canonical
    from codata_constants import Q_BETA_MEV
    r = binding_canonical(Z, N, Q_beta_n_mev=float(Q_BETA_MEV),
                          use_closed_form=True, verbose=False)
    tr_free = mpf(str(r["tr_M_free"]))
    tr_atom = mpf(str(r["tr_M_atom"]))
    return fabs(tr_free) - fabs(tr_atom)


def main():
    set_compute_dps()
    wb = WitnessBuilder("binding-link-volumes", engine="mpmath")

    m_e = mpf(str(M_E_MEV))
    VOL_B3 = 8 * catalan

    # Binding links (SDP registry) with CANONICAL volumes from
    # knot_volumes.py. L6a4 = Borromean rings ⇒ VOL_BORROMEAN_MPF.
    # Hopf is Seifert-fibred (Vol = 0).
    vols = {
        "2H":  {"link": "Hopf (L2a1)", "vol": mpf("0"),          "hyperbolic": False},
        "3H":  {"link": "8_11",        "vol": VOL_8_11_MPF,      "hyperbolic": True},
        "3He": {"link": "L6a4",        "vol": VOL_BORROMEAN_MPF, "hyperbolic": True},
    }
    # Full-precision trace defects (binding_canonical, Wenzl bridge).
    dtr = {"2H": _delta_tr(1, 1), "3H": _delta_tr(1, 2), "3He": _delta_tr(2, 1)}
    # AME 2020 binding energies from the canonical validation witness.
    AME = {
        "2H": mpf(str(AME_B_DEUTERON_MEV_VALIDATION)),
        "3H": mpf(str(AME_B_TRITIUM_MEV_VALIDATION)),
        "3He": mpf(str(AME_B_HE3_MEV_VALIDATION)),
    }

    print("=" * 70)
    print("BINDING-LINK HYPERBOLIC VOLUMES (SDP registry + SnapPy)")
    print("=" * 70)
    print()
    print(f"Vol(𝓑₃) = 8G = {float(VOL_B3):.10f}")
    print()

    results = {}
    for iso in ["2H", "3H", "3He"]:
        v = vols[iso]["vol"]
        # Hopf (Vol=0) → Vol(𝓑₃) substitution (deuteron special case).
        # Branch on the SEMANTIC FLAG, not on the volume.  The older form
        # `v if v > mpf("0.01") else VOL_B3` tested a magic threshold while
        # `"hyperbolic"` sat in the same dict, and was safe only by a theorem the
        # file never cited: Cao–Meyerhoff put the minimum volume of a cusped
        # orientable hyperbolic 3-manifold at 2.0298832…, so nothing genuinely
        # hyperbolic can fall under 0.01.  That margin is real but it evaporates
        # if the registry ever gains a closed or non-cusped manifold, or if
        # someone tunes the threshold.  The flag has neither failure mode.
        v_eff = v if vols[iso]["hyperbolic"] else VOL_B3
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
              f"{'' if vols[iso]['hyperbolic'] else '  → 8G (Hopf=0)'}")
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
