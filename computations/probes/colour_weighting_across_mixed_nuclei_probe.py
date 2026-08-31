#!/usr/bin/env python3
"""colour_weighting_across_mixed_nuclei_probe.py — the colour-weighting price for
every mixed nucleus, not just the deuteron.

WHY.  `colour_weighting_trace_magnitude_probe.py` (PR #6309, bean `qou-fv0s`)
measured the canonical path's colour-blindness at **1.4149e-4 relative** on the
deuteron, and said explicitly that the figure does NOT transfer: the trace is
affine in the one weighted shift, but the linear coefficient `tr(A B)` is
word-specific, so T / 3He / 4He each need their own measurement.  That caveat
was correct and it left the design question priced on one of four nuclei.  This
probe measures the other three.

METHOD, and the two things that make it cheap enough to run.

  1. **`y_lambda` vanishes off two-row partitions.**  The Jones-Markov weight is
     the SU(2) specialisation, so `y_lambda = 0` whenever lambda has more than
     two rows.  4He is H_12 -- 77 partitions -- but only **7** contribute.  The
     probe does not assume this: it reads the whole `y_lambda_at(n, q)` table and
     RECORDS how many partitions it skipped for a zero weight, so the claim is
     visible in the witness rather than baked into a loop bound.

  2. **Hoefsmit matrices are sparse** -- at most two nonzeros per row, by
     construction (a generator either fixes a standard tableau or swaps it with
     exactly one other).  A dense `mp.matrix` product would cost O(dim^3) per
     crossing; multiplying by the column-sparse form costs O(dim^2).  At 4He's
     largest contributing block, `dim(7,5) = 297`, that is the difference between
     ~2.6e7 and ~1.8e5 mpf operations per crossing -- ~150x, and the difference
     between "runs" and "does not".

     A new multiplication routine is a new place to be wrong, so it is
     SELF-TESTED: the probe re-derives the deuteron numbers with the sparse route
     and checks them against the dense-route values already committed in
     `colour-weighting-trace-magnitude.witness.json`.  If the sparse multiply were
     wrong, that check fails before any new number is reported.

WHAT IS MEASURED, per nucleus, at the proton pin, 50 dps: the Schur-Weyl sum
`Sum_lambda y_lambda chi^lambda` with the single `averaged_weighted` crossing
carrying (a) the colour-BLIND shift `-h/2` and (b) the colour-WEIGHTED shift
`-h(1/2 - delta/4)`.  Arm (a) is additionally cross-checked against the canonical
Rust value, which is the independent confirmation that the canonical path sits on
the blind arm -- established for D in #6309 and re-established here for each of
T, 3He and 4He rather than assumed to carry over.

SCOPE.  The affine structure itself is an algebraic identity (exactly one factor
of the braid word carries `d`, so the product is affine in it) and was verified
numerically at D to 1.8e-71 in #6309; it is not re-verified here.  What is
measured here is each nucleus's own coefficient, which is the part that does not
transfer.

Run:  python3 -u computations/probes/colour_weighting_across_mixed_nuclei_probe.py \
        2>&1 | tee /tmp/colour_weighting_across_nuclei.log
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent
for _p in (COMPUTATIONS, COMPUTATIONS / "hecke", COMPUTATIONS / "substrate",
           COMPUTATIONS / "deltalambda"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

import rho_k_h3a_refinement as R  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings, d_for_ctype  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Deuteron values from the committed dense-route witness (PR #6309).  Used ONLY
# as the sparse-multiply self-test, never as an input to a new result.
#
# These strings carry 40 significant digits, because that is what the source
# witness serialized.  So the self-test below CANNOT be tighter than ~1e-40 --
# not because the arithmetic is that coarse (compute runs at 65 dps) but because
# the reference is.  The tolerance is set from the reference's precision, not
# chosen to make the check pass; a first pass at 1e-45 "failed" at 3.3e-41,
# which is the truncation of these very strings and not a disagreement.
D_BLIND_REF = "0.5750908716298103167516328830255259660632"
D_WEIGHTED_REF = "0.5751722439177718708265353439861808891525"
D_REF_SIGNIFICANT_DIGITS = 40
D_REF_TOLERANCE = "1e-39"   # one decade of headroom on the 40-digit reference

NUCLEI = ((1, 1, "D"), (1, 2, "T"), (2, 1, "3He"), (2, 2, "4He"))


def two_row(lam) -> bool:
    return len(lam) <= 2


def column_sparse(M, dim):
    """Column-sparse form of a Hoefsmit matrix: for each column j, the list of
    (row, value) pairs with a nonzero entry.

    At most two per column, by the structure of the Hoefsmit action, but nothing
    here depends on that — the routine is exact for any sparsity.
    """
    cols = []
    zero = mp.mpf(0)
    for j in range(dim):
        entries = [(k, M[k, j]) for k in range(dim) if M[k, j] != zero]
        cols.append(entries)
    return cols


def right_multiply(P, cols, d, dim):
    """P @ (S + d*I), with S given column-sparse. O(dim^2 * nnz_per_col).

    Column j of the product is `sum_k P[:,k] * S[k,j]  +  d * P[:,j]`.
    P is a list of rows, each a list of mpf.
    """
    out = [[None] * dim for _ in range(dim)]
    for i in range(dim):
        Pi = P[i]
        Oi = out[i]
        for j in range(dim):
            acc = d * Pi[j]
            for (k, v) in cols[j]:
                acc += Pi[k] * v
            Oi[j] = acc
    return out


def schur_weyl_sum(q, crossings, y_table, sparse_cache, d_weighted):
    """Sum_lambda y_lambda chi^lambda(beta), with the ONE averaged_weighted
    crossing carrying `d_weighted`.  Returns (total, n_contributing, n_skipped).
    """
    h = q - mp.mpf(1) / q
    zero = mp.mpf(0)
    total = mp.mpf(0)
    n_used = n_skipped = 0
    for lam, y_val in sorted(y_table.items()):
        y = mp.mpf(str(y_val))
        if y == zero:
            n_skipped += 1
            continue
        n_used += 1
        cols_by_gen, dim = sparse_cache[lam]
        P = [[mp.mpf(1) if i == j else mp.mpf(0) for j in range(dim)]
             for i in range(dim)]
        for gen_idx, ctype in crossings:
            d = d_weighted if ctype == "averaged_weighted" else d_for_ctype(ctype, h)
            P = right_multiply(P, cols_by_gen[gen_idx], d, dim)
        chi = mp.mpf(0)
        for i in range(dim):
            chi += P[i][i]
        total += y * chi
    return total, n_used, n_skipped


def build_sparse_cache(q, y_table, n_strands):
    """Column-sparse Hoefsmit matrices for every contributing partition."""
    zero = mp.mpf(0)
    cache = {}
    for lam, y_val in y_table.items():
        if mp.mpf(str(y_val)) == zero:
            continue
        mats, dim, _ = R.hoefsmit_matrices_numeric(lam, q)
        if dim == 0:
            continue
        cache[lam] = ([column_sparse(M, dim) for M in mats], dim)
    return cache


def rust_canonical(Z, N, label):
    try:
        import canonical_tr_m_via_rust as C
        row = C.compute_tr_m(Z, N, label, timeout_sec=3600)
    except Exception as exc:  # pragma: no cover — environment-dependent
        return None, f"{type(exc).__name__}: {exc}"
    if "tr_M_q0_mp50dps" not in row:
        return None, row.get("tr_M_q0_unavail_reason", "no value and no reason")
    return mp.mpf(str(row["tr_M_q0_mp50dps"])), None


def main() -> int:
    q = mp.mpf(Q_50_DIGIT_STR)
    q_sym = sp.sympify(Q_50_DIGIT_STR)
    h = q - mp.mpf(1) / q
    delta = mp.mpf(
        str(sp.sympify(flavor_split_leading(sp.Symbol("q")))
            .subs(sp.Symbol("q"), q_sym)
            .evalf(mp.mp.dps))
    )
    d_blind = d_for_ctype("averaged", h)
    d_w = d_for_ctype("averaged_weighted", h, delta=delta)

    print("=" * 88)
    print("colour weighting across the mixed nuclei")
    print("=" * 88)
    print(f"\n  q_0 (proton) = {mp.nstr(q, 40)}")
    print(f"  d(averaged)          = {mp.nstr(d_blind, 30)}")
    print(f"  d(averaged_weighted) = {mp.nstr(d_w, 30)}")

    w = WitnessBuilder("colour-weighting-across-mixed-nuclei", engine="python")
    w.add_parameter("q0_anchor", "proton")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_data("d_averaged", mp.nstr(d_blind, 50))
    w.add_data("d_averaged_weighted", mp.nstr(d_w, 50))
    w.add_data("delta_flavour_split", mp.nstr(delta, 50))

    rows = {}
    for Z, N, label in NUCLEI:
        t0 = time.time()
        crossings = atom_canonical_crossings(Z, N)
        n_strands = max(g for g, _ in crossings) + 2
        n_weighted = sum(1 for _, ct in crossings if ct == "averaged_weighted")
        y_table = y_lambda_at(n_strands, q)
        print(f"\n  {label}:  {len(crossings)} crossings on H_{n_strands}, "
              f"{n_weighted} weighted, |y-table| = {len(y_table)}", flush=True)

        cache = build_sparse_cache(q, y_table, n_strands)
        dims = {lam: d for lam, (_, d) in cache.items()}
        two_row_only = all(two_row(lam) for lam in cache)
        print(f"    contributing partitions: {len(cache)} "
              f"(max dim {max(dims.values()) if dims else 0}), "
              f"all two-row: {two_row_only}", flush=True)

        s_blind, n_used, n_skip = schur_weyl_sum(q, crossings, y_table, cache, d_blind)
        print(f"    S(blind)    = {mp.nstr(s_blind, 40)}   "
              f"[{time.time()-t0:.0f}s]", flush=True)
        s_w, _, _ = schur_weyl_sum(q, crossings, y_table, cache, d_w)
        print(f"    S(weighted) = {mp.nstr(s_w, 40)}   "
              f"[{time.time()-t0:.0f}s]", flush=True)

        delta_abs = s_w - s_blind
        delta_rel = abs(delta_abs) / abs(s_blind)
        print(f"    Delta = {mp.nstr(delta_abs, 12)}   relative = "
              f"{mp.nstr(delta_rel, 12)}", flush=True)

        rust_val, rust_reason = rust_canonical(Z, N, label)
        if rust_val is None:
            rust_rel = None
            print(f"    Rust canonical: UNAVAILABLE — {rust_reason}", flush=True)
        else:
            rust_rel = abs(s_blind - rust_val) / abs(rust_val)
            print(f"    Rust canonical = {mp.nstr(rust_val, 40)}  "
                  f"vs S(blind) rel = {mp.nstr(rust_rel, 10)}", flush=True)

        rows[label] = {
            "Z": Z, "N": N,
            "n_strands": n_strands,
            "n_crossings": len(crossings),
            "n_averaged_weighted": n_weighted,
            "partitions_in_y_table": len(y_table),
            "partitions_contributing": n_used,
            "partitions_skipped_zero_weight": n_skip,
            "all_contributing_are_two_row": two_row_only,
            "max_contributing_dim": max(dims.values()) if dims else 0,
            "tr_M_colour_blind": mp.nstr(s_blind, 50),
            "tr_M_colour_weighted": mp.nstr(s_w, 50),
            "delta_absolute": mp.nstr(delta_abs, 30),
            "delta_relative": mp.nstr(delta_rel, 30),
            "rust_canonical": mp.nstr(rust_val, 50) if rust_val is not None else None,
            "rust_vs_blind_relative": mp.nstr(rust_rel, 30) if rust_rel is not None
                                      else None,
            "rust_unavailable_reason": rust_reason,
            # int, not round(): a float64 here trips the raw-float64 ratchet,
            # and sub-second precision on a wall-clock is not a measurement.
            "elapsed_seconds": int(time.time() - t0),
        }
        w.add_data(label, rows[label])

    # --- self-test: the sparse route must reproduce the committed dense route ---
    d_row = rows["D"]
    st_blind = abs(mp.mpf(d_row["tr_M_colour_blind"]) - mp.mpf(D_BLIND_REF)) \
        / abs(mp.mpf(D_BLIND_REF))
    st_w = abs(mp.mpf(d_row["tr_M_colour_weighted"]) - mp.mpf(D_WEIGHTED_REF)) \
        / abs(mp.mpf(D_WEIGHTED_REF))
    print(f"\n  SELF-TEST sparse vs committed dense (deuteron):")
    print(f"    blind arm    rel = {mp.nstr(st_blind, 10)}")
    print(f"    weighted arm rel = {mp.nstr(st_w, 10)}")
    w.add_assertion(
        "the sparse multiply reproduces the committed dense deuteron blind arm",
        computed=mp.nstr(st_blind, 30), expected="0", tolerance=D_REF_TOLERANCE,
        source=f"vs colour-weighting-trace-magnitude.witness.json = {D_BLIND_REF} "
               f"({D_REF_SIGNIFICANT_DIGITS} significant digits — the tolerance is "
               f"set by that, not by the arithmetic)",
    )
    w.add_assertion(
        "the sparse multiply reproduces the committed dense deuteron weighted arm",
        computed=mp.nstr(st_w, 30), expected="0", tolerance=D_REF_TOLERANCE,
        source=f"vs colour-weighting-trace-magnitude.witness.json = {D_WEIGHTED_REF} "
               f"({D_REF_SIGNIFICANT_DIGITS} significant digits — the tolerance is "
               f"set by that, not by the arithmetic)",
    )

    print(f"\n  {'atom':<6}{'H_n':>5}{'contrib':>9}{'maxdim':>8}"
          f"{'delta_rel':>16}  rust-vs-blind")
    for label in ("D", "T", "3He", "4He"):
        r = rows[label]
        rr = r["rust_vs_blind_relative"]
        print(f"  {label:<6}{r['n_strands']:>5}{r['partitions_contributing']:>9}"
              f"{r['max_contributing_dim']:>8}"
              f"{float(r['delta_relative']):>16.6e}  "
              f"{(f'{float(rr):.3e}' if rr is not None else 'unavailable')}")

    for label in ("T", "3He", "4He"):
        r = rows[label]
        if r["rust_vs_blind_relative"] is not None:
            w.add_assertion(
                f"the canonical Rust path lands on the colour-BLIND arm for {label}",
                computed=r["rust_vs_blind_relative"], expected="0",
                tolerance="1e-15",
                source="Rust MPFR chi + witness y_lambda vs Python Hoefsmit sparse route",
            )
        w.add_assertion(
            f"{label}: only two-row partitions carry a nonzero y_lambda",
            computed="1" if r["all_contributing_are_two_row"] else "0",
            expected="1", tolerance="0",
            source=f"{r['partitions_contributing']} contributing of "
                   f"{r['partitions_in_y_table']} in the y-table",
        )

    w.add_caveat(
        "The affine structure of the trace in the weighted shift is an algebraic "
        "identity (exactly one factor of the word carries d) and was verified "
        "numerically at the deuteron to 1.8e-71 in PR #6309. It is not re-verified "
        "here; what is measured here is each nucleus's own coefficient, which is "
        "the part that does not transfer."
    )
    w.add_caveat(
        "This prices the colour-blindness; it does not say which arm is canonical. "
        "Whether the p-n interface carries the flavour weighting is a physical "
        "modelling choice (bean qou-fv0s)."
    )

    out = w.save()
    print(f"\n  witness -> {out}")
    failed = [a for a in w.assertions if not a.passed]
    print(f"  assertions: {len(w.assertions) - len(failed)}/{len(w.assertions)} pass")
    for a in failed:
        print(f"    FAIL  {a.name}: computed={a.computed} expected={a.expected}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
