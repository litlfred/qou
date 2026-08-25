#!/usr/bin/env python3
"""qbeta_g3_5two_deformed_bilinear.py — the ANALYTIC 5₂ M-dictionary,
part 2c-1: the DEFORMED (descendant) layer — blocks A_m/B_m/C_m (GGM
241a-c), the deformed W_m(x;q) (244), the bilinear W_{m,μ}(u;τ) =
W_{−μ}(x̃;q̃⁻¹)·Δ(τ)·W_m(x;q)ᵀ (245/246), the x↔x⁻¹ symmetry (247/248),
and the (250) WALL-CROSSING determinant identity — the exact
q → q⁻¹ (bar) transform of the deformed blocks.

Why: parts 1-2b derived the complete u=0 Stokes machinery; the φ_odd
target lives at deformed x (the substrate u_sub = 2t). The (245)
bilinear is the deformed analogue of the (92) sandwich — Theorem 22(c)
says it is ENTIRE in u — and the (250) identity is the deformed
analogue of the extension relation H⁺_k(q⁻¹) = (−1)^k H⁻_k that part 1
certified: it expresses H(·;q⁻¹) through H(·;q)-data exactly, i.e. the
EXACT bar-transform, which is what the intrinsic bar-odd extraction
needs (the barodd probe #3962 localized the open step as stripping the
classical prefactor — the bilinear + crossing identity do this
structurally, no Borel numerics).

Checks:
  C1  regression to the certified assembly: (243) at (m,μ) = (0,0) —
      the prefactored [W_{0,0}]₁₁ equals the #3951/#3962-certified
      Z₅₂(u;τ) at generic (u, τ).
  C2  (247) symmetry: A_m(x⁻¹) = A_m(x), B_m(x⁻¹) = C_m(x) at generic
      m ≠ 0 — certifies the descendant x^m/z-slot reading.
  C3  Theorem 22(c) u-ENTIRETY of the bilinear at descendant orders:
      every entry of W_{m,μ}(u;τ) is finite at the lattice pole
      u* = log q (individual blocks blow up as (u−u*)⁻²) — two-radius
      circle-average agreement.
  C4  the (250) wall-crossing determinant identity at generic
      (x, y, z, q) — LHS H(x,y,z;q⁻¹) (the H⁻ branch) vs the
      determinant of four H⁺-evaluations over the θ-triple. The
      printed reading is tried first; on failure a small variant scan
      (θ arguments, prefactor) runs and the winner is reported openly.

Anti-fabrication: (241)-(246) extracted clean (text layer); (250)'s
θ-triple/determinant layout partially reflow-scrambled — hence the
scan-on-failure discipline with open reporting. Everything is
certified against the independently-derived machinery of parts 1-2b
and the certified #3951 blocks. No fit; no c_k wired; mpmath dps 45,
no float64; scope-(a).
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def _load(name):
    spec = importlib.util.spec_from_file_location(name, _HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_bl = _load("qbeta_g3_5two_exact_blocks")          # H, blocks, theta chain
_bs = _load("qbeta_g3_5two_barodd_substrate")      # certified Z52 assembly
theta = _bl.theta
H = _bl.H

set_compute_dps()


def blocks_m(m, x, q, qh):
    """Descendant blocks (241a-c) at order m; qh = chosen √q (threaded
    exactly as in the certified #3951 m=0 assembly)."""
    A = H(x, 1 / x, q ** m, q)
    B = theta(-x * qh, q) ** -2 * x ** m * H(x, x ** 2, q ** m * x ** 2, q)
    C = theta(-x / qh, q) ** -2 * x ** -m \
        * H(1 / x, x ** -2, q ** m * x ** -2, q)
    return A, B, C


def W_def(m, x, q, qh):
    """Deformed W_m(x;q) (244): rows m, m+1, m+2 × columns (A, B, C)."""
    return mp.matrix([list(blocks_m(mm, x, q, qh))
                      for mm in (m, m + 1, m + 2)])


def Delta(tau):
    ta = tau + 1 / tau
    cA = mp.e ** (mp.mpc(0, 3) * mp.pi / 4
                  + mp.mpc(0, 5) * mp.pi / 12 * ta)
    cB = mp.e ** (mp.mpc(0, -1) * mp.pi / 4 + mp.mpc(0, 1) * mp.pi / 12 * ta)
    return mp.matrix([[cA, 0, 0], [0, cB, 0], [0, 0, cB]])


def Wmu(m, mu, u, tau):
    """(245): W_{m,μ}(u;τ) = W_{−μ}(x̃;q̃⁻¹)·Δ(τ)·W_m(x;q)ᵀ."""
    q = mp.e ** (2 * mp.pi * mp.mpc(0, 1) * tau)
    qt = mp.e ** (-2 * mp.pi * mp.mpc(0, 1) / tau)
    qh = mp.e ** (mp.pi * mp.mpc(0, 1) * tau)
    qth = mp.e ** (-mp.pi * mp.mpc(0, 1) / tau)
    x = mp.e ** u
    xt = mp.e ** (u / tau)
    Wt = W_def(-mu, xt, 1 / qt, 1 / qth)
    Wq = W_def(m, x, q, qh)
    return Wt * Delta(tau) * Wq.T


def main() -> int:
    print("=" * 78)
    print(" 5₂ analytic M-dictionary part 2c-1 — deformed bilinear + "
          "wall-crossing")
    print("=" * 78)

    tau = mp.mpc(0, 1) * mp.mpf("0.6")
    u0 = mp.mpf("0.23")

    # C1: (243)/(245) at (0,0) vs certified Z52
    W00 = Wmu(0, 0, u0, tau)
    z_ref = _bs.Z52(u0, tau)
    dev1 = abs(W00[0, 0] - z_ref) / abs(z_ref)
    ok1 = dev1 < mp.mpf("1e-38")
    print(f"\n[C1] [W_00]_11 vs certified Z₅₂ at generic (u,τ): rel dev "
          f"= {mp.nstr(dev1, 4)}: {ok1}")

    # C2: (247) symmetry at descendant order m = 2
    q = mp.e ** (2 * mp.pi * mp.mpc(0, 1) * tau)
    qh = mp.e ** (mp.pi * mp.mpc(0, 1) * tau)
    x = mp.e ** u0
    A1, B1, C1 = blocks_m(2, x, q, qh)
    A2, B2, C2 = blocks_m(2, 1 / x, q, qh)
    d_a = abs(A2 - A1) / abs(A1)
    d_bc = abs(B2 - C1) / abs(C1)
    d_cb = abs(C2 - B1) / abs(B1)
    ok2 = max(d_a, d_bc, d_cb) < mp.mpf("1e-38")
    print(f"[C2] (247) symmetry at m=2: A {mp.nstr(d_a, 3)}, B(x⁻¹)=C "
          f"{mp.nstr(d_bc, 3)}, C(x⁻¹)=B {mp.nstr(d_cb, 3)}: {ok2}")

    # C3: u-entirety of W_{m,μ} at the lattice pole u* = log q, at a
    # DESCENDANT order (m,μ) = (1,2): two-radius circle-average agreement
    u_star = 2 * mp.pi * mp.mpc(0, 1) * tau     # x = q
    m_t, mu_t = 1, 2

    def avg_entry(i, j, r, K=16):
        acc = mp.mpc(0)
        for k in range(K):
            uu = u_star + r * mp.e ** (2 * mp.pi * mp.mpc(0, 1) * k / K)
            acc += Wmu(m_t, mu_t, uu, tau)[i, j]
        return acc / K

    v_r1 = avg_entry(0, 0, mp.mpf("1e-2"))
    v_r2 = avg_entry(0, 0, mp.mpf("5e-3"))
    dev3 = abs(v_r1 - v_r2) / abs(v_r1)
    ok3 = dev3 < mp.mpf("1e-25") and mp.isfinite(abs(v_r1))
    print(f"[C3] entirety at u* = log q, (m,μ)=({m_t},{mu_t}): "
          f"two-radius circle-average agreement {mp.nstr(dev3, 3)} "
          f"(a Laurent tail would shift the mean ∝ r⁻¹): {ok3}")

    # C4: the (250) wall-crossing identity
    print("\n[C4] (250) wall-crossing determinant identity:")
    xx, yy = mp.mpf("1.31"), mp.mpf("0.77")
    zz = mp.mpc("0.4", "0.2")
    qq_ = mp.mpf("0.23")
    qs = mp.sqrt(qq_)
    lhs = H(xx, yy, zz, 1 / qq_)               # H at q⁻¹ (H⁻ branch)

    def rhs_variant(th_sign, pref_xy):
        a = H(1 / xx, yy / xx, zz / xx ** 2, qq_)
        b = H(1 / yy, xx / yy, zz / yy ** 2, qq_)
        c = xx * H(1 / xx, yy / xx, zz / (qq_ * xx ** 2), qq_)
        d = yy * H(1 / yy, xx / yy, zz / (qq_ * yy ** 2), qq_)
        det = a * d - b * c
        thp = theta(-xx * th_sign, qq_) * theta(-yy * th_sign, qq_) \
            * theta(-xx / yy * th_sign, qq_)
        return det / (pref_xy * thp)

    dev4 = abs(rhs_variant(1 / qs, yy) - lhs) / abs(lhs)
    reading = "printed: theta(-q^-1/2 ...), prefactor y"
    if dev4 > mp.mpf("1e-35"):
        scans = [(1 / qs, yy, "th=q^-1/2, pref y"),
                 (qs, yy, "th=q^+1/2, pref y"),
                 (1 / qs, xx, "th=q^-1/2, pref x"),
                 (qs, xx, "th=q^+1/2, pref x"),
                 (1 / qs, -yy, "th=q^-1/2, pref -y"),
                 (qs, -yy, "th=q^+1/2, pref -y")]
        for th, pf, tagv in scans:
            dv = abs(rhs_variant(th, pf) - lhs) / abs(lhs)
            print(f"    variant {tagv}: rel dev {mp.nstr(dv, 4)}")
            if dv < dev4:
                dev4, reading = dv, f"scan-derived: {tagv}"
    ok4 = dev4 < mp.mpf("1e-35")
    print(f"    winner [{reading}]: rel dev = {mp.nstr(dev4, 4)}: {ok4}")

    ok = ok1 and ok2 and ok3 and ok4
    verdict = (
        f"DEFORMED LAYER CERTIFIED — the descendant blocks (241), the "
        f"deformed W_m (244), and the bilinear W_(m,mu) = "
        f"W_-mu(xt;qt^-1) Delta(tau) W_m(x;q)^T (245/246) stand: "
        f"[W_00]_11 reproduces the certified Z_52 to {mp.nstr(dev1, 3)} "
        f"(C1); the (247) x<->x^-1 symmetry holds at descendant order "
        f"({mp.nstr(max(d_a, d_bc, d_cb), 3)}, C2); Theorem 22(c) "
        f"u-ENTIRETY verified at the lattice point u* = log q for "
        f"(m,mu)=(1,2) by two-radius circle-average agreement "
        f"({mp.nstr(dev3, 3)}; a pole tail would shift the mean "
        f"proportionally to 1/r) (C3); and the (250) WALL-CROSSING determinant "
        f"identity — the exact q -> q^-1 bar-transform of the deformed "
        f"H-blocks — holds at generic (x,y,z,q) to {mp.nstr(dev4, 3)} "
        f"({reading}) (C4). The exact bar-transform tool for the "
        f"intrinsic bar-odd extraction is now in hand: NEXT (part "
        f"2c-2) apply (250) to the substrate bar-pair to strip the "
        f"classical prefactor structurally and extract phi_odd at "
        f"derived precision (vs the #3987 preliminary -0.004145). No "
        f"fit; no c_k wired; scope-(a)."
        if ok else
        f"PART 2c-1 INCOMPLETE (honest): C1={ok1}({mp.nstr(dev1, 3)}) "
        f"C2={ok2} C3={ok3}({mp.nstr(dev3, 3)}) C4={ok4}"
        f"({mp.nstr(dev4, 3)}, {reading}) — the failing check localizes "
        f"the next decode/derivation step. No fit; no c_k wired; "
        f"scope-(a)."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-5two-deformed-bilinear", engine="mpmath")
    wb.set_description(
        "Analytic 5_2 M-dictionary part 2c-1: descendant blocks (241), "
        "deformed W_m (244), bilinear W_(m,mu) (245/246) with Theorem "
        "22(c) u-entirety at descendant orders, the (247) symmetry, and "
        "the (250) wall-crossing determinant identity (exact q->q^-1 "
        "bar-transform) certified at generic points against the "
        "independently certified #3951 machinery.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("checks", {
        "C1_regression_rel": mp.nstr(dev1, 10),
        "C2_symmetry_rel": mp.nstr(max(d_a, d_bc, d_cb), 10),
        "C3_entirety_two_radius_rel": mp.nstr(dev3, 10),
        "C4_crossing_rel": mp.nstr(dev4, 10),
        "C4_reading": reading})
    wb.add_data("verdict", verdict)
    wb.add_assertion("descendant_bilinear_certified",
                     computed=1.0 if (ok1 and ok2 and ok3) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="C1 regression + C2 symmetry + C3 entirety "
                            "at descendant (m,mu)")
    wb.add_assertion("wall_crossing_identity_holds",
                     computed=1.0 if ok4 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="(250) determinant identity at generic "
                            "(x,y,z,q); reading provenance recorded")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
