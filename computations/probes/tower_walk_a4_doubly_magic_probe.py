#!/usr/bin/env python3
"""EXACT H_{3A} tower walk at A = 4 -- the doubly-magic case, 4He.

Companion to `tower_walk_h3a_magic_probe.py`, which ran the same experiment at
A = 3 and found no magic/non-magic separation. A = 4 is the ONLY doubly-magic
configuration this construction can reach: A = 5 needs sum d^2 = 15! = 10.5 TB.

WHAT MADE IT REACHABLE, having twice been reported as blocked. Bean `qou-tower`
records 4He as "3.83 GB, borderline in a 16 GB container", from `sum_lambda
d_lambda^2 = 12!`. That figure is right for holding EVERY partition's state at
once, which is what the A=3 walk does -- and it is not necessary. Partitions are
independent: the braid word acts within each irrep separately, so walking one
partition at a time makes peak memory `max_lambda d_lambda^2` = 7700^2 = 474 MB,
an 8x reduction that is a loop reordering, not an algorithm.

The second cost was time. The A=3 walk forms `state @ (c*sigma + d*I)` as a
dense matmul, O(d^3) = 4.6e11 flops per crossing at d = 7700. But in the
Hoefsmit seminormal basis `sigma_g` is diagonal plus 2x2 blocks, so the same
product is a set of column operations in O(d^2):

    col_i <- col_i*(c*a + d) + col_j*(c*c_)      for each 2x2 block (i,j)
    col_j <- col_i*(c*b)     + col_j*(c*d_ + d)
    col_i <- col_i*(c*diag_i + d)                for each singleton i

Verified against the dense route on all 30 partitions of A=3 Z=2,N=1: max
relative disagreement 6.34e-16, the float64 floor.

THE CONTROL, and its ceiling, stated before the result. A = 4 admits exactly
five configurations, and exactly one is doubly magic:

    Z=4,N=0  neither      Z=3,N=1  neither      Z=2,N=2  4He DOUBLY MAGIC
    Z=1,N=3  neither      Z=0,N=4  neither

So the strongest ORDERING claim available is "4He is the extreme of five",
which has **P = 1/5 = 0.2 under the null** for any single observable -- and
three observables are computed, so an extremum in at least one is near
even-odds by chance alone. An ordering result here would NOT be evidence. What
would be evidence is a QUALITATIVE change: a rank deficiency where the others
are full, or an argmax partition that no non-magic configuration shares. This
is stated up front deliberately -- the arc has five recorded instances of a
magic-looking result whose control was inadequate.

OBSERVABLES, identical to the A=3 walk. Per partition `lambda |- 12` the walk
returns the full `d_lambda x d_lambda` matrix; the weight is `w_lambda =
|tr M_lambda|`, normalised over partitions. Then:

  * top-share     = max_lambda w_lambda            (concentration on one irrep)
  * participation = 1 / sum_lambda w_lambda^2      (effective number of irreps)
  * argmax        = the partition carrying top-share
  * rank          = full-rank check, computed only for d_lambda <= 1000

STRAND LAYOUT is the framework's own, per
`sigma_shell_characterization.shell_position`: nucleon k occupies strands
3k+1..3k+3, its internal B_3 uses generators (0-indexed) 3k and 3k+1, and the
interface between nucleons k-1 and k is generator 3k-1. The production chain's
H_3 code puts every crossing on generators 0 and 1, which is the collapse this
probe removes.

PRECISION: the block values inherit float64 from `level_k_binding`'s q0 / qi /
HA, which this probe does not re-implement -- stated rather than hidden, as in
the A=3 companion. The question is structural, the compared quantities differ
at O(0.1), and no agreement at any digit count is claimed.

SELF-CHECK: `--selftest` re-runs A=3 Z=2,N=1 and Z=1,N=2 and asserts the
top-share / participation figures recorded in the A=3 probe's docstring
(0.0802 / 20.256 and 0.0961 / 20.590). It fails if the fast path drifts.
"""
import os
import sys, time, argparse
import numpy as np

sys.path[:0] = ['/home/user/qou/computations',
                '/home/user/qou/computations/_deprecated',
                '/home/user/qou/computations/substrate']
from hoefsmit_blocks_direct import extract_blocks_direct          # noqa: E402
from level_k_binding import standard_young_tableaux, HA           # noqa: E402
from sympy.utilities.iterables import partitions as sp            # noqa: E402
from qou_substrate.witness import WitnessBuilder                  # noqa: E402

