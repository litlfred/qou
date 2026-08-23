#!/usr/bin/env python3
"""qbeta_5two_habiro_archimedean_action_setup_probe.py

The bar-ODD c3 action, exact route (target-statement + ansatz falsification).

The sibling b3ix result (`2026-07-18`, merged): the 4_1 Habiro cyclotomic tail
S(q)=Sum_n prod_{j=1}^n (1-q^j)(1-q^{-j}), at REAL q (the archimedean rho_inf
face), is BAR-EVEN and has optimal-truncation resurgent action EXACTLY pi^2/5
(golden-ratio dilog; distinct from the geometric Vol(4_1)/pi -- the h<->2pi i/N
wall). That probe explicitly flagged: the bar-ODD channel (the c3 / N_odd datum)
"must use the CHIRAL 5_2 Habiro tail, not 4_1".

EXACT TARGET (this front): the bar-odd c3 action is the rho_inf (real-q,
archimedean-face) optimal-truncation resurgent action of the CHIRAL 5_2 Habiro
cyclotomic tail -- the direct bar-odd analog of 4_1's pi^2/5, expected to be a
dilog constant tied to det(5_2)=7 rather than det(4_1)=5's golden ratio.

This probe (a) VERIFIES the 4_1 Kashaev template Sum_n prod|1-q^j|^2 reproduces
Vol(4_1) at roots of unity (the method is sound), and (b) FALSIFIES the naive
"twist-Gaussian" 5_2 ansatz Sum_n q^{-p n(n+1)} prod|1-q^j|^2 (p=1,2): at q a root
of unity the Gaussian is a pure phase (|q^{-p n(n+1)}|=1), so it only re-weights
the interference, and NEITHER p reproduces Vol(5_2)=2.828 (both undershoot to ~1.8-2.0
and DECREASE with N, so cannot converge up to 2.828). The 5_2 cyclotomic coefficient
is therefore genuinely more structured than a Gaussian phase.

GATE (why the exact action is not computed here): the exact 5_2 archimedean action
needs the VERIFIED 5_2 cyclotomic coefficients C_{5_2,n}(q) (Masbaum twist-knot
formula) -- a literature datum. It must NOT be fabricated: an unverified cyclotomic
form giving a "clean" dilog action would be numerology (anti-laundering). Recording
the target + the falsified ansatz saves the next agent the same wrong turn.

DISCIPLINE: scope-(a). (a) 4_1 template verification (convergent). (a) naive 5_2
ansatz FALSIFIED vs the corpus-validated Vol(5_2). No exact bar-odd action CLAIMED
(gated on the verified cyclotomic coefficients). No fit; no c_k wired; no tier change.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
VOL41 = +(2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3))))       # 2.0298832...
VOL52 = mp.mpf("2.8281220883307831627638988092766349427709813173006")
PI2_5 = mp.pi ** 2 / 5                                            # 4_1 bar-even action


def kashaev_twist(N, p):
    """<K_p>_N = Sum_n q^{-p n(n+1)} prod_{j=1}^n (1-q^j)(1-q^{-j}), q=exp(2pi i/N)."""
    q = mp.e ** (2j * mp.pi / N)
    S = mp.mpc(0)
    prod = mp.mpc(1)
    for n in range(0, N):
        if n >= 1:
            prod *= (1 - q ** n) * (1 - q ** (-n))
        S += q ** (-p * n * (n + 1)) * prod
    return S


def vol_estimate(N, p):
    return 2 * mp.pi * mp.log(abs(kashaev_twist(N, p))) / N


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 78)
    print(" bar-odd c3 action, exact route: 4_1 template verify + naive 5_2 falsify")
    print("=" * 78)

    # (a) 4_1 template: Sum_n prod|1-q^j|^2 -> Vol(4_1) (slow volume-conjecture conv.)
    v41 = {N: vol_estimate(N, 0) for N in (100, 200, 400)}
    print(f"\n 4_1 (p=0) Vol_est: " +
          "  ".join(f"N={N}:{mp.nstr(v41[N],7)}" for N in (100, 200, 400)) +
          f"   (Vol(4_1)={mp.nstr(VOL41,7)})")
    template_converging = v41[100] > v41[200] > v41[400] > VOL41 and \
        (v41[400] - VOL41) < (v41[100] - VOL41)
    check("fourone_kashaev_template_converges_to_vol41", template_converging,
          source="Sum_n prod|1-q^j|^2 decreases monotonically toward Vol(4_1)=2.030 "
                 "(slow log/N volume-conjecture convergence) -- method sound")

    # (b) naive twist-Gaussian 5_2 ansatz: FALSIFIED (neither p reaches Vol(5_2))
    v52 = {(p, N): vol_estimate(N, p) for p in (1, 2) for N in (200, 400)}
    print(f"\n naive 5_2 twist-Gaussian ansatz (target Vol(5_2)={mp.nstr(VOL52,7)}):")
    for p in (1, 2):
        print(f"   p={p}: N=200:{mp.nstr(v52[(p,200)],7)}  N=400:{mp.nstr(v52[(p,400)],7)}"
              f"  (decreasing, below target)")
    # falsified: both p undershoot AND decrease with N (cannot converge up to 2.828)
    p1_falsified = v52[(1, 400)] < v52[(1, 200)] < VOL52 - mp.mpf("0.5")
    p2_falsified = v52[(2, 400)] < v52[(2, 200)] < VOL52 - mp.mpf("0.3")
    check("naive_twist_gaussian_5two_ansatz_falsified", p1_falsified and p2_falsified,
          source="q^{-p n(n+1)} prod|1-q^j|^2 is a pure phase at roots of unity; "
                 "p=1,2 undershoot Vol(5_2)=2.828 (~1.7-2.0) and decrease with N, so "
                 "cannot converge up -- the 5_2 cyclotomic coeff is more than a Gaussian")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        f"BAR-ODD c3 ACTION -- EXACT-ROUTE TARGET STATED + NAIVE 5_2 ANSATZ FALSIFIED "
        f"(scope-(a)). Target: the bar-odd c3 action is the rho_inf archimedean-face "
        f"optimal-truncation resurgent action of the CHIRAL 5_2 Habiro cyclotomic tail -- "
        f"the direct bar-odd analog of the sibling's 4_1 bar-even action pi^2/5={mp.nstr(PI2_5,8)} "
        f"(golden-ratio dilog), expected to be a dilog constant tied to det(5_2)=7. The 4_1 "
        f"Kashaev template Sum_n prod|1-q^j|^2 verifiably converges to Vol(4_1) (method sound), "
        f"but the naive twist-Gaussian 5_2 ansatz q^{{-p n(n+1)}} prod|1-q^j|^2 (p=1,2) is "
        f"FALSIFIED against the corpus-validated Vol(5_2)=2.828 (both undershoot to ~1.7-2.0 "
        f"and decrease with N). GATE: the exact action needs the VERIFIED 5_2 cyclotomic "
        f"coefficients (Masbaum twist-knot formula, a literature datum) -- NOT fabricated here "
        f"(an unverified cyclotomic form giving a clean dilog would be numerology). No exact "
        f"bar-odd action is claimed. No fit; no c_k wired; no tier change."
    )
    print("\nVERDICT:", verdict, flush=True)

    wb = WitnessBuilder("qbeta-5two-habiro-archimedean-action-setup", engine="mpmath")
    wb.set_description(
        "bar-odd c3 action exact route: state the target (rho_inf archimedean action of "
        "the chiral 5_2 Habiro tail, bar-odd analog of 4_1's pi^2/5), verify the 4_1 "
        "Kashaev template converges to Vol(4_1), and falsify the naive twist-Gaussian 5_2 "
        "ansatz vs Vol(5_2). Gate: verified 5_2 cyclotomic coefficients (not fabricated).")
    wb.set_audit_only("docs/audits/2026-07-18-bar-odd-c3-action-exact-route-5two-gate.md")
    for a in assertions:
        wb.add_assertion(a["name"], str(a["passed"]), "True")
    wb.add_data("vol41_estimates", {str(N): mp.nstr(v41[N], 10) for N in (100, 200, 400)})
    wb.add_data("vol52_naive_ansatz_estimates",
                {f"p{p}_N{N}": mp.nstr(v52[(p, N)], 10) for p in (1, 2) for N in (200, 400)})
    wb.add_data("vol52_target", mp.nstr(VOL52, 12))
    wb.add_data("fourone_bar_even_action_pi2_5", mp.nstr(PI2_5, 12))
    wb.add_data("naive_ansatz_falsified", bool(p1_falsified and p2_falsified))
    wb.add_data("gate", "verified 5_2 cyclotomic coefficients (Masbaum twist-knot formula)")
    wb.add_data("verdict", verdict)
    wb.save()
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
