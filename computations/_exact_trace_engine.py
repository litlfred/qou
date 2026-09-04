"""Exact (MPFR) twin of the float64 trace engine used in the mass/binding-gap
arc.  No float64 anywhere in the hot path; q comes from `Q_50_DIGIT_STR`.

This is the engine that produced the 200-bit A<=5 and 128-bit A=6 sidecars
next to `probes/the_binding_arc_was_measured_in_float64_probe.py` and
`probes/the_size_only_recursion_reaches_order_six_probe.py`.  It is committed
so the provenance of those sidecars is reproducible; the probes themselves
carry a single-process copy of the same engine and do not import this file.

Mirrors `hecke/hecke_characters.build_seminormal_matrices_mp` (same a / a' / b
formulas, same index conventions) but stores rows as `[(col, mpfr)]` so the
sparse structure (<=2 nnz per row) is exploited.

Environment:
  EXACT_BITS   working precision in bits (default 200, ~60 digits)
  EXACT_PROCS  worker processes for the row loop of each block (default 1);
               rows are independent, so the split is embarrassingly parallel.
"""
from __future__ import annotations

import os
import sys
import time
from math import comb
from pathlib import Path

import gmpy2
from gmpy2 import mpfr

COMP = Path(__file__).resolve().parent
ROOT = COMP.parent
for p in (ROOT / "tools" / "pyhecke" / "python", COMP / "hecke", COMP):
    sys.path.insert(0, str(p))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from hecke_characters import standard_young_tableaux  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

BITS = int(os.environ.get("EXACT_BITS", "200"))
PROCS = int(os.environ.get("EXACT_PROCS", "1"))
VERBOSE = False
gmpy2.get_context().precision = BITS
mp.mp.dps = 60

Q = mpfr(Q_50_DIGIT_STR)
H = Q - 1 / Q
# d_pn = -h(1 - delta/2)/2, delta = (q-1)^2 (1 - q^-4)/3: the closed form of
# `pyhecke.constants.pn_interface_offset` under `bring_color_weighted`.
DELTA = (Q - 1) ** 2 * (1 - Q ** -4) / 3
D_PN = -(H * (1 - DELTA / 2) / 2)
ONE, ZERO = mpfr(1), mpfr(0)


def qint(m):
    return sum(Q ** (m - 1 - 2 * i) for i in range(m))