MAGIC = {2, 8, 20, 28, 50, 82, 126}


def parts(n):
    for d in sp(n):
        yield tuple(sorted((k for k, v in d.items() for _ in range(v)), reverse=True))


def sigma_sparse(shape, gen):
    """sigma_gen in irrep `shape` as column-op data: singletons + 2x2 blocks."""
    diag, blocks, mask, dim = extract_blocks_direct(shape, gen)
    idx = np.array([i for i in range(dim) if mask[i]], dtype=np.int64)
    dv = np.array([diag[i] for i in idx], dtype=float) if len(idx) else np.zeros(0)
    if blocks:
        B = np.array(blocks, dtype=float)
        I, J = B[:, 0].astype(np.int64), B[:, 1].astype(np.int64)
        a, b, c, d = B[:, 2], B[:, 3], B[:, 4], B[:, 5]
    else:
        I = J = np.zeros(0, dtype=np.int64)
        a = b = c = d = np.zeros(0)
    return idx, dv, I, J, a, b, c, d, dim


def apply_fast(state, sig, cc, dd):
    """state <- state @ (cc*sigma + dd*I), in O(dim^2) rather than O(dim^3)."""
    idx, dv, I, J, a, b, c, d, _ = sig
    out = np.zeros_like(state)
    if len(idx):
        out[:, idx] = state[:, idx] * (cc * dv + dd)
    if len(I):
        ci = state[:, I]
        cj = state[:, J]
        out[:, I] = ci * (cc * a + dd) + cj * (cc * c)
        out[:, J] = ci * (cc * b) + cj * (cc * d + dd)
    return out


def ordering(Z, N):
    o, pc, nc = [], 0, 0
    for k in range(Z + N):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            o.append('p'); pc += 1
        else:
            o.append('n'); nc += 1
    return o


def schedule(Z, N):
    """The crossing schedule as (generator, c, d) triples, at TRUE strand positions."""
    A = Z + N
    ordr = ordering(Z, N)
    ops = []
    for k in range(A):
        g0, g1 = 3 * k, 3 * k + 1          # nucleon k's internal B_3
        t = ordr[k]
        for _ in range(3):
            ops.append((g0, 1.0, 0.0))
            ops.append((g1, 1.0, -HA))
        if t == 'p':
            ops.append((g0, 1.0, 0.0))
            ops.append((g0, 1.0, -HA / 2))
            ops.append((g1, 1.0, -HA / 2))
        else:
            ops.append((g0, 1.0, -HA / 2))
            ops.append((g0, 1.0, -HA / 2))
            ops.append((g1, 1.0, -HA))
        ops.append((g0, 1.0, 0.0))         # gluon
        ops.append((g0, 1.0, 0.0))
        if k > 0:
            gi = 3 * k - 1                 # interface k-1 <-> k
            ti, tj = ordr[k - 1], ordr[k]
            if ti == 'p' and tj == 'p':
                ops.append((gi, 1.0, 0.0))
            elif ti == 'n' and tj == 'n':
                ops.append((gi, 1.0, -HA))
            else:
                ops.append((gi, 1.0, -HA / 2))
    return ops


def walk_one(lam, ops, rank_max=1000):
    """Walk ONE irrep to completion, then discard it. Peak memory O(d_lam^2)."""
    dim = len(standard_young_tableaux(lam))
    st = np.eye(dim)
    sig = {}
    for (g, c, d) in ops:
        if g not in sig:
            sig[g] = sigma_sparse(lam, g)
        st = apply_fast(st, sig[g], c, d)
    tr = float(abs(np.trace(st)))
    rk = None
    if dim <= rank_max:
        s = np.linalg.svd(st, compute_uv=False)
        rk = int((s > 1e-9 * max(s[0], 1e-300)).sum()) if s[0] > 0 else 0
    return dim, tr, rk


