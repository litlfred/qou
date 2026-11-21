#!/usr/bin/env python3
"""Does "V^k is reading-3 feasible iff 3 | k" hold for every k at the proton pin? (bean qou-ales)

On H_3 the gamma-gamma vertex V = sigma_0 sigma_1^-1 has det 1 and trace t = -1 - h^2 in the
(2,1) Hoefsmit block (GammaGammaVertexOrder.lean). So chi_k = tr V^k obeys the Chebyshev
recurrence chi_{k+1} = t chi_k - chi_{k-1}, chi_0 = 2, chi_1 = t, i.e. chi_k = 2 cos(k theta)
with 2 cos theta = t. The (3) block gives 1 for every k and the (1^3) block has weight 0 under
convention D, so feasibility is chi_k >= 0.

GammaGammaSelectionTen.lean proves the 3 | k pattern for k <= 10 and leaves all k open. This
probe answers it at q0: theta = 2 pi/3 + delta, and the pattern breaks once k delta is large
enough. GammaGammaSelectionAllK.lean shows the selection of V^3 does not depend on it.

mpmath at 60 digits; prints only; writes no witness.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402,F401

import mpmath as mp  # noqa: E402

from qou_substrate.constants import q_at  # noqa: E402

K_MAX = 400


def main() -> int:
    mp.mp.dps = 60
    q = mp.mpf(str(q_at()))
    h = q - 1 / q
    t = -1 - h**2
    chi = [mp.mpf(2), t]
    for _ in range(2, K_MAX + 1):
        chi.append(t * chi[-1] - chi[-2])
    theta = mp.acos(t / 2)
    delta = theta - 2 * mp.pi / 3
    ok = True
    # recurrence agrees with the closed form
    rec_ok = all(mp.almosteq(chi[k], 2 * mp.cos(k * theta), mp.mpf(10) ** -40) for k in range(K_MAX + 1))
    print(f"[{'PASS' if rec_ok else 'FAIL'}] chi_k = 2 cos(k theta) for k <= {K_MAX}")
    ok &= rec_ok
    small_ok = all((chi[k] > 0) == (k % 3 == 0) for k in range(1, 11))
    print(f"[{'PASS' if small_ok else 'FAIL'}] 3 | k pattern for 1 <= k <= 10 (matches GammaGammaSelectionTen)")
    ok &= small_ok
    viol = [k for k in range(1, K_MAX + 1) if (chi[k] >= 0) != (k % 3 == 0)]
    print(f"\nq0 = {mp.nstr(q, 20)}, h^2 = {mp.nstr(h**2, 12)}")
    print(f"theta = {mp.nstr(theta, 15)} = 2 pi/3 + delta, delta = {mp.nstr(delta, 12)}")
    print(f"first k breaking the 3 | k pattern: {viol[:6]}  (k mod 3 = {[k % 3 for k in viol[:6]]})")
    print(f"  chi_{viol[0]} = {mp.nstr(chi[viol[0]], 12)}; cost of V^{viol[0]} = {2 * viol[0]} crossings")
    print(f"  first multiple of 3 that is infeasible: {next(k for k in viol if k % 3 == 0)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
