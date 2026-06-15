#!/usr/bin/env python3
"""
Production atomic Markov-trace witness via Markov-axiom recursive ascent.

For each atom (Z, N) in the spectrum p, n, D, T, ³He, ⁴He, ⁵Li, ⁶Li:

  1. Build the production atomic braid `β_atom` via
     `mass_at_3A_proper.atom_braid_word_3A`.
  2. Reduce in `H_{3A}(q)` via incremental Gröbner–Shirshov
     (`markov_peel.incremental_reduced_element`) — interleaved
     reduce + multiply that keeps intermediate term count bounded.
  3. Take the canonical Markov trace via the recursive Markov-axiom
     ascent (`markov_trace_canonical.tr_M_element`, `simplify=False`).
  4. Evaluate the symbolic result at q = q₀ to 30 digits.
  5. Cross-check against `atomic-tr-m-mpfr-50dps.witness.json`
     (Hoefsmit + Wenzl bridge) for the atoms it covers.

This is the **production** atomic Markov-trace witness — the Hoefsmit
path materialises dim-up-to-462 sympy matrices per partition and is
infeasible for A ≥ 4 (the headline target of #508 / PR #516).  The
recursive-ascent path computes ⁴He end-to-end in ~60 seconds.

Witness: `markov-peel-atomic-tr-m.witness.json`
Reference: prop:markov-pair-z2 (QOU narrative)

Usage:
    python folio-assistant/computations/markov_peel_atomic_witness.py
    python folio-assistant/computations/markov_peel_atomic_witness.py --include-li
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import argparse
import json
import sys
import time
from pathlib import Path

import sympy as sp
import mpmath

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from markov_peel import incremental_reduced_element  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A     # noqa: E402
from markov_trace_canonical import tr_M_element       # noqa: E402
from hecke_symbolic import q as q_sym                  # noqa: E402
from q_parameter import Q as Q0                        # noqa: E402
from witness_base import WitnessBuilder                # noqa: E402

# Per CLAUDE.md / Gemini-flagged precision policy: pin a high-precision
# floor at the module level so all symbolic→numeric casts respect it.
# 50 dps matches the Hoefsmit + Wenzl bridge witness this script
# cross-checks against (`atomic-tr-m-mpfr-50dps.witness.json`).
mpmath.mp.dps = 50


# Atom spectrum.  Beyond ⁴He is gated by `--include-li` since GS reduce
# scales ~10× per A unit (about 10 minutes for ⁵Li).
ATOMS_DEFAULT = [
    ("proton",   1, 0),
    ("neutron",  0, 1),
    ("deuteron", 1, 1),
    ("tritium",  1, 2),
    ("helium-3", 2, 1),
    ("helium-4", 2, 2),
]
ATOMS_LITHIUM = [
    ("lithium-5", 3, 2),
    ("lithium-6", 3, 3),
]


def _load_bridge_witness() -> dict[str, str]:
    """Return atom -> tr_M(q₀) string from the Hoefsmit + Wenzl bridge
    witness, for cross-check.  Empty dict if the file is missing.
    """
    f = _pb.witness_path("atomic-tr-m-mpfr-50dps.witness.json", HERE)
    if not f.exists():
        return {}
    data = json.loads(f.read_text())
    return {e["atom"]: e["tr_M_at_q0_50dps"] for e in data["results"]}


def compute_atom(Z: int, N: int) -> dict:
    """Compute one row of the witness for atom (Z, N)."""
    A = Z + N
    n_strands = 3 * A
    word = atom_braid_word_3A(Z, N)

    t0 = time.time()
    elem = incremental_reduced_element(word, max_iterations_per_step=2000)
    t_reduce = time.time() - t0

    t0 = time.time()
    tr_sym = tr_M_element(elem, n_strands, simplify=False)
    t_trace = time.time() - t0

    t0 = time.time()
    # Evaluate at the current mpmath precision floor (50 dps), then
    # convert to mpf so the full precision survives.  Casting to a
    # Python float here would silently truncate to ~15-17 digits and
    # defeat the high-precision evaluation.
    tr_at_q0_mpf = mpmath.mpf(
        str(tr_sym.subs(q_sym, Q0).evalf(mpmath.mp.dps))
    )
    t_eval = time.time() - t0

    try:
        ops = sp.count_ops(tr_sym)
    except Exception:  # noqa: BLE001
        ops = -1

    # Format the witness value at full mpmath precision so downstream
    # cross-checks against `atomic-tr-m-mpfr-50dps.witness.json`
    # (Hoefsmit + Wenzl bridge) compare apples-to-apples.
    return {
        "Z": Z,
        "N": N,
        "A": A,
        "n_strands": n_strands,
        "word_length": len(word),
        "reduced_term_count": len(elem.terms),
        "trace_sympy_ops": int(ops),
        "tr_M_at_q0": mpmath.nstr(
            tr_at_q0_mpf, mpmath.mp.dps, strip_zeros=False
        ),
        "elapsed_reduce_sec": round(t_reduce, 3),
        "elapsed_trace_sec": round(t_trace, 3),
        "elapsed_evalf_sec": round(t_eval, 3),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--include-li", action="store_true",
        help="Also compute ⁵Li and ⁶Li (≥ 10 min reduce per atom)",
    )
    parser.add_argument(
        "--out", type=str, default="markov-peel-atomic-tr-m.witness.json",
        help="Witness output filename (relative to computations/)",
    )
    args = parser.parse_args()

    bridge = _load_bridge_witness()

    atoms = list(ATOMS_DEFAULT)
    if args.include_li:
        atoms.extend(ATOMS_LITHIUM)

    print(
        "Atomic tr_M(β) via Markov-axiom recursive ascent (#508 / PR #516)",
        flush=True,
    )
    print("=" * 70, flush=True)

    rows = []
    total_t = time.time()
    for label, Z, N in atoms:
        print(f"\n  === {label} (Z={Z}, N={N}, A={Z + N}) ===", flush=True)
        try:
            row = compute_atom(Z, N)
            row["atom"] = label
            print(
                f"    word_len={row['word_length']:3d} "
                f"reduce={row['elapsed_reduce_sec']:6.1f}s "
                f"terms={row['reduced_term_count']:5d} "
                f"trace={row['elapsed_trace_sec']:6.2f}s "
                f"ops={row['trace_sympy_ops']:>6d}",
                flush=True,
            )
            print(f"    tr_M(q₀) = {row['tr_M_at_q0']}", flush=True)
            if label in bridge:
                # Compare at full mpmath precision — strings round-trip
                # losslessly through `mpf(str(...))`.
                bridge_val = mpmath.mpf(bridge[label])
                got = mpmath.mpf(row["tr_M_at_q0"])
                diff = abs(got - bridge_val)
                row["bridge_witness_value"] = bridge[label]
                row["abs_diff_vs_bridge"] = mpmath.nstr(diff, 6)
                # Tolerance scales with the precision floor — at 50 dps
                # we expect agreement to ~10^{-(dps − 5)}.
                tol = mpmath.mpf(10) ** -(mpmath.mp.dps - 5)
                tag = "OK" if diff < tol else "MISMATCH"
                print(
                    f"    bridge = {bridge[label]}  "
                    f"|diff| = {mpmath.nstr(diff, 3)}  {tag}",
                    flush=True,
                )
            else:
                row["bridge_witness_value"] = None
                row["abs_diff_vs_bridge"] = None
                print(
                    f"    (no bridge witness for {label} — "
                    "this row is the production reference)",
                    flush=True,
                )
            rows.append(row)
        except Exception as exc:  # noqa: BLE001
            print(f"    FAILED: {type(exc).__name__}: {exc}", flush=True)
            rows.append({
                "atom": label, "Z": Z, "N": N, "A": Z + N,
                "error": f"{type(exc).__name__}: {exc}",
            })

    total_elapsed = time.time() - total_t
    print(
        f"\n  === total wall = {total_elapsed:.1f}s ===",
        flush=True,
    )

    w = WitnessBuilder("markov-peel-atomic-tr-m", engine="sympy")
    w.set_description(
        "Production atomic Markov trace tr_M(β_atom) at q = q₀ via the "
        "Markov-axiom recursive-ascent path (markov_peel + "
        "markov_trace_canonical, #508 / PR #516).  Cross-checks against "
        "atomic-tr-m-mpfr-50dps.witness.json (Hoefsmit + Wenzl bridge) "
        "for the atoms it covers (proton, neutron, D, T, ³He); ⁴He and "
        "beyond are first-time computations enabled by this rewrite."
    )
    w.set_content_block("prop:markov-pair-z2")
    w.add_parameter("q0", str(Q0))
    w.add_data(
        "method",
        "incremental_reduced_element + tr_M_element(simplify=False)",
    )
    w.add_data("results", rows)
    w.add_data("bridge_witness_compared",
                "atomic-tr-m-mpfr-50dps.witness.json")
    out_path = w.save()
    print(f"\n  → wrote {out_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
