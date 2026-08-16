#!/usr/bin/env python3
"""ρ_K via Frobenius co-Casimir (Option B) — multi-atom extension.

Generalises `rho_k_h3a_co_casimir.py` (deuteron-only) to compute the
substrate-derived ρ_K^pred via

    ρ_K^pred = ρ_K^LO + (1 / |tr_M(β_K)|) · Σ_λ y_λ(q_0) · χ^λ(β_K) · (1/dim_q(λ))

for every atom in the L1 canonical |tr_M| catalogue: p, n, T, ³He, ⁴He.
The Δ_λ^B = 1/dim_q(λ) selector is the Frobenius co-Casimir restriction
(thm:frobenius-codim-universal) — zero free parameters, τ-invariant.

Per repo-owner directive 2026-05-19 ("Frobenius co-Casimir Option B for
other?") after PR #802 opened: extend the substrate-derivation status
from D-only (1 atom) to all 5 additional L1 atoms covered by the
y-lambda-wenzl-bridge-symbolic-witness.json table (n=3, 6, 9, 12).

Output: rho-k-co-casimir-extended.witness.json with per-atom
contribution tables, predicted ρ_K, predicted mass, and side-by-side
comparison vs current empirical-assignment quality.

Notes
-----
- ⁵Li (n=15) and ⁶Li (n=18) are out of scope here: the
  y-lambda-wenzl-bridge-symbolic-witness only covers n=2..12. Extending
  would require running the Wenzl-bridge producer for n=15, 18.
- Per the τ-invariance theorem (frobenius-codim-universal §"Independence
  of the vortex"), the Δ_λ^B profile is the same for every β_K on
  H_n(q). The knot-specific information enters only through χ^λ(β_K).
  This is a known "feature/limitation" — expect substrate-only ρ_K^pred
  quality to be lower than the current empirical-(Knot, ρ_K) hypothesis
  table on D-⁴He, but with the upgrade in provenance from
  `canonical-with-empirical-assignment` → `canonical-substrate`.

Per `canonical-discipline` PR #802: this script outputs the
provenance-upgraded ρ_K candidates; downstream consumer
`canonical_isotope_witness.py` would consume them in a follow-up
patch to flip the `canonical_status` field for matching atoms.
"""
from __future__ import annotations

# ── BLAS thread pinning — must precede ANY import that loads numpy ────────
# This producer fans out over partitions with `multiprocessing.Pool`, and each
# worker calls into scipy-openblas, which by default spawns one thread per core.
# Four workers x four BLAS threads on a four-core box is 16 runnable threads
# competing for 4 cores: the per-worker matrix products are already the whole
# cost, so the extra threads buy nothing and the context switching is pure loss.
#
# Measured on the ⁴He leg (bean qou-mnrd), 4 partitions of dim ≈ 2100 through a
# 4-worker pool:
#     BLAS threads unset : 25.4 s
#     BLAS threads = 1   : 18.6 s      1.37x
#
# `setdefault`, so an operator who deliberately exports a value keeps it.
# It must run before numpy is first imported — OpenBLAS reads these at library
# load, and a fork inherits the already-loaded library, so setting them inside
# the worker is too late.
import os  # noqa: E402
for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
           "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import argparse
import json
import multiprocessing as multi
import os
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import str_at_true_precision  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV as _M_E_MEV_MP  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from hoefsmit_symbolic import dim_q  # noqa: E402
# chi_numeric (mpmath, ~1000× faster than chi_lambda_symbolic for
# numeric-only consumers like this co-Casimir loop): the Hoefsmit
# matrices are built once at concrete q_0 and the trace product runs
# in mpmath float math throughout. Per-partition cost ≈ ms, not min.
from rho_k_h3a_refinement import chi_numeric  # noqa: E402

mp.mp.dps = 60
M_E_MEV = _M_E_MEV_MP

Q_SYM = sp.Symbol("q", positive=True)
Q_MP = mp.mpf(Q_50_DIGIT_STR)


# ── Worker cap (memory-bound, see the note at the call site) ─────
_WORKER_OVERRIDE: int | None = None


def _worker_cap() -> int:
    """Workers to use: CLI --workers, else $RHO_K_WORKERS, else cpu_count().

    Deliberately a cap and not a fixed number, so the default behaviour is
    exactly what it was before (cpu_count()) and only an explicit request
    lowers it.
    """
    if _WORKER_OVERRIDE is not None:
        return max(1, _WORKER_OVERRIDE)
    env = os.environ.get("RHO_K_WORKERS")
    if env:
        try:
            return max(1, int(env))
        except ValueError:
            print(f"  RHO_K_WORKERS={env!r} is not an integer — ignoring.")
    return multi.cpu_count()


