#!/usr/bin/env python3
"""Degree-0 purity of the Coxeter-length spectral sequence for HH^*(H_n, M).

Bean qou-6qbv (conj:homological-shell-condensation), reading "Hochschild
cohomology of H_n with coefficients in a natural bimodule M != H_n".

Structural reduction (Hochschild 1945; Weibel 1994 Thm 9.2.11): H_n(q) is
semisimple, hence separable, over a field of characteristic 0 at real q > 1
(and over F_P at an integer q whose square has multiplicative order > n), so
HH^k(H_n, M) = 0 for k >= 1 and EVERY bimodule M.  The length-filtration
spectral sequence is finite, so it converges, and its limit page is
concentrated in total degree 0, where it is the associated graded of
HH^0 = M^A = {m : a.m = m.a} under the filtration induced from M.

Weight convention (as gb_spectral_sequence_h3_probe.py): an elementary cochain
(T_w1 (x)...(x) T_wk -> b) has weight sum l(w_i) - deg(b).  In degree 0 the
weight of b in M is -deg(b).  F^p = span{weight >= p}.  The limit page entry
E_inf^{p,-p} = dim (M^A cap F^p) - dim (M^A cap F^{p+1}).

PURITY in degree 0 (SelectorPrune.offDiag_vanish_iff_pure, H 0 = E 0 0):
E_inf^{p,-p} = 0 for p != 0.

This probe computes, exactly (integers mod two primes, q in {2, 3}, no floats):
  * dim M^A and its length profile E_inf^{p,-p}, for n = 2..6;
  * dim Der(A, M) from the presentation of H_n, hence dim HH^1 (expected 0), n = 2..5;
  * the full Hochschild complex in degrees 0..2 at n = 2, 3 (HH^0, HH^1, HH^2),
for the bimodules
  A      H_n, regular bimodule                         (reference: already merged)
  Ddn    H_n^*, (a.f.b)(x) = f(b x a), deg(T_w^*) = -l(w)
  Dup    H_n^*, same bimodule, deg(T_w^*) = +l(w)
  1(a,b) the 1-dim bimodule with T_s acting by a on the left and b on the right,
         a, b in {ind = q, sgn = -q^{-1}}; deg = 0.
Every bimodule is reported; none is chosen by its result.
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import numpy as np

PRIMES = [1_000_003, 999_983]
QS = [2, 3]
NMAX_PROFILE = 6
NMAX_DER = 5
NMAX_FULL = 3


# ------------------------------------------------------------------ linear algebra mod P
def rank_mod(M: np.ndarray, P: int) -> int:
    if M.size == 0:
        return 0
    A = (M % P).astype(np.int64).copy()
    rows, cols = A.shape
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
        below = np.nonzero(A[r + 1:, c])[0] + r + 1
        if below.size:
            A[below] = (A[below] - (A[below, c][:, None] * A[r][None, :]) % P) % P
        r += 1
    return r


def nullity(M: np.ndarray, P: int) -> int:
    return M.shape[1] - rank_mod(M, P)


# ------------------------------------------------------------------ H_n(q) mod P
def perm_length(w):
    n = len(w)
    return sum(1 for i in range(n) for j in range(i + 1, n) if w[i] > w[j])


def hecke(n: int, q: int, P: int):
    W = sorted(itertools.permutations(range(n)), key=lambda w: (perm_length(w), w))
    idx = {w: i for i, w in enumerate(W)}
    lw = [perm_length(w) for w in W]
    h = (q - pow(q, P - 2, P)) % P
    d = len(W)
    gens = []
    for i in range(n - 1):
        s = list(range(n)); s[i], s[i + 1] = s[i + 1], s[i]
        gens.append(tuple(s))
    comp = lambda a, b: tuple(a[b[k]] for k in range(n))
    L, R = [], []
    for s in gens:
        Ls = np.zeros((d, d), dtype=np.int64)
        Rs = np.zeros((d, d), dtype=np.int64)
        for j, w in enumerate(W):
            for (M, x) in ((Ls, comp(s, w)), (Rs, comp(w, s))):
                if perm_length(x) > lw[j]:
                    M[idx[x], j] = 1
                else:
                    M[j, j] = (M[j, j] + h) % P
                    M[idx[x], j] = (M[idx[x], j] + 1) % P
        L.append(Ls); R.append(Rs)
    return W, lw, gens, L, R, h


def full_mult(W, lw, gens, L, P, n):
    """mult[a, b] = coordinates of T_a T_b (needed only for the full complex)."""
    d = len(W)
    idx = {w: i for i, w in enumerate(W)}
    comp = lambda a, b: tuple(a[b[k]] for k in range(n))
    # left multiplication matrix of T_w, built from a reduced word
    Lw = [None] * d
    Lw[0] = np.eye(d, dtype=np.int64)
    for j, w in enumerate(W):
        if j == 0:
            continue
        for i, s in enumerate(gens):
            sw = comp(s, w)
            if perm_length(sw) < lw[j]:  # w = s (s w), T_w = T_s T_{sw}
                Lw[j] = (L[i] @ Lw[idx[sw]]) % P
                break
    mult = np.zeros((d, d, d), dtype=np.int64)
    for a in range(d):
        mult[a] = Lw[a].T  # mult[a, b] = column b of L_{T_a}
    return mult, Lw


# ------------------------------------------------------------------ bimodules
def bimodules(n, q, P, lw, L, R):
    """name -> (left gen matrices, right gen matrices, degree vector)."""
    qi = pow(q, P - 2, P)
    ind, sgn = q % P, (-qi) % P
    out = {
        "A": (L, R, list(lw)),
        # (T_s . f)(x) = f(x T_s): matrix R_s^T;  (f . T_s)(x) = f(T_s x): matrix L_s^T
        "Ddn": ([m.T.copy() for m in R], [m.T.copy() for m in L], [-x for x in lw]),
        "Dup": ([m.T.copy() for m in R], [m.T.copy() for m in L], list(lw)),
    }
    for (na, a), (nb, b) in itertools.product((("ind", ind), ("sgn", sgn)), repeat=2):
        one = lambda c: [np.array([[c]], dtype=np.int64) for _ in range(n - 1)]
        out[f"1({na},{nb})"] = (one(a), one(b), [0])
    return out


def compatible(Lm, Rm, deg, gen_len=1):
    """deg(T_s . b), deg(b . T_s) <= deg(b) + l(s) for every basis b: the filtration is
    then preserved by d (generators suffice because degree is subadditive in words)."""
    deg = np.array(deg)
    bad = 0
    for M in list(Lm) + list(Rm):
        rr, cc = np.nonzero(M)
        bad += int(np.sum(deg[rr] > deg[cc] + gen_len))
    return bad


def invariants_profile(Lm, Rm, deg, P):
    """dim M^A and E_inf^{p,-p} = dim(M^A cap F^p) - dim(M^A cap F^{p+1}), weight = -deg."""
    S = np.concatenate([(a - b) % P for a, b in zip(Lm, Rm)], axis=0) if Lm else np.zeros((0, len(deg)), dtype=np.int64)
    wt = -np.array(deg)
    ps = sorted(set(wt.tolist()))
    dimF = {}
    for p in ps + [max(ps) + 1]:
        cols = np.nonzero(wt >= p)[0]
        dimF[p] = 0 if cols.size == 0 else (cols.size if S.shape[0] == 0 else nullity(S[:, cols], P))
    prof = {p: dimF[p] - dimF[p + 1] for p in ps if dimF[p] - dimF[p + 1]}
    return dimF[min(ps)], prof


def derivations(Lm, Rm, h, n, P):
    """dim Der(A, M): unknowns m_i = D(T_i), relations of the Hecke presentation."""
    k = n - 1
    dm = Lm[0].shape[0]
    I = np.eye(dm, dtype=np.int64)
    Z = np.zeros((dm, dm), dtype=np.int64)
    blocks = []
    for i in range(k):  # T_i^2 = h T_i + 1  =>  L_i m_i + R_i m_i - h m_i = 0
        row = [Z] * k
        row = list(row); row[i] = (Lm[i] + Rm[i] - h * I) % P
        blocks.append(row)
    for i, j in itertools.combinations(range(k), 2):
        row = [Z] * k; row = list(row)
        if j - i >= 2:  # T_i T_j = T_j T_i
            row[j] = (Lm[i] - Rm[i]) % P
            row[i] = (Rm[j] - Lm[j]) % P
        else:  # T_i T_j T_i = T_j T_i T_j
            row[i] = (Lm[i] @ Lm[j] + Rm[i] @ Rm[j] - Lm[j] @ Rm[j]) % P
            row[j] = (Lm[i] @ Rm[i] - Lm[j] @ Lm[i] - Rm[j] @ Rm[i]) % P
        blocks.append(row)
    S = np.block(blocks) % P
    return nullity(S, P)


# ------------------------------------------------------------------ full Hochschild complex (small n)
def act_all(Lgen_full, Rgen_full):
    return Lgen_full, Rgen_full


def module_actions_full(name, mult, Lw, deg_len, P, q, d):
    """Left/right action matrices of every T_a on M."""
    qi = pow(q, P - 2, P)
    if name == "A":
        return [Lw[a] for a in range(d)], [mult[:, a, :].T.copy() for a in range(d)]  # R_a[:, b] = T_b T_a
    if name in ("Ddn", "Dup"):
        Ra = [mult[:, a, :].T.copy() for a in range(d)]
        return [Ra[a].T.copy() for a in range(d)], [Lw[a].T.copy() for a in range(d)]
    ch = {"ind": q % P, "sgn": (-qi) % P}
    na, nb = name[2:-1].split(",")
    return ([np.array([[pow(ch[na], l, P)]], dtype=np.int64) for l in deg_len],
            [np.array([[pow(ch[nb], l, P)]], dtype=np.int64) for l in deg_len])


def hochschild_dims(mult, La, Ra, P, kmax=2):
    d = mult.shape[0]
    dm = La[0].shape[0]

    def dmat(k):
        src = d ** k * dm
        cols = []
        for j in range(src):
            F = np.zeros(src, dtype=np.int64); F[j] = 1
            F = F.reshape((d,) * k + (dm,))
            G = np.zeros((d,) * (k + 1) + (dm,), dtype=np.int64)
            for t in itertools.product(range(d), repeat=k + 1):
                v = (La[t[0]] @ F[t[1:]]) % P
                for i in range(k):
                    # f(.., t_i t_{i+1}, ..) = sum_j mult[t_i, t_{i+1}, j] F[.., j, ..]
                    pre, post = t[:i], t[i + 2:]
                    acc = np.zeros(dm, dtype=np.int64)
                    for jj in np.nonzero(mult[t[i], t[i + 1]])[0]:
                        acc = (acc + mult[t[i], t[i + 1], jj] * F[pre + (jj,) + post]) % P
                    v = (v + (-1 if i % 2 == 0 else 1) * acc) % P
                v = (v + (1 if (k + 1) % 2 == 0 else -1) * (Ra[t[k]] @ F[t[:k]])) % P
                G[t] = v
            cols.append(G.reshape(-1))
        return np.array(cols, dtype=np.int64).T % P

    Ds = [dmat(k) for k in range(kmax + 1)]
    ranks = [rank_mod(D, P) for D in Ds]
    dims = [d ** k * dm for k in range(kmax + 1)]
    return [dims[k] - ranks[k] - (ranks[k - 1] if k else 0) for k in range(kmax + 1)]


# ------------------------------------------------------------------ driver
def order_q2(q, P, nmax):
    x = q * q % P
    for e in range(1, nmax + 2):
        if pow(x, e, P) == 1:
            return e
    return None


def run(q, P):
    res = {"q2_order_exceeds_nmax": order_q2(q, P, NMAX_PROFILE) is None, "n": {}}
    for n in range(2, NMAX_PROFILE + 1):
        W, lw, gens, L, R, h = hecke(n, q, P)
        # sanity: Hecke relation and braid relation on the regular representation
        d = len(W)
        I = np.eye(d, dtype=np.int64)
        for M in L + R:
            assert not np.any((M @ M - h * M - I) % P)
        for i in range(n - 2):
            assert not np.any((L[i] @ L[i + 1] @ L[i] - L[i + 1] @ L[i] @ L[i + 1]) % P)
        assert not any(np.any((a @ b - b @ a) % P) for a in L for b in R)  # left/right commute
        row = {}
        mods = bimodules(n, q, P, lw, L, R)
        full = None
        if n <= NMAX_FULL:
            mult, Lw = full_mult(W, lw, gens, L, P, n)
            full = (mult, Lw)
        for name, (Lm, Rm, deg) in mods.items():
            entry = {}
            entry["filtration_violations"] = compatible(Lm, Rm, deg)
            dim0, prof = invariants_profile(Lm, Rm, deg, P)
            entry["HH0"] = dim0
            entry["Einf_degree0_profile"] = {str(p): v for p, v in prof.items()}
            entry["pure_in_degree0"] = set(prof) <= {0}
            if n <= NMAX_DER:
                der = derivations(Lm, Rm, h, n, P)
                inner = len(deg) - dim0  # dim of inner derivations = dim M - dim M^A
                entry["HH1_from_presentation"] = der - inner
            if full is not None:
                mult, Lw = full
                La, Ra = module_actions_full(name, mult, Lw, lw, P, q, len(W))
                entry["HH_full_0_1_2"] = hochschild_dims(mult, La, Ra, P, kmax=2)
            row[name] = entry
        res["n"][n] = row
        print(f"q={q} P={P} n={n}", json.dumps({k: (v["HH0"], v["Einf_degree0_profile"]) for k, v in row.items()}), flush=True)
    return res


def main():
    out = {}
    for q in QS:
        for P in PRIMES:
            out[f"q={q},P={P}"] = run(q, P)
    keys = list(out)
    ref = json.dumps(out[keys[0]], sort_keys=True)
    agree = all(json.dumps(out[k], sort_keys=True) == ref for k in keys)
    print("ALL RUNS AGREE:", agree)
    Path(__file__).with_name("hochschild-coefficient-purity.result.json").write_text(
        json.dumps({"agree": agree, "runs": out}, indent=1) + "\n")
    return 0 if agree else 1


if __name__ == "__main__":
    sys.exit(main())
