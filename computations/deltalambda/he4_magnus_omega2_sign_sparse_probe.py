#!/usr/bin/env python3
"""he4_magnus_omega2_sign_sparse_probe.py — the A=4 (⁴He, H₁₂) sign datum for the
2nd-order Magnus pairing, via a SPARSE / matrix-free route that makes H₁₂ feasible.

THE QUESTION (extends the A=2 deuteron and A=3 triton probes).
  A=2 (deuteron_magnus_omega2_sign_probe.py, qou-dp32): P<0, control tr_M(Ω₂)=0,
       sign-indefinite. A viable negative-at-A=2 sign-carrier.
  A=3 (triton_magnus_omega2_sign_probe.py, PR #6107): P<0 — NO flip vs A=2. The
       simple "negative→positive at A≥3" reading fails at the triton.
  A=4 (this probe, ⁴He = 2p2n, 12 strands, H₁₂): does P(A=4) continue the negative
       run, or does the sign finally move at the alpha particle? This is the next
       point on the sign-vs-A map the owner asked to extend.

WHY A SPARSE ROUTE (owner directive 2026-08-30). The A=3→A=4 jump is H₉→H₁₂:
partitions 30→77, MAX irrep dim 216→7700, and the dense matmul-cost proxy Σ dim³
rises 35,300× (6.0e7 → 2.1e12). A dense seminormal build allocates an mp.zeros(7700,
7700) (~9 GB) PER generator and OOM-crashes before any arithmetic — the H₁₂ table is
not "slow", it is impossible densely on this hardware. The structure that rescues it:

  1. BLOCK-DIAGONAL GENERATORS. In Young's seminormal (orthogonal) form σ_k mixes
     only pairs of standard tableaux related by swapping k↔k+1, so σ_k is a direct
     sum of 1×1 and 2×2 blocks — O(dim) nonzeros, never O(dim²). σ_k is symmetric.
  2. THE GERM INHERITS THE BLOCKS. A_g = q·(∂_q σ_g)·σ_g⁻¹: ∂_q σ_g and σ_g⁻¹ share
     σ_g's block structure, so A_g is block-diagonal too — computed per 2×2 block
     (exact 2×2 inverse; NO dense O(dim³) inversion, which the dense probe wasted).
  3. FAR-COMMUTATIVITY. [A_a,A_b]=0 whenever |a−b|≥2 (σ_a,σ_b commute ⇒ their germs
     do). Ω₂ = ½Σ_{i<j}[A_{g_i},A_{g_j}] keeps ONLY adjacent-generator commutators.
  4. MATRIX-FREE TRACE. ρ = ∏σ_{g_i} is never materialized. tr(ρ·Ω₂) =
     Σ_k Σ_i Ω₂[k,i]·(ρ e_k)[i]: for each nonzero row k of the sparse Ω₂, apply the
     word to the basis vector e_k as a chain of L sparse mat-vecs (O(dim) each),
     memory O(dim). Cost O(#rows(Ω₂)·L·dim), memory O(dim) — never O(dim²) stored.

THE OBJECT is IDENTICAL to the A=2/A=3 probes (0-fit, canonical, derived):
  germ       A_g = q·(∂_q σ_g)·σ_g⁻¹            (central finite diff, per 2×2 block)
  2nd Magnus Ω₂  = ½ Σ_{i<j} [A_{g_i}, A_{g_j}] (adjacent pairs only, far-comm.)
  ⁴He word   β = atom_braid_word_3A(2,2)         SOURCE OF TRUTH (47 crossings, σ₀..σ₁₀,
             12 strands; the corpus convention, qou-oppb RESOLVED; the same
             constructor the triton used with (1,2))
  density    ρ = ∏ σ_{g_i}                        (bare word; central dressing drops)
  pairing    P = Σ_λ y_λ tr(ρ_λ Ω₂_λ), y_λ = d_q(λ)²/[n]_q!, λ ⊢ 12

CORRECTNESS GATE (runs before any H₁₂ is trusted; see --gate). The sparse method must
(a) reproduce the DENSE seminormal generators exactly on small λ, (b) reproduce the
dense full-matrix germ exactly on small λ, and (c) reproduce the COMMITTED triton
witness P_total to full precision on H₉ with the SAME word. Only then is the H₁₂ run
run. The germ additionally passes the differentiated-Hecke identity per block.

HONESTY (STRICT). scope-(a): a dimensionless structural SIGN datum. Does NOT reproduce
any MeV (open Δ_λ magnitude gate — a number would be a fit). Does NOT assert a physical
binding-sign convention (qou-v7ro / PR #6077, cited not re-derived). No fit; nothing
inverted; nothing wired. NO-FLOAT64: mpmath mpf end to end, dps=140, eps=1e-50; the
germ is a finite-difference q-derivative that cancels ~50 digits, so ~90 remain.
Cites, does not rebuild: qou-dp32 (A=2 carrier+method), PR #6107 (A=3), the merged
Magnus-wall audit (2026-08-29), qou-v7ro/#6077 (sign convention), qou-oppb (⁴He word).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
import time
from math import prod

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "hecke"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "substrate"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402
# Option A (bean qou-q2q7): production Wenzl/Markov weight carried alongside
# the Plancherel measure this probe aggregates with. See
# docs/audits/2026-09-07-magnus-omega2-weight-family-analysis.md.
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402

set_compute_dps()
mp.mp.dps = 140

from hecke_characters import (  # noqa: E402
    build_seminormal_matrices_mp,
    standard_young_tableaux,
)
from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402

Q0 = mp.mpf(_Q0_RESOLVED)
H = Q0 - 1 / Q0
EPS = mp.mpf(10) ** -50
_EXACT = mp.mpf(10) ** -30


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def _dim_estimate(shape):
    """Hook-length dimension f^λ (integer) — for biggest-first scheduling."""
    from math import factorial
    rows = list(shape)
    cols = [sum(1 for r in rows if r > c) for c in range(rows[0])]
    hooks = []
    for i, ri in enumerate(rows):
        for j in range(ri):
            hooks.append((ri - j - 1) + (cols[j] - i - 1) + 1)
    return factorial(sum(shape)) // prod(hooks)


def q_int(k, q):
    if q == 1:
        return mp.mpf(k)
    return (q ** k - q ** (-k)) / (q - 1 / q)


def wedderburn_weight(shape, q):
    """**quantum Plancherel** measure `w_planch(λ) = d_q(λ)² / [n]_q!`
    (symmetric q-integers).

    NOT the Wenzl y_λ (bean qou-za3q). AGENTS.md is explicit that the three
    partition-weight families y_λ / w_λ / w̃_λ are DISTINCT at q ≠ 1 and must
    never be conflated; this docstring used to call this one `y_λ`, which is
    the conflation it forbids, and which makes a corpus scan keying on the
    name `y_lambda` unable to tell this apart from the production weight.

    The two are not a rescaling of each other. At H₃, measured:

        λ            Wenzl y_λ (production)   d_q²/[n]_q! (here)
        (3,)             0.50540423              0.16338323
        (2,1)            0.24729789              0.66067377
        (1,1,1)          0                       0.16338323

    and at higher n the divergence is structural: the Wenzl row cap (level
    r = 2, bean qou-fq0f) annihilates every shape with ≥3 rows, which is where
    the Plancherel measure puts most of its mass — 70 of the 77 partitions of
    12 carry Wenzl weight exactly zero.

    The name is fixed here; whether the Plancherel measure is the RIGHT pairing
    for a Magnus Ω₂ sign question is a separate matter and is not settled by
    this rename. What IS settled (see `sign_robust_to_weight_family` in the
    witness) is that the probe's headline conclusion — the sign of P_total —
    does not depend on the choice.
    """
    n = sum(shape)
    rows = list(shape)
    cols = [sum(1 for r in rows if r > c) for c in range(rows[0])]
    hooks = []
    for i, ri in enumerate(rows):
        for j in range(ri):
            arm = ri - j - 1
            leg = cols[j] - i - 1
            hooks.append(arm + leg + 1)
    # HOOK-LENGTH FORMULA: d_q(λ) = [n]_q! / ∏_x [h(x)]_q.
    #
    # This previously read `dq = prod(q_int(hh, q) for hh in hooks)` — the
    # DENOMINATOR of that formula, not d_q — and then returned dq²/[n]_q!.
    # The result was the EXACT RECIPROCAL of the documented weight:
    # computed H²/[n]_q! where d_q²/[n]_q! = [n]_q!/H². Verified against the
    # committed witnesses to a relative 1e-40, and probe × correct = 1.0
    # identically on every partition checked.
    hook_prod = prod(q_int(hh, q) for hh in hooks)
    nfact = prod(q_int(k, q) for k in range(1, n + 1))
    dq = nfact / hook_prod
    return (dq * dq) / nfact


# ── sparse seminormal structure ──────────────────────────────────────────────
#
# block_structure(shape) returns, for each generator k = 1..n-1 (index k-1), a
# q-INDEPENDENT list of blocks; each block is one of
#   ("diag", i, rho)          σ_k acts as the scalar a(q) on basis vector i
#   ("pair", i, j, rho)       σ_k acts as [[a, b],[b, a']] on the (i,j) 2-space
# rho = content(cell of k+1) − content(cell of k) is the axial distance. This is the
# EXACT block logic of build_seminormal_matrices_mp, factored out of q so the block
# membership is computed once and only the scalars a,a',b depend on q.


def block_structure(shape):
    n = sum(shape)
    syts, cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    syt_index = {tuple(sorted(t.items())): idx for idx, t in enumerate(syts)}
    per_gen = []
    for k in range(1, n):
        blocks = []
        processed = set()
        for i in range(dim):
            if i in processed:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]
            swap_map = dict(syts[i])
            swap_map[k] = ci_k1
            swap_map[k + 1] = ci_k
            j = syt_index.get(tuple(sorted(swap_map.items())))
            if j == i:
                j = None
            if j is None:
                blocks.append(("diag", i, rho))
                processed.add(i)
            else:
                blocks.append(("pair", i, j, rho))
                processed.add(i)
                processed.add(j)
        per_gen.append(blocks)
    return per_gen, dim


def _a_scalars(rho, q):
    """(a, a') for axial distance rho at q — the seminormal block entries."""
    a = H_of(q) / (1 - q ** (-2 * rho))
    a_prime = H_of(q) / (1 - q ** (2 * rho))
    return a, a_prime


def H_of(q):
    return q - 1 / q


def sigma_csr(per_gen, dim, q):
    """List over generators of CSR rows: sig[g][i] = list of (col, val). Symmetric."""
    sig = []
    for blocks in per_gen:
        rows = [[] for _ in range(dim)]
        for blk in blocks:
            if blk[0] == "diag":
                _, i, rho = blk
                a, _ = _a_scalars(rho, q)
                rows[i].append((i, a))
            else:
                _, i, j, rho = blk
                a, ap = _a_scalars(rho, q)
                b = mp.sqrt(abs(a * ap + 1))
                rows[i].append((i, a))
                rows[i].append((j, b))
                rows[j].append((j, ap))
                rows[j].append((i, b))
        sig.append(rows)
    return sig


def germ_csr(per_gen, dim, q, eps):
    """A_g = q·(∂_q σ_g)·σ_g⁻¹ per block (central finite diff). CSR rows.

    Also returns the max residual of the differentiated-Hecke identity
    {σ, σ'} = h'σ + hσ' evaluated per block (must be ~0), as a sanity gate."""
    qp, qm = q + eps, q - eps
    hp = 1 + 1 / q ** 2  # h' = d/dq (q - 1/q)
    hcheck = mp.mpf(0)
    germ = []
    for blocks in per_gen:
        rows = [[] for _ in range(dim)]
        for blk in blocks:
            if blk[0] == "diag":
                _, i, rho = blk
                a, _ = _a_scalars(rho, q)
                ap_p, _ = _a_scalars(rho, qp)
                ap_m, _ = _a_scalars(rho, qm)
                da = (ap_p - ap_m) / (2 * eps)
                rows[i].append((i, q * da / a))
                # Hecke check (scalar block): 2 a da == hp a + H da
                hcheck = max(hcheck, abs(2 * a * da - (hp * a + H_of(q) * da)))
            else:
                _, i, j, rho = blk
                a, apr = _a_scalars(rho, q)
                b = mp.sqrt(abs(a * apr + 1))
                B = mp.matrix([[a, b], [b, apr]])
                a1, ap1 = _a_scalars(rho, qp)
                b1 = mp.sqrt(abs(a1 * ap1 + 1))
                Bp = mp.matrix([[a1, b1], [b1, ap1]])
                a2, ap2 = _a_scalars(rho, qm)
                b2 = mp.sqrt(abs(a2 * ap2 + 1))
                Bm = mp.matrix([[a2, b2], [b2, ap2]])
                dB = (Bp - Bm) / (2 * eps)
                det = a * apr - b * b
                Binv = mp.matrix([[apr, -b], [-b, a]]) / det
                A = q * dB * Binv
                rows[i].append((i, A[0, 0]))
                rows[i].append((j, A[0, 1]))
                rows[j].append((i, A[1, 0]))
                rows[j].append((j, A[1, 1]))
                lhs = B * dB + dB * B
                rhs = hp * B + H_of(q) * dB
                hcheck = max(hcheck, max(abs(lhs[r, c] - rhs[r, c]) for r in range(2) for c in range(2)))
        germ.append(rows)
    return germ, hcheck


def csr_to_dict(rows):
    """CSR rows (list of (col,val) per row) -> dict{row:{col:val}} accumulating dups."""
    d = {}
    for i, entries in enumerate(rows):
        if not entries:
            continue
        acc = {}
        for c, v in entries:
            acc[c] = acc.get(c, mp.mpf(0)) + v
        d[i] = acc
    return d


def spmatmul(Ad, Bd):
    """Sparse row-dict × row-dict -> row-dict.  (A·B)[i][l] = Σ_k A[i][k] B[k][l]."""
    out = {}
    for i, arow in Ad.items():
        orow = {}
        for k, av in arow.items():
            brow = Bd.get(k)
            if not brow:
                continue
            for l, bv in brow.items():
                orow[l] = orow.get(l, mp.mpf(0)) + av * bv
        if orow:
            out[i] = orow
    return out


def commutator(Ad, Bd):
    """[A,B] = A·B − B·A as row-dict."""
    AB = spmatmul(Ad, Bd)
    BA = spmatmul(Bd, Ad)
    out = {}
    for i in set(AB) | set(BA):
        r = dict(AB.get(i, {}))
        for l, v in BA.get(i, {}).items():
            r[l] = r.get(l, mp.mpf(0)) - v
        r = {l: v for l, v in r.items() if v != 0}
        if r:
            out[i] = r
    return out


def spmatvec(sig_rows, v):
    """CSR rows (list of (col,val)) applied to dense list v -> dense list."""
    n = len(v)
    out = [mp.mpf(0)] * n
    for i, entries in enumerate(sig_rows):
        s = mp.mpf(0)
        for c, val in entries:
            s += val * v[c]
        out[i] = s
    return out


def apply_word_to_e(gens, sig, k, dim):
    """ρ·e_k = σ_{g0}·(σ_{g1}·(…·(σ_{g_{L-1}}·e_k))) as a chain of sparse mat-vecs."""
    v = [mp.mpf(0)] * dim
    v[k] = mp.mpf(1)
    for g in reversed(gens):
        v = spmatvec(sig[g], v)
    return v


# ── correctness gate ─────────────────────────────────────────────────────────


def _dense_from_csr(sig_rows, dim):
    M = mp.zeros(dim, dim)
    for i, entries in enumerate(sig_rows):
        for c, v in entries:
            M[i, c] += v
    return M


def gate_sparse_vs_dense(shapes, verbose=True):
    """Verify sparse σ and germ reproduce the dense builder / dense germ exactly."""
    worst_sig = mp.mpf(0)
    worst_germ = mp.mpf(0)
    for shape in shapes:
        per_gen, dim = block_structure(shape)
        sig = sigma_csr(per_gen, dim, Q0)
        dsig, ddim, _ = build_seminormal_matrices_mp(shape, Q0)
        assert ddim == dim, f"dim mismatch {shape}: {dim} vs {ddim}"
        for g in range(len(dsig)):
            Ms = _dense_from_csr(sig[g], dim)
            d = max(abs(Ms[r, c] - dsig[g][r, c]) for r in range(dim) for c in range(dim))
            worst_sig = max(worst_sig, d)
        # dense reference germ (as the A=2/A=3 probes compute it)
        if dim > 1:
            germ, _ = germ_csr(per_gen, dim, Q0, EPS)
            sig_p, _, _ = build_seminormal_matrices_mp(shape, Q0 + EPS)
            sig_m, _, _ = build_seminormal_matrices_mp(shape, Q0 - EPS)
            for g in range(len(dsig)):
                dref = (sig_p[g] - sig_m[g]) / (2 * EPS)
                Aref = Q0 * dref * mp.inverse(dsig[g])
                Ms = _dense_from_csr(germ[g], dim)
                d = max(abs(Ms[r, c] - Aref[r, c]) for r in range(dim) for c in range(dim))
                worst_germ = max(worst_germ, d)
        if verbose:
            print(f"  gate {str(shape):>18} dim={dim:>3}  Δσ={mp.nstr(worst_sig,3)}  Δgerm={mp.nstr(worst_germ,3)}", flush=True)
    return worst_sig, worst_germ


# ── main pairing computation (sparse, matrix-free) ───────────────────────────


def _aggregate_P(rows):
    """(P_total, P_ctrl) = Σ_λ y_λ·tr(ρΩ₂), Σ_λ y_λ·tr(Ω₂) from row records.

    Each row carries y_λ, tr(ρΩ₂), tr(Ω₂) as fmt-strings, so P is reproducible
    from the checkpoint alone — the aggregation never depends on in-memory mpf
    accumulators that a reclaim would lose."""
    P_total = mp.mpf(0)
    P_ctrl = mp.mpf(0)
    P_wenzl = mp.mpf(0)   # HEADLINE arm (option A); also reproducible from rows
    for r in rows:
        y = mp.mpf(r["y_lambda"])
        P_total += y * mp.mpf(r["tr_rho_Omega2"])
        P_ctrl += y * mp.mpf(r["tr_Omega2_ctrl"])
        P_wenzl += (y_lambda_wenzl_bridge_numeric(tuple(r["lambda"]), Q0,
                                                  dps=mp.mp.dps)
                    * mp.mpf(r["tr_rho_Omega2"]))
    return P_total, P_ctrl, P_wenzl


def _partition_contribution(shape, gens):
    """Per-partition worker: returns (row_dict, y*tr_rO, y*tr_O, tr_rO, hcheck).

    Self-contained (module globals Q0/H/EPS are set at import in every worker),
    so it is safe to dispatch under multiprocessing across the 77 partitions."""
    per_gen, dim = block_structure(shape)
    y = wedderburn_weight(shape, Q0)
    if dim == 1:  # singlet: germs abelian ⇒ Ω₂ = 0
        row = {"lambda": list(shape), "dim": dim, "y_lambda": fmt(y),
               "tr_rho_Omega2": fmt(mp.mpf(0)), "tr_Omega2_ctrl": fmt(mp.mpf(0))}
        return row, mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0), dim, 0
    sig = sigma_csr(per_gen, dim, Q0)
    germ_rows, hcheck = germ_csr(per_gen, dim, Q0, EPS)
    assert hcheck < mp.mpf(10) ** -55, f"germ Hecke check failed {shape}: {mp.nstr(hcheck,3)}"
    A = [csr_to_dict(germ_rows[g]) for g in range(len(germ_rows))]

    # Ω₂ = ½ Σ_{i<j} [A_{g_i}, A_{g_j}] — adjacent generators only
    # (far-commutativity: [A_a,A_b] = 0 for |a-b| >= 2, and a == b commutes).
    #
    # Multiplicities folded BEFORE any matrix is touched. The ⁴He word has 47
    # letters giving 145 adjacent (i<j) pairs over 14 distinct (a,b) keys — but
    # only **10** commutators survive with a nonzero net coefficient once
    # [A_a,A_b] = −[A_b,A_a] is used. The previous loop re-added the same sparse
    # matrix once per pair occurrence: 145 sparse accumulations where 10
    # scalar-times-matrix do. (Same fix as the dense deuteron/triton probes,
    # bean qou-q2q7; verified there bit-identical.)
    L = len(gens)
    net: dict[tuple[int, int], int] = {}
    for i in range(L):
        a = gens[i]
        for j in range(i + 1, L):
            b = gens[j]
            if abs(a - b) != 1:
                continue
            key = (a, b) if a < b else (b, a)
            net[key] = net.get(key, 0) + (1 if a < b else -1)

    Om2 = {}
    for (a, b), n in net.items():
        if not n:
            continue
        C = commutator(A[a], A[b])
        for r, crow in C.items():
            orow = Om2.setdefault(r, {})
            for c, v in crow.items():
                orow[c] = orow.get(c, mp.mpf(0)) + n * v
    for r in Om2:
        for c in Om2[r]:
            Om2[r][c] = Om2[r][c] / 2

    tr_O = mp.mpf(0)
    for r, orow in Om2.items():
        tr_O += orow.get(r, mp.mpf(0))
    tr_rO = mp.mpf(0)
    for k, orow in Om2.items():
        w = apply_word_to_e(gens, sig, k, dim)
        s = mp.mpf(0)
        for c, v in orow.items():
            s += v * w[c]
        tr_rO += s

    row = {"lambda": list(shape), "dim": dim, "y_lambda": fmt(y),
           "tr_rho_Omega2": fmt(tr_rO), "tr_Omega2_ctrl": fmt(tr_O)}
    return row, y * tr_rO, y * tr_O, tr_rO, hcheck, dim, len(Om2)


