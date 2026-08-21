#!/usr/bin/env python3
"""
High-precision substrate parameter pinning at 50 decimal digits.

> Note (2026-05-24, PR #1127): the scalar quantity formerly named
> `ρ_q = 1/ℏ_q²` was structurally wrong as a dimensional factor and
> has been removed from this script's outputs (see the audit doc
> dated 2026-05-24 under `docs/audits/` for full context). The q₀ derivation below is unchanged (the Skein
> formula remains accurate to ~ppb at the lepton level where
> operator-valued corrections are small). Canonical replacement for
> the dimensional factor: `prop:rho-k-graded-expansion` (operator-
> valued graded expansion).

CALIBRATION INPUTS (precision-limited by CODATA / SnapPy):

  Vol(4_1) = 2.029 883 212 819 307 250 042 405 108 549 040 ...
             (SnapPy verified hyperbolic structure, ~50+ digits)

  m_p/m_e  = 1836.152 673 426 ± 3.2e-8  (CODATA — the ANCHOR,
             0.017 ppb, the most precise mass ratio available)
             — propagates to σ(q₀)/q₀ ≈ 8.30e-13 relative (830 ppQ),
             NOTE: this said "± 1.1e-7 ... 0.06 ppb ... 2.85e-12" until
             2026-08-21. The live CODATA table (qou_substrate.constants,
             MASS_RATIO_P_E_ERR = float(_P_E.uncertainty)) has carried the
             tighter 0.017 ppb figure for some time; the docstring and the
             committed witness were both stale against it, and a re-run
             refreshed the witness. The 0.06 ppb figure is repeated in
             AGENTS.md too and is stale there.
             computed below from dq/dR via the proton identity
  m_μ/m_e  = 206.768 283 0 ± 4.6e-6  (CODATA 2022 — now a 9.5σ
             PREDICTION, kept only for the cross-check print)

DERIVATION (q₀ pinned from m_p/m_e via the proton substrate identity):

  m_p/m_e =  2·(Vol(4_1)/ℏ_q²)·F_Bor(q) − 12   (Newton-solved for q,
             |tr_M(β_Bor)| = (4+h²−3h⁴−h⁶)/(h²+4), pure-q closed form)
  ℏ_q   =  1 - q⁻¹
  H_A   =  q - q⁻¹
  z     =  1 / (q^{1/2} + q^{-1/2})  (Markov parameter)
  [n]_q =  (q^n - q^{-n}) / (q - q⁻¹)

ξ(q₀) = D(z_q) / ℏ_q², where:
  z_q    = Legendre λ-invariant of Bring elliptic curve at q₀
  D(z)   = Bloch-Wigner dilogarithm

This module computes ALL of the above to 50 decimal places via mpmath.
The PHYSICAL anchoring is bounded by CODATA's 0.017 ppb on m_p/m_e
(σ(q₀)/q₀ ≈ 8.30e-13), but the INTERNAL framework arithmetic is exact
to 50 digits, allowing relative-quantity predictions (ratios,
dimensionless invariants) at that precision.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
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

# CODATA 2022 proton-electron mass ratio — the ANCHOR (0.017 ppb).
from q_parameter import MASS_RATIO_P_E_STR, MASS_RATIO_P_E_ERR  # noqa: E402
R_P = mpf(MASS_RATIO_P_E_STR)

# CODATA 2022 muon-electron mass ratio (now a 9.5σ PREDICTION, kept for
# the cross-check print; q₀ is no longer pinned from it — see below).
#
# READ from the registry, not transcribed. These were the literals
# "206.7682830" / "0.0000046"; the first is the CODATA-**2018** value, 1.451
# ppb from the 2022 value 206.7682827, carried here under a "CODATA 2022"
# comment. qou_substrate.constants now reads the NIST table directly
# (PR #5149), so this picks the correct edition up automatically -- and will
# follow the next adjustment without anyone remembering to edit this line.
from qou_substrate.constants import (  # noqa: E402
    MASS_RATIO_MU_E_STR as M_MU_OVER_E_STR,
    MASS_RATIO_MU_E_ERR as _M_MU_OVER_E_ERR,
)
M_MU_OVER_E_ERR_STR = repr(_M_MU_OVER_E_ERR)
M_MU_OVER_E = mpf(M_MU_OVER_E_STR)

# ── Substrate parameter q₀ — canonical single source ─────────
# Re-pinned 2026-05-28 from m_p/m_e via the proton substrate identity
# (q_parameter.q_at, the Newton solve). Read it here rather than
# re-deriving, so this witness can never drift from the canonical value.
# The old muon derivation (ℏ_q² = Vol/(m_μ/m_e)) is q_parameter.q_muon_at.
from q_parameter import q_at  # noqa: E402
Q         = q_at(mp.dps)
Q_INV     = mpf(1) / Q
HBAR_Q    = mpf(1) - Q_INV
HBAR_Q_SQ = HBAR_Q ** 2
H_A       = Q - Q_INV
TWO_Q     = Q + Q_INV       # [2]_q
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


# ── Bring elliptic curve λ-invariant at q₀ ────────────
def bring_lambda(q: mpf) -> mpc:
    """Legendre λ-invariant of E_q — DISABLED pending verified coefficients.

    The previous implementation used placeholder Weierstrass coefficients
    p(q), r(q) that did NOT come from the paper's Bring-curve
    derivation.  To compute ξ(q) at 50 digits, import the verified
    Weierstrass form from ``lambda_bring_q0.py`` (on main) and
    rewrite this routine.  Until then, this function raises to prevent
    downstream consumers from using unreliable numeric values.
    """
    raise NotImplementedError(
        "bring_lambda() placeholder disabled.  Wire in the verified "
        "Bring-curve coefficients from lambda_bring_q0.py before "
        "computing λ or ξ(q) at 50 digits."
    )


def xi_q(q: mpf) -> mpf:
    """ξ(q) = D(λ_Bring(q)) / ℏ_q² — universal shape coupling.

    DISABLED: depends on ``bring_lambda`` which is currently pinned
    to placeholder coefficients.  See ``lambda_bring_q0.py`` for
    the verified 15-digit path; a 50-digit port is pending.
    """
    raise NotImplementedError(
        "xi_q(q) disabled pending verified Bring-curve coefficients."
    )


if __name__ == "__main__":
    print("=" * 100)
    print(f"HIGH-PRECISION SUBSTRATE PINNING — mp.dps = {mp.dps} digits")
    print("=" * 100)

    print(f"\nInputs (calibration anchor = m_p/m_e via proton identity):")
    print(f"  Vol(4_1)          = {VOL_4_1}")
    print(f"  m_p / m_e (CODATA, ANCHOR) = 1836.152673426")
    print(f"  m_μ / m_e (CODATA, now a 9.5σ PREDICTION) = {M_MU_OVER_E}")

    print(f"\nDerived substrate constants (q from q_parameter.q_at):")
    print(f"  ℏ_q² = (1−q⁻¹)²  = {HBAR_Q_SQ}")
    print(f"  ℏ_q              = {HBAR_Q}")
    print(f"  q                = {Q}")
    print(f"  q⁻¹              = {Q_INV}")
    print(f"  H_A = q - q⁻¹    = {H_A}")
    print(f"  [2]_q = q + q⁻¹  = {TWO_Q}")
    print(f"  z (Markov)       = {Z_MARKOV}")
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
        lam = bring_lambda(Q)
        D_lam = bloch_wigner(lam)
        print(f"  λ_Bring(q₀) = {lam}")
        print(f"  D(λ)            = {D_lam}")
        print(f"  ξ(q₀) = D/ℏ_q² = {xi}")
    except NotImplementedError as e:
        print(f"  DISABLED — placeholder Bring coefficients removed.")
        print(f"  See lambda_bring_q0.py (15-digit verified) on main.")
        print(f"  TODO: port that routine to 50-digit mpmath.")

    print(f"\nUncertainty propagation (m_p/m_e anchor):")
    # q is pinned from m_p/m_e via the proton substrate identity
    # G(q) = 2·(Vol/ℏ_q²)·F_Bor − 12.  σ(q) = σ(R)/|G'(q)|, derivative
    # by central difference.  dq is scaled to the working precision —
    # in this mpmath context dps-scaling is correct and avoids
    # subtractive-cancellation loss (contrast the fixed f64 step in the
    # import-time solver of qou_substrate.constants).
    def _proton_identity(qv: mpf) -> mpf:
        h = qv - mpf(1) / qv
        hbar2 = (mpf(1) - mpf(1) / qv) ** 2
        trM = abs((4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4))
        qf3 = (qv**2 + 1 + qv**(-2)) * (qv + mpf(1) / qv)
        return 2 * VOL_4_1 / hbar2 * (trM * qf3 / qv**3) - 12
    DQ = Q * mpf(10) ** -(mp.dps // 2)
    G_PRIME = (_proton_identity(Q + DQ) - _proton_identity(Q - DQ)) / (2 * DQ)
    DQ_DR = mpf(1) / G_PRIME                       # dq/dR = 1/G'(q)
    R_P_ERR = mpf(str(MASS_RATIO_P_E_ERR))
    Q_ERR = abs(DQ_DR) * R_P_ERR
    S_PROTON = (Q / R_P) * G_PRIME                 # dln(R)/dln(q) ≈ 21
    print(f"  G'(q) = dR/dq            = {G_PRIME}")
    print(f"  sensitivity S=dlnR/dlnq  = {S_PROTON}")
    print(f"  σ(m_p/m_e)               = {R_P_ERR}")
    print(f"  σ(q₀) [absolute]         = {Q_ERR}")
    print(f"  σ(q₀)/q₀ [rel]           = {Q_ERR / Q}")
    rel_prec = float(Q_ERR / Q)
    ppq = rel_prec / 1e-15
    print(f"  → CODATA-bounded relative precision: ~{rel_prec:.2e} ({ppq:.0f} ppQ)")
    # muon cross-check (now a 9.5σ prediction, not the anchor)
    DQ_DR_MU = Q ** 2 * HBAR_Q / (mpf(2) * M_MU_OVER_E)
    Q_ERR_MU = DQ_DR_MU * mpf(M_MU_OVER_E_ERR_STR)
    print(f"  (muon-anchor cross-check would give σ(q₀)/q₀ ≈ "
          f"{float(Q_ERR_MU / Q):.2e} — {float(Q_ERR_MU / Q_ERR):.0f}× looser)")

    # ξ(q₀) is DISABLED pending verified Bring-curve derivation at
    # 50-digit mpmath precision; a 15-digit path exists in
    # lambda_bring_q0.py (on main) and must be ported.
    universal_shape_coupling = {
        "status": "disabled",
        "reason": (
            "bring_lambda() placeholder disabled to prevent "
            "unreliable xi(q₀) values.  Port the verified "
            "lambda_bring_q0.py derivation to 50-digit mpmath "
            "before re-enabling."
        ),
        "formula": "xi(q) = D(lambda_bring(q)) / hbar_q^2",
    }

    # Witness output
    witness = {
        "computation": "q-pinning-50-digit",
        "description": (
            "Substrate parameter q₀ pinned to 50 decimal digits via "
            "mpmath.  READ THE THREE anchor_* ROLE FIELDS BELOW BEFORE "
            "USING THIS: the word \"anchor\" does three different jobs in "
            "this witness and they do NOT all say the same thing.  This "
            "producer is listed under ideal_muon in q0_anchor_manifest.json, "
            "so when run under its own name q_parameter rebinds q_at to "
            "return the MUON literal and the Newton solve described below "
            "never executes -- derived_50_digit.q is the muon value.  The "
            "m_p/m_e route is what DEFINES the quantity, not what ran.  "
            "Internal arithmetic is exact to 50 digits; "
            "physical anchoring is bounded by the propagated CODATA "
            f"relative uncertainty ≈ {float(Q_ERR / Q):.2e} "
            f"({float(Q_ERR / Q) * 1e15:.0f} ppQ) from the "
            f"{float(mpf(str(MASS_RATIO_P_E_ERR)) / R_P) * 1e9:.3f} ppb "
            "m_p/m_e ratio (see physical_anchoring_bound).  "
            "m_μ/m_e is recorded only as a 9.5σ cross-check prediction.  "
            "Recorded 50-digit outputs: q, q^{-1}, ℏ_q², ℏ_q, H_A, "
            "[2]_q, z_markov, s_skein; plus quantum integers/"
            "factorials and n=3 Plancherel weights.  ξ(q₀) via "
            "Bring-curve λ is NOT yet recorded — the current "
            "placeholder has been disabled; port lambda_bring_q0.py "
            "to 50 digits and re-emit."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "precision_decimal_digits": mp.dps,
        "calibration_inputs": {
            "Vol_4_1_str": VOL_4_1_STR,
            "Vol_4_1_source": "SnapPy 3.3.2 verified hyperbolic structure",
            # NOTE: this is the DERIVATION ROUTE, not the layer this witness
            # reports at and not the value it emits. Under the ideal_muon
            # manifest entry the Newton solve does not run. A reader wanting
            # "which pin is this number" wants q0Anchor; a reader wanting
            # "whose uncertainty is quoted" wants physical_anchoring_bound.
            "anchor": "m_p/m_e",
            "anchor_role": (
                "DERIVATION ROUTE — the identity that defines q0. NOT the "
                "layer emitted: under the ideal_muon manifest entry this run "
                "returns the muon literal and this solve does not execute. "
                "For the emitted layer read q0Anchor (muon)."
            ),
            "m_p_over_e_str": MASS_RATIO_P_E_STR,
            "m_p_over_e_err": str(MASS_RATIO_P_E_ERR),
            "m_p_over_e_source": f"CODATA 2022 ({float(mpf(str(MASS_RATIO_P_E_ERR)) / R_P) * 1e9:.3f} ppb)",
            "m_mu_over_e_str": M_MU_OVER_E_STR,
            "m_mu_over_e_err": "0.0000046",
            "m_mu_over_e_role": "9.5σ cross-check PREDICTION (not the anchor)",
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
            "anchor": "m_p/m_e",
            "codata_relative_uncertainty": str(Q_ERR / Q),
            "sensitivity_S_dlnR_dlnq": str(S_PROTON),
            "sigma_q0_absolute": str(Q_ERR),
            "ppq": f"{float(Q_ERR / Q) / 1e-15:.0f}",
            "limited_by":
                f"CODATA m_p/m_e ({float(R_P_ERR / R_P) * 1e9:.3f} ppb) "
                f"at σ(q)/q ≈ {float(Q_ERR/Q):.2e}",
            "muon_cross_check_relative_uncertainty": str(Q_ERR_MU / Q),
            "comment": (
                "Internal arithmetic is at 50 digits.  The framework's "
                "DIMENSIONLESS predictions (ratios, equality of "
                "computed quantities) can be checked at 50-digit "
                "precision.  q₀ is anchored on m_p/m_e (the most precise "
                f"ratio, {float(R_P_ERR / R_P) * 1e9:.3f} ppb); the "
                "propagated bound σ(q₀)/q₀ ≈ "
                f"{float(Q_ERR / Q):.2e} ({float(Q_ERR / Q) * 1e15:.0f} ppQ) "
                "improves one-for-one as CODATA "
                "improves m_p/m_e — it is not a framework ceiling.  The "
                "muon-anchor bound (~1.22e-9) is shown for comparison "
                "and is ~429× looser; m_μ/m_e is now a 9.5σ prediction."
            ),
        },
    }
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, str(Path(__file__).parent / "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
    witness["scriptFile"] = Path(__file__).name
    out = Path(__file__).parent / "q-pinning-50-digit.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