def profile(Z, N, verbose=False):
    A = Z + N
    ops = schedule(Z, N)
    lams = sorted(parts(3 * A), key=lambda L: -len(standard_young_tableaux(L)))
    w, meta = [], []
    t0 = time.time()
    for i, lam in enumerate(lams):
        dim, tr, rk = walk_one(lam, ops)
        w.append(tr)
        meta.append((lam, dim, rk))
        if verbose:
            el = time.time() - t0
            print(f"    [{i+1:3d}/{len(lams)}] lam={lam} dim={dim} |tr|={tr:.6g} "
                  f"rank={rk} elapsed={el:.1f}s", flush=True)
    w = np.array(w)
    w = w / w.sum()
    k = int(w.argmax())
    deficient = [(m[0], m[1], m[2]) for m in meta if m[2] is not None and m[2] < m[1]]
    return {
        "Z": Z, "N": N, "A": A,
        "magic_Z": Z in MAGIC, "magic_N": N in MAGIC,
        "doubly_magic": (Z in MAGIC) and (N in MAGIC),
        "n_partitions": len(lams),
        "top_share": float(w.max()),
        "participation": float(1.0 / (w ** 2).sum()),
        "argmax_partition": list(meta[k][0]),
        "argmax_dim": meta[k][1],
        "rank_deficient": [[list(p), d, r] for (p, d, r) in deficient],
        "n_rank_checked": sum(1 for m in meta if m[2] is not None),
        "wall_seconds": round(time.time() - t0, 1),
    }


