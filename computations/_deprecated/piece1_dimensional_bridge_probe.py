#!/usr/bin/env python3
"""
Piece 1: dimensional-bridge investigation.

The graded ρ_K expansion has THREE dimensional anchors:
  - E_0 (Hecke-energy quantum, proton-calibrated; ≈ 174.3 MeV/Hecke)
  - α  = m_e · 8G (Borromean binding scale; ≈ 3.74 MeV)
  - m_e (electron rest energy; ≈ 0.511 MeV)

Empirical ratios at q_0:
  E_0 / α ≈ 46.6 (factor of ~47 unaccounted)
  E_0 / m_e ≈ 341 (the "341" the user spotted earlier)
  α / m_e = 8G ≈ 7.33 (proven via Borromean volume)

This probe tries to express E_0/α structurally in terms of the
categorical constants at q_0 (q, c_q, ℏ_q, [n]_q, weights, etc.).

Closed form for tr_M(proton) from PR #546 hoefsmit_symbolic.py:
  tr_M(p) = (q^20 + q^18 + 2q^12 - 2q^8 - q^2 - 1) / (12 q^10)
  leading coefficient: -1/12 EXACTLY

If E_0 = m_p / |tr_M(p)|_q0_subset, then E_0 = m_p · 12 / |coefficient_polynomial|.
The factor of 12 is intriguing because:
  12 = 2 · 3! = 2 · |S_3|        (symmetric group order)
  12 = 4 · 3 = 2² · 3              (could be related to dim sym + dim std)
  12 = 1 + 4 + 4 + 1 + ... ? (Wedderburn related)

Output: piece1-dimensional-bridge.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from q_parameter import Q_MP  # noqa: E402

q = Q_MP

M_E = mp.mpf("0.51099895")
M_P = mp.mpf("938.27208816")
G_CATALAN = mp.catalan
ALPHA = M_E * 8 * G_CATALAN

# Categorical constants at q_0
h_bar_q = (q - 1) / q
c_q     = 1 / (q - 1)
z       = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
n2_q    = q + 1 / q
n3_q    = (q ** 3 - q ** -3) / (q - 1 / q)
nf3     = n2_q * n3_q  # [3]_q! (with [1]_q = 1)


def closed_form_tr_M_proton(q_val: mp.mpf) -> mp.mpf:
    """tr_M(proton) closed form from PR #546:
      (q^20 + q^18 + 2q^12 - 2q^8 - q^2 - 1) / (12 q^10)
    """
    q = q_val
    num = q**20 + q**18 + 2*q**12 - 2*q**8 - q**2 - 1
    den = 12 * q**10
    return num / den


def main() -> int:
    print("=" * 96)
    print("  Piece 1: dimensional bridge E_0 ↔ α at q_0")
    print("=" * 96)

    # Closed-form tr_M(p) at q_0
    tr_M_p_closed = closed_form_tr_M_proton(q)
    abs_tr_M_p_closed = abs(tr_M_p_closed)

    # Reference numerical |tr_M(p)| from atomic-tr-m-mpfr-50dps
    ref_path = HERE / "atomic-tr-m-mpfr-50dps.witness.json"
    ref_data = json.load(open(ref_path))
    abs_tr_M_p_ref = None
    for r in ref_data["results"]:
        if r["atom"] == "proton":
            abs_tr_M_p_ref = abs(mp.mpf(r["tr_M_at_q0_50dps"]))
            break

    print(f"\n  Closed-form |tr_M(p)| at q_0 (PR #546):     {float(abs_tr_M_p_closed):.10f}")
    print(f"  Reference |tr_M(p)| at q_0 (50dps witness):  {float(abs_tr_M_p_ref):.10f}")
    if abs_tr_M_p_ref:
        ratio = abs_tr_M_p_ref / abs_tr_M_p_closed
        print(f"  Ratio (ref / closed-form):                   {float(ratio):.6f}")
        if abs(float(ratio) - 2.0) < 0.001:
            print(f"  → factor-of-2 normalisation mismatch flagged in #546")

    # Compute E_0 candidates
    E_0_full = M_P / abs_tr_M_p_ref           # using full reference (with all six terms, not just tr_M)
    E_0_bare = M_P / abs_tr_M_p_closed         # using bare tr_M (closed form)
    print(f"\n  E_0 candidates:")
    print(f"    E_0 = m_p / |tr_M(p)|_ref       = {float(E_0_full):.4f} MeV/Hecke")
    print(f"    E_0 = m_p / |tr_M(p)|_closed    = {float(E_0_bare):.4f} MeV/Hecke")

    # Reference E_0 from six-term theorem (proton calibration with all 5 Hecke terms)
    E_0_six_term = mp.mpf("174.30")  # from paper-six-term-isotope-sweep witness

    print(f"    E_0 = six-term proton calib    = {float(E_0_six_term):.4f} MeV/Hecke (T_1+T_2+T_3+T_4+T_5)")

    # Ratios
    print(f"\n  Dimensional ratios at q_0:")
    print(f"    α = m_e · 8G                    = {float(ALPHA):.6f} MeV")
    print(f"    E_0_six_term / α                 = {float(E_0_six_term / ALPHA):.4f}")
    print(f"    E_0_six_term / m_e               = {float(E_0_six_term / M_E):.4f}")
    print(f"    E_0_six_term / (12 m_e)          = {float(E_0_six_term / (12 * M_E)):.4f}")
    print(f"    α / m_e (= 8G)                   = {float(ALPHA / M_E):.4f}")
    print(f"    m_p / m_e                        = {float(M_P / M_E):.4f}")
    print(f"    m_p / (m_e · 12)                 = {float(M_P / (12 * M_E)):.4f}")
    print(f"    m_p / α                          = {float(M_P / ALPHA):.4f}")
    print(f"    m_p / (α · 12)                   = {float(M_P / (12 * ALPHA)):.4f}")

    # Categorical constants
    print(f"\n  Categorical constants at q_0 = {float(q):.10f}:")
    print(f"    [2]_q                  = {float(n2_q):.6f}")
    print(f"    [3]_q                  = {float(n3_q):.6f}")
    print(f"    [3]_q!                  = {float(nf3):.6f}")
    print(f"    z                      = {float(z):.6f}")
    print(f"    z²                     = {float(z**2):.6f}")
    print(f"    h_bar_q                = {float(h_bar_q):.6f}")
    print(f"    c_q = 1/(q-1)          = {float(c_q):.6f}")
    print(f"    c_q²                   = {float(c_q**2):.6f}")

    # Try to express E_0/α as a categorical formula
    target_E0_alpha = float(E_0_six_term / ALPHA)
    target_mp_me = float(M_P / M_E)
    print(f"\n  Targets:")
    print(f"    E_0 / α = {target_E0_alpha:.4f}")
    print(f"    m_p / m_e = {target_mp_me:.4f}")

    # Candidate formulas
    candidates = {
        "[3]_q!^2": float(nf3 ** 2),
        "12 · [3]_q":  float(12 * n3_q),
        "12 · [2]_q":  float(12 * n2_q),
        "[2]_q · c_q²": float(n2_q * c_q ** 2),
        "[3]_q · c_q":  float(n3_q * c_q),
        "[3]_q · c_q²": float(n3_q * c_q ** 2),
        "c_q² + 2[3]_q²": float(c_q ** 2 + 2 * n3_q ** 2),
        "12 / h_bar_q":  float(12 / h_bar_q),
        "8G · [3]_q":   float(8 * G_CATALAN * n3_q),
        "8G · 6":       float(8 * G_CATALAN * 6),  # 6 = |S_3|
        "8G · 12":      float(8 * G_CATALAN * 12),
        "1 / h_bar_q":   float(1 / h_bar_q),
        "1 / h_bar_q²":  float(1 / h_bar_q ** 2),
        "(c_q²+1)²":    float((c_q ** 2 + 1) ** 2),
        "c_q · [2]_q · [3]_q": float(c_q * n2_q * n3_q),
        "c_q² · [3]_q":  float(c_q ** 2 * n3_q),
    }

    print(f"\n  Candidate categorical formulas for E_0/α = {target_E0_alpha:.4f}:")
    print(f"  {'formula':<28} {'value':>14}  {'err vs E_0/α %':>14}")
    print("  " + "-" * 60)
    matches = []
    for name, val in sorted(candidates.items(), key=lambda x: abs(x[1] - target_E0_alpha)):
        err = (val - target_E0_alpha) / target_E0_alpha * 100
        marker = " ★" if abs(err) < 5 else ""
        print(f"  {name:<28} {val:>14.4f}  {err:>+14.3f}%{marker}")
        if abs(err) < 5:
            matches.append({"formula": name, "value": val, "err_pct": err})

    print(f"\n  Candidate categorical formulas for m_p/m_e = {target_mp_me:.4f}:")
    candidates_mp = {
        "12 · 153": 12 * 153,
        "12 · c_q²": float(12 * c_q ** 2),
        "12 · [3]_q²": float(12 * n3_q ** 2),
        "(c_q · [2]_q)² · 12 / (c_q²)": float((c_q * n2_q) ** 2 * 12 / c_q ** 2),
        "8G · c_q²": float(8 * G_CATALAN * c_q ** 2),
        "(8G)² · c_q²": float((8 * G_CATALAN) ** 2 * c_q ** 2),
        "1/h_bar_q² · 18": float(18 / h_bar_q ** 2),  # since 1836 ≈ 18 · 102
        "1/h_bar_q² · [2]_q · 9": float(9 * n2_q / h_bar_q ** 2),
    }
    print(f"  {'formula':<28} {'value':>14}  {'err vs m_p/m_e %':>16}")
    print("  " + "-" * 62)
    for name, val in sorted(candidates_mp.items(), key=lambda x: abs(x[1] - target_mp_me)):
        err = (val - target_mp_me) / target_mp_me * 100
        marker = " ★" if abs(err) < 1 else ""
        print(f"  {name:<28} {val:>14.4f}  {err:>+16.3f}%{marker}")

    print(f"\n  Conclusion:")
    if matches:
        best = matches[0]
        print(f"    Best fit for E_0/α: {best['formula']} → {best['value']:.4f}")
        print(f"    Error: {best['err_pct']:+.3f}%")
        print(f"    Closer scrutiny needed; this is suggestive, not derived.")
    else:
        print(f"    No simple closed form fits within 5%. The factor 46.6")
        print(f"    likely involves additional structure (Habiro residue,")
        print(f"    Plancherel weights, or higher-order q-corrections).")

    witness = {
        "computation": "piece1-dimensional-bridge",
        "description": (
            "Piece 1 of the open functional-form problem: structural "
            "investigation of the dimensional bridge E_0 ↔ α = m_e·8G. "
            "Tests categorical formulas (combinations of [n]_q, c_q, "
            "ℏ_q, weights) against the empirical ratio E_0/α ≈ 46.6 "
            "and m_p/m_e ≈ 1836.15. Closed-form tr_M(proton) from PR "
            "#546 (leading coefficient -1/12) provides the categorical "
            "anchor. The factor of 12 in the denominator is suggestive "
            "of |S_3| · 2 = 12 or [2]_q · [3]_q normalisation."
        ),
        "reference_blocks": [
            "prop:rho-k-graded-expansion",
            "prop:atomic-mass-gb-nf",
            "prop:hecke-branching-trace-decomposition",
            "prop:binding-scale-catalan",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": float(q),
            "m_e_MeV": float(M_E),
            "m_p_MeV": float(M_P),
            "alpha_MeV": float(ALPHA),
        },
        "targets": {
            "E_0_alpha_ratio": target_E0_alpha,
            "m_p_m_e_ratio": target_mp_me,
        },
        "categorical_constants": {
            "h_bar_q": float(h_bar_q),
            "c_q": float(c_q),
            "z": float(z),
            "[2]_q": float(n2_q),
            "[3]_q": float(n3_q),
            "[3]_q!": float(nf3),
        },
        "candidate_formulas_E0_alpha": candidates,
        "matches_within_5pct_E0_alpha": matches,
        "candidate_formulas_mp_me": candidates_mp,
    }
    out = HERE / "piece1-dimensional-bridge.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
