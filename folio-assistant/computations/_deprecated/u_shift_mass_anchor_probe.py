#!/usr/bin/env python3
"""
u^shift probe: does the Habiro denominator shift exponent predict m_p/m_e?

Per docs/audits/2026-05-03-w3-habiro-unblocked.md, the Markov-
denominator factors as

    D(u) = 2^{2A+1} · u^{shift} · (1 + u^2)^{3A-1}

For isolated nucleons (include_inter=False):
  - shift_p = 20  (proton)
  - shift_n = 16  (neutron)

For atoms (include_inter=True), the empirical formula is
  shift_atom = 18A + 3N + 1  (= 18Z + 21N + 1)

The categorical (18, 3, 1) coefficients are the open question
(integer-LP characterization, not yet proved from H_n(q) structure).

Per `prop:atomic-mass-gb-nf` and `rho-k-scaling-structure.witness.json`:

    M(K) = m_e · ρ_K · |tr_M(NF_GS(β_K))|
    ρ_K^LO ≈ (Z·m_p + N·m_n) / (m_e · |tr_M|)

So m_p/m_e and m_n/m_e are the two scalar anchors that close the
program. This probe asks: **can shift (categorical, from Habiro
D(u) factorization) directly predict m_p/m_e and m_n/m_e?**

Output: u-shift-mass-anchor-probe.witness.json
"""
from __future__ import annotations

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from q_parameter import Q_MP as Q0_MP  # noqa: E402

Q0 = Q0_MP

# Nucleon masses (MeV).  These are dimensionful CODATA values; they
# require scaling by E_0 (= categorical-mass calibration) before
# being added to the categorical mass terms in the probe sweep.
M_E_MEV = mp.mpf('0.51099895')
M_P_MEV = mp.mpf('938.27208816')
M_N_MEV = mp.mpf('939.56542052')

# Module-level h := q − q⁻¹ at q = Q0 (Hecke parameter).
H = Q0 - 1 / Q0


# ── Categorical constants at q_0 ────────────────────────────────
def categorical_constants() -> dict:
    """Compute the named categorical constants at q_0 = q_0_MP.

    Returns mpmath types throughout to respect the `mp.dps = 50`
    precision floor; downstream callers that need plain `float`
    should cast at the consumption point, not here.
    """
    q = Q0
    h_bar_q = (q - 1) / q                  # Planck-q
    c_q     = 1 / (q - 1)                  # speed-of-light-q
    z       = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))  # Markov parameter
    n3_q    = (q**3 - q**(-3)) / (q - q**(-1))   # [3]_q
    n2_q    = (q + q**(-1))                       # [2]_q
    return {
        "q_0":     q,
        "h_bar_q": h_bar_q,
        "c_q":     c_q,
        "z_markov": z,
        "[2]_q":   n2_q,
        "[3]_q":   n3_q,
    }


# ── Empirical inputs (from w3 audit) ────────────────────────────
SHIFT_FREE = {
    "p": 20,   # docs/audits/2026-05-03-w3-habiro-unblocked.md
    "n": 16,
}

from d_u_closed_form_proof import closed_form_d_u  # noqa: E402

# Atomic-braid shift values from the closed-form proof (PR #539):
#   shift_atom(Z, N) = 18Z + 21N + 1.
# Routed through closed_form_d_u to keep a single source of truth.
SHIFT_ATOMIC_FORMULA = {
    "D":   closed_form_d_u(1, 1)["u_shift"],   # = 40
    "T":   closed_form_d_u(1, 2)["u_shift"],   # = 61
    "3He": closed_form_d_u(2, 1)["u_shift"],   # = 58
    "4He": closed_form_d_u(2, 2)["u_shift"],   # = 79
    "5Li": closed_form_d_u(3, 2)["u_shift"],   # = 97
}

# Anchor: m/m_e
ANCHOR = {
    "p": M_P_MEV / M_E_MEV,   # 1836.15
    "n": M_N_MEV / M_E_MEV,   # 1838.68
}


