#!/usr/bin/env python3
"""Probe: bar-parity loading of the LINEAR Markov trace under binding —
second test of the isospin-asymmetry pattern (mirror pairs vs N=Z).

EXPLORATORY (no production rewire, no fit). Companion to
`gram_norm_binding_probe.py` §bar-parity: the Gram-norm (quadratic) split
found that N = Z isotopes (²H, ⁴He) bind bar-parity-neutrally while the
A = 3 mirror pair splits antisymmetrically (³H sheds bar-odd weight under
binding, ³He gains it). The dense seminormal sweep caps at n = 3A = 12,
so the only mirror pair it reaches is ³H/³He. This probe re-tests the
SAME question at the linear-trace level, where the fine-Bratteli transfer
engine (`tr_m_atom_zn`) reaches n = 21 at the full 50-dps floor:

    parity(W) = (tr(q₀) − tr(q₀⁻¹)) / (tr(q₀) + tr(q₀⁻¹))     (signed odd/even)
    Δ_parity  = parity(atom) − parity(free)

for ²H, ⁴He, ⁶Li (N = Z controls) and the mirror pairs ³H/³He and
⁷Li/⁷Be. Prediction from the Gram-level pattern: Δ_parity ≈ 0 for N = Z;
opposite signs within each mirror pair.

Both legs use the q-parameterised word path (`atom_braid_word_3A(q=…)`
inside `tr_m_atom_zn(q=…)`) so the q₀ and q₀⁻¹ evaluations are internally
consistent (same flavor-split convention), mirroring the choice in the
Gram probe and the dashboard's entanglement table.

PRECISION: mpmath 50-dps throughout (the transfer engine's native floor)
— unlike the float64 Gram probe, this one is at the production precision
floor. Still EXPLORATORY in status (observation, not a wired claim).

Emits `mirror-parity-linear-trace-probe.witness.json` (audit-only).

Usage:
    python3 -u probes/mirror_parity_linear_trace_probe.py 2>&1 | tee /tmp/mirror_parity_probe.log
"""
from __future__ import annotations

# Path bridge (probes/ cluster subdirectory — flat-namespace imports).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time  # noqa: E402

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

# (name, Z, N, class): N=Z controls + the two feasible mirror pairs.
ISOTOPES = [
    ("2H", 1, 1, "N=Z"),
    ("3H", 1, 2, "mirror A=3"),
    ("3He", 2, 1, "mirror A=3"),
    ("4He", 2, 2, "N=Z"),
    ("6Li", 3, 3, "N=Z"),
    ("7Li", 3, 4, "mirror A=7"),
    ("7Be", 4, 3, "mirror A=7"),
]


def _parity(t0: "mp.mpf", ti: "mp.mpf"):
    """Signed odd/even ratio (t(q₀) − t(q₀⁻¹)) / (t(q₀) + t(q₀⁻¹))."""
    den = t0 + ti
    return (t0 - ti) / den if den != 0 else None


