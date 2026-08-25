#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""rho_w_crystal_vertex_trace.py — the GENUINE per-crystal-vertex trace ρ_w.

Implements, from first principles, the Kashiwara crystal-vertex trace that the
2026-05-25 Option-E audit listed as ``(NOT EXIST)`` and the 2026-05-31 Option-E
refresh confirmed v6–v9 never built (they computed a *global* χ-sum + a
back-solved scalar ``C_knot = 5.852``, not the per-vertex object).

Design note (written BEFORE this compute):
``docs/audits/2026-05-31-rho-w-crystal-vertex-trace-design.md``.

Definition (parameter-free — NO scalar, NO scale menu, NO multiplicity choice):

    Crystal vertices (type A):   B(λ) ≅ SYT(λ),   |B(λ)| = f^λ = dim V_λ.
    Per-vertex weight:           ρ_w(K) := ⟨ v_T | ρ_λ(β_K) | v_T ⟩,  w = T ∈ SYT(λ),
                                 where ρ_λ is the Hoefsmit/Young seminormal
                                 (orthogonal) representation of H_n(q), built here
                                 in closed form from axial (content) distances.
    Crystal-summed Δ_λ:          Δ_λ^{ρ_w}(K) = Σ_w n^w_λ ρ_w(K),  n^w_λ = 1
                                 (regular multiplicity; the diagonal counts each
                                 crystal vertex exactly once).

Forced identity (a trace is the sum of its diagonal):

    Δ_λ^{ρ_w}(K) = Σ_{T∈SYT(λ)} ⟨v_T|ρ_λ(β_K)|v_T⟩ = tr ρ_λ(β_K) = χ^λ(β_K).

So the genuine crystal-vertex trace, summed over the crystal, IS the Hecke
character already on disk — NO new degree of freedom. This script (a) builds
ρ_w genuinely per SYT vertex, (b) verifies Σ_w ρ_w = χ^λ against the cached
``chi-deuteron-h6-at-q0-50dps.witness.json`` (a real cross-check, not a
restatement), and (c) reports the honest, parameter-free deuteron Δ_λ residual.

closure_status: does_not_close.  NO C_knot, NO back-solve, NO content prop.

Substrate braid word β_D from ``atom_canonical_crossings(1,1)`` — the IDENTICAL
canonical deuteron word the χ-cache was built from (sigma / sigma_inv / averaged
= interface σ_g − h/2·1).

@module computations/rho_w_crystal_vertex_trace
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from itertools import product
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

# Centralised precision (COMPUTE 65 dps / SERIALIZE 50 dps defaults).
from _precision import set_compute_dps, fmt  # noqa: E402

