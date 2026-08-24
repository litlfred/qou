#!/usr/bin/env python3
"""A=5 (⁵He) end-to-end combiner cross-check via the contraction-only diagonal.

Extends the A=4 ⁴He cross-check (`a_operator_recursive_he4_crosscheck.py`,
#2405) to A=5 using the diagonal-only / contraction-only `ρ_ξ` (#2449 / #2456):
only `diag(ρ_ξ(W_inner))` is needed (A^λ_{ξν} block-diagonal in V_ξ), and at A=5
the inner factor is ξ⊢12 (`d_ξ ≤ 7700`) — too large for the 50-dps dense build
(~8 h) but feasible in **float64** (~minutes), the realistic A=5 backend per the
cost wall (`docs/audits/2026-06-17-aoperator-a6-cost-wall-contraction-only.md`).

## The combiner bottleneck and the fix (this file, 2026-06-18)

The naive A=5 combiner re-builds the production `interface_blocks` (mpmath A^λ_{ξν}
matrices, an `O(d_ξ)` mpmath loop) **once per λ — all 176 partitions of 15** — and
ran > 2.75 h without finishing (the cost-wall doc's "float64 ~5 min" covered only
the ρ_ξ *diagonal* builds, not the combiner contraction). `combiner_chi_fast`
below is an **exact regrouping** of that contraction (partial trace reordered) —
identical arithmetic, never materialising A, with the `d_ξ` loop in float64:

    χ^λ = Σ_{(ξ,ν)} Σ_a dg[a]·( Σ_w bridge(cfirst[w] − c_a[a])·G[w] + d_coef·ΣG ),
    G[w] = Σ_{b,b'} rb[b',b] Σ_kk Cinv[j1,w]·C[w,j2]   (a-independent).

`G[w]` comes from the tiny `nW×nW` block-to-standard alignment (mpmath, cheap);
the only `O(d_ξ)` work is then a float64 sum with `bridge(·)` cached by integer δ.

Validation ladder:
  (A4-a) `combiner_chi_fast` vs the EXACT `young_seminormal.chi_young` on the real
         ⁴He word (small-d λ⊢12) — confirms the fast regrouping itself.
  (A4-b) `combiner_chi_fast` vs the ORIGINAL `combiner_chi_float` (mpmath A) on
         the same λ — confirms the regrouping is identical to the production form.
  (A5)   `combiner_chi_fast` vs the canonical fine-Bratteli transfer
         (`reduced_block_kernel.chi_all_lambda_reduced_block`) on the real ⁵He
         word, per-λ and assembled `tr_M = Σ_λ y_λ χ^λ`.

Coarse by design (float64 ≈ 1e-8 after the long word product); the point is that
the combiner KERNEL reproduces the production transfer at A=5. No production value
changes (tr_M already validated by the transfer); no fit, nothing rewired.

`diag(ρ_ξ)` and the per-λ `χ^λ` are checkpointed to `/tmp` so a container reclaim
re-runs only the unfinished work.

Run: `python3 -u aoperator_a5_crosscheck.py 2>&1 | tee /tmp/a5.log`  (minutes).
"""
from __future__ import annotations

import datetime
import json
import pickle
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np
import scipy
import scipy.sparse as sp

HERE = Path(__file__).resolve().parents[1]               # computations/
AOP = HERE / "a_operator"
for p in (str(HERE), str(AOP), str(HERE / "substrate")):
    sys.path.insert(0, p)

import a_operator_categorical as aoa            # noqa: E402
import a_operator_recursive as rec              # noqa: E402
import rho_xi_diagonal as rxd                   # noqa: E402
from young_seminormal import chi_young, seminormal_sigma, standard_tableaux  # noqa: E402
from lr_coefficients import partitions_of       # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from reduced_block_kernel import chi_all_lambda_reduced_block  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q0                 # noqa: E402

DPS = 50
mp.mp.dps = 60
BATCH = 256
DIAG_CACHE = Path("/tmp/a5_diags_n12.pkl")
CHI_CKPT = Path("/tmp/a5_chi_comb.json")