def _pool_worker(args):
    shape, gens = args
    return _partition_contribution(shape, gens)


def pairing_for_word(gens, n_strands, log_prefix="", a_baseline_sign=None, workers=1,
                     checkpoint=None):
    """Compute P = Σ_λ y_λ tr(ρ_λ Ω₂_λ) over λ ⊢ n_strands, matrix-free.

    workers>1 dispatches the independent partitions across a process pool
    (biggest-first so the long-pole partition starts immediately).

    checkpoint: path to a JSONL file. Each completed partition's row (which
    carries y_λ, tr(ρΩ₂) and the control as fmt-strings — everything needed to
    re-aggregate) is appended and flushed as it lands, and on start any rows
    already present are loaded and their partitions skipped. This makes the run
    resumable across container reclaims: re-invoking the same command banks the
    partitions already done and only recomputes the ones still missing."""
    parts = list(partitions(n_strands))
    # smallest-first: with per-partition checkpointing, this banks dozens of cheap
    # partitions within minutes so a container reclaim loses at most the few large
    # partitions in flight, not the whole run (the prior biggest-first run died
    # with 0 banked). Trades a little makespan for reclaim-resilience.
    parts_sorted = sorted(parts, key=_dim_estimate)
    rows_by_shape = {}
    worst_hcheck = mp.mpf(0)
    t0 = time.time()

    # resume from checkpoint
    ckpt_fh = None
    if checkpoint:
        if os.path.exists(checkpoint):
            with open(checkpoint) as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    rec = json.loads(line)
                    rows_by_shape[tuple(rec["lambda"])] = rec
            print(f"{log_prefix}  resumed: {len(rows_by_shape)}/{len(parts)} partitions "
                  f"already in {os.path.basename(checkpoint)}", flush=True)
        ckpt_fh = open(checkpoint, "a")

    todo = [s for s in parts_sorted if tuple(s) not in rows_by_shape]
    done = len(rows_by_shape)

    def _record(res):
        nonlocal worst_hcheck, done
        row, dP, dC, tr_rO, hcheck, dim, nnz = res
        rows_by_shape[tuple(row["lambda"])] = row
        worst_hcheck = max(worst_hcheck, hcheck)
        done += 1
        if ckpt_fh is not None:
            ckpt_fh.write(json.dumps(row) + "\n")
            ckpt_fh.flush()
            os.fsync(ckpt_fh.fileno())
        el = time.time() - t0
        Prun = _aggregate_P(rows_by_shape.values())[0]
        print(f"{log_prefix}  [{done:>2}/{len(parts)}] {str(tuple(row['lambda'])):>28} dim={dim:>5} "
              f"nnzΩ2rows={nnz:>5}  tr(ρΩ2)={mp.nstr(tr_rO,6):>14}  "
              f"[P={mp.nstr(Prun,6)}]  {el:7.1f}s", flush=True)

    if todo:
        if workers > 1:
            import multiprocessing as _mp
            with _mp.Pool(workers) as pool:
                for res in pool.imap_unordered(_pool_worker, [(s, gens) for s in todo]):
                    _record(res)
        else:
            for shape in todo:
                _record(_partition_contribution(shape, gens))
    if ckpt_fh is not None:
        ckpt_fh.close()

    rows = [rows_by_shape[tuple(s)] for s in parts]  # canonical partition order
    P_total, P_ctrl, P_wenzl = _aggregate_P(rows)
    ctrl_ok = abs(P_ctrl) < _EXACT
    P_sign = 0 if abs(P_total) < _EXACT else (1 if P_total > 0 else -1)
    npos = sum(1 for r in rows if mp.mpf(r["tr_rho_Omega2"]) > _EXACT)
    nneg = sum(1 for r in rows if mp.mpf(r["tr_rho_Omega2"]) < -_EXACT)
    return {
        "rows": rows, "P_total": P_total, "P_ctrl": P_ctrl, "ctrl_ok": ctrl_ok,
        "P_wenzl": P_wenzl,
        "P_sign": P_sign, "npos": npos, "nneg": nneg,
        "worst_hcheck": worst_hcheck,
    }


