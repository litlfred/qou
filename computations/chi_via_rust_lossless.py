#!/usr/bin/env python3
"""Lossless per-λ χ at q₀ via the Rust `chi_q_via_gp` path — ANY atom (Z,N).

Generalizes `chi_4he_via_rust_lossless.py` (hard-coded ⁴He) to any nuclide. The
pure-Python matrix-M producer (`chi_at_q0_via_matrix_m_mpfr.py`) builds the full
dim×dim seminormal per partition — infeasible past H₁₂ (the ⁵Li H₁₅ mpmath run
spends ~9 s on a single dim-90 λ; dims reach the thousands). The canonical Rust
`pyhecke_native.chi_q_via_gp` returns the exact Laurent character per λ in ~20 ms
**independent of dim V_λ**, so a whole nucleus is seconds:

    ⁴He H₁₂ (77 λ) ≈ 2 s · ⁵Li H₁₅ (176 λ) ≈ 4 s · ⁶Li H₁₈ (385 λ) ≈ 8 s

The matrix-M backend was verified to MATCH `chi_q_via_gp` to the 50-dps floor
(18/18 partitions D/T/³He/⁴He, PR #2062 §8), so this Rust producer yields the
SAME values the matrix-M producer would — fast and lossless (no max_dim cap, no
skipped-max-dim placeholders). It consumes the closed-form y_λ tower
(`y_lambda_tower_infra.py`, n>12) so tr_M(q₀) = Σ_λ y_λ·χ_λ is the complete
1-ppQ Wedderburn trace.

Convention: sign-only crossings (chi_q_via_gp) — matches the D/T/³He/⁴He lossless
matrix-M caches (#2089). NOT the averaged-crossing binding trace.

Output: chi-{atom}-h{n}-at-q0-50dps-matrix-m.witness.json (one per atom; the
active-set consumers read this format transparently).

Usage:  python3 chi_via_rust_lossless.py 5Li 6Li [7Li 8Be ...]
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp

# Standalone high-precision compute script: enforce the 50-dps floor at module
# load so compute_atom / _ensure_y_lambda are correct when imported as a library,
# not only under main().
mp.mp.dps = 50

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from tr_m_wenzl_bridge_mpfr import _load_y_lambda  # noqa: E402
from per_irrep_pole_atom import ATOMS, ATOM_ALIASES, parts_of  # noqa: E402
from derived_chi_catalogue_matrix_m import _word_for_braid_word_3a  # noqa: E402
from derived_chi_catalogue_matrix_m_mpfr import chi_rust_at_q_mpf  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def _ensure_y_lambda(n: int) -> None:
    """Guarantee the canonical y_λ witness has a table for H_n — extend if not.

    ARBITRARY n: y_λ is the closed-form principal specialization (O(p(n)·n) mpf
    ops, no recursion), so there is no cap — any nucleus's H_n is covered
    on-demand. The only wall for the FULL Wedderburn χ below is p(n) (partition
    count), not y_λ.
    """
    W = json.loads((HERE / "y-lambda-mpfr-witness.json").read_text(encoding="utf-8"))
    if str(n) not in W.get("tables_by_n", {}):
        from y_lambda_tower_infra import extend_y_lambda_tower
        print(f"     (y_λ tower has no H{n}; extending closed-form, gated)",
              flush=True)
        extend_y_lambda_tower(n)   # closed-form, gated, non-destructive merge


def compute_atom(atom: str, q: mp.mpf) -> dict:
    """Lossless χ cache for one atom via Rust chi_q_via_gp. Writes the witness."""
    Z, N = ATOMS[atom]
    n_strands, word = _word_for_braid_word_3a(Z, N)
    n = n_strands
    out = HERE / f"chi-{atom}-h{n}-at-q0-50dps-matrix-m.witness.json"

    # Idempotent / resumable: a COMPLETE cache (lossless, all λ) is reused as-is
    # so a batch re-run (e.g. to refresh the summary witness) never recomputes a
    # finished nucleus.
    if out.exists():
        cached = json.loads(out.read_text(encoding="utf-8"))
        if (not cached.get("tr_M_partial", True)
                and cached.get("n_partitions") == cached.get("n_partitions_total")):
            print(f"  {atom:>10} cached ({cached['n_partitions']} λ, complete) "
                  f"— skip recompute", flush=True)
            return {"atom": atom, "n_strands": n, "Z": Z, "N": N,
                    "n_partitions": cached["n_partitions"],
                    "tr_M_at_q0": cached["tr_M_at_q0"],
                    "compute_time_sec": cached.get("compute_time_sec", 0.0),
                    "cache_path": str(out), "reused": True}

    _ensure_y_lambda(n)                 # arbitrary n: extend the y_λ tower on-demand
    y_table = _load_y_lambda(n, None)   # closed-form tower covers any n
    shapes = list(parts_of(n))

    t0 = time.monotonic()
    per_partition = []
    running = mp.mpf(0)
    print(f"  {atom:>10} H{n}: {len(shapes)} partitions via Rust chi_q_via_gp",
          flush=True)
    for i, shape in enumerate(shapes):
        shape_t = tuple(shape)
        y_lam = y_table.get(shape_t)
        if y_lam is None:
            continue
        t1 = time.monotonic()
        chi = chi_rust_at_q_mpf(shape_t, n_strands, word, q)
        contrib = mp.mpf(str(y_lam)) * chi
        running += contrib
        per_partition.append({
            "partition": list(shape_t),
            "y_lambda": str(y_lam),
            "chi_lambda": mp.nstr(chi, 50),
            "contribution": mp.nstr(contrib, 50),
            "compute_time_sec": round(time.monotonic() - t1, 4),
        })
        if (i + 1) % 40 == 0:
            print(f"     [{i+1}/{len(shapes)}] {time.monotonic()-t0:.1f}s", flush=True)
    elapsed = time.monotonic() - t0

    payload = {
        "computation": f"chi-{atom}-h{n}-at-q0-50dps-matrix-m",
        "description": (
            f"Lossless per-λ χ^λ(β_atomic({Z},{N}))={atom} at q_0, 50 dps, ALL "
            f"{len(per_partition)} partitions of S_{n} via the canonical Rust "
            f"chi_q_via_gp path (sign-only crossings; matches the matrix-M "
            f"backend to the 50-dps floor, PR #2062 §8). No max_dim cap — "
            f"feasible at any n because χ_λ is dim-independent (~20 ms/λ). "
            f"y_λ from the closed-form tower (y_lambda_tower_infra.py)."
        ),
        "producer": "rust-chi-q-via-gp-lossless",
        "convention": "sign-only-crossings",
        "q_0_50dps": str(q),
        "dps": 50,
        "n_strands": n,
        "atom": atom,
        "Z": Z, "N": N,
        "n_partitions": len(per_partition),
        "n_partitions_total": len(shapes),
        "max_dim": None,
        "n_skipped_max_dim": 0,
        "tr_M_partial": False,
        "partial": False,
        "compute_time_sec": round(elapsed, 2),
        "tr_M_at_q0": str(running),
        "by_partition": per_partition,
    }
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  {atom:>10} LOSSLESS: {len(per_partition)} λ, "
          f"tr_M(q0)={mp.nstr(running,16)}, {elapsed:.1f}s  →  {out.name}",
          flush=True)
    return {"atom": atom, "n_strands": n, "Z": Z, "N": N,
            "n_partitions": len(per_partition), "tr_M_at_q0": str(running),
            "compute_time_sec": round(elapsed, 2), "cache_path": str(out)}


def main() -> int:
    mp.mp.dps = 50
    raw = sys.argv[1:] or ["5Li", "6Li"]
    atoms = [ATOM_ALIASES.get(a, a) for a in raw]
    q = mp.mpf(Q_50_DIGIT_STR)
    t0 = time.monotonic()   # WitnessBuilder durationMs = monotonic() − start_time
    print("=" * 84)
    print(" Lossless per-λ χ at q₀ via Rust chi_q_via_gp — general (any atom)")
    print(f"   q₀ = {Q_50_DIGIT_STR[:22]}…")
    print("=" * 84)
    results = []
    for atom in atoms:
        if atom not in ATOMS:
            print(f"  {atom}: not in ATOMS, skip", flush=True)
            continue
        results.append(compute_atom(atom, q))

    wb = WitnessBuilder("chi-via-rust-lossless-general", engine="python",
                        start_time=t0)
    wb.set_description(
        "Lossless per-λ χ(q₀) caches via Rust chi_q_via_gp for arbitrary nuclides "
        "(generalizes chi_4he_via_rust_lossless.py). χ_λ is dim-independent "
        "(~20 ms/λ) so any H_n is seconds; consumes the closed-form y_λ tower for "
        "n>12. Produces the canonical chi-{atom}-h{n}-...-matrix-m.witness.json "
        "the active-set / binding consumers read. Sign-only convention; matches "
        "the matrix-M backend to the 50-dps floor (#2062 §8)."
    )
    wb.add_data("atoms", [r["atom"] for r in results])
    wb.add_data("results", results)
    wb.add_data("total_time_sec", round(time.monotonic() - t0, 2))
    out = wb.save()
    print("-" * 84)
    print(f" done: {len(results)} nuclide(s) in {time.monotonic()-t0:.1f}s")
    print(f" Witness: {out}")
    return 0 if results else 1


if __name__ == "__main__":
    raise SystemExit(main())
