"""Closure-b step 2g/3 — ρ_ξ⊗ρ_ν gauge alignment + H_9 universality (WIP).

Builds on the verified step-2 result (PR #2353): the categorical interface operator
A^λ_{ξν}(I) = Π_{ξν} ρ_λ(I) Π_{ξν} reconstructs χ^λ exactly (deuteron, 1.5e-49).
This module adds the remaining pieces toward feeding the combiner / unlocking
A ≥ 3:

  2g. Express A^λ_{ξν}(I) as a (d_ξ·d_ν)×(d_ξ·d_ν) matrix in V_ξ⊗V_ν
      coordinates (gauge alignment) — a basis-change of range(Π_{ξν}).
  3.  Construct A at H_9 and reconstruct tr_M(T)/tr_M(³He) (the case the
      least-squares fit misses by 21–42 %).

## Verified building block in this file

`range_basis_and_restricted_gens` constructs, per (ξ,ν), an orthonormal basis Q
of range(Π_{ξν}) (the invariant subspace) and the restricted generators
g̃ = Qᵀ ρ_λ(g) Q. Because range(Π_{ξν}) is invariant under the inner H_3
(⟨σ_0,σ_1⟩) and block H_3 (⟨σ_3,σ_4⟩) — both commute with Π_{ξν} — the
compression Qᵀ σ Q IS the genuine restriction. Verified properties (exact, 50 dps):
  - Q orthonormal (QᵀQ = I_m, m = c·d_ξ·d_ν);
  - restricted inner/block generators satisfy the Hecke relation
    (g̃ − q)(g̃ + q⁻¹) = 0;
  - the inner class-sum acts as the scalar e_ξ on range (ξ-isotypic), the block
    class-sum as e_ν (ν-isotypic) — confirming the (ξ,ν) labelling.

## Remaining (TODO closure-b — precise spec)

The gauge-aligning isometry U_{ξν}: V_ξ⊗V_ν⊗ℂ^c → range(Π_{ξν}) must satisfy
  Uᵀ ρ_λ(g_in) U = ρ_ξ(g)⊗I_ν⊗I_c,   Uᵀ ρ_λ(g_bl) U = I_ξ⊗ρ_ν(g)⊗I_c,
with ρ_ξ, ρ_ν from `seminormal_matrices_mpfr` at H_3. Construction (exact):
  (i)  Young seminormal matrix units E^ξ_{tt'} of the inner H_3 on Q (polynomials
       in the restricted inner generators) expose the V_ξ factor;
  (ii) within a fixed inner idempotent's range, the block H_3 matrix units E^ν
       expose V_ν; the residual degeneracy is the multiplicity ℂ^c;
  (iii) A_full = Uᵀ (Π_{ξν} ρ_λ(I) Π_{ξν}) U  [(d_ξ d_ν c)²];
        A_combiner = partial-trace over ℂ^c.
Verification target: Σ_{ξν} Tr[A_combiner·(ρ_ξ(W)⊗ρ_ν(β))] = χ^λ(W·I·β) at
1e-25, with ρ_ξ(W), ρ_ν(β) evaluated at H_3 (the speedup — small dim). Internal
consistency only is needed (same seminormal source on both sides); matching the
legacy fitted extract entrywise is optional.

Design: docs/audits/2026-06-16-categorical-interface-operator-closure-b-design.md
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from lr_coefficients import partitions_of  # noqa: E402
import a_operator_categorical as aoa  # noqa: E402

EXACT_TOL = mp.mpf("1e-25")



def _d_pn(h, q=None):
    """Colour-weighted p-n interface shift -h(1/2 - delta/4) (qou-gdtb).

    The interface here is the PHYSICAL p-n bridge (the docstring's
    "reconstructs chi^lambda exactly (deuteron, 1.5e-49)"), so it must carry
    the same colour weighting the canonical braid word emits. It previously
    used the colour-blind -h/2; that agreed to 1.5e-49 only because the chi
    path was colour-blind too. Both are now weighted.

    `q` threads the flavour split (2026-08-24, bean `qou-8chw`). The default
    `_avg_color_delta()` is a LAZILY-CACHED MODULE GLOBAL evaluated once at the
    anchor q_0 and taking no q argument, so building the interface at any other
    q silently baked a q_0-pinned constant into it — the layer straddle
    `d_for_ctype`'s own `delta=` docstring already warns about for q-symbolic
    callers, here reached by a numeric off-anchor caller instead.

    It is not a small effect off-anchor: δ SIGN-FLIPS under q -> 1/q
    (+0.0013757 at q_0, -0.0016949 at 1/q_0), moving the shift by 1.5e-3
    relative. It was the last of three frozen inputs standing between the A=2
    branching combiner and the fine-Bratteli transfer at the bar image;
    threading it took tr_M^atom(D) at 1/q_0 from 3.2e-4 to **2.3e-15** against
    the transfer's -0.0014808531711619370338, giving that value its second
    independent method.

    Passing `q` is a PROVABLE NO-OP at the anchor: `flavor_split_leading(q_0)`
    and `_avg_color_delta()` were measured EXACTLY equal (diff 0.0 at 60 dps),
    which is why every call site in this module could be threaded without
    re-verifying each one. The owner-gated `_avg_color_delta()` default is
    untouched — the muon/proton split rule in AGENTS.md §"q₀ anchor convention"
    is not in scope here.
    """
    if q is not None:
        from _li_2_q_util import flavor_split_leading
        return -h * (1 - flavor_split_leading(q) / 2) / 2
    from canonical_braid_crossings import _avg_color_delta
    return -h * (1 - _avg_color_delta() / 2) / 2

def _kron(A: "mp.matrix", B: "mp.matrix") -> "mp.matrix":
    """Kronecker product of two mpmath matrices."""
    ra, ca = A.rows, A.cols
    rb, cb = B.rows, B.cols
    out = mp.zeros(ra * rb, ca * cb)
    for i in range(ra):
        for j in range(ca):
            aij = A[i, j]
            if aij == 0:
                continue
            for k in range(rb):
                for l in range(cb):
                    out[i * rb + k, j * cb + l] = aij * B[k, l]
    return out


def _nullspace(M: "mp.matrix", tol: "mp.mpf") -> list:
    """Right null space of M: list of column vectors (mp.matrix n×1) spanning
    {x : M x = 0}, via SVD (right singular vectors with ~0 singular value)."""
    _U, S, V = mp.svd(M)          # M = U diag(S) V ; V is (n×n)
    n = V.cols
    smax = max(S) if len(S) else mp.mpf(1)
    thresh = max(tol, smax * tol)
    null = []
    # Singular values S correspond to the first len(S) rows of V (V's rows are
    # the right singular vectors). Rows beyond len(S) (if M has fewer rows than
    # cols) are also null directions.
    for idx in range(n):
        sv = S[idx] if idx < len(S) else mp.mpf(0)
        if sv <= thresh:
            # idx-th right singular vector as a column. Build explicitly rather
            # than slice (`V[idx, :].T`) — portable across mpmath versions
            # whose matrix slicing support varies (Gemini review #2360).
            null.append(mp.matrix([V[idx, j] for j in range(n)]))
    return null



def _orthonormal_range_basis(P: "mp.matrix", rank: int) -> "mp.matrix":
    """Orthonormal basis (dim×rank) of the column space of the idempotent P.

    P = Π_{ξν} = P_in·P_bl is an OBLIQUE (non-Hermitian) idempotent — a product
    of spectral projectors of non-normal class-sums — so a plain QR's leading
    columns need not span range(P). Use the SVD: range(P) is spanned by the left
    singular vectors with nonzero singular value (the leading `rank` columns of
    U, since the singular values are returned in descending order)."""
    U, S, _V = mp.svd(P)
    dim = P.rows
    out = mp.zeros(dim, rank)
    for i in range(dim):
        for j in range(rank):
            out[i, j] = U[i, j]
    return out


def _compress(Q: "mp.matrix", M: "mp.matrix") -> "mp.matrix":
    """Restriction Qᵀ M Q of M to the invariant subspace spanned by Q."""
    return Q.T * M * Q


def range_basis_and_restricted_gens(lam: tuple[int, ...], q_str: str,
                                    dps: int) -> dict:
    """Per (ξ,ν): orthonormal basis Q of range(Π_{ξν}) and restricted inner /
    block generators. Returns a dict keyed (ξ,ν) with verified diagnostics."""
    mp.mp.dps = dps + 10
    q = mp.mpf(q_str)
    mats, dim = aoa.exact_seminormal_matrices(lam, q_str, dps)
    if dim == 0:
        return {}
    ev = aoa._h3_class_sum_eigenvalues(q_str, dps)
    C_in = aoa._class_sum_C2(mats, 0, 1)
    C_bl = aoa._class_sum_C2(mats, 3, 4)
    P_in = aoa._lagrange_projectors(C_in, ev, dim)
    P_bl = aoa._lagrange_projectors(C_bl, ev, dim)
    out = {}
    for xi in ev:
        for nu in ev:
            Pi = P_in[xi] * P_bl[nu]
            r = int(mp.nint(aoa._trace(Pi)).real)
            if r == 0:
                continue
            Q = _orthonormal_range_basis(Pi, r)
            inner = [_compress(Q, mats[0]), _compress(Q, mats[1])]
            block = [_compress(Q, mats[3]), _compress(Q, mats[4])]
            out[(xi, nu)] = {
                "rank": r, "Q": Q, "inner": inner, "block": block,
            }
    return out


def verify_restricted_gens(dps: int = 50) -> dict:
    """Verify (deuteron H_6, exact): Q orthonormal; restricted inner/block gens
    satisfy the Hecke relation; inner/block class-sums act as the scalars
    e_ξ / e_ν on each range (confirming the (ξ,ν) isotypic labelling)."""
    q = aoa.q0_mp(dps)
    q_str = mp.nstr(q, dps)
    ev = aoa._h3_class_sum_eigenvalues(q_str, dps)
    max_ortho = mp.mpf(0)
    max_hecke = mp.mpf(0)
    max_iso = mp.mpf(0)
    n_blocks = 0
    for lam in partitions_of(6):
        info = range_basis_and_restricted_gens(lam, q_str, dps)
        for (xi, nu), d in info.items():
            n_blocks += 1
            Q, r = d["Q"], d["rank"]
            Ir = mp.eye(r)
            # Orthonormality QᵀQ = I_r
            G = Q.T * Q
            max_ortho = max(max_ortho,
                            max(abs(G[i, j] - Ir[i, j])
                                for i in range(r) for j in range(r)))
            # Hecke relation on each restricted generator
            for g in d["inner"] + d["block"]:
                rel = (g - q * Ir) * (g + (1 / q) * Ir)
                max_hecke = max(max_hecke,
                                max(abs(rel[i, j])
                                    for i in range(r) for j in range(r)))
            # Isotypic: inner class-sum = e_ξ·I_r ; block class-sum = e_ν·I_r
            si0, si1 = d["inner"]
            sb0, sb1 = d["block"]
            C_in_r = si0 + si1 + si0 * si1 * si0
            C_bl_r = sb0 + sb1 + sb0 * sb1 * sb0
            max_iso = max(max_iso,
                          max(abs(C_in_r[i, j] - (ev[xi] if i == j else 0))
                              for i in range(r) for j in range(r)),
                          max(abs(C_bl_r[i, j] - (ev[nu] if i == j else 0))
                              for i in range(r) for j in range(r)))
    passed = (max_ortho < EXACT_TOL and max_hecke < EXACT_TOL
              and max_iso < EXACT_TOL)
    return {
        "n_blocks": n_blocks,
        "max_orthonormality_residual": mp.nstr(max_ortho, 6),
        "max_hecke_relation_residual": mp.nstr(max_hecke, 6),
        "max_isotypic_residual": mp.nstr(max_iso, 6),
        "tolerance": mp.nstr(EXACT_TOL, 4),
        "all_passed": passed,
    }


def verify_isotypic_multiplicity_structure(dps: int = 50) -> dict:
    """Verify (deuteron H_6, exact) that range(Π_{ξν}) decomposes as
    V_ξ ⊗ V_ν ⊗ ℂ^c with the correct multiplicity c = c^λ_{ξν}.

    Method (convention-free — no Jucys-Murphy needed): the inner factor ρ_ξ is
    irreducible, so the restricted inner algebra ⟨σ̃_0,σ̃_1⟩ is the full matrix
    algebra M_{d_ξ} acting as ρ_ξ⊗I_{c d_ν}. A *generic* inner element therefore
    has d_ξ distinct eigenvalues, each of multiplicity c·d_ν; a generic block
    element has d_ν distinct, each mult c·d_ξ. Since inner ⊥ block (commute), a
    generic M = G_in + φ·G_bl has exactly **d_ξ·d_ν distinct eigenvalues, each
    of multiplicity c** — which must equal the LR coefficient c^λ_{ξν}.
    """
    from lr_coefficients import get_lr_table
    mp.mp.dps = dps + 10   # set precision floor before any mp.sqrt/pi/e constants
    q = aoa.q0_mp(dps)
    q_str = mp.nstr(q, dps)
    lr = get_lr_table(3, 3)
    # Irrational generic coefficients (avoid accidental degeneracy).
    a1, a2, b1, b2, phi = mp.sqrt(2), mp.sqrt(3), mp.pi, mp.sqrt(5), mp.e
    clust_tol = mp.mpf("1e-18")
    n_blocks = 0
    n_fail = 0
    failures = []
    for lam in partitions_of(6):
        info = range_basis_and_restricted_gens(lam, q_str, dps)
        for (xi, nu), d in info.items():
            n_blocks += 1
            si0, si1 = d["inner"]
            sb0, sb1 = d["block"]
            G_in = si0 + a1 * si1 + a2 * (si0 * si1)
            G_bl = sb0 + b1 * sb1 + b2 * (sb0 * sb1)
            M = G_in + phi * G_bl
            E, _ER = mp.eig(M)
            clusters: list[list] = []
            for e in E:
                for cl in clusters:
                    if abs(e - cl[0]) < clust_tol:
                        cl.append(e)
                        break
                else:
                    clusters.append([e])
            sizes = sorted(len(cl) for cl in clusters)
            c_lr = lr.get((xi, nu, lam), 0)
            expect_n = aoa.partition_dim(xi) * aoa.partition_dim(nu)
            ok = (len(clusters) == expect_n and sizes == [c_lr] * expect_n)
            if not ok:
                n_fail += 1
                if len(failures) < 5:
                    failures.append({
                        "lambda": list(lam), "xi": list(xi), "nu": list(nu),
                        "n_distinct": len(clusters), "expect_distinct": expect_n,
                        "cluster_sizes": sizes, "c_lr": c_lr})
    return {
        "n_blocks": n_blocks, "n_fail": n_fail,
        "all_passed": n_fail == 0, "failures": failures,
        "method": "generic inner+block eigenvalue multiplicities vs c^λ_ξν",
    }


def _transposition_factor_words(strand_lo: int, strand_hi: int) -> list:
    """Hecke words (lists of (c,d,gen0) factors) for every transposition (i,j),
    strand_lo ≤ i < j ≤ strand_hi (0-based strands). T_(i,j) =
    σ_{j-1}…σ_{i+1} σ_i σ_{i+1}…σ_{j-1} (0-based generators)."""
    words = []
    for i in range(strand_lo, strand_hi + 1):
        for j in range(i + 1, strand_hi + 1):
            mid = list(range(i + 1, j))            # 0-based gens between i,j
            gens = mid[::-1] + [i] + mid
            words.append([(mp.mpf(1), mp.mpf(0), g) for g in gens])
    return words


def _transposition_class_sum(mats: list, strand_lo: int, strand_hi: int) -> "mp.matrix":
    """Σ over transpositions of strands [lo,hi] of ρ(T_(i,j)) (central in that
    H_k factor), built from the H_n seminormal generator matrices `mats`."""
    dim = mats[0].rows
    out = mp.zeros(dim, dim)
    for w in _transposition_factor_words(strand_lo, strand_hi):
        M = mp.eye(dim)
        for (c, d, g) in w:
            M = M * (c * mats[g] + d * mp.eye(dim))
        out += M
    return out


def _classsum_eigenvalues(n_strands: int, q_str: str, dps: int) -> dict:
    """e_μ = (Σ_{transpositions} χ^μ)/d_μ for μ ⊢ n_strands — the scalar by which
    the transposition class-sum acts on the μ-isotypic component. Native chars on
    the standalone H_{n_strands} transposition words (strands 0..n-1)."""
    words = _transposition_factor_words(0, n_strands - 1)
    # native (sign, gen1based) form — all factors here are +σ (sign +1).
    nat = [[(1, g + 1) for (_c, _d, g) in w] for w in words]
    ev = {}
    for mu in partitions_of(n_strands):
        s = sum(mp.mpf(aoa._pyn.chi_lambda_braid_mpfr(list(mu), w, q_str, dps))
                for w in nat)
        ev[mu] = s / aoa.partition_dim(mu)
    return ev


def gauge_aligned_A_combiner_general(lam: tuple[int, ...], n_inner: int,
                                     n_block: int, q_str: str, dps: int) -> dict:
    """General-n_inner version of `gauge_aligned_A_combiner`: the combiner-ready
    A^λ_{μν}(I_pn) for the split H_{n_inner} × H_{n_block} → H_n (μ⊢n_inner,
    ν⊢n_block). Isotypic projectors from the transposition class-sums (separating
    at q₀ — verified for H_6, min eigen-gap 1.15). Same intertwiner null-space
    construction as the deuteron path."""
    q = mp.mpf(q_str)
    h = q - 1 / q
    n = n_inner + n_block
    mats, dim = aoa.exact_seminormal_matrices(lam, q_str, dps)
    if dim == 0:
        return {}
    ev_in = _classsum_eigenvalues(n_inner, q_str, dps)
    ev_bl = _classsum_eigenvalues(n_block, q_str, dps)
    C_in = _transposition_class_sum(mats, 0, n_inner - 1)
    C_bl = _transposition_class_sum(mats, n_inner, n - 1)
    P_in = aoa._lagrange_projectors(C_in, ev_in, dim)
    P_bl = aoa._lagrange_projectors(C_bl, ev_bl, dim)
    # Interface I_pn = σ_{n_inner-1} − (h/2)·1 (the bridge generator).
    I_iface = mats[n_inner - 1] + _d_pn(h, q) * mp.eye(dim)
    null_tol = mp.mpf("1e-30")
    out = {}
    for mu in ev_in:
        d_mu = aoa.partition_dim(mu)
        rmu, _ = aoa.exact_seminormal_matrices(mu, q_str, dps)  # H_{n_inner} gens
        for nu in ev_bl:
            Pi = P_in[mu] * P_bl[nu]
            r = int(mp.nint(aoa._trace(Pi)).real)
            if r == 0:
                continue
            d_nu = aoa.partition_dim(nu)
            rnu, _ = aoa.exact_seminormal_matrices(nu, q_str, dps)
            c = r // (d_mu * d_nu)
            Q = _orthonormal_range_basis(Pi, r)
            Itil = Q.T * I_iface * Q
            # restricted inner gens (0..n_inner-2) and block gens (n_inner..n-2)
            g_in = [Q.T * mats[a] * Q for a in range(n_inner - 1)]
            g_bl = [Q.T * mats[n_inner + b] * Q for b in range(n_block - 1)]
            Ic, Imu, Inu = mp.eye(c), mp.eye(d_mu), mp.eye(d_nu)
            R = ([_kron(_kron(rmu[a], Inu), Ic) for a in range(n_inner - 1)]
                 + [_kron(_kron(Imu, rnu[b]), Ic) for b in range(n_block - 1)])
            G = g_in + g_bl
            Ir = mp.eye(r)
            nrows = len(G) * r * r
            M = mp.zeros(nrows, r * r)
            for bi, (Gk, Rk) in enumerate(zip(G, R)):
                blk = _kron(Ir, Gk) - _kron(Rk.T, Ir)
                for i in range(r * r):
                    for j in range(r * r):
                        M[bi * r * r + i, j] = blk[i, j]
            null = _nullspace(M, null_tol)
            if len(null) == 0:
                out[(mu, nu)] = {"error": "empty intertwiner null space"}
                continue
            coeffs = [mp.sqrt(2) + i + mp.pi * (i + 1) for i in range(len(null))]
            vecU = mp.zeros(r * r, 1)
            for z, v in zip(coeffs, null):
                vecU += z * v
            U = mp.zeros(r, r)
            for i in range(r):
                for j in range(r):
                    U[i, j] = vecU[j * r + i, 0]
            Atil = U ** -1 * Itil * U
            dd = d_mu * d_nu
            A = mp.zeros(dd, dd)
            for a in range(d_mu):
                for b in range(d_nu):
                    for ap in range(d_mu):
                        for bp in range(d_nu):
                            s = mp.mpf(0)
                            for t in range(c):
                                s += Atil[a * d_nu * c + b * c + t,
                                          ap * d_nu * c + bp * c + t]
                            A[a * d_nu + b, ap * d_nu + bp] = s
            out[(mu, nu)] = {"A": A, "c": c, "d_mu": d_mu, "d_nu": d_nu}
    return out


# ──────────────────────────────────────────────────────────────────────
# Cyclic-vector intertwiner (Task B, handover §5): O(r³) replacement for the
# O(r⁴)-memory / O(r⁶)-time vectorised null-space U above. Never forms an
# r²×r² matrix, so it clears the 4 large-r (r=64) λ⊢9 that OOM the null-space
# path AND speeds up every block. Correctness is gated by the same combiner
# identity at 1e-25.
# ──────────────────────────────────────────────────────────────────────

_GROUP_WORDS_CACHE: dict = {}
_COL0_PREIMAGE_CACHE: dict = {}


def _group_words(ngen: int) -> list:
    """One generator-index word per element of S_{ngen+1}, via BFS over the
    Cayley graph with adjacent-transposition generators (g swaps positions
    g, g+1). The Hecke basis {T_w : w ∈ S_n} spans H_n, so {ρ(T_w)} spans
    End(V_μ) — enough to recover any matrix unit. Bounded by n! (≤720 for n≤6)."""
    if ngen in _GROUP_WORDS_CACHE:
        return _GROUP_WORDS_CACHE[ngen]
    from collections import deque
    n = ngen + 1
    start = tuple(range(n))
    seen = {start: ()}
    queue = deque([start])
    while queue:
        perm = queue.popleft()
        word = seen[perm]
        for g in range(ngen):
            nl = list(perm)
            nl[g], nl[g + 1] = nl[g + 1], nl[g]
            nt = tuple(nl)
            if nt not in seen:
                seen[nt] = word + (g,)
                queue.append(nt)
    words = list(seen.values())
    _GROUP_WORDS_CACHE[ngen] = words
    return words


def _col0_matrix_unit_preimages(rgens: list, d: int, mu, tol: "mp.mpf",
                                q_str: str, dps: int):
    """Words T_w and coeffs so that Σ_w coeffs[a][w]·ρ(T_w) = E_{a0}=|e_a⟩⟨e_0|
    (column-0 matrix units), for the small seminormal rep `rgens` (d×d each) of
    partition `mu`. The coeffs depend on `rgens` (hence on `q_str`, `dps`), so
    the cache key carries (μ, q_str, dps). Row-major vec convention."""
    key = (mu, q_str, dps)
    if key in _COL0_PREIMAGE_CACHE:
        return _COL0_PREIMAGE_CACHE[key]
    if d == 1:
        res = ([()], [[mp.mpf(1)]])
        _COL0_PREIMAGE_CACHE[key] = res
        return res
    ngen = len(rgens)
    eye = mp.eye(d)

    def flat(M):
        return [M[i, j] for i in range(d) for j in range(d)]

    sel_words, sel_vecs, onb = [], [], []

    def try_add(word, M):
        v = flat(M)
        w = list(v)
        for u in onb:
            proj = mp.fsum(mp.conj(u[t]) * v[t] for t in range(d * d))
            for t in range(d * d):
                w[t] -= proj * u[t]
        nrm = mp.sqrt(mp.fsum(abs(w[t]) ** 2 for t in range(d * d)))
        if nrm > tol:
            onb.append([w[t] / nrm for t in range(d * d)])
            sel_words.append(word)
            sel_vecs.append(v)
            return True
        return False

    target = d * d
    # ρ(word) over all reduced words of S_{ngen+1}; greedily keep independent.
    cache = {(): eye}
    for word in _group_words(ngen):
        if len(sel_words) >= target:
            break
        if word in cache:
            M = cache[word]
        else:
            M = cache[word[:-1]] * rgens[word[-1]]
            cache[word] = M
        try_add(word, M)
    if len(sel_words) < target:
        raise RuntimeError(f"word span failed: {len(sel_words)}/{target} (μ={mu})")
    V = mp.zeros(d * d, d * d)
    for j, v in enumerate(sel_vecs):
        for i in range(d * d):
            V[i, j] = v[i]
    Vinv = V ** -1
    coeffs = [[Vinv[j, a * d] for j in range(d * d)] for a in range(d)]
    res = (sel_words, coeffs)
    _COL0_PREIMAGE_CACHE[key] = res
    return res


def _restricted_col0_units(ggens: list, words: list, coeffs: list, r: int):
    """Restricted matrix-unit operators H_{a0}|_range (r×r) for a=0..d-1:
    H_{a0} = Σ_w coeffs[a][w]·(product of restricted gens ggens over word w).
    Realises E_{a0}⊗I⊗I on range(Π) (conjugated by the unknown intertwiner)."""
    cache = {(): mp.eye(r)}

    def prod(word):
        m = cache.get(word)
        if m is None:
            m = prod(word[:-1]) * ggens[word[-1]]
            cache[word] = m
        return m

    H = []
    for ca in coeffs:
        M = mp.zeros(r, r)
        for cw, word in zip(ca, words):
            if cw != 0:
                M += cw * prod(word)
        H.append(M)
    return H


def _cyclic_intertwiner(g_in: list, g_bl: list, rmu: list, rnu: list,
                        r: int, d_mu: int, d_nu: int, c: int,
                        mu, nu, tol: "mp.mpf", q_str: str, dps: int) -> "mp.matrix":
    """Intertwiner U (r×r), r = c·d_mu·d_nu, with g̃_in U = U(ρ_μ⊗I⊗I) and
    g̃_bl U = U(I⊗ρ_ν⊗I), via the handover §5 cyclic-vector construction.
    Column (a,b,k) ordering a·d_nu·c + b·c + k matches the partial-trace code."""
    w_mu, c_mu = _col0_matrix_unit_preimages(rmu, d_mu, mu, tol, q_str, dps)
    w_nu, c_nu = _col0_matrix_unit_preimages(rnu, d_nu, nu, tol, q_str, dps)
    Hmu = _restricted_col0_units(g_in, w_mu, c_mu, r)   # H^μ_{a0}|range, a=0..d_mu-1
    Hnu = _restricted_col0_units(g_bl, w_nu, c_nu, r)   # H^ν_{b0}|range, b=0..d_nu-1
    # Reference subspace = range(E^μ_00 · E^ν_00)|range, dim c (idempotent).
    ref = Hmu[0] * Hnu[0]
    W = _orthonormal_range_basis(ref, c)                # r×c, columns w_k
    U = mp.zeros(r, r)
    for a in range(d_mu):
        for b in range(d_nu):
            col_op = Hmu[a] * Hnu[b]                     # E^μ_a0 ⊗ E^ν_b0 on range
            for k in range(c):
                wk = mp.matrix([W[i, k] for i in range(r)])
                colv = col_op * wk
                col = a * d_nu * c + b * c + k
                for i in range(r):
                    U[i, col] = colv[i]
    return U


def gauge_aligned_A_combiner_general_cyclic(lam: tuple[int, ...], n_inner: int,
                                            n_block: int, q_str: str,
                                            dps: int) -> dict:
    """O(r³) cyclic-vector variant of `gauge_aligned_A_combiner_general` — same
    return format and same pn interface, but builds the intertwiner U via the
    handover §5 matrix-unit / cyclic-vector construction instead of the O(r⁴)
    vectorised null space. Clears the 4 large-r (r=64) λ⊢9 the null-space path
    OOMs on. Internal consistency gated by the combiner identity at 1e-25."""
    q = mp.mpf(q_str)
    h = q - 1 / q
    n = n_inner + n_block
    mats, dim = aoa.exact_seminormal_matrices(lam, q_str, dps)
    if dim == 0:
        return {}
    ev_in = _classsum_eigenvalues(n_inner, q_str, dps)
    ev_bl = _classsum_eigenvalues(n_block, q_str, dps)
    C_in = _transposition_class_sum(mats, 0, n_inner - 1)
    C_bl = _transposition_class_sum(mats, n_inner, n - 1)
    P_in = aoa._lagrange_projectors(C_in, ev_in, dim)
    P_bl = aoa._lagrange_projectors(C_bl, ev_bl, dim)
    I_iface = mats[n_inner - 1] + _d_pn(h, q) * mp.eye(dim)
    tol = mp.mpf("1e-30")
    out = {}
    for mu in ev_in:
        d_mu = aoa.partition_dim(mu)
        rmu, _ = aoa.exact_seminormal_matrices(mu, q_str, dps)
        for nu in ev_bl:
            Pi = P_in[mu] * P_bl[nu]
            r = int(mp.nint(aoa._trace(Pi)).real)
            if r == 0:
                continue
            d_nu = aoa.partition_dim(nu)
            rnu, _ = aoa.exact_seminormal_matrices(nu, q_str, dps)
            c = r // (d_mu * d_nu)
            Q = _orthonormal_range_basis(Pi, r)
            Itil = Q.T * I_iface * Q
            g_in = [Q.T * mats[a] * Q for a in range(n_inner - 1)]
            g_bl = [Q.T * mats[n_inner + b] * Q for b in range(n_block - 1)]
            U = _cyclic_intertwiner(g_in, g_bl, rmu, rnu, r, d_mu, d_nu, c,
                                    mu, nu, tol, q_str, dps)
            Atil = U ** -1 * Itil * U
            dd = d_mu * d_nu
            A = mp.zeros(dd, dd)
            for a in range(d_mu):
                for b in range(d_nu):
                    for ap in range(d_mu):
                        for bp in range(d_nu):
                            s = mp.fsum(Atil[a * d_nu * c + b * c + t,
                                             ap * d_nu * c + bp * c + t]
                                        for t in range(c))
                            A[a * d_nu + b, ap * d_nu + bp] = s
            out[(mu, nu)] = {"A": A, "c": c, "d_mu": d_mu, "d_nu": d_nu}
    return out


def gauge_aligned_A_combiner_general_rust(lam: tuple[int, ...], n_inner: int,
                                          n_block: int, q_str: str, dps: int = 50):
    """Rust-backed drop-in for `gauge_aligned_A_combiner_general` — delegates each
    `(μ,ν)` block to the merged `pyhecke_native.gauge_aligned_a_combiner_mpfr`
    (closure-b Rust port, PR #2376), resolving the O(r⁶) pure-mpmath wall that
    forces a `dim(V_λ)` cap on the pure-Python version. Identical return format
    `{(μ,ν): {"A","c","d_mu","d_nu"}}` and identical pn interface
    (`I = σ_{n_inner-1} − h/2`), so callers swap the import and lift the cap.

    Requires the native wheel (`pip install -e tools/pyhecke-native`); raises a
    clear ImportError otherwise.
    """
    try:
        import pyhecke_native as pn
    except ImportError as e:  # pragma: no cover
        raise ImportError(
            "gauge_aligned_A_combiner_general_rust needs pyhecke_native "
            "(pip install -e tools/pyhecke-native) — the Rust combiner from "
            "PR #2376") from e
    from lr_coefficients import lr_coef
    # Raise the mpmath precision floor for the whole body (Gemini review #2380):
    # the Python boundary parses Rust's dps-digit strings via mp.mpf and
    # serialises eigenvalues/interface via mp.nstr — under the caller's default
    # global mp.dps (15) those would silently truncate the 50-digit values.
    # workdps restores the caller's context on exit; nstr digit counts are tied
    # to the active mp.mp.dps so caller-configured extra precision is preserved.
    with mp.workdps(dps + 10):
        sig = mp.mp.dps
        q = mp.mpf(q_str)
        h = q - 1 / q
        d_pn = mp.nstr(_d_pn(h, q), sig)
        ev_in = _classsum_eigenvalues(n_inner, q_str, dps)
        ev_bl = _classsum_eigenvalues(n_block, q_str, dps)
        p_in, p_bl = partitions_of(n_inner), partitions_of(n_block)
        eig_in = [mp.nstr(ev_in[p], sig) for p in p_in]
        eig_bl = [mp.nstr(ev_bl[p], sig) for p in p_bl]
        # ONE all-blocks call per λ (builds the λ seminormal + both class-sums
        # once and loops (μ,ν) internally) — the ~10× speedup over the former
        # per-(μ,ν) call that rebuilt them each time.
        blocks = pn.gauge_aligned_a_combiner_all_blocks_mpfr(
            list(lam), n_inner, n_block,
            [list(p) for p in p_in], eig_in,
            [list(p) for p in p_bl], eig_bl, d_pn, q_str, dps)
        out = {}
        for mu_l, nu_l, R in blocks:
            mu, nu = tuple(mu_l), tuple(nu_l)
            A = mp.matrix([[mp.mpf(x) for x in row] for row in R])
            out[(mu, nu)] = {"A": A, "c": lr_coef(mu, nu, lam),
                             "d_mu": aoa.partition_dim(mu),
                             "d_nu": aoa.partition_dim(nu)}
    return out


def gauge_aligned_A_combiner(lam: tuple[int, ...], q_str: str,
                            dps: int) -> dict:
    """Construct the combiner-ready A^λ_{μν}(I_pn) in standard ρ_μ⊗ρ_ν
    coordinates, per (μ,ν) with c^λ_{μν} > 0 (deuteron H_6).

    A^λ_{μν} = partial-trace over ℂ^c of (U⁻¹ Ĩ U), where:
      - Ĩ = Qᵀ ρ_λ(I) Q is the interface restricted to range(Π_{μν});
      - U: V_μ⊗V_ν⊗ℂ^c → range is an invertible intertwiner satisfying
        ã_a U = U (ρ_μ(σ_a)⊗I_ν⊗I_c), b̃_b U = U (I_μ⊗ρ_ν(σ_b)⊗I_c),
        found as a generic element of the null space of the vectorised
        intertwiner constraints (no isometry needed — the combiner identity is
        preserved under similarity). Target basis order: μ⊗ν⊗c (multiplicity
        fastest).
    """
    q = mp.mpf(q_str)
    h = q - 1 / q
    mats, dim = aoa.exact_seminormal_matrices(lam, q_str, dps)
    if dim == 0:
        return {}
    ev = aoa._h3_class_sum_eigenvalues(q_str, dps)
    C_in = aoa._class_sum_C2(mats, 0, 1)
    C_bl = aoa._class_sum_C2(mats, 3, 4)
    P_in = aoa._lagrange_projectors(C_in, ev, dim)
    P_bl = aoa._lagrange_projectors(C_bl, ev, dim)
    I_iface = mats[2] + _d_pn(h, q) * mp.eye(dim)     # pn interface I = σ_2 − (h/2)·1
    null_tol = mp.mpf("1e-30")
    out = {}
    for mu in ev:
        rmu, _ = aoa.exact_seminormal_matrices(mu, q_str, dps)   # [σ_0,σ_1] H_3
        d_mu = aoa.partition_dim(mu)
        for nu in ev:
            Pi = P_in[mu] * P_bl[nu]
            r = int(mp.nint(aoa._trace(Pi)).real)
            if r == 0:
                continue
            rnu, _ = aoa.exact_seminormal_matrices(nu, q_str, dps)
            d_nu = aoa.partition_dim(nu)
            c = r // (d_mu * d_nu)
            Q = _orthonormal_range_basis(Pi, r)                 # dim×r
            Itil = Q.T * I_iface * Q                            # r×r
            atil = [Q.T * mats[0] * Q, Q.T * mats[1] * Q]
            btil = [Q.T * mats[3] * Q, Q.T * mats[4] * Q]
            # Target generators on V_μ⊗V_ν⊗ℂ^c (order μ⊗ν⊗c).
            Ic, Imu, Inu = mp.eye(c), mp.eye(d_mu), mp.eye(d_nu)
            R = [_kron(_kron(rmu[0], Inu), Ic), _kron(_kron(rmu[1], Inu), Ic),
                 _kron(_kron(Imu, rnu[0]), Ic), _kron(_kron(Imu, rnu[1]), Ic)]
            G = [atil[0], atil[1], btil[0], btil[1]]
            # Vectorised constraint (I_r ⊗ G_k − R_kᵀ ⊗ I_r) vec(U) = 0.
            Ir = mp.eye(r)
            rows = []
            for k in range(4):
                rows.append(_kron(Ir, G[k]) - _kron(R[k].T, Ir))
            M = mp.zeros(4 * r * r, r * r)
            for bi, blk in enumerate(rows):
                for i in range(r * r):
                    for j in range(r * r):
                        M[bi * r * r + i, j] = blk[i, j]
            null = _nullspace(M, null_tol)
            if len(null) == 0:
                out[(mu, nu)] = {"error": "empty intertwiner null space"}
                continue
            # Generic invertible combination of null-space vectors → U.
            coeffs = [mp.sqrt(2) + i + mp.pi * (i + 1) for i in range(len(null))]
            vecU = mp.zeros(r * r, 1)
            for z, v in zip(coeffs, null):
                vecU += z * v
            U = mp.zeros(r, r)
            for i in range(r):
                for j in range(r):
                    # column-major vec (matches vec(AXB)=(Bᵀ⊗A)vec(X)): vecU[j*r+i]
                    U[i, j] = vecU[j * r + i, 0]
            Atil = U ** -1 * Itil * U               # similarity
            # Partial trace over ℂ^c (fastest index): A[(a,b),(a',b')]
            #   = Σ_t Atil[a*d_nu*c + b*c + t, a'*d_nu*c + b'*c + t]
            dd = d_mu * d_nu
            A = mp.zeros(dd, dd)
            for a in range(d_mu):
                for b in range(d_nu):
                    for ap in range(d_mu):
                        for bp in range(d_nu):
                            s = mp.mpf(0)
                            for t in range(c):
                                s += Atil[a * d_nu * c + b * c + t,
                                          ap * d_nu * c + bp * c + t]
                            A[a * d_nu + b, ap * d_nu + bp] = s
            out[(mu, nu)] = {"A": A, "c": c, "d_mu": d_mu, "d_nu": d_nu}
    return out


def verify_combiner_identity(dps: int = 50) -> dict:
    """Step 2g (deuteron H_6, exact 1e-25): verify the gauge-aligned A_combiner
    reproduces χ^λ via the SMALL H_3 reps —

        χ^λ(β_1 · I_pn · β_2) = Σ_{μ,ν} Tr[ A^λ_{μν}(I) · (ρ_μ(β_1)⊗ρ_ν(β_2)) ]

    with ρ_μ(β_1), ρ_ν(β_2) at H_3 (the speedup). Self-consistent (same
    seminormal source on both sides)."""
    q = aoa.q0_mp(dps)
    q_str = mp.nstr(q, dps)
    h = q - 1 / q

    def braid_to_factors(braid):
        return [(mp.mpf(1), mp.mpf(0) if s > 0 else -h, g) for (s, g) in braid]

    def word_matrix(mats, factors):
        d = mats[0].rows
        Mm = mp.eye(d)
        for (cc, dd, g) in factors:
            Mm = Mm * (cc * mats[g] + dd * mp.eye(d))
        return Mm

    inner_braids = aoa._braid_test_words(3)
    block_braids = aoa._braid_test_words(3)
    parts3 = partitions_of(3)
    max_abs = mp.mpf(0)
    n_checks = 0
    n_fail = 0
    worst = None
    rho3 = {p: aoa.exact_seminormal_matrices(p, q_str, dps)[0] for p in parts3}

    for lam in partitions_of(6):
        mats6, dim = aoa.exact_seminormal_matrices(lam, q_str, dps)
        if dim == 0:
            continue
        I_iface = mats6[2] + _d_pn(h, q) * mp.eye(dim)
        Acomb = gauge_aligned_A_combiner(lam, q_str, dps)
        if any("error" in v for v in Acomb.values()):
            return {"all_passed": False,
                    "error": "intertwiner failed for λ=" + str(list(lam))}
        for wi in inner_braids:
            fi = braid_to_factors(wi)
            W6 = word_matrix(mats6, fi)
            rho_mu = {mu: word_matrix(rho3[mu], fi) for mu in parts3}
            for wb in block_braids:
                fb6 = [(cc, dd, g + 3) for (cc, dd, g) in braid_to_factors(wb)]
                B6 = word_matrix(mats6, fb6)
                lhs = aoa._trace(W6 * I_iface * B6)            # ground truth
                fbl = braid_to_factors(wb)
                rho_nu = {nu: word_matrix(rho3[nu], fbl) for nu in parts3}
                rhs = mp.mpf(0)
                for (mu, nu), info in Acomb.items():
                    A = info["A"]
                    K = _kron(rho_mu[mu], rho_nu[nu])          # (d_mu d_nu)²
                    rhs += aoa._trace(A * K)
                ad = abs(lhs - rhs)
                if ad > max_abs:
                    max_abs = ad
                if not (ad < EXACT_TOL):
                    n_fail += 1
                    if worst is None:
                        worst = {"lambda": list(lam), "abs_residual": mp.nstr(ad, 6)}
                n_checks += 1
    return {
        "n_checks": n_checks, "n_fail": n_fail,
        "max_absolute_residual": mp.nstr(max_abs, 8),
        "tolerance": mp.nstr(EXACT_TOL, 4),
        "all_passed": n_fail == 0,
        "worst_failure": worst,
    }


def verify_combiner_h9(lambdas=None, dps: int = 50) -> dict:
    """Step 3 (H_9 universality, exact 1e-25): verify the categorical A^λ_{μν}
    (μ⊢6, ν⊢3) reconstructs χ^λ for *generic multi-strand H_6 inner words* —
    the case the least-squares fit misses by 21–42 %.

        χ^λ(β_1^{H6} · I_pn · β_2^{H3}) = Σ_{μ,ν} Tr[ A^λ_{μν}(I)·(ρ_μ(β_1)⊗ρ_ν(β_2)) ]

    with ρ_μ at H_6, ρ_ν at H_3. Restricted to a curated set of small λ⊢9 (the
    full sweep over all p(9)=30 needs the Rust kernel — pure-mpmath null-space
    SVD is O(r^6)).
    """
    if lambdas is None:
        # Fast, reproducible demonstration set (small range-blocks). The pure-
        # mpmath null-space SVD is O(r^6); larger λ⊢9 (e.g. (7,2),(6,3)) and the
        # full p(9)=30 sweep are correct but slow — deferred to the Rust kernel.
        lambdas = [(9,), (8, 1)]
    q = aoa.q0_mp(dps)
    q_str = mp.nstr(q, dps)
    h = q - 1 / q
    p6, p3 = partitions_of(6), partitions_of(3)

    def fac(br):
        return [(mp.mpf(1), mp.mpf(0) if s > 0 else -h, gg) for (s, gg) in br]

    def wm(mats, f):
        M = mp.eye(mats[0].rows)
        for (c, d, gg) in f:
            M = M * (c * mats[gg] + d * mp.eye(mats[0].rows))
        return M

    # Generic multi-strand H_6 inner words (NOT H_3-lifted) + H_3 block words.
    inner_panel = [[(1, 0), (1, 2), (1, 4), (-1, 1), (1, 3)],
                   [(1, 1), (-1, 3), (1, 0), (1, 4)],
                   [(-1, 2), (1, 0), (1, 3), (1, 1)]]
    block_panel = [[(1, 0), (-1, 1)], [(1, 1), (1, 0)], [(-1, 0)]]
    rho6 = {m: aoa.exact_seminormal_matrices(m, q_str, dps)[0] for m in p6}
    rho3 = {n: aoa.exact_seminormal_matrices(n, q_str, dps)[0] for n in p3}

    max_abs = mp.mpf(0)
    n_checks = 0
    n_fail = 0
    worst = None
    for lam in lambdas:
        mats9, dim = aoa.exact_seminormal_matrices(lam, q_str, dps)
        if dim == 0:
            continue
        I_iface = mats9[5] + _d_pn(h, q) * mp.eye(dim)        # bridge gen 5
        Ac = gauge_aligned_A_combiner_general(lam, 6, 3, q_str, dps)
        if any("error" in v for v in Ac.values()):
            return {"all_passed": False, "error": "intertwiner failed λ=" + str(list(lam))}
        for ib in inner_panel:
            W = wm(mats9, fac(ib))
            rmu = {m: wm(rho6[m], fac(ib)) for m in p6}
            for bb in block_panel:
                B = wm(mats9, [(c, d, gg + 6) for (c, d, gg) in fac(bb)])
                lhs = aoa._trace(W * I_iface * B)
                rnu = {n: wm(rho3[n], fac(bb)) for n in p3}
                rhs = sum((aoa._trace(info["A"] * _kron(rmu[mu], rnu[nu]))
                           for (mu, nu), info in Ac.items() if "A" in info),
                          mp.mpf(0))
                ad = abs(lhs - rhs)
                if ad > max_abs:
                    max_abs = ad
                if not (ad < EXACT_TOL):
                    n_fail += 1
                    if worst is None:
                        worst = {"lambda": list(lam), "abs_residual": mp.nstr(ad, 6)}
                n_checks += 1
    return {
        "lambdas": [list(l) for l in lambdas],
        "n_checks": n_checks, "n_fail": n_fail,
        "max_absolute_residual": mp.nstr(max_abs, 8),
        "tolerance": mp.nstr(EXACT_TOL, 4),
        "all_passed": n_fail == 0, "worst_failure": worst,
    }


def main() -> int:
    dps = 50
    print("=" * 78)
    print("  Closure-b step 2g/3 — gauge-alignment building blocks (WIP)")
    print("=" * 78)
    res = verify_restricted_gens(dps)
    print(f"  [a] range-basis + restricted generators (deuteron H_6, {res['n_blocks']} blocks):")
    print(f"      orthonormality   max residual = {res['max_orthonormality_residual']}")
    print(f"      Hecke relation   max residual = {res['max_hecke_relation_residual']}")
    print(f"      isotypic e_ξ/e_ν max residual = {res['max_isotypic_residual']}")
    print(f"      → {'PASS' if res['all_passed'] else 'FAIL'} (tol {res['tolerance']})")
    print()
    mres = verify_isotypic_multiplicity_structure(dps)
    print(f"  [b] V_ξ⊗V_ν⊗ℂ^c multiplicity structure ({mres['n_blocks']} blocks):")
    print(f"      joint-weight count + multiplicities vs c^λ_ξν")
    print(f"      → {'PASS' if mres['all_passed'] else 'FAIL'} ({mres['n_fail']} fail)")
    for f in mres["failures"]:
        print(f"        FAIL {f}")
    print()
    cres = verify_combiner_identity(dps)
    print(f"  [c] gauge-aligned A_combiner (standard ρ_μ⊗ρ_ν coords) — combiner identity:")
    print(f"      χ^λ(β_1·I·β_2) = Σ_μν Tr[A^λ_μν·(ρ_μ(β_1)⊗ρ_ν(β_2))], ρ at H_3")
    if cres.get("error"):
        print(f"      → FAIL — {cres['error']}")
    else:
        print(f"      → {'PASS' if cres['all_passed'] else 'FAIL'} — "
              f"{cres['n_checks']} checks ({cres['n_fail']} fail), "
              f"max abs residual = {cres['max_absolute_residual']}")
        if not cres["all_passed"]:
            print(f"        worst: {cres['worst_failure']}")
    print()
    hres = verify_combiner_h9(dps=dps)
    print(f"  [d] H_9 universality — categorical A^λ_μν (μ⊢6,ν⊢3), GENERIC H_6 inner words:")
    print(f"      λ⊢9 tested: {hres.get('lambdas')}")
    if hres.get("error"):
        print(f"      → FAIL — {hres['error']}")
    else:
        print(f"      → {'PASS' if hres['all_passed'] else 'FAIL'} — "
              f"{hres['n_checks']} checks ({hres['n_fail']} fail), "
              f"max abs residual = {hres['max_absolute_residual']}")
        if not hres["all_passed"]:
            print(f"        worst: {hres['worst_failure']}")
    print()
    print("  (full p(9)=30 sweep + recursive tr_M(T)/³He → Rust-kernel follow-up.)")
    return 0 if (res["all_passed"] and mres["all_passed"]
                 and cres["all_passed"] and hres["all_passed"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
