"""Recursion-kernel interface operator A^λ_{ξν}(I) — the A≥4 unlock.

The operator-valued Wenzl branching combiner peels one nucleon (an H_3 block)
at a time:

    χ^λ(W_inner · I · β_block)
      = Σ_{ξ⊢n-3, ν⊢3} Tr_{V_ξ⊗V_ν}( A^λ_{ξν}(I) · (ρ_ξ(W_inner) ⊗ ρ_ν(β_block)) )

The earlier full-seminormal construction (`a_operator_gauge_align`, ported to the
Rust kernel in `tools/pyhecke-native/src/lib.rs`) builds `A^λ_{ξν}(I)` as the
isotypic block `Π_{ξν} ρ_λ(I) Π_{ξν}` and gauge-aligns it with an intertwiner.
That approach is exact and verified at n=9, but does not extend past A=3: the
ambient `ρ_λ(I)` has dimension `d_λ` (≤ 7700 at λ⊢12, ≤ 2.9·10⁵ at λ⊢15) and the
gauge-alignment matrix-unit solve is O(d_ξ⁶) on the inner factor (d_ξ ≤ 216 at
ξ⊢9).

## Structural result — A^λ_{ξν} is block-diagonal in the V_ξ index

Both walls are sidestepped by building `A^λ_{ξν}(I)` directly in the Young
(Gelfand–Tsetlin) standard-tableau basis. In that basis the bridge generator
`σ_{n_inner}` is sparse, and its ξ→ξ diagonal block is **diagonal**: its only
off-diagonal partner `s_{n_inner}·T` swaps the values `n_inner, n_inner+1`, which
always changes the shape of the first `n_inner` cells (the inner factor leaves
the box holding `n_inner`, the block box joins it), so the isotypic projector
`Π_{ξξ}` annihilates it. Consequently — because `ρ_ξ(W)` acts as `ρ_ξ(W)⊗I` and
`ρ_ν(β)` as `I⊗ρ_ν(β)`, forcing equal inner indices against the diagonal bridge —

    A^λ_{ξν}(I) = Σ_a |e^ξ_a⟩⟨e^ξ_a| ⊗ M_a       (block-diagonal in V_ξ)

with each `M_a` a `d_ν×d_ν` matrix assembled from the bridge diagonal
coefficients on the standard tableaux of `ξ` and the skew `λ/ξ`. No `d_λ`
ambient, no null-space intertwiner — only a `(≤3)`-dimensional change of basis
aligning the block-S_3 action on `SkewSYT(λ/ξ)` to the standard `ρ_ν`.

The bridge diagonal coefficient on a tableau `T` depends only on the content
difference `δ = c(box of n_inner+1) − c(box of n_inner)`:

    δ = +1 → q,   δ = −1 → −q⁻¹,   |δ| ≥ 2 → (q−q⁻¹)/(1 − q^{−2δ}),

i.e. `c(box of n_inner)` is fixed by the inner tableau `a` (the corner holding
the largest inner value) and `c(box of n_inner+1)` by the skew filling `w`.

## Verification

- Reproduces the verified Rust combiner at λ⊢9 (max |A_mine − A_rust| ≈ 5e-50).
- Combiner identity holds at λ⊢12 / A=4 (residual ≈ 1e-49) against the direct
  character `young_seminormal.chi_young`.

## Honest ceiling (no production-value change)

Per the main-merged bond-dimension verdict `χ_eff(k) = p(3k)`, the recursion
kernel cannot beat the fine-Bratteli transfer matrix asymptotically. Its value
is (a) making the operator-valued combiner *run* at A=4+ as an independent
cross-check of the transfer, (b) preserving the A-operator's structural content
(which Wedderburn blocks saturate) that the scalar transfer discards, and (c) a
constant-factor speedup. The A≥3 `tr_M` value is already validated by the
transfer; this changes the route, not the number — no fit, no fourth calibration.

Companion: `a_operator_categorical.py` (Π ρ_λ(I) Π construction),
`a_operator_gauge_align.py` (gauge-aligned full-seminormal combiner + oracle).
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import mpmath as mp  # noqa: E402
from functools import lru_cache  # noqa: E402

import a_operator_categorical as aoa  # noqa: E402
from young_seminormal import standard_tableaux, _boxes, _content_by_index  # noqa: E402
from lr_coefficients import partitions_of  # noqa: E402

partition_dim = aoa.partition_dim


def _bridge_diag_coeff(delta: int, q: "mp.mpf", qi: "mp.mpf") -> "mp.mpf":
    """Diagonal seminormal coefficient of a Hecke generator on a standard
    tableau whose two swapped values sit at content difference `delta`."""
    if delta == 1:
        return q
    if delta == -1:
        return -qi
    return (q - qi) / (1 - q ** (-2 * delta))


@lru_cache(maxsize=256)
def skew_standard_tableaux(lam: tuple[int, ...], xi: tuple[int, ...]
                           ) -> tuple[dict, ...]:
    """Standard fillings of the skew shape `λ/ξ` with `1..|λ/ξ|`, as dicts
    {value: λ-box-index}, deterministic order. A skew box is fillable when its
    left and top λ-neighbours are either in `ξ` (already smaller) or filled."""
    boxes = _boxes(lam)
    pos = {b: i for i, b in enumerate(boxes)}
    xi_boxes = set()
    for r, w in enumerate(xi):
        for c in range(w):
            xi_boxes.add((r, c))
    skew_idx = [i for i, b in enumerate(boxes) if b not in xi_boxes]
    m = len(skew_idx)
    left = {}
    above = {}
    for i in skew_idx:
        r, c = boxes[i]
        lb = pos.get((r, c - 1))
        ab = pos.get((r - 1, c))
        # a λ-box in ξ counts as "already present" (holds a smaller value)
        left[i] = None if (lb is None or boxes[lb] in xi_boxes) else lb
        above[i] = None if (ab is None or boxes[ab] in xi_boxes) else ab
    results: list[dict] = []

    def rec(filled: frozenset, assign: dict, val: int):
        if val > m:
            results.append(dict(assign))
            return
        for i in skew_idx:
            if i in filled:
                continue
            if (left[i] is None or left[i] in filled) and \
               (above[i] is None or above[i] in filled):
                assign[val] = i
                rec(filled | {i}, assign, val + 1)
                del assign[val]

    rec(frozenset(), {}, 1)
    return tuple(results)


def _block_gens_on_skew(lam, skew_tabs, n_block, q, qi):
    """Block-S_{n_block} generator matrices ρ(σ_j) (j=1..n_block-1, 1-based) on
    the SkewSYT(λ/ξ) basis, via Young's non-symmetric seminormal rule on the
    λ-contents of the skew boxes. Returns a list of `nW×nW` mpmath matrices."""
    cont = _content_by_index(lam)
    nW = len(skew_tabs)
    index = {tuple(sorted(t.items())): k for k, t in enumerate(skew_tabs)}
    gens = []
    for j in range(1, n_block):
        M = mp.zeros(nW, nW)
        for k, t in enumerate(skew_tabs):
            bi, bj = t[j], t[j + 1]
            delta = cont[bj] - cont[bi]
            if delta == 1:
                M[k, k] = q
            elif delta == -1:
                M[k, k] = -qi
            else:
                u = dict(t)
                u[j], u[j + 1] = t[j + 1], t[j]
                uk = index.get(tuple(sorted(u.items())))
                if uk is None:
                    # s_j·t not standard for the skew → pure diagonal
                    M[k, k] = (q - qi) / (1 - q ** (-2 * delta))
                    continue
                if k < uk:
                    dt = (q - qi) / (1 - q ** (-2 * delta))
                    du = (q - qi) - dt
                    M[k, k] = dt
                    M[uk, uk] = du
                    M[k, uk] = mp.mpf(1)
                    M[uk, k] = dt * du + 1
        gens.append(M)
    return gens


def _align_block_to_standard(blockgens_W, n_block, q_str, dps):
    """Square change of basis `C` (nW×nW) whose columns are the standard-ρ_ν
    coordinates of the block-S_{n_block} action on `SkewSYT(λ/ξ)`, for every
    ν⊢n_block present. Returns `(C, layout)` with `layout[j] = (ν, b)`; the
    operator pulled back as `C⁻¹ diag C` is block-diagonal in ν."""
    nW = blockgens_W[0].rows if blockgens_W else 0
    cols = []
    layout = []
    tol = mp.mpf(10) ** -(dps - 10)
    for nu in partitions_of(n_block):
        mats, d_nu = aoa.exact_seminormal_matrices(nu, q_str, dps)
        # Intertwiner B (nW×d_nu): blockgen_W·B = B·ρ_ν(gen) for every gen.
        rows = []
        for gi, gW in enumerate(blockgens_W):
            gN = mats[gi]
            for i in range(nW):
                for jj in range(d_nu):
                    row = [mp.mpf(0)] * (nW * d_nu)
                    for k in range(nW):
                        row[k + jj * nW] += gW[i, k]
                    for ll in range(d_nu):
                        row[i + ll * nW] -= gN[ll, jj]
                    rows.append(row)
        if not rows:
            continue
        ns = _nullspace(mp.matrix(rows), tol)
        # Each independent null vector is one copy of ν (multiplicity c^λ_{ξν}).
        for v in ns:
            B = mp.matrix(nW, d_nu)
            for i in range(nW):
                for jj in range(d_nu):
                    B[i, jj] = v[i + jj * nW]
            for b in range(d_nu):
                cols.append([B[w, b] for w in range(nW)])
                layout.append((nu, b))
    C = mp.matrix(nW, len(cols))
    for j, col in enumerate(cols):
        for w in range(nW):
            C[w, j] = col[w]
    return C, layout


def _nullspace(M: "mp.matrix", tol: "mp.mpf") -> list:
    """Right null space of `M` (list of mpmath column vectors). Gaussian
    elimination with partial pivoting at MPFR precision."""
    A = M.copy()
    rows, cols = A.rows, A.cols
    pivots = []
    r = 0
    for c in range(cols):
        if r >= rows:
            break
        piv = max(range(r, rows), key=lambda i: abs(A[i, c]))
        if abs(A[piv, c]) < tol:
            continue
        A[r, :], A[piv, :] = A[piv, :].copy(), A[r, :].copy()
        A[r, :] = A[r, :] / A[r, c]
        for i in range(rows):
            if i != r and abs(A[i, c]) > tol:
                A[i, :] = A[i, :] - A[i, c] * A[r, :]
        pivots.append(c)
        r += 1
    free = [c for c in range(cols) if c not in pivots]
    basis = []
    for f in free:
        v = mp.zeros(cols, 1)
        v[f] = mp.mpf(1)
        for i, pc in enumerate(pivots):
            v[pc] = -A[i, f]
        basis.append(v)
    return basis


def interface_blocks(lam: tuple[int, ...], n_inner: int, n_block: int,
                     q_str: str, d_coef, dps: int = 50) -> dict:
    """`A^λ_{ξν}(I)` for every (ξ⊢n_inner, ν⊢n_block) with c^λ_{ξν} > 0, in
    standard `V_ξ⊗V_ν` coordinates, built in the Young/GT basis without the
    `d_λ` ambient. `I = σ_{n_inner} + d_coef·1` (the bridge; `d_coef` = 0 pp,
    −h nn, −h/2 pn). Returns `{(ξ,ν): {"A","c","d_mu","d_nu"}}`."""
    q = mp.mpf(q_str)
    qi = 1 / q
    n = n_inner + n_block
    assert sum(lam) == n, "lam must have n_inner + n_block cells"
    out = {}
    for xi in partitions_of(n_inner):
        # ξ must fit inside λ.
        if len(xi) > len(lam) or any(xi[i] > lam[i] for i in range(len(xi))):
            continue
        skew_tabs = skew_standard_tableaux(lam, xi)
        if not skew_tabs:
            continue
        nW = len(skew_tabs)
        cont = _content_by_index(lam)
        # content of each skew filling's first block box (value 1 in the skew).
        cfirst = [cont[t[1]] for t in skew_tabs]
        # V_ξ basis = SYT(ξ); c_a = content of ξ's box holding the max value.
        xi_tabs = standard_tableaux(xi)
        d_xi = len(xi_tabs)
        cont_xi = _content_by_index(xi)
        c_a = [cont_xi[t[n_inner]] for t in xi_tabs]
        # Diagonal coefficients D[a][w] = bridge(cfirst[w] − c_a[a]) + d_coef.
        D = [[_bridge_diag_coeff(cfirst[w] - c_a[a], q, qi) + d_coef
              for w in range(nW)] for a in range(d_xi)]
        # Block-S_{n_block} action on the skew, aligned to standard ρ_ν.
        blockgens_W = _block_gens_on_skew(lam, skew_tabs, n_block, q, qi)
        C, layout = _align_block_to_standard(blockgens_W, n_block, q_str, dps)
        if C.cols != nW:
            # Defensive: the block decomposition must span the skew space.
            continue
        Cinv = C ** -1
        # Group aligned columns by ν. `_align_block_to_standard` lays them out
        # copy-major: for each multiplicity copy k it emits b = 0..d_nu−1, so
        # ν's columns are ordered (k=0,b=0..),(k=1,b=0..),… The combiner takes
        # the partial trace over the c multiplicity copies.
        nu_cols: dict = {}
        for j, (nu, b) in enumerate(layout):
            nu_cols.setdefault(nu, []).append((j, b))
        for nu, jbs in nu_cols.items():
            d_nu = partition_dim(nu)
            c_lr = len(jbs) // d_nu
            # Map (copy k, basis b) → column index. Emission order is copy-major
            # (each run of d_nu columns is one multiplicity copy).
            col_of = {(idx // d_nu, b): j for idx, (j, b) in enumerate(jbs)}
            dim = d_xi * d_nu
            A = mp.zeros(dim, dim)
            for a in range(d_xi):
                Da = D[a]
                for b1 in range(d_nu):
                    for b2 in range(d_nu):
                        s = mp.mpf(0)
                        for kk in range(c_lr):           # partial trace over ℂ^c
                            j1 = col_of[(kk, b1)]
                            j2 = col_of[(kk, b2)]
                            for w in range(nW):
                                s += Cinv[j1, w] * Da[w] * C[w, j2]
                        A[a * d_nu + b1, a * d_nu + b2] = s
            out[(xi, nu)] = {"A": A, "c": c_lr, "d_mu": d_xi, "d_nu": d_nu}
    return out


def _self_test() -> int:
    """A=4 combiner identity (λ⊢12, n_inner=9) via the recursion kernel,
    cross-checked against the direct character `young_seminormal.chi_young`.
    Self-contained (no Rust wheel) — the A-operator builds in the Young basis."""
    from young_seminormal import chi_young
    mp.mp.dps = 60
    q = aoa.q0_mp(50)
    q_str = mp.nstr(q, 50)
    h = q - 1 / q

    def fac(br):
        return [(mp.mpf(1), mp.mpf(0) if s > 0 else -h, g) for (s, g) in br]

    def wm(ms, f):
        M = mp.eye(ms[0].rows)
        for (c, d, g) in f:
            M = M * (c * ms[g] + d * mp.eye(ms[0].rows))
        return M

    inner = [(1, 0), (1, 3), (-1, 5), (1, 7), (1, 1)]   # generic H_9 inner word
    block = [(1, 0), (-1, 1)]                            # H_3 block word
    rin = {xi: aoa.exact_seminormal_matrices(xi, q_str, 50)[0]
           for xi in partitions_of(9)}
    rbl = {nu: aoa.exact_seminormal_matrices(nu, q_str, 50)[0]
           for nu in partitions_of(3)}
    worst = mp.mpf(0)
    for lam in [(10, 2), (11, 1), (7, 5)]:
        blocks = interface_blocks(lam, 9, 3, q_str, -h / 2, 50)
        full = (fac(inner) + [(mp.mpf(1), -h / 2, 8)]
                + [(c, d, g + 9) for (c, d, g) in fac(block)])
        lhs = chi_young(lam, full, q)
        rhs = sum((aoa._trace(info["A"] * ga_kron(
                       wm(rin[xi], fac(inner)), wm(rbl[nu], fac(block))))
                   for (xi, nu), info in blocks.items()), mp.mpf(0))
        worst = max(worst, abs(lhs - rhs))
    ok = worst < mp.mpf(10) ** -25
    print(f"  recursion-kernel A=4 combiner identity (λ⊢12): "
          f"max|lhs−rhs|={mp.nstr(worst, 4)}  {'OK' if ok else 'FAIL'}")
    return 0 if ok else 1


def ga_kron(A, B):
    """Kronecker product A⊗B (mpmath)."""
    ra, ca = A.rows, A.cols
    rb, cb = B.rows, B.cols
    M = mp.zeros(ra * rb, ca * cb)
    for i in range(ra):
        for j in range(ca):
            for k in range(rb):
                for l in range(cb):
                    M[i * rb + k, j * cb + l] = A[i, j] * B[k, l]
    return M


if __name__ == "__main__":
    import sys as _s
    _s.exit(_self_test())