def weights(n):
    """Convention-D (Wenzl r=2) block weights: only <=2-row shapes survive."""
    ks = list(range(n // 2 + 1))
    ps = [((n - k, k) if k else (n,)) for k in ks]
    raw = [qint(n - 2 * k + 1) for k in ks]
    dims = [comb(n, k) - comb(n, k - 1) if k else 1 for k in ks]
    Z = sum(r * d for r, d in zip(raw, dims))
    return ps, [r / Z for r in raw]


_SIG: dict = {}


def sigmas(shape):
    key = tuple(shape)
    if key in _SIG:
        return _SIG[key]
    n = sum(shape)
    syts, _cells, contents = standard_young_tableaux(list(shape))
    dim = len(syts)
    idx = {tuple(sorted(t.items())): i for i, t in enumerate(syts)}
    out = []
    for k in range(1, n):
        rows: list[list] = [[] for _ in range(dim)]
        seen: set[int] = set()
        for i in range(dim):
            if i in seen:
                continue
            ci, ci1 = syts[i][k], syts[i][k + 1]
            rho = contents[ci1] - contents[ci]
            a = H / (1 - Q ** (-2 * rho))
            ap = H / (1 - Q ** (2 * rho))
            sw = dict(syts[i])
            sw[k], sw[k + 1] = ci1, ci
            j = idx.get(tuple(sorted(sw.items())))
            if j == i:
                j = None
            if j is None:
                rows[i].append((i, a))
                seen.add(i)
            else:
                b = gmpy2.sqrt(abs(a * ap + 1))
                rows[i] += [(i, a), (j, b)]
                rows[j] += [(j, ap), (i, b)]
                seen.add(i)
                seen.add(j)
        out.append(rows)
    _SIG[key] = (out, dim)
    return out, dim


def _op(rows, c, d):
    res = []
    for i, r in enumerate(rows):
        acc: dict = {}
        for j, v in r:
            acc[j] = acc.get(j, ZERO) + c * v
        if d != 0:
            acc[i] = acc.get(i, ZERO) + d
        res.append([(j, v) for j, v in acc.items() if v != 0])
    return res


def _rows_partial(ops, dim, s0, s1):
    acc = ZERO
    for s in range(s0, s1):
        v = [ZERO] * dim
        v[s] = ONE
        nz = [s]
        for op in ops:
            out = [ZERO] * dim
            seen = []
            for i in nz:
                vi = v[i]
                if vi == 0:
                    continue
                for j, m in op[i]:
                    if out[j] == 0:
                        seen.append(j)
                    out[j] = out[j] + vi * m
            v, nz = out, seen
        acc += v[s]
    return acc


_CUR: dict = {}


def _worker(args):
    shape, s0, s1 = args
    gmpy2.get_context().precision = BITS
    rows, dim = sigmas(shape)
    ops = [_op(rows[g], mpfr(c), d) for c, d, g in _CUR["word"]]
    return gmpy2.to_binary(_rows_partial(ops, dim, s0, s1))


def trM(n, word):
    """Weighted trace sum_lambda w_lambda * tr_lambda(prod (c sigma_g + d I))."""
    ps, ws = weights(n)
    tot = ZERO
    for shape, w in zip(ps, ws):
        t0 = time.time()
        rows, dim = sigmas(shape)
        if PROCS > 1 and dim >= 64:
            import multiprocessing as mproc
            _CUR["word"] = word
            step = -(-dim // (PROCS * 4))
            chunks = [(shape, s0, min(s0 + step, dim)) for s0 in range(0, dim, step)]
            with mproc.get_context("fork").Pool(PROCS) as pool:
                parts = pool.map(_worker, chunks)
            acc = sum((gmpy2.from_binary(b) for b in parts), ZERO)
        else:
            ops = [_op(rows[g], mpfr(c), d) for c, d, g in word]
            acc = _rows_partial(ops, dim, 0, dim)
        tot += w * acc
        if VERBOSE:
            print(f"      block {shape} dim {dim:6d}  {time.time() - t0:7.1f}s", flush=True)
    return tot


# ── words, mirroring the production `atom_gen_chains` order letter for letter ──
B_P = (ZERO, ONE / 2, ONE / 2)
B_N = (ONE / 2, ONE / 2, ONE)


def nucleon_word(b, g0, g1):
    w = []
    for _ in range(3):
        w += [(1, ZERO, g0), (1, -H, g1)]
    w += [(1, -b[0] * H, g0), (1, -b[1] * H, g0), (1, -b[2] * H, g1)]
    return w + [(1, ZERO, g0), (1, ZERO, g0)]


def bond_d(a, b):
    return ZERO if a == b == "p" else (-H if a == b == "n" else D_PN)


def band(i, j, d):
    a, b = 3 * i + 2, 3 * j
    ups = list(range(b - 1, a, -1))
    return ([(1, ZERO, g) for g in ups] + [(1, d, a)]
            + [(1, -H, g) for g in reversed(ups)])


def word(order, S):
    w = []
    for k in range(len(order)):
        w += nucleon_word(B_P if order[k] == "p" else B_N, 3 * k, 3 * k + 1)
        if k in S:
            for prev in range(k):
                if prev in S:
                    d = bond_d(order[prev], order[k])
                    w += ([(1, d, 3 * prev + 2)] if k == prev + 1 else band(prev, k, d))
    return w


def L(order, S):
    n = 3 * len(order)
    return gmpy2.log(trM(n, word(order, set())) / trM(n, word(order, set(S))))
