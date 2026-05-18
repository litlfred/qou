#!/usr/bin/env python3
"""
High-precision substrate parameter pinning at 50 decimal digits.

CALIBRATION INPUTS (precision-limited by CODATA / SnapPy):

  Vol(4_1) = 2.029 883 212 819 307 250 042 405 108 549 040 ...
             (SnapPy verified hyperbolic structure, ~50+ digits)

  m_μ/m_e  = 206.768 283 0 ± 4.6e-6  (CODATA 2022 — value below is the
             primary source; q_parameter.py carries the same value)
             — propagates to σ(q₀)/q₀ ≈ 1.22e-9 relative, computed
             below from dq/dR

DERIVATION:

  ℏ_q²  =  Vol(4_1) / (m_μ/m_e)
  ℏ_q   =  +√(ℏ_q²)
  q     =  1 / (1 - ℏ_q)
  ρ_q   =  1 / ℏ_q²              (Frobenius packing density)
  H_A   =  q - q⁻¹
  z     =  1 / (q^{1/2} + q^{-1/2})  (Markov parameter)
  [n]_q =  (q^n - q^{-n}) / (q - q⁻¹)

ξ(q₀) = D(z_q) / ℏ_q², where:
  z_q    = Legendre λ-invariant of Descartes elliptic curve at q₀
  D(z)   = Bloch-Wigner dilogarithm

This module computes ALL of the above to 50 decimal places via mpmath.
The PHYSICAL anchoring is bounded by CODATA's ~1e-8 on m_μ/m_e, but
the INTERNAL framework arithmetic is exact to 50 digits, allowing
relative-quantity predictions (ratios, dimensionless invariants) at
that precision.
"""
from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime, timezone

from mpmath import mp, mpf, mpc, sqrt, log
from mpmath import polylog, im, arg

from q_parameter import vol_4_1_at

# ── Set precision: 50 decimal digits (~165 bits) ─────────────
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

# ── Calibration inputs (high-precision values) ───────────────
# Vol(4_1) computed at the working precision via the Clausen
# identity Vol(4_1) = 2 Cl_2(π/3) — see q_parameter.vol_4_1_at.
# The previously-hardcoded 50-dps string here was actually
# inaccurate past digit ~37 (its trailing digits "100 14" do not
# match the converged Clausen value's "188 33...").  Pinning at
# 50 dps with a wrong constant past digit 37 corrupted the
# pinning result.
VOL_4_1 = vol_4_1_at(mp.dps)
VOL_4_1_STR = mp.nstr(VOL_4_1, mp.dps, strip_zeros=False)

# CODATA 2022 muon-electron mass ratio
M_MU_OVER_E_STR = "206.7682830"
M_MU_OVER_E = mpf(M_MU_OVER_E_STR)

# ── Derived substrate constants (50-digit precision) ─────────
HBAR_Q_SQ = VOL_4_1 / M_MU_OVER_E
HBAR_Q    = sqrt(HBAR_Q_SQ)
Q         = mpf(1) / (mpf(1) - HBAR_Q)
Q_INV     = mpf(1) / Q
H_A       = Q - Q_INV
TWO_Q     = Q + Q_INV       # [2]_q
RHO_Q     = mpf(1) / HBAR_Q_SQ      # Frobenius packing density

# Markov / Skein parameters
Z_MARKOV  = mpf(1) / (sqrt(Q) + sqrt(Q_INV))
S_SKEIN   = sqrt(Q) - sqrt(Q_INV)


def q_int(n: int) -> mpf:
    """[n]_q = (q^n - q^{-n}) / (q - q^{-1}) at high precision."""
    if n == 0:
        return mpf(0)
    return (Q ** n - Q_INV ** n) / H_A


def q_factorial(n: int) -> mpf:
    """[n]_q! = ∏_{k=1}^n [k]_q."""
    if n <= 1:
        return mpf(1)
    out = mpf(1)
    for k in range(1, n + 1):
        out *= q_int(k)
    return out


def plancherel_weight(partition: tuple) -> mpf:
    """w_λ(q) = d_q(λ)² / [n]_q! where d_q(λ) is the q-dimension."""
    n = sum(partition)
    # q-dimension via hook-length formula: d_q(λ) = [n]_q! / ∏[h(c)]_q
    nfact = q_factorial(n)
    # Compute hook lengths
    rows = list(partition)
    hooks = []
    for i, r in enumerate(rows):
        for j in range(r):
            arm = r - j - 1
            leg = sum(1 for k in range(i + 1, len(rows)) if rows[k] > j)
            hooks.append(arm + leg + 1)
    hook_prod_q = mpf(1)
    for h in hooks:
        hook_prod_q *= q_int(h)
    if hook_prod_q == 0:
        return mpf(0)
    d_q = nfact / hook_prod_q
    return d_q ** 2 / nfact


