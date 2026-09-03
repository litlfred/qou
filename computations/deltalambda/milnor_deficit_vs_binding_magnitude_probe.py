#!/usr/bin/env python3
"""milnor_deficit_vs_binding_magnitude_probe.py — is the Milnor deficit D_A the binding MAGNITUDE,
or only its structure? A measurement (qou-v7ro × qou-brng).

The ∀A recursion `D_{A+1}=−h²(h²+2)D_A` is proved (audit
2026-08-30-milnor-recursion-forall-A-PROVED.md). The qou-brng arc separately proved the binding
MAGNITUDE handle `binding = −log I` (interaction free energy; `QOU.Mass.ArchimedeanTraceBridge`),
with the coordination count `z = A−1` (so binding RISES with A). This probe measures whether the
deficit `D_A` is that magnitude — the claim recorded in the milnor-brunnian-deficit coordination
ledger is "D_A supplies structure (Milnor order, sign/parity), NOT the binding magnitude."

Measured at the proton-pin q₀ (owner default for compute), exact mpmath (no float64):

  D_A(h) = (−1)^{A−3} h^{2(A−1)} (h²+2)^{A−3} (h²+3)/(h²+4),   h = q₀ − 1/q₀.

Two trends decide it:
  • |D_A| vs A                       — the deficit's A-dependence.
  • empirical B/A/m_N (÷ ℏ_q²) vs A  — the binding fraction (from the qou-brng R3 table).

If |D_A| FALLS with A while B/A RISES, D_A is not the binding magnitude — it is the Milnor
order/parity structure, exactly as the ledger claims. This substantiates that claim with numbers
rather than asserting it. NO wiring, NO fit; scope-(a) measurement.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str((HERE / ".." / ".." / "tools" / "qou-substrate" / "python").resolve()))
from qou_substrate.constants import Q_50_DIGIT_STR  # proton-pin q₀, 50-digit string  # noqa: E402

mp.mp.dps = 50
q0 = mp.mpf(Q_50_DIGIT_STR)
h = q0 - 1 / q0
h2 = h ** 2
hbarq = 1 - 1 / q0            # ℏ_q = 1 − q₀⁻¹
hbarq2 = hbarq ** 2


def deficit_closed(A: int) -> mp.mpf:
    """D_A(h) = (−1)^{A−3} h^{2(A−1)} (h²+2)^{A−3} (h²+3)/(h²+4)."""
    k = A - 3
    return (mp.mpf(-1)) ** k * h ** (2 * (A - 1)) * (h2 + 2) ** k * (h2 + 3) / (h2 + 4)


def main():
    # deficit at q0 for A = 3..8
    deficits = {}
    for A in range(3, 9):
        D = deficit_closed(A)
        deficits[A] = D

    # empirical binding fraction B/A/m_N ÷ ℏ_q² (from qou-brng R3 table, 2026-08-30-brng-residuals-worked.md)
    # these are recorded empirical AME/CODATA ratios, carried here only to compare the TREND.
    binding_frac_over_hbarq2 = {4: mp.mpf("0.767"), 40: mp.mpf("0.928"),
                                56: mp.mpf("0.954"), 62: mp.mpf("0.954"),
                                120: mp.mpf("0.923"), 238: mp.mpf("0.821")}

    # trend tests
    absD = {A: abs(deficits[A]) for A in deficits}
    deficit_falls = all(absD[A + 1] < absD[A] for A in range(3, 8))
    # binding fraction rises then falls (peak ~A=60); over the light range 4->56 it RISES
    bf = binding_frac_over_hbarq2
    binding_rises_light = bf[4] < bf[40] < bf[56]
    sign_alternates = all(mp.sign(deficits[A + 1]) == -mp.sign(deficits[A]) for A in range(3, 8))

    res = {
        "q0_pin": "proton (owner default)",
        "q0": mp.nstr(q0, 20),
        "h": mp.nstr(h, 20),
        "h2": mp.nstr(h2, 20),
        "hbarq2": mp.nstr(hbarq2, 20),
        "deficit_D_A_at_q0": {str(A): mp.nstr(deficits[A], 12) for A in deficits},
        "abs_deficit": {str(A): mp.nstr(absD[A], 12) for A in absD},
        "deficit_ratio_A_to_Ap1": {f"{A}->{A+1}": mp.nstr(deficits[A + 1] / deficits[A], 12)
                                   for A in range(3, 8)},
        "deficit_recursion_factor_-h2(h2+2)": mp.nstr(-h2 * (h2 + 2), 12),
        "empirical_binding_frac_over_hbarq2": {str(A): mp.nstr(bf[A], 6) for A in bf},
        "deficit_magnitude_FALLS_with_A": bool(deficit_falls),
        "binding_fraction_RISES_with_A_light": bool(binding_rises_light),
        "deficit_sign_alternates": bool(sign_alternates),
    }

    # the verdict
    opposite_trends = deficit_falls and binding_rises_light
    res["opposite_trends"] = bool(opposite_trends)
    res["verdict"] = (
        "MEASURED: D_A is the Milnor STRUCTURE, not the binding magnitude. At the proton q₀, "
        f"|D_A| falls geometrically (ratio per step = −h²(h²+2) = {mp.nstr(-h2*(h2+2),8)}, |·|<1) "
        "and its sign alternates as (−1)^{A−3} — the deficit is a rapidly-decaying, sign-carrying "
        "order marker. The empirical binding fraction B/A/m_N RISES with A over the light range "
        "(0.767→0.954·ℏ_q², ⁴He→⁵⁶Fe) via the coordination count z=A−1 (qou-brng, binding=−log I). "
        "The two objects have OPPOSITE A-dependence, so D_A cannot be the binding magnitude; it "
        "carries the Milnor order/parity. This substantiates with numbers the coordination-ledger "
        "claim that a MeV binding number from D_A would be a fit (the magnitude lives in the "
        "qou-brng coordination free energy, not in D_A)."
        if opposite_trends else
        "UNEXPECTED: trends do not oppose — re-examine before updating the ledger claim."
    )

    out = {
        "q0Anchor": "proton",
        "q0AnchorReason": (
            "Evaluates at the PROTON pin. q0 enters through "
            "q_parameter.Q_50_DIGIT_STR, which resolves to the proton "
            "anchor (1.1099785827513808075...) because this stem is not "
            "listed under ideal_muon; proton is the standing default for "
            "compute per the 2026-08-07 owner directive. The stem IS "
            "declared physical_proton in "
            "computations/q0_anchor_manifest.json, and that declaration "
            "cannot stamp this witness: the manifest is read inside "
            "WitnessBuilder.build(), and this producer hand-rolls its "
            "witness and never enters build(). Hence the declaration "
            "here, which is the only route that reaches the file."),
        "computation": "milnor-deficit-vs-binding-magnitude",
        "scriptFile": "milnor_deficit_vs_binding_magnitude_probe.py",
        "engine": "python-mpmath-exact",
        "free_parameters": 0,
        "q0_anchor": "physical_proton",
        "description": (
            "Measures the proved Milnor deficit D_A at the proton q₀ (A=3..8) against the empirical "
            "binding fraction trend, to test whether D_A is the binding magnitude. Finds OPPOSITE "
            "A-dependence (|D_A| falls geometrically + sign alternates; B/A rises via coordination), "
            "so D_A is the Milnor order/parity structure, not the magnitude — substantiating the "
            "milnor-brunnian-deficit coordination-ledger claim. No fit, no wiring; scope-(a). "
            "mpmath dps=50, zero float64."
        ),
        "results": res,
    }
    # Hand-rolled dump: build() never runs, so the manifest cannot stamp
    # this one. Ask for the anchor with the same precedence q_parameter
    # uses at compute time (env var > manifest stem > proton) rather than
    # hardcoding a pin this run may not have used.
    from qou_substrate.witness import resolve_q0_anchor as _rq0  # noqa: PLC0415
    _q0a, _q0v = _rq0(__file__)
    out["q0Anchor"] = _q0a
    if _q0v:
        out["q0Value"] = _q0v
    (HERE / "milnor-deficit-vs-binding-magnitude.witness.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(res, indent=1))
    print("wrote milnor-deficit-vs-binding-magnitude.witness.json")
    assert opposite_trends, "trend measurement did not confirm opposite dependence"


if __name__ == "__main__":
    main()