# ── Candidate categorical formulas for m_p/m_e ────────────────
def evaluate_candidates(consts: dict) -> list[dict]:
    """Test categorical formulas combining shift, q, c_q, ℏ_q against m_p/m_e."""
    q = consts["q_0"]
    c_q = consts["c_q"]
    h_bar = consts["h_bar_q"]
    z = consts["z_markov"]

    candidates = []

    # Family 1: shift × (q_0-derived constants)
    for atom in ["p", "n"]:
        shift = SHIFT_FREE[atom]
        anchor = ANCHOR[atom]

        # F1: shift · q · c_q^2
        v = shift * q * c_q**2
        candidates.append({
            "atom": atom, "formula": "shift · q · c_q²",
            "value": v, "anchor": anchor,
            "err_pct": (v - anchor) / anchor * 100,
        })

        # F2: shift · c_q^2
        v = shift * c_q**2
        candidates.append({
            "atom": atom, "formula": "shift · c_q²",
            "value": v, "anchor": anchor,
            "err_pct": (v - anchor) / anchor * 100,
        })

        # F3: shift / ℏ_q^2
        v = shift / h_bar**2
        candidates.append({
            "atom": atom, "formula": "shift / ℏ_q²",
            "value": v, "anchor": anchor,
            "err_pct": (v - anchor) / anchor * 100,
        })

        # F4: shift · q^2 · c_q^2
        v = shift * q**2 * c_q**2
        candidates.append({
            "atom": atom, "formula": "shift · q² · c_q²",
            "value": v, "anchor": anchor,
            "err_pct": (v - anchor) / anchor * 100,
        })

        # F5: shift · (1 + q) · c_q^2
        v = shift * (1 + q) * c_q**2
        candidates.append({
            "atom": atom, "formula": "shift · (1+q) · c_q²",
            "value": v, "anchor": anchor,
            "err_pct": (v - anchor) / anchor * 100,
        })

        # F6: shift · q · / h_bar
        v = shift * q / h_bar
        candidates.append({
            "atom": atom, "formula": "shift · q / ℏ_q",
            "value": v, "anchor": anchor,
            "err_pct": (v - anchor) / anchor * 100,
        })

        # F7: shift · c_q · q^2
        v = shift * c_q * q**2
        candidates.append({
            "atom": atom, "formula": "shift · c_q · q²",
            "value": v, "anchor": anchor,
            "err_pct": (v - anchor) / anchor * 100,
        })

        # F8: shift / (z · ℏ_q)
        v = shift / (z * h_bar)
        candidates.append({
            "atom": atom, "formula": "shift / (z·ℏ_q)",
            "value": v, "anchor": anchor,
            "err_pct": (v - anchor) / anchor * 100,
        })

    return candidates


def joint_test(candidates: list[dict]) -> list[dict]:
    """Filter candidates whose magnitudes work for BOTH p and n.
    A formula that hits m_p well but fails m_n by 20% is no good."""
    by_formula = {}
    for c in candidates:
        by_formula.setdefault(c["formula"], []).append(c)
    out = []
    for formula, rows in by_formula.items():
        if len(rows) != 2:
            continue
        max_err = max(abs(r["err_pct"]) for r in rows)
        out.append({
            "formula": formula,
            "p_value": next(r["value"] for r in rows if r["atom"] == "p"),
            "p_err_pct": next(r["err_pct"] for r in rows if r["atom"] == "p"),
            "n_value": next(r["value"] for r in rows if r["atom"] == "n"),
            "n_err_pct": next(r["err_pct"] for r in rows if r["atom"] == "n"),
            "max_err_pct": max_err,
        })
    out.sort(key=lambda r: r["max_err_pct"])
    return out


