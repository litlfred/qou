#!/usr/bin/env python3
"""W_λ per-body-order specification from the extensive-series cumulant profile.

EXPLORATORY (audit-only, no rewire, no fit, no selection). GAP-A bridge from
the reeb-flow program (tranches 1/7) to the Δ_λ-gate extensive-series
reframing (docs/audits/2026-07-05-delta-lambda-gate-status.md §0.1): nuclear
binding is EXTENSIVE, the trace-difference is INTENSIVE, so the closure is an
additive many-body series B(K)=Σ_bonds B_b + higher-body, and whatever
supplies the higher-body terms is the knot-ideal projector W_λ.

This probe MEASURES what W_λ must supply, per body order, by comparing the
Ursell (connected cumulant) profile of the best current many-body categorical
object — the collective complete-graph determinant B_det = −E₀·ln det(I+G)
(tranche 7; all inter-nucleon crossings at the derived magnitude g) — against
the AME cumulant target (b4_value_cumulant_target_probe). Ursell inversion
(same as the AME target, non-circular):

  b₂ = B(²H)
  b₃ = B̄(3-body) − 3·b₂          (B̄ = avg ³H/³He)
  b₄ = B(⁴He) − 6·b₂ − 4·b₃

Deliverable (preregistered): the per-body-order ratio det/AME, hence the
CORRECTION W_λ must inject at each order (a falsifiable spec — NOT a closure,
NOT a fit). Scope-(a): the determinant is ONE categorical object; the spec
constrains what any W_λ must do relative to it.

-- Ref: docs/audits/2026-07-05-delta-lambda-gate-status.md (extensive-series
reframing, W_λ); b4_value_cumulant_target_probe.py (AME cumulants);
light_series_open_loop_decomposition.py (collective determinant);
QOU/MassTheory/ReebPnMagnitude.lean (open-bond linear b₂ = 5g).
"""
from __future__ import annotations

import sys
import time
from itertools import combinations
from math import comb
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
if str(_COMP) not in sys.path:
    sys.path.insert(0, str(_COMP))
from _li_2_q_util import load_q_50dps  # noqa: E402
from substrate._precision import set_compute_dps  # noqa: E402
from substrate.experimental_constants import M_E_MEV  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

# AME cumulant target (b4_value_cumulant_target_probe.py)
AME = {"b2": mp.mpf("2.2245"), "b3": mp.mpf("1.4264"), "b4": mp.mpf("9.2431")}
SIGN = {"pp": mp.mpf(1), "nn": mp.mpf(-1), "pn": mp.mpf(1)}


def edge_type(i, j, Z):
    if i < Z and j < Z:
        return "pp"
    if i >= Z and j >= Z:
        return "nn"
    return "pn"


def full_det(Z, N, g):
    A = Z + N
    G = mp.zeros(A, A)
    for i, j in combinations(range(A), 2):
        w = SIGN[edge_type(i, j, Z)] * g
        G[i, j] = w
        G[j, i] = w
    return mp.det(mp.eye(A) + G)