def _shim(lam, q_str, dps):
    """Pure-Python `exact_seminormal_matrices` (no native wheel) for ν⊢3."""
    qq = mp.mpf(q_str)
    n = sum(lam)
    mats = [seminormal_sigma(tuple(lam), i, qq) for i in range(1, n)]
    return mats, (mats[0].rows if mats else 1)


aoa.exact_seminormal_matrices = _shim            # interface_blocks' ν-alignment


def peel(word, A):
    """Split the 3A word at the last-nucleon bridge (gen 3A−4); n_inner = 3A−3.

    Returns `(W_inner, I_d, block, n_inner)` with `block` shifted to 0-based
    H_3 generators, matching the A=4 cross-check convention generalised."""
    n_inner = 3 * A - 3
    bridge = 3 * A - 4
    idx = next(i for i, (c, d, g) in enumerate(word) if g == bridge)
    W_inner = word[:idx]
    I_d = word[idx][1]
    block = [(c, d, g - n_inner) for (c, d, g) in word[idx + 1:]]
    return W_inner, I_d, block, n_inner


def diag_rho_float(xi, q_str, word, batch=BATCH):
    """`diag(ρ_ξ(word))` in float64, batched sparse mat-vec. `O(d·batch)` memory."""
    nz, d = rxd.sparse_generators(xi, q_str, DPS)
    gens = []
    for e in nz:
        if e:
            rows = [i for (i, _, _) in e]
            cols = [j for (_, j, _) in e]
            vals = [float(v) for (_, _, v) in e]
            gens.append(sp.csr_matrix((vals, (rows, cols)), shape=(d, d)))
        else:
            gens.append(sp.csr_matrix((d, d)))
    rev = [(float(c), float(dc), g) for (c, dc, g) in reversed(word)]
    diag = np.zeros(d)
    for a0 in range(0, d, batch):
        cols = list(range(a0, min(a0 + batch, d)))
        V = np.zeros((d, len(cols)))
        for k, a in enumerate(cols):
            V[a, k] = 1.0
        for (c, dc, g) in rev:
            V = c * (gens[g] @ V) + dc * V
        for k, a in enumerate(cols):
            diag[a] = V[a, k]
    return diag, d


def all_diags(parts, q_str, W_inner, label):
    """All `diag(ρ_ξ(W_inner))` (float64), checkpointed to `/tmp` per container."""
    key = (len(W_inner), q_str[:14])
    if DIAG_CACHE.exists():
        blob = pickle.loads(DIAG_CACHE.read_bytes())
        if blob.get("key") == key:
            print(f"[{label}] diag(ρ_ξ) restored from cache "
                  f"({len(blob['diags'])} ξ)", flush=True)
            return {tuple(k): v for k, v in blob["diags"].items()}
    t0 = time.time()
    diags = {}
    for xi in parts:
        td = time.time()
        diags[xi], d = diag_rho_float(xi, q_str, W_inner)
        if d >= 1000:
            print(f"   ρ_ξ {xi} d={d}: {float(time.time()-td):.1f}s "
                  f"(cum {float(time.time()-t0):.0f}s)", flush=True)
    print(f"[{label}] all ρ_ξ diagonals (float64): {float(time.time()-t0):.0f}s", flush=True)
    DIAG_CACHE.write_bytes(pickle.dumps(
        {"key": key, "diags": {k: v for k, v in diags.items()}}))
    return diags


def rho_full_float(nu, q_str, word):
    """Small full float64 ρ_ν(word) for ν⊢3 (d_ν ≤ 2)."""
    qq = mp.mpf(q_str)
    n = sum(nu)
    mats = [np.array([[float(x) for x in row]
                      for row in seminormal_sigma(tuple(nu), i, qq).tolist()])
            for i in range(1, n)]
    d = mats[0].shape[0] if mats else 1
    M = np.eye(d)
    for (c, dc, g) in word:
        M = float(c) * (M @ mats[g]) + float(dc) * M
    return M