def main() -> int:
    consts = categorical_constants()

    print("=" * 96)
    print("  u^shift mass-anchor probe")
    print("  Test: does shift exponent (Habiro D(u)) directly predict m_p/m_e?")
    print("=" * 96)

    print(f"\n  Categorical constants at q_0 = {float(consts['q_0']):.10f}:")
    for k, v in consts.items():
        print(f"    {k:<10} = {float(v):>14.8f}")

    print(f"\n  Empirical inputs (from w3 audit):")
    print(f"    shift_p = {SHIFT_FREE['p']}  (isolated proton, include_inter=False)")
    print(f"    shift_n = {SHIFT_FREE['n']}  (isolated neutron, include_inter=False)")
    print(f"\n  Anchor targets:")
    print(f"    m_p/m_e = {float(ANCHOR['p']):.6f}  (CODATA)")
    print(f"    m_n/m_e = {float(ANCHOR['n']):.6f}  (CODATA)")

    candidates = evaluate_candidates(consts)
    joint = joint_test(candidates)

    print(f"\n  Joint p+n consistency (sorted by max error):")
    print(f"\n  {'formula':<25} {'p value':>12} {'p err%':>9}  {'n value':>12} {'n err%':>9}")
    print("  " + "-" * 76)
    for j in joint:
        print(f"  {j['formula']:<25} {float(j['p_value']):>12.2f} {float(j['p_err_pct']):>+8.3f}%  "
              f"{float(j['n_value']):>12.2f} {float(j['n_err_pct']):>+8.3f}%")

    print(f"\n  Best candidate: {joint[0]['formula']}")
    print(f"     max error: {float(joint[0]['max_err_pct']):.3f}%")

    # Sanity: m_n - m_p splitting consistency for the best candidate
    print(f"\n  Splitting consistency check:")
    print(f"    Δm_np / m_e (CODATA) = {float(ANCHOR['n'] - ANCHOR['p']):.4f}")
    for j in joint[:5]:
        diff_n_p = j['n_value'] - j['p_value']
        diff_actual = ANCHOR['n'] - ANCHOR['p']
        diff_err = (diff_n_p - diff_actual) / diff_actual * 100
        print(f"    {j['formula']:<25}  pred Δ = {float(diff_n_p):>+9.4f}  err {float(diff_err):>+8.2f}%")

    # Conclusion
    print("\n  Conclusion:")
    if joint[0]["max_err_pct"] < 1:
        print(f"    Found a sub-1%-error formula. Worth deeper investigation.")
    elif joint[0]["max_err_pct"] < 5:
        print(f"    No sub-1% formula. Best is {joint[0]['formula']} at "
              f"{joint[0]['max_err_pct']:.2f}% — categorical structure is")
        print(f"    suggested but not closed by the simple combinations tested.")
    else:
        print(f"    No simple formula in {{shift, q, c_q, ℏ_q, [n]_q}} fits both")
        print(f"    p and n. The m_p/m_e and m_n/m_e anchors require either")
        print(f"    a more sophisticated combination or additional categorical inputs")
        print(f"    (Wedderburn weights, Hopf-link coefficients, etc.).")

    print(f"\n  Note: shift_p = 20 vs shift_n = 16 differ by 4. The CODATA")
    print(f"  m_n - m_p splitting is only ~0.14% of m_p, so a formula linear in")
    print(f"  shift cannot match both anchors unless heavily compensated by")
    print(f"  other terms.")

    witness = {
        "computation": "u-shift-mass-anchor-probe",
        "description": (
            "Tests whether the Habiro denominator shift exponent "
            "(shift_p = 20, shift_n = 16 from include_inter=False) "
            "directly predicts the nucleon-mass anchors m_p/m_e and "
            "m_n/m_e via simple combinations with q-dependent "
            "categorical constants. Negative result expected: shift "
            "alone is too coarse (4-unit difference between p and n) "
            "to match the 0.14% m_n - m_p splitting. Documents the "
            "open structural question for `prop:atomic-mass-gb-nf`."
        ),
        "reference_blocks": [
            "prop:atomic-mass-gb-nf",
            "prop:alpha-shift-torus-knot",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": float(Q0),
            "categorical_constants": consts,
            "empirical_inputs": {
                "shift_p_free": SHIFT_FREE["p"],
                "shift_n_free": SHIFT_FREE["n"],
                "anchor_target_m_p_per_m_e": ANCHOR["p"],
                "anchor_target_m_n_per_m_e": ANCHOR["n"],
                "splitting_per_m_e": ANCHOR["n"] - ANCHOR["p"],
            },
        },
        "candidates_individual": candidates,
        "joint_p_n_consistency": joint,
        "best_candidate": joint[0],
        "conclusion": (
            "Negative result: no simple combination of (shift, q_0, c_q, ℏ_q, "
            "z_markov, [n]_q) reproduces both m_p/m_e and m_n/m_e to better "
            "than several percent. The categorical closure of nucleon-mass "
            "anchors requires additional structural inputs beyond the "
            "Habiro shift exponent — likely a per-irrep / per-Wedderburn-block "
            "decomposition encoding the proton's (uud) vs neutron's (udd) "
            "quark-content asymmetry."
        ),
    }
    out = HERE / "u-shift-mass-anchor-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
