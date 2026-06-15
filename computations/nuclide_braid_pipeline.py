#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical character table at q_0.
"""
General per-nuclide braid → χ_λ pipeline, with explicit ⋈_K witnessing.

THE GOAL (user direction 2026-06-01): build the FULL pipeline for ANY
nuclide/isotope (Z, N) — even though the Hecke dimension grows like
(3A)! — then optimize. And: **the inter-nucleon coupling ⋈_K must be
saved/witnessed** whenever the braid / Gröbner data is computed for a
nuclide, not left implicit.

## Why ⋈_K matters (the load-bearing finding, PR #1582)

A nucleus is NOT a free product of its nucleons.  Computing χ_λ from the
*disjoint* iterated Littlewood-Richardson product (free baseline)
over-counts by ~20× for ³He (Σχ_free = 865 vs Σχ_true = 45).  The
difference is exactly the inter-nucleon coupling generators ⋈_K — the
interface braids `σ_{3k+2}` between adjacent nucleon triples, with
coupling-type-dependent weights:

    p–p interface :  (c, d) = (1,  0   ),  multiplicity m_pp
    n–n interface :  (c, d) = (1, −h   ),  multiplicity m_nn
    p–n / n–p     :  (c, d) = (1, −h/2 ),  multiplicity m_pn

(h = ℏ_q at q_0).  These are the ⋈_K data.  This script extracts them
from `atom_braid_word_3A` and writes them into the witness as a
first-class `coupling_kappa` block, so any downstream consumer (mass
formula, real SDP, Gröbner basis reduction) reads the SAME coupling
structure rather than re-deriving it.

## What it produces (per nuclide)

  nuclide-braid-<sym>.witness.json
    data.coupling_kappa      — the ⋈_K interface list (gen idx, type,
                               c, d, multiplicity) — WITNESSED
    data.braid_word          — full (c, d, gen) triple list at H_{3A}
    data.per_partition       — {partition, dim, y_lambda, chi_lambda,
                               contribution} for every λ ⊢ 3A
    data.tr_M                — Σ_λ y_λ χ_λ / d_λ (Markov trace)

For A ≤ 4 this completes in seconds–minutes; for higher A it grows with
p(3A)·(3A)! and is the optimization target.  Correctness first.

Usage:  python3 nuclide_braid_pipeline.py --Z 2 --N 1            # ³He
        python3 nuclide_braid_pipeline.py --Z 3 --N 3 --sym Li6  # ⁶Li
        python3 nuclide_braid_pipeline.py --Z 2 --N 1 --max-dim 200   # cap
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import argparse
import json
import math
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
import sys

sys.path.insert(0, str(HERE))

# h = ℏ_q at q_0, and the q_0 value (for recording the coupling weights).
_QPIN = json.loads((_pb.witness_path("q-pinning-50-digit.witness.json", HERE)).read_text())
Q0_STR = _QPIN["derived_50_digit"]["q"]
H_STR = _QPIN["derived_50_digit"].get("hbar_q") or _QPIN["derived_50_digit"].get("h")


def sanitize_nan(val):
    if isinstance(val, dict):
        return {k: sanitize_nan(v) for k, v in val.items()}
    if isinstance(val, list):
        return [sanitize_nan(x) for x in val]
    if isinstance(val, float) and not math.isfinite(val):
        return None
    return val


def extract_coupling_kappa(Z: int, N: int, m_pp: int, m_pn: int, m_nn: int):
    """The ⋈_K interface data — coupling type + weight + multiplicity per
    inter-nucleon generator.  This is what must be witnessed."""
    ordering = ["p"] * Z + ["n"] * N
    A = Z + N
    kappa = []
    for k in range(A - 1):
        nuc, nxt = ordering[k], ordering[k + 1]
        gen = 3 * k + 2
        if nuc == "p" and nxt == "p":
            typ, c, d_sym, mult = "pp", 1.0, "0", m_pp
        elif nuc == "n" and nxt == "n":
            typ, c, d_sym, mult = "nn", 1.0, "-h", m_nn
        else:
            typ, c, d_sym, mult = "pn", 1.0, "-h/2", m_pn
        kappa.append({
            "interface_index": k,
            "generator": gen,
            "between": f"{nuc}{k}-{nxt}{k + 1}",
            "coupling_type": typ,
            "c": c,
            "d_symbolic": d_sym,
            "multiplicity": mult,
        })
    return kappa


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--Z", type=int, required=True)
    ap.add_argument("--N", type=int, required=True)
    ap.add_argument("--sym", type=str, default=None, help="nuclide symbol, e.g. He3")
    ap.add_argument("--m-pp", type=int, default=1)
    ap.add_argument("--m-pn", type=int, default=1)
    ap.add_argument("--m-nn", type=int, default=1)
    ap.add_argument("--max-dim", type=int, default=None,
                    help="skip partitions with dim S^λ above this (compute cap)")
    ap.add_argument("--precision", choices=["mpmath50", "double"],
                    default="mpmath50",
                    help="χ_λ precision: mpmath50 (50-dps, default, full "
                         "high-precision chain) or double (float64, fast). "
                         "y_λ is ALWAYS canonical 50-dps regardless.")
    args = ap.parse_args()
    Z, N = args.Z, args.N
    A = Z + N
    n_strands = 3 * A
    sym = args.sym or f"Z{Z}N{N}"

    # Import the heavy engine lazily so --help stays fast.
    import mpmath as mp
    mp.mp.dps = 50
    from mass_at_3A_proper import atom_braid_word_3A
    from hecke_characters import partitions_of
    from char_fast import chi_lambda_fast
    from schur_principal_mpmath import y_lambda_at_q0_mpmath
    q0 = mp.mpf(Q0_STR)

    kappa = extract_coupling_kappa(Z, N, args.m_pp, args.m_pn, args.m_nn)
    word = atom_braid_word_3A(Z, N, m_pp=args.m_pp, m_pn=args.m_pn,
                              m_nn=args.m_nn, include_inter=True)
    from char_fast import chi_lambda_fast_mp

    print(f"{sym}: Z={Z} N={N} A={A} → H_{n_strands}, braid length {len(word)}")
    print(f"  ⋈_K interfaces: {[(k['between'], k['coupling_type']) for k in kappa]}")

    shapes = list(partitions_of(n_strands))
    print(f"  p({n_strands}) = {len(shapes)} partitions")

    # Canonical y_λ = s_λ(principal spec) / Z, normalised Σ y_λ f^λ = 1
    # (schur_principal_mpmath — matches the per-nucleus χ witnesses to ~1e-49).
    y_canon = y_lambda_at_q0_mpmath(n_strands, q0)

    def f_lambda(shape):
        """Integer dim f^λ = SYT count via the hook-length formula."""
        s = list(shape)
        cols = [0] * (s[0] if s else 0)
        for r in s:
            for j in range(r):
                cols[j] += 1
        prod = 1
        for i, row in enumerate(s):
            for j in range(row):
                prod *= (row - j - 1) + (cols[j] - i - 1) + 1
        return math.factorial(sum(s)) // prod

    # χ precision: "mpmath50" (50-dps, ~1e-49, DEFAULT — full high-precision
    # chain feeding the clarabel-MPFR SDP) or "double" (float64, fast, for
    # quick smoke tests only).  y_λ is ALWAYS the canonical 50-dps
    # principal-spec Schur weight regardless.
    use_mp = (args.precision == "mpmath50")
    q0_chi = q0 if use_mp else float(q0)

    per_partition = []
    total = mp.mpf(0)
    skipped = 0
    t0 = time.time()
    for idx, shape in enumerate(shapes):
        f_dim = f_lambda(shape)
        if args.max_dim is not None and f_dim > args.max_dim:
            skipped += 1
            continue
        if use_mp:
            chi_re = mp.re(chi_lambda_fast_mp(shape, word, q0))
        else:
            chi_re = mp.mpf(float(chi_lambda_fast(shape, word, q_val=q0_chi,
                                                  precision="double").real))
        y = y_canon[tuple(shape)]
        contrib = y * chi_re
        total += contrib
        per_partition.append({
            "partition": list(shape), "dim": f_dim,
            "y_lambda": mp.nstr(y, 50), "chi_lambda": mp.nstr(chi_re, 50),
            "contribution": mp.nstr(contrib, 50),
        })
        if (idx + 1) % 10 == 0 or idx == len(shapes) - 1:
            el = time.time() - t0
            print(f"    [{idx + 1}/{len(shapes)}] {el:.1f}s  tr_M(partial)={float(total):.8f}")
    total = float(total)

    witness = {
        "engine": "nuclide_braid_pipeline",
        "engineVersion": "0.1.0",
        "computation": (
            f"{sym} per-nuclide coupled braid → χ_λ table at q_0, with "
            "witnessed ⋈_K inter-nucleon coupling."
        ),
        "scriptFile": "nuclide_braid_pipeline.py",
        "data": {
            "nuclide": sym,
            "Z": Z, "N": N, "A": A, "n_strands": n_strands,
            "q_0": Q0_STR,
            "h": H_STR,
            # ── ⋈_K witnessed (user directive) ──
            "coupling_kappa": kappa,
            "coupling_multiplicities": {"m_pp": args.m_pp, "m_pn": args.m_pn,
                                        "m_nn": args.m_nn},
            "braid_word": [[float(c), float(d), int(g)] for (c, d, g) in word],
            "braid_length": len(word),
            # ── character table ──
            "n_partitions": len(shapes),
            "n_partitions_computed": len(per_partition),
            "n_partitions_skipped_dim_cap": skipped,
            "partial": skipped > 0,
            "max_dim_cap": args.max_dim,
            "per_partition": per_partition,
            "tr_M": total,
            "wall_seconds": time.time() - t0,
        },
    }
    out = HERE / f"nuclide-braid-{sym}.witness.json"
    out.write_text(json.dumps(sanitize_nan(witness), indent=2) + "\n")
    print(f"  tr_M = {total:.10f}   ({time.time() - t0:.1f}s, "
          f"{len(per_partition)}/{len(shapes)} partitions"
          f"{f', {skipped} skipped' if skipped else ''})")
    print(f"  wrote {out.name}  (⋈_K witnessed: {len(kappa)} interfaces)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