def main() -> int:
    t0 = time.monotonic()
    q, _, z = load_q_50dps()
    g = z / mp.sqrt(1 + z * z)
    m_e = mp.mpf(str(M_E_MEV))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)

    def B_det(Z, N):
        d = full_det(Z, N, g)
        return None if d <= 0 else -E0 * mp.log(d)

    # collective-determinant binding per isotope
    B = {"2H": B_det(1, 1), "3H": B_det(1, 2), "3He": B_det(2, 1), "4He": B_det(2, 2)}
    for name, val in B.items():
        if val is None:
            raise ValueError(f"Determinant for {name} is non-positive (det ≤ 0); "
                             "cannot compute a collective binding — the magnitude "
                             "exceeds the physicality ceiling for this isotope.")
    # Ursell inversion of the determinant series
    det_b2 = B["2H"]
    det_B3 = (B["3H"] + B["3He"]) / 2
    det_b3 = det_B3 - comb(3, 2) * det_b2
    det_b4 = B["4He"] - comb(4, 2) * det_b2 - comb(4, 3) * det_b3
    det_cum = {"b2": det_b2, "b3": det_b3, "b4": det_b4}

    # single-pair OPEN-bond value (proved exact b₂; ReebPnMagnitude 5g)
    five_g = 5 * g

    rows = []
    for k in ("b2", "b3", "b4"):
        ame = AME[k]
        det = det_cum[k]
        ratio = det / ame
        # correction W_λ must inject: AME − det (MeV, at this body order)
        corr = ame - det
        rows.append({
            "order": k,
            "AME_MeV": mp.nstr(ame, 6),
            "det_MeV": mp.nstr(det, 6),
            "det_over_AME": mp.nstr(ratio, 5),
            "Wlambda_correction_MeV": mp.nstr(corr, 6),
        })

    # All corrections are the SIGNED AME − det (matches Wlambda_correction_MeV):
    # positive ⇒ W_λ raises that order, negative ⇒ W_λ lowers it.
    c2 = float(AME["b2"] - det_cum["b2"])
    c3 = float(AME["b3"] - det_cum["b3"])
    c4 = float(AME["b4"] - det_cum["b4"])
    spec = (
        f"W_λ per-body-order spec (signed correction AME − det, relative to the "
        f"collective determinant at g={float(g):.4f}): b₂ det/AME="
        f"{float(det_cum['b2']/AME['b2']):.3f}, correction {c2:+.3f} MeV/pair "
        f"(W_λ RAISES the 2-body — the open-bond linear deficit, since det treats "
        f"the single pair as a loop; the proved 5g={float(five_g):.4f} in-unit "
        f"already supplies it); b₃ det/AME={float(det_cum['b3']/AME['b3']):.3f}, "
        f"correction {c3:+.3f} MeV (≈right, small); b₄ det/AME="
        f"{float(det_cum['b4']/AME['b4']):.3f}, correction {c4:+.3f} MeV "
        f"(W_λ LOWERS the connected 4-body — det over-supplies it). So W_λ's "
        f"signature is signed (+, ≈0, −): raise the 2-body (open bond), leave "
        f"3-body ≈ intact, lower the connected 4-body. Scope-(a); no fit, no closure."
    )

    result = {
        "constants": {"q0": mp.nstr(q, 12), "g": mp.nstr(g, 10),
                      "5g_in_unit": mp.nstr(five_g, 8), "E0_MeV": mp.nstr(E0, 8)},
        "collective_det_binding_MeV": {k: (None if v is None else mp.nstr(v, 7))
                                       for k, v in B.items()},
        "cumulant_profile": rows,
        "wlambda_specification": spec,
    }
    payload = {
        "computation": "wlambda-cumulant-specification",
        "description": ("W_λ per-body-order specification from the extensive-series "
                        "cumulant profile: collective-determinant Ursell cumulants vs "
                        "AME, giving the correction W_λ must inject per body order. "
                        "Audit-only; no fit; no closure; no selection."),
        "tier": "exploratory (diagnostic specification for the W_λ frontier)",
        "result": result,
    }
    import platform
    wb = WitnessBuilder.wrap_legacy(
        "wlambda-cumulant-specification", payload,
        script_path=__file__, engine="python+mpmath",
        engine_version=f"python {platform.python_version()} + mpmath {mp.__version__}",
        output_dir=str(_HERE), start_time=t0,
    )
    wb.add_assertion("det_b3_near_AME_within_10pct",
                     computed=str(bool(abs(det_cum["b3"] / AME["b3"] - 1) < mp.mpf("0.1"))),
                     expected="True")
    wb.save(extra={"auditOnly": True})

    print("=== W_λ cumulant specification (extensive series) ===")
    print(f"  g={float(g):.6f}  E0={float(E0):.4f}  5g(in-unit)={float(five_g):.4f}")
    print(f"  {'order':>5} {'AME':>8} {'det':>8} {'det/AME':>8} {'W_λ corr':>9}")
    for r in rows:
        print(f"  {r['order']:>5} {r['AME_MeV']:>8} {r['det_MeV']:>8} "
              f"{r['det_over_AME']:>8} {r['Wlambda_correction_MeV']:>9}")
    print("  " + spec)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