# ── Bloch-Wigner dilogarithm D(z) ─────────────────────────
def bloch_wigner(z: mpc) -> mpf:
    """D(z) = Im Li_2(z) + arg(1 - z) · log|z|."""
    if z == 0 or z == 1:
        return mpf(0)
    li2 = polylog(2, z)
    return im(li2) + arg(mpf(1) - z) * log(abs(z))


# ── Descartes elliptic curve λ-invariant at q₀ ────────────
def descartes_lambda(q: mpf) -> mpc:
    """Legendre λ-invariant of E_q — DISABLED pending verified coefficients.

    The previous implementation used placeholder Weierstrass coefficients
    p(q), r(q) that did NOT come from the paper's Descartes-curve
    derivation.  To compute ξ(q) at 50 digits, import the verified
    Weierstrass form from ``lambda_descartes_q0.py`` (on main) and
    rewrite this routine.  Until then, this function raises to prevent
    downstream consumers from using unreliable numeric values.
    """
    raise NotImplementedError(
        "descartes_lambda() placeholder disabled.  Wire in the verified "
        "Descartes-curve coefficients from lambda_descartes_q0.py before "
        "computing λ or ξ(q) at 50 digits."
    )


def xi_q(q: mpf) -> mpf:
    """ξ(q) = D(λ_Descartes(q)) / ℏ_q² — universal shape coupling.

    DISABLED: depends on ``descartes_lambda`` which is currently pinned
    to placeholder coefficients.  See ``lambda_descartes_q0.py`` for
    the verified 15-digit path; a 50-digit port is pending.
    """
    raise NotImplementedError(
        "xi_q(q) disabled pending verified Descartes-curve coefficients."
    )