from canonical_braid_crossings import (  # noqa: E402
    atom_canonical_crossings, d_for_ctype,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


# ----------------------------------------------------------------------------
# Substrate constants.
# ----------------------------------------------------------------------------
# Q0_STR used to be a hardcoded literal here, commented "from the deuteron χ
# cache header". It did not match that header: the literal was the MUON pin
# (1.10997859555733471…) while the cache declares q0Anchor "proton" and
# q0Value 1.10997858275138080…. Since `q` is hardcoded it also bypassed both
# the q0_anchor_manifest and QOU_Q0_ANCHOR, so neither could correct it.
#
# That one-line mismatch WAS the whole 8.9e-7 "Δ_λ cross-check residual" this
# script reports. The identity Σ_w ρ_w = χ^λ is exact — verified to 1e-49 when
# both sides use the same q — so the residual was measuring the μ–p anchor
# separation and nothing else. Kept as a named fallback only; `main` now takes
# q FROM the cache header, which makes the comment true by construction and
# means the cross-check can never again be run at two different anchors.
Q0_STR_FALLBACK = "1.1099785827513808075916690956107688798744991218736"
# CODATA electron mass (MeV); matches docs/audits gating residual −4.353.
M_E_MEV_STR = "0.51099895069"
# B_D AME (MeV) — used ONLY to report the honest residual, never to fit.
B_D_AME_MEV_STR = "2.224566"


# ----------------------------------------------------------------------------
# Standard Young tableaux (the crystal vertices B(λ) = SYT(λ)).
# ----------------------------------------------------------------------------
def partitions_of(n: int) -> list[tuple[int, ...]]:
    """All partitions of n (weakly decreasing tuples), descending order."""
    out: list[tuple[int, ...]] = []

    def rec(rem: int, maxp: int, acc: list[int]) -> None:
        if rem == 0:
            out.append(tuple(acc))
            return
        for p in range(min(rem, maxp), 0, -1):
            rec(rem - p, p, acc + [p])

    rec(n, n, [])
    return out


def cells_of(lam: tuple[int, ...]) -> list[tuple[int, int]]:
    """Young-diagram cells (row, col), 0-indexed."""
    return [(r, c) for r, row in enumerate(lam) for c in range(row)]


def standard_young_tableaux(lam: tuple[int, ...]) -> list[dict[int, tuple[int, int]]]:
    """Enumerate SYT(λ) as maps {entry 1..n -> cell (row,col)}.

    These maps ARE the crystal vertices w ∈ B(λ). The entry k sits in cell
    T^{-1}(k); content(k) = col − row gives the axial coordinate used by the
    seminormal representation.
    """
    cells = cells_of(lam)
    n = len(cells)
    cellset = set(cells)
    results: list[dict[int, tuple[int, int]]] = []

    # Place entries 1..n so that each is the lower-right-most so far
    # (standard = increasing along rows and columns).
    def rec(k: int, placed: dict[tuple[int, int], int]) -> None:
        if k > n:
            inv = {v: cell for cell, v in placed.items()}
            results.append(inv)
            return
        for (r, c) in cells:
            if (r, c) in placed:
                continue
            # left neighbour must be filled (or be column 0)
            if c > 0 and (r, c - 1) not in placed:
                continue
            # upper neighbour must be filled (or be row 0)
            if r > 0 and (r - 1, c) not in placed:
                continue
            placed[(r, c)] = k
            rec(k + 1, placed)
            del placed[(r, c)]

    rec(1, {})
    return results


def content_vector(T: dict[int, tuple[int, int]], n: int) -> list[int]:
    """content[k] = col − row of the cell holding entry k+1 (0-indexed k)."""
    return [T[k + 1][1] - T[k + 1][0] for k in range(n)]


def swap_tableau(T: dict[int, tuple[int, int]], i: int) -> dict[int, tuple[int, int]] | None:
    """Apply s_i (swap entries i, i+1). Returns the new SYT, or None if the
    swap is not standard (i, i+1 adjacent in a row or column)."""
    ci, ci1 = T[i], T[i + 1]
    (ri, coli), (ri1, coli1) = ci, ci1
    # adjacent in same row or same column => swap stays non-standard => no swap
    if ri == ri1 or coli == coli1:
        return None
    new = dict(T)
    new[i], new[i + 1] = ci1, ci
    return new


# ----------------------------------------------------------------------------
# Hoefsmit / Young seminormal representation of H_n(q) — closed form.
# ----------------------------------------------------------------------------
# Convention (matches AGENTS.md §7a Hecke relation (σ−q)(σ+q⁻¹)=0):
#   For a SYT basis {v_T}, generator σ_i acts:
#     • i, i+1 same row     →  σ_i v_T = q · v_T
#     • i, i+1 same column  →  σ_i v_T = −q⁻¹ · v_T
#     • else (s_i·T standard): 2×2 block on {v_T, v_{s_i T}} with axial
#       distance d = content(i+1) − content(i):
#           σ_i v_T = (1/[d]_q?) ... — we use the standard seminormal form
#         in the variable r = q^{d} as below.
# We build the matrix of σ_i in the SYT basis explicitly (dense, exact mpf).
def seminormal_generator_matrix(
    lam: tuple[int, ...],
    syts: list[dict[int, tuple[int, int]]],
    syt_index: dict[tuple, int],
    i: int,
    q: mpf,
    qi: mpf,
) -> list[list[mpf]]:
    """Dense matrix of σ_i (generator i, 1-indexed: swaps strands i,i+1)
    in the SYT basis, via the canonical Hoefsmit seminormal (orthogonal) form.

    Convention identical to ``tools/hecke-engine/src/seminormal.rs``
    (``seminormal_block_generators``), so Σ_w ρ_w = tr ρ_λ(β) reproduces the
    cached χ^λ to full precision (a genuine cross-check, not a restatement):

      h = q − q⁻¹ ;  ρ = content(i+1) − content(i)  (axial distance).
      Diagonal value on v_T:   a  = h / (1 − q^{−2ρ}).
      If s_i·T is standard (2×2 block with partner T' = s_i·T):
          a' = h / (1 − q^{2ρ})  (partner diagonal),
          b  = √|a·a' + 1|        (symmetric off-diagonal).
      If s_i·T is non-standard (i,i+1 in same row → ρ=−1 → a=q;
          same column → ρ=+1 → a=−q⁻¹): 1×1 block, diagonal a only.

    This is exactly content-determined — NO free parameter.
    """
    from mpmath import sqrt as _sqrt
    dim = len(syts)
    M = [[mpf(0) for _ in range(dim)] for _ in range(dim)]
    h = q - qi
    processed = [False] * dim

    def content(rc: tuple[int, int]) -> int:
        return rc[1] - rc[0]

    for idx, T in enumerate(syts):
        if processed[idx]:
            continue
        ci, ci1 = T[i], T[i + 1]            # cells of entries i, i+1
        rho = content(ci1) - content(ci)    # axial distance (int)
        a = h / (mpf(1) - q ** (-2 * rho))
        Tp = swap_tableau(T, i)
        if Tp is None:
            # 1×1 block — same row (a = q) or same column (a = −q⁻¹).
            M[idx][idx] = a
            processed[idx] = True
            continue
        jdx = syt_index[tuple(sorted(Tp.items()))]
        a_prime = h / (mpf(1) - q ** (2 * rho))
        b = _sqrt(abs(a * a_prime + mpf(1)))
        M[idx][idx] = a
        M[jdx][jdx] = a_prime
        M[idx][jdx] = b
        M[jdx][idx] = b
        processed[idx] = True
        processed[jdx] = True
    return M


def mat_mul(A, B):
    n = len(A)
    m = len(B[0])
    k = len(B)
    C = [[mpf(0)] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Ci = C[i]
        for t in range(k):
            a = Ai[t]
            if a == 0:
                continue
            Bt = B[t]
            for j in range(m):
                Ci[j] += a * Bt[j]
    return C


def identity(n):
    return [[mpf(1) if i == j else mpf(0) for j in range(n)] for i in range(n)]


def generator_word_matrices(lam, syts, syt_index, q, qi):
    """Pre-build σ_g, σ_g⁻¹, and BOTH interfaces for each generator
    g = 1..n−1, in the SYT basis. h = q − q⁻¹ (substrate).

    Two interfaces, not one: the colour-blind `averaged` (σ_g − (h/2)·1) and
    the colour-weighted `averaged_weighted` (σ_g − h(1/2 − δ/4)·1) that the
    canonical word carries on the p-n bond. Building only the first is what
    made this module raise on every Z≥1,N≥1 atom.
    """
    n = sum(lam)
    h = q - qi
    sig: dict[int, list] = {}
    sig_inv: dict[int, list] = {}
    inter: dict[int, list] = {}
    inter_w: dict[int, list] = {}
    d_w = d_for_ctype("averaged_weighted", h)
    for g in range(1, n):
        S = seminormal_generator_matrix(lam, syts, syt_index, g, q, qi)
        sig[g] = S
        # σ⁻¹ = σ − h·1   (from σ − σ⁻¹ = h, the Skein relation)
        Sinv = [[S[i][j] - (h if i == j else mpf(0)) for j in range(len(S))]
                for i in range(len(S))]
        sig_inv[g] = Sinv
        # interface operator I_g = σ_g − (h/2)·1  ("averaged" crossing)
        Ig = [[S[i][j] - (h / 2 if i == j else mpf(0)) for j in range(len(S))]
              for i in range(len(S))]
        inter[g] = Ig
        # colour-weighted interface I^w_g = σ_g + d_w·1, d_w = −h(1/2 − δ/4).
        # `d_for_ctype` returns the signed shift, so this ADDS it — matching
        # `Ig` above, which subtracts the positive h/2.
        inter_w[g] = [[S[i][j] + (d_w if i == j else mpf(0))
                       for j in range(len(S))] for i in range(len(S))]
    return sig, sig_inv, inter, inter_w


def rho_lambda_of_word(lam, word, q, qi):
    """Build the full matrix ρ_λ(β) for braid word `word` = list of
    (gen_idx_0based, ctype), and return (matrix, syts, syt_index)."""
    n = sum(lam)
    syts = standard_young_tableaux(lam)
    syt_index = {tuple(sorted(T.items())): i for i, T in enumerate(syts)}
    dim = len(syts)
    sig, sig_inv, inter, inter_w = generator_word_matrices(
        lam, syts, syt_index, q, qi)
    M = identity(dim)
    for (g0, ctype) in word:
        g = g0 + 1  # 1-indexed generator
        if ctype == "sigma":
            G = sig[g]
        elif ctype == "sigma_inv":
            G = sig_inv[g]
        elif ctype == "averaged":
            G = inter[g]
        elif ctype == "averaged_weighted":
            G = inter_w[g]
        else:
            raise ValueError(f"unknown ctype {ctype!r}")
        M = mat_mul(M, G)
    return M, syts


# ----------------------------------------------------------------------------
# Driver: deuteron.
# ----------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()
    set_compute_dps()
    # q comes from the χ cache this script cross-checks against, so both sides
    # of `Σ_w ρ_w = χ^λ` are evaluated at one anchor by construction.
    _cache_path0 = _pb.witness_path("chi-deuteron-h6-at-q0-50dps.witness.json", HERE)
    _cache0 = json.loads(_cache_path0.read_text())
    Q0_STR = str(_cache0.get("q0Value") or Q0_STR_FALLBACK)
    Q0_ANCHOR = str(_cache0.get("q0Anchor") or "proton")
    q = mpf(Q0_STR)
    qi = mpf(1) / q
    m_e = mpf(M_E_MEV_STR)
    B_D_AME = mpf(B_D_AME_MEV_STR)

    Z, N = 1, 1
    A = Z + N
    n = 3 * A  # 6 strands for the deuteron
    word = atom_canonical_crossings(Z, N)  # the IDENTICAL canonical β_D word

    print(f"[rho_w] deuteron (Z={Z},N={N}), H_{n}, |word|={len(word)} crossings")

    # Load cached χ^λ + y_λ + dim to (a) cross-check Σ_w ρ_w = χ^λ and
    # (b) form the parameter-free binding via the SAME formula the retraction used.
    cache_path = _pb.witness_path("chi-deuteron-h6-at-q0-50dps.witness.json", HERE)
    cache = json.loads(cache_path.read_text())
    chi_cache = {tuple(e["partition"]): mpf(e["chi_lambda"]) for e in cache["by_partition"]}
    y_cache = {tuple(e["partition"]): mpf(e["y_lambda"]) for e in cache["by_partition"]}
    dim_cache = {tuple(e["partition"]): int(e["dim"]) for e in cache["by_partition"]}

    parts = partitions_of(n)
    by_partition = []
    sum_signed = mpf(0)   # Σ_λ y_λ · Δ_λ^{ρ_w} · sgn(w0) · f^λ  (= retraction's Σ)
    max_xcheck_err = mpf(0)

    for lam in parts:
        t_lam = time.time()
        M, syts = rho_lambda_of_word(lam, word, q, qi)
        # ρ_w per crystal vertex w = diagonal of ρ_λ(β_D).
        rho_w = [M[i][i] for i in range(len(syts))]
        delta_lambda = sum(rho_w, mpf(0))   # Σ_w n^w_λ ρ_w, n^w_λ = 1
        f_lambda = len(syts)                # = dim V_λ = |SYT(λ)|

        # Cross-check the FORCED identity against the independent χ cache.
        chi_cached = chi_cache.get(lam)
        xcheck_err = None
        if chi_cached is not None:
            xcheck_err = abs(delta_lambda - chi_cached)
            if xcheck_err > max_xcheck_err:
                max_xcheck_err = xcheck_err

        # Parameter-free binding contribution (SAME formula, SAME sgn·f^λ
        # as the 2026-05-26 retracted claim — but using Δ_λ^{ρ_w}, which ≡ χ^λ).
        # sgn(w0^{S_{λ'}}) = (−1)^{Σ_i C(λ'_i,2)} where λ' is the conjugate;
        # equivalently (−1)^{(n − ℓ(λ))... } — we reuse the cached sign convention
        # by noting the retraction's contribution = y·χ·sgn·f, and chi_cache already
        # carries the physical χ. To stay honest and parameter-free we form the
        # crystal binding directly from Δ_λ^{ρ_w}, y_λ, f^λ and the longest-element
        # sign computed below.
        lam_conj = _conjugate(lam)
        sgn_w0 = mpf((-1) ** sum((c * (c - 1)) // 2 for c in lam_conj))
        y_lambda = y_cache.get(lam, mpf(0))
        contrib = y_lambda * delta_lambda * sgn_w0 * f_lambda
        sum_signed += contrib

        by_partition.append({
            "partition": list(lam),
            "n_crystal_vertices": f_lambda,
            "delta_lambda_rho_w": fmt(delta_lambda),
            "chi_lambda_cached": fmt(chi_cached) if chi_cached is not None else None,
            "crosscheck_abs_err": fmt(xcheck_err) if xcheck_err is not None else None,
            "sgn_w0": int(sgn_w0),
            "y_lambda": fmt(y_lambda),
            "signed_contribution": fmt(contrib),
        })
        print(f"  λ={str(lam):16s} |SYT|={f_lambda:3d} "
              f"Δ_λ^ρw={fmt(delta_lambda, dps=12):>16s} "
              f"χ_cache={fmt(chi_cached, dps=12) if chi_cached is not None else 'NA':>16s} "
              f"|err|={fmt(xcheck_err, dps=4) if xcheck_err is not None else 'NA':>10s} "
              f"({time.time()-t_lam:.2f}s)")

    # Parameter-free binding + honest residual (NO C_knot, NO back-solve).
    B_pred = m_e * abs(sum_signed)
    rel_err = (B_pred - B_D_AME) / B_D_AME
    delta_target = -B_D_AME / m_e         # −4.353 m_e
    delta_pred = sum_signed               # in m_e units
    captured = (B_pred / B_D_AME)
    c_knot_backsolve = B_D_AME / B_pred if B_pred != 0 else None  # NOT applied

    print()
    print(f"[rho_w] max cross-check |Σ_w ρ_w − χ^λ_cache| = {fmt(max_xcheck_err)}")
    print(f"[rho_w] Σ y·Δ_λ^ρw·sgn·f^λ (signed) = {fmt(sum_signed)}")
    print(f"[rho_w] B_pred = m_e·|Σ| = {fmt(B_pred)} MeV  (AME {fmt(B_D_AME)})")
    print(f"[rho_w] rel err = {fmt(rel_err*100, dps=4)} %   captured = {fmt(captured*100, dps=4)} %")
    print(f"[rho_w] Δ_λ residual: predicted {fmt(delta_pred, dps=6)} m_e "
          f"vs target {fmt(delta_target, dps=6)} m_e")
    print(f"[rho_w] back-solve C_knot = target/pred = {fmt(c_knot_backsolve, dps=6)} "
          f"(NOT applied — forbidden)")

    closes = abs(rel_err) < mpf("0.01")  # 1% defensible band
    closure_status = "candidate" if closes else "does_not_close"

    witness = {
        "computation": "rho-w-crystal-vertex-trace",
        "description": (
            "Genuine Kashiwara crystal-vertex trace ρ_w := ⟨v_T|ρ_λ(β_D)|v_T⟩ over "
            "crystal vertices w = T ∈ SYT(λ) = B(λ), via the Hoefsmit/Young seminormal "
            "representation built from first principles (content-determined, "
            "parameter-free). The crystal-summed Δ_λ^{ρ_w} = Σ_w n^w_λ ρ_w with regular "
            "multiplicity n^w_λ = 1 equals the trace = χ^λ(β_D) (FORCED identity, "
            "cross-checked against chi-deuteron-h6-at-q0-50dps.witness.json). Reports the "
            "honest parameter-free deuteron Δ_λ residual. NO C_knot, NO scale menu, NO "
            "back-solve. See docs/audits/2026-05-31-rho-w-crystal-vertex-trace-design.md."
        ),
        "atom": "deuteron",
        "Z": Z, "N": N, "A": A, "n_strands": n,
        "n_partitions": len(parts),
        "braid_word_len": len(word),
        "q_0_50dps": Q0_STR,
        # Recorded so a consumer can tell which layer this witness belongs to
        # WITHOUT inferring it from the digits. Its absence is why a hardcoded
        # muon q sat here against a proton cache without anything noticing.
        #
        # q0Value / q0AnchorReason follow the contract main's labelling pass
        # (4101909790) introduced. That pass transcribed this witness's pin from
        # `q_0_50dps` and correctly labelled it "muon" — a faithful reading of the
        # hardcoded value that was here at the time. Emitting all three from the
        # producer means the label now tracks the pin instead of being recovered
        # from it afterwards, so it cannot go stale when the pin changes.
        "q0Anchor": Q0_ANCHOR,
        "q0Value": Q0_STR,
        "q0AnchorReason": (
            "read from the chi cache this script cross-checks against "
            "(chi-deuteron-h6-at-q0-50dps.witness.json), so both sides of "
            "Sum_w rho_w = chi^lambda are evaluated at one anchor by construction"
        ),
        "m_e_MeV": M_E_MEV_STR,
        "dps": mp.dps,
        "parameter_free": True,
        "free_parameters": [],
        "multiplicity_convention": "n^w_lambda = 1 (regular; diagonal counts each crystal vertex once)",
        "forced_identity": "Delta_lambda^{rho_w} = sum_w rho_w = tr rho_lambda(beta) = chi^lambda(beta)",
        "crosscheck_max_abs_err_vs_chi_cache": fmt(max_xcheck_err),
        "sum_signed_y_delta_sgn_f": fmt(sum_signed),
        "B_pred_MeV": fmt(B_pred),
        "B_D_AME_MeV": fmt(B_D_AME),
        "rel_err": fmt(rel_err),
        "captured_fraction": fmt(captured),
        "delta_lambda_residual_predicted_m_e": fmt(delta_pred),
        "delta_lambda_residual_target_m_e": fmt(delta_target),
        "unaccounted_residual_m_e": fmt(delta_pred - delta_target),
        "c_knot_backsolve_NOT_applied": fmt(c_knot_backsolve),
        "closure_status": closure_status,
        "verdict": (
            "ρ_w is genuinely parameter-free; precisely because it is, the crystal-summed "
            "trace collapses to χ^λ and carries NO degree of freedom beyond the character "
            "the six prior ansätze already exhausted. The deuteron target −4.353 m_e is "
            "unreachable without the forbidden back-solve C_knot. Negative result: "
            "Option-E crystal weights do NOT close the Δ_λ gate."
        ),
        "by_partition": by_partition,
        "compute_time_sec": round(time.time() - t0, 2),
        "design_note": "docs/audits/2026-05-31-rho-w-crystal-vertex-trace-design.md",
    }
    out_path = HERE / "rho-w-crystal-vertex-trace.witness.json"
    out_path.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n[rho_w] closure_status = {closure_status}")
    print(f"[rho_w] witness -> {out_path}")
    print(f"[rho_w] done in {time.time()-t0:.1f}s")
    return 0


def _conjugate(lam: tuple[int, ...]) -> tuple[int, ...]:
    if not lam:
        return ()
    m = lam[0]
    return tuple(sum(1 for p in lam if p > j) for j in range(m))


if __name__ == "__main__":
    raise SystemExit(main())