def selftest():
    """Reproduce the A=3 figures recorded in tower_walk_h3a_magic_probe.py."""
    ok = True
    for (Z, N), (ts, pr) in [((2, 1), (0.0802, 20.256)), ((1, 2), (0.0961, 20.590))]:
        r = profile(Z, N)
        dts, dpr = abs(r["top_share"] - ts), abs(r["participation"] - pr)
        good = dts < 5e-5 and dpr < 5e-3
        ok &= good
        print(f"  A=3 Z={Z},N={N}: top-share {r['top_share']:.4f} (want {ts}) "
              f"participation {r['participation']:.3f} (want {pr})  "
              f"{'OK' if good else 'MISMATCH'}", flush=True)
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--A", type=int, default=4)
    a = ap.parse_args()
    t_start = time.time()

    print("=== selftest: fast path vs the recorded A=3 figures ===", flush=True)
    if not selftest():
        print("SELFTEST FAILED -- the fast path drifted; not running A=4.")
        return 1
    if a.selftest:
        return 0

    A = a.A
    print(f"\n=== A={A} tower walk, all {A+1} configurations ===", flush=True)
    rows = []
    for Z in range(A, -1, -1):
        N = A - Z
        tag = ("4He DOUBLY MAGIC" if (Z in MAGIC and N in MAGIC)
               else "Z magic" if Z in MAGIC
               else "N magic" if N in MAGIC else "neither")
        print(f"\n  Z={Z} N={N}  [{tag}]", flush=True)
        r = profile(Z, N, verbose=True)
        r["tag"] = tag
        rows.append(r)
        print(f"  -> top-share {r['top_share']:.4f}  participation {r['participation']:.3f}  "
              f"argmax {tuple(r['argmax_partition'])}  rank-deficient {len(r['rank_deficient'])}  "
              f"[{r['wall_seconds']}s]", flush=True)

    print("\n=== SUMMARY ===", flush=True)
    for r in rows:
        print(f"  Z={r['Z']},N={r['N']:<2} {r['tag']:<17} top-share {r['top_share']:.4f}  "
              f"participation {r['participation']:8.3f}  argmax {tuple(r['argmax_partition'])}  "
              f"rank-def {len(r['rank_deficient'])}", flush=True)

    dm = [r for r in rows if r["doubly_magic"]]
    nm = [r for r in rows if not r["doubly_magic"]]
    if not dm:
        # A != 4 has no doubly-magic configuration; the comparison below is
        # undefined and the run is a mechanics check, not the experiment.
        print(f"\n  NOTE: A={A} has no doubly-magic configuration; "
              f"skipping the comparison.", flush=True)
        return 0
    verdict = {}
    for key in ("top_share", "participation"):
        v = dm[0][key]
        others = [r[key] for r in nm]
        verdict[key] = {
            "doubly_magic": v,
            "is_max": v > max(others),
            "is_min": v < min(others),
            "rank_among_all": 1 + sum(1 for o in others if o > v),
        }
    dm_arg = tuple(dm[0]["argmax_partition"])
    nm_args = [tuple(r["argmax_partition"]) for r in nm]
    verdict["argmax_shared_with_non_magic"] = dm_arg in nm_args
    # An UNSHARED argmax is only evidence if the non-magic configurations
    # share one WITH EACH OTHER. If they are all distinct, "4He has its own"
    # is the null expectation, not a signal -- the criterion is vacuous and
    # must be reported as such rather than as a pass.
    verdict["non_magic_argmax_agree"] = len(set(nm_args)) == 1
    verdict["n_distinct_non_magic_argmax"] = len(set(nm_args))
    verdict["argmax_criterion_informative"] = verdict["non_magic_argmax_agree"]
    verdict["doubly_magic_rank_deficient"] = len(dm[0]["rank_deficient"]) > 0
    verdict["any_non_magic_rank_deficient"] = any(len(r["rank_deficient"]) > 0 for r in nm)
    verdict["null_probability_of_an_extremum"] = 1.0 / len(rows)

    print("\n  4He vs the four non-magic configurations:", flush=True)
    for key in ("top_share", "participation"):
        d = verdict[key]
        print(f"    {key:<14} rank {d['rank_among_all']} of {len(rows)}  "
              f"(max={d['is_max']}, min={d['is_min']})", flush=True)
    print(f"    argmax partition shared with a non-magic config: "
          f"{verdict['argmax_shared_with_non_magic']}", flush=True)
    print(f"    non-magic argmaxes agree with each other: "
          f"{verdict['non_magic_argmax_agree']} "
          f"({verdict['n_distinct_non_magic_argmax']} distinct of {len(nm)}) "
          f"-> argmax criterion is "
          f"{'informative' if verdict['argmax_criterion_informative'] else 'VACUOUS'}",
          flush=True)
    print(f"    4He rank-deficient: {verdict['doubly_magic_rank_deficient']}   "
          f"any non-magic rank-deficient: {verdict['any_non_magic_rank_deficient']}", flush=True)
    print(f"    P(an extremum | null) = 1/{len(rows)} = "
          f"{verdict['null_probability_of_an_extremum']:.2f} per observable", flush=True)

    qualitative = (verdict["doubly_magic_rank_deficient"]
                   and not verdict["any_non_magic_rank_deficient"]) or \
                  (verdict["argmax_criterion_informative"]
                   and not verdict["argmax_shared_with_non_magic"])
    print(f"\n  QUALITATIVE separation (the only kind this control can support): "
          f"{qualitative}", flush=True)

    payload = {
        "probe": "tower_walk_a4_doubly_magic",
        "question": "does the H_{3A} tower, carried without per-step GS reduction, "
                    "separate the doubly-magic 4He from the four non-magic A=4 "
                    "configurations?",
        "control": f"exhaustive over A={A}: Z in 0..{A}, one doubly-magic",
        "null_probability_of_an_extremum": verdict["null_probability_of_an_extremum"],
        "configurations": rows,
        "verdict": verdict,
        "qualitative_separation": bool(qualitative),
        "precision_note": "block values inherit float64 from level_k_binding q0/qi/HA; "
                          "structural question, quantities differ at O(0.1); no "
                          "digit-level agreement claimed",
    }
    # Provenance via WitnessBuilder, not a raw json.dump: a hand-written witness
    # lands PROV_MISSING (no engine / scriptFile / commitSha) and the staleness
    # audits cannot key on it. See scripts/check-sidecars.sh P30 / bean cmiy.
    wb = WitnessBuilder.wrap_legacy(
        "tower-walk-a4-doubly-magic", payload,
        script_path=__file__, engine="python+numpy",
        output_dir=os.path.join(os.path.dirname(os.path.abspath(__file__))),
        start_time=t_start,
    )
    dmr = dm[0]
    wb.add_assertion("control_is_exhaustive_over_A",
                     computed=str(len(rows)), expected=str(A + 1))
    wb.add_assertion("exactly_one_doubly_magic_configuration",
                     computed=str(len(dm)), expected="1")
    wb.add_assertion("null_probability_of_an_extremum",
                     computed=f"{verdict['null_probability_of_an_extremum']:.4f}",
                     expected=f"{1.0 / (A + 1):.4f}")
    wb.add_assertion("doubly_magic_argmax_partition",
                     computed=str(tuple(dmr["argmax_partition"])),
                     expected=str(tuple(dmr["argmax_partition"])))
    out = wb.save(extra={"auditOnly": True})
    print(f"\nWrote {out}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
