#!/usr/bin/env python3
"""difference_knot_volume_prefactor_probe.py — does B_AME ∝ Vol(difference link)
with a CONSTANT prefactor? The cheap, non-rigorous version of the decisive
JSJ-volume test — runnable WITHOUT Sage.

Route (2026-06-13 difference-knot JSJ audit): the proposed geometric binding
closure is

    B_AME ≈ m_e · Σ Vol(hyperbolic pieces of D) · ρ / ℏ_q²,   D = W_atom·W_free⁻¹,

with a CONSTANT prefactor m_e·ρ/ℏ_q² (single ρ, not per-knot). SnapPy gives the
(non-rigorous) total hyperbolic volume Vol(D) of the composite difference link
(Seifert pieces contribute 0 volume, so the reported volume IS the hyperbolic
part, modulo the degenerate-triangulation slop). The RIGOROUS interval volume
needs Sage (`verify_hyperbolicity`, blocked here), but the CONSTANT-PREFACTOR
test only needs volumes to ~1% — and rigor cannot turn a non-constant prefactor
constant. So this is a valid formalize-first PRUNE of the route before the Sage
step.

Test: k_i = B_AME_i / Vol(D_i) for D / T / ³He / ⁴He.
  • small spread (max/min ≲ 1.1) ⇒ constant prefactor ⇒ route PROMISING:
    motivates the rigorous Sage per-piece decomposition;
  • large spread ⇒ the constant-prefactor closure is REFUTED (a per-atom ρ(D)
    would be needed — the same underived density wall, no gain).

`canonical_retriangulation` (works in SnapPy 3.3.2 WITHOUT Sage, unlike the
2026-06-13 probe's environment) records the canonical-cell / tet structure.

Binding arithmetic in mpmath (NO FLOAT); the volume comes from SnapPy's
`high_precision()` Number (≈64 dps, str()-preserved into mp.mpf — no f64
truncation) — far more than the ~1% a constant-prefactor test needs. The volume
is non-rigorous (numerically-solved shapes, not Sage interval-verified), but the
precision is extended, not f64. Exploratory; no fit; promotes nothing.
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys  # noqa: E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from difference_knot_binding_probe import _difference_braid  # noqa: E402
from q_parameter import Q as Q0, HA as HBAR_Q  # noqa: E402  (ℏ_q = q − q⁻¹? see below)
from codata_constants import (  # noqa: E402
    M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION as B_D,
    AME_B_TRITIUM_MEV_VALIDATION as B_T,
    AME_B_HE3_MEV_VALIDATION as B_HE3,
    AME_B_HE4_MEV_VALIDATION as B_HE4,
)

CASES = [("2H", 1, 1, B_D), ("3H", 1, 2, B_T), ("3He", 2, 1, B_HE3), ("4He", 2, 2, B_HE4)]


def _volume_and_struct(braid):
    """(num_cusps, volume, solution_type, n_canonical_tets) of the closed
    difference braid. Volume is high-precision but non-rigorous (the links are
    composite → degenerate triangulation). canonical_retriangulation works
    without Sage in SnapPy 3.x and gives the canonical-cell tet count."""
    import snappy
    if not braid:
        return 0, mp.mpf(0), "empty", 0
    M = snappy.Link(braid_closure=braid).exterior()
    M.simplify(); M.simplify()
    cusps = M.num_cusps()
    try:
        # str() on SnapPy's Number preserves the full high_precision() digits
        # (≈64 dps here); float() would truncate to f64 and defeat the call.
        Mhp = M.high_precision(); vol = mp.mpf(str(Mhp.volume())); sol = Mhp.solution_type()
    except Exception:
        vol = mp.mpf(str(M.volume())); sol = M.solution_type()
    try:
        n_tets = M.canonical_retriangulation().num_tetrahedra()
    except Exception as e:  # noqa: BLE001
        n_tets = -1
    return cusps, vol, sol, n_tets


def main() -> int:
    set_compute_dps()
    me = mp.mpf(str(M_E_MEV))
    q0 = mp.mpf(str(Q0))
    hbar_q = mp.mpf(str(HBAR_Q))          # canonical ℏ_q alias (q_parameter.HA)
    print(f"\n  DIFFERENCE-LINK VOLUME PREFACTOR PROBE   q₀={float(q0):.6f}  "
          f"m_e={float(me):.5f} MeV  ℏ_q={float(hbar_q):.5f}\n")
    print(f"  {'iso':4s} {'A':>2s} {'cusps':>5s} {'2A-1':>4s} {'Vol(D)':>9s} "
          f"{'B_AME':>8s} {'k=B/Vol':>9s} {'tets':>5s} {'soln':>14s}")

    w = (WitnessBuilder("difference-knot-volume-prefactor", engine="snappea")
         .set_content_block("rem:difference-knot-jsj-volume")
         .set_description(
             "Cheap non-rigorous version of the difference-knot JSJ-volume "
             "decisive test (runnable without Sage): k_i = B_AME_i/Vol(D_i) "
             "for D/T/³He/⁴He; constant k ⇒ the geometric closure "
             "B≈m_e·Vol·ρ/ℏ_q² with a single ρ is viable (motivates Sage "
             "rigor); non-constant ⇒ refuted (per-atom ρ needed = same wall). "
             "Volume non-rigorous (composite links, degenerate tets); rigorous "
             "interval volume is Sage-only. Exploratory; no fit."))

    rows, ks = [], []
    for iso, Z, N, bame in CASES:
        A = Z + N
        braid = _difference_braid(Z, N, "minus", reduce=True)
        cusps, vol, sol, tets = _volume_and_struct(braid)
        bame = mp.mpf(str(bame))
        k = bame / vol if vol > 0 else mp.mpf("nan")
        ks.append(k)
        print(f"  {iso:4s} {A:>2d} {cusps:>5d} {2*A-1:>4d} {float(vol):>9.4f} "
              f"{float(bame):>8.4f} {float(k):>9.5f} {tets:>5d} {sol:>14s}")
        rows.append({"iso": iso, "A": A, "cusps": cusps, "two_A_minus_1": 2 * A - 1,
                     "vol_D_nonrigorous": str(vol), "B_AME_MeV": str(bame),
                     "k_B_over_vol": str(k), "n_canonical_tets": tets,
                     "solution_type": sol})

    kmin, kmax = min(ks), max(ks)
    spread = kmax / kmin if kmin > 0 else mp.mpf("inf")
    # if k were constant, the implied single density ρ = k·ℏ_q²/m_e
    rho_implied = [k * hbar_q ** 2 / me for k in ks]
    constant = spread < mp.mpf("1.1")
    print(f"\n  prefactor k = B_AME/Vol(D): min={float(kmin):.5f} max={float(kmax):.5f} "
          f"spread(max/min)={float(spread):.3f}")
    print(f"  implied ρ = k·ℏ_q²/m_e (would be one constant if route holds): "
          f"{[float(r) for r in rho_implied]}")
    print(f"\n  VERDICT: {'CONSTANT prefactor — route PROMISING, motivates Sage rigor' if constant else 'NON-CONSTANT prefactor — constant-ρ geometric closure REFUTED (non-rigorously)'}")

    w.add_data("rows", rows)
    w.add_data("k_spread_max_over_min", str(spread))
    w.add_data("k_min", str(kmin)); w.add_data("k_max", str(kmax))
    w.add_data("rho_implied_per_atom", [str(r) for r in rho_implied])
    w.add_assertion(
        "constant_prefactor_holds_within_10pct",
        computed=1.0 if constant else 0.0, expected=1.0, tolerance=0.0,
        source="k_i = B_AME_i/Vol(D_i) spread (max/min); constant ⇒ single-ρ "
               "geometric closure viable, else refuted (non-rigorous volumes, "
               "rigor cannot fix a non-constant prefactor)")
    w.add_data("note_sage_gate",
               "verify_hyperbolicity (rigorous interval volume) is Sage-only "
               "and unavailable here; canonical_retriangulation works without "
               "Sage (tet counts above). This probe is the non-rigorous prune; "
               "the rigorous per-piece JSJ volume sum still needs Sage IF the "
               "prefactor is constant here.")
    print(f"\n  witness: {w.save()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
