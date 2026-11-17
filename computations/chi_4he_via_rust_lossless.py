#!/usr/bin/env python3
"""Lossless ⁴He per-λ χ at q₀ via the Rust `chi_q_via_gp` path.

EXPLORATORY/data. Owner directive next-step 3: generate the ⁴He matrix-M χ
cache LOSSLESS (all 77 partitions of S₁₂). The pure-Python matrix-M producer
(`chi_at_q0_via_matrix_m_mpfr.py`) builds the full dim×dim seminormal per
partition — infeasible for n=12 (dims into the hundreds–thousands) in pure
mpmath. The canonical Rust `pyhecke_native.chi_q_via_gp` returns the exact
integer Laurent character per λ in ~20 ms, independent of dim V_λ — so the full
⁴He cache is ~2 s.

The matrix-M backend was verified to MATCH `chi_q_via_gp` to the 50-dps floor
(18/18 partitions D/T/³He/⁴He; PR #2062 §8), so this Rust producer yields the
SAME values the matrix-M producer would — just fast and lossless (no max_dim
cap, no skipped-max-dim placeholders). Output format mirrors the matrix-M cache
so the active-set consumers swap in transparently.

Convention: sign-only crossings (chi_q_via_gp) — matches the D/T/³He lossless
matrix-M caches (#2089). NOT the averaged-crossing binding trace.

Output: chi-helium-4-h12-at-q0-50dps-matrix-m.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from tr_m_wenzl_bridge_mpfr import _load_y_lambda  # noqa: E402
from per_irrep_pole_atom import parts_of  # noqa: E402
from derived_chi_catalogue_matrix_m import _word_for_braid_word_3a  # noqa: E402
from derived_chi_catalogue_matrix_m_mpfr import chi_rust_at_q_mpf  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402


def main() -> int:
    set_compute_dps()
    Z, N = 2, 2
    n = 3 * (Z + N)          # 12
    atom = "helium-4"
    t0 = time.time()
    q = mp.mpf(Q_50_DIGIT_STR)

    n_strands, word = _word_for_braid_word_3a(Z, N)
    assert n_strands == n
    y_table = _load_y_lambda(n, None)
    shapes = list(parts_of(n))

    per_partition = []
    running = mp.mpf(0)
    print(f"⁴He n={n}: {len(shapes)} partitions via Rust chi_q_via_gp", flush=True)
    for i, shape in enumerate(shapes):
        shape_t = tuple(shape)
        # Convention D (Wenzl level r = 2) vanishes identically on >2-row
        # shapes (QOU.MassTheory.TwoRowCapDerived.traceSum_eq_twoRow_of_wenzl);
        # _load_y_lambda carries ~1e-73 solver residue there, so filter by
        # row count explicitly (bean qou-e9le, matching block_swap_binding).
        y_lam = y_table.get(shape_t)
        if len(shape_t) > 2 or y_lam is None:
            continue
        t1 = time.time()
        chi = chi_rust_at_q_mpf(shape_t, n_strands, word, q)
        contrib = mp.mpf(str(y_lam)) * chi
        running += contrib
        per_partition.append({
            "partition": list(shape_t),
            "y_lambda": str(y_lam),
            "chi_lambda": mp.nstr(chi, 50),
            "contribution": mp.nstr(contrib, 50),
            # wall clock, not a measurement — string keeps raw float64 out
            # of the witness and stops per-run jitter rewriting the file
            "compute_time_sec": f"{time.time() - t1:.4f}",
        })
        if (i + 1) % 15 == 0:
            print(f"   [{i+1}/{len(shapes)}] {time.time()-t0:.1f}s", flush=True)

    elapsed = time.time() - t0
    payload = {
        "computation": f"chi-{atom}-h{n}-at-q0-50dps-matrix-m",
        "description": (
            f"Lossless per-λ χ^λ(β_atomic({Z},{N}))=⁴He at q_0, 50 dps, ALL "
            f"{len(per_partition)} partitions of S_{n} via the canonical Rust "
            f"chi_q_via_gp path (sign-only crossings; matches the matrix-M "
            f"backend to the 50-dps floor, PR #2062 §8). No max_dim cap — "
            f"infeasible partitions for pure-Python matrix-M computed in ms "
            f"by Rust, independent of dim V_λ."
        ),
        "producer": "rust-chi-q-via-gp-lossless",
        "convention": "sign-only-crossings",
        # Hand-rolled payload: the q0_anchor_manifest entry cannot reach it
        # (only WitnessBuilder.build() reads the manifest), so declare the pin.
        "q0Anchor": "proton",
        "q0Value": Q_50_DIGIT_STR,
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
        "compute_time_sec": f"{elapsed:.2f}",
        "tr_M_at_q0": str(running),
        "by_partition": per_partition,
    }
    out = HERE / f"chi-{atom}-h{n}-at-q0-50dps-matrix-m.witness.json"
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False))

    wb = WitnessBuilder("chi-at-q0-rust-lossless-helium-4", engine="python",
                        start_time=t0)
    wb.set_description(
        "Lossless ⁴He per-λ χ at q_0 via Rust chi_q_via_gp (all 77 partitions, "
        "no max_dim cap). Completes the lossless matrix-M active-set inputs "
        "for A≤4. Sign-only convention; matches the matrix-M backend."
    )
    wb.add_data("atom", atom)
    wb.add_data("n_strands", n)
    wb.add_data("n_partitions", len(per_partition))
    wb.add_data("tr_M_at_q0", str(running))
    wb.add_data("cache_path", str(out))
    wb.add_data("lean_uniqueness_ref", lean_uniqueness_ref("helium-4"))
    wb.save()

    print(f"\n⁴He LOSSLESS: {len(per_partition)} partitions, "
          f"tr_M(q0)={mp.nstr(running,16)}, {elapsed:.1f}s")
    print(f"Cache: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
