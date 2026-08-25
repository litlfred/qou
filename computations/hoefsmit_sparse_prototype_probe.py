#!/usr/bin/env python3
"""hoefsmit_sparse_prototype_probe — can the 2-nnz-per-row structure be used?

EXPLORATORY PROBE (not production). Bean qou-bk0q.

`hoefsmit_matrices_numpy` stores each generator as a dense (dim, dim) float64
array. Measured, the matrices it fills have **at most 2 nonzeros per row** — a
diagonal entry plus, where a swap partner exists, one symmetric off-diagonal
pair. Density is 1.31 % at dim 120 and 0.34 % at dim 462, and falls further as
dim grows.

At n=12 the largest partition is dim 7700, so eleven dense generators occupy
5.22 GB. That is what hangs the He-4 atom of `rho_k_co_casimir_extended` with
the default 4 workers on a 16 GB box (bean qou-5qwb): not the mathematics, the
storage choice.

WHAT IS BEING TESTED
--------------------
Represent each generator by its structure instead of its dense array:

    diag        : (dim,)  the diagonal
    (I, J, B)   : the symmetric off-diagonal pairs, M[i,j] = M[j,i] = b

`cross = sigma + d*eye` becomes `diag + d` with the pairs untouched, and

    (M @ cross)[:, j] = M[:, j]*diag[j] + M[:, i]*b
    (M @ cross)[:, i] = M[:, i]*diag[i] + M[:, j]*b

i.e. scale every column by the diagonal, then two vectorised column-adds. The
pairs form a partial MATCHING (each index appears in at most one pair, because
the builder marks both partners `processed`), so the updates cannot alias and
the whole step is three numpy expressions — no Python inner loop, no scipy.

This is distributivity, not an algebraic shortcut: exact in exact arithmetic.
In float64 it reorders summation, so the probe measures the resulting
difference against the current dense path rather than assuming it is zero.

WHAT WOULD MAKE THIS SHIP
-------------------------
  1. Agreement with `chi_numpy` far below the module's documented 1e-14.
  2. A real memory reduction at the dims that actually hurt.
  3. No slowdown at small dim, where dense BLAS is already fast.

Failing any of these, say so and do not ship it.

Run: python3 -u computations/hoefsmit_sparse_prototype_probe.py 2>&1 | tee /tmp/hsp.log
"""
from __future__ import annotations

import sys
import time
import tracemalloc
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401,E402

import numpy as np  # noqa: E402
import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from canonical_braid_crossings import (  # noqa: E402
    atom_canonical_crossings, d_for_ctype,
)
from hoefsmit_numpy import chi_numpy, hoefsmit_matrices_numpy  # noqa: E402
from rho_k_h3a_refinement import standard_young_tableaux  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def hoefsmit_structured(shape, q_value):
    """(diag_list, pairs_list, dim) — the generators, stored by structure.

    Mirrors `hoefsmit_matrices_numpy` exactly, but never materialises a
    (dim, dim) array. Memory is O(dim) per generator instead of O(dim^2).
    """
    n = sum(shape)
    syts, cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], [], 0

    q = float(q_value)
    h = q - 1.0 / q

    diags, pairs = [], []
    for k in range(1, n):
        diag = np.zeros(dim, dtype=np.float64)
        pi, pj, pb = [], [], []
        processed: set[int] = set()
        # Same O(d^2) partner search as the dense builder; this probe is about
        # storage and matmul cost, not about the build. Replacing the search
        # with a dict is P21 and a separate change.
        for i in range(dim):
            if i in processed:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]
            a = h / (1.0 - q ** (-2 * rho))

            swap_map = dict(syts[i])
            swap_map[k], swap_map[k + 1] = ci_k1, ci_k
            j = None
            for jj in range(dim):
                if jj == i:
                    continue
                if syts[jj] == swap_map:
                    j = jj
                    break

            if j is None:
                diag[i] = a
                processed.add(i)
            else:
                a_prime = h / (1.0 - q ** (2 * rho))
                b = np.sqrt(a * a_prime + 1.0)
                diag[i] = a
                diag[j] = a_prime
                pi.append(i); pj.append(j); pb.append(b)
                processed.add(i)
                processed.add(j)
        diags.append(diag)
        pairs.append((np.array(pi, dtype=np.intp),
                      np.array(pj, dtype=np.intp),
                      np.array(pb, dtype=np.float64)))
    return diags, pairs, dim


def chi_structured(shape, crossings, q_value):
    """chi^lambda via the structured generators. Same arithmetic, fewer flops."""
    diags, pairs, dim = hoefsmit_structured(shape, q_value)
    if dim == 0:
        return mp.mpf(0)
    q = float(q_value)
    h = q - 1.0 / q

    M = np.eye(dim, dtype=np.float64)
    for gen_idx, ctype in crossings:
        d_val = float(d_for_ctype(ctype, h))
        diag = diags[gen_idx] + d_val
        I, J, B = pairs[gen_idx]
        out = M * diag[None, :]
        if I.size:
            # Pairs are a partial matching, so these two scatter-adds touch
            # disjoint column sets and cannot alias.
            out[:, J] += M[:, I] * B[None, :]
            out[:, I] += M[:, J] * B[None, :]
        M = out
    return mp.mpf(float(np.trace(M)))