def combiner_chi_float(lam, n_inner, I_d, diags, RB, q_str):
    """χ^λ via the float64 contraction-only combiner (mpmath A, original form).

    Kept as the A4 cross-validation reference for `combiner_chi_fast`."""
    blocks = rec.interface_blocks(lam, n_inner, 3, q_str, mp.mpf(I_d), DPS)
    total = 0.0
    for (xi, nu), info in blocks.items():
        A = info["A"]
        d_mu, d_nu = info["d_mu"], info["d_nu"]
        dg = diags[xi]
        rb = RB[nu]
        for a in range(d_mu):
            da = dg[a]
            if da == 0.0:
                continue
            s = 0.0
            for b in range(d_nu):
                for bp in range(d_nu):
                    s += float(A[a * d_nu + b, a * d_nu + bp]) * rb[bp, b]
            total += da * s
    return total


def combiner_chi_fast(lam, n_inner, I_d, diags, RB, q, qi, q_str, xi_cache):
    """χ^λ via the regrouped contraction-only combiner — exact regrouping of
    `combiner_chi_float`/`interface_blocks` that never materialises A and runs the
    `d_ξ` loop in float64. See module docstring for the identity."""
    n_block = 3
    cont_lam = rec._content_by_index(lam)
    dcf = float(I_d)
    total = 0.0
    for xi in partitions_of(n_inner):
        if len(xi) > len(lam) or any(xi[i] > lam[i] for i in range(len(xi))):
            continue
        skew_tabs = rec.skew_standard_tableaux(lam, xi)
        if not skew_tabs:
            continue
        nW = len(skew_tabs)
        cfirst = [cont_lam[t[1]] for t in skew_tabs]
        # per-ξ a-loop contents (content of ξ's box holding the max value), cached
        # across λ (ξ-only, λ-independent).
        c_a = xi_cache.get(xi)
        if c_a is None:
            xi_tabs = standard_tableaux(xi)
            cont_xi = rec._content_by_index(xi)
            c_a = [cont_xi[t[n_inner]] for t in xi_tabs]
            xi_cache[xi] = c_a
        d_xi = len(c_a)
        dg = diags[xi]
        # block-S_3 action on the skew → standard ρ_ν alignment (tiny nW×nW).
        blockgens_W = rec._block_gens_on_skew(lam, skew_tabs, n_block, q, qi)
        C, layout = rec._align_block_to_standard(blockgens_W, n_block, q_str, DPS)
        if C.cols != nW:
            continue
        Cinv = C ** -1
        Cf = [[float(C[w, j]) for j in range(C.cols)] for w in range(nW)]
        Cinvf = [[float(Cinv[i, j]) for j in range(Cinv.cols)]
                 for i in range(Cinv.rows)]
        nu_cols: dict = {}
        for j, (nu, b) in enumerate(layout):
            nu_cols.setdefault(nu, []).append((j, b))
        # bridge(δ) cache (float), shared across ν for this (λ,ξ).
        br: dict = {}
        for nu, jbs in nu_cols.items():
            d_nu = rec.partition_dim(nu)
            c_lr = len(jbs) // d_nu
            col_of = {(idx // d_nu, b): j for idx, (j, b) in enumerate(jbs)}
            rb = RB[nu]
            # G[w] = Σ_{b,b'} rb[b',b] Σ_kk Cinv[col_of[(kk,b)],w]·C[w,col_of[(kk,b')]]
            G = [0.0] * nW
            for w in range(nW):
                g = 0.0
                for b1 in range(d_nu):
                    for b2 in range(d_nu):
                        coef = float(rb[b2, b1])
                        if coef == 0.0:
                            continue
                        acc = 0.0
                        for kk in range(c_lr):
                            acc += Cinvf[col_of[(kk, b1)]][w] * Cf[w][col_of[(kk, b2)]]
                        g += coef * acc
                G[w] = g
            sumG = sum(G)
            for a in range(d_xi):
                da = dg[a]
                if da == 0.0:
                    continue
                ca = c_a[a]
                s = dcf * sumG
                for w in range(nW):
                    delta = cfirst[w] - ca
                    bv = br.get(delta)
                    if bv is None:
                        bv = float(rec._bridge_diag_coeff(delta, q, qi))
                        br[delta] = bv
                    s += bv * G[w]
                total += da * s
    return total


def main() -> int:
    q = aoa.q0_mp(DPS)
    q_str = mp.nstr(q, DPS)
    qm = mp.mpf(q_str)
    qim = 1 / qm
    print(f"q₀={q_str[:12]}  dps={DPS} (transfer ref) / float64 (combiner)\n", flush=True)
    xi_cache: dict = {}

    # ---- (A4) float64 path self-check on the real ⁴He word --------------------
    w4 = atom_braid_word_3A(2, 2)
    Wi4, Id4, bl4, ni4 = peel(w4, 4)
    print(f"[A4 self-check] n_inner={ni4} |W_inner|={len(Wi4)} "
          f"bridge_d={mp.nstr(Id4, 5)}", flush=True)  # display only; mpf has no %f
    diags4 = {xi: diag_rho_float(xi, q_str, Wi4)[0] for xi in partitions_of(ni4)}
    RB4 = {nu: rho_full_float(nu, q_str, bl4) for nu in partitions_of(3)}
    worst_fy = 0.0   # fast vs exact chi_young
    worst_fo = 0.0   # fast vs original mpmath combiner
    for lam in partitions_of(12):
        if len(standard_tableaux(lam)) > 60:
            continue
        ref = float(chi_young(lam, w4, q))
        fast = combiner_chi_fast(lam, ni4, Id4, diags4, RB4, qm, qim, q_str, xi_cache)
        orig = combiner_chi_float(lam, ni4, Id4, diags4, RB4, q_str)
        worst_fy = max(worst_fy, abs(fast - ref))
        worst_fo = max(worst_fo, abs(fast - orig))
    print(f"[A4-a] max|fast − chi_young|       (small-d λ⊢12) = {float(worst_fy):.2e}"
          f"   {'OK' if worst_fy < 1e-6 else 'FAIL'}", flush=True)
    print(f"[A4-b] max|fast − orig combiner|   (small-d λ⊢12) = {float(worst_fo):.2e}"
          f"   {'OK' if worst_fo < 1e-6 else 'FAIL'}\n", flush=True)
    xi_cache.clear()   # ξ⊢9 cache is useless for the ξ⊢12 A5 run

    # ---- (A5) fast combiner vs the fine-Bratteli transfer on the real ⁵He word
    w5 = atom_braid_word_3A(2, 3)
    Wi5, Id5, bl5, ni5 = peel(w5, 5)
    print(f"[A5] ⁵He n_inner={ni5} |W_inner|={len(Wi5)} bridge_d={float(Id5):.4f}"
          f"  #ξ⊢{ni5}={len(partitions_of(ni5))}", flush=True)
    diags5 = all_diags(partitions_of(ni5), q_str, Wi5, "A5")
    RB5 = {nu: rho_full_float(nu, q_str, bl5) for nu in partitions_of(3)}

    t0 = time.time()
    chi_ref = chi_all_lambda_reduced_block(w5, 15, q=None)
    chi_ref = {tuple(k): float(v) for k, v in chi_ref.items()}
    print(f"[A5] transfer reference (all λ⊢15): {float(time.time()-t0):.0f}s", flush=True)

    # combiner over all λ⊢15, with progress + checkpoint (resume on reclaim).
    chi_comb: dict = {}
    if CHI_CKPT.exists():
        chi_comb = {tuple(eval(k)): v for k, v in json.loads(CHI_CKPT.read_text()).items()}
        print(f"[A5] resumed {len(chi_comb)} λ from checkpoint", flush=True)
    lams = [tuple(l) for l in partitions_of(15)]
    t0 = time.time()
    for i, lam in enumerate(lams):
        if lam in chi_comb:
            continue
        chi_comb[lam] = combiner_chi_fast(lam, ni5, Id5, diags5, RB5, qm, qim, q_str, xi_cache)
        if (i + 1) % 20 == 0 or i == len(lams) - 1:
            done = sum(1 for l in lams if l in chi_comb)
            el = time.time() - t0
            eta = el / done * (len(lams) - done) if done else 0
            print(f"   λ {done}/{len(lams)}  elapsed {float(el):.0f}s  ETA {float(eta):.0f}s", flush=True)
            CHI_CKPT.write_text(json.dumps({str(k): v for k, v in chi_comb.items()}))
    comb_secs = time.time() - t0
    print(f"[A5] combiner all-λ χ (float64): {float(comb_secs):.0f}s", flush=True)

    worst = max(abs(chi_comb[k] - chi_ref[k]) for k in chi_comb)
    denom = max(abs(chi_ref[k]) for k in chi_ref) or 1.0
    argworst = max(chi_comb, key=lambda k: abs(chi_comb[k] - chi_ref[k]))
    y = {tuple(k): float(v) for k, v in y_lambda_at(15, Q0).items()}
    trM_comb = sum(y[k] * chi_comb[k] for k in chi_comb)
    trM_ref = sum(y[k] * chi_ref[k] for k in chi_ref)
    print(f"\n[A5] per-λ max|χ_comb − χ_transfer| (all {len(chi_comb)}) = {float(worst):.2e}"
          f"  at {argworst}  (rel to max|χ| {float(worst/denom):.2e})", flush=True)
    print(f"[A5] tr_M_combiner = {float(trM_comb):.10g}", flush=True)
    print(f"[A5] tr_M_transfer = {float(trM_ref):.10g}", flush=True)
    rel = abs(trM_comb - trM_ref) / (abs(trM_ref) or 1.0)
    print(f"[A5] |Δtr_M|={float(abs(trM_comb-trM_ref)):.2e}  rel={float(rel):.2e}"
          f"   {'OK — combiner reproduces transfer at A=5 (float64)' if rel < 1e-5 else 'CHECK'}",
          flush=True)

    assertions = [
        {"name": "a4_fast_vs_chi_young", "computed": float(worst_fy), "expected": 0.0,
         "passed": bool(worst_fy < 1e-6), "tolerance": 1e-6,
         "source": "A4: float64 regrouped combiner vs exact young_seminormal.chi_young "
                   "(small-d λ⊢12) on the real ⁴He word — validates the fast path."},
        {"name": "a4_fast_vs_orig_combiner", "computed": float(worst_fo), "expected": 0.0,
         "passed": bool(worst_fo < 1e-6), "tolerance": 1e-6,
         "source": "A4: float64 regrouped combiner vs the original mpmath interface_blocks "
                   "combiner — confirms the regrouping is the same arithmetic."},
        {"name": "a5_per_lambda_max_abs_diff", "computed": float(worst), "expected": 0.0,
         "passed": bool(worst / denom < 1e-8), "tolerance": float(denom * 1e-8),
         "source": f"A5 ⁵He: max over all {len(chi_comb)} λ⊢15 of |χ_comb − χ_transfer| "
                   f"(rel to max|χ| = {float(worst/denom):.2e}) at λ={argworst}."},
        {"name": "a5_trM_combiner_vs_transfer", "computed": float(rel), "expected": 0.0,
         "passed": bool(rel < 1e-5), "tolerance": 1e-5,
         "source": f"A5 ⁵He: relative |Δtr_M| between the operator combiner and the "
                   f"fine-Bratteli transfer (tr_M = Σ_λ y_λ χ^λ = {float(trM_ref):.10g})."},
    ]
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(HERE)).decode().strip()
    except Exception:
        sha = "unknown"
    witness = {
        "engine": "numpy/scipy float64 (combiner + diag ρ_ξ); mpmath 50 dps "
                  "(ν-alignment + fine-Bratteli transfer reference)",
        "engineVersion": f"numpy {np.__version__}, scipy {scipy.__version__}, "
                         f"mpmath {mp.__version__}",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": sha,
        "description": "A=5 (⁵He) end-to-end operator-combiner cross-check vs the "
                       "production fine-Bratteli transfer (contraction-only diag ρ_ξ).",
        "q0": q_str,
        "trM_combiner": float(trM_comb),
        "trM_transfer": float(trM_ref),
        "n_lambda": int(len(chi_comb)),
        "combiner_seconds": float(comb_secs),
        "assertions": assertions,
        "allPassed": bool(all(a["passed"] for a in assertions)),
        "auditOnly": True,
    }
    wpath = Path(__file__).with_suffix("").as_posix() + ".witness.json"
    Path(wpath).write_text(json.dumps(witness, indent=2))
    print(f"[A5] witness → {wpath}  allPassed={witness['allPassed']}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
