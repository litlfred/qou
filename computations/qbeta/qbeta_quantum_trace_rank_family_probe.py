#!/usr/bin/env python3
"""Q_beta from the categorical quantum trace, every rank N at once (bean qou-99qc).

The chain def:frobenius-pairing -> def:mass-identity -> prop:feynman-categorical-trace
reads a braid in C = Rep(SU_q(N)) with the quantum trace on V^{(x)n}, block weights
y_lambda = dim_q(V_lambda)/[N]^n. QBetaChiralityReduction.lean: on Delta_S only the
(3) and (1^3) blocks survive, functional = (h[2]/2)(y_3 - y_111).

QuantumTraceFamilyCoth.lean (sorry-free) proves, with a = q^N,
    (h[2]/2)(y_3 - y_111) = (h^2/2) (a^2+1)/(a^2-1) = (h^2/2) coth(N ln q).
N = 1 is the augmentation, N = 2 the ruled z_D, N -> oo the standard symmetrising
trace tau(sigma_w) = delta_{w,e} (the Frobenius form of H_n as a symmetric algebra).

This probe re-checks the closed form exactly (sympy over Q(q, a)), checks N = 2 against
the direct z_D trace of Delta_S and N -> oo against the standard trace, checks that the
framing-corrected trace of def:mass-identity gives sigma and sigma^-1 the same value,
and prints Q_beta per rank at the proton pin with both E0 forms. It also prints the
scale CODATA would need on the ruled trace and the mass channel's own scale per unit
trace. Prints only; writes no witness. The real-N solve is a DIAGNOSTIC: selecting N by
it would be selection against the target (AGENTS.md NO FITTING). mpmath end to end.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402,F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from qou_substrate.constants import q_at  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

Q_BETA_CODATA_STR = "0.78233341"  # comparison only, never an input


def exact_checks() -> list[tuple[str, bool]]:
    q, a = sp.symbols("q a", positive=True)
    B = lambda x: (x - 1 / x) / (q - 1 / q)  # noqa: E731  quantum number of x = q^k
    den = B(q**2) * B(q**3) * B(a) ** 2
    y3 = B(a * q) * B(a * q**2) / den
    y1 = B(a / q) * B(a / q**2) / den
    h, b2 = q - 1 / q, q + 1 / q
    fam = h * b2 / 2 * (y3 - y1)
    closed = h**2 / 2 * (a**2 + 1) / (a**2 - 1)
    zD = q**3 / (q**2 + 1)
    delta_zD = h**2 / 2 - h * zD          # tr_{z_D}(Delta_S), sigma_i -> z_D, 1 -> 1
    return [
        ("closed form (h[2]/2)(y3-y111) = (h^2/2)(a^2+1)/(a^2-1)", sp.simplify(fam - closed) == 0),
        ("N=1 (a=q) is the augmentation h[2]/2", sp.simplify(closed.subs(a, q) - h * b2 / 2) == 0),
        ("N=2 (a=q^2) is |tr_{z_D}(Delta_S)|", sp.simplify(closed.subs(a, q**2) + delta_zD) == 0),
        ("N->oo is the standard trace value h^2/2", sp.simplify(sp.limit(closed, a, sp.oo) - h**2 / 2) == 0),
        ("framed trace: q^-2 z_D = q^2 (z_D - h) = q/(q^2+1)",
         sp.simplify(zD / q**2 - q / (q**2 + 1)) == 0 and sp.simplify(q**2 * (zD - h) - q / (q**2 + 1)) == 0),
    ]


def main() -> int:
    mp.mp.dps = 50
    q_codata = mp.mpf(Q_BETA_CODATA_STR)
    ok = True
    for name, passed in exact_checks():
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
        ok &= passed
    q = mp.mpf(str(q_at()))
    me = mp.mpf(str(M_E_MEV))
    lam = mp.log(q)
    h = q - 1 / q
    hb = (q - 1) / q
    E0 = me / (q * (q - 1))
    E0t = E0 / (1 - hb**2)
    fam = lambda N: h**2 / 2 / mp.tanh(N * lam)  # noqa: E731
    print(f"\nq0 = {mp.nstr(q, 20)} (proton pin); CODATA Q_beta = {q_codata} MeV (comparison only)")
    print("rank N | (h^2/2)coth(N lam) | Q_beta order-zero E0 | Q_beta tower E0")
    for N in [1, 2, 3, 4, 6, 10, 50]:
        v = fam(N)
        print(f"  {N:4d} | {mp.nstr(v, 10):>12} | {mp.nstr(v * E0, 8)} MeV ({mp.nstr((v * E0 / q_codata - 1) * 100, 5)} %)"
              f" | {mp.nstr(v * E0t, 8)} MeV ({mp.nstr((v * E0t / q_codata - 1) * 100, 5)} %)")
    v_inf = h**2 / 2
    print(f"   inf | {mp.nstr(v_inf, 10):>12} | {mp.nstr(v_inf * E0, 8)} MeV ({mp.nstr((v_inf * E0 / q_codata - 1) * 100, 5)} %)")
    print("\nDIAGNOSTIC ONLY (not a selection): real N where the family meets CODATA")
    for lab, E in (("order-zero E0", E0), ("tower E0", E0t)):
        Ns = mp.findroot(lambda N: fam(N) * E - q_codata, 1.2)
        print(f"  {lab}: N* = {mp.nstr(Ns, 12)}, a* = q^N* = {mp.nstr(q**Ns, 12)}")
    v2 = fam(2)
    print("\nScale on the ruled trace (N = 2):")
    print(f"  |tr_zD(Delta_S)| = {mp.nstr(v2, 12)}")
    print(f"  E0 order zero = {mp.nstr(E0, 10)} MeV, tower = {mp.nstr(E0t, 10)} MeV")
    print(f"  scale CODATA needs = {mp.nstr(q_codata / v2, 10)} MeV = {mp.nstr(q_codata / v2 / E0, 10)} x E0(order zero)")
    vol41 = 2 * mp.clsin(2, mp.pi / 3)
    mmu = me * vol41 / hb**2
    qf3 = (q + 1 / q) * (q**2 + 1 + q**-2)
    unit = 2 * mmu * qf3 / q**3
    print(f"  mass-channel scale 2 m_mu [3]!/q^3 = {mp.nstr(unit, 10)} MeV per unit trace"
          f" -> Delta through it = {mp.nstr(unit * v2, 8)} MeV")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
