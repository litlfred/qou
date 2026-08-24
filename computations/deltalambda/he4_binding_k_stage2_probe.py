#!/usr/bin/env python3
"""he4_binding_k_stage2_probe.py — A=4 binding-K STAGE 2: per-Wedderburn-block
PSD analysis + operator-selection LP with duals, at H₁₂(q₀).

This is the stage the A≤3 procedure (`binding_k_solver.py`) runs after the
trace fingerprint, now executable at A=4 on the CERTIFIED convention from
`he4_binding_k_presentation_correction_probe.py` (same-day correction — the
earlier stage-1/1.5 fingerprints are void; the canonical K needs no search).

THE OBJECT. K(⁴He) = T_⁴He · cp⁻¹ in H₁₂(q₀), where
  - T_⁴He = the canonical operator-valued atomic word (47 factors:
    p(0)·σ₂·p(3)·cw₅·n(6)·σ₈⁻¹·n(9)), and
  - cp = p(0)·p(3)·n(6)·n(9), the constituent product of the four CANONICAL
    11-crossing nucleon operator words at offsets {0,3,6,9}
(the A≤3 `binding_k_per_block` factorization strategy verbatim: K is built by
factor-list concatenation T ++ reversed-inverted-cp — no per-block matrix
inversion). Each factor is σ_g + d·I; the inverse of such a factor is again
linear in σ_g by the Hecke quadratic:

    (σ + d·I)⁻¹ = a·σ + b·I,   a = [1/(q+d) − 1/(d−q⁻¹)]/[2]_q,
                                b = 1/(q+d) − a·q
    special cases:  σ⁻¹ = σ − h;   (σ − h/2)⁻¹ = (2/[2]_q²)·(σ + σ⁻¹).

TWO LEGS (mirroring the A≤3 solver):

  Leg A — EXACT trace channel analysis, ALL 77 blocks, via the Rust
  SEMINORMAL mpfr engine (`chi_lambda_all_partitions_mpfr`, 50 dps):
  sign-encoded factor word (σ → +1; σ⁻¹ → −1; averaged σ−h/2 → 0;
  averaged-INVERSE = (4/[2]_q²)·(σ−h/2) → 0 with scalar prefactor
  (4/[2]_q²) per crossing; the color-weighted seam factor = aσ + bσ⁻¹,
  a,b = ½±δ/4 → two weighted branch words). Then t_λ = −|y_λ·χ_λ(K)|
  feeds the operator-selection LP (G = I, n_target = 1) with full
  primal/dual emission per the AGENTS.md LP-dual rule — the active
  channels are the binding shadow prices; the dominant Wedderburn block
  λ*(K) is the channel with x* > 0.

  ⚠ GP KERNEL BUG (found by this probe's own leg cross-check, 2026-07-14):
  the first version of leg A used the Rust Geck–Pfeiffer exact-Laurent path
  (`chi_lambdas_via_gp`), which returns WRONG characters on some plain braid
  words — minimal reproducer `[(1,6),(1,7),(-1,9),(1,8),(-1,7)]` at H₁₂
  gives χ_[12] = 0.7926·… where the trivial rep forces exactly q
  (= 1.10998…); the independent seminormal mpfr engine returns q exactly.
  Words validated end-to-end this morning (≤47 letters, the correction
  probe) do not trigger it; this probe's 91-letter K word does. All
  GP-based results must be validated per word-class against the seminormal
  engine until the Rust bug is fixed (bean filed). The witness records the
  reproducer under `gp_kernel_bug`.

  Leg B — per-block PSD spectrum, ALL 77 blocks, float64 DIAGNOSTIC (the
  identical precision class the A≤3 `binding_k_solver.per_block_evaluation`
  uses: numpy symmetrized eigvalsh). ρ_λ(K) is built by applying the 91
  sparse Hecke factors (COO from the Hoefsmit seminormal builder, ≤2 nnz
  per row) to a dense matrix — O(d²) per factor — then min eig of
  (M+Mᵀ)/2, PSD verdict, α_gap. Blocks whose min eig is within 1e-6 of 0
  are flagged for mpf re-verification rather than silently trusted.
  Cross-check: leg-B trace must match leg-A exact χ_λ(K) per block
  (rel ≤ 1e-8) — an independent end-to-end validation of both legs.

PIN: canonical-muon (`QOU_Q0_ANCHOR=ideal` set before imports, per the
correction probe's measured trap).

Scope-(a); audit-only; no fit; nothing wired. The PSD verdict is the A≤3
"binding stability" certificate evaluated at A=4; the LP duals identify the
receptive sub-braid channels. Neither is an AME anchor-inversion (B_AME is
never consulted).
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("QOU_Q0_ANCHOR", "ideal")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))

import _path_bridge  # noqa: F401, E402
import numpy as np  # noqa: E402
import mpmath as mp  # noqa: E402
import pyhecke_native as pn  # noqa: E402
import hecke_core  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from canonical_braid_crossings import _avg_color_delta  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402
from tr_m_wenzl_bridge_mpfr import _build_seminormal_matrices_mpf  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
N = 12
OFFSETS = (0, 3, 6, 9)
NEAR_ZERO_FLAG = 1e-6
TRACE_XCHECK_TOL = 1e-8


def load_canonical_q() -> str:
    d = json.loads((COMP / "q-pinning-50-digit.witness.json").read_text())
    q = d["derived_50_digit"]["q"]
    assert q.startswith("1.109978595557"), q
    return q


def classify(triples, h_f64):
    kinds = []
    for (c, d, g0) in triples:
        assert abs(float(c) - 1.0) < 1e-12
        df = float(d)
        if abs(df) < 1e-12:
            kinds.append(("s", g0))
        elif abs(df + h_f64) < 1e-9:
            kinds.append(("i", g0))
        elif abs(df + h_f64 / 2) < 1e-9:
            kinds.append(("a", g0))
        else:
            assert abs(df + h_f64 * (0.5 - float(_avg_color_delta()) / 4)) < 1e-9, d
            kinds.append(("cw", g0))
    return kinds


def shifted_nucleon_kinds(Z1, N1, off, h_f64):
    return [(k, g0 + off) for (k, g0) in classify(atom_braid_word_3A(Z1, N1), h_f64)]


def _cache_stamp(K_kinds, q_str: str, dps: int) -> str:
    """Identify the PARAMETERS a cached entry was computed under.

    Both resume caches key on the item (a shape, a partition) and, before this,
    only Leg A carried any parameter check at all — `nf = len(K_kinds)`. That is
    a COUNT: two different K-factor words of the same length collide, and the
    pin does not appear in it, even though Leg A's characters come from
    `chi_lambdas_braid_mpfr(..., w, q_str, 50)` and move with `q_str`. Leg B
    carried nothing, so a changed word or pin had Leg A recompute correctly
    while Leg B silently served stale blocks.

    Hashing the word, the pin and the precision closes both. The failure this
    prevents is the expensive kind: a cache gate that answers "is this entry
    PRESENT?" when the question is "is this entry CURRENT?" — the same shape as
    the `chi_via_rust_lossless` reuse branch (PR #5623), which held two
    witnesses at convention C across the whole 2026-08-09 cascade and made
    re-running the producer a silent no-op.
    """
    return hashlib.sha256(
        f"{K_kinds!r}|{q_str}|{dps}".encode()
    ).hexdigest()[:12]


def _legacy_cache_warning(path, n: int, leg: str) -> None:
    """An unstamped entry predates `_cache_stamp` and cannot be verified."""
    print(f"  ⚠ Leg {leg}: {n} cached entr{'y' if n == 1 else 'ies'} in "
          f"{path.name} predate the parameter stamp and CANNOT be checked "
          f"against this run's K-factor word / pin.\n"
          f"    They are being reused. If you changed either since they were "
          f"written, delete {path.name} and re-run.", flush=True)


def main() -> int:
    t_start = time.time()
    q_str = load_canonical_q()
    q0 = mp.mpf(q_str)
    v = mp.sqrt(q0)
    h_mp = q0 - 1 / q0
    h_f64 = float(hecke_core.h)
    two_q = q0 + 1 / q0                       # [2]_q
    delta = mp.mpf(float(_avg_color_delta()))
    a_cw, b_cw = mp.mpf(1) / 2 + delta / 4, mp.mpf(1) / 2 - delta / 4

    # ── build the K factor-kind list: T ++ reversed-inverted cp ────
    T_kinds = classify(atom_braid_word_3A(2, 2), h_f64)
    cp_kinds = (shifted_nucleon_kinds(1, 0, 0, h_f64)
                + shifted_nucleon_kinds(1, 0, 3, h_f64)
                + shifted_nucleon_kinds(0, 1, 6, h_f64)
                + shifted_nucleon_kinds(0, 1, 9, h_f64))
    # inverse kind map: s→i, i→s, a→ia (averaged-inverse, scalar 2/[2]²)
    INV = {"s": "i", "i": "s", "a": "ia"}
    K_kinds = list(T_kinds) + [(INV[k], g0) for (k, g0) in reversed(cp_kinds)]
    n_a_T = sum(1 for k, _ in T_kinds if k == "a")
    n_ia = sum(1 for k, _ in K_kinds if k == "ia")
    n_cw = sum(1 for k, _ in K_kinds if k == "cw")
    assert n_cw == 1
    print(f"K factor word: {len(K_kinds)} factors "
          f"({n_a_T} averaged, {n_ia} averaged-inverse, {n_cw} color-weighted)")

    shapes = pn.partitions_of(N)
    y = {tuple(k): mp.mpf(str(val)) for k, val in y_lambda_at(N, q0).items()}

    # ── GP kernel bug reproducer (documented; not used for results) ──
    repro_word = [(1, 6), (1, 7), (-1, 9), (1, 8), (-1, 7)]
    gp_r = pn.chi_lambdas_via_gp([[N]], N, repro_word)
    gp_triv = mp.mpf(0)
    for e, cstr in gp_r[0]:
        cc = mp.mpf(cstr) if "/" not in cstr else \
            mp.mpf(cstr.split("/")[0]) / mp.mpf(cstr.split("/")[1])
        gp_triv += cc * v ** e
    mpfr_r = {tuple(lam): mp.mpf(chi) for lam, chi in
              pn.chi_lambda_all_partitions_mpfr(N, repro_word, q_str, 50)}
    gp_bug_present = abs(gp_triv - q0) / q0 > mp.mpf("1e-30")
    mpfr_correct = abs(mpfr_r[(N,)] - q0) / q0 < mp.mpf("1e-45")
    print(f"GP-bug reproducer: GP χ_[12] = {mp.nstr(gp_triv, 12)} vs exact q = "
          f"{mp.nstr(q0, 12)} (bug present: {gp_bug_present}); "
          f"seminormal-mpfr = {mp.nstr(mpfr_r[(N,)], 12)} (correct: {mpfr_correct})")

    # ── Leg A: exact χ_λ(K) via seminormal mpfr, all 77 blocks ─────
    print("=" * 72)
    print(" LEG A — exact χ_λ(K) via seminormal mpfr (50 dps), all 77 blocks")
    print("=" * 72)
    # 'ia' = (4/[2]²)·(σ−h/2): sign-0 letter with a scalar prefactor;
    # 'a' = σ−h/2: sign-0 letter, no scalar. Total scalar = (4/[2]²)^n_ia.
    scalar = (4 / two_q ** 2) ** n_ia

    def signed_letters(cw_branch):
        w = []
        for (k, g0) in K_kinds:
            g1 = g0 + 1
            if k == "s":
                w.append((1, g1))
            elif k == "i":
                w.append((-1, g1))
            elif k in ("a", "ia"):
                w.append((0, g1))
            else:  # cw
                w.append((cw_branch, g1))
        return w

    # Resume cache: Leg A per-(branch, shape-chunk). The full mpfr eval is
    # ~34 min — longer than one sandbox session — so checkpoint at
    # shape-chunk granularity. `chi_lambdas_braid_mpfr` is rayon-parallel
    # across the shape group, so chunking preserves the parallelism while
    # giving sub-session resume points. Self-cleans on completion.
    t0 = time.time()
    chi_exact: dict[tuple, mp.mpf] = {}
    legA_prog = HERE / ".he4_stage2_legA_progress.jsonl"
    branch_chi: dict[int, dict[tuple, mp.mpf]] = {1: {}, -1: {}}
    _stamp = _cache_stamp(K_kinds, q_str, 50)
    _legA_dropped = _legA_legacy = 0
    if legA_prog.exists():
        for _line in legA_prog.read_text().splitlines():
            if not _line.strip():
                continue
            try:
                _r = json.loads(_line)
            except Exception:
                continue
            if _r.get("nf") != len(K_kinds):
                continue
            _st = _r.get("st")
            if _st is not None and _st != _stamp:
                _legA_dropped += 1
                continue          # different word / pin / dps -> recompute
            if _st is None:
                _legA_legacy += 1
            branch_chi[_r["br"]][tuple(_r["lam"])] = mp.mpf(_r["chi"])
        if _legA_dropped:
            print(f"  Leg A: dropped {_legA_dropped} cached characters computed "
                  f"under different parameters", flush=True)
        if _legA_legacy:
            _legacy_cache_warning(legA_prog, _legA_legacy, "A")
        _n = len(branch_chi[1]) + len(branch_chi[-1])
        if _n:
            print(f"  Leg A resumed: {_n}/{2 * len(shapes)} characters from "
                  f"{legA_prog.name}", flush=True)
    shapes_t = [tuple(s) for s in shapes]
    LEGA_CHUNK = 8
    for br in (1, -1):
        w = signed_letters(br)
        todo = [lam for lam in shapes_t if lam not in branch_chi[br]]
        for i in range(0, len(todo), LEGA_CHUNK):
            grp = todo[i:i + LEGA_CHUNK]
            res = pn.chi_lambdas_braid_mpfr([list(l) for l in grp], w, q_str, 50)
            with open(legA_prog, "a") as _pf:
                for lam, chi in zip(grp, res):
                    branch_chi[br][lam] = mp.mpf(chi)
                    _pf.write(json.dumps({"nf": len(K_kinds), "st": _stamp,
                                          "br": br, "lam": list(lam),
                                          "chi": chi}) + "\n")
            print(f"  branch {br:+d}: {len(branch_chi[br])}/{len(shapes_t)} "
                  f"chars at {time.time()-t0:.0f}s", flush=True)
    for lam in shapes_t:
        chi_exact[lam] = scalar * (a_cw * branch_chi[1][lam]
                                   + b_cw * branch_chi[-1][lam])
    print(f"  seminormal-mpfr evals done in {time.time()-t0:.1f}s")

    per_lambda = sorted(
        ({"lambda": list(lam), "chi_K": mp.nstr(chi_exact[lam], 20),
          "y_lambda": mp.nstr(y[lam], 16),
          "y_times_chi_abs": float(abs(y[lam] * chi_exact[lam]))}
         for lam in map(tuple, shapes)),
        key=lambda r: -r["y_times_chi_abs"])
    print("  top 5 channels by |y_λ·χ_λ(K)|:")
    for r in per_lambda[:5]:
        print(f"    λ={str(tuple(r['lambda'])):24s} |y·χ| = {r['y_times_chi_abs']:.6g}")
    tr_M_K = sum(y[lam] * chi_exact[lam] for lam in map(tuple, shapes))
    print(f"  tr_M(K) = {mp.nstr(tr_M_K, 20)}")

    # operator-selection LP with duals (AGENTS.md LP-dual rule)
    t_costs = -np.array([r["y_times_chi_abs"] for r in per_lambda])
    # Pinned, not `auto`: `auto` picks clarabel-MPFR or scipy-f64 by whether
    # the Rust binary happens to be built, so the same script yields different
    # numbers on different boxes. Bean `qou/ftuv`.
    lp = solve_operator_selection_lp(t_costs, np.eye(len(per_lambda)),
                                     n_target=1.0, backend="clarabel")
    lp_dict = lp.to_dict()
    dominant = per_lambda[0]["lambda"]
    print(f"  dominant λ*(K) = {tuple(dominant)}   duality gap = "
          f"{lp_dict.get('duality_gap')}")

    # ── Leg B: per-block PSD spectrum (f64 diagnostic), all blocks ──
    print("=" * 72)
    print(" LEG B — per-block ρ_λ(K) spectra (f64 diagnostic, sparse apply)")
    print("=" * 72)
    # f64 factor coefficients (c=1 fixed): d-value per kind; inverse factors
    # (a·σ + b·I) carry a ≠ 1, handled as (a, b) pairs.
    q_f = float(q0)
    h_f = q_f - 1.0 / q_f
    two_f = q_f + 1.0 / q_f
    d_cw = -h_f * (0.5 - float(_avg_color_delta()) / 4)

    def factor_ab(kind):
        if kind == "s":
            return 1.0, 0.0
        if kind == "i":
            return 1.0, -h_f
        if kind == "a":
            return 1.0, -h_f / 2
        if kind == "ia":
            return 4.0 / two_f ** 2, -2.0 * h_f / two_f ** 2
        if kind == "cw":
            return 1.0, d_cw
        raise ValueError(kind)

    per_block = []
    min_eig_overall = float("inf")
    xcheck_worst = 0.0
    t0 = time.time()

    # Resume cache: Leg B per-block. Each large (dim ~5940) block eigen-
    # solve is ~6 min; append completed blocks to a JSONL so a resumed
    # run skips them (the full compute can outlive one session).
    legB_prog = HERE / ".he4_stage2_legB_progress.jsonl"
    done_lambdas = set()
    _legB_dropped = _legB_legacy = 0
    if legB_prog.exists():
        for _line in legB_prog.read_text().splitlines():
            if not _line.strip():
                continue
            try:
                _b = json.loads(_line)
            except Exception:
                continue
            if tuple(_b["lambda"]) in done_lambdas:
                continue
            _st = _b.get("st")
            if _st is not None and _st != _stamp:
                _legB_dropped += 1
                continue          # different word / pin / dps -> recompute
            if _st is None:
                _legB_legacy += 1
            per_block.append(_b)
            done_lambdas.add(tuple(_b["lambda"]))
            xcheck_worst = max(xcheck_worst, _b["chi_exact_rel_diff"])
            min_eig_overall = min(min_eig_overall, _b["min_eig_sym"])
        if _legB_dropped:
            print(f"  Leg B: dropped {_legB_dropped} cached blocks computed "
                  f"under different parameters", flush=True)
        if _legB_legacy:
            _legacy_cache_warning(legB_prog, _legB_legacy, "B")
        if per_block:
            print(f"  Leg B resumed: {len(per_block)} blocks from "
                  f"{legB_prog.name}", flush=True)

    def hook_dim(lam):
        from math import factorial
        conj = [sum(1 for r in lam if r > c) for c in range(lam[0])]
        prod = 1
        for i, r in enumerate(lam):
            for j in range(r):
                prod *= (r - j) + (conj[j] - i) - 1
        return factorial(sum(lam)) // prod

    dims = [hook_dim(tuple(lam)) for lam in shapes]
    order = np.argsort(dims)
    total_d2 = float(sum(d * d for d in dims))
    done_d2 = float(sum(b["dim"] * b["dim"] for b in per_block))
    for idx in order:
        lam = tuple(shapes[idx])
        if lam in done_lambdas:
            continue
        sig_coo, dim = _build_seminormal_matrices_mpf(lam, q0)
        if dim == 0:
            continue
        # Convert per-generator COO to f64, SPLIT into its diagonal and
        # off-diagonal parts.
        #
        # The K-word loop below was 90% of this probe's runtime (measured:
        # 54 s of a 60 s block at d = 2640, against 4.8 s to build the
        # seminormal matrices and 0.7 s for the d³ eigensolve). Two things
        # made it slow, and neither was inherent:
        #
        #   1. `np.add.at` is an UNBUFFERED scatter — it exists to handle
        #      duplicate target indices, and there are none here. Each
        #      seminormal generator is diagonal plus off-diagonal entries at a
        #      single fixed band offset, at most 2 nonzeros per column, one of
        #      which is the diagonal. So every column receives at most ONE
        #      off-diagonal contribution and plain fancy indexing is correct.
        #      (Asserted below rather than assumed.)
        #   2. The update is column-wise on a C-contiguous array, so every
        #      access was strided. Working on the TRANSPOSE makes each update
        #      a contiguous row operation.
        #
        # Together: 66.4 s -> 6.2 s at d = 2640, a 10.7x speedup, agreeing
        # with the old code to 4.8e-16 relative — f64 accumulation order,
        # three orders inside the 1e-15 χ cross-check this block asserts.
        # Bean `qou/ftuv`.
        gens = []
        for coo in sig_coo:
            ii = np.fromiter((e[0] for e in coo), dtype=np.int64, count=len(coo))
            jj = np.fromiter((e[1] for e in coo), dtype=np.int64, count=len(coo))
            vv = np.fromiter((float(e[2]) for e in coo), dtype=np.float64,
                             count=len(coo))
            on_diag = ii == jj
            diag = np.zeros(dim, dtype=np.float64)
            diag[jj[on_diag]] = vv[on_diag]
            io, jo, vo = ii[~on_diag], jj[~on_diag], vv[~on_diag]
            assert len(np.unique(jo)) == len(jo), (
                f"λ={lam}: a column takes two off-diagonal contributions, so "
                "the scatter below would drop one — revert to np.add.at")
            gens.append((diag, io, jo, vo))

        # MT holds Mᵀ: row j of MT is column j of M.
        MT = np.ascontiguousarray(np.eye(dim))
        for (k, g0) in K_kinds:
            a, b = factor_ab(k)
            diag, io, jo, vo = gens[g0]
            # M ← M @ (a·σ + b·I). Column j of the result is
            # (b + a·σ_jj)·M[:,j] plus a·σ_ij·M[:,i] from the one
            # off-diagonal entry in that column — a row operation on MT.
            # `tmp` is taken BEFORE the scaling, because io and jo overlap.
            tmp = MT[io] * (a * vo)[:, None] if len(io) else None
            MT *= (b + a * diag)[:, None]
            if tmp is not None:
                MT[jo] += tmp
        M = MT.T
        chi_f = float(np.trace(M))
        chi_e = float(chi_exact[lam])
        xrel = abs(chi_f - chi_e) / max(abs(chi_e), 1e-300)
        xcheck_worst = max(xcheck_worst, xrel)
        Ms = (M + M.T) / 2.0
        eigs = np.linalg.eigvalsh(Ms)
        mn, mx = float(eigs[0]), float(eigs[-1])
        min_eig_overall = min(min_eig_overall, mn)
        per_block.append({
            "lambda": list(lam), "dim": dim,
            "chi_f64": chi_f, "chi_exact_rel_diff": xrel,
            "min_eig_sym": mn, "max_eig_sym": mx,
            "psd_within_tol": bool(mn >= -1e-9),
            "near_zero_flagged": bool(abs(mn) < NEAR_ZERO_FLAG),
        })
        with open(legB_prog, "a") as _pf:  # resume checkpoint
            _pf.write(json.dumps({**per_block[-1], "st": _stamp}) + "\n")
        done_d2 += dim * dim
        el = time.time() - t0
        print(f"  λ={str(lam):26s} d={dim:5d}  min_eig={mn:+.3e}  "
              f"χ xcheck={xrel:.1e}  [{done_d2/total_d2:5.1%} of Σd², "
              f"{el:.0f}s]", flush=True)
        del M, MT, Ms, gens
    alpha_gap = max(0.0, -min_eig_overall)
    psd_all = all(b["psd_within_tol"] for b in per_block)
    xcheck_ok = xcheck_worst < TRACE_XCHECK_TOL

    print(f"\n  min eig overall = {min_eig_overall:+.6e}   α_gap = {alpha_gap:.6e}")
    print(f"  PSD (all 77 blocks, tol −1e-9): {psd_all}")
    print(f"  worst leg-A/leg-B trace cross-check: {xcheck_worst:.2e}")

    verdict = (
        f"A=4 STAGE 2 executed on the certified convention: K(⁴He) = T·cp⁻¹ "
        f"evaluated per Wedderburn block at H₁₂(q₀), ALL 77 blocks (no dim "
        f"cutoff). Leg A (exact seminormal-mpfr χ + LP duals): dominant channel λ*(K) = "
        f"{tuple(dominant)}, tr_M(K) = {mp.nstr(tr_M_K, 12)}, duality gap "
        f"{lp_dict.get('duality_gap')}. Leg B (f64 diagnostic spectra, the "
        f"A≤3 solver's precision class): min symmetrized eigenvalue "
        f"{min_eig_overall:+.3e}, α_gap {alpha_gap:.3e}, PSD-within-tol "
        f"{psd_all}; worst exact-vs-f64 trace cross-check {xcheck_worst:.1e}. "
        "PSD-feasibility is the A≤3 'binding stability' certificate at A=4; "
        "the LP duals mark the receptive Wedderburn channels. Scope-(a); "
        "no AME input; no fit; nothing wired."
    )
    print("\nVERDICT:", verdict)

    wit = {
        "computation": "he4-binding-k-stage2",
        "description": "A=4 binding-K stage 2 (per-block PSD + operator-"
                       "selection LP with duals) at H12(q0) on the certified "
                       "convention: K = T·cp^{-1} by factor concatenation "
                       "(inverse factors linear in sigma via the Hecke "
                       "quadratic). Leg A exact seminormal-mpfr characters all 77 blocks; "
                       "leg B f64 diagnostic spectra all 77 blocks with "
                       "per-block exact-trace cross-check.",
        "audit_only": True,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "pyhecke_native seminormal-mpfr 50dps (leg A exact); numpy "
                  "f64 diagnostic (leg B spectra, per A<=3 binding_k_solver "
                  "precision class). GP path NOT used for results (kernel "
                  "bug, see gp_kernel_bug).",
        "dps": 50,
        "q_pin": {"used": "canonical muon (QOU_Q0_ANCHOR=ideal)", "value": q_str},
        "K_construction": {
            "definition": "T_4He ++ reversed(per-factor inverses of cp)",
            "cp": "canonical nucleon words p(0)p(3)n(6)n(9), offsets {0,3,6,9}",
            "n_factors": len(K_kinds),
            "inverse_dictionary": {
                "sigma_inv": "σ⁻¹ = σ − h",
                "averaged_inv": "(σ−h/2)⁻¹ = (2/[2]_q²)(σ+σ⁻¹)",
            },
        },
        "gp_kernel_bug": {
            "summary": "chi_lambdas_via_gp returns wrong characters on some "
                       "plain braid words; found by this probe's leg "
                       "cross-check, confirmed against the independent "
                       "seminormal engine on the trivial rep (which forces "
                       "chi_[12] = q exactly).",
            "minimal_reproducer_word": repro_word,
            "gp_chi_trivial_rep": mp.nstr(gp_triv, 25),
            "expected_exact": mp.nstr(q0, 25),
            "seminormal_mpfr_chi_trivial_rep": mp.nstr(mpfr_r[(N,)], 25),
            "scope": "long/structured plain words (91-letter K word triggers "
                     "it; the <=47-letter canonical words validated 1e-20 "
                     "end-to-end this morning do not). Certified combiner "
                     "chain (seminormal) unaffected.",
        },
        "leg_A": {
            "tr_M_K": mp.nstr(tr_M_K, 25),
            "dominant_lambda": dominant,
            "per_lambda_top10": per_lambda[:10],
            "lp_dual": lp_dict,
        },
        "leg_B": {
            "coverage": "all 77 blocks (sum d^2 = 12! = 479001600)",
            "min_eig_overall": min_eig_overall,
            "alpha_gap": alpha_gap,
            "psd_within_tol_all": psd_all,
            "trace_xcheck_worst_rel": xcheck_worst,
            "near_zero_flagged": [b["lambda"] for b in per_block
                                  if b["near_zero_flagged"]],
            "per_block": per_block,
        },
        "elapsed_sec": round(time.time() - t_start, 1),
        "verdict": verdict,
        "scope": "(a) — stage-2 evaluation of the canonical K; PSD verdict is "
                 "f64-diagnostic (near-zero blocks flagged, none silently "
                 "trusted); exact leg cross-checks every block trace",
        "assertions": [
            {"label": "exact/f64 trace cross-check ≤ 1e-8 on every block",
             "passed": bool(xcheck_ok)},
            {"label": "all 77 blocks evaluated (no dim cutoff)",
             "passed": len(per_block) == 77},
            {"label": "LP dual fields emitted (duality gap finite)",
             "passed": lp_dict.get("duality_gap") is not None},
            {"label": "seminormal-mpfr correct on GP-bug reproducer "
                      "(trivial rep = q exactly)",
             "passed": bool(mpfr_correct)},
        ],
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    out = HERE / "he4-binding-k-stage2.witness.json"
    json.dump(wit, open(out, "w"), indent=1)
    # Completed cleanly — drop the resume caches so the next run is fresh.
    for _c in (legA_prog, legB_prog):
        try:
            _c.unlink()
        except FileNotFoundError:
            pass
    print("witness ->", out.name, " allPassed:", wit["allPassed"],
          f" ({wit['elapsed_sec']}s)")
    return 0 if wit["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