def run_gate():
    print("[gate 1] sparse σ / germ vs dense builder on small λ ⊢ 4..7 …", flush=True)
    small = []
    for nn in (4, 5, 6, 7):
        small += list(partitions(nn))
    ws, wg = gate_sparse_vs_dense(small)
    assert ws < mp.mpf(10) ** -60, f"sparse σ mismatch {mp.nstr(ws,3)}"
    assert wg < mp.mpf(10) ** -55, f"sparse germ mismatch {mp.nstr(wg,3)}"
    print(f"[gate 1] PASS  Δσ={mp.nstr(ws,3)}  Δgerm={mp.nstr(wg,3)}", flush=True)

    print("[gate 2] reproduce COMMITTED triton H₉ P_total with the sparse method …", flush=True)
    from mass_at_3A_proper import atom_braid_word_3A
    tri = [int(t[2]) for t in atom_braid_word_3A(1, 2)]
    res = pairing_for_word(tri, 9, log_prefix="[gate2]")
    a3_path = os.path.join(os.path.dirname(__file__), "triton-magnus-omega2-sign.witness.json")
    with open(a3_path) as fh:
        committed = json.load(fh)["results"]
    dense_P = mp.mpf(committed["P_total"])
    reldiff = abs(res["P_total"] - dense_P) / abs(dense_P)
    print(f"[gate2] sparse P_total = {mp.nstr(res['P_total'],12)}", flush=True)
    print(f"[gate2] dense  P_total = {mp.nstr(dense_P,12)}  (committed witness)", flush=True)
    print(f"[gate2] rel diff = {mp.nstr(reldiff,3)}   sign sparse={res['P_sign']:+d} "
          f"committed={int(committed['P_total_sign']):+d}", flush=True)
    assert res["P_sign"] == int(committed["P_total_sign"]), "GATE FAIL: sign disagrees with triton"
    assert reldiff < mp.mpf(10) ** -30, f"GATE FAIL: P_total disagrees with triton ({mp.nstr(reldiff,3)})"
    assert res["ctrl_ok"], "GATE FAIL: control tr(Ω₂) did not vanish on triton"
    print("[gate2] PASS — sparse method reproduces the committed triton datum to <1e-30.", flush=True)
    return True


