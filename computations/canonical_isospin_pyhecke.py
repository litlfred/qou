#!/usr/bin/env python3
"""
Canonical Markov isospin test — OPTIMIZED via pyhecke.

Replaces the slow `SymbolicHeckeDivision` path
(`canonical_isospin_test.py`, ³He timed out >25 min) with the
optimized `pyhecke.trace.markov_trace_symbolic_eval` entry
point: numerical Markov trace at q_0 for atomic braids in
H_{3A}(q), routing through the optimized backend
(pyhecke_native PyO3 if available, Python+CRT otherwise).

Witness: canonical-isospin-pyhecke.witness.json
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent / "../../tools/pyhecke/python"))
import pyhecke

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0


def trace_atom(Z, N, include_inter=True, m_pp=1, m_pn=1, m_nn=1,
                precision=30):
    """tr_M(W_atom, q=q_0) via pyhecke.trace.markov_trace_symbolic_eval."""
    t0 = time.time()
    try:
        tr = pyhecke.trace.markov_trace_symbolic_eval(
            Z, N, include_inter, m_pp, m_pn, m_nn, float(Q0),
            precision=precision)
        return tr, time.time() - t0, None
    except Exception as exc:
        return None, time.time() - t0, f"{type(exc).__name__}: {exc}"


if __name__ == "__main__":
    import time
    start_time = time.monotonic()
    print("PYHECKE-OPTIMIZED CANONICAL MARKOV TRACE — T vs ³He vs others")
    print("=" * 80)
    print(f"q_0 = {float(Q0):.6f}")
    print(f"pyhecke version: {getattr(pyhecke, '__version__', '?')}")
    try:
        import pyhecke_native
        print(f"pyhecke_native: AVAILABLE")
    except ImportError:
        print(f"pyhecke_native: NOT installed (CRT/Python fallback)")
    try:
        crt_avail = pyhecke.trace.has_crt_backend()
        print(f"CRT backend:    {'AVAILABLE' if crt_avail else 'unavailable'}")
    except Exception:
        print(f"CRT backend:    unknown")
    print()

    cases = [
        ("p   (Z=1, N=0)", 1, 0, False),  # sanity
        ("n   (Z=0, N=1)", 0, 1, False),
        ("D   (Z=1, N=1)", 1, 1, True),
        ("T   (Z=1, N=2)", 1, 2, True),
        ("³He (Z=2, N=1)", 2, 1, True),
        ("⁴He (Z=2, N=2)", 2, 2, True),
    ]

    results = {}
    for label, Z, N, inter in cases:
        tr, dt, err = trace_atom(Z, N, include_inter=inter)
        if err:
            print(f"  {label}: ERROR ({dt:.2f}s)  {err}")
            results[label] = {"Z": Z, "N": N, "error": err,
                                "walltime_sec": dt}
        else:
            tr_real = tr if not hasattr(tr, 'imag') else (
                tr.real if abs(tr.imag) < 1e-9 else tr)
            print(f"  {label}: tr_M = {float(tr_real):+.10e}  ({dt:.3f}s)")
            results[label] = {
                "Z": Z, "N": N, "include_inter": inter,
                "tr_M_q0": float(tr_real),
                "walltime_sec": dt,
            }

    # Isospin comparison (T vs ³He)
    print("\n── ISOSPIN COMPARISON (T vs ³He) ──")
    T = results.get("T   (Z=1, N=2)")
    He3 = results.get("³He (Z=2, N=1)")
    if T and He3 and "error" not in T and "error" not in He3:
        diff = T["tr_M_q0"] - He3["tr_M_q0"]
        ratio = abs(T["tr_M_q0"] - He3["tr_M_q0"]) / max(
            abs(T["tr_M_q0"]), abs(He3["tr_M_q0"]))
        print(f"  tr_M(T)   = {T['tr_M_q0']:+.10e}")
        print(f"  tr_M(³He) = {He3['tr_M_q0']:+.10e}")
        print(f"  diff      = {diff:+.6e}  ({100*ratio:.4f}% relative)")
        print()
        # Speedup vs SymbolicHeckeDivision baseline
        speedup_T = 163.3 / max(T['walltime_sec'], 1e-6)
        speedup_3He = 1500.0 / max(He3['walltime_sec'], 1e-6)
        print(f"  Speedup vs SymbolicHeckeDivision:")
        print(f"    T:   {T['walltime_sec']:.3f}s  vs 163.3s baseline → "
              f"{speedup_T:.0f}× faster")
        print(f"    ³He: {He3['walltime_sec']:.3f}s vs >25 min timeout → "
              f"≥{speedup_3He:.0f}× faster")

    witness = {
        "computation": "canonical-isospin-pyhecke",
        "description": (
            "Canonical Markov trace via pyhecke.trace.markov_trace_symbolic_eval "
            "for atomic braids p, n, D, T, ³He, ⁴He.  Routes through the "
            "optimized backend (CRT/native).  Replaces the symbolic-q "
            "SymbolicHeckeDivision path which timed out on ³He at "
            ">25 min wallclock."
        ),
        "reference_blocks": [
            "prop:categorical-mass-markov",
            "thm:jones-markov-trace",
            "rem:commutative-crossing-energy",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": float(Q0),
            "precision": 30,
        },
        "results": results,
    }
    # Wrap legacy payload via WitnessBuilder.wrap_legacy for provenance
    # (engine, scriptFile, commitSha, scriptHash, computedAt) per the I14
    # witness-provenance audit. Preserves every original key verbatim.
    sys.path.insert(0, str(Path(__file__).parent))
    from witness_base import WitnessBuilder  # noqa: E402
    (WitnessBuilder
        .wrap_legacy("canonical-isospin-pyhecke", witness,
                     script_path=__file__, engine="python",
                     start_time=start_time)
        .save())
    out = Path(__file__).parent / "canonical-isospin-pyhecke.witness.json"
    print(f"\nWitness: {out}")
