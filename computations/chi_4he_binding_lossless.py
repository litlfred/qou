#!/usr/bin/env python3
"""Lossless ⁴He per-λ χ in the **binding** (color-weighted averaged-crossing)
convention at q₀, all 77 λ⊢12.

In the binding convention the inter-nucleon crossings are Hecke elements
`c·σ + d·1` (p-n → `σ − h·(½ − δ/4)`, n-n → `σ − h`, δ = flavor_split_leading(q₀)),
not braid generators. The dim-independent Rust binding character
`chi_q_atomic_all_partitions` evaluates `tr_λ(Π(c·σ+d·1))` for every λ⊢n in a
single call, with **no dim×dim seminormal** (the matrix-M producer is infeasible
at n = 12, dims to 7700). That is the default, fast path here (all 77 λ ≈ 10 s,
f64), and resolves the completeness of the binding cache (bean `b0vf`,
previously 27/77).

The default precision is the f64 Rust binding character; per-λ values agree with
the matrix-M 50-dps reference (the feasible-λ subset) to the f64 floor, which the
gate checks. A 50-dps per-λ pass for **all** 77 λ is available under `--exact`:
it reconstructs the binding word at full MPFR precision, collapses each maximal
same-generator run `Π(c·σ+d)` to a linear `a·σ + b·1` via `σ²=h·σ+1`, expands the
binomials into sign-only braid branches, and accumulates the dim-independent
`chi_lambda_all_partitions_mpfr` of each (correct, but ≫ slower than the atomic
path, which reduces the Hecke word once rather than per branch).

Output: chi-helium-4-h12-at-q0-50dps-binding.witness.json
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from itertools import product
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

import pyhecke_native as pn  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from tr_m_wenzl_bridge_mpfr import _load_y_lambda  # noqa: E402
from per_irrep_pole_atom import parts_of  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

GATE_F64 = mp.mpf("1e-5")   # f64 char vs the 50-dps matrix-M reference (rel·|χ|)


def _hp_binding_word(Z: int, N: int, q):
    """The ⁴He binding word as MPFR `(c, d, gen0)` triples (color-weighted p-n).
    Mirrors `mass_at_3A_proper.atom_braid_word_3A` but keeps every coefficient at
    the active mpmath precision instead of floating it."""
    from pyhecke.atom import nucleon_gen_chains
    from _li_2_q_util import flavor_split_leading
    h = q - 1 / q
    delta = flavor_split_leading(q)
    p_g0, p_g1 = nucleon_gen_chains(['u', 'u', 'd'], q=q)
    n_g0, n_g1 = nucleon_gen_chains(['u', 'd', 'd'], q=q)
    word, ordering, A = [], ['p'] * Z + ['n'] * N, Z + N
    for k, nuc in enumerate(ordering):
        g0, g1 = (p_g0, p_g1) if nuc == 'p' else (n_g0, n_g1)
        for c, d in g0:
            word.append((mp.mpf(c), mp.mpf(d), 3 * k))
        for c, d in g1:
            word.append((mp.mpf(c), mp.mpf(d), 3 * k + 1))
        if k < A - 1:
            nxt = ordering[k + 1]
            if nuc == 'p' and nxt == 'p':
                cd = (mp.mpf(1), mp.mpf(0))
            elif nuc == 'n' and nxt == 'n':
                cd = (mp.mpf(1), -h)
            else:
                cd = (mp.mpf(1), -h * (mp.mpf(1) / 2 - delta / 4))
            word.append((cd[0], cd[1], 3 * k + 2))
    return word


def _chi_binding_mpfr_exact(word, n, q, q_str, dps):
    """50-dps per-λ binding χ for ALL λ⊢n via Hecke-run collapse + sign-only
    branch expansion (no dim×dim matrix). Slow (one GP expansion per branch);
    the high-precision reference for the fast atomic path."""
    h = q - 1 / q
    gen_runs = []
    for c, d, g in word:
        if gen_runs and gen_runs[-1][0] == g:
            gen_runs[-1][1].append((c, d))
        else:
            gen_runs.append((g, [(c, d)]))
    binomials, layout = [], []
    for g, factors in gen_runs:
        a, b = mp.mpf(0), mp.mpf(1)
        for c, d in factors:
            a, b = a * c * h + a * d + b * c, a * c + b * d
        if b == 0:
            layout.append(('fix', g, a))
        else:
            layout.append(('bin', len(binomials)))
            binomials.append((g, a, b))
    nb = len(binomials)
    shapes = [tuple(s) for s in parts_of(n)]
    acc_terms = {s: [] for s in shapes}
    for choice in product((0, 1), repeat=nb):
        coeff, signed = mp.mpf(1), []
        for item in layout:
            if item[0] == 'fix':
                _, g, a = item
                coeff *= a
                signed.append((1, g + 1))
            else:
                g, a, b = binomials[item[1]]
                if choice[item[1]] == 1:
                    coeff *= a
                    signed.append((1, g + 1))
                else:
                    coeff *= b
        if coeff == 0:
            continue
        for part, chi_str in pn.chi_lambda_all_partitions_mpfr(n, signed, q_str, dps):
            acc_terms[tuple(part)].append(coeff * mp.mpf(chi_str))
    return {s: mp.fsum(t) for s, t in acc_terms.items()}, 2 ** nb


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--exact", action="store_true",
                    help="50-dps per-λ via the MPFR branch expansion (slow)")
    ap.add_argument("--dps", type=int, default=50)
    args = ap.parse_args()
    dps = args.dps
    mp.mp.dps = dps + 10
    Z, N, n = 2, 2, 12
    q = mp.mpf(Q_50_DIGIT_STR)
    q_str = mp.nstr(q, dps)
    t0 = time.time()

    word = _hp_binding_word(Z, N, q)
    shapes = [tuple(s) for s in parts_of(n)]

    n_branches = None
    if args.exact:
        acc, n_branches = _chi_binding_mpfr_exact(word, n, q, q_str, dps)
        precision = f"mpfr-{dps}dps-branch-expansion"
    else:
        # Default path: dim-independent MPFR binding character. The factors
        # (c, d) and q are passed as decimal strings to avoid the lossy f64
        # boundary; the Rust kernel reduces the Hecke word once per λ and
        # traces at `dps` precision (parallel over basis vectors per λ,
        # serial over partitions so the huge-dim λ⊢12 get all cores).
        cd_str = [(mp.nstr(c, dps), mp.nstr(d, dps), g + 1)
                  for c, d, g in word]   # 1-based gens, decimal strings
        acc = dict((tuple(p), mp.mpf(v))
                   for p, v in pn.chi_q_atomic_all_partitions_mpfr(
                       n, cd_str, q_str, dps))
        precision = "mpfr-50dps-rust-binding-atomic"

    # Gate against the matrix-M 50-dps binding reference (feasible λ subset).
    ref_path = HERE / "chi-helium-4-h12-at-q0-50dps.witness.json"
    max_rel = mp.mpf(0)
    n_ref = 0
    if ref_path.exists():
        for e in json.load(open(ref_path)).get("by_partition", []):
            s = tuple(e["partition"])
            if s in acc and "chi_lambda" in e:
                ref = mp.mpf(e["chi_lambda"])
                rel = abs(acc[s] - ref) / max(abs(ref), mp.mpf(1))
                max_rel = max(max_rel, rel)
                n_ref += 1
    # Both the default (MPFR atomic) and --exact (MPFR branch-expansion)
    # paths now compute at `dps` (50) precision, so both gate at 1e-25
    # against the matrix-M 50-dps reference.
    tol = mp.mpf("1e-25")
    gate_ok = (n_ref > 0) and (max_rel < tol)

    y_table = _load_y_lambda(n, None)
    per_partition, trM = [], mp.mpf(0)
    for s in shapes:
        y = y_table.get(s)
        rec = {"partition": list(s), "chi_lambda": mp.nstr(acc[s], dps)}
        if y is not None:
            contrib = mp.mpf(str(y)) * acc[s]
            trM += contrib
            rec["y_lambda"] = str(y)
            rec["contribution"] = mp.nstr(contrib, dps)
        per_partition.append(rec)

    elapsed = time.time() - t0
    print(f"⁴He binding χ ({precision}): {len(per_partition)}/{len(shapes)} λ⊢12")
    if n_branches:
        print(f"  branches: {n_branches}")
    print(f"  tr_M_binding(q0) = {mp.nstr(trM, 18)}")
    print(f"  gate vs matrix-M 50dps ref ({n_ref} λ): max rel = "
          f"{mp.nstr(max_rel, 6)}  {'PASS' if gate_ok else 'FAIL'} (tol {mp.nstr(tol,2)})")
    print(f"  {elapsed:.1f}s")

    payload = {
        "computation": "chi-helium-4-h12-at-q0-50dps-binding",
        "description": (
            f"Lossless per-λ χ^λ(β_atomic(2,2))=⁴He in the BINDING "
            f"(color-weighted averaged-crossing) convention at q_0, all "
            f"{len(per_partition)} λ⊢12, via the dim-independent Rust binding "
            f"character ({precision}). No dim×dim seminormal (matrix-M is "
            f"infeasible at n=12). Resolves the partial binding cache (bean "
            f"b0vf, was 27/77). Gated against the matrix-M 50-dps reference on "
            f"the feasible-λ subset."
        ),
        "producer": "chi-q-atomic-binding-lossless",
        "convention": "bring_color_weighted-averaged-crossings",
        "precision": precision,
        "q_0_50dps": str(q), "dps": dps, "n_strands": n,
        "atom": "helium-4", "Z": Z, "N": N,
        "n_partitions": len(per_partition), "n_partitions_total": len(shapes),
        "max_dim": None, "n_skipped_max_dim": 0, "partial": False,
        "n_branches": n_branches,
        "gate_vs_matrix_m_50dps_max_rel": mp.nstr(max_rel, 8),
        "gate_n_ref": n_ref,
        "tr_M_at_q0": str(trM),
        "compute_time_sec": round(elapsed, 2),
        "by_partition": per_partition,
    }
    out = HERE / "chi-helium-4-h12-at-q0-50dps-binding.witness.json"
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False))

    wb = WitnessBuilder("chi-at-q0-binding-lossless-helium-4", engine="python",
                        start_time=t0)
    wb.set_description(
        "Lossless ⁴He per-λ χ in the binding (color-weighted averaged-crossing) "
        "convention at q_0, all 77 λ⊢12, via the dim-independent Rust binding "
        "character (no dim×dim matrix). Resolves bean b0vf (was 27/77)."
    )
    wb.add_data("n_partitions", len(per_partition))
    wb.add_data("precision", precision)
    wb.add_data("tr_M_at_q0", str(trM))
    wb.add_data("gate_vs_matrix_m_50dps_max_rel", mp.nstr(max_rel, 8))
    wb.add_assertion(name="binding_chi_matches_matrix_m_reference",
                     computed=1 if gate_ok else 0, expected=1,
                     source="binding χ^λ agrees with the matrix-M 50-dps "
                            "reference on the feasible-λ subset within tol")
    wb.save()
    print(f"  Cache: {out}")
    return 0 if gate_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