def run_he4(workers=1, checkpoint=None):
    from mass_at_3A_proper import atom_braid_word_3A
    triples = atom_braid_word_3A(2, 2)
    gens = [int(t[2]) for t in triples]
    mult = {g: gens.count(g) for g in sorted(set(gens))}

    # A=2, A=3 baselines for the sign-vs-A map
    def _sign(path):
        try:
            with open(os.path.join(os.path.dirname(__file__), path)) as fh:
                return int(json.load(fh)["results"]["P_total_sign"])
        except Exception:
            return None
    a2_sign = _sign("deuteron-magnus-omega2-sign.witness.json")
    a3_sign = _sign("triton-magnus-omega2-sign.witness.json")

    print(f"[he4] word: {mult}  ({len(gens)} crossings, 12 strands, H₁₂; 77 partitions; "
          f"{workers} worker(s))", flush=True)
    if checkpoint is None:
        checkpoint = os.path.join(os.path.dirname(__file__), "he4-magnus-omega2-sign.checkpoint.jsonl")
    res = pairing_for_word(gens, 12, log_prefix="[he4]", a_baseline_sign=a3_sign,
                           workers=workers, checkpoint=checkpoint)
    P_total, P_ctrl = res["P_total"], res["P_ctrl"]
    P_wenzl = res["P_wenzl"]
    P_sign, npos, nneg = res["P_sign"], res["npos"], res["nneg"]
    ctrl_ok = res["ctrl_ok"]
    sign_indefinite = npos > 0 and nneg > 0

    flip_vs_a3 = None
    if a3_sign is not None and P_sign != 0 and a3_sign != 0:
        flip_vs_a3 = (P_sign != a3_sign)

    run_desc = {(-1): "negative", 0: "zero", 1: "positive"}
    pat = f"A2={a2_sign:+d} A3={a3_sign:+d} A4={P_sign:+d}" if (a2_sign is not None and a3_sign is not None) else f"A4={P_sign:+d}"

    if not ctrl_ok:
        verdict = ("INVALID — control tr_M(Ω₂) did not vanish at A=4; germ or trace broken. "
                   "Do not read the sign.")
    elif P_sign == 0:
        verdict = ("DECOUPLED — the Magnus pairing vanishes against the ⁴He density at A=4.")
    elif flip_vs_a3 is True:
        verdict = (
            f"SIGN MOVES AT A=4 — P(A=4) is {run_desc[P_sign].upper()} while A=2 and A=3 were "
            f"both negative ({pat}). The 2nd-order Magnus pairing, negative through the deuteron "
            f"and triton, reverses at the alpha particle. Control tr_M(Ω₂)=0 holds; per-partition "
            f"sign-indefinite ({npos}+/{nneg}-). scope-(a): dimensionless SIGN datum only — NOT a "
            f"MeV (open Δ_λ gate), NOT a physical binding-sign assertion (qou-v7ro/#6077, cited). "
            f"Whether a move precisely at the doubly-magic A=4 is meaningful needs the sign "
            f"convention; the datum itself is the fact that the sign is not constant in A.")
    elif flip_vs_a3 is False:
        verdict = (
            f"NO MOVE — P(A=4) has the SAME sign as A=2 and A=3 (all {run_desc[P_sign]}; {pat}). "
            f"The 2nd-order Magnus pairing is sign-STABLE across the deuteron, triton and alpha "
            f"particle: A=2,3,4 all {run_desc[P_sign]}. This strengthens the A=3 finding — the "
            f"'flips positive at A≥3' reading fails not just at the triton but at ⁴He too — and "
            f"makes a constant-sign Magnus carrier the working hypothesis through the light nuclei. "
            f"Control tr_M(Ω₂)=0 holds; per-partition sign-indefinite ({npos}+/{nneg}-). scope-(a): "
            f"dimensionless SIGN datum; NOT a MeV (open Δ_λ gate), NOT a physical binding-sign "
            f"convention (qou-v7ro/#6077, cited not re-derived).")
    else:
        verdict = (f"A=4 sign measured (P {'>' if P_sign>0 else '<'} 0) but an A≤3 baseline "
                   f"was unreadable, so no full sign-vs-A comparison. scope-(a).")

    witness = {
        "computation": "he4-magnus-omega2-sign",
        "scriptFile": "he4_magnus_omega2_sign_sparse_probe.py",
        "computedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "engine": (f"mpmath mpf at {mp.mp.dps} dps; SPARSE block-diagonal seminormal (H₁₂, 77 "
                   f"partitions); matrix-free tr(ρ·Ω₂); finite-diff germ; 0 free params"),
        "free_parameters": 0,
        "method": {
            "route": "sparse / matrix-free (owner directive 2026-08-30)",
            "why": ("dense H₁₂ allocates mp.zeros(7700,7700)~9GB per generator and OOM-crashes; "
                    "Σdim³ rises 35,300× from H₉. Block-diagonal generators + germ, "
                    "far-commutativity (adjacent [A_a,A_b] only), matrix-free trace via sparse "
                    "mat-vec chains make it O(dim²·L) time, O(dim) memory."),
            "correctness_gate": ("sparse σ and germ reproduce the dense builder to <1e-60/<1e-55 on "
                                 "λ⊢4..7; sparse method reproduces the COMMITTED triton H₉ P_total "
                                 "to <1e-30; germ passes the differentiated-Hecke identity per block "
                                 f"(worst residual {mp.nstr(res['worst_hcheck'],3)})."),
        },
        "inputs": {
            "q0": _Q0_RESOLVED, "q0_pin": "proton (experimental pin, resolved)", "h": fmt(H),
            "eps_finite_difference": fmt(EPS),
            "he4_word_source": "mass_at_3A_proper.atom_braid_word_3A(2,2) — source of truth (qou-oppb)",
            "he4_word_gens": gens,
            "he4_word_multiplicities": {str(k): v for k, v in mult.items()},
            "n_strands": 12, "n_crossings": len(gens),
            "germ": "A_g = q·(∂_q σ_g)·σ_g⁻¹ (central finite diff, per 2×2 block; validated vs differentiated Hecke)",
            "Omega2": "½ Σ_{i<j} [A_{g_i},A_{g_j}] over ordered crossings, adjacent generators only (far-commutativity)",
            "density": "ρ(β_He4) = ∏ σ_{g_i} (bare word; applied matrix-free, never materialized)",
            "pairing": "P = Σ_λ y_λ tr(ρ_λ Ω₂_λ), y_λ = d_q(λ)²/[n]_q!, λ ⊢ 12",
        },
        "results": {
            "per_partition": res["rows"],
            # Declares WHICH partition-weight family the `y_lambda` column
            # above actually holds (bean qou-za3q). The column name is left
            # alone deliberately — several sibling probes read `r["y_lambda"]`
            # from this witness, so renaming the field would break them; an
            # explicit declaration removes the ambiguity without that.
            "weight_family": "quantum_plancherel_dq2_over_n_factorial",
            "weight_family_note": (
                "NOT the Wenzl y_lambda used by the production Markov trace. "
                "AGENTS.md forbids conflating y_lambda / w_lambda / w~_lambda, "
                "which are distinct at q != 1. Re-weighting this witness's own "
                "per-partition tr(rho.Omega2) with the Wenzl bridge weight "
                "leaves the sign of P_total unchanged — measured in "
                "magnus_omega2_weight_family_robustness_probe.py."
            ),
            # HEADLINE (Option A, bean qou-q2q7). `P_total` keeps its existing
            # name and Plancherel meaning deliberately: gate 2 above does a
            # NUMERICAL dense-vs-sparse check against the committed `P_total`,
            # and he4_magnus_mpfr_probe.py reads it too, so silently re-meaning
            # it would break a real cross-check.
            "headline_pairing": "P_total_wenzl",
            "P_total_wenzl": fmt(P_wenzl),
            "P_total_wenzl_sign": (0 if abs(P_wenzl) < _EXACT
                                   else (1 if P_wenzl > 0 else -1)),
            "P_total": fmt(P_total),
            "P_total_sign": P_sign,
            "P_control_rho_identity": fmt(P_ctrl),
            "control_tr_M_Omega2_vanishes": bool(ctrl_ok),
            "n_partitions_positive": npos,
            "n_partitions_negative": nneg,
            "sign_indefinite_across_partitions": bool(sign_indefinite),
            "A2_P_total_sign": a2_sign,
            "A3_P_total_sign": a3_sign,
            "sign_flip_vs_A3": flip_vs_a3,
            "sign_vs_A": {"A2": a2_sign, "A3": a3_sign, "A4": P_sign},
            "germ_hecke_check_worst_residual": fmt(res["worst_hcheck"]),
        },
        "verdict": verdict,
        "scope": (
            "scope-(a): decides the A=4 SIGN of tr_M(ρ·Ω₂) and its place in the sign-vs-A map "
            "(A=2,3,4). Dimensionless structural datum. Does NOT reproduce any MeV (open Δ_λ gate — "
            "a number would be a fit). Does NOT assert a physical binding-sign convention "
            "(qou-v7ro / PR #6077, cited not re-derived). No fit; nothing inverted; nothing wired."
        ),
        "wired": False,
        "notes": ("Sparse/matrix-free route (owner directive 2026-08-30) extending the A=2 deuteron "
                  "(qou-dp32) and A=3 triton (PR #6107) Magnus-sign probes to the alpha particle "
                  "(H₁₂). Same construction; feasible only because block-diagonal generators + "
                  "far-commutativity + matrix-free trace avoid the dense 7700² OOM. ⁴He word "
                  "atom_braid_word_3A(2,2) (qou-oppb). Cites qou-v7ro/#6077 for the sign convention."),
    }

    from qou_substrate.witness import WitnessBuilder as _WB
    _WB.stamp_staleness_metadata(witness, script_path=__file__, engine=None, q0_anchor=None)
    out = os.path.join(os.path.dirname(__file__), "he4-magnus-omega2-sign.witness.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(witness, fh, indent=1)
        fh.write("\n")

    print(f"\nq0={mp.nstr(Q0,17)}  ⁴He word: {mult}  ({len(gens)} crossings, 12 strands, H₁₂)")
    print(f"P_control (ρ=I, must be 0) = {mp.nstr(P_ctrl,6)} -> vanishes: {ctrl_ok}")
    print(f"P_total(A=4) = {mp.nstr(P_total,8)}   sign = {P_sign:+d}   (per-partition {npos}+ / {nneg}-)")
    print(f"sign-vs-A:  {pat}   ->  flip vs A=3 = {flip_vs_a3}")
    print(f"\n[verdict] {verdict}")
    print(f"wrote {out}")
    assert ctrl_ok, "control tr_M(Ω₂) must vanish by cyclicity"
    print("CONTROL ASSERTION PASSES")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate", action="store_true", help="run the correctness gate only")
    ap.add_argument("--full", action="store_true", help="run gate then the full H₁₂ ⁴He")
    ap.add_argument("--workers", type=int, default=1, help="process-pool size for the H₁₂ partitions")
    ap.add_argument("--skip-gate", action="store_true", help="skip the gate (gate already passed)")
    ap.add_argument("--checkpoint", default=None,
                    help="JSONL checkpoint path (resumable across reclaims; default alongside the witness)")
    args = ap.parse_args()
    if args.gate:
        run_gate()
        return
    # default and --full: gate first (unless already verified), then He4
    if not args.skip_gate:
        run_gate()
    run_he4(workers=args.workers, checkpoint=args.checkpoint)


if __name__ == "__main__":
    main()