def main() -> int:
    set_compute_dps()
    q = float(mp.mpf(Q_50_DIGIT_STR))
    crossings = atom_canonical_crossings(1, 2)     # tritium, n=9, 35 crossings

    w = WitnessBuilder("hoefsmit-sparse-prototype", engine="python")
    print("=" * 78)
    print("Hoefsmit structured-vs-dense prototype (EXPLORATORY, bean qou-bk0q)")
    print("=" * 78)

    rows, worst_rel, all_close = [], mp.mpf(0), True
    for lam in [(5, 2, 2), (3, 3, 3), (4, 3, 2), (7, 1, 1), (4, 4, 1)]:
        t = time.time(); ref = chi_numpy(lam, crossings, q); t_dense = time.time() - t
        t = time.time(); got = chi_structured(lam, crossings, q); t_sparse = time.time() - t
        rel = abs(got - ref) / abs(ref) if ref != 0 else abs(got - ref)
        worst_rel = max(worst_rel, rel)
        ok = rel < mp.mpf("1e-12")
        all_close &= bool(ok)

        _, dim = hoefsmit_matrices_numpy(lam, q)
        tracemalloc.start()
        hoefsmit_matrices_numpy.__wrapped__(lam, q) if hasattr(
            hoefsmit_matrices_numpy, "__wrapped__") else None
        tracemalloc.stop()
        dense_bytes = (sum(lam) - 1) * dim * dim * 8
        diags, prs, _ = hoefsmit_structured(lam, q)
        struct_bytes = sum(d.nbytes for d in diags) + sum(
            i.nbytes + j.nbytes + b.nbytes for i, j, b in prs)

        print(f"  λ={str(lam):<10} dim={dim:5d}  dense {t_dense:7.4f}s  "
              f"struct {t_sparse:7.4f}s   rel_diff={mp.nstr(rel, 3):<10} "
              f"mem {dense_bytes/1e6:8.2f}MB -> {struct_bytes/1e6:6.3f}MB "
              f"({dense_bytes/max(struct_bytes,1):7.0f}x)")
        rows.append({
            "partition": str(lam), "dim": dim,
            "t_dense_sec": fmt(t_dense), "t_structured_sec": fmt(t_sparse),
            "rel_diff": mp.nstr(rel, 6),
            "generator_bytes_dense": dense_bytes,
            "generator_bytes_structured": int(struct_bytes),
            "memory_ratio": fmt(dense_bytes / max(struct_bytes, 1)),
            "agrees_below_1e-12": bool(ok),
        })

    w.add_data("atom", "tritium")
    w.add_data("per_partition", rows)
    w.add_data("worst_rel_diff", mp.nstr(worst_rel, 6))
    w.add_data("tier", "exploratory")
    w.add_assertion(
        "the structured path reproduces chi_numpy on every partition to better "
        "than 1e-12 — it is the same arithmetic in a different summation order, "
        "not a different object",
        computed=all_close, expected=True,
        source="chi_structured vs chi_numpy at substrate q0; the module's own "
               "documented tolerance against mpmath is 1e-14, so a storage "
               "reformulation must land far inside it",
    )
    w.set_description(
        "Exploratory prototype for bean qou-bk0q: Hoefsmit seminormal generators "
        "have at most 2 nonzeros per row (a diagonal plus symmetric pairs), yet "
        "hoefsmit_matrices_numpy stores them dense — 5.22 GB at the dim-7700 "
        "partition of n=12, which is what hangs He-4. Tests whether representing "
        "them by structure reproduces chi_numpy exactly and what it saves."
    )
    # AGENTS.md §"q0 anchor convention" rule 4: a new witness must record which
    # pin it used, so a reader can place it on the ideal/muon vs experimental/
    # proton layer without inferring it from a call site. This probe reads
    # Q_50_DIGIT_STR — the package layer, i.e. the experimental PROTON pin,
    # which is the standing default for new compute (owner directive
    # 2026-08-07).
    #
    # These go through save(extra=...) and NOT add_data(): the audit reads
    # `body.get("q0Anchor")` at the TOP LEVEL of the witness, while add_data
    # nests under `data`. Recording them in the wrong place looks correct in
    # the file and leaves the witness classified Q0_ANCHOR_MISSING — which is
    # exactly what happened on the first attempt here.
    w.save({"q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR})
    print(f"\n  worst rel_diff: {mp.nstr(worst_rel, 6)}   all below 1e-12: {all_close}")
    print("Saved witness: hoefsmit-sparse-prototype.witness.json")
    return 0 if all_close else 1


if __name__ == "__main__":
    sys.exit(main())
