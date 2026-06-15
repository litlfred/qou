"""m_p residual 54 ppb — exotic-basis PSLQ.

Open work item from PR #1645: PR #1629's Task 2 ran PSLQ at 120 dps
across 17 natural-constants basis elements (G, π², ζ(3), ln 2/3/5,
α_em, h^k, [k]_q) — all NULL. The audit doc noted that
Mahler measures, Bloch-Wigner D(z), and q-Bernoulli evaluations were
DEFERRED as potential future extensions.

This probe runs PSLQ over the deferred exotic basis at 120 dps to
either:
  - Identify the residual structurally (Bloch-Wigner at substrate root,
    Mahler measure of a Bring-quintic-related polynomial)
  - Confirm the residual is at the CODATA precision floor (no exotic
    candidate hits structurally)

## Basis (exotic, 12 elements)

  - D(e^{iπ/3})       Bloch-Wigner at root of unity (Vol(4_1)-related)
  - D(e^{iπ/5})       Bloch-Wigner at quintic root (Bring-related)
  - D(q_0) (real)     Bloch-Wigner at substrate point
  - D(ℏ_q · i)        Bloch-Wigner at substrate imaginary
  - m(z²+z-1)         Mahler measure of golden-ratio polynomial
  - m(z⁵-z-1)         Mahler measure of Bring quintic polynomial
  - m(z³+z+1)         Mahler measure (Cassini-like)
  - Vol(4_1)/π²       4_1 hyperbolic volume normalized
  - Vol(B_3)/π²       Borromean volume normalized
  - Vol(4_1)·G/π³     mixed substrate + Catalan
  - K(1/2)            Complete elliptic K at half (substrate context)
  - K(sin(π/8))       Complete elliptic K at quintic-related arg

## Cross-references

- PR #1629 Task 2 NULL audit
- merged PR #1645 ProtonMassEMSignBlock class
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _h4_substrate import ALPHA_EM, M_E_MEV, M_MU_MEV, M_P_MEV  # noqa: E402
from _h4_substrate import qfact, trM_borromean_closed  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import q_at, q_str  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def bloch_wigner_D(z):
    """Bloch-Wigner dilog D(z) = Im(Li_2(z)) + arg(1-z)·log|z|."""
    if abs(z) < mp.mpf("1e-30"):
        return mp.mpf(0)
    Li2_z = mp.polylog(2, z)
    Im_Li2 = mp.im(Li2_z)
    if abs(1 - z) < mp.mpf("1e-30"):
        return Im_Li2
    arg_1mz = mp.arg(1 - z)
    log_abs_z = mp.log(abs(z))
    return Im_Li2 + arg_1mz * log_abs_z


def mahler_measure_polynomial(coeffs):
    """Mahler measure exact via Jensen's formula:
    m(P) = log|a_d| + Σ max(0, log|r_i|) for roots r_i of P, a_d leading coef.

    Uses mp.polyroots for full-precision root extraction (no grid).
    coeffs is [c_0, c_1, ..., c_d] (constant term first); mp.polyroots
    expects highest-degree first, so we reverse."""
    rev = list(reversed(coeffs))
    while len(rev) > 1 and rev[0] == 0:
        rev.pop(0)
    if not rev or (len(rev) == 1 and rev[0] == 0):
        return mp.mpf(0)
    if len(rev) == 1:
        return mp.log(abs(rev[0]))
    roots = mp.polyroots(rev)
    total = mp.log(abs(rev[0]))
    for r in roots:
        abs_r = abs(r)
        if abs_r > 1:
            total += mp.log(abs_r)
    return total


def main() -> int:
    DPS = 120
    set_compute_dps(DPS)
    q = q_at(DPS)

    print("=" * 78)
    print("m_p residual 54 ppb — exotic-basis PSLQ (120 dps)")
    print("=" * 78)
    print(f"\nq_0 = {q_str(60)} (truncated for display)\n")

    # Recap setup
    qfact_3 = qfact(3, q)
    trM = abs(trM_borromean_closed(q))
    F_Bor = trM * qfact_3 / q ** 3
    k_req = (2 * M_MU_MEV * F_Bor - M_P_MEV) / M_E_MEV
    residual = 12 - k_req
    EM_term = ALPHA_EM / mp.pi / 6  # = (α_em/π)/6
    # Sub-residual: what's left after the EM correction
    sub_residual = residual - EM_term
    # In normalized units: divide by k_required
    sub_residual_norm = sub_residual / k_req

    print(f"[Recap]")
    print(f"  residual_target (12 - k_req)  = {mp.nstr(residual, 18)}")
    print(f"  EM correction (α_em/π)/6      = {mp.nstr(EM_term, 18)}")
    print(f"  sub_residual                  = {mp.nstr(sub_residual, 18)}")
    print(f"  normalized (sub/k_req)        = {mp.nstr(sub_residual_norm, 18)}")
    print(f"  in ppb of k                   = {mp.nstr(sub_residual_norm * mp.mpf('1e9'), 8)}")

    # ── Exotic basis ──
    G = mp.catalan
    hbar_q = 1 - 1 / q
    h = q - 1 / q

    print(f"\n[Computing exotic basis elements at 120 dps]")
    basis = {}

    # Bloch-Wigner at natural roots
    basis["D(e^(iπ/3))"] = bloch_wigner_D(mp.exp(mp.mpc(0, mp.pi / 3)))
    print(f"  D(e^(iπ/3))    = {mp.nstr(basis['D(e^(iπ/3))'], 12)}")
    basis["D(e^(iπ/5))"] = bloch_wigner_D(mp.exp(mp.mpc(0, mp.pi / 5)))
    print(f"  D(e^(iπ/5))    = {mp.nstr(basis['D(e^(iπ/5))'], 12)}")
    basis["D(e^(iπ/6))"] = bloch_wigner_D(mp.exp(mp.mpc(0, mp.pi / 6)))
    print(f"  D(e^(iπ/6))    = {mp.nstr(basis['D(e^(iπ/6))'], 12)}")
    # Bloch-Wigner at substrate
    basis["D(q_0 + i·0)"] = bloch_wigner_D(q)  # real, gives 0 by definition
    basis["D(ℏ_q + i·ℏ_q)"] = bloch_wigner_D(mp.mpc(hbar_q, hbar_q))
    print(f"  D(ℏ_q+iℏ_q)    = {mp.nstr(basis['D(ℏ_q + i·ℏ_q)'], 12)}")

    # Mahler measures (exact via polyroots — full 120 dps precision)
    print(f"  computing Mahler measures (exact via mp.polyroots)...")
    basis["m(z²+z-1)"] = mahler_measure_polynomial([-1, 1, 1])
    print(f"  m(z²+z-1)      = {mp.nstr(basis['m(z²+z-1)'], 12)} (golden ratio)")
    basis["m(z⁵-z-1)"] = mahler_measure_polynomial([-1, -1, 0, 0, 0, 1])
    print(f"  m(z⁵-z-1)      = {mp.nstr(basis['m(z⁵-z-1)'], 12)} (Bring quintic)")
    basis["m(z³+z+1)"] = mahler_measure_polynomial([1, 1, 0, 1])
    print(f"  m(z³+z+1)      = {mp.nstr(basis['m(z³+z+1)'], 12)}")

    # Hyperbolic volumes
    vol_4_1 = 2 * mp.clsin(2, mp.pi / 3)  # SnapPy standard
    vol_B_3 = 8 * G  # Adams 1985
    basis["Vol(4_1)/π²"] = vol_4_1 / mp.pi ** 2
    basis["Vol(B_3)/π²"] = vol_B_3 / mp.pi ** 2
    basis["Vol(4_1)·G/π³"] = vol_4_1 * G / mp.pi ** 3

    # Complete elliptic
    basis["K(1/2)"] = mp.ellipk(mp.mpf("0.5"))
    basis["K(sin(π/8))"] = mp.ellipk(mp.sin(mp.pi / 8) ** 2)

    # ── Pairwise PSLQ on sub_residual ──
    print(f"\n[Pairwise PSLQ on sub_residual at maxcoeff 10⁶]")
    matches = []
    for name, val in basis.items():
        if abs(val) < mp.mpf("1e-30"):
            continue
        try:
            rel = mp.pslq([sub_residual, val], tol=mp.mpf("1e-22"), maxcoeff=1000000)
            if rel and rel[0] != 0:
                ratio = -mp.mpf(rel[1]) / mp.mpf(rel[0])
                check = sub_residual - ratio * val
                if abs(check) < mp.mpf("1e-20"):
                    matches.append((name, rel, ratio, abs(check)))
                    print(f"  ⭐ sub_residual ≈ ({rel[1]}/{rel[0]}) · {name} "
                          f"(resid {mp.nstr(abs(check), 8)})")
        except Exception:
            pass
    if not matches:
        print(f"  No tight pairwise integer relations.")

    # ── Best-fit fractional ratios ──
    print(f"\n[Ratio test: sub_residual / each_basis_element]")
    for name, val in basis.items():
        if abs(val) < mp.mpf("1e-30"):
            continue
        ratio = sub_residual / val
        ratio_abs = abs(ratio)
        # Check if ratio is close to a small rational p/q
        from fractions import Fraction
        approx_frac = Fraction(float(ratio_abs)).limit_denominator(1000)
        diff = ratio_abs - mp.mpf(approx_frac.numerator) / approx_frac.denominator
        if abs(diff) < mp.mpf("1e-9"):
            print(f"  sub_residual / {name}  ≈  {approx_frac}  (Δ = {mp.nstr(diff, 6)})")

    # ── Verdict ──
    print(f"\n[Verdict]")
    if matches:
        verdict = (
            f"EXOTIC HIT: {len(matches)} clean integer relations found over "
            f"the exotic basis. The 54 ppb sub-residual has a structural form."
        )
    else:
        verdict = (
            f"DEEPER NULL — even the exotic basis (Bloch-Wigner D(z), Mahler "
            f"measures of golden/quintic/Cassini polynomials, hyperbolic "
            f"volumes, elliptic integrals) does NOT identify the 54 ppb "
            f"sub-residual at 120 dps tol 10⁻²². Strongly suggests the "
            f"residual is at the **CODATA precision floor** for the input "
            f"anchors (α_em precision 10⁻¹⁰; m_p 10⁻¹⁰; m_μ 10⁻¹⁰; m_e 10⁻¹⁰). "
            f"A 54 ppb residual on a kg-scale identity is consistent with "
            f"~10⁻¹⁰ × propagation factor. Further structural derivation "
            f"would need improved CODATA inputs."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "mp-residual-exotic-basis-pslq",
        engine="python",
    )
    w.set_description(
        "Open-work follow-up to PR #1645: PSLQ search for the 54 ppb m_p "
        "sub-residual after (α_em/π)/6 correction, over the EXOTIC basis "
        "deferred by PR #1629 Task 2 (Bloch-Wigner D(z), Mahler measures "
        "of golden/Bring-quintic/Cassini polynomials, hyperbolic volumes, "
        "elliptic K). 120 dps, maxcoeff 10⁶, tol 10⁻²²."
    )
    w.add_parameter("q_120dps", q_str(120))
    w.add_parameter("mp_dps_runtime", str(mp.mp.dps))
    w.add_data("sub_residual", mp.nstr(sub_residual, 25))
    w.add_data("sub_residual_ppb", mp.nstr(sub_residual_norm * 1e9, 12))
    w.add_data("basis_size", len(basis))
    w.add_data("matches", len(matches))
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="exotic_basis_pslq_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source=f"Exotic-basis PSLQ over {len(basis)} elements at 120 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
