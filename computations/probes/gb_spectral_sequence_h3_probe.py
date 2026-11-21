#!/usr/bin/env python3
"""Hochschild spectral sequence of H_3(q) under the two candidate filtrations.

Bean qou-6qbv (W8, 2026-11-20). Owner asked for both readings of the filtration
in conj:spectral-sequence-h3-explicit / prop:gb-spectral-sequence:

  Option 1  Coxeter length.  L_a = span{T_w : l(w) <= a}, an increasing algebra
            filtration (L_a L_b <= L_{a+b}).  Cochain weight of the elementary
            map (T_w1 (x) ... (x) T_wk -> T_v) is sum l(w_i) - l(v);
            F^p C^k = span of elementary cochains of weight >= p.

  Option 2  Confinement filtration (def:confinement-level).  At n = 3 the only
            block with nonzero knot-operator energy is (2,1) (the 1-dimensional
            (3) and (1^3) have E = 0), so the proof's decreasing reading is
            J^0 = H_3 > J^1 = B_(2,1) > J^2 = 0.  Cochain filtration read the
            standard way: f in F^p iff f(J^a1 (x) ... (x) J^ak) <= J^(a1+...+ak+p),
            on a basis of Wedderburn matrix units.

The complex is C^k = Hom(A^{(x)k}, A) with the standard Hochschild differential,
k = 0..3.  Arithmetic is EXACT: integers modulo a large prime P, with q an
integer (q = 2 and q = 3; h = q - q^{-1} mod P).  No floats anywhere.  Every
rank is computed at two primes and two values of q and must agree.

Output: E_r^{p,k} dimensions for k = 0, 1, 2 until the page stabilises, the rank
of each d_r, the abutment (should be HH^k(H_3) = dim 3, 0, 0), and for option 2
whether d preserves the filtration at all.
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import numpy as np

PRIMES = [1_000_003, 999_983]  # < 2^20: a product is < 2^40 and a sum of <= 2^20 of them < 2^60, so int64 never overflows
QS = [2, 3]
KMAX = 3  # need C^0..C^3 to read cohomology in degrees 0..2


# ---------------------------------------------------------------- linear algebra mod P
def rref_mod(M: np.ndarray, P: int):
    """Row-reduce a copy of M (int64) mod P. Returns (R, pivot_cols)."""
    A = (M % P).astype(np.int64).copy()
    rows, cols = A.shape
    piv = []
    r = 0
    for c in range(cols):
        if r >= rows:
            break
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0:
            continue
        i = r + nz[0]
        if i != r:
            A[[r, i]] = A[[i, r]]
        inv = pow(int(A[r, c]), P - 2, P)
        A[r] = (A[r] * inv) % P
        col = A[:, c].copy()
        col[r] = 0
        nzr = np.nonzero(col)[0]
        if nzr.size:
            A[nzr] = (A[nzr] - (col[nzr, None] * A[r][None, :]) % P) % P
        piv.append(c)
        r += 1
    return A[:r], piv


def rank_mod(M: np.ndarray, P: int) -> int:
    if M.size == 0:
        return 0
    return len(rref_mod(M, P)[1])


def kernel_mod(M: np.ndarray, P: int) -> np.ndarray:
    """Basis (as columns) of ker M mod P. M is (m x n)."""
    m, n = M.shape
    if m == 0:
        return np.eye(n, dtype=np.int64)
    R, piv = rref_mod(M, P)
    free = [c for c in range(n) if c not in set(piv)]
    K = np.zeros((n, len(free)), dtype=np.int64)
    for j, f in enumerate(free):
        K[f, j] = 1
        for i, pc in enumerate(piv):
            K[pc, j] = (-R[i, f]) % P
    return K


def span_dim(cols: list[np.ndarray], n: int, P: int) -> int:
    mats = [c for c in cols if c.size and c.shape[1]]
    if not mats:
        return 0
    return rank_mod(np.concatenate(mats, axis=1).T, P)


# ---------------------------------------------------------------- the algebra H_3(q)
def perms3():
    return list(itertools.permutations(range(3)))


def compose(a, b):  # (a o b)(i) = a(b(i))
    return tuple(a[b[i]] for i in range(3))


def length(w):
    return sum(1 for i in range(3) for j in range(i + 1, 3) if w[i] > w[j])


S = [(1, 0, 2), (0, 2, 1)]  # s1, s2


def reduced_word(w):
    word = []
    cur = w
    while length(cur) > 0:
        for i, s in enumerate(S):
            if length(compose(s, cur)) < length(cur):  # left descent
                word.append(i)
                cur = compose(s, cur)
                break
    return word  # w = s_{word[0]} s_{word[1]} ...


def hecke_structure(q: int, P: int):
    W = sorted(perms3(), key=lambda w: (length(w), w))
    idx = {w: i for i, w in enumerate(W)}
    h = (q - pow(q, P - 2, P)) % P

    def left_gen(i, vec):  # T_{s_i} * vec
        out = np.zeros(6, dtype=np.int64)
        s = S[i]
        for w, c in zip(W, vec):
            if c == 0:
                continue
            sw = compose(s, w)
            if length(sw) > length(w):
                out[idx[sw]] = (out[idx[sw]] + c) % P
            else:
                out[idx[w]] = (out[idx[w]] + h * c) % P
                out[idx[sw]] = (out[idx[sw]] + c) % P
        return out

    mult = np.zeros((6, 6, 6), dtype=np.int64)  # mult[a, b] = coords of T_a T_b
    for a, wa in enumerate(W):
        for b in range(6):
            vec = np.zeros(6, dtype=np.int64)
            vec[b] = 1
            for i in reversed(reduced_word(wa)):
                vec = left_gen(i, vec)
            mult[a, b] = vec
    return W, mult, h


def check_assoc(mult, P):
    for a, b, c in itertools.product(range(6), repeat=3):
        lhs = np.einsum("i,ij->j", mult[a, b], mult[:, c]) % P
        rhs = np.einsum("j,ij->j", np.ones(6, dtype=np.int64), np.zeros((6, 6), dtype=np.int64))
        rhs = np.zeros(6, dtype=np.int64)
        for j in range(6):
            if mult[b, c][j]:
                rhs = (rhs + mult[b, c][j] * mult[a, j]) % P
        if not np.array_equal(lhs % P, rhs % P):
            return False
    return True


# ---------------------------------------------------------------- Hochschild complex
def cochain_index(k):
    return [(ins, out) for ins in itertools.product(range(6), repeat=k) for out in range(6)]


def hochschild_d(mult, k, P):
    """Matrix of d: C^k -> C^{k+1} in elementary bases."""
    src = cochain_index(k)
    tgt = cochain_index(k + 1)
    tpos = {t: i for i, t in enumerate(tgt)}
    D = np.zeros((len(tgt), len(src)), dtype=np.int64)
    for j, (ins, out) in enumerate(src):
        # f = elementary: f(e_ins) = e_out, zero on other basis tuples.
        # (df)(a0..ak) on basis tuple (b0..bk):
        for t in itertools.product(range(6), repeat=k + 1):
            val = np.zeros(6, dtype=np.int64)
            # a0 f(a1..ak)
            if t[1:] == ins:
                val = (val + mult[t[0], out]) % P
            # sum_i (-1)^{i+1} f(.. a_i a_{i+1} ..)
            for i in range(k):
                prod = mult[t[i], t[i + 1]]
                c = 0
                # argument list (t0..t_{i-1}, t_i t_{i+1}, t_{i+2}..t_k) has k entries;
                # f is elementary at e_ins, so take the coefficient of e_ins[i] in the product
                ok = all(t[m] == ins[m] for m in range(i)) and all(
                    t[m + 1] == ins[m] for m in range(i + 1, k)
                )
                if ok:
                    c = prod[ins[i]]
                if c:
                    sgn = -1 if i % 2 == 0 else 1
                    val[out] = (val[out] + sgn * c) % P
            # (-1)^{k+1} f(a0..a_{k-1}) a_k
            if t[:k] == ins:
                sgn = -1 if (k + 1) % 2 else 1
                val = (val + sgn * mult[out, t[k]]) % P
            for o in np.nonzero(val)[0]:
                D[tpos[(t, int(o))], j] = val[o] % P
    return D


# ---------------------------------------------------------------- spectral sequence
def pages(Ds, weights, P, kmax_read=2, rmax=14):
    """E_r^{p,k} dims for a split weight filtration F^p = span{weight >= p}."""
    res = {}
    for k in range(kmax_read + 1):
        wk = np.array(weights[k])
        wk1 = np.array(weights[k + 1])
        wkm = np.array(weights[k - 1]) if k > 0 else None
        Dk = Ds[k]
        Dkm = Ds[k - 1] if k > 0 else None
        ps = sorted(set(wk.tolist()))

        def Z(r, p):  # basis of {x in F^p C^k : dx in F^{p+r}}
            cols = np.nonzero(wk >= p)[0]
            if cols.size == 0:
                return np.zeros((len(wk), 0), dtype=np.int64)
            rows = np.nonzero(wk1 < p + r)[0]
            sub = Dk[np.ix_(rows, cols)]
            K = kernel_mod(sub, P) if rows.size else np.eye(cols.size, dtype=np.int64)
            full = np.zeros((len(wk), K.shape[1]), dtype=np.int64)
            full[cols] = K
            return full

        def dZprev(r, p):  # d Z_r^{p} computed in degree k-1, image in C^k
            if k == 0:
                return np.zeros((len(wk), 0), dtype=np.int64)
            cols = np.nonzero(wkm >= p)[0]
            if cols.size == 0:
                return np.zeros((len(wk), 0), dtype=np.int64)
            rows = np.nonzero(wk < p + r)[0]
            sub = Dkm[np.ix_(rows, cols)]
            K = kernel_mod(sub, P) if rows.size else np.eye(cols.size, dtype=np.int64)
            full = np.zeros((len(wkm), K.shape[1]), dtype=np.int64)
            full[cols] = K
            return (Dkm @ full) % P

        table = {}
        prev = None
        for r in range(1, rmax + 1):
            row = {}
            for p in ps:
                zr = Z(r, p)
                denom = span_dim([Z(r - 1, p + 1), dZprev(r - 1, p - r + 1)], len(wk), P)
                row[p] = span_dim([zr], len(wk), P) - denom
            row = {p: v for p, v in row.items() if v}
            table[r] = row
            prev = row
        res[k] = table
    return res


def filtration_preserved(Ds, weights):
    bad = 0
    for k, D in enumerate(Ds):
        w_src = np.array(weights[k])
        w_tgt = np.array(weights[k + 1])
        rr, cc = np.nonzero(D)
        bad += int(np.sum(w_tgt[rr] < w_src[cc]))
    return bad


# ---------------------------------------------------------------- option 2 basis
def wedderburn_basis(W, mult, q, P):
    """Change of basis to matrix units of K x M_2 x K via the seminormal reps."""
    qi = pow(q, P - 2, P)
    # generator images
    triv = {0: q % P, 1: q % P}
    sign = {0: (-qi) % P, 1: (-qi) % P}
    # 2-dim seminormal (Hoefsmit) for (2,1) needs sqrt; use a rational model instead:
    # sigma1 = [[q, 0],[0, -q^-1]], sigma2 = [[a, b],[c, d]] with the Hecke and braid
    # relations; take the standard form with b = 1 (Kazhdan-Lusztig style W-graph).
    s1 = np.array([[q % P, 0], [1, (-qi) % P]], dtype=np.int64)
    s2 = np.array([[(-qi) % P, 1], [0, q % P]], dtype=np.int64)
    mats = {0: s1, 1: s2}

    def rep(word, which):
        if which == "triv":
            v = 1
            for i in word:
                v = v * triv[i] % P
            return v
        if which == "sign":
            v = 1
            for i in word:
                v = v * sign[i] % P
            return v
        M = np.eye(2, dtype=np.int64)
        for i in word:
            M = (M @ mats[i]) % P
        return M

    # image of each T_w: 6-vector (triv, M00, M01, M10, M11, sign)
    Phi = np.zeros((6, 6), dtype=np.int64)
    for j, w in enumerate(W):
        word = reduced_word(w)
        M = rep(word, "M")
        Phi[:, j] = [rep(word, "triv"), M[0, 0], M[0, 1], M[1, 0], M[1, 1], rep(word, "sign")]
    return Phi % P


def check_rep(W, mult, Phi, P):
    """Phi(T_a T_b) = Phi(T_a) Phi(T_b) blockwise."""
    def blocks(v):
        return v[0], np.array([[v[1], v[2]], [v[3], v[4]]]), v[5]
    for a in range(6):
        for b in range(6):
            lhs = (Phi @ mult[a, b]) % P
            ta, Ma, sa = blocks(Phi[:, a])
            tb, Mb, sb = blocks(Phi[:, b])
            M = (Ma @ Mb) % P
            rhs = np.array([ta * tb % P, M[0, 0], M[0, 1], M[1, 0], M[1, 1], sa * sb % P]) % P
            if not np.array_equal(lhs, rhs):
                return False
    return True


def run(q, P):
    W, mult, h = hecke_structure(q, P)
    assert check_assoc(mult, P), "associativity failed"
    Ds = [hochschild_d(mult, k, P) for k in range(KMAX)]
    dd = [int(np.count_nonzero((Ds[k + 1] @ Ds[k]) % P)) for k in range(KMAX - 1)]
    total = {}
    for k in range(KMAX):
        n = Ds[k].shape[1]
        rk = rank_mod(Ds[k], P)
        rprev = rank_mod(Ds[k - 1], P) if k else 0
        total[k] = n - rk - rprev
    lw = [length(w) for w in W]
    w1 = [[sum(lw[i] for i in ins) - lw[out] for ins, out in cochain_index(k)] for k in range(KMAX + 1)]
    opt1 = {"filtration_violations": filtration_preserved(Ds, w1), "pages": pages(Ds, w1, P)}

    # option 2: conjugate the complex to the Wedderburn basis
    Phi = wedderburn_basis(W, mult, q, P)
    assert check_rep(W, mult, Phi, P), "representation check failed"
    Pinv_ok = rank_mod(Phi, P) == 6
    level = [0, 1, 1, 1, 1, 0]  # matrix units of B_(2,1) sit at level 1
    # structure constants in the new basis
    Phi_inv = kernel_free_inverse(Phi, P)
    mult2 = np.zeros((6, 6, 6), dtype=np.int64)
    for a in range(6):
        for b in range(6):
            # e_a e_b = Phi( (Phi^-1 e_a)(Phi^-1 e_b) )
            xa, xb = Phi_inv[:, a], Phi_inv[:, b]
            prod = np.zeros(6, dtype=np.int64)
            for i in np.nonzero(xa)[0]:
                for j in np.nonzero(xb)[0]:
                    prod = (prod + xa[i] * xb[j] % P * mult[i, j]) % P
            mult2[a, b] = (Phi @ prod) % P
    Ds2 = [hochschild_d(mult2, k, P) for k in range(KMAX)]
    # J^m = 0 for m >= 2: weight = level(out) - sum level(ins), with outputs at level >= 2 impossible;
    # encode by treating a cochain as lying in F^p iff level(out) >= sum(level(ins)) + p and
    # sum(level(ins)) + p <= 1 (J^{>=2} = 0).  The strict test below is the first half.
    w2 = [[level[out] - sum(level[i] for i in ins) for ins, out in cochain_index(k)] for k in range(KMAX + 1)]
    # Minimal counterexample, independent of how the cochain weights are read:
    # a = E_00 and x = E_01 both lie in J^1 = B_(2,1); the 0-cochain a is in F^1, so
    # compatibility needs (da)(x) = x a - a x in J^2 = 0.  Basis order: (triv, M00, M01, M10, M11, sign).
    a, x = 1, 2
    comm = (mult2[x, a] - mult2[a, x]) % P
    comm_support = [int(i) for i in np.nonzero(comm)[0]]
    opt2 = {"filtration_violations": filtration_preserved(Ds2, w2), "basis_invertible": Pinv_ok,
            "inner_derivation_counterexample": {"a": "E00 in B_(2,1)", "x": "E01 in B_(2,1)",
                                                 "xa_minus_ax_support": comm_support,
                                                 "lies_in_J2_zero": len(comm_support) == 0}}
    return {"h": int(h), "dd_nonzero_entries": dd, "HH_dims": total, "option1": opt1, "option2": opt2}


def kernel_free_inverse(M, P):
    n = M.shape[0]
    aug = np.concatenate([M % P, np.eye(n, dtype=np.int64)], axis=1)
    R, piv = rref_mod(aug, P)
    assert piv[:n] == list(range(n))
    return R[:n, n:]


def main():
    out = {}
    for q in QS:
        for P in PRIMES:
            key = f"q={q},P={P}"
            print("running", key, flush=True)
            out[key] = run(q, P)
            print(json.dumps(out[key], default=str)[:2000], flush=True)
    keys = list(out)
    ref = json.dumps({k: v for k, v in out[keys[0]].items() if k != "h"}, sort_keys=True, default=str)
    agree = all(
        json.dumps({k: v for k, v in out[x].items() if k != "h"}, sort_keys=True, default=str) == ref
        for x in keys
    )
    print("ALL RUNS AGREE:", agree)
    Path(__file__).with_name("gb-spectral-sequence-h3.result.json").write_text(
        json.dumps({"agree": agree, "runs": out}, indent=1, default=str) + "\n"
    )
    return 0 if agree else 1


if __name__ == "__main__":
    sys.exit(main())
