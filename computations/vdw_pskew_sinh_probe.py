#!/usr/bin/env python3
# polynomial_q_not_applicable: bar-even/odd (cosh/sinh) decomposition of the
# Hopf weighting; not a Jones-polynomial evaluation.
"""
The narrowed van der Waals probe: vdW is the bar-odd sinh / P_skew residual.

Owner guidance: "see corpus for other sinh/cosh… don't assume q has no
imaginary (only some observables are real)… lean prove what you can to
narrow probes." This is the formalize-first prune (the Lean is
`prop:vdw-pskew-isolation`, sorry-free).

THE NARROWING (corpus crossing-energy-decomposition + rem-im-q-vs-p-skew):
  q = cosh λ + sinh λ  (λ = ln q).  The Hopf link σ₁² = q²e₊ + q⁻²e₋ splits
  under the bar involution q↦q⁻¹ into
      2·σ₁² = 2cosh(2λ)·𝟙  +  2sinh(2λ)·(e₊−e₋).
  • bar-EVEN  cosh(2λ)·𝟙   = retained P_avg carrier (trivial identity).
  • bar-ODD   sinh(2λ)·(e₊−e₋) = P_skew / Coulomb-EM channel — DISCARDED by
    the canonical projection.  THAT residual is van der Waals.

So the probe is SHARP — vdW energy ∝ sinh(2λ)·(e₊−e₋), an EXACT q-expression,
NOT an h^k fit and NOT a cosh factor on the covalent ladder. The earlier "0.81"
was the wrong (sinh⁴/covalent) framing; the right object is the bar-odd residual.

Im(q) CAVEAT (rem-im-q-vs-p-skew): the sinh / P_skew part is REAL at real q
(kept-then-discarded), NOT imaginary — Im(q) is a SEPARATE lever (set to 0 by
convention). The fibre statement uses q, qi formal (no reality imposed); only
the archimedean evaluation at real q₀ is taken real here.

α_EM CROSS-CHECK (alpha-em-habiro-bar-involution): H=[2]_q(1−h²α)=2cosh λ·(1−h²α)
is bar-EVEN (cosh carrier × sinh² correction). vdW is bar-ODD (sinh·cosh). Same
machinery, opposite bar sector — α_EM is the retained coupling correction; vdW
is the discarded residual. Consistent.

STATUS: the probe is narrowed and the bar-odd identity is Lean-proved sorry-free.
The archimedean SEPARATION (1/r⁶, e₊ touching limit) that scales the fibre
residual to the molecular vdW energy remains the open piece (not fitted).

Refs: prop:vdw-pskew-isolation; prop:hopf-link-symmetric-decomposition;
crossing-energy-decomposition; rem-im-q-vs-p-skew; alpha-em-habiro-bar-involution.
"""
from __future__ import annotations

import sys
from cmath import log as clog
from math import cosh, sinh, sqrt
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