def main() -> int:
    set_compute_dps()
    q0 = mp.mpf(str(Q0))
    qi = 1 / q0
    rows = []
    for name, Z, N, cls in ISOTOPES:
        n = 3 * (Z + N)
        t0w = time.time()
        ta0, tf0, _, _ = tr_m_atom_zn(Z, N, q=q0, dps=50)
        tai, tfi, _, _ = tr_m_atom_zn(Z, N, q=qi, dps=50)
        p_atom = _parity(ta0, tai)
        p_free = _parity(tf0, tfi)
        d_par = (p_atom - p_free) if (p_atom is not None and p_free is not None) else None
        rows.append({
            "iso": name, "Z": Z, "N": N, "n": n, "class": cls,
            "parity_atom": float(p_atom) if p_atom is not None else None,
            "parity_free": float(p_free) if p_free is not None else None,
            "delta_parity": float(d_par) if d_par is not None else None,
            "tr_atom_q0": mp.nstr(ta0, 20), "tr_atom_qi": mp.nstr(tai, 20),
            "tr_free_q0": mp.nstr(tf0, 20), "tr_free_qi": mp.nstr(tfi, 20),
            "wall_sec": round(time.time() - t0w, 2),
        })
        print(f"  {name:<4} n={n:<3} [{cls:>10}] parity atom={float(p_atom):+.6f} "
              f"free={float(p_free):+.6f} Δ={float(d_par):+.6f} "
              f"({rows[-1]['wall_sec']}s)", flush=True)

    print("\n| iso | class | parity atom | parity free | Δ parity (binding) |")
    print("|---|:--|--:|--:|--:|")
    for r in rows:
        print(f"| {r['iso']} | {r['class']} | {r['parity_atom']:+.6f} "
              f"| {r['parity_free']:+.6f} | {r['delta_parity']:+.6f} |")

    # pattern checks: N=Z deltas small; mirror pairs opposite-signed
    nz = [r for r in rows if r["class"] == "N=Z"]
    max_nz = max(abs(r["delta_parity"]) for r in nz)
    pairs = {"A=3": ("3H", "3He"), "A=7": ("7Li", "7Be")}
    by = {r["iso"]: r for r in rows}
    opposite = {k: by[a]["delta_parity"] * by[b]["delta_parity"] < 0
                for k, (a, b) in pairs.items()}
    min_mirror = min(abs(by[i]["delta_parity"])
                     for p in pairs.values() for i in p)
    print(f"\n  max |Δ| over N=Z controls: {max_nz:.2e}")
    print(f"  min |Δ| over mirror-pair members: {min_mirror:.2e}")
    for k, (a, b) in pairs.items():
        print(f"  {k}: Δ({a}) = {by[a]['delta_parity']:+.6f}, "
              f"Δ({b}) = {by[b]['delta_parity']:+.6f} — "
              f"{'OPPOSITE signs' if opposite[k] else 'same sign'}")

    builder = WitnessBuilder("mirror-parity-linear-trace-probe", engine="mpmath")
    builder.set_description(
        "Bar-parity loading of the linear Markov trace under binding: "
        "N=Z controls vs the A=3 and A=7 mirror pairs (second test of the "
        "Gram-probe isospin-asymmetry pattern).")
    builder.add_parameter("q0", mp.nstr(q0, 30))
    builder.add_parameter("dps", 50)
    builder.add_parameter("parity_def",
                          "(tr(q0) - tr(1/q0)) / (tr(q0) + tr(1/q0)), signed")
    builder.add_data("rows", rows)
    # VERDICT (recorded as data, not assertions — the prediction FAILED and
    # that is the finding, not a compute error): the Gram-level sign
    # antisymmetry does NOT transfer to the linear trace. The linear parity
    # saturates → 1 with n (tr(q₀⁻¹)/tr(q₀) → 0 exponentially), so Δ_parity
    # shrinks with n regardless of isotope class; both mirror pairs shift
    # with the SAME sign. Only the A=3 magnitude asymmetry survives
    # (|Δ(³H)| ≈ 16×|Δ(³He)|). The antisymmetric bar-parity loading is a
    # property of the QUADRATIC (operator-space Gram) observable, invisible
    # to the linear trace.
    builder.add_data("prediction_checks", {
        "mirror_pairs_opposite_signed": {k: bool(v) for k, v in opposite.items()},
        "nz_controls_more_neutral_than_mirrors": bool(max_nz < min_mirror),
        "verdict": "REFUTED at the linear-trace level (scope (a): this "
                   "observable, alone; the Gram-level observation stands)",
        "max_abs_delta_nz": max_nz,
        "min_abs_delta_mirror": min_mirror,
        "a3_magnitude_asymmetry": abs(by["3H"]["delta_parity"])
        / abs(by["3He"]["delta_parity"]),
    })
    builder.add_assertion(
        name="all_isotopes_computed_finite_parity",
        computed=float(sum(1 for r in rows
                           if r["parity_atom"] is not None
                           and r["parity_free"] is not None)),
        expected=float(len(ISOTOPES)), tolerance=0.0,
        unit="isotopes with finite parity ratios (compute validity)",
        source="transfer-engine evaluation at q0 and 1/q0, 50 dps.",
    )
    builder.add_assertion(
        name="a3_mirror_magnitude_asymmetry_present",
        computed=0.0 if abs(by["3H"]["delta_parity"])
        > 5 * abs(by["3He"]["delta_parity"]) else 1.0,
        expected=0.0, tolerance=0.0,
        unit="boolean (0 = |Δ(3H)| > 5×|Δ(3He)| at equal n)",
        source="the surviving (magnitude-level) mirror asymmetry at A=3.",
    )
    builder.set_audit_only("docs/audits/2026-07-03-qbar-norm-repitch-assessment.md")
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
