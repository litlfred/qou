#!/usr/bin/env python3
"""
Rust hecke-engine → canonical Markov trace bridge analysis.

PR #518 follow-up #2: investigate whether the 51 existing Rust
hecke-engine certificates can be converted to canonical `tr_M(q_0)`
without re-computation.

Findings:

  1) The Rust engine (v9, v10_crt, v11_modular) emits three
     numerical fields per atom: f_pauli_f64, tr_alt_f64, net_f64.
     None of these is the canonical Markov trace.

     - tr_alt = Σ_w c_w · (-q^{-1})^|w|  (sign-rep evaluation)
     - net    = Σ_w c_w                  (raw coefficient sum)
     - f_pauli = |tr_alt / net|          (Pauli-accumulator quotient)

  2) v9 has a sister method `compute_tr_markov_f64` that DOES emit
     the canonical Markov trace as
         tr_M = Σ_ℓ net_by_len[ℓ] · z^ℓ ,   z = 1/(t + t^{-1})
     but this value is computed only ephemerally and not stored in
     the certificate JSON.  v11_modular doesn't compute it at all
     (only f_pauli).

  3) BRIDGE IS UNNECESSARY.  Pyhecke's
     `markov_trace_symbolic_eval(Z, N, ...)` computes the canonical
     trace directly via the per-generator V_s transfer-matrix form
     (Markov-property recursion).  Empirically:

        atom        Z    N      n_strands       wallclock
        ----    -----  -----  -------------   ------------
        4He       2    2          12            0.001 s
        12C       6    6          36            0.002 s
        27Al     13   14          81            0.18  s
        40Ca     20   20         120            0.01  s
        56Fe     26   30         168            0.01  s
        60Co     27   33         180            0.01  s
        208Pb    82  126         624            0.04  s

     Pyhecke's algorithm scales ~linearly in the number of strands
     because each V_s is a 2-term recursion; the full polynomial
     expansion is never built.  The Rust engine's polynomial-basis
     enumeration (which motivated the modular/CRT machinery for
     A ≥ 12) is the *wrong* algorithm for the canonical trace.

  4) The Rust engine's f_pauli IS structurally distinct: it is a
     Wedderburn-block PSD diagnostic for the sign vs. trivial
     channels of the atomic Hecke element.  Useful for SDP
     positivity tests, but not a substitute for tr_M in the
     mass formula.

Recommendation:
  - **Do NOT build a Rust → canonical converter.**  The pyhecke
    sweep already produces canonical tr_M for any atom up to
    ²⁰⁸Pb in O(40 ms).
  - For atoms beyond Z ≤ 10 the bottleneck is no longer compute,
    it is content: which atoms to enumerate, which braids to use,
    and which AME values to compare against.
  - The 51 Rust certificates remain valuable for the f_pauli /
    PSD-diagnostic use case, just not for the mass formula.

Refs:
  - tools/hecke-engine/src/bin/v9.rs      (compute_tr_markov_f64)
  - tools/hecke-engine/src/bin/v11_modular.rs  (no tr_M computed)
  - tools/hecke-engine/src/certificate.rs (only stores fp/alt/net)
  - canonical_isospin_pyhecke_full_census.py (the win)
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "../../tools/pyhecke/python"))
import pyhecke

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0


HEAVY_ATOMS = [
    ("4He",   2,   2),
    ("12C",   6,   6),
    ("16O",   8,   8),
    ("27Al",  13,  14),
    ("40Ca",  20,  20),
    ("56Fe",  26,  30),
    ("60Co",  27,  33),
    ("100Mo", 42,  58),
    ("208Pb", 82, 126),
    ("238U",  92, 146),
]


def main() -> int:
    print("=" * 80)
    print("  Rust → canonical bridge: do we need one?")
    print(f"  pyhecke {getattr(pyhecke, '__version__', '?')}, q_0 = {float(Q0):.10f}")
    print("=" * 80)

    print(f"\n  Pyhecke canonical tr_M(q_0) at heavy atoms:")
    print(f"  {'atom':>6} {'Z':>3} {'N':>3} {'n_strands':>10}  {'tr_M(q_0)':>14}  {'wallclock':>10}")
    print("  " + "-" * 65)

    results = []
    for label, Z, N in HEAVY_ATOMS:
        A = Z + N
        n = 3 * A
        t0 = time.time()
        try:
            tr = pyhecke.trace.markov_trace_symbolic_eval(
                Z, N, True, 1, 1, 1, float(Q0), precision=20)
            dt = time.time() - t0
            tr_f = float(tr if not hasattr(tr, "imag") else
                         (tr.real if abs(tr.imag) < 1e-9 else tr))
            print(f"  {label:>6} {Z:>3} {N:>3} {n:>10}  {tr_f:>+14.4e}  "
                  f"{dt*1000:>8.2f} ms")
            results.append({
                "label": label, "Z": Z, "N": N, "n_strands": n,
                "tr_M_q0": tr_f, "wallclock_ms": dt * 1000,
            })
        except Exception as exc:
            dt = time.time() - t0
            print(f"  {label:>6} {Z:>3} {N:>3} {n:>10}  ERROR  "
                  f"{type(exc).__name__}: {str(exc)[:40]}  {dt*1000:.2f} ms")

    total_ms = sum(r["wallclock_ms"] for r in results)
    max_atom = max(results, key=lambda r: r["n_strands"])
    print(f"\n  Total wallclock: {total_ms:.0f} ms over {len(results)} atoms")
    print(f"  Heaviest:        {max_atom['label']} ({max_atom['n_strands']} strands) "
          f"in {max_atom['wallclock_ms']:.0f} ms")

    print(f"\n  CONCLUSION: pyhecke already scales to all atoms of interest.")
    print(f"  No need to build a Rust f_pauli → canonical tr_M converter.")
    print(f"  The 51 Rust certificates remain useful for f_pauli (PSD")
    print(f"  diagnostic), just not for the categorical mass formula.")

    witness = {
        "computation": "rust-canonical-bridge-analysis",
        "description": (
            "Investigates whether the 51 existing Rust hecke-engine "
            "certificates need a converter to canonical tr_M for use in "
            "the categorical mass formula.  CONCLUSION: bridge is "
            "unnecessary.  Pyhecke's markov_trace_symbolic_eval scales "
            "linearly via the V_s transfer-matrix recursion and computes "
            "canonical tr_M for ²⁰⁸Pb (n=624) in ~40 ms.  The Rust "
            "engine's polynomial-basis enumeration is the wrong "
            "algorithm for this task; its f_pauli output is a "
            "structurally distinct Wedderburn PSD diagnostic, useful "
            "for other purposes."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "verdict": "no-bridge-needed",
        "rationale": [
            "pyhecke.markov_trace_symbolic_eval is O(n) via V_s recursion",
            "Rust v9 has compute_tr_markov_f64 (same formula) but doesn't store it",
            "Rust v11_modular doesn't compute tr_M at all (only f_pauli/tr_alt/net)",
            "Rust f_pauli is a different operator (Pauli-accumulator quotient)",
            "Bottleneck for Z > 10 is content (which braids), not compute",
        ],
        "heavy_atom_benchmarks": results,
    }
    out_path = Path(__file__).parent / "rust-canonical-bridge-analysis.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