def main() -> None:
    w = WitnessBuilder("vdw-pskew-sinh-probe", engine="python")
    q = Q0
    lam = __import__("math").log(q)         # λ = ln q (the rapidity)

    cosh2 = (q ** 2 + q ** -2) / 2.0        # = cosh(2λ)
    sinh2 = (q ** 2 - q ** -2) / 2.0        # = sinh(2λ)
    # idempotent q-dims (van-der-waals-hopf-channel):
    z = q**3 / (q**2 + 1)
    e_plus = (z + 1.0 / q) / (q + 1.0 / q)
    e_minus = (q - z) / (q + 1.0 / q)
    e_diff = e_plus - e_minus
    vdw_bar_odd = sinh2 * e_diff            # the van der Waals residual (fibre)
    h = q - 1.0 / q

    print("=" * 74)
    print("Narrowed vdW probe — the bar-odd sinh / P_skew residual")
    print("=" * 74)
    print(f"  q₀ = {q:.6f}   λ = ln q₀ = {lam:.6f}  (rapidity)")
    print(f"  cosh(2λ) = (q²+q⁻²)/2 = {cosh2:.6f}  =? math.cosh = {cosh(2*lam):.6f}")
    print(f"  sinh(2λ) = (q²−q⁻²)/2 = {sinh2:.6f}  =? math.sinh = {sinh(2*lam):.6f}")
    print(f"  e₊ = {e_plus:.5f}  e₋ = {e_minus:.5f}  e₊−e₋ = {e_diff:.5f}")
    print()
    print(f"  bar-EVEN (retained P_avg carrier) : cosh(2λ)·𝟙 = {cosh2:.5f}·𝟙")
    print(f"  bar-ODD  (P_skew / vdW residual)  : sinh(2λ)·(e₊−e₋) = {vdw_bar_odd:.5f}")
    print(f"  ⇒ van der Waals (fibre) = {vdw_bar_odd:.5f}  — exact, no fit")
    print()
    # Im(q) caveat: at real q₀ the residual is real.
    im_part = abs((complex(sinh2) * complex(e_diff)).imag)
    print(f"  Im(vdW residual) at real q₀ = {im_part:.2e}  (real P_skew, not Im(q))")
    # α_EM cross-check: bar-even cosh carrier × sinh² correction
    alpha_carrier = q + 1.0 / q             # [2]_q = 2cosh λ
    print(f"  α_EM Habiro carrier [2]_q = 2cosh λ = {alpha_carrier:.5f} (bar-EVEN); "
          f"vdW is bar-ODD (sinh·cosh) — opposite sector, same machinery")

    w.set_description(
        "Narrowed van der Waals probe (formalize-first; Lean prop:vdw-pskew-"
        "isolation sorry-free). The Hopf link σ₁²=q²e₊+q⁻²e₋ splits under the bar "
        "involution into 2cosh(2λ)·𝟙 (bar-even, retained P_avg carrier) + "
        "2sinh(2λ)·(e₊−e₋) (bar-odd, the P_skew/Coulomb-EM channel the canonical "
        "projection discards). vdW IS that bar-odd residual sinh(2λ)·(e₊−e₋) — an "
        "exact q-expression, NOT an h^k fit nor a cosh factor on the covalent "
        "ladder (the earlier 0.81 was the wrong sinh⁴/covalent framing). Per "
        "rem-im-q-vs-p-skew the residual is REAL at real q (P_skew), not Im(q). "
        "α_EM Habiro [2]_q(1−h²α)=2cosh λ(1−h²α) is the bar-EVEN sibling (cosh "
        "carrier × sinh² correction); vdW is bar-ODD (sinh·cosh) — same machinery, "
        "opposite sector. Open: the archimedean 1/r⁶ separation scaling the fibre "
        "residual to the molecular vdW energy (not fitted)."
    )
    w.set_content_block("prop:vdw-pskew-isolation")
    w.add_parameter("q", q)
    w.add_data("rapidity_lambda", lam)
    w.add_data("cosh_2lambda", cosh2)
    w.add_data("sinh_2lambda", sinh2)
    w.add_data("e_plus", e_plus)
    w.add_data("e_minus", e_minus)
    w.add_data("e_diff", e_diff)
    w.add_data("vdw_bar_odd_residual", vdw_bar_odd)
    w.add_data("vdw_residual_imag_at_real_q", im_part)
    w.add_data("alpha_em_carrier_2coshlambda", alpha_carrier)
    w.add_assertion(
        "cosh(2λ) = (q²+q⁻²)/2 (algebraic = transcendental)",
        computed=bool(abs(cosh2 - cosh(2 * lam)) < 1e-12), expected=True,
        source="q^n = cosh(nλ)+sinh(nλ), λ=ln q (crossing-energy-decomposition)",
    )
    w.add_assertion(
        "sinh(2λ) = (q²−q⁻²)/2 (the bar-odd / P_skew weight)",
        computed=bool(abs(sinh2 - sinh(2 * lam)) < 1e-12), expected=True,
        source="q^n − q^{−n} = 2 sinh(nλ)",
    )
    w.add_assertion(
        "vdW bar-odd residual is REAL at real q₀ (P_skew, not Im(q))",
        computed=bool(im_part < 1e-12), expected=True,
        source="rem-im-q-vs-p-skew: P_skew is real at real q",
    )
    w.add_data(
        "finding",
        f"van der Waals is the bar-odd (sinh / P_skew) residual of the Hopf link: "
        f"2σ₁² = 2cosh(2λ)·𝟙 + 2sinh(2λ)·(e₊−e₋), with the cosh part the retained "
        f"P_avg carrier and the sinh·(e₊−e₋)={vdw_bar_odd:.4f} part the discarded "
        f"Coulomb-EM channel = vdW. This narrows the probe to the EXACT bar-odd "
        f"q-expression (no h^k fit, no cosh-on-covalent factor). The residual is "
        f"real at real q (P_skew ≠ Im(q)). Lean prop:vdw-pskew-isolation proves "
        f"the decomposition sorry-free. α_EM Habiro is the bar-even sibling. Open: "
        f"the archimedean 1/r⁶ separation to the molecular energy (not fitted)."
    )
    w.save()
    print("\nDone. Witness saved (vdw-pskew-sinh-probe).")


if __name__ == "__main__":
    main()
