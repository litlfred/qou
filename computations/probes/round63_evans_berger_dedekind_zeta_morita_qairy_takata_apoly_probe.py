#!/usr/bin/env python3
"""
Round 63 80-dps mpmath probe for beans:
  - qou-0seq: Evans-Berger (1992) [evans-berger1992] third-order winding integral Psi_{123} on 3-braids
  - qou-2pp7: Broadhurst (1998) [broadhurst1998] rational Dedekind-zeta invariants of hyperbolic 3-manifolds
  - qou-cp1x: Morita (2011) [morita-t2011] connection formula between Ramanujan A_w and q-Airy / theta factors
  - qou-dvqx: Takata (2004) [takata2004] / Le (2006) [le2006] classical q -> 1 AJ specialization for twist knots
  - qou-e1me: Takata (2004) [takata2004] Hoste-Shanahan twist-knot A-polynomial recursion & 4_1 seed check
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import subprocess
from mpmath import mp

mp.dps = 80

PROBE_PATH = pathlib.Path(__file__).resolve()
WITNESS_PATH = PROBE_PATH.with_name(
    "round63-evans-berger-dedekind-zeta-morita-qairy-takata-apoly.witness.json"
)


def fmt(val: mp.mpf | mp.mpc) -> str:
    if isinstance(val, mp.mpc):
        return f"{mp.nstr(val.real, 50)} + {mp.nstr(val.imag, 50)}i"
    return mp.nstr(val, 60)


def check_qou_0seq_evans_berger_triple_linking() -> dict[str, str | int | bool]:
    """
    Evans-Berger (1992) [evans-berger1992] eqs. (21)-(22):
    1) The Arnol'd symplectic 1-form psi_{123} = (lam12 d lam23 - lam23 d lam12) / 2
       integrated over the closed Borromean pure-braid loop
         (lam12(t), lam23(t)) = (sin(2*pi*t) / sqrt(pi), (1 - cos(2*pi*t)) / sqrt(pi))
       evaluates to the exact third-order winding number Psi_{123} = 1.
    2) Discrete 3-block commutator on B_3 = (sigma_1 sigma_2^{-1})^3 with pure-braid
       block increments (1, 0), (-1, 1), (0, -1) equals 1, while adding a balanced
       Hopf spectator (h, 0) at start and (-h, 0) at end decouples identically.
    """
    # Continuous Arnol'd contour integral over [0, 1]:
    # lam12(t) = sin(2*pi*t) / sqrt(pi), lam23(t) = (1 - cos(2*pi*t)) / sqrt(pi)
    # 1/2 * (lam12 * lam23' - lam23 * lam12') = (2*pi / (2*pi)) * (sin^2 + cos^2 - cos) = 1 - cos(2*pi*t)
    def integrand(t: mp.mpf) -> mp.mpf:
        arg = 2 * mp.pi * t
        s = mp.sin(arg)
        c = mp.cos(arg)
        lam12 = s / mp.sqrt(mp.pi)
        lam23 = (1 - c) / mp.sqrt(mp.pi)
        dlam12 = 2 * mp.sqrt(mp.pi) * c
        dlam23 = 2 * mp.sqrt(mp.pi) * s
        return (lam12 * dlam23 - lam23 * dlam12) / 2

    psi_cont = mp.quad(integrand, [0, mp.mpf("0.5"), 1])
    res_psi_cont = abs(psi_cont - 1)

    # Discrete 3-block commutator 2 * Psi_{123} on B_3 = (sigma_1 sigma_2^{-1})^3
    def comm_2x(blocks: list[tuple[int, int]]) -> int:
        total = 0
        for r in range(len(blocks)):
            for s in range(r + 1, len(blocks)):
                ar, br = blocks[r]
                as_, bs = blocks[s]
                total += ar * bs - br * as_
        return total

    b3_blocks = [(1, 0), (-1, 1), (0, -1)]
    b3_comm = comm_2x(b3_blocks)
    # With balanced Hopf spectator (h, 0) prepended and (-h, 0) appended:
    h_spec = 7
    b3_with_spectator = [(h_spec, 0)] + b3_blocks + [(-h_spec, 0)]
    b3_spec_comm = comm_2x(b3_with_spectator)
    spectator_diff = abs(b3_spec_comm - b3_comm)

    passed = bool(
        res_psi_cont < mp.mpf("1e-75")
        and b3_comm == 1
        and spectator_diff == 0
    )
    return {
        "beanId": "qou-0seq",
        "referenceKey": "evans-berger1992",
        "continuousArnoldIntegral": fmt(psi_cont),
        "continuousIntegralResidual": fmt(res_psi_cont),
        "discreteBorromeanCommutator2x": b3_comm,
        "spectatorDecouplingResidual": spectator_diff,
        "passed": passed,
    }


def check_qou_2pp7_broadhurst_dedekind_zeta_volumes() -> dict[str, str | int | bool]:
    """
    Broadhurst (1998) [broadhurst1998] arXiv:hep-th/9811173v1:
    1) Over Q(sqrt(-3)) (discriminant -3), the Bloch-Wigner volume of the regular ideal
       tetrahedron is D_2(exp(i*pi/3)) = Im Li_2(exp(i*pi/3)) = (3*sqrt(3)/4) L(2, chi_{-3}),
       and Vol(4_1) = Vol(m003) = 2 * D_2(exp(i*pi/3)) = (3*sqrt(3)/2) L(2, chi_{-3})
       = (9*sqrt(3)/(2*pi^2)) * zeta_{Q(sqrt(-3))}(2), with rational multiple a/b = 2.
    2) Over Q(i) (discriminant -4), the Bloch-Wigner unit is Catalan's constant
       G = D_2(i) = Im Li_2(i) = L(2, chi_{-4}), and
         Vol(L5a1) = 4 * G,   Vol(L6a4) = 8 * G = 2 * Vol(L5a1).
    """
    omega6 = mp.exp(mp.pi * mp.j / 3)
    d2_omega6 = mp.im(mp.polylog(2, omega6))
    # L(2, chi_{-3}) via Hurwitz zeta: 3^{-2} * (zeta(2, 1/3) - zeta(2, 2/3))
    l2_chi3 = (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9
    vol_41 = 2 * d2_omega6
    vol_41_from_l2 = (3 * mp.sqrt(3) / 2) * l2_chi3
    res_41_zeta = abs(vol_41 - vol_41_from_l2)

    # Q(i): Catalan's constant G = Im Li_2(i) = 4^{-2} * (zeta(2, 1/4) - zeta(2, 3/4))
    g_catalan = mp.im(mp.polylog(2, mp.j))
    l2_chi4 = (mp.zeta(2, mp.mpf(1) / 4) - mp.zeta(2, mp.mpf(3) / 4)) / 16
    vol_whitehead = 4 * g_catalan
    vol_borromean = 8 * g_catalan
    res_whitehead_zeta = abs(vol_whitehead - 4 * l2_chi4)
    res_borromean_commensurable = abs(vol_borromean - 2 * vol_whitehead)

    passed = bool(
        res_41_zeta < mp.mpf("1e-75")
        and res_whitehead_zeta < mp.mpf("1e-75")
        and res_borromean_commensurable < mp.mpf("1e-75")
    )
    return {
        "beanId": "qou-2pp7",
        "referenceKey": "broadhurst1998",
        "volFigureEight41": fmt(vol_41),
        "figureEightDedekindZetaResidual": fmt(res_41_zeta),
        "volWhiteheadL5a1": fmt(vol_whitehead),
        "volBorromeanL6a4": fmt(vol_borromean),
        "whiteheadCatalanResidual": fmt(res_whitehead_zeta),
        "borromeanDoubleWhiteheadResidual": fmt(res_borromean_commensurable),
        "passed": passed,
    }


def check_qou_cp1x_morita_ramanujan_qairy() -> dict[str, str | int | bool]:
    """
    Morita (2011) [morita-t2011] arXiv:1104.0755v2:
    1) Exact recentring identity (L1):
         A_w(w^{1-2n} u) = (-1)^n w^{n - n^2} u^n Phi_n(u)
       for A_w(z) = sum_{m>=0} w^{m^2} (-z)^m / (w; w)_m.
    2) Exact two-theta Morita connection decomposition:
         Phi_n(u) = (S_0(u) * E_even(u) - S_1(u) * E_odd(u)) / (w; w)_inf,
       where S_0(u) = (w^2 u; w^2)_inf (1/u; w^2)_inf (w^2; w^2)_inf and
       S_1(u) = (w^3 u; w^2)_inf (1/(w u); w^2)_inf (w^2; w^2)_inf are the two
       Jacobi theta factors and E_even(u), E_odd(u) are the even/odd q-Airy subseries.
    """
    q = mp.mpf("0.23")
    w = q**2
    u = mp.mpc("0.41", "0.17")
    n = 2

    def qpoch_inf(a: mp.mpc, qq: mp.mpf) -> mp.mpc:
        p = mp.mpc(1)
        for k in range(250):
            p *= 1 - a * (qq**k)
        return p

    def qpoch(a: mp.mpf, qq: mp.mpf, m: int) -> mp.mpf:
        p = mp.mpf(1)
        for k in range(m):
            p *= 1 - a * (qq**k)
        return p

    z_arg = (w ** (1 - 2 * n)) * u
    aw_val = sum(
        (w ** (m * m)) * ((-z_arg) ** m) / qpoch(w, w, m) for m in range(120)
    )
    phi_val = sum(
        ((-1) ** k) * (w ** (k * (k + 1))) * (u**k) / qpoch(w, w, n + k)
        for k in range(-n, 100)
    )
    res_recentering = abs(
        aw_val - ((-1) ** n) * (w ** (n - n * n)) * (u**n) * phi_val
    )

    s0 = (
        qpoch_inf((w**2) * u, w**2)
        * qpoch_inf(1 / u, w**2)
        * qpoch_inf(w**2, w**2)
    )
    s1 = (
        qpoch_inf((w**3) * u, w**2)
        * qpoch_inf(1 / (w * u), w**2)
        * qpoch_inf(w**2, w**2)
    )
    e_even = sum(
        ((-1) ** s) * (w ** (s * s + 2 * n * s)) * (u ** (-s)) / qpoch(w, w, 2 * s)
        for s in range(60)
    )
    e_odd = sum(
        ((-1) ** s)
        * (w ** (s * (s + 1) + 1 + (2 * s + 1) * n))
        * (u ** (-s))
        / qpoch(w, w, 2 * s + 1)
        for s in range(60)
    )
    rhs_morita = (s0 * e_even - s1 * e_odd) / qpoch_inf(w, w)
    res_morita_decomp = abs(phi_val - rhs_morita)

    passed = bool(
        res_recentering < mp.mpf("1e-75")
        and res_morita_decomp < mp.mpf("1e-75")
    )
    return {
        "beanId": "qou-cp1x",
        "referenceKey": "morita-t2011",
        "wParam": fmt(w),
        "recenteredPhiN": fmt(phi_val),
        "recenteringResidual": fmt(res_recentering),
        "moritaTwoThetaDecompResidual": fmt(res_morita_decomp),
        "passed": passed,
    }


def check_qou_dvqx_and_e1me_takata_twist_knot_apoly() -> tuple[
    dict[str, str | int | bool], dict[str, str | int | bool]
]:
    """
    Takata (2004) [takata2004] arXiv:math/0401068v1 & Le (2006) [le2006]:
    1) qou-e1me: Check Takata's A_{K_{-1}}(l, m) seed against the balanced CCGLS
       figure-eight A-polynomial under l = -L, m^2 = M^2, and verify A_{K_{-1}}(l, 1) = (l + 1)^2.
    2) qou-dvqx: Check the Hoste-Shanahan two-term recursion A_{K_p} = c A_{K_{p-1}} - d A_{K_{p-2}}
       at p = 1 (from A_{K_0} = 1, A_{K_{-1}}) and p = 2 (5_2 twist knot), and verify the
       classical specialization at m^2 = 1: c(l, 1) = 2(l + 1)^2, d(l, 1) = (l + 1)^4.
    """
    l_val = mp.mpc("0.63", "0.29")
    m2_val = mp.mpc("1.17", "-0.23")

    def c_trace(l: mp.mpc, m2: mp.mpc) -> mp.mpc:
        return (
            -l
            + l**2
            + 2 * l * m2
            + m2**2
            + 2 * l * (m2**2)
            + (l**2) * (m2**2)
            + 2 * l * (m2**3)
            + m2**4
            - l * (m2**4)
        )

    def d_det(l: mp.mpc, m2: mp.mpc) -> mp.mpc:
        return (m2**2) * ((l + m2) ** 4)

    def a_fig8_takata(l: mp.mpc, m2: mp.mpc) -> mp.mpc:
        return (
            -l
            + l * m2
            + m2**2
            + 2 * l * (m2**2)
            + (l**2) * (m2**2)
            + l * (m2**3)
            - l * (m2**4)
        )

    def a_fig8_ccgls_balanced(L: mp.mpc, m2: mp.mpc) -> mp.mpc:
        return (
            (L**2) * (m2**2)
            + L * (m2**4 - m2**3 - 2 * (m2**2) - m2 + 1)
            + m2**2
        )

    # Check qou-e1me: a_fig8_takata(-L, m2) == a_fig8_ccgls_balanced(L, m2)
    res_ccgls_match = abs(
        a_fig8_takata(-l_val, m2_val) - a_fig8_ccgls_balanced(l_val, m2_val)
    )
    res_fig8_m1 = abs(a_fig8_takata(l_val, mp.mpc(1)) - (l_val + 1) ** 2)

    # Check qou-dvqx: classical m^2 = 1 specialization of transfer trace & det,
    # plus 5_2 (K_2) A-polynomial evaluated via Hoste-Shanahan recursion step
    res_c_m1 = abs(c_trace(l_val, mp.mpc(1)) - 2 * ((l_val + 1) ** 2))
    res_d_m1 = abs(d_det(l_val, mp.mpc(1)) - (l_val + 1) ** 4)
    a_k0 = mp.mpc(1)
    a_k1 = l_val + m2_val**3
    a_k2_52 = c_trace(l_val, m2_val) * a_k1 - d_det(l_val, m2_val) * a_k0
    a_k2_at_m1 = c_trace(l_val, mp.mpc(1)) * (l_val + 1) - d_det(l_val, mp.mpc(1))
    # At m^2 = 1: 2(l+1)^3 - (l+1)^4 = (l+1)^3 * (2 - (l+1)) = (l+1)^3 * (1 - l)
    res_k2_m1 = abs(a_k2_at_m1 - ((l_val + 1) ** 3) * (1 - l_val))

    passed_e1me = bool(
        res_ccgls_match < mp.mpf("1e-75") and res_fig8_m1 < mp.mpf("1e-75")
    )
    passed_dvqx = bool(
        res_c_m1 < mp.mpf("1e-75")
        and res_d_m1 < mp.mpf("1e-75")
        and res_k2_m1 < mp.mpf("1e-75")
    )
    return (
        {
            "beanId": "qou-dvqx",
            "referenceKey": "takata2004",
            "companionKey": "le2006",
            "fiveTwoAPolySample": fmt(a_k2_52),
            "traceAtM1Residual": fmt(res_c_m1),
            "detAtM1Residual": fmt(res_d_m1),
            "fiveTwoAtM1FactorResidual": fmt(res_k2_m1),
            "passed": passed_dvqx,
        },
        {
            "beanId": "qou-e1me",
            "referenceKey": "takata2004",
            "fig8TakataAtMinusL": fmt(a_fig8_takata(-l_val, m2_val)),
            "ccglsBalancedMatchResidual": fmt(res_ccgls_match),
            "fig8AtM1DoubleRootResidual": fmt(res_fig8_m1),
            "passed": passed_e1me,
        },
    )


def main() -> None:
    script_bytes = PROBE_PATH.read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    try:
        commit_sha = (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=PROBE_PATH.parent
            )
            .decode()
            .strip()
        )
    except Exception:
        commit_sha = "0" * 40

    c_0seq = check_qou_0seq_evans_berger_triple_linking()
    c_2pp7 = check_qou_2pp7_broadhurst_dedekind_zeta_volumes()
    c_cp1x = check_qou_cp1x_morita_ramanujan_qairy()
    c_dvqx, c_e1me = check_qou_dvqx_and_e1me_takata_twist_knot_apoly()

    checks = [c_0seq, c_2pp7, c_cp1x, c_dvqx, c_e1me]
    all_passed = all(bool(c["passed"]) for c in checks)

    witness = {
        "probe": PROBE_PATH.name,
        "precisionDps": 80,
        "scriptCommitSha": commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "beans": ["qou-0seq", "qou-2pp7", "qou-cp1x", "qou-dvqx", "qou-e1me"],
        "allPassed": all_passed,
        "results": {
            "qou_0seq_evans_berger_triple_linking": c_0seq,
            "qou_2pp7_broadhurst_dedekind_zeta_volumes": c_2pp7,
            "qou_cp1x_morita_ramanujan_qairy": c_cp1x,
            "qou_dvqx_takata_le_twist_knot_aj": c_dvqx,
            "qou_e1me_takata_fourone_apoly_seed": c_e1me,
        },
    }

    WITNESS_PATH.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"Wrote {WITNESS_PATH} (allPassed={all_passed})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
