#!/usr/bin/env python3
"""qbeta_fmap_modular_dual_missing_probe.py — WHERE the modular dual matters.

Quantifies the Faddeev modular dual `q̃` relative to the compact q-dilog,
WITHOUT evaluating the transcendental `Φ_b` (safe from summation/contour error).
It locates WHERE the compact `phi_q` (which has no `q̃` dependence) diverges
from `Φ_b`.

Foundation (convention `q = e^{2πi b²}`; the 'modular double = bar involution'
framing was retracted 2026-07-07):
  * `Φ_b` is a ratio of products at reciprocal scales `b`, `b^{-1}`, with
    `q̃ = e^{2πi b^{-2}}` the modular DUAL (b↔b^{-1} ⇒ q↦q̃, not q↦q^{-1}).
  * The compact `phi_q` depends on `q` alone. Its accuracy vs `Φ_b` is therefore
    governed by the SIZE of the missing `q̃` (dual) product: negligible when
    `|q̃|≈0`, order-one when `|q̃|≈1`.

KEY FINDING (corrected framing, 2026-07-07):
  * On the REAL substrate `q₀>1` the dual is NEGLIGIBLE (`|q̃|≈10^{-165}`), so
    `Φ_b ≈ phi_q` there — this is WHY the compact form is correct on the
    mass / real-q / Rogers face.
  * At a ROOT-OF-UNITY `q` (the decay / fibre saddle) the dual is ORDER ONE
    (`|q̃|=1`), so `Φ_b ≠ phi_q` there — this is WHY the compact form fails on
    the Q_β / decay / Faddeev face.
  The modular dual is thus the FIBRE (root-of-unity) structure; it is absent
  from the compact form and only matters where Q_β lives.

Honest scope: `Φ_b` itself is not evaluated; the u↔x (f-map) link to the
observed u_substrate pole (PR #1727) is open. Quantifies WHERE the missing
structure bites; fits nothing.
"""
from __future__ import annotations

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


def q_tilde_from_q(q: mp.mpc) -> mp.mpc:
    """Modular dual q̃ = e^{2πi b^{-2}} with q = e^{2πi b²} ⇒ b^{-2} = 2πi/ln q."""
    lnq = mp.log(q)
    binv2 = (2 * mp.pi * mp.mpc(0, 1)) / lnq
    return mp.e ** (2 * mp.pi * mp.mpc(0, 1) * binv2)


def report(label: str, q: mp.mpc) -> None:
    qt = q_tilde_from_q(q)
    aqt = mp.fabs(qt)
    print(f"  {label}")
    print(f"     q            = {mp.nstr(q, 14)}   |q| = {mp.nstr(mp.fabs(q), 6)}")
    print(f"     q̃ (dual)     = {mp.nstr(qt, 10)}   |q̃| = {mp.nstr(aqt, 6)}")


def main() -> int:
    print("=" * 78)
    print(" Q_β f-map — where the Faddeev modular dual q̃ bites (compact q-dilog has none)")
    print("=" * 78)

    # (A) real substrate q₀ > 1 — the mass / real-q / Rogers saddle.
    Q0 = mp.mpf("1.10997859555733471989976322048322502665620840878015")
    print("\n(A) REAL SUBSTRATE (mass / real-q face):")
    report("q₀ substrate", Q0)
    aA = mp.fabs(q_tilde_from_q(Q0))
    print(f"     => |q̃| ≈ {mp.nstr(aA, 4)} ≈ 0  ⇒ dual NEGLIGIBLE ⇒ Φ_b ≈ phi_q here.")
    print("        (This is why the compact form is CORRECT on the mass face.)")

    # (B) root-of-unity q — the decay / fibre / Faddeev saddle.
    # b² = 2/5 ⇒ q = e^{4πi/5}; b^{-2} = 5/2 ⇒ q̃ = e^{5πi} = -1 (|q̃| = 1).
    qB = mp.e ** (2 * mp.pi * mp.mpc(0, 1) * mp.mpf(2) / 5)
    print("\n(B) ROOT OF UNITY q = e^{4πi/5} (decay / fibre face, b² = 2/5):")
    report("q = ζ_5^2", qB)
    aB = mp.fabs(q_tilde_from_q(qB))
    print(f"     => |q̃| = {mp.nstr(aB, 4)} = O(1)  ⇒ dual ORDER-ONE ⇒ Φ_b ≠ phi_q here.")
    print("        (This is why the compact form FAILS on the Q_β / decay face.)")

    print("\n  CONCLUSION: the modular dual q̃ (the b^{-1} product the compact form")
    print("  lacks) is the FIBRE / root-of-unity structure. It is ~0 on the real")
    print("  substrate (compact ≈ Φ_b, mass face) and O(1) at root-of-unity q")
    print("  (compact ≠ Φ_b, decay face) — quantitatively the mass/decay split.")
    print("\n  HONEST SCOPE: Φ_b not evaluated (state-integral deferred); u↔x f-map")
    print("  link to the observed u_substrate pole (PR #1727) is OPEN. Fits nothing.")

    ok = aA < mp.mpf("1e-50") and abs(aB - 1) < mp.mpf("1e-30")
    print(f"\n  check (|q̃|≈0 at substrate AND |q̃|=1 at root of unity): {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