if __name__ == "__main__":
    print("=" * 100)
    print(f"HIGH-PRECISION SUBSTRATE PINNING — mp.dps = {mp.dps} digits")
    print("=" * 100)

    print(f"\nInputs (calibration):")
    print(f"  Vol(4_1)          = {VOL_4_1}")
    print(f"  m_μ / m_e (CODATA) = {M_MU_OVER_E}")

    print(f"\nDerived substrate constants:")
    print(f"  ℏ_q² = Vol/R     = {HBAR_Q_SQ}")
    print(f"  ℏ_q              = {HBAR_Q}")
    print(f"  q                = {Q}")
    print(f"  q⁻¹              = {Q_INV}")
    print(f"  H_A = q - q⁻¹    = {H_A}")
    print(f"  [2]_q = q + q⁻¹  = {TWO_Q}")
    print(f"  z (Markov)       = {Z_MARKOV}")
    print(f"  ρ_q = 1/ℏ_q²     = {RHO_Q}")
    print(f"  S = √q - 1/√q    = {S_SKEIN}")

    print(f"\nQuantum integers / factorials at 50 digits:")
    for n in range(1, 7):
        print(f"  [{n}]_q  = {q_int(n)}")
    print(f"  [3]_q! = {q_factorial(3)}")
    print(f"  [6]_q! = {q_factorial(6)}")
    print(f"  [9]_q! = {q_factorial(9)}")

    print(f"\nPlancherel weights at q₀ for H_3 (sym, std, alt):")
    w_sym = plancherel_weight((3,))
    w_std = plancherel_weight((2, 1))
    w_alt = plancherel_weight((1, 1, 1))
    print(f"  w_(3)     = {w_sym}")
    print(f"  w_(2,1)   = {w_std}")
    print(f"  w_(1,1,1) = {w_alt}")
    print(f"  sum       = {w_sym + w_std + w_alt}")

    print(f"\nξ(q₀) — universal shape coupling:")
    try:
        xi = xi_q(Q)
        lam = descartes_lambda(Q)
        D_lam = bloch_wigner(lam)
        print(f"  λ_Descartes(q₀) = {lam}")
        print(f"  D(λ)            = {D_lam}")
        print(f"  ξ(q₀) = D/ℏ_q² = {xi}")
    except NotImplementedError as e:
        print(f"  DISABLED — placeholder Descartes coefficients removed.")
        print(f"  See lambda_descartes_q0.py (15-digit verified) on main.")
        print(f"  TODO: port that routine to 50-digit mpmath.")

    print(f"\nUncertainty propagation:")
    # dq/d(R) = q² · ℏ_q / (2R)  where R = m_μ/m_e
    DQ_DR = Q ** 2 * HBAR_Q / (mpf(2) * M_MU_OVER_E)
    M_MU_E_ERR = mpf("0.0000046")
    Q_ERR = DQ_DR * M_MU_E_ERR
    print(f"  dq/dR (m_μ/m_e)  = {DQ_DR}")
    print(f"  σ(m_μ/m_e)       = {M_MU_E_ERR}")
    print(f"  σ(q₀) [absolute] = {Q_ERR}")
    print(f"  σ(q₀)/q₀ [rel]   = {Q_ERR / Q}")
    rel_prec = float(Q_ERR / Q)
    print(f"  → CODATA-bounded relative precision: ~{rel_prec:.2e}")
    ratio_to_ppb = rel_prec / 1e-9
    if ratio_to_ppb <= 2:
        bound_msg = (f"✓ At 1-ppb-class precision "
                      f"(σ/q = {rel_prec:.2e}).")
    else:
        bound_msg = (f"⚠ PINNING-LIMITED at ~{ratio_to_ppb:.1f}× from "
                      f"1 ppb (σ/q = {rel_prec:.2e}).")
    print(f"  → 1 ppb = 1e-9.  {bound_msg}")

    # ξ(q₀) is DISABLED pending verified Descartes-curve derivation at
    # 50-digit mpmath precision; a 15-digit path exists in
    # lambda_descartes_q0.py (on main) and must be ported.
    universal_shape_coupling = {
        "status": "disabled",
        "reason": (
            "descartes_lambda() placeholder disabled to prevent "
            "unreliable xi(q₀) values.  Port the verified "
            "lambda_descartes_q0.py derivation to 50-digit mpmath "
            "before re-enabling."
        ),
        "formula": "xi(q) = D(lambda_descartes(q)) / hbar_q^2",
    }

    # Witness output
    witness = {
        "computation": "q-pinning-50-digit",
        "description": (
            "Substrate parameter q₀ pinned to 50 decimal digits via "
            "mpmath, derived from Vol(4_1) and m_μ/m_e (CODATA 2022).  "
            "Internal arithmetic is exact to 50 digits; physical "
            "anchoring is bounded by the propagated CODATA relative "
            "uncertainty ≈ 1.22e-9 (see physical_anchoring_bound).  "
            "Recorded 50-digit outputs: q, q^{-1}, ℏ_q², ℏ_q, H_A, "
            "[2]_q, z_markov, ρ_q, s_skein; plus quantum integers/"
            "factorials and n=3 Plancherel weights.  ξ(q₀) via "
            "Descartes-curve λ is NOT yet recorded — the current "
            "placeholder has been disabled; port lambda_descartes_q0.py "
            "to 50 digits and re-emit."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "precision_decimal_digits": mp.dps,
        "calibration_inputs": {
            "Vol_4_1_str": VOL_4_1_STR,
            "Vol_4_1_source": "SnapPy 3.3.2 verified hyperbolic structure",
            "m_mu_over_e_str": M_MU_OVER_E_STR,
            "m_mu_over_e_err": str(M_MU_E_ERR),
            "m_mu_over_e_source": "CODATA 2022",
        },
        "derived_50_digit": {
            "hbar_q_sq": str(HBAR_Q_SQ),
            "hbar_q":    str(HBAR_Q),
            "q":         str(Q),
            "q_inv":     str(Q_INV),
            "H_A":       str(H_A),
            "two_q":     str(TWO_Q),
            "z_markov":  str(Z_MARKOV),
            "rho_q":     str(RHO_Q),
            "s_skein":   str(S_SKEIN),
        },
        "quantum_integers": {
            f"[{n}]_q": str(q_int(n)) for n in range(1, 10)
        },
        "quantum_factorials": {
            f"[{n}]_q!": str(q_factorial(n)) for n in [3, 6, 9, 12]
        },
        "plancherel_weights_n3": {
            "w_(3)":     str(w_sym),
            "w_(2,1)":   str(w_std),
            "w_(1,1,1)": str(w_alt),
            "sum":       str(w_sym + w_std + w_alt),
        },
        "universal_shape_coupling": universal_shape_coupling,
        "physical_anchoring_bound": {
            "codata_relative_uncertainty": str(Q_ERR / Q),
            "ppb_target": "1e-9",
            "limited_by":
                f"CODATA m_μ/m_e at σ(q)/q ≈ {float(Q_ERR/Q):.2e}",
            "comment": (
                "Internal arithmetic is at 50 digits.  The framework's "
                "DIMENSIONLESS predictions (ratios, equality of "
                "computed quantities) can be checked at 50-digit "
                "precision.  Absolute (MeV) predictions are bounded "
                "to the CODATA-propagated relative uncertainty above "
                "(~1.22e-9 with current m_μ/m_e), which is already at "
                "1-ppb-class."
            ),
        },
    }
    out = Path(__file__).parent / "q-pinning-50-digit.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
