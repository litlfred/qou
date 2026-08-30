"""qou-brng volume-defect route — REFUTED (scope-a): binding is not a mass-scale volume defect.

Bean qou-brng candidate route 1 (PR #5346). The mass/binding rung derivation (Lane 4,
`binding_mass_rung_derivation_probe.py`) floated the mass-DIFFERENCE / volume-defect picture as a
possible mechanism for why binding sits at the electron scale `m_e·Vol` while mass sits at
`m_e·Vol/ℏ_q²`: if binding is `B = Σ m_free − m_bound` and both masses carry the `lw/ℏ_q²` factor,
then `B = (m_e·lw/ℏ_q²)·ΔVol` with `ΔVol = A·Vol_nucleon − Vol_interface`, and the ℏ_q²-suppression
of binding would follow IF `ΔVol/Vol ~ ℏ_q²`.

## Result — REFUTED

The knot-volume defect is O(1), not O(ℏ_q²): with the free nucleon knot = Borromean 𝓑₃
(Vol = 7.328) and the nucleus = its interface link,

  iso   ΔVol = A·Vol(𝓑₃) − Vol_int   ΔVol/Vol   B_pred = (m_e·lw/ℏ_q²)·ΔVol   actual   overpred
  ³H    13.70                        1.65        1806 MeV                       8.48     213×
  ³He   14.66                        2.00        1932 MeV                       7.72     250×
  ⁴He   21.98                        3.00        2898 MeV                      28.30     102×

The volume-defect route OVERPREDICTS binding by ~1/ℏ_q² (102–250×): `ΔVol/Vol = O(1)`, so
`B_pred = (m_e·lw/ℏ_q²)·O(1) ~ GeV`, not the MeV reality. **Binding is NOT a hyperbolic-volume
defect at the mass scale**, and the O(1/ℏ_q²) mass terms do NOT cancel down to O(ℏ_q²) at the
volume level.

## Consequence (sharpens qou-brng, adds skepticism)

1. The mass-DIFFERENCE / cancellation framing floated in the Lane-4 derivation Step 3 is **refuted**
   as a mechanism: binding is not the residual of two nearly-cancelling mass-scale volumes. Binding
   is directly an electron-scale × coordination-count object `B = m_e·Vol·M`; the ℏ_q² gap to mass
   is because MASS carries the CAL-2 muon-anchor factor that binding never had — not a cancellation.
2. Therefore the **saturated-fraction ≈ ℏ_q² coincidence** (Lane 4, 0.95·ℏ_q² at ⁵⁶Fe) loses its one
   candidate mechanism. With the volume-defect route eliminated, that agreement is — on current
   evidence — **more likely a numerical coincidence than a derived prediction** (numerology guard).
   Do not chase it further without a genuinely new structural mechanism.

Scope-(a): the volume-defect construction is tested and shown insufficient; no proved invariant
excludes every mass-difference picture. No fit; no wiring; q₀ proton-anchored.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from _li_2_q_util import linking_weight_family_a  # noqa: E402
import q_parameter as qp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# nucleus = interface link volume (arc committed values); free nucleon knot = Borromean 𝓑₃.
ISO = [
    ("3H",  3, "8.286316817806593", "8.481821"),
    ("3He", 3, "7.327724753417752", "7.718041"),
    ("4He", 4, "7.327724753417752", "28.295674"),
]


def main() -> int:
    set_compute_dps(50)
    q = qp.Q_MP
    qi = 1 / q
    me = mp.mpf(str(qp.M_E_MEV))
    hbar2 = qp.HBAR_Q_SQ_MP
    lw = linking_weight_family_a(q, qi)
    vol_nucleon = qp.VOL_BORROMEAN
    prefactor = me * lw / hbar2

    print("=" * 78)
    print("qou-brng volume-defect route — REFUTED")
    print("=" * 78)
    print(f"  free nucleon knot Vol(𝓑₃) = {mp.nstr(vol_nucleon,8)}")
    print(f"  mass prefactor m_e·lw/ℏ_q² = {mp.nstr(prefactor,7)} MeV / volume-unit\n")
    print(f"  {'iso':<5}{'ΔVol':>9}{'ΔVol/Vol':>10}{'B_pred (MeV)':>14}{'actual':>10}{'overpred':>10}")
    overs = []
    for name, A, volint, B in ISO:
        vi = mp.mpf(volint)
        dVol = A * vol_nucleon - vi
        B_pred = prefactor * dVol
        over = B_pred / mp.mpf(B)
        overs.append(over)
        print(f"  {name:<5}{float(dVol):>9.2f}{float(dVol/vi):>10.2f}{float(B_pred):>14.0f}"
              f"{float(mp.mpf(B)):>10.2f}{float(over):>9.0f}×")
    print(f"\n  ⇒ ΔVol/Vol = O(1) (1.65–3.0), NOT O(ℏ_q²) ⇒ B_pred ~ GeV, overpredicts by ~1/ℏ_q².")
    print("    Binding is NOT a mass-scale hyperbolic-volume defect. REFUTED (scope-a).")
    print("\n### Consequence for qou-brng:")
    print("  • The mass-difference/cancellation framing (Lane-4 Step 3) is refuted as a mechanism.")
    print("  • The saturated-fraction ≈ ℏ_q² coincidence loses its one candidate mechanism ⇒ on")
    print("    current evidence more likely NUMEROLOGY than a derived prediction. Do not chase it")
    print("    without a genuinely new structural mechanism.")

    min_over = min(overs)
    refuted = min_over > mp.mpf("50")   # overpredicts by ≳ 1/(2ℏ_q²)
    wb = WitnessBuilder("binding-volume-defect-route-refuted", engine="python (mpf 50 dps)")
    wb.set_description(
        "qou-brng candidate route 1 (volume-defect / mass-difference) REFUTED (scope-a). If binding "
        "were B=(m_e·lw/ℏ_q²)·ΔVol with ΔVol=A·Vol(𝓑₃)−Vol_interface, the ℏ_q² suppression would need "
        "ΔVol/Vol~ℏ_q². Measured: ΔVol/Vol=1.65 (³H), 2.00 (³He), 3.00 (⁴He) — O(1), not O(ℏ_q²) — so "
        "B_pred=(m_e·lw/ℏ_q²)·O(1)~GeV, overpredicting binding by 102–250× (≈1/ℏ_q²). Binding is NOT "
        "a mass-scale hyperbolic-volume defect; the O(1/ℏ_q²) mass terms do not cancel to O(ℏ_q²) at "
        "the volume level. Consequence: the mass-difference/cancellation framing of Lane-4 Step 3 is "
        "refuted, and the saturated-fraction≈ℏ_q² coincidence loses its one candidate mechanism — on "
        "current evidence more likely numerology than a derived prediction. No fit; no wiring; q₀ "
        "proton-anchored.")
    wb.add_parameter("q0_anchor", "proton/experimental (q_parameter.Q_MP)")
    wb.add_data("mass_prefactor_MeV_per_volunit", mp.nstr(prefactor, 12))
    for (name, A, volint, B), over in zip(ISO, overs):
        wb.add_data(f"overprediction_factor_{name}", mp.nstr(over, 8))
    wb.add_assertion(
        name="volume_defect_route_overpredicts_by_inverse_hbar_q_sq",
        computed=bool(refuted), expected=True, tolerance=0,
        source=("ΔVol/Vol = O(1) (1.65–3.0), not O(ℏ_q²), so B_pred=(m_e·lw/ℏ_q²)·ΔVol overpredicts "
                "binding by >50× (102–250×, ≈1/ℏ_q²). The volume-defect/mass-difference route is "
                "refuted (scope-a): binding is not a mass-scale volume defect. No fit."))
    out = wb.save()
    print(f"\nWitness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
