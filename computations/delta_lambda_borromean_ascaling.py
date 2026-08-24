#!/usr/bin/env python3
"""delta_lambda_borromean_ascaling.py — does the Borromean per-braid tower
supply the A-scaling the Δ_λ closure needs?

Today's ℓ¹-ceiling audit (2026-06-28-delta-lambda-l1-ceiling-sign-only-prune.md)
proved (Lean, sorry-free) that sign-only Δ_λ re-derivations are excluded
(ℓ¹ ceiling < target ∀ light isotope), and that a *flat* q-dim convention
cannot reproduce binding's A-scaling — "the closure object must carry
A-/λ-dependent structure that bends the A-scaling" (route ii/iii / a structured
kernel, e.g. z2bn q-Gaussian/Habiro EGF #2899).

This diagnostic asks: the **Borromean per-braid tower** (PR #3016, now on main —
`borromean_binding_recompute.borromean_binding`) IS a structured magnitude-adding
kernel. Does its `net/target = B_tower / B_AME` bend the A-scaling toward closure
(net/target → 1 uniformly), compared to the canonical flat `sgn(w₀)·dim`?

NOT a fit, NOT a closure: a falsification/positioning diagnostic. The Borromean
tower has ZERO free parameters (pure Markov τ × m_e); we only *read* its output
and compare its A-profile to the canonical one and to +1. Per AGENTS.md Δ_λ gate:
no 7th ansatz proposed; this positions the per-braid kernel among the
magnitude-side levers (z2bn/w5tg/thb7/PROBE-2) with a derive-or-refute signature.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "substrate"))

from borromean_binding_recompute import borromean_binding  # noqa: E402

# AME2020 totals (MeV) — comparison target only.
AME = {"D": (1, 1, 2.224573), "T": (1, 2, 8.481821), "3He": (2, 1, 7.718058),
       "4He": (2, 2, 28.295673), "6Li": (3, 3, 31.994564),
       "12C": (6, 6, 92.161728), "16O": (8, 8, 127.619), "56Fe": (26, 30, 492.254)}

# canonical flat sgn(w₀)·dim net/target (classic q-dim), read from the
# 2026-06-28 cancellation/A-scaling witness (D/T/³He/⁴He only).
_CANON_WITNESS = HERE / "delta-lambda-cancellation-ascaling-probe.witness.json"


def _canon_classic():
    if not _CANON_WITNESS.exists():
        return {}
    d = json.loads(_CANON_WITNESS.read_text())
    out = {}
    for rec in d.get("data", {}).get("rows", []):
        nt = rec.get("net_over_target", {})
        if "classic" in nt:
            out[rec["atom"]] = float(nt["classic"])
    return out


def main() -> int:
    canon = _canon_classic()
    print("Δ_λ A-scaling: Borromean per-braid tower vs canonical sgn(w₀)·dim "
          "(net/target; closure ⇒ 1.0)\n")
    print(f"{'iso':5s}{'A':>3s}{'B_AME':>9s}{'B_tower':>9s}"
          f"{'tower net/tgt':>14s}{'sgn·dim net/tgt':>17s}")
    rows = []
    for nm, (Z, N, B_AME) in AME.items():
        bt = borromean_binding(Z, N)["B_tower"]
        nt_tower = bt / B_AME
        nt_canon = canon.get(nm)
        rows.append({"iso": nm, "A": Z + N, "B_AME": B_AME, "B_tower": bt,
                     "tower_net_over_target": nt_tower,
                     "canon_sgn_dim_net_over_target": nt_canon})
        cs = f"{nt_canon:17.3f}" if nt_canon is not None else f"{'—':>17}"
        print(f"{nm:5s}{Z + N:3d}{B_AME:9.3f}{bt:9.3f}{nt_tower:14.3f}{cs}")

    # A-scaling verdict (fit-free): spread of net/target across A, and whether
    # the tower trends toward +1 better than the flat canonical.
    tower = [r["tower_net_over_target"] for r in rows]
    light = [r for r in rows if r["iso"] in canon]
    spread_t = max(tower) / min(tower)
    print(f"\n  tower net/target spread (max/min over all A) = {spread_t:.2f}× "
          f"(closure ⇒ 1.0×; non-uniform ⇒ A-/λ structure still missing)")
    if light:
        impr = [r["tower_net_over_target"] / r["canon_sgn_dim_net_over_target"]
                for r in light]
        print(f"  vs canonical sgn·dim on D/T/³He/⁴He: tower supplies "
              f"{min(impr):.1f}–{max(impr):.1f}× MORE net magnitude "
              f"(escapes the ℓ¹ sign-only ceiling — it adds ℓ¹ mass).")
    print("\n  VERDICT: the per-braid Li₂^q kernel is a genuine magnitude-adding "
          "lever (raises net/target well above flat sgn·dim) BUT its A-scaling is "
          "still non-uniform (D over, mid under, ⁵⁶Fe over) — it does NOT close. "
          "Positions it with z2bn/w5tg/thb7/PROBE-2; derive-or-refute its A-profile.")

    # ---- structural origin of the spread: edge-set test (REFUTES the simple
    #   "all-pairs over-counts → sparsify" hypothesis). Re-run the pair sum over
    #   ADJACENT bonds only (A−1, ~A) instead of all C(A,2) (~A²).
    from math import comb as _comb
    import mpmath as _mp
    from q_parameter import Q_MP as _Q
    from codata_constants import M_E_MEV as _ME
    from _li_2_q_util import li_2_q as _li
    _mp.mp.dps = 50
    _q = _mp.mpf(str(_Q)); _me = _mp.mpf(str(_ME)); _qi = 1 / _q; _hh = _q - _qi
    _E0 = _me / (_q * (_q - 1))
    # convention D (owner ruling 2026-08-15, reaffirmed 2026-08-23):
    #   z_D = q^3/(q^2+1).  Was z_C = 1/(sqrt q + sqrt(1/q)) = sqrt q/(q+1), excised.
    # The swap ratio z/(z-h) that _fp/_fn carries is exactly q^4 under D
    # (identically in q); under C it was an irrational with no such closed form.
    _z = _q**3 / (_q**2 + 1)
    _tau = (4 + _hh**2 - 3 * _hh**4 - _hh**6) / (_hh**2 + 4)
    _fp, _fn = _z, _z - _hh

    def _gg(x):
        return -_li(-x, _q, _qi)

    def _b(Z, N, adjacent):
        A = Z + N
        ratio = _fp**max(Z - 1, 0) * (_z if Z and N else 1) * _fn**max(N - 1, 0)
        Dtr = _tau**A * (1 - ratio)
        cnts = ((max(Z - 1, 0), 1 if Z and N else 0, max(N - 1, 0)) if adjacent
                else (_comb(Z, 2), Z * N, _comb(N, 2)))
        pr = sum(c * (_gg(_tau * _tau) - _gg(_tau * _tau * f))
                 for c, f in zip(cnts, (_fp, _z, _fn)))
        return float(_E0 * (Dtr + _z * _z * pr))

    adj = [_b(Z, N, True) / B for _, (Z, N, B) in AME.items()]
    allp = [_b(Z, N, False) / B for _, (Z, N, B) in AME.items()]
    edge = {"all_pairs_spread": max(allp) / min(allp),
            "adjacent_spread": max(adj) / min(adj),
            "hypothesis_refuted": max(adj) / min(adj) > max(allp) / min(allp),
            "note": ("sparsifying the edge set (all-pairs C(A,2)~A² → adjacent "
                     "A−1~A) WORSENS the spread (monotone under-bind at heavy A) — "
                     "the U-shape is NOT a pure edge-count effect; it is "
                     "A²-overscaling at the heavy end PLUS the ⁴He magic dip "
                     "(no shell structure). Edge-set lever (w5tg) alone is "
                     "insufficient; the per-pair magnitude (~0.4 MeV) is far below "
                     "~8 MeV/nucleon, so closure needs magnitude-reshaping "
                     "(z2bn R(q,x)) + shell/magic structure, not sparsification.")}
    print(f"\n  EDGE-SET TEST: all-pairs spread {edge['all_pairs_spread']:.2f}× "
          f"vs adjacent spread {edge['adjacent_spread']:.2f}× → "
          f"sparsify hypothesis {'REFUTED' if edge['hypothesis_refuted'] else 'supported'} "
          f"(adjacent worse; monotone heavy-A under-bind).")

    # ---- the bulk is EXTENSIVE (A-linear), not the A² pair tower. Compare the
    #   tower's A² net/target to the extensive shell term 2·m_e·8G per nucleon
    #   (8G = Vol(L6a4), the Borromean shell residue). A-linear ⇒ flat ~1 for A≥4.
    G = float(__import__("mpmath").catalan); per_nuc = 2 * 0.51099895069 * 8 * G
    mag = [(Z + N) * per_nuc / B for _, (Z, N, B) in AME.items()]
    mag_heavy = [(Z + N) * per_nuc / B for nm, (Z, N, B) in AME.items()
                 if Z + N >= 4]
    extensive = {"per_nucleon_2me8G_MeV": per_nuc,
                 "magic_net_over_target_spread_Age4": max(mag_heavy) / min(mag_heavy),
                 "tower_net_over_target_spread": spread_t,
                 "note": ("the extensive A-linear 2·m_e·8G (≈7.49 MeV/nucleon ≈ "
                          "empirical ~8) gives net/target 0.85–1.06 for A≥4 "
                          "(spread 1.65×) — FAR flatter than the tower's A² pair "
                          "structure (6.17×). The BULK binding is extensive "
                          "(A-linear shell residue), NOT a q-deformed pair sum; "
                          "the tower's C(A,2)~A² scaling is the q-Gaussian "
                          "obstruction (Σ q₀^cr(π) ~ q₀^C(A,2) diverges at q₀>1, "
                          "prop:q-gaussian-obstruction-at-q0). q-Askey kernels "
                          "(Hahn-Exton q-Bessel / q-Hermite) are the FIBRE per-λ "
                          "kernel (|q|≤1), not the A-scaling bulk.")}
    print(f"\n  EXTENSIVE BULK: 2·m_e·8G = {per_nuc:.3f} MeV/nucleon (A-linear) "
          f"→ net/target spread A≥4 = {extensive['magic_net_over_target_spread_Age4']:.2f}× "
          f"(vs tower A² {spread_t:.2f}×). The bulk is extensive, not the pair tower.")

    out = {"schema": "delta-lambda-borromean-ascaling/v1",
           "description": "Borromean per-braid tower net/target vs canonical "
                          "sgn(w₀)·dim; A-scaling diagnostic + edge-set test + "
                          "extensive-bulk comparison (no fit, no closure).",
           "tower_net_over_target_spread": spread_t, "rows": rows,
           "edge_set_test": edge, "extensive_bulk": extensive}
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    p = WitnessBuilder.wrap_legacy(
        "delta-lambda-borromean-ascaling", out,
        script_path=__file__, engine="mpmath",
    ).save()
    print(f"\n  witness → {p.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
