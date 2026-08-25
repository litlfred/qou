#!/usr/bin/env python3
"""⁴He ν_SDP = 2 not 3 — the binding data is the arbiter (bean qou-k2xr).

The monotone count sc(3A)=A−1 predicts ⁴He ν_SDP=3; the corpus assumes 2. Since
⁴He's ρ_F IS the ν_SDP in question (magic-A closure B=ρ_F·m_e·A·8G, where ρ_F=ν_SDP
per conj:kashaev-density-equals-sdp-multiplicity), the experimental binding pins it.

RESULT: data-implied ρ_F(⁴He) = B_AME/(m_e·A·8G) = 1.89 → 2; ρ_F=3 overshoots by
+59%. The monotone {sc(n)=A−1} family is REFUTED at the first doubly-magic nucleus.
See docs/audits/2026-08-02-he4-nu-sdp-decisive-2-not-3.md.
"""
import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
G = mp.catalan
eightG = 8 * G                      # = Vol(L6a4) = 7.32772
me = mp.mpf('0.51099895')           # MeV
A = 4
vol = A * eightG
B_AME = mp.mpf('28.295673')         # ⁴He total binding, MeV (AME2020)


def main() -> int:
    print(f"8G = Vol(L6a4) = {mp.nstr(eightG, 8)}   A·8G = {mp.nstr(vol, 8)}")
    print(f"{'ρ_F':>4} {'B_pred (MeV)':>13} {'err vs AME 28.296':>18}")
    for rho in (1, 2, 3):
        B = rho * me * vol
        print(f"{rho:>4} {float(B):>13.3f} {float((B - B_AME) / B_AME * 100):>+17.1f}%")
    rho_data = B_AME / (me * vol)
    print(f"\nData-implied ρ_F(⁴He) = {float(rho_data):.4f} → 2, NOT 3.")
    print("Verdict: ρ_F=3 overshoots +59% ⇒ the monotone sc(3A)=A−1=3 count is "
          "REFUTED by binding. ν_SDP is regime-dependent (A−1 for linear-chain "
          "census atoms; ~2 for the doubly-magic ⁴He closed shell), not a single "
          "monotone count. (ρ_F=2 itself is corpus-rounded empirical, not derived.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
