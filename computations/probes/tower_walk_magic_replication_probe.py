#!/usr/bin/env python3
"""EXACT H_{3A} tower walk -- does the tower distinguish magic from non-magic?

RESULT, CORRECTLY SCOPED: no separation IN THE NUMERIC MAGNITUDES AT q = q_0,
at A = 2, 3 or 4 -- and the one observable that looked promising at A = 3
points the OTHER WAY at A = 2.

🛑 READ THE SCOPE BEFORE THE RESULT (owner correction, 2026-08-30). This probe
evaluates everything at the single point q = q_0, which COLLAPSES the
Groebner-Shirshov filtration into one float per basis element. The corpus is
explicit that the filtration is where the many-body structure lives: the GS
algorithm "digests global entanglement into local coefficients"
(`trace-locality-gs-reconciliation`), adding a nucleon "rais[es] the
normal-form length by a fixed increment" placing the n-nucleon cluster at
"jet vertical degree n" (`bond-order-eq-jet-degree-proof`), and the associated
graded gr_n IS the n-nucleon cluster contribution (`prop:gb-spectral-sequence`
E_2 collapse, `prop:jet-prefix-gb-filtration`). So the negative below is about
MAGNITUDES AT A POINT and says nothing about the graded structure -- which
this probe never looked at. The object to measure is the symbolic NF over
Q(q, sqrt q), `hecke_core_symbolic.build_atom_nf_sym`, and its q-degree /
filtration shape. Bean `qou-tower` (reopened).

The production chain collapses every nucleus to the same 6-dim H_3 quotient
(`gamma_chain_tower_magic_probe.py`) because `build_atom_nf_mp` applies the
Groebner-Shirshov reduction after every crossing, so hydrogen and 208-Pb occupy
the same state space and no shell degree of freedom is expressible. This probe
removes that collapse: a full `d_lambda x d_lambda` matrix per partition
`lambda |- 3A`, no per-step reduction, and generators at their TRUE strand
positions per `sigma_shell_characterization.shell_position` (nucleon k on
strands 3k+1..3k+3, internal B_3 on generators 3k / 3k+1, interface at 3k-1).
The H_3 code puts every crossing on generators 0 and 1.

THE CONTROL IS THE POINT, AND IT IS EXHAUSTIVE. Magic-ness is a property of Z
or N separately, so magic numbers appear from A = 2 onward, and every level
admits exactly A+1 configurations -- ALL of which are walked. The contrast is
therefore at fixed algebra, fixed partitions and fixed strand count, with only
the nucleon composition varying, and there is no configuration left unmeasured
to appeal to.

    A=2 (H_6,  11 partitions)  Z=2 and Z=0 singly magic, deuteron neither
    A=3 (H_9,  30 partitions)  3He (Z=2) and 3H (N=2) magic, two neither
    A=4 (H_12, 77 partitions)  4He (Z=N=2) DOUBLY magic, four neither

MEASURED:

    A=2  Z=2,N=0  MAGIC    top-share 0.1996  participation  7.624  argmax (6,)
         Z=1,N=1  neither  top-share 0.1960  participation  7.801  argmax (3,3)
         Z=0,N=2  MAGIC    top-share 0.1909  participation  7.560  argmax (2,2,2)

    A=3  Z=3,N=0  neither  top-share 0.0907  participation 18.895  argmax (6,3)
         Z=2,N=1  MAGIC    top-share 0.0802  participation 20.256  argmax (3,3,1,1,1)
         Z=1,N=2  MAGIC    top-share 0.0961  participation 20.590  argmax (3,3,1,1,1)
         Z=0,N=3  neither  top-share 0.0968  participation 19.819  argmax (3,3,1,1,1)

    A=4  Z=4,N=0  neither  top-share 0.0530  participation 42.169  argmax (9,3)
         Z=3,N=1  neither  top-share 0.0436  participation 44.400  argmax (5,4,1,1,1)
         Z=2,N=2  DOUBLY   top-share 0.0504  participation 45.487  argmax (5,4,1,1,1)
         Z=1,N=3  neither  top-share 0.0481  participation 44.826  argmax (5,4,1,1,1)
         Z=0,N=4  neither  top-share 0.0567  participation 43.818  argmax (3,3,3,1,1,1)

THE CROSS-LEVEL TEST IS WHAT SETTLES IT. A single level's split is cheap: at
A = 3 there are 2 magic against 2 non-magic, so a clean split has **P = 1/3**
under the null; at A = 4, one doubly-magic among five gives an extremum
**P = 1/5**. Neither is evidence on its own. The real question is whether a
PRE-SPECIFIED observable behaves the same way at every level.

    participation   A=2 magic BELOW    A=3 magic ABOVE    A=4 magic max
    top-share       interleaved at every level

The participation ratio is **contradictory**, not merely weak: the magic
configurations are the two LOWEST at A = 2 (7.624, 7.560 against the
deuteron's 7.801) and the two HIGHEST at A = 3. A quantity that reverses sign
between levels is measuring the level, not the magic number. That is the whole
finding, and A = 2 -- which costs seconds -- is what produced it, after the
A = 3 split had been carried for a session as "the one thing that separated".

The other two criteria fail outright rather than ambiguously:

  * **rank** -- every block is full rank in every configuration at every level.
  * **argmax** -- 4He's argmax `(5,4,1,1,1)` is shared with THREE non-magic
    A = 4 configurations. And the criterion carries its own control: an
    unshared argmax is evidence only if the non-magic configurations share one
    WITH EACH OTHER, which at A = 2 they cannot (three configurations, three
    distinct argmaxes). `argmax_criterion_informative` reports that, and a
    vacuous pass is never counted as a separation.

WHAT MADE A = 4 REACHABLE, having twice been recorded as blocked. Bean
`qou-tower` gives 4He as "3.83 GB, borderline in a 16 GB container", from
`sum_lambda d_lambda^2 = 12!`. That is the cost of holding EVERY partition's
state at once. Partitions are independent under the braid action, so walking
one at a time makes peak memory `max_lambda d_lambda^2` = 7700^2 = 474 MB.
Measured RSS: **0.64 GB**. The second cost was time and was real: forming
`state @ (c*sigma + d*I)` as a dense matmul is `O(d^3)` = 4.6e11 flops per
crossing at d = 7700, but in the Hoefsmit seminormal basis sigma is diagonal
plus 2x2 blocks, so the same product is a set of column operations in `O(d^2)`.
Verified against the dense route on all 30 partitions of A=3 Z=2,N=1: max
relative disagreement **6.34e-16**, the float64 floor.

WHERE THE TOWER ENDS. A = 5 needs `max_lambda d_lambda^2` at n = 15 =
292,864^2 = 686 GB, so A = 4 is the last reachable level and 4He the only
doubly-magic nucleus this construction can ever test. The tower buys the first
magic number, not the ladder.

OBSERVABLES. Per partition the walk returns the full `d_lambda x d_lambda`
matrix; the weight is `w_lambda = |tr M_lambda|`, normalised over partitions:

  * top-share     = max_lambda w_lambda           (concentration on one irrep)
  * participation = 1 / sum_lambda w_lambda^2     (effective number of irreps)
  * argmax        = the partition carrying top-share
  * rank          = full-rank check, for d_lambda <= 1000

PRECISION: the block values inherit float64 from `level_k_binding`'s q0 / qi /
HA, which this probe does not re-implement -- stated rather than hidden. The
question is structural and the compared quantities differ at O(0.1), ~15 orders
above the float64 floor; no agreement at any digit count is claimed. Note the
headline result is a NEGATIVE plus a sign REVERSAL of ~0.24 in a quantity of
size ~7.7, neither of which float64 can manufacture.

SELF-CHECK: `--selftest` re-runs A=3 Z=2,N=1 and Z=1,N=2 and asserts the
figures recorded in `tower_walk_h3a_magic_probe.py` (0.0802 / 20.256 and
0.0961 / 20.590). It fails, and refuses to run, if the fast path drifts.
"""
import os
import sys, time, argparse
import numpy as np  # float64-ok: scope-(a) numpy Hoefsmit matrix walk (see header scope note)

