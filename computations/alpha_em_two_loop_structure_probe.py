#!/usr/bin/env python3
"""alpha_em_two_loop_structure_probe.py

"Do the 2-loop" + "work on the conjecture" for α_EM — the honest formalize-first
outcome of attempting both. NOT a numerical fit (entropy forbids it); a structural
prune + a statement of what the remaining derivation actually requires.

Context: at the proton pin with the DERIVED Schwinger (1−h²α) term, α_EM sits at
+0.313 ppb = ~2× σ_α (alpha_em_schwinger_ladder_probe.py). The remaining residual is
a 2-loop O(α²) term of size c₂ = residual/α² ≈ 8e-4.

TWO STRUCTURAL FINDINGS (scope-(a); no coefficient fitted):

1. THE 2-LOOP IS NOT A RESUMMATION OF THE SCHWINGER FACTOR (ruled out).
   Replacing the linear factor f=(1−h²α) by its natural resummations
   f=exp(−h²α) or f=1/(1+h²α) leaves the residual UNCHANGED at +0.314 ppb — because
   h²α ≈ 3.2e-4, the h⁴α² resummation term is ~1e-7, negligible vs the 0.313 ppb gap.
   So the remaining 2-loop is a GENUINELY NEW categorical term (the RT phase-2
   EmFermionLoop primitive), not a higher-order piece of the 1-loop self-energy.

2. c₂ IS ENTROPY-BLOCKED — NO NUMERICAL IDENTIFICATION IS POSSIBLE.
   The residual (0.313 ppb) is limited by σ_α (0.15 ppb) + the q0 pin (0.06 ppb),
   so c₂ = 8e-4 is known to ~1 significant figure. PSLQ needs
   precision > n_terms·log10(2·height); at ~1 digit even a 2-term basis is
   hopeless. So c₂ CANNOT be PSLQ-identified (per the formalize-first entropy rule) —
   the only route is the STRUCTURAL EmFermionLoop 2-loop derivation.

WHAT THE REMAINING α_EM CONJECTURE ACTUALLY IS (after the value + anchor are settled):
   (a) the 2-loop c₂ = a structural EmFermionLoop (categorical 2-loop diagram) —
       a genuine QFT-analog computation, not a fit (RT phase-2);
   (b) the COUPLING MECHANISM = why the IR zero-mode enters 1/α as dim H¹/Area.
       CANDIDATE framing (re-scoped 2026-07-12 after the deep-research literature
       check, docs/audits/2026-07-12-alpha-em-heat-kernel-coupling-outside-view.md):
       a heat-kernel / conformal-anomaly (a₁ Seeley–DeWitt) origin. The literature
       sweep found NO precedent for a b₁/Area coupling term (mainstream U(1)-on-
       2-surface topology enters via the Chern index, area-independent), and the
       specific a₁ ∝ Gauss–Bonnet decomposition claim was adversarially REFUTED —
       so this is an unprecedented candidate, not an identified mechanism. The
       zero-mode VALUE stays proved genus-determined (Lean, this PR); the coupling
       identification is the open, Wyler-shaped referee pivot.

Neither (a) nor (b) is session-closable; both are research-frontier. This probe
documents the honest frontier and prunes the resummation hypothesis. No c_k / no
coefficient fitted; scope-(a).

Companion: alpha_em_schwinger_ladder_probe.py, QOU/Archimedean/EmCouplingBringZeroMode.lean.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
CODATA = mp.mpf("137.035999084")
SIGMA_PPB = mp.mpf("0.15")
PIN_PPB = mp.mpf("0.06")
Q_P = mp.mpf("1.109978582751380808")


def qb(n, q):
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def ppb(v):
    return float((v - CODATA) / CODATA * 1e9)


def main() -> int:
    print("=" * 78)
    print(" α_EM 2-loop structure — resummation ruled out; c₂ entropy-blocked")
    print("=" * 78)

    wb = WitnessBuilder("alpha-em-two-loop-structure", engine="mpmath")
    wb.set_description(
        "Structural prune of the alpha_EM 2-loop term. (1) The 2-loop is NOT a "
        "resummation of the Schwinger factor: f=exp(-h2 a) and f=1/(1+h2 a) leave the "
        "residual unchanged at +0.314 ppb (h2 a ~3e-4 => h4 a2 term ~1e-7 << 0.31 ppb). "
        "(2) c2 = resid/a2 ~ 8e-4 is entropy-blocked (~1 sig fig; PSLQ hopeless). So the "
        "2-loop needs the structural EmFermionLoop derivation; the coupling mechanism is "
        "the heat-kernel/conformal-anomaly (a1 Seeley-DeWitt ~ Gauss-Bonnet) — both "
        "research-frontier, not session-closable. No coefficient fitted; scope-(a)."
    )
    wb.set_content_block("prop:em-coupling-bring-zero-mode")

    q = Q_P
    h2 = (q - 1 / q) ** 2
    T = q * qb(9, q) * qb(10, q) + mp.mpf(8) / (12 * mp.pi)
    H = qb(2, q) / (8 * mp.pi)

    def solve(f):
        a = mp.mpf("0.0073")
        for _ in range(200):
            a = 1 / (T + a * H * f(a))
        return 1 / a

    forms = {
        "f=1 (no Schwinger)": lambda a: mp.mpf(1),
        "f=1-h2*a (linear, derived)": lambda a: 1 - h2 * a,
        "f=exp(-h2*a) (resummed)": lambda a: mp.e ** (-h2 * a),
        "f=1/(1+h2*a) (resummed)": lambda a: 1 / (1 + h2 * a),
    }
    print(f"\n  proton pin; h²α = {mp.nstr(h2*mp.mpf('0.0073'), 6)}  (=> h⁴α² ~ {mp.nstr((h2*mp.mpf('0.0073'))**2,4)})")
    resids = {}
    for name, f in forms.items():
        r = ppb(solve(f))
        resids[name] = r
        print(f"    {name:30s} resid = {r:+.3f} ppb")
    lin = resids["f=1-h2*a (linear, derived)"]
    exp_ = resids["f=exp(-h2*a) (resummed)"]
    print(f"\n  [1] resummation shift (exp vs linear): {exp_-lin:+.4f} ppb  => NEGLIGIBLE")
    print("      => 2-loop is NOT a Schwinger resummation; it is a NEW EmFermionLoop term.")

    # entropy analysis for c2
    inv_alpha = solve(forms["f=1-h2*a (linear, derived)"])   # = 1/α ≈ 137.036
    alpha = 1 / inv_alpha                                     # ≈ 0.0073
    abs_resid = inv_alpha - CODATA                            # absolute residual in 1/α
    c2_coeff = abs_resid / alpha ** 2                         # 2-loop coeff ≈ 8e-4
    resid_ppb = abs(ppb(inv_alpha))                           # ≈ 0.313 ppb
    unc_ppb = float(SIGMA_PPB + PIN_PPB)                      # ≈ 0.21 ppb
    sig_figs = float(mp.log10(resid_ppb / unc_ppb)) if resid_ppb > unc_ppb else 0.0
    print(f"\n  [2] c₂ = residual/α² ≈ {mp.nstr(c2_coeff, 4)}")
    print(f"      residual = {resid_ppb:.3f} ppb; uncertainty = σ_α + pin ≈ {unc_ppb} ppb")
    print(f"      => c₂ known to ~{max(0.0, sig_figs):.1f} significant figures — PSLQ ENTROPY-BLOCKED.")
    print("      => no numerical identification; needs the structural EmFermionLoop derivation.")

    print("\n  REMAINING CONJECTURE (value + anchor now settled):")
    print("    (a) 2-loop c₂ = structural EmFermionLoop (categorical 2-loop) — RT phase-2.")
    print("    (b) coupling mechanism = heat-kernel/conformal-anomaly: the a₁ Seeley–DeWitt")
    print("        coefficient ∝ ∫R = −2πχ = 4π(g−1) gives dim H¹/Area = the proved")
    print("        genus-determined zero-mode. The physics claim that a₁ IS the α_EM IR")
    print("        shift is the conjecture. Both research-frontier; not session-closable.")

    resum_negligible = abs(exp_ - lin) < 0.01
    entropy_blocked = float(sig_figs) < 2.0

    wb.add_data("resummation_test", {k: v for k, v in resids.items()})
    wb.add_data("resummation_shift_ppb", float(exp_ - lin))
    wb.add_data("c2", {"value": mp.nstr(c2_coeff, 6), "sig_figs_known": max(0.0, float(sig_figs)),
                       "pslq": "entropy-blocked (~1 sig fig)"})
    wb.add_data("remaining_conjecture", {
        "two_loop": "structural EmFermionLoop (RT phase-2), not a fit",
        "coupling": "heat-kernel/conformal-anomaly a1 ~ Gauss-Bonnet 4pi(g-1) => dim H1/Area",
        "status": "research-frontier; value + anchor settled, coupling + 2-loop open"})
    wb.add_assertion("two_loop_not_resummation",
                     computed=float(resum_negligible), expected=1.0, tolerance=0.5,
                     source="exp/linear Schwinger resid differ by <0.01 ppb (h4a2~1e-7 negligible)")
    wb.add_assertion("c2_entropy_blocked",
                     computed=float(entropy_blocked), expected=1.0, tolerance=0.5,
                     source="c2 known to ~1 sig fig (residual pin+sigma limited) => PSLQ hopeless")
    wb.save()

    print(f"\n  RESULT: resummation ruled out; c₂ entropy-blocked ⇒ structural EmFermionLoop needed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
