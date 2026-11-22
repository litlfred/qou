#!/usr/bin/env python3
"""Structure probes for the convention-D Markov trace of the v9 nuclear
element at large A (bean / audit: docs/audits/2026-10-12-large-A-markov-trace-structure.md).

The element (same as markov_trace_two_row_tower_probe.py):

    E = prod_{k=1}^{A-1} prod_{i=0}^{k-1} f(type_i, type_k; sigma_i)

right-multiplied in that order, strands 0..Z-1 'p', Z..A-1 'n',
    f(p,p) = sigma,  f(n,n) = sigma - h = sigma^{-1},
    f(p,n) = sigma - h/2 = (sigma + sigma^{-1})/2,     h = q - 1/q,
and tr = convention-D Markov trace (z = q^3/(q^2+1)), which equals the
quantum trace on (C^2)^{(x)A}:

    tr(x) = Tr( K^{(x)A} rho(x) ) / [2]_q^A,   K = diag(q, 1/q),
    rho(sigma_i) = Rcheck on sites i, i+1,
    Rcheck = [[q,0,0,0],[0,h,1,0],[0,1,0,0],[0,0,0,q]]   (basis 00,01,10,11).

(Schur-Weyl: (C^2)^{(x)A} = sum_k V_{A-2k} (x) S_{(A-k,k)}, quantum dimension
[A-2k+1]_q, so this IS sum_k [A-2k+1]/[2]^A chi_{(A-k,k)}.)

What this file does (all arithmetic exact: mpmath at >= 70 dps for values at
q0, or integers mod a 29-bit prime for structure tests; no float anywhere):

  validate   -- planar tensor-network contraction of Tr(K rho(E)) in a greedy
                low-cut order, at q0 in mpmath; compared with the committed
                witness markov-trace-two-row-tower.witness.json.
  cutwidth   -- the largest cut (number of 2-dim legs alive) of that order,
                i.e. log2 of the state size, for A = 10..60.
  q1         -- at q = 1 every factor is the transposition s_i, so
                tr(E)|_{q=1} = 2^{c(w_A) - A}, c = number of cycles of the
                staircase permutation w_A (independent of Z).  Prints w_A's
                cycle type for the requested A.
  osr        -- operator-Schmidt rank of rho(E) across every site cut
                (exact rank mod p at a random q), against the same network
                with random gate coefficients (generic baseline).
  extend     -- the validated network contraction at A beyond the witness
                (A = 17..20 for the chains given by --chains Z:Nmin:Nmax),
                written to large-a-trace-network-extension.witness.json.
  recur      -- fixed-Z sequences a_A = [2]^A tr(E) mod p at random q:
                Berlekamp-Massey linear complexity and a q-holonomic
                recurrence search.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
import time

import mpmath as mp
import numpy as np

Q0_STR = "1.1099785827513808075916690956107688798744991218736"
P = 536870909  # prime < 2^29: products < 2^58, sums of 16 of them < 2^62


# ---------------------------------------------------------------- element

def gate_list(z, n):
    """Word order list of (i, kind) for the v9 element with z protons."""
    types = ["p"] * z + ["n"] * n
    out = []
    for k in range(1, z + n):
        for i in range(k):
            ti, tk = types[i], types[k]
            out.append((i, "pp" if ti == tk == "p" else "nn" if ti == tk == "n" else "pn"))
    return out


def staircase_perm(A):
    """Permutation of positions produced by the word, q = 1 (left-to-right)."""
    pos = list(range(A))
    for k in range(1, A):
        for i in range(k):
            pos[i], pos[i + 1] = pos[i + 1], pos[i]
    return pos


def cycle_type(perm):
    seen, cyc = set(), []
    for s in range(len(perm)):
        if s in seen:
            continue
        c, x = 0, s
        while x not in seen:
            seen.add(x)
            x = perm[x]
            c += 1
        cyc.append(c)
    return sorted(cyc, reverse=True)


# ---------------------------------------------------------------- network

def network(gates):
    """Edges between gate legs.  A gate j on positions (i,i+1) has legs
    ('r',i),('r',i+1) (row / input) and ('c',i),('c',i+1) (column / output)
    of the matrix rho(f_j); Tr(K A_1 ... A_M) joins the column leg of the
    previous gate on position p to the row leg of the next one, and closes
    the last column leg on p to the first row leg on p through K."""
    last, first, edges = {}, {}, []
    for g, (i, _) in enumerate(gates):
        for p in (i, i + 1):
            if p in last:
                edges.append(((last[p], "c", p), (g, "r", p)))
            else:
                first[p] = g
            last[p] = g
    closure = set()
    for p in first:
        edges.append(((last[p], "c", p), (first[p], "r", p)))
        closure.add((first[p], p))
    return edges, closure


def greedy_order(M, edges):
    """Greedy min-cut linear order of the M gates (max-gain next node)."""
    adj = [[] for _ in range(M)]
    for (a, _, _), (b, _, _) in edges:
        adj[a].append(b)
        adj[b].append(a)
    inside, ext, order, cand = [False] * M, [0] * M, [], set()
    cut, worst = 0, 0

    def add(v):
        nonlocal cut
        inside[v] = True
        order.append(v)
        cut += len(adj[v]) - 2 * ext[v]
        for u in adj[v]:
            if not inside[u]:
                ext[u] += 1
                cand.add(u)
        cand.discard(v)

    add(0)
    worst = cut
    while len(order) < M:
        v = max(cand, key=lambda u: (2 * ext[u] - len(adj[u]), -u)) if cand else \
            next(u for u in range(M) if not inside[u])
        add(v)
        worst = max(worst, cut)
    return order, worst


# ---------------------------------------------------------------- rings

class MpRing:
    dtype = object

    def __init__(self, q):
        self.q = q
        self.h = q - 1 / q
        self.zero, self.one = mp.mpf(0), mp.mpf(1)

    def red(self, x):
        return x

    def coeffs(self, kind):
        h = self.h
        return {"pp": (self.zero, self.one), "nn": (-h, self.one),
                "pn": (-h / 2, self.one)}[kind]

    def inv(self, x):
        return 1 / x


class ModRing:
    dtype = np.int64

    def __init__(self, q):
        self.q = q % P
        self.qi = pow(self.q, P - 2, P)
        self.h = (self.q - self.qi) % P
        self.zero, self.one = 0, 1
        self.half = pow(2, P - 2, P)

    def red(self, x):
        return np.mod(x, P)

    def coeffs(self, kind):
        h = self.h
        return {"pp": (0, 1), "nn": ((-h) % P, 1),
                "pn": ((-h * self.half) % P, 1)}[kind]

    def inv(self, x):
        return pow(int(x) % P, P - 2, P)


def rcheck(R, a, b):
    """4x4 matrix a*I + b*Rcheck as a (2,2,2,2) tensor [r_i,r_i1,c_i,c_i1]."""
    q, h = R.q, R.h
    if R.dtype is object:
        Z = mp.mpf(0)
        Rc = [[q, Z, Z, Z], [Z, h, 1, Z], [Z, 1, Z, Z], [Z, Z, Z, q]]
        Mx = [[(a if r == c else Z) + b * Rc[r][c] for c in range(4)] for r in range(4)]
        T = np.empty((4, 4), dtype=object)
        for r in range(4):
            for c in range(4):
                T[r, c] = Mx[r][c]
    else:
        Rc = np.array([[q, 0, 0, 0], [0, h, 1, 0], [0, 1, 0, 0], [0, 0, 0, q]], dtype=np.int64)
        T = np.mod(a * np.eye(4, dtype=np.int64) + b * Rc, P)
    return T.reshape(2, 2, 2, 2)


def kdiag(R):
    if R.dtype is object:
        return [R.q, 1 / R.q]
    return [R.q, R.qi]


def contract(gates, R, order=None, coeff_override=None):
    """Tr( K^{(x)A} rho(E) ) by contracting the network in `order`."""
    M = len(gates)
    edges, closure = network(gates)
    if order is None:
        order, _ = greedy_order(M, edges)
    # label every leg by its edge id
    leg_edge = {}
    for e, (u, v) in enumerate(edges):
        leg_edge[u] = e
        leg_edge[v] = e
    K = kdiag(R)
    state = None
    labels = []
    for g in order:
        i, kind = gates[g]
        a, b = coeff_override[g] if coeff_override is not None else R.coeffs(kind)
        T = rcheck(R, a, b)
        # K on the first row leg of a position (closure)
        for ax, p in ((0, i), (1, i + 1)):
            if (g, p) in closure:
                sl = [slice(None)] * 4
                for s in (0, 1):
                    sl[ax] = s
                    T[tuple(sl)] = R.red(T[tuple(sl)] * K[s])
        tl = [leg_edge[(g, "r", i)], leg_edge[(g, "r", i + 1)],
              leg_edge[(g, "c", i)], leg_edge[(g, "c", i + 1)]]
        if state is None:
            state, labels = T, tl
        else:
            common = [e for e in tl if e in labels]
            ax_s = [labels.index(e) for e in common]
            ax_t = [tl.index(e) for e in common]
            if R.dtype is object:
                new = np.tensordot(state, T, axes=(ax_s, ax_t))
            else:
                new = np.mod(np.tensordot(state, T, axes=(ax_s, ax_t)), P)
            labels = [e for e in labels if e not in common] + [e for e in tl if e not in common]
            state = new
        # a gate whose two row legs and two column legs hit the same edge
        # (self-loop) cannot occur here; trace out repeated labels if any
        while len(labels) != len(set(labels)):
            e = next(x for x in labels if labels.count(x) == 2)
            i1 = labels.index(e)
            i2 = labels.index(e, i1 + 1)
            state = np.trace(state, axis1=i1, axis2=i2)
            if R.dtype is not object:
                state = np.mod(state, P)
            labels = [x for k_, x in enumerate(labels) if k_ not in (i1, i2)]
    assert labels == [], labels
    return state[()] if hasattr(state, "shape") else state


def trace_mp(z, n, q):
    gates = gate_list(z, n)
    R = MpRing(q)
    T = contract(gates, R)
    two = q + 1 / q
    return T / two ** (z + n)


# ---------------------------------------------------------------- modes

def mode_validate(args):
    mp.mp.dps = args.dps
    q = mp.mpf(Q0_STR)
    d = json.load(open(args.witness))
    worst = mp.mpf(0)
    n_ok = 0
    t0 = time.time()
    rows = [r for r in d["rows"] if r["a"] <= args.amax]
    for r in rows:
        v = trace_mp(r["z"], r["n"], q)
        w = mp.mpf(r["tr_markov_d"])
        diff = abs(v - w)
        worst = max(worst, diff)
        ok = diff < mp.mpf(10) ** (-55)
        n_ok += ok
        print(f"{r['isotope']:>5} A={r['a']:2d}  network={mp.nstr(v, 30):>36}  "
              f"|diff|={mp.nstr(diff, 3)}  {'OK' if ok else 'MISMATCH'}  "
              f"t={time.time() - t0:.0f}s", flush=True)
    print(f"validated {n_ok}/{len(rows)} rows (A <= {args.amax}); worst |diff| = {mp.nstr(worst, 3)}")
    return n_ok == len(rows)


def mode_cutwidth(args):
    for A in args.alist:
        gates = gate_list(A, 0)
        edges, _ = network(gates)
        _, w = greedy_order(len(gates), edges)
        print(f"A={A:3d}  gates={len(gates):5d}  greedy max cut = {w:3d} legs  "
              f"(state 2^{w}; two-row tower Catalan({A}) = {mp.nstr(mp.binomial(2 * A, A) / (A + 1), 4)})")


def mode_q1(args):
    for A in args.alist:
        w = staircase_perm(A)
        ct = cycle_type(w)
        print(f"A={A:3d}  cycles={len(ct):3d}  cycle type={ct}  "
              f"tr(E)|q=1 = 2^({len(ct)}-{A})")


def mat_rank_mod(Mx):
    Mx = np.array(Mx, dtype=np.int64) % P
    r, (rows, cols) = 0, Mx.shape
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if Mx[i, c]:
                piv = i
                break
        if piv is None:
            continue
        Mx[[r, piv]] = Mx[[piv, r]]
        inv = pow(int(Mx[r, c]), P - 2, P)
        Mx[r] = (Mx[r] * inv) % P
        col = Mx[:, c].copy()
        col[r] = 0
        nz = np.nonzero(col)[0]
        if len(nz):
            Mx[nz] = (Mx[nz] - np.outer(col[nz], Mx[r]) % P) % P
        r += 1
        if r == rows:
            break
    return r


def full_matrix_mod(gates, A, R, coeffs):
    """rho(E) as a dense 2^A x 2^A matrix mod p (A <= 10)."""
    D = 1 << A
    Mx = np.eye(D, dtype=np.int64)
    for (i, kind), (a, b) in zip(gates, coeffs):
        G = rcheck(R, a, b).reshape(4, 4)
        # right-multiply: Mx <- Mx * (I (x) G_{i,i+1} (x) I), site 0 = MSB
        Mx = Mx.reshape(D, 1 << i, 4, 1 << (A - i - 2))
        Mx = np.mod(np.einsum("xaby,bc->xacy", Mx, G), P)
        Mx = Mx.reshape(D, D)
    return Mx


def osr_profile(Mx, A):
    T = Mx.reshape([2] * (2 * A))  # row sites 0..A-1, col sites 0..A-1
    out = []
    for j in range(1, A):
        # left block: row+col sites 0..j-1
        perm = list(range(j)) + list(range(A, A + j)) + list(range(j, A)) + list(range(A + j, 2 * A))
        B = np.transpose(T, perm).reshape(4 ** j, 4 ** (A - j))
        out.append(mat_rank_mod(B))
    return out


def mode_osr(args):
    rng = random.Random(20261012)
    q = rng.randrange(2, P - 1)
    R = ModRing(q)
    for A in args.alist:
        for z in sorted({0, A // 2, A}):
            gates = gate_list(z, A - z)
            Mx = full_matrix_mod(gates, A, R, [R.coeffs(k) for _, k in gates])
            prof = osr_profile(Mx, A)
            print(f"A={A} Z={z:2d} structured OSR per cut: {prof}", flush=True)
        gates = gate_list(A, 0)
        rnd = [(rng.randrange(P), rng.randrange(1, P)) for _ in gates]
        Mx = full_matrix_mod(gates, A, R, rnd)
        print(f"A={A}       random-coefficient OSR:    {osr_profile(Mx, A)}")
        print(f"A={A}       naive max min(4^j,4^(A-j)): {[min(4 ** j, 4 ** (A - j)) for j in range(1, A)]}",
              flush=True)


def berlekamp_massey(s):
    C, B, L, m, b = [1], [1], 0, 1, 1
    for n_ in range(len(s)):
        d = s[n_]
        for i in range(1, L + 1):
            d = (d + C[i] * s[n_ - i]) % P
        if d == 0:
            m += 1
            continue
        T = C[:]
        coef = d * pow(b, P - 2, P) % P
        C = C + [0] * (len(B) + m - len(C))
        for i in range(len(B)):
            C[i + m] = (C[i + m] - coef * B[i]) % P
        if 2 * L <= n_:
            L, B, b, m = n_ + 1 - L, T, d, 1
        else:
            m += 1
    return L


def nullity_mod(rows, ncols):
    return ncols - mat_rank_mod(np.array(rows, dtype=np.int64))


def mode_recur(args):
    rng = random.Random(7)
    q = rng.randrange(2, P - 1)
    R = ModRing(q)
    for z in args.zlist:
        seq = []
        t0 = time.time()
        for A in range(max(z, 1) + 1, args.amax + 1):
            gates = gate_list(z, A - z)
            seq.append(int(contract(gates, R)) % P)
        L = berlekamp_massey(seq)
        print(f"Z={z}: {len(seq)} terms (A={max(z,1)+1}..{args.amax}), "
              f"BM linear complexity = {L} (a recurrence would show L << len/2 = {len(seq)/2})  "
              f"t={time.time()-t0:.0f}s", flush=True)
        # q-holonomic: sum_{j<=d} sum_{e<=deg} c_{je} q^{e*A} a_{A+j} = 0
        A0 = max(z, 1) + 1
        for d_, deg in ((1, 3), (2, 2), (2, 3), (3, 1)):
            nunk = (d_ + 1) * (deg + 1)
            rows = []
            for t in range(len(seq) - d_):
                A = A0 + t
                rows.append([pow(q, e * A, P) * seq[t + j] % P
                             for j in range(d_ + 1) for e in range(deg + 1)])
            if len(rows) <= nunk:
                continue
            nul = nullity_mod(rows, nunk)
            print(f"    q-holonomic order {d_}, coeff degree {deg}: {len(rows)} eqs, "
                  f"{nunk} unknowns, nullity {nul}  ({'RECURRENCE' if nul else 'none'})", flush=True)


SYM = {8: "o", 9: "f", 10: "ne", 11: "na", 12: "mg"}


def mode_extend(args):
    mp.mp.dps = args.dps
    q = mp.mpf(Q0_STR)
    rows = []
    for spec in args.chains:
        z, n0, n1 = (int(x) for x in spec.split(":"))
        for n in range(n0, n1 + 1):
            t0 = time.time()
            gates = gate_list(z, n)
            edges, _ = network(gates)
            _, w = greedy_order(len(gates), edges)
            v = trace_mp(z, n, q)
            pn = z * n
            rows.append({"isotope": f"{z + n}{SYM.get(z, '?')}", "z": z, "n": n, "a": z + n,
                         "pn": pn, "max_cut_legs": w, "tr_markov_d": mp.nstr(v, 60),
                         "elapsed_sec": round(time.time() - t0, 1)})
            print(rows[-1], flush=True)
            if args.out:
                json.dump({"description": "Convention-D Markov trace of the v9 nuclear element "
                           "(same element and normalisation as markov-trace-two-row-tower), by "
                           "planar tensor-network contraction of Tr(K^{(x)A} rho(E))/[2]^A in "
                           "a greedy low-cut order, mpmath; validated 63/63 against the two-row "
                           "tower witness for A <= 16.",
                           "producer": "computations/probes/large_a_trace_structure_probe.py",
                           "q0": Q0_STR, "q0_anchor": "proton",
                           "q0Anchor": "proton", "q0Value": Q0_STR,
                           "z": "q^3/(q^2+1)", "dps": args.dps, "rows": rows},
                          open(args.out, "w"), indent=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["validate", "cutwidth", "q1", "osr", "recur", "extend"])
    ap.add_argument("--dps", type=int, default=70)
    ap.add_argument("--amax", type=int, default=16)
    ap.add_argument("--alist", type=int, nargs="*", default=[10, 16, 20, 30, 40, 60])
    ap.add_argument("--zlist", type=int, nargs="*", default=[0, 1, 2, 3])
    ap.add_argument("--chains", nargs="*", default=["8:9:12", "9:8:11", "10:7:10"])
    ap.add_argument("--out", default=None)
    ap.add_argument("--witness", default="computations/probes/markov-trace-two-row-tower.witness.json")
    args = ap.parse_args()
    ok = {"validate": mode_validate, "cutwidth": mode_cutwidth, "q1": mode_q1,
          "osr": mode_osr, "recur": mode_recur, "extend": mode_extend}[args.mode](args)
    if ok is False:
        sys.exit(1)


if __name__ == "__main__":
    main()
