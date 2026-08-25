#!/usr/bin/env python3
"""dim HH^1(H_n(q)) via the GENERATOR-RESTRICTED derivation method.

A derivation D of H_n(q) is determined by its values on the Coxeter
generators s_1,...,s_{n-1}, subject to Leibniz-preservation of the defining
relations (quadratic, braid, commuting).  This makes dim Der computable from
(n-1) unknown vectors D(s_i) in C^{n!}, rather than a full n!xn! map -- the
tractable extension of the n=3 brute-force probe to n=5 (dim 120) WITHOUT a
Hecke reduction engine: the T_w-basis multiplication by a generator is pure
Coxeter length/permutation combinatorics.

  T_{s_i} T_w = T_{s_i w}          if l(s_i w) > l(w)
              = a T_w + T_{s_i w}  if l(s_i w) < l(w)     (a = q - q^{-1})
  T_w T_{s_i} = T_{w s_i} / a T_w + T_{w s_i}   symmetrically.

dim Inn = n! - dim Z(A);   dim HH^1 = dim Der - dim Inn.

Validation gate: reproduce the prior n=3 probe (dim HH^1 = 1 at q=i and
q=zeta_6, = 0 at semisimple q=2) before trusting the n=5 number.

Exact cyclotomic arithmetic via mpmath at high dps; rank by Gaussian
elimination with a pivot-gap certificate (no float64).  No fit.
"""
import itertools
import sys
import time

import mpmath as mp
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def perms(n):
    return list(itertools.permutations(range(1, n + 1)))


def inversions(w):
    n = len(w)
    return sum(1 for i in range(n) for j in range(i + 1, n) if w[i] > w[j])


def left_apply(i, w):
    """s_i o w : swap VALUES i, i+1 in the image tuple w."""
    return tuple(i + 1 if x == i else (i if x == i + 1 else x) for x in w)


def right_apply(i, w):
    """w o s_i : swap POSITIONS i-1, i (0-indexed) in w."""
    w = list(w)
    w[i - 1], w[i] = w[i], w[i - 1]
    return tuple(w)


def gen_matrices(n, a):
    """L[i], R[i] : n!xn! left/right multiplication by s_i, in the T_w basis."""
    P = perms(n)
    idx = {w: k for k, w in enumerate(P)}
    N = len(P)
    length = {w: inversions(w) for w in P}
    L = {}
    R = {}
    for i in range(1, n):
        Li = mp.zeros(N, N)
        Ri = mp.zeros(N, N)
        for w in P:
            c = idx[w]
            # left
            u = left_apply(i, w)
            if length[u] > length[w]:
                Li[idx[u], c] += 1
            else:
                Li[c, c] += a
                Li[idx[u], c] += 1
            # right
            v = right_apply(i, w)
            if length[v] > length[w]:
                Ri[idx[v], c] += 1
            else:
                Ri[c, c] += a
                Ri[idx[v], c] += 1
        L[i] = Li
        R[i] = Ri
    return N, L, R


def mat_rank(rows, ncols, tol=None):
    """Rank of a list-of-rows (each a list of mpc) by partial-pivot GE.
    Returns (rank, min_retained_pivot, max_dropped)."""
    if tol is None:
        tol = mp.mpf(10) ** (-20)
    M = [list(r) for r in rows]
    nr = len(M)
    rank = 0
    min_piv = None
    max_drop = mp.mpf(0)
    col = 0
    row = 0
    while col < ncols and row < nr:
        # find pivot
        piv = row
        best = abs(M[row][col])
        for r in range(row + 1, nr):
            v = abs(M[r][col])
            if v > best:
                best = v
                piv = r
        if best <= tol:
            if best > max_drop:
                max_drop = best
            col += 1
            continue
        M[row], M[piv] = M[piv], M[row]
        if min_piv is None or best < min_piv:
            min_piv = best
        pv = M[row][col]
        for r in range(nr):
            if r != row and M[r][col] != 0:
                f = M[r][col] / pv
                Mr = M[r]
                Mrow = M[row]
                for c in range(col, ncols):
                    Mr[c] -= f * Mrow[c]
        rank += 1
        row += 1
        col += 1
    return rank, min_piv, max_drop


def matvec_rows_from(mats_and_slots, N, nblocks):
    """Assemble constraint rows: each 'op' is a dict {block: matrix}; a row
    r of the operator contributes a row over the stacked unknown of length
    nblocks*N with M[block][r,:] placed in that block's column slice."""
    rows = []
    for op in mats_and_slots:
        for r in range(N):
            row = [mp.mpc(0)] * (nblocks * N)
            for b, Mb in op.items():
                base = b * N
                for c in range(N):
                    row[base + c] = Mb[r, c]
            rows.append(row)
    return rows


