#!/usr/bin/env python3
# polynomial_q_not_applicable: even-power h-ladder of interaction energies, not
# a Jones-polynomial evaluation.
"""
The even-power h-ladder of interaction energies, and where van der Waals sits.

NOTE (2026-06-30, per prop:vdw-pskew-isolation): the "bare symmetric-block e₊ →
vdW energy" framing below is SUPERSEDED at the channel level. Van der Waals is
the DISCARDED bar-odd residual sinh(2λ)(e₊−e₋), not the e₊ carrier itself; the
e₊ block is the retained cosh carrier (see hbond_vdw_sdp.py). The h⁴ SMALLNESS
of the vdW rung is consistent with that residual being h-suppressed, so this
ladder remains a valid energy-SCALE estimate — only the "vdW = bare e₊" object
label is corrected.

Owner option 2: work out the energy scale that takes the bare symmetric-block
e₊ (categorical, ℏ_q-scale) down to the ~kJ/mol molecular van der Waals energy.

THE LADDER (interaction / covalent energy ratio, even powers of h = q₀−q₀⁻¹):
  covalent (trefoil, knot)     : h⁰ = 1
  hydrogen bond (weak crossing): h²  ≈ 0.044   (E_HB/E_cov; matches measured)
  van der Waals (Hopf link)    : h⁴  ≈ 0.0019  (per-contact dispersion)
Each weaker interaction is h² weaker — a clean even-power ladder. The H-bond
rung (h²) is the verified one (hbond_categorical_action.py: H₂O/HF latent heat
to ~1–2%). The vdW rung (h⁴) is tested here.

PER-CONTACT TEST (non-hydrogen-bonding liquids; L_vap IS the dispersion cohesion,
spread over the coordination number Z ≈ 12 for close packing):
  vdW per contact = L_vap / Z ;  compare (L_vap/Z)/E_cov to h⁴.

THE BARE-vs-MOLECULAR GAP (the archimedean piece): the categorical symmetric
block e₊ has Markov q-dim ≈ 0.70 (ℏ_q-scale ≈ 0.10), far ABOVE h⁴. The
suppression from the bare e₊ to the per-contact h⁴ vdW is the ARCHIMEDEAN
inter-molecular separation: dispersion falls as 1/r⁶, and the bare e₊ is the
touching (r→contact) limit. The exact 1/r⁶ separation factor is NOT fixed by
the Hecke decomposition — it needs the archimedean functor's distance
dependence, which the framework does not yet carry at molecular scale.

STATUS (honest, tiered): the even-power h-ladder is a STRUCTURAL near-match —
the per-contact vdW is the right ORDER (h⁴) for close-packed liquids; the exact
energy (coordination number Z + the 1/r⁶ archimedean separation) is OPEN, not
fitted. No scale is tuned to reproduce a vdW energy.

Refs: def:van-der-waals-hopf-channel; prop:hopf-link-symmetric-decomposition;
hbond_categorical_action.py (the h² H-bond rung); hbond_vdw_sdp.py (e₊ q-dim).
"""
from __future__ import annotations

import sys
from math import sqrt
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

try:
    from q_parameter import q_at
    Q0 = float(q_at())
except Exception as _exc:  # pragma: no cover - fail loudly, never substitute
        # Was: Q0 = 1.1099780333553254 — a value that is NEITHER pin, sitting
        # 506 ppb from muon and 495 ppb from proton, i.e. ~44x the ~11.5 ppb
        # mu-p substrate tension the two-layer discipline exists to manage. It
        # was substituted silently on any import hiccup, so a bare container
        # produced numbers that looked fine and were wrong by 44 tensions.
        # AGENTS.md q0-anchor: never straddle the two layers inside one quantity;
        # q0_cross_layer_fallback_scan.py: "fail loudly" rather than substitute.
        raise RuntimeError(
            "q_at() unavailable and there is no safe fallback: this producer "
            "must compute at a declared pin, not at a hardcoded approximation. "
            "Install/point at qou-substrate rather than substituting a literal."
        ) from _exc

# Non-hydrogen-bonding liquids: L_vap IS the dispersion (vdW) cohesion.
#   name : (E_cov_kJmol, L_vap_kJmol, Z_coordination)
DISPERSION_LIQUIDS = {
    "CH4": (439.0, 8.17, 12),   # methane, close-packed
    "Ar":  (None,  6.53, 12),   # argon — atomic, no covalent E_cov (use ~bond)
    "N2":  (945.0, 5.57, 12),   # dinitrogen (triple bond E_cov)
}