# ── Multiprocessing worker (top-level so Pool can pickle) ────────


def _lambda_cost_proxy(lam: tuple[int, ...]) -> int:
    """Scheduling weight for one partition: its Specht dimension (# SYT).

    Only the ORDER matters — this decides which λ a free worker takes next, so
    a monotone proxy for cost is enough and an exact model would be wasted. The
    Hoefsmit kernel builds dim x dim matrices, and measured cost tracks
    ~dim^2.4 on this path, so dimension ranks the work correctly.

    Hook-length formula. Cheap (integer arithmetic on a partition of ≤ 12) next
    to the χ^λ it is scheduling.
    """
    import math
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])] if lam else []
    prod = 1
    for i, r in enumerate(lam):
        for j in range(r):
            prod *= (r - j) + (conj[j] - i) - 1
    return math.factorial(n) // prod if prod else 1


def _chi_worker(args):
    """Pool worker: chi_numpy for one partition (10-50× faster than
    chi_numeric, validated against mpmath at 1e-14 relative tolerance
    per docs/audits/2026-05-19-cocasimir-compute-bottleneck.md).

    NO SILENT FALLBACK (owner directive 2026-08-15): if the numpy fast path
    is unavailable, refuse loudly rather than silently dropping to the slow
    mpmath chi_numeric path (the ct80/#2747 silent-degradation class — a slow
    run that also looks like a correct one). The slow path stays available as
    an EXPLICIT opt-in via QOU_ALLOW_SLOW_CHI_FALLBACK=1. Mirrors
    pyhecke.gram._native_ok()'s loud-refusal philosophy. See
    docs/pyhecke-native-setup.md."""
    lam, crossings, q_str, dps = args
    mp.mp.dps = dps
    try:
        from hoefsmit_numpy import chi_numpy as _chi  # noqa: E402
        return _chi(lam, crossings, float(mp.mpf(q_str)))
    except ImportError as e:
        import os
        if os.environ.get("QOU_ALLOW_SLOW_CHI_FALLBACK") != "1":
            raise RuntimeError(
                "chi_numpy (numpy fast path) is unavailable: " + repr(e) + ". "
                "Refusing to silently fall back to the slow mpmath chi_numeric "
                "path. Fix the numpy/hoefsmit_numpy import, or set "
                "QOU_ALLOW_SLOW_CHI_FALLBACK=1 to explicitly permit the slow "
                "path. See docs/pyhecke-native-setup.md."
            ) from e
        from rho_k_h3a_refinement import chi_numeric as _chi  # noqa: E402
        return _chi(lam, crossings, mp.mpf(q_str))


# ── Helpers ──────────────────────────────────────────────────────

def partitions_of(n: int) -> list[tuple[int, ...]]:
    """Enumerate partitions of n in weakly-decreasing tuples."""
    out: list[tuple[int, ...]] = []
    def _rec(rem: int, max_part: int, acc: list[int]):
        if rem == 0:
            out.append(tuple(acc))
            return
        for k in range(min(rem, max_part), 0, -1):
            _rec(rem - k, k, acc + [k])
    _rec(n, n, [])
    return out


def conjugate(lam: tuple[int, ...]) -> tuple[int, ...]:
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p > i) for i in range(lam[0]))


def evaluate_at_q0(expr) -> mp.mpf:
    """Numerically evaluate a sympy expression in q at q_0."""
    free = expr.free_symbols
    if not free:
        return mp.mpf(str(expr.evalf(60)))
    qsym = next(iter(free))
    val = expr.subs(qsym, sp.Float(Q_50_DIGIT_STR, 60))
    return mp.mpf(str(val.evalf(60)))


_Y_LAMBDA_CACHE: dict[int, dict] = {}