def compute(n, qval, label):
    t0 = time.time()
    a = qval - 1 / qval
    N, L, R = gen_matrices(n, a)
    I = mp.eye(N)
    gens = list(range(1, n))          # s_1 .. s_{n-1}
    nb = len(gens)

    # ---- center: Z = ker of stacked (L_i - R_i), i=1..n-1 ; dim Inn = N - dimZ
    zrows = []
    for i in gens:
        D = L[i] - R[i]
        for r in range(N):
            zrows.append([D[r, c] for c in range(N)])
    rz, mpz, mdz = mat_rank(zrows, N)
    dimZ = N - rz
    dimInn = N - dimZ

    # ---- derivations: unknown v_b = D(s_{gens[b]}), b=0..nb-1
    ops = []
    # quadratic:  (L_i + R_i - a I) v_i = 0
    for b, i in enumerate(gens):
        ops.append({b: L[i] + R[i] - a * I})
    # commuting: s_i s_j = s_j s_i for |i-j|>=2
    #   (R_j - L_j) v_i + (L_i - R_i) v_j = 0
    for bi, i in enumerate(gens):
        for bj, j in enumerate(gens):
            if j >= i + 2:
                ops.append({bi: R[j] - L[j], bj: L[i] - R[i]})
    # braid: s_i s_{i+1} s_i = s_{i+1} s_i s_{i+1}
    #   LHS D = R_{s_{i+1}s_i} v_i + L_{s_i}R_{s_i} v_{i+1} + L_{s_i s_{i+1}} v_i
    #   RHS D = R_{s_i s_{i+1}} v_{i+1} + L_{s_{i+1}}R_{s_{i+1}} v_i + L_{s_{i+1}s_i} v_{i+1}
    # R_{ab} = R_b R_a ; L_{ab} = L_a L_b
    for b in range(nb - 1):
        i = gens[b]
        j = gens[b + 1]
        Li, Lj, Ri, Rj = L[i], L[j], R[i], R[j]
        # coeff of v_i (block b) and v_j (block b+1)
        coef_i = (Ri * Rj) + (Li * Lj)          # R_{s_j s_i}=R_i R_j? careful below
        # Recompute with explicit product order:
        R_sjsi = Ri * Rj      # R_{s_{i+1} s_i}: R_{ab}=R_b R_a, a=s_{i+1},b=s_i -> R_{s_i}R_{s_{i+1}}=Ri*Rj
        R_sisj = Rj * Ri      # R_{s_i s_{i+1}} = R_{s_{i+1}} R_{s_i} = Rj*Ri
        L_sisj = Li * Lj      # L_{s_i s_{i+1}} = L_{s_i} L_{s_{i+1}}
        L_sjsi = Lj * Li      # L_{s_{i+1} s_i}
        LHS_i = R_sjsi + L_sisj
        LHS_j = Li * Ri       # L_{s_i} R_{s_i}
        RHS_i = Lj * Rj       # L_{s_{i+1}} R_{s_{i+1}}
        RHS_j = R_sisj + L_sjsi
        ops.append({b: LHS_i - RHS_i, b + 1: LHS_j - RHS_j})

    drows = matvec_rows_from(ops, N, nb)
    rd, mpd, mdd = mat_rank(drows, nb * N)
    dimDer = nb * N - rd
    dimHH1 = dimDer - dimInn
    dt = time.time() - t0
    print(f"[{label}] N={N} dimZ={dimZ} dimInn={dimInn} dimDer={dimDer} "
          f"dimHH1={dimHH1}  (pivot_gap Der: min_ret={mp.nstr(mpd,3) if mpd else None} "
          f"max_drop={mp.nstr(mdd,3)})  {dt:.1f}s", flush=True)
    return dict(n=n, label=label, N=N, dimZ=dimZ, dimInn=dimInn,
                dimDer=dimDer, dimHH1=dimHH1)


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else "all"
    zeta6 = mp.mpc(mp.cos(mp.pi / 3), mp.sin(mp.pi / 3))
    zeta5 = mp.mpc(mp.cos(2 * mp.pi / 5), mp.sin(2 * mp.pi / 5))
    results = []
    if only in ("all", "val", "3"):
        # VALIDATION against prior n=3 probe
        results.append(compute(3, mp.mpc(0, 1), "n=3 q=i   [2]_q=0"))
        results.append(compute(3, zeta6, "n=3 q=zeta6 [3]_q=0"))
        results.append(compute(3, mp.mpf(2), "n=3 q=2   semisimple"))
    if only in ("all", "4"):
        results.append(compute(4, mp.mpf(2), "n=4 q=2   semisimple"))
    if only in ("all", "5"):
        results.append(compute(5, mp.mpf(2), "n=5 q=2   semisimple ctrl"))
        results.append(compute(5, zeta5, "n=5 q=zeta5 [5]_q=0 BRING"))
    print("\nSUMMARY")
    for r in results:
        print(f"  {r['label']:28s} dim HH^1 = {r['dimHH1']}")


if __name__ == "__main__":
    main()