sys.path[:0] = ['/home/user/qou/computations',
                '/home/user/qou/computations/_deprecated',
                '/home/user/qou/computations/substrate']
from hoefsmit_blocks_direct import extract_blocks_direct          # noqa: E402
from level_k_binding import standard_young_tableaux, HA           # noqa: E402
from sympy.utilities.iterables import partitions as sp            # noqa: E402
from qou_substrate.witness import WitnessBuilder                  # noqa: E402
from _precision import fmt, mp, set_compute_dps                    # noqa: E402

# The aggregation below carries mpf specifically so that summing 77 values does
# not pile error on top of float64 inputs. That only works above float64: at
# mpmath's DEFAULT dps of 15 an mpf sum accumulates exactly as a float sum
# does, so the mpf was a no-op wearing the costume of precision. `_precision`
# is explicit that importing it does NOT raise dps — the call has to be here.
set_compute_dps()

# Serialization width for anything descending from `walk_one`. Its return is
# `float(abs(np.trace(st)))` — float64 by construction, and irreducibly so
# since the whole walk is numpy. So ~17 significant digits is the honest width
#
# MEASURED 2026-09-03, because both numbers here are easy to assume and I got
# one wrong first time: `mp.dps` on entry was **15**, mpmath's default — so
# the mpf aggregation above was float64-grade and bought nothing — and `fmt`'s
# default output width is **60**, not 50. Sixty digits on a float64-sourced
# value is fake precision by ~43 orders; the float64-padding ratchet counted
# 22 such fields in this one witness.
#
# The two halves pull opposite ways: raising dps fixes the ARITHMETIC and
# makes the serialization worse. Both are needed.
F64_DPS = 17

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
    tr = float(abs(np.trace(st)))  # float64-ok: scope-(a) numpy Hoefsmit matrix trace (see header scope note)
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
    # AGGREGATE IN MPMATH. The per-partition |tr| values are float64 inputs
    # (inherited from level_k_binding and stated in the module docstring), but
    # normalising and summing 77 of them in float64 would accumulate error on
    # top of that -- AGENTS.md "PROBES ARE NOT EXEMPT" item 2. Carry mpf from
    # here on and serialize with _precision.fmt; never stringify a float.
    wm = [mp.mpf(x) for x in w]
    tot = mp.fsum(wm)
    wm = [x / tot for x in wm]
    k = max(range(len(wm)), key=lambda i: wm[i])
    top = wm[k]
    part = mp.mpf(1) / mp.fsum([x * x for x in wm])
    deficient = [(m[0], m[1], m[2]) for m in meta if m[2] is not None and m[2] < m[1]]
    return {
        "Z": Z, "N": N, "A": A,
        "magic_Z": Z in MAGIC, "magic_N": N in MAGIC,
        "doubly_magic": (Z in MAGIC) and (N in MAGIC),
        "n_partitions": len(lams),
        "top_share": fmt(top, dps=F64_DPS),
        "participation": fmt(part, dps=F64_DPS),
        "_top_share_mp": top,          # popped before the witness is built
        "_participation_mp": part,
        "argmax_partition": list(meta[k][0]),
        "argmax_dim": meta[k][1],
        "rank_deficient": [[list(p), d, r] for (p, d, r) in deficient],
        "n_rank_checked": sum(1 for m in meta if m[2] is not None),
        "wall_seconds": int(round(time.time() - t0)),
    }


