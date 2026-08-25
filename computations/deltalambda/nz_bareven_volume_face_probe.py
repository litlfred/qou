#!/usr/bin/env python3
"""The arg(u) wall is a QUADRATURE effect: the bar-EVEN Volume face (g₂) is MAXIMAL exactly where the
bar-ODD CS face (c₃) is frozen. Forward, no fit. Corrects the prior "r frozen like c₃" pessimism.

CHAIN (read first):
  * c₃ wall (#4293, ArgUPhaseBranchSelection.lean): the NZ bar-ODD/CS face
    nzImVolume(r,φ) = (√3/2)·r²·sin(2φ) is FROZEN on the real substrate ray φ=0 (u=2 log q₀ real ⇒
    sin 0 = 0). c₃'s percent swing has nowhere to live (magnitude smooth #4288 + phase frozen here).
  * THIS probe (bar-even, the μ₀ g₂ side, distinct angle): g₂ is the Volume face = the cos-quadrature
    partner nzReVolume(r,φ) = (√3/2)·r²·cos(2φ). At the SAME φ=0, cos 0 = 1 ⇒ MAXIMAL, not frozen.

WHAT THIS ESTABLISHES (all forward; exact trig, no observable fitted):
  A. QUADRATURE: nzReVolume² + nzImVolume² = (3/4)·r⁴ (Pythagorean, sin²+cos²=1). At the real ray φ=0
     ALL of it is in the bar-EVEN face: nzImVolume(r,0)=0 (frozen, c₃), nzReVolume(r,0)=(√3/2)r² (peak).
  B. PHASE-SLOPE contrast: d(nzImVolume)/dφ|₀ = √3·r² (MAXIMAL slope — c₃'s steepest, but value 0);
     d(nzReVolume)/dφ|₀ = 0 (STATIONARY — g₂ is doubly anchor-smooth: magnitude r² smooth #4288 AND
     phase-flat). Even vs odd in φ (nzReVolume_phase_even vs nzImVolume odd).
  C. VERDICT: the arg(u) wall that freezes c₃ LEAVES g₂ maximal and stable — g₂ lives exactly where c₃
     dies. The μ₀ bar-even and Q_β bar-odd closures are the two quadrature faces of ONE NZ object; the
     real substrate ray is the point where CS(c₃)=0 and Vol(g₂)=peak. Corrects the pessimistic "r
     frozen like c₃": r is NOT in the frozen channel — the bar-even face is alive.

SCOPE (honest): this shows the c₃ wall does NOT transfer to g₂ (opposite quadrature). It does NOT
derive g₂'s value/r — that is still the trefoil bar-even NZ coefficient (leading 1 from the coloring,
#4319). The √3/2 coefficient here is the figure-eight cusp modulus (illustrative); the trefoil's own
bar-even modulus is the g₂ leading value. scope-(a), audit-only, nothing wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from substrate.witness_base import WitnessBuilder  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def nz_im(r, phi):   # corpus bar-odd / CS face
    return (mp.sqrt(3) / 2) * r ** 2 * mp.sin(2 * phi)


def nz_re(r, phi):   # bar-even / Volume face (cos-quadrature partner)
    return (mp.sqrt(3) / 2) * r ** 2 * mp.cos(2 * phi)


def main() -> int:
    r = mp.mpf("0.2086")   # |u| = 2 log q0 illustrative magnitude (substrate)
    phi0 = mp.mpf("0")     # real substrate ray

    # A. quadrature (Pythagorean) + real-ray split
    pyth = nz_re(r, phi0) ** 2 + nz_im(r, phi0) ** 2
    pyth_target = mp.mpf("0.75") * r ** 4
    pyth_ok = abs(pyth - pyth_target) < mp.mpf("1e-30")
    im_frozen = abs(nz_im(r, phi0)) < mp.mpf("1e-35")
    re_peak = nz_re(r, phi0)
    re_peak_target = (mp.sqrt(3) / 2) * r ** 2
    re_maximal = abs(re_peak - re_peak_target) < mp.mpf("1e-35") and re_peak > 0

    # B. phase slopes at φ=0
    dim = mp.diff(lambda p: nz_im(r, p), phi0)     # = √3 r² (max slope)
    dre = mp.diff(lambda p: nz_re(r, p), phi0)     # = 0 (stationary)
    im_max_slope = abs(dim - mp.sqrt(3) * r ** 2) < mp.mpf("1e-25")
    re_stationary = abs(dre) < mp.mpf("1e-25")

    result = {
        "A_quadrature": {
            "pythagorean_nzRe2_plus_nzIm2": mp.nstr(pyth, 8),
            "equals_3_4_r4": bool(pyth_ok),
            "real_ray_nzIm_frozen": bool(im_frozen),       # c₃ face = 0
            "real_ray_nzRe_peak": mp.nstr(re_peak, 8),     # g₂ face = (√3/2)r²
            "nzRe_is_maximal": bool(re_maximal),
            "meaning": "on the real substrate ray φ=0 ALL the NZ quadratic is in the bar-EVEN (Volume) "
                       "face; the bar-ODD (CS, c₃) face is null.",
        },
        "B_phase_slopes_at_phi0": {
            "d_nzIm_dphi": mp.nstr(dim, 8) + " (= √3 r², MAX slope — c₃'s steepest, but value 0)",
            "d_nzRe_dphi": mp.nstr(dre, 6) + " (= 0, STATIONARY — g₂ doubly anchor-smooth)",
            "nzIm_max_slope": bool(im_max_slope),
            "nzRe_stationary": bool(re_stationary),
            "parity": "nzIm ODD in φ (sin) ⇒ φ=0 steepest; nzRe EVEN (cos) ⇒ φ=0 extremum "
                      "(nzReVolume_phase_even).",
        },
        "C_verdict": {
            "wall_is_quadrature": "the arg(u) wall freezes the bar-odd CS face (sin, φ=0) but leaves "
                                  "the bar-even Volume face (cos, φ=0) MAXIMAL and stationary.",
            "g2_lives_where_c3_dies": True,
            "corrects": "the prior 'r frozen like c₃' pessimism — r is NOT in the frozen channel; the "
                        "bar-even face is alive at the substrate.",
            "still_open": "g₂'s VALUE/r = the TREFOIL bar-even NZ coefficient (leading 1 from the "
                          "coloring, #4319); the √3/2 here is the figure-eight modulus (illustrative).",
        },
    }

    payload = {
        "computation": "nz-bareven-volume-face",
        "description": ("The arg(u) wall is a QUADRATURE effect: the c₃ front proved the NZ bar-odd/CS "
                        "face nzImVolume=(√3/2)r²sin(2φ) is FROZEN on the real substrate ray φ=0. The "
                        "μ₀ g₂ is the bar-even/Volume face = the cos partner nzReVolume=(√3/2)r²cos(2φ), "
                        "MAXIMAL (cos 0=1) and STATIONARY (even in φ, zero phase-slope) at the SAME "
                        "φ=0 — doubly anchor-smooth. Pythagorean nzRe²+nzIm²=(3/4)r⁴; at φ=0 all the "
                        "energy is in the bar-even face (CS=0, Vol=peak). So the wall that kills c₃ "
                        "LEAVES g₂ maximal — g₂ lives where c₃ dies. Corrects the prior 'r frozen like "
                        "c₃'. Does NOT derive g₂'s value (=trefoil bar-even NZ coeff, #4319). scope-(a), "
                        "audit-only, nothing wired."),
        "audit_only": True,
        "tier": "quadrature structure of the arg(u) wall (exact trig; no fit)",
        "result": result,
        "context": {
            "axis": "Δ_λ binding — μ₀ −9% closure, g₂ = bar-even Volume face vs the c₃ arg(u) wall",
            "lean": "QOU/MassTheory/NZBarEvenVolumeFace.lean (nzReVolume_real_ray[_ne_zero/_pos], "
                    "nzReVolume_phase_even)",
            "corpus_bar_odd": "QOU/QBeta/ArgUPhaseBranchSelection.lean (nzImVolume, frozen at φ=0)",
            "builds_on": "#4319 (trefoil coloring, g₂=cusp-shape barEven face), #4293 (c₃ arg(u) wall), "
                         "#4288 (magnitude smooth)",
            "no_fit": True,
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "nz-bareven-volume-face", payload,
        script_path=__file__, engine="mpmath", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("pythagorean_quadrature", computed=str(bool(pyth_ok)), expected="True")
    wb.add_assertion("bar_odd_frozen_bar_even_maximal",
                     computed=str(bool(im_frozen and re_maximal)), expected="True")
    wb.add_assertion("bar_even_phase_stationary", computed=str(bool(re_stationary)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== The arg(u) wall is a QUADRATURE effect (bar-even Volume face) ===")
    print(f"A. real ray φ=0:  nzIm (CS, c₃) = {mp.nstr(nz_im(r,phi0),4)} (FROZEN)   "
          f"nzRe (Vol, g₂) = {mp.nstr(re_peak,6)} (PEAK = √3/2·r²)")
    print(f"   Pythagorean nzRe²+nzIm² = {mp.nstr(pyth,6)} = (3/4)r⁴: {pyth_ok}  "
          f"⇒ all energy in the bar-even face at φ=0")
    print(f"B. phase slope @φ=0:  d(nzIm)/dφ = {mp.nstr(dim,5)} (MAX, c₃ steepest)   "
          f"d(nzRe)/dφ = {mp.nstr(dre,3)} (STATIONARY, g₂ flat)")
    print("C. VERDICT: g₂ (bar-even Vol) is MAXIMAL where c₃ (bar-odd CS) is FROZEN — the wall is "
          "quadrature. Corrects 'r frozen like c₃'. g₂ value = trefoil bar-even NZ coeff (#4319). No fit.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