def load_y_lambda_for_n(n: int):
    """Load y_λ for the given n. Returns dict[partition_tuple, value].

    Prefer the SYMBOLIC witness (`y-lambda-wenzl-bridge-symbolic-
    witness.json`) covering n=2..12 — full sympy expressions in q
    (value type: sp.Expr).
    Fall back to the NUMERIC witness (`y-lambda-wenzl-witness.json`)
    covering n=2..30 — y_λ pre-evaluated at q_0 (value type: mp.mpf).

    Cached per-n at module scope (Copilot review #1 on PR #822):
    multi-atom runs no longer re-parse the (large) witness JSON
    per atom — once per `n`, then dict lookup.

    Per repo-owner directive 2026-05-19 "all nucleotides": the numeric
    fallback extends co-Casimir coverage from n=12 (only ⁴He) to
    n=30 (covers ⁵Li, ⁶Li, ⁷Li, ⁸Be, ⁹Be, ¹⁰Be — up to A=10).
    """
    if n in _Y_LAMBDA_CACHE:
        return _Y_LAMBDA_CACHE[n]
    # Try symbolic first (n=2..12)
    sym_path = HERE / "y-lambda-wenzl-bridge-symbolic-witness.json"
    if sym_path.exists():
        d = json.loads(sym_path.read_text())
        block = d.get("tables_by_n", {}).get(str(n))
        if block:
            out = {}
            for w in block["weights"]:
                lam = tuple(w["partition"])
                expr = sp.sympify(w["y_lambda_symbolic"])
                free = expr.free_symbols
                if free:
                    qsym = next(iter(free))
                    if qsym is not Q_SYM:
                        expr = expr.subs(qsym, Q_SYM)
                out[lam] = expr
            _Y_LAMBDA_CACHE[n] = out
            return out
    # Fall back to numeric (n=2..30) — pre-evaluated at q_0
    num_path = HERE / "y-lambda-wenzl-witness.json"
    if not num_path.exists():
        raise FileNotFoundError(
            f"No y_λ witness has n={n}; need symbolic (n≤12) or "
            f"numeric (n≤30). Generate via "
            f"`python3 y_lambda_wenzl_bridge.py {n}`."
        )
    d = json.loads(num_path.read_text())
    block = d.get("tables_by_n", {}).get(str(n))
    if not block:
        raise KeyError(
            f"y_λ numeric witness has no n={n}. Run "
            f"`python3 y_lambda_wenzl_bridge.py {n}` to extend."
        )
    out_num = {}
    for w in block["weights"]:
        lam = tuple(w["partition"])
        out_num[lam] = mp.mpf(w["y_lambda_numeric"])
    _Y_LAMBDA_CACHE[n] = out_num
    return out_num


def load_tr_M_for_atom(Z: int, N: int) -> mp.mpf | None:
    """Load |tr_M(β_atom, q_0)| from L1 canonical witness."""
    path = _pb.witness_path("canonical-mass-table-extended.witness.json", HERE)
    d = json.loads(path.read_text())
    for r in d.get("data", {}).get("rows", []):
        if r.get("Z") == Z and r.get("N") == N:
            v = r.get("tr_M_q0_canonical_50dps")
            if v:
                return mp.mpf(v)
    return None


# ── Atom-level computation ───────────────────────────────────────