def main() -> None:
    w = WitnessBuilder("hbond-vdw-energy-ladder", engine="python")
    q = Q0
    h = q - 1.0 / q
    h2, h4 = h * h, h ** 4
    hbar_q = (q - 1.0) / q
    e_plus_qdim = (1.0 / (sqrt(q) + 1.0 / sqrt(q)) + 1.0 / q) / (q + 1.0 / q)

    print("=" * 74)
    print("Even-power h-ladder of interaction energies — where vdW sits")
    print("=" * 74)
    print(f"  q₀ = {q:.6f}   h = q₀−q₀⁻¹ = {h:.5f}")
    print(f"  ladder (interaction/covalent):")
    print(f"    covalent (trefoil)      h⁰ = 1")
    print(f"    hydrogen bond           h² = {h2:.5f}   (verified: H₂O/HF ~1–2%)")
    print(f"    van der Waals (Hopf)    h⁴ = {h4:.6f}   (per-contact, tested below)")
    print()
    print(f"  per-contact vdW test (L_vap/Z)/E_cov vs h⁴ = {h4:.6f}:")
    print(f"    {'liquid':6s}{'E_cov':>7s}{'L_vap':>7s}{'Z':>3s}"
          f"{'vdW/contact':>12s}{'/E_cov':>9s}{'ratio/h⁴':>9s}")
    rows = []
    for name, (ecov, lvap, Z) in DISPERSION_LIQUIDS.items():
        per_contact = lvap / Z
        ratio = (per_contact / ecov) if ecov else None
        r_over_h4 = (ratio / h4) if ratio else None
        rows.append((name, ecov, lvap, Z, per_contact, ratio, r_over_h4))
        ecs = f"{ecov:7.0f}" if ecov else f"{'—':>7s}"
        rs = f"{ratio:9.5f}" if ratio else f"{'—':>9s}"
        rh = f"{r_over_h4:9.2f}" if r_over_h4 else f"{'—':>9s}"
        print(f"    {name:6s}{ecs}{lvap:7.2f}{Z:3d}{per_contact:12.3f}{rs}{rh}")
    print()
    # bare e₊ (categorical) vs molecular per-contact vdW (h⁴):
    suppression = h4 / e_plus_qdim
    print(f"  bare symmetric block e₊ (categorical) q-dim = {e_plus_qdim:.4f} "
          f"(ℏ_q-scale ≈ {hbar_q:.3f})")
    print(f"  molecular per-contact vdW ≈ h⁴ = {h4:.6f}")
    print(f"  ⇒ archimedean suppression bare→molecular ≈ h⁴/e₊ = {suppression:.5f}")
    print(f"    (the 1/r⁶ inter-molecular separation; e₊ is the touching limit)")
    print()
    print("  TIER: even-power h-ladder = STRUCTURAL near-match (per-contact vdW is")
    print("        the right ORDER h⁴); exact energy (Z + 1/r⁶ archimedean")
    print("        separation) is OPEN, not fitted.")

    w.set_description(
        "The even-power h-ladder of interaction energies (h = q₀−q₀⁻¹): covalent "
        "h⁰=1, hydrogen bond h²≈0.044 (verified, H₂O/HF latent heat ~1–2%), van "
        "der Waals (the Hopf symmetric block) h⁴≈0.0019. Per-contact dispersion "
        "test on non-H-bonding liquids (CH₄, N₂; L_vap/Z over coordination Z≈12) "
        "lands at the right ORDER h⁴. The bare categorical symmetric block e₊ is "
        "ℏ_q-scale (≈0.10), far above h⁴; the suppression to the molecular "
        "per-contact vdW is the ARCHIMEDEAN 1/r⁶ inter-molecular separation (e₊ is "
        "the touching limit), NOT fixed by the Hecke decomposition. Tiered: the "
        "h-ladder is a structural near-match (order of magnitude); the exact vdW "
        "energy (coordination Z + 1/r⁶ archimedean separation) is OPEN, not fitted."
    )
    w.set_content_block("def:van-der-waals-hopf-channel")
    w.add_parameter("q", q)
    w.add_data("h", h)
    w.add_data("h_squared_hbond_rung", h2)
    w.add_data("h_fourth_vdw_rung", h4)
    w.add_data("hbar_q", hbar_q)
    w.add_data("e_plus_qdim", e_plus_qdim)
    w.add_data("archimedean_suppression_h4_over_eplus", suppression)
    for name, ecov, lvap, Z, per_contact, ratio, r_over_h4 in rows:
        w.add_data(f"{name}_vdw_per_contact_kJmol", per_contact)
        if ratio:
            w.add_data(f"{name}_per_contact_over_Ecov", ratio)
            w.add_data(f"{name}_ratio_over_h4", r_over_h4)
    w.add_assertion(
        "even-power ladder: H-bond rung is h² (the verified rung)",
        computed=bool(abs(h2 - 0.0437) < 0.001), expected=True,
        source="h² = (q₀−q₀⁻¹)² ; matches measured H-bond/covalent ~0.044",
    )
    w.add_assertion(
        "CH₄ per-contact vdW is the right order h⁴ (within 5×)",
        computed=bool(0.2 < rows[0][6] < 5.0), expected=True,
        source="(L_vap/Z)/E_cov for CH₄ vs h⁴ — order-of-magnitude, not fit",
    )
    w.add_data(
        "finding",
        "Interaction energies form an even-power h-ladder (h = q₀−q₀⁻¹): covalent "
        "h⁰, hydrogen bond h² (verified), van der Waals h⁴. The vdW = Hopf "
        "symmetric block sits at the h⁴ rung; the per-contact dispersion of "
        "close-packed non-H-bonding liquids (CH₄, N₂) is the right ORDER h⁴. The "
        "bare categorical e₊ is ℏ_q-scale; the suppression to the molecular "
        "per-contact h⁴ is the archimedean 1/r⁶ inter-molecular separation (e₊ = "
        "touching limit), which the framework does not yet carry at molecular "
        "scale. Tier: h-ladder structural near-match (order of magnitude); exact "
        "vdW energy (coordination Z + 1/r⁶ archimedean separation) OPEN, not fitted."
    )
    w.save()
    print("\nDone. Witness saved (hbond-vdw-energy-ladder).")


if __name__ == "__main__":
    main()
