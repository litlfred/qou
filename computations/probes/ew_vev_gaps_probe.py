#!/usr/bin/env python3
"""Derivation attempts for the four open slots of the electroweak vev fixed point.

Companion to `QOU/StandardModel/ElectroweakVevGaps.lean` and
`docs/audits/2026-11-20-ew-vev-gaps.md`. Beans `qou-rpt1`, `qou-myxi`.

    N_v = 1/a = T - s*a_loop*H*(1 - c*a_loop),
    T = q([2]/2)^k [4][6][8] + Z,   H = [2]/(8 pi),
    published: k = 1, Z = 1/pi, s = -1, c = hbar_q^2, a_loop = a = 1/N_v.

For each slot this probe evaluates what a stated, target-independent rule
FORCES, and reports the resulting N_v and its miss against v/m_p. It does not
pick among rules by agreement. Rules are fixed in the source before the
comparison is printed; the comparison is printed last.

Exact arithmetic: mpmath at 60 dps. Inputs: proton-pinned q0 (literal below),
G_F and m_p from library/codata-2022/values.json, m_W (PDG 2024, used only for
the alpha_2 reading of the loop coupling, an imported measured value, not fit).
No witness is written.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
from mpmath import mpf

mp.mp.dps = 60
ROOT = Path(__file__).resolve().parents[2]


def codata(key: str) -> tuple[mpf, mpf]:
    vals = json.loads((ROOT / "library/codata-2022/values.json").read_text())
    e = vals[key]
    return mpf(e["value"]), mpf(e["uncertainty"])


def main() -> int:
    q = mpf("1.10997858275138080759166909561")  # proton pin (AGENTS.md q0 convention)
    qi = 1 / q
    h = q - qi
    hbar = 1 - qi
    pi = mp.pi

    def bal(n: int, x: mpf = q) -> mpf:
        return (x ** n - x ** -n) / (x - 1 / x)

    G_F, G_F_sig = codata("fermi-coupling-constant")
    vals = json.loads((ROOT / "library/codata-2022/values.json").read_text())
    pkey = next(k for k, e in vals.items()
                if e.get("quantity") == "proton mass energy equivalent in MeV")
    m_p = mpf(vals[pkey]["value"]) / 1000
    v = 1 / mp.sqrt(mp.sqrt(2) * G_F)
    N_exp = v / m_p
    sig = N_exp * G_F_sig / (2 * G_F)
    H = bal(2) / (8 * pi)
    bare = q * bal(4) * bal(6) * bal(8)

    def solve(T: mpf, s: int, c: mpf) -> mpf:
        f = lambda a: 1 / a - (T + s * a * H * (1 - c * a))  # noqa: E731
        return 1 / mp.findroot(f, 1 / T)

    def fixed(T: mpf, s: int, c: mpf, kappa: mpf) -> mpf:
        return T + s * kappa * H * (1 - c * kappa)

    def miss(N: mpf) -> str:
        ppb = (N - N_exp) / N_exp * mpf(10) ** 9
        return f"N_v = {mp.nstr(N, 15):>18s}  miss {mp.nstr(ppb, 6):>12s} ppb  {mp.nstr((N - N_exp) / sig, 4):>9s} sigma"

    out = []
    P = out.append
    P(f"q0 = {mp.nstr(q, 30)};  v/m_p = {mp.nstr(N_exp, 15)};  sigma = {mp.nstr(sig / N_exp * 1e9, 6)} ppb")

    # ---- Gap 1: tree prefactor -------------------------------------------------
    P("\n[gap 1] tree prefactor q*([2]/2)^k; derived rules give k=0 or k=3")
    # (a) EM tree rule  T_EM = q * prod_carriers [n_i]  applied uniformly -> k = 0.
    # (b) one quantum/classical dimension ratio [2]/2 per extra link component
    #     (mu - 1 = 1 per 2-component carrier, 3 carriers) -> k = 3.
    # (c) published k = 1: no rule found.
    for k, lab in [(0, "k=0 uniform EM tree rule"), (1, "k=1 published (no rule)"), (3, "k=3 per extra component")]:
        P(f"  {lab:28s} " + miss(solve(bare * (bal(2) / 2) ** k + 1 / pi, -1, hbar ** 2)))
    # Bar-parity of the tree: [n] is bar-invariant, q is not.
    tree = bare * bal(2) / 2
    tree_bar = (1 / q) * bal(2, 1 / q) * bal(4, 1 / q) * bal(6, 1 / q) * bal(8, 1 / q) / 2
    P(f"  T_tree(q)/T_tree(1/q) = {mp.nstr(tree / tree_bar, 20)}  (= q^2 = {mp.nstr(q ** 2, 20)})")
    # (d) convention-D Markov trace of the carrier word sigma1^4 sigma3^6 sigma5^8:
    #     Ocneanu trace is multiplicative on the far-commuting factors,
    #     tr(sigma^n) = b_n + a_n z_D on H_2, z_D = q^3/(q^2+1).
    zD = q ** 3 / (q ** 2 + 1)

    def ab(n: int) -> tuple[mpf, mpf]:
        a, b = mpf(0), mpf(1)
        for _ in range(n):
            a, b = h * a + b, a
        return a, b
    trM = mpf(1)
    for n in (4, 6, 8):
        a, b = ab(n)
        trM *= b + a * zD
    P(f"  conv-D Markov trace of carrier word = {mp.nstr(trM, 15)}  (tree needs {mp.nstr(tree, 15)})")

    # ---- Gap 4: zero-mode counting rule -----------------------------------------
    P("\n[gap 4] zero mode Z = n_carriers * g(Sigma_4) / Area(Sigma_4)  (unique genus-affine rule)")
    Area = 4 * pi * 3
    Z_em = 2 * 4 / Area
    Z_ew = 3 * 4 / Area
    P(f"  EM (n=2): {mp.nstr(Z_em, 20)} vs 2/(3pi) = {mp.nstr(2 / (3 * pi), 20)}")
    P(f"  EW (n=3): {mp.nstr(Z_ew, 20)} vs 1/pi    = {mp.nstr(1 / pi, 20)}")

    # ---- Gap 2: loop sign --------------------------------------------------------
    P("\n[gap 2] sign rule s = -sgn(b0) of the gauge group dressing the sector")
    b0_su2 = -mpf(22) / 3 + mpf(2) / 3 * mpf(1) / 2 * 12 + mpf(1) / 3 * mpf(1) / 2 * 1
    b0_y = mpf(41) / 6  # U(1)_Y, SM normalisation Q = T3 + Y
    P(f"  b0(SU(2)_L, SM) = {mp.nstr(b0_su2, 10)} -> s = -1 ;  b0(U(1)_Y) = {mp.nstr(b0_y, 10)} -> s = +1")
    for s, lab in [(-1, "s=-1 (SU(2)_L reading)"), (+1, "s=+1 (U(1) / EM reading)")]:
        P(f"  {lab:28s} " + miss(solve(tree + 1 / pi, s, hbar ** 2)))

    # ---- Gap 3: loop coupling ----------------------------------------------------
    P("\n[gap 3] loop coupling kappa (non-self-consistent: N = T - kappa*H*(1 - c*kappa))")
    T = tree + 1 / pi
    a_v = 1 / N_exp
    m_W = mpf("80.3692")  # GeV, PDG 2024 world average; imported measured value, not fit
    alpha2 = mp.sqrt(2) * G_F * m_W ** 2 / pi  # g^2/(4 pi), g^2 = 4 sqrt2 G_F m_W^2
    alpha_em = 1 / mpf("137.035999177")
    for kap, lab in [(a_v, "kappa = m_p/v (published)"), (alpha2, "kappa = alpha_2 (G_F, m_W)"),
                     (alpha_em, "kappa = alpha_em(0)"), (mpf(0), "kappa = 0")]:
        P(f"  {lab:28s} kappa={mp.nstr(kap, 8):>12s} " + miss(fixed(T, -1, hbar ** 2, kap)))
    # 1-sigma window in kappa
    lo = mp.findroot(lambda k: fixed(T, -1, hbar ** 2, k) - (N_exp + sig), a_v)
    hi = mp.findroot(lambda k: fixed(T, -1, hbar ** 2, k) - (N_exp - sig), a_v)
    P(f"  1-sigma window kappa in [{mp.nstr(lo, 8)}, {mp.nstr(hi, 8)}];  relative to m_p/v: "
      f"[{mp.nstr(lo / a_v, 6)}, {mp.nstr(hi / a_v, 6)}]")

    # ---- All slots by uniform rules ---------------------------------------------
    P("\n[combined] every slot set by the uniform cross-sector rule (k=0, Z per-carrier, c=h^2)")
    for s in (-1, +1):
        P(f"  s={s:+d} self-consistent       " + miss(solve(bare + Z_ew, s, h ** 2)))
    for line in out:
        print(line)
    assert abs(Z_em - 2 / (3 * pi)) < mpf(10) ** -50 and abs(Z_ew - 1 / pi) < mpf(10) ** -50
    assert abs(tree / tree_bar - q ** 2) < mpf(10) ** -50
    assert b0_su2 == -mpf(19) / 6
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