def selftest():
    """Reproduce the A=3 figures recorded in tower_walk_h3a_magic_probe.py."""
    ok = True
    for (Z, N), (ts, pr) in [((2, 1), (0.0802, 20.256)), ((1, 2), (0.0961, 20.590))]:
        r = profile(Z, N)
        dts = abs(r["_top_share_mp"] - mp.mpf(str(ts)))
        dpr = abs(r["_participation_mp"] - mp.mpf(str(pr)))
        good = dts < mp.mpf("5e-5") and dpr < mp.mpf("5e-3")
        ok &= good
        print(f"  A=3 Z={Z},N={N}: top-share {mp.nstr(r['_top_share_mp'], 4)} (want {ts}) "
              f"participation {mp.nstr(r['_participation_mp'], 6)} (want {pr})  "
              f"{'OK' if good else 'MISMATCH'}", flush=True)
    return ok


def run_level(A, verbose=True):
    """All A+1 configurations at nucleon number A, exhaustively."""
    print(f"\n=== A={A} tower walk, all {A + 1} configurations ===", flush=True)
    rows = []
    for Z in range(A, -1, -1):
        N = A - Z
        both = (Z in MAGIC) and (N in MAGIC)
        tag = ("DOUBLY MAGIC" if both
               else "Z magic" if Z in MAGIC
               else "N magic" if N in MAGIC else "neither")
        print(f"\n  Z={Z} N={N}  [{tag}]", flush=True)
        r = profile(Z, N, verbose=verbose)
        r["tag"] = tag
        r["any_magic"] = (Z in MAGIC) or (N in MAGIC)
        rows.append(r)
        print(f"  -> top-share {mp.nstr(r['_top_share_mp'], 4)}  "
              f"participation {mp.nstr(r['_participation_mp'], 6)}  "
              f"argmax {tuple(r['argmax_partition'])}  "
              f"rank-deficient {len(r['rank_deficient'])}  [{r['wall_seconds']}s]", flush=True)
    return rows


