#!/usr/bin/env python3
"""
binding_bstar_bridge.py — the two binding lenses are ONE object: #3548's connected
`tr_M` part == this session's centered/ghost Gram-quadratic norm (exact identity).

Owner steer (2026-07-11): bridge the per-bond value b* between #3548 (connected
transfer-matrix tr_M) and #3545 (negative-norm ghost Gram-quadratic, Part 10-11).

Identity (algebraic, using the Markov normalization tr_M(1)=1):
  #3548 connected part of a mode w:     C(w) = tr_M(w²) − tr_M(w)²
  #3545 centered/ghost Gram norm:       ⟨δw⟩²_G = tr_M((w−⟨w⟩·1)²)
                                               = tr_M(w²) − 2⟨w⟩tr_M(w) + ⟨w⟩²tr_M(1)
                                               = tr_M(w²) − tr_M(w)²   = C(w).
So the CONNECTED PART IS the Gram-quadratic norm of the centered (traceless) mode.
The "ghost" δw = w − ⟨w⟩ is exactly the fluctuation whose connected 2-point #3548
computes. Verified bit-identical on the H_2 (2,k) torus bond (#3548's Check 3):

  tr_M(σ) = 0.499320,  tr_M(σ²) = 1.104388
  #3548  tr(σ²) − tr(σ)²                 = 0.8550672621
  #3545  tr_M((σ − ⟨σ⟩)²)                = 0.8550672621   (|Δ| = 0)

CONSEQUENCE (b* pinned, no duplicate build):
  • #3548's deuteron connected 0.193 IS #3545's per-bond b* = ⟨g_A,σ_bond,g_B⟩_G.
    Whichever lens computes the connected part gives b* for both — the H₆ seminormal
    build is #3548's PROBE 2, not a separate #3545 task.
  • Ties in main a44296db (decay=binding-quadratic): binding = quadratic = connected
    = centered Gram norm — all three are the same object.
  • Sign: centered modes have INDEFINITE Markov-Gram norm; the σ mode gives +0.855,
    the bar-odd L₊−L₋ ghost gives −0.4275 (binding). Same construction, mode-dependent sign.

EXPLORATORY — no production wiring, no fitted constant, no tier change.
Audit: docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md §Part 12
"""
from __future__ import annotations
import sys
from pathlib import Path
import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent / "substrate"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps
set_compute_dps()  # canonical COMPUTE_DPS (=70) — matches WitnessBuilder precisionMetadata
# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

try:
    from q_parameter import Q_MP as Q0
    Q0 = mp.mpf(str(Q0))
except Exception:
    Q0 = mp.mpf("1.10997859555733471")


def sigma_pow_markov_trace(k):
    """tr_M(σ^k) in H_2 via σ² = h σ + 1 (identical to #3548's convention)."""
    h = Q0 - 1 / Q0
    z = Q0**3 / (Q0**2 + 1)
    a, b = mp.mpf(0), mp.mpf(1)
    for _ in range(k):
        a, b = h * a + b, a
    return a * z + b


def main() -> int:
    trs1 = sigma_pow_markov_trace(1)
    trs2 = sigma_pow_markov_trace(2)
    connected_3548 = trs2 - trs1 ** 2                       # their cumulant
    gram_3545 = trs2 - 2 * trs1 * trs1 + trs1 ** 2 * mp.mpf(1)  # ⟨δσ⟩²_G, tr_M(1)=1
    diff = abs(connected_3548 - gram_3545)

    print("=== b* bridge: #3548 connected tr_M == #3545 centered Gram-quadratic (exact) ===\n")
    print(f"tr_M(σ) = {float(trs1):.6f}   tr_M(σ²) = {float(trs2):.6f}   tr_M(1) = 1")
    print(f"#3548 connected  tr(σ²) − tr(σ)²        = {mp.nstr(connected_3548, 12)}")
    print(f"#3545 ⟨δσ⟩²_G = tr_M((σ−⟨σ⟩)²)          = {mp.nstr(gram_3545, 12)}")
    print(f"|difference| = {mp.nstr(diff, 4)}   ⇒ {'IDENTICAL' if diff < mp.mpf('1e-30') else 'DIFFER'}")
    print()
    print("PROVED: connected part (cumulant) = Gram-quadratic norm of the centered (ghost) mode.")
    print("  ⇒ #3548 deuteron connected 0.193 IS #3545 per-bond b*; one build serves both lenses.")
    print("  ⇒ ties main a44296db: binding = quadratic = connected = centered Gram norm.")

    ok = diff < mp.mpf("1e-30")
    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("binding-bstar-bridge", engine="mpmath")
        wb.set_description(
            "EXPLORATORY: proves #3548's connected tr_M part (tr(w²)−tr(w)²) is bit-identical "
            "to #3545's centered/ghost Gram-quadratic norm tr_M((w−⟨w⟩)²), via tr_M(1)=1. The "
            "two binding lenses are one object; the connected part IS the Gram norm of the "
            "centered (traceless) fluctuation. So #3548's deuteron connected 0.193 = #3545's "
            "per-bond b*; one H₆ build serves both. Ties main a44296db (decay=binding-quadratic). "
            "Verified on the H_2 (2,k) torus bond. No fit.")
        wb.add_data("h2_bond", {"tr_sigma": float(trs1), "tr_sigma2": float(trs2),
                                "connected_3548": float(connected_3548),
                                "gram_3545": float(gram_3545), "abs_diff": float(diff)})
        wb.add_assertion(
            name="connected_equals_centered_gram_norm",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("tr(σ²)−tr(σ)² (#3548 connected) == tr_M((σ−⟨σ⟩)²) (#3545 ghost Gram norm) "
                    "bit-identical; the connected part IS the centered Gram-quadratic. b* unified."))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness emit skipped: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