def compute_co_casimir_for_atom(
    Z: int, N: int, label: str,
    *,
    skip_chi: bool = False,
) -> dict:
    """Compute substrate-derived ρ_K^pred via co-Casimir for one atom."""
    A = Z + N
    n = 3 * A
    t0 = time.time()
    print(f"\n=== {label} (Z={Z}, N={N}, A={A}, n={n}) ===", flush=True)

    abs_tr_M = load_tr_M_for_atom(Z, N)
    if abs_tr_M is None:
        return {
            "label": label, "Z": Z, "N": N, "A": A, "n_strands": n,
            "status": "no_tr_M_in_L1_witness",
        }
    print(f"  |tr_M|     = {mp.nstr(abs_tr_M, 25)}")

    # ρ_K^LO = (Z·m_p + N·m_n) / (m_e · |tr_M|) — tautological,
    # but needed as the baseline that the co-Casimir correction
    # modifies.
    # CODATA m_p, m_n imported from codata_constants registry
    # (P31 compliance per Copilot review): these are VALIDATION
    # targets — the script uses them as the LO baseline that the
    # substrate-derived co-Casimir correction modifies, NOT as
    # independent calibration inputs. The substrate-derivation
    # status is captured by the Borromean tower elsewhere; this
    # script's job is to numerically evaluate the Frobenius
    # co-Casimir refinement against that baseline.
    from codata_constants import M_P_MEV_VALIDATION, M_N_MEV_VALIDATION
    m_p_codata = mp.mpf(str(M_P_MEV_VALIDATION))
    m_n_codata = mp.mpf(str(M_N_MEV_VALIDATION))
    constituent_sum = Z * m_p_codata + N * m_n_codata
    rho_K_LO = constituent_sum / (M_E_MEV * abs_tr_M)
    print(f"  ρ_K^LO     = {mp.nstr(rho_K_LO, 18)}")

    if skip_chi:
        return {
            "label": label, "Z": Z, "N": N, "A": A, "n_strands": n,
            "abs_tr_M_at_q0": str(abs_tr_M),
            "rho_K_LO": str(rho_K_LO),
            "status": "skip_chi",
        }

    # y_λ + 1/dim_q(λ) tables for all p(n) partitions
    try:
        y_lambda = load_y_lambda_for_n(n)
    except KeyError:
        return {
            "label": label, "Z": Z, "N": N, "A": A, "n_strands": n,
            "abs_tr_M_at_q0": str(abs_tr_M),
            "rho_K_LO": str(rho_K_LO),
            "status": f"no_y_lambda_for_n={n}",
        }
    parts = partitions_of(n)
    print(f"  partitions of {n}: {len(parts)}")

    # χ^λ(β_atom) for each partition (the expensive step)
    crossings = atom_canonical_crossings(Z, N)
    print(f"  braid crossings: {len(crossings)}")

    # Parallel per-λ Hoefsmit χ^λ. Partition input is (lam, crossings,
    # q_str_50dps, dps) so the worker is self-contained.
    # WORKER COUNT IS MEMORY-BOUND, NOT CPU-BOUND, at n >= 12. Each worker holds
    # one partition's Hoefsmit generators DENSE: the largest partition of 12 is
    # dim 7700, so 11 generators occupy 7700^2 * 8 B * 11 = 5.22 GB. Four
    # workers want ~20 GB, and on a 16 GB box the run does not merely slow down
    # — it HANGS, workers parked in futex_do_wait with khugepaged thrashing
    # (bean qou-5qwb; the underlying dense-storage issue is qou-bk0q).
    # `cpu_count()` cannot see any of that.
    #
    # Two mechanisms, deliberately kept distinct (rebase resolution, qou-mnrd
    # x qou-5qwb — both arcs hit this independently and neither is redundant):
    #
    #   1. `_worker_cap()` — EXPLICIT operator control via `--workers` /
    #      $RHO_K_WORKERS. Authoritative: if someone asks for N, they get N.
    #      That is qou-5qwb's design and it is not overridden below.
    #   2. the MemAvailable-derived ceiling — applies only when NOTHING explicit
    #      was requested, so the *default* stops being a number that OOMs. An
    #      operator who has to know to pass `--workers 1` has to know the box
    #      first; a default derived from /proc/meminfo does not.
    #
    # PEAK IS 268 BYTES PER dim², MEASURED. The generator storage above (5.22 GB)
    # is not the process peak — intermediates in the braid-word chain roughly
    # triple it. A single SERIAL process on (5,3,2,1,1) peaks at 15.9 GiB:
    #     Out of memory: Killed process 26199 anon-rss:15884144kB
    # An earlier estimate of 84 B/dim² came from `ps` on a worker the kernel was
    # about to kill, i.e. one still growing. Read the peak off the OOM line's
    # anon-rss, never off `ps` mid-flight.
    _explicit_workers = _WORKER_OVERRIDE is not None or os.environ.get("RHO_K_WORKERS")
    _peak_bytes = 268 * max(_lambda_cost_proxy(l) for l in parts) ** 2
    try:
        _avail = next(int(l.split()[1]) * 1024 for l in
                      open("/proc/meminfo") if l.startswith("MemAvailable:"))
    except Exception:  # noqa: BLE001 — non-Linux or unreadable: defer to _worker_cap
        _avail = 0
    _mem_cap = int(_avail * 0.60 / _peak_bytes) if _avail else multi.cpu_count()
    if _avail and not _explicit_workers:
        print(f"  worker cap: cores={multi.cpu_count()} "
              f"mem={_avail / 2**30:.1f}GiB avail / "
              f"{_peak_bytes / 2**30:.1f}GiB peak-per-worker -> {_mem_cap}",
              flush=True)

    if _avail and not _explicit_workers and _mem_cap < 1:
        # REFUSE rather than attempt. Not even one process fits, so running
        # anyway means an OOM kill partway through the χ fan-out — i.e. AFTER
        # the incremental save has already replaced the committed witness.
        # `_carry_forward` makes that non-destructive now, but knowingly
        # starting a computation that cannot finish still burns 20 minutes to
        # end in SIGKILL. Record the reason instead; the committed entry for
        # this atom is carried forward untouched.
        #
        # Only when nothing explicit was asked for: `--workers 1` on a box the
        # operator knows better than /proc/meminfo does must still run.
        print(f"  SKIP {label}: needs ~{_peak_bytes / 2**30:.1f}GiB for the "
              f"largest λ (dim {max(_lambda_cost_proxy(l) for l in parts)}), "
              f"{_avail / 2**30:.1f}GiB available — pass --workers N to force",
              flush=True)
        return {
            "label": label, "Z": Z, "N": N, "A": A, "n_strands": n,
            "abs_tr_M_at_q0": str(abs_tr_M),
            "rho_K_LO": str(rho_K_LO),
            "status": "skip_insufficient_memory",
            "required_bytes_estimate": int(_peak_bytes),
            "available_bytes": int(_avail),
        }

    n_workers = min(_worker_cap(), len(parts))
    if not _explicit_workers and _avail:
        n_workers = min(n_workers, max(1, _mem_cap))
    print(f"  computing per-λ χ^λ via {n_workers} workers (numeric path) …", flush=True)
    # Largest λ FIRST, and chunksize=1 (bean qou-mnrd). Per-λ cost is steeply
    # superlinear in the partition's dimension — measured ~dim^2.4 on this
    # kernel (dim 1925 → 7.1 s, dim 3520 → 30.4 s), so the single largest
    # partition of 12 (dim 7700) costs ≈ 200 s while the smallest cost
    # milliseconds. Two consequences the previous call got wrong:
    #
    #   * `pool.map`'s default chunksize splits the list into ~4 contiguous
    #     blocks, so whichever worker draws the block holding the big λ runs
    #     alone while the others finish and idle. Observed on the ⁴He leg:
    #     worker CPU 11m51s / 4m35s / 1m35s / 0m00s over 2h05m wall.
    #   * feeding them in enumeration order leaves a 200 s task to be picked up
    #     last, so the whole run waits on one straggler at the end.
    #
    # Longest-processing-time-first with chunksize=1 is the standard remedy for
    # both. `pool.map` returns in INPUT order, so the results are reordered back
    # to `parts` order below — the per-λ loop indexes `chi_values[i]` against
    # `parts[i]` and would silently mismatch otherwise.
    order = sorted(range(len(parts)), key=lambda i: -_lambda_cost_proxy(parts[i]))
    pool_args = [(parts[i], crossings, Q_50_DIGIT_STR, mp.mp.dps) for i in order]
    if n_workers > 1:
        with multi.Pool(n_workers) as pool:
            _out = pool.map(_chi_worker, pool_args, chunksize=1)
        chi_values = [None] * len(parts)
        for slot, val in zip(order, _out):
            chi_values[slot] = val
    else:
        # Single worker: same reordering, so the un-permute below is the only
        # place that knows about `order` and the two branches cannot diverge.
        _out = [_chi_worker(a) for a in pool_args]
        chi_values = [None] * len(parts)
        for slot, val in zip(order, _out):
            chi_values[slot] = val

    per_lambda: list[dict] = []
    sum_contributions = mp.mpf(0)
    for i, lam in enumerate(parts):
        # 1/dim_q(λ) at q_0
        d_q = dim_q(lam)
        d_q_q0 = evaluate_at_q0(d_q)
        delta_B = mp.mpf(1) / d_q_q0

        # y_λ at q_0 — load_y_lambda_for_n returns sp.Expr (n≤12,
        # symbolic) or mp.mpf (n>12, pre-evaluated). Handle both.
        y_lam_val = y_lambda[lam]
        if isinstance(y_lam_val, mp.mpf):
            y_q0 = y_lam_val
        else:
            y_q0 = evaluate_at_q0(y_lam_val)

        # χ^λ(β_atom) at q_0 — from parallel pool result.
        chi_q0 = chi_values[i]

        # _chi_worker returns the numpy f64 kernel's result when numpy is
        # importable and the full-precision mpmath result otherwise, so
        # neither form can be assumed here.
        chi_str = str_at_true_precision(chi_q0)

        y_chi = y_q0 * chi_q0
        contribution = y_chi * delta_B
        sum_contributions += contribution

        per_lambda.append({
            "partition": list(lam),
            "self_dual": lam == conjugate(lam),
            "dim_q_at_q0": str(d_q_q0),
            "Delta_lambda_co_casimir": str(delta_B),
            "y_lambda_at_q0": str(y_q0),
            "chi_lambda_at_q0": chi_str,
            "y_chi_product_signed": str(y_chi),
            "contribution_y_chi_Delta": str(contribution),
        })

        if (i + 1) % max(1, len(parts) // 10) == 0 or i == len(parts) - 1:
            print(f"    [{i+1:>3}/{len(parts):>3}] λ={list(lam)} → contribution = {mp.nstr(contribution, 8)}",
                  flush=True)

    # Δρ_K from co-Casimir = (1/|tr_M|) · Σ_λ y_λ χ^λ Δ_λ
    delta_rho_pred = sum_contributions / abs_tr_M
    rho_K_pred = rho_K_LO + delta_rho_pred
    M_pred = rho_K_pred * M_E_MEV * abs_tr_M

    # Comparison vs CODATA / AME
    M_codata = constituent_sum  # M = Z·m_p + N·m_n (no binding here;
                                 # binding emerges as residual)
    err_MeV = M_pred - M_codata
    err_ppm = (err_MeV / M_codata * 1e6) if M_codata else None

    t1 = time.time()
    print(f"  Σ_λ contributions   = {mp.nstr(sum_contributions, 12)}")
    print(f"  Δρ_K^pred           = {mp.nstr(delta_rho_pred, 12)}")
    print(f"  ρ_K^pred            = {mp.nstr(rho_K_pred, 18)}")
    print(f"  M_pred = ρ·m_e·|tr| = {mp.nstr(M_pred, 12)} MeV")
    print(f"  M_codata (Zm_p+Nm_n) = {mp.nstr(M_codata, 12)} MeV")
    print(f"  err vs CODATA       = {mp.nstr(err_MeV, 8)} MeV ({mp.nstr(err_ppm, 6)} ppm)")
    print(f"  wall: {t1 - t0:.1f}s")

    return {
        "label": label, "Z": Z, "N": N, "A": A, "n_strands": n,
        "abs_tr_M_at_q0": str(abs_tr_M),
        "rho_K_LO": str(rho_K_LO),
        "constituent_sum_MeV": str(constituent_sum),
        "delta_rho_pred_co_casimir": str(delta_rho_pred),
        "rho_K_pred_co_casimir": str(rho_K_pred),
        "M_pred_MeV": str(M_pred),
        "M_codata_MeV": str(M_codata),
        "err_MeV": str(err_MeV),
        "err_ppm": str(err_ppm) if err_ppm is not None else None,
        "n_partitions": len(parts),
        "per_lambda": per_lambda,
        "compute_wall_sec": f"{t1 - t0:.2f}",
        "status": "ok",
    }


# ── Main ─────────────────────────────────────────────────────────

# Default atoms — every L1 atom for which we have BOTH |tr_M| and y_λ.
DEFAULT_ATOMS = [
    (1, 0, "proton"),
    (0, 1, "neutron"),
    (1, 1, "deuteron"),
    (1, 2, "tritium"),
    (2, 1, "helium-3"),
    (2, 2, "helium-4"),
    # Extended coverage (per repo-owner directive 2026-05-19
    # "all nucleotides" + Wenzl-bridge numeric witness now n=2..30
    # which covers A up to 10 via 3A=30 strands).
    (3, 2, "lithium-5"),    # A=5, n=15, p(15)=176 partitions
    (3, 3, "lithium-6"),    # A=6, n=18, p(18)=385 partitions
    (3, 4, "lithium-7"),    # A=7, n=21, p(21)=792 partitions
    (4, 3, "beryllium-7"),  # A=7, n=21
    (4, 4, "beryllium-8"),  # A=8, n=24, p(24)=1575 partitions
    (4, 5, "beryllium-9"),  # A=9, n=27, p(27)=3010 partitions
    (5, 5, "boron-10"),     # A=10, n=30, p(30)=5604 partitions (boundary)
]


def main(argv: list[str] | None = None) -> int:
    # Capture start_time at the very top so WitnessBuilder.durationMs
    # reflects actual compute time, not just serialization.
    # (Copilot review #4 on PR #808.)
    start_time = time.monotonic()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--atoms", default=None,
        help="Comma-separated atom labels (default: p,n,D,T,3He,4He)."
    )
    parser.add_argument(
        "--workers", type=int, default=None,
        help="Cap the per-lambda worker pool (default: cpu_count()). Each "
             "worker holds one partition's DENSE Hoefsmit generators — 5.22 GB "
             "at the dim-7700 partition of n=12 — so the default can exceed "
             "RAM and hang rather than slow down. Also settable as "
             "$RHO_K_WORKERS.")
    parser.add_argument(
        "--max-A", type=int, default=4,
        help="Skip atoms with A > this (default 4; ⁴He included; ⁵/⁶Li skipped)."
    )
    args = parser.parse_args(argv)
    if args.workers is not None:
        global _WORKER_OVERRIDE
        _WORKER_OVERRIDE = args.workers

    if args.atoms:
        wanted = {s.strip().lower() for s in args.atoms.split(",")}
    else:
        wanted = None

    print("=" * 96)
    print("ρ_K via Frobenius co-Casimir Option B — multi-atom extension")
    print(f"  q_0 = {mp.nstr(Q_MP, 25)}")
    print(f"  m_e = {mp.nstr(M_E_MEV, 8)} MeV")
    print("=" * 96)

    # Incremental save: write witness after each atom so an interrupt
    # doesn't lose completed work.
    #
    # ...which is exactly what it USED to do (bean qou-mnrd). The write was a
    # plain overwrite of `per_atom` with whatever this run had reached, so any
    # atom the run had not got to yet VANISHED from the committed witness. On a
    # 16 GiB box the ⁴He leg OOMs (a single process peaks at 15.9 GiB at
    # n=12, dim 7700), and each attempt left a 5-atom witness where a 6-atom one
    # had been — `durationMs` 2,552,837 -> 806. Three times in one session.
    #
    # So the "incremental" save loses committed work precisely when the run
    # fails, which is the only time it matters. Same defect, same fix, as
    # `ground_state_ordering_argmin_sweep.py` earlier in this arc: **carry
    # forward what is already on disk and this run did not recompute**, and say
    # which. A producer that can only ever be run to completion on a big enough
    # machine is not a safe producer.
    def _carry_forward(results_so_far: list[dict]) -> list[dict]:
        out_path = HERE / "rho-k-co-casimir-extended.witness.json"
        if not out_path.exists():
            return results_so_far
        try:
            prior = json.loads(out_path.read_text())["data"]["per_atom"]
        except Exception:  # noqa: BLE001 — unreadable/absent: nothing to preserve
            return results_so_far
        # A DID-NOT-COMPUTE RESULT MUST NOT DISPLACE A COMPUTED ONE. The first
        # version of this keyed purely on label, so the `skip_insufficient_memory`
        # stub counted as "this run has helium-4" and overwrote the committed
        # entry — 77 `per_lambda` rows and a real `compute_wall_sec` replaced by
        # a five-field stub. Quieter than dropping the atom outright and just as
        # much data gone, which is the failure mode this function exists to stop.
        _NON_RESULT = {"skip_insufficient_memory", "skip_chi"}
        computed = {r.get("label") for r in results_so_far
                    if r.get("status") not in _NON_RESULT}
        prior_by_label = {p.get("label"): p for p in prior}

        kept: list[dict] = []
        for r in results_so_far:
            lbl = r.get("label")
            if r.get("status") in _NON_RESULT and lbl in prior_by_label:
                # Keep the committed result, but say why it was not recomputed —
                # a preserved value that silently looks fresh is its own trap.
                p = dict(prior_by_label[lbl])
                p["not_recomputed_this_run"] = r.get("status")
                if "required_bytes_estimate" in r:
                    p["not_recomputed_required_bytes"] = r["required_bytes_estimate"]
                    p["not_recomputed_available_bytes"] = r.get("available_bytes")
                print(f"  PRESERVING committed {lbl}: this run returned "
                      f"{r.get('status')}, keeping the stored result", flush=True)
                kept.append(p)
            else:
                kept.append(r)

        carried = [p for p in prior
                   if p.get("label") not in {k.get("label") for k in kept}]
        if carried:
            print(f"  carrying forward {len(carried)} atom(s) this run did not "
                  f"reach: {', '.join(str(c.get('label')) for c in carried)}",
                  flush=True)
        # Preserve the committed ordering: prior order first, then anything new.
        order = {p.get("label"): i for i, p in enumerate(prior)}
        merged = kept + carried
        return sorted(merged, key=lambda r: order.get(r.get("label"), 10**6))

    def _save_incremental(results_so_far: list[dict]) -> Path:
        results_so_far = _carry_forward(results_so_far)
        b = (
            WitnessBuilder(
                "rho-k-co-casimir-extended",
                engine="python+mpmath",
                start_time=start_time,
            )
            .set_description(
                "Substrate-derived ρ_K^pred via the Frobenius co-Casimir "
                "Option B for every L1 atom — incremental save."
            )
            .add_parameter("q_0", Q_50_DIGIT_STR)
            .add_parameter("m_e_MeV", str(M_E_MEV))
            .add_parameter("n_ok", sum(1 for r in results_so_far if r["status"] == "ok"))
            .add_data("per_atom", results_so_far)
        )
        for u in [
            _pb.witness_path("canonical-mass-table-extended.witness.json", HERE),
            HERE / "y-lambda-wenzl-bridge-symbolic-witness.json",
            _pb.witness_path("rho-k-h3a-refinement.witness.json", HERE),
            _pb.witness_path("rho-k-h3a-co-casimir.witness.json", HERE),
        ]:
            if u.exists():
                b.add_upstream(u)
        return b.save()

    results: list[dict] = []
    for Z, N, label in DEFAULT_ATOMS:
        A = Z + N
        if A > args.max_A:
            print(f"\n  skipping {label} (A={A} > max_A={args.max_A})")
            continue
        if wanted is not None:
            short_aliases = {
                "p", "n", "d", "t", "3he", "4he",
                "proton", "neutron", "deuteron", "tritium",
                "helium-3", "helium-4",
            }
            aliases = {label.lower()}
            if label == "proton": aliases |= {"p"}
            if label == "neutron": aliases |= {"n"}
            if label == "deuteron": aliases |= {"d"}
            if label == "tritium": aliases |= {"t"}
            if label == "helium-3": aliases |= {"3he"}
            if label == "helium-4": aliases |= {"4he"}
            if not (aliases & wanted):
                continue
        results.append(compute_co_casimir_for_atom(Z, N, label))
        # Save after each atom so interrupts don't lose work.
        _save_incremental(results)

    # Route the FINAL write through the same merge as the incremental ones.
    # Missing this was a real bug: `_save_incremental` preserved the committed
    # ⁴He block correctly on every intermediate save, and then the final
    # `builder.save()` below — a separate WitnessBuilder that never consulted
    # what was on disk — overwrote it with the skip stub anyway. A guard applied
    # on all but the last write is not a guard. `_carry_forward` reads the file,
    # so it must run BEFORE this builder replaces it.
    results = _carry_forward(results)

    # Emit witness
    builder = (
        WitnessBuilder(
            "rho-k-co-casimir-extended",
            engine="python+mpmath",
            start_time=start_time,
        )
        .set_description(
            "Substrate-derived ρ_K^pred via the Frobenius co-Casimir "
            "Option B (Δ_λ := 1/dim_q(λ), forced by "
            "thm:frobenius-codim-universal — zero free parameters, "
            "τ-invariant). Loads y_λ from EITHER the symbolic Wenzl-"
            "bridge witness (n=2..12, sp.Expr in q) OR the numeric "
            "Wenzl witness (n=2..30, mp.mpf at q_0) — picks whichever "
            "covers the requested n. Per repo-owner directive 2026-"
            "05-19 'all nucleotides', DEFAULT_ATOMS extended to "
            "A ≤ 10 (5Li, 6Li, 7Li, 7Be, 8Be, 9Be, 10B); gate via "
            "--max-A (default 4). Generalises rho_k_h3a_co_casimir.py "
            "from D-only. Witness MeV scaling: rows use m_e (CAL-1) "
            "as the natural scale for ρ_K^LO and the co-Casimir "
            "correction; per-atom 'M_pred_MeV' = ρ_K_pred · m_e · "
            "|tr_M|. Note: binding-via-interface-knot.witness.json "
            "uses E_0 = Q_β(n) instead — different scale by ~m_e/E_0 "
            "≈ 0.65×."
        )
        .add_parameter("q_0", Q_50_DIGIT_STR)
        .add_parameter("m_e_MeV", str(M_E_MEV))
        .add_parameter("atoms_attempted", [r["label"] for r in results])
        .add_parameter("n_ok", sum(1 for r in results if r["status"] == "ok"))
        .add_data("per_atom", results)
    )
    for u in [
        _pb.witness_path("canonical-mass-table-extended.witness.json", HERE),
        HERE / "y-lambda-wenzl-bridge-symbolic-witness.json",
        _pb.witness_path("rho-k-h3a-refinement.witness.json", HERE),
        _pb.witness_path("rho-k-h3a-co-casimir.witness.json", HERE),
    ]:
        if u.exists():
            builder.add_upstream(u)
    out = builder.save()
    print()
    print(f"  Witness: {out.name}")

    # Brief summary
    print()
    print("=" * 96)
    print(f"  {'atom':<10} {'n':>3} {'p(n)':>5} {'status':<12} {'ρ_K^pred':>22} {'err vs CODATA':>20}")
    print("-" * 96)
    for r in results:
        if r["status"] != "ok":
            print(f"  {r['label']:<10} {r.get('n_strands','?'):>3} {'':>5} {r['status']:<12}")
            continue
        print(f"  {r['label']:<10} {r['n_strands']:>3} {r['n_partitions']:>5} {'ok':<12} "
              f"{r['rho_K_pred_co_casimir'][:18]:>22}  {r['err_ppm']:>16} ppm")
    return 0


if __name__ == "__main__":
    sys.exit(main())