def judge_level(A, rows):
    """Magic vs neither at ONE level, with each criterion's own control."""
    mg = [r for r in rows if r["any_magic"]]
    nm = [r for r in rows if not r["any_magic"]]
    v = {"A": A, "n_configurations": len(rows),
         "n_magic": len(mg), "n_non_magic": len(nm)}
    if not mg or not nm:
        v["comparable"] = False
        return v
    v["comparable"] = True
    for key in ("top_share", "participation"):
        mv = [r["_" + key + "_mp"] for r in mg]
        nv = [r["_" + key + "_mp"] for r in nm]
        v[key] = {
            "magic": [fmt(x, dps=F64_DPS) for x in mv],
            "non_magic": [fmt(x, dps=F64_DPS) for x in nv],
            "magic_all_above": bool(min(mv) > max(nv)),
            "magic_all_below": bool(max(mv) < min(nv)),
            "magic_mean_minus_non_magic_mean":
                fmt(mp.fsum(mv) / len(mv) - mp.fsum(nv) / len(nv), dps=F64_DPS),
        }
    # Rank: a deficiency the non-magic configurations lack.
    v["magic_rank_deficient"] = any(r["rank_deficient"] for r in mg)
    v["non_magic_rank_deficient"] = any(r["rank_deficient"] for r in nm)
    # Argmax: unshared is evidence ONLY if the non-magic configurations share
    # one with each other. All-distinct makes the criterion vacuous.
    mg_args = [tuple(r["argmax_partition"]) for r in mg]
    nm_args = [tuple(r["argmax_partition"]) for r in nm]
    v["argmax_magic"] = mg_args
    v["argmax_non_magic"] = nm_args
    v["argmax_shared_across_groups"] = bool(set(mg_args) & set(nm_args))
    # THE ARGMAX CRITERION NEEDS THREE THINGS, not one. "The magic group has an
    # argmax the non-magic group lacks" is evidence only if BOTH groups are
    # internally consistent AND each has at least two members. A singleton
    # group "agrees with itself" trivially -- which is exactly how A=2, with
    # one non-magic configuration, returned a spurious qualitative separation
    # from the first version of this guard. It also requires the magic group to
    # agree: at A=2 the two magic argmaxes are (6,) and (2,2,2), so "magic has
    # its own" is meaningless there whatever the non-magic group does.
    v["non_magic_argmax_agree"] = len(set(nm_args)) == 1
    v["magic_argmax_agree"] = len(set(mg_args)) == 1
    v["argmax_criterion_informative"] = bool(
        len(mg) >= 2 and len(nm) >= 2
        and v["magic_argmax_agree"] and v["non_magic_argmax_agree"])
    v["argmax_criterion_vacuity_reason"] = (
        None if v["argmax_criterion_informative"]
        else "magic group has one member" if len(mg) < 2
        else "non-magic group has one member" if len(nm) < 2
        else "magic argmaxes disagree with each other" if not v["magic_argmax_agree"]
        else "non-magic argmaxes disagree with each other")
    v["qualitative_separation"] = bool(
        (v["magic_rank_deficient"] and not v["non_magic_rank_deficient"])
        or (v["argmax_criterion_informative"] and not v["argmax_shared_across_groups"]))
    return v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--levels", default="2,3,4",
                    help="comma-separated nucleon numbers to walk")
    a = ap.parse_args()
    t_start = time.time()

    print("=== selftest: fast path vs the recorded A=3 figures ===", flush=True)
    if not selftest():
        print("SELFTEST FAILED -- the fast path drifted; not running.")
        return 1
    if a.selftest:
        return 0

    levels = [int(x) for x in a.levels.split(",") if x.strip()]
    all_rows, judgements = {}, {}
    for A in levels:
        rows = run_level(A)
        all_rows[A] = rows
        judgements[A] = judge_level(A, rows)

    print("\n=== SUMMARY ===", flush=True)
    for A in levels:
        print(f"  A={A}:", flush=True)
        for r in all_rows[A]:
            print(f"    Z={r['Z']},N={r['N']:<2} {r['tag']:<13} "
                  f"top-share {mp.nstr(r['_top_share_mp'], 4)}  "
                  f"participation {mp.nstr(r['_participation_mp'], 6)}  "
                  f"argmax {tuple(r['argmax_partition'])}  "
                  f"rank-def {len(r['rank_deficient'])}", flush=True)

    # --- The cross-level test. A single level's split is cheap; the question
    # --- is whether the SAME pre-specified observable behaves the same way at
    # --- every level. It does not, and that is the result.
    replication = {}
    for key in ("top_share", "participation"):
        dirs = {}
        for A in levels:
            j = judgements[A]
            if not j.get("comparable"):
                continue
            d = j[key]
            dirs[A] = ("magic_above" if d["magic_all_above"]
                       else "magic_below" if d["magic_all_below"]
                       else "interleaved")
        vals = set(dirs.values())
        replication[key] = {
            "per_level_direction": dirs,
            "consistent_across_levels": len(vals) == 1 and "interleaved" not in vals,
            "contradictory": ("magic_above" in vals) and ("magic_below" in vals),
        }

    print("\n=== CROSS-LEVEL REPLICATION (the actual test) ===", flush=True)
    for key, rep in replication.items():
        per = "  ".join(f"A={A}:{d}" for A, d in rep["per_level_direction"].items())
        print(f"  {key:<14} {per}", flush=True)
        print(f"  {'':14} consistent={rep['consistent_across_levels']}  "
              f"CONTRADICTORY={rep['contradictory']}", flush=True)

    qual = {A: judgements[A].get("qualitative_separation") for A in levels}
    print("", flush=True)
    for A in levels:
        j = judgements[A]
        if not j.get("comparable"):
            continue
        why = j.get("argmax_criterion_vacuity_reason")
        print(f"  A={A}: qualitative separation {j['qualitative_separation']}  "
              f"(rank: magic-def={j['magic_rank_deficient']} "
              f"non-magic-def={j['non_magic_rank_deficient']}; "
              f"argmax criterion "
              f"{'informative' if j['argmax_criterion_informative'] else 'VACUOUS -- ' + str(why)})",
              flush=True)
    any_qual = any(bool(v) for v in qual.values())
    any_rep = any(r["consistent_across_levels"] for r in replication.values())
    print(f"  ANY qualitative separation: {any_qual}", flush=True)
    print(f"  ANY observable replicating across levels: {any_rep}", flush=True)

    for A in levels:
        for r in all_rows[A]:
            r.pop("_top_share_mp", None)
            r.pop("_participation_mp", None)
    payload = {
        "probe": "tower_walk_magic_replication",
        "question": "does the H_{3A} tower, carried WITHOUT the per-step "
                    "Groebner-Shirshov reduction, distinguish magic from "
                    "non-magic nucleon configurations?",
        "control": "exhaustive at each level: every Z in 0..A, so the contrast "
                   "is at fixed algebra, fixed partitions and fixed strand "
                   "count with only nucleon composition varying",
        "levels": levels,
        "configurations": {str(A): all_rows[A] for A in levels},
        "per_level_verdict": {str(A): judgements[A] for A in levels},
        "cross_level_replication": replication,
        "any_qualitative_separation": any_qual,
        "any_observable_replicates": any_rep,
        "precision_note": "block values inherit float64 from level_k_binding "
                          "q0/qi/HA; the question is structural and the compared "
                          "quantities differ at O(0.1); no digit-level agreement "
                          "is claimed",
    }
    wb = WitnessBuilder.wrap_legacy(
        "tower-walk-magic-replication", payload,
        script_path=__file__, engine="python+numpy",
        output_dir=os.path.join(os.path.dirname(os.path.abspath(__file__))),
        start_time=t_start,
    )
    for A in levels:
        wb.add_assertion(f"control_exhaustive_at_A{A}",
                         computed=str(len(all_rows[A])), expected=str(A + 1))
    # The two lines that used to sit here asserted `expected="False"` on the
    # verdict itself -- a test that passes exactly when the answer is the one
    # wanted. The verdict belongs in the payload as data; assertions record the
    # CONTROL, which is what a later reader needs to trust the verdict.
    for A in levels:
        j = judgements[A]
        if j.get("comparable"):
            wb.add_assertion(f"both_groups_non_empty_at_A{A}",
                             computed=str(j["n_magic"] > 0 and j["n_non_magic"] > 0),
                             expected="True")
    wb.add_assertion("selftest_reproduces_A3_reference_figures",
                     computed="True", expected="True")
    out = wb.save(extra={"auditOnly": True})
    print(f"\nWrote {out}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
