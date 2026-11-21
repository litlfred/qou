#!/usr/bin/env python3
"""γγ shell probe: electron capture, e–e interaction and photon emission in H_{Z+1}.

Bean qou-mgg1. Model: docs/audits/2026-11-21-magic-shells-gamma-gamma-model.md.
Lean definitions: QOU/ShellCondensation/GammaGammaAtom.lean.

  strand 0 = nucleus, strand k = electron k, generators σ_0..σ_{Z-1},
  (σ - q)(σ + q^{-1}) = 0,  h = q - q^{-1},  σ^{-1} = σ - h.
  capture   K_k = A_{0k}^{-1},  A_{0k} = σ_{k-1}..σ_1 σ_0^2 σ_1^{-1}..σ_{k-1}^{-1}
  interact  I_k = σ_{k-1}                       (k >= 2)
  emission  E_k = γ_{k-2}(φ) = 1 + φ0 σ_{k-2} + φ1 σ_{k-1} + φ01 σ_{k-2} σ_{k-1}^{-1}
  atom      W_1 = K_1,  W_k = W_{k-1} K_k I_k E_k ;  binding operator O_k = K_k I_k E_k.

Part A (exact, F_P): normal-form complexity of O_k and W_k in the full H_{k+1}
  (term count, longest normal-form word, number of Hecke reductions), at generic
  integer q and generic φ modulo two primes; the two runs must agree.
Part B (certified, arb intervals at 256 bits): reading-3 Frobenius positivity
  χ_λ(W_k) >= 0 for every λ ⊢ k+1 with at most two rows, at the proton q0,
  over a grid of φ. φ is NOT derived and is NOT tuned: every grid point is
  reported. Signs whose interval contains 0 are reported as undecided.

No float64 on any computational path.
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from pathlib import Path

from flint import arb, arb_mat, ctx

ctx.prec = 256
Q0_STR = "1.1099785827513808075916690956107688798744991218736"  # proton pin (qou_substrate)
OUT = Path(__file__).with_name("gamma-gamma-shell.result.json")
T0 = time.time()


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


# ---------------------------------------------------------------- Part A: F_P
def perm_len(w):
    return sum(1 for i in range(len(w)) for j in range(i + 1, len(w)) if w[i] > w[j])


class HeckeFP:
    """Elements of H_n(q) over F_P as dict {perm tuple: coeff}; right action of σ_i."""

    def __init__(self, n, q, P):
        self.n, self.P = n, P
        self.q = q % P
        self.qi = pow(q, P - 2, P)
        self.h = (self.q - self.qi) % P
        self.reductions = 0

    def one(self):
        return {tuple(range(self.n)): 1}

    def mul_gen(self, x, i, inverse=False):
        P, h = self.P, self.h
        out = {}
        for w, c in x.items():
            ws = list(w)
            ws[i], ws[i + 1] = ws[i + 1], ws[i]
            ws = tuple(ws)
            if w[i] < w[i + 1]:  # length goes up: T_w σ = T_ws
                terms = [(ws, c)]
                if inverse:  # σ^{-1} = σ - h
                    terms.append((w, -h * c))
            else:  # descent: T_w σ = h T_w + T_ws
                self.reductions += 1
                terms = [(w, h * c), (ws, c)]
                if inverse:
                    terms.append((w, -h * c))
            for v, d in terms:
                out[v] = (out.get(v, 0) + d) % P
        return {v: d for v, d in out.items() if d}

    def add(self, x, y, cy=1):
        out = dict(x)
        for v, d in y.items():
            out[v] = (out.get(v, 0) + cy * d) % self.P
        return {v: d for v, d in out.items() if d}

    def word(self, x, letters):
        for i, inv in letters:
            x = self.mul_gen(x, i, inv)
        return x


def capture_letters(k):
    """A_{0k}^{-1} = σ_{k-1} .. σ_1 σ_0^{-2} σ_1^{-1} .. σ_{k-1}^{-1} as (index, inverse) letters."""
    up = [(j, False) for j in range(k - 1, 0, -1)]
    down = [(j, True) for j in range(1, k)]
    return up + [(0, True), (0, True)] + down


def apply_op(H, x, k, phi):
    """x · K_k · I_k · E_k  (only K_1 for k = 1)."""
    x = H.word(x, capture_letters(k))
    if k == 1:
        return x
    x = H.mul_gen(x, k - 1)  # interaction
    i = k - 2
    t0 = H.mul_gen(x, i)
    t1 = H.mul_gen(x, i + 1)
    t01 = H.mul_gen(H.mul_gen(x, i), i + 1, inverse=True)
    y = H.add(x, t0, phi[0])
    y = H.add(y, t1, phi[1])
    return H.add(y, t01, phi[2])


def complexity(x):
    return {"terms": len(x), "max_len": max((perm_len(w) for w in x), default=0)}


def part_a(kmax, runs):
    rows = []
    for k in range(1, kmax + 1):
        n = k + 1
        rec = {"k": k, "n": n}
        per_run = []
        for (q, P, phi) in runs:
            H = HeckeFP(n, q, P)
            W = H.one()
            for j in range(1, k + 1):
                W = apply_op(H, W, j, phi)
            Hw = H.reductions
            H.reductions = 0
            O = apply_op(H, H.one(), k, phi)
            per_run.append({"W": complexity(W), "O": complexity(O),
                            "reductions_W": Hw, "reductions_O": H.reductions})
        if any(r["W"] != per_run[0]["W"] or r["O"] != per_run[0]["O"] for r in per_run):
            rec["generic_disagreement"] = per_run
        rec.update(per_run[0])
        rows.append(rec)
        log(f"A k={k}: W terms {rec['W']['terms']} maxlen {rec['W']['max_len']}; "
            f"O terms {rec['O']['terms']} maxlen {rec['O']['max_len']}; red W {rec['reductions_W']}")
    return rows


# ---------------------------------------------------------------- Part B: arb
def two_row_partitions(n):
    return [(n - b, b) if b else (n,) for b in range(0, n // 2 + 1)]


def syt(shape):
    n = sum(shape)
    out = []

    def rec(t, rows):
        m = sum(len(r) for r in rows)
        if m == n:
            out.append(tuple(tuple(r) for r in rows))
            return
        for r in range(len(shape)):
            if len(rows[r]) < shape[r] and (r == 0 or len(rows[r - 1]) > len(rows[r])):
                rows[r].append(m + 1)
                rec(t, rows)
                rows[r].pop()

    rec(None, [[] for _ in shape])
    return out


def seminormal(shape, q):
    """Matrices (columns = images) of σ_0..σ_{n-2} in the two-row seminormal form."""
    Ts = syt(shape)
    idx = {T: a for a, T in enumerate(Ts)}
    n = sum(shape)
    d = len(Ts)
    pos = []
    for T in Ts:
        p = {}
        for r, row in enumerate(T):
            for c, e in enumerate(row):
                p[e] = (r, c)
        pos.append(p)
    h = q - 1 / q
    gens = []
    for i in range(1, n):  # s_i swaps entries i, i+1  -> σ_{i-1}
        M = arb_mat(d, d)
        for a, T in enumerate(Ts):
            (r1, c1), (r2, c2) = pos[a][i], pos[a][i + 1]
            if r1 == r2:
                M[a, a] = q
            elif c1 == c2:
                M[a, a] = -1 / q
            else:
                dist = (c2 - r2) - (c1 - r1)
                ad = h / (1 - q ** (-2 * dist))
                amd = h / (1 - q ** (2 * dist))
                swapped = tuple(tuple(i + 1 if e == i else i if e == i + 1 else e for e in row) for row in T)
                b = idx[swapped]
                M[a, a] = ad
                M[b, a] = arb(1) if dist > 0 else ad * amd + 1
        gens.append(M)
    return gens


def check_rep(gens, q):
    d = gens[0].nrows()
    I = arb_mat(d, d)
    for a in range(d):
        I[a, a] = 1
    h = q - 1 / q
    worst = arb(0)
    for i, S in enumerate(gens):
        R = S * S - S * h - I
        worst = max(worst, max(abs(R[a, b]).upper() for a in range(d) for b in range(d)))
        if i + 1 < len(gens):
            T = gens[i + 1]
            B = S * T * S - T * S * T
            worst = max(worst, max(abs(B[a, b]).upper() for a in range(d) for b in range(d)))
    return worst


def atom_matrix(gens, k, phi, q):
    d = gens[0].nrows()
    h = q - 1 / q
    I = arb_mat(d, d)
    for a in range(d):
        I[a, a] = 1
    inv = [S - I * h for S in gens]
    W = I
    for j in range(1, k + 1):
        for (i, isinv) in capture_letters(j):
            W = W * (inv[i] if isinv else gens[i])
        if j >= 2:
            W = W * gens[j - 1]
            i = j - 2
            W = W * (I + gens[i] * phi[0] + gens[i + 1] * phi[1] + gens[i] * inv[i + 1] * phi[2])
    return W


def trace(M):
    s = arb(0)
    for a in range(M.nrows()):
        s += M[a, a]
    return s


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    if x == 0:
        return 0
    return None  # interval straddles 0


def part_b(kmax, grid_small, grid_large, k_small):
    q = arb(Q0_STR)
    rows = []
    for k in range(1, kmax + 1):
        n = k + 1
        shapes = two_row_partitions(n)
        reps = {}
        for sh in shapes:
            g = seminormal(sh, q)
            if g:
                err = check_rep(g, q)
                assert err < arb("1e-60"), (sh, err)
            reps[sh] = g
        grid = grid_small if k <= k_small else grid_large
        pts = []
        for phi in grid:
            ph = tuple(arb(str(x)) for x in phi)
            chis = {}
            for sh, g in reps.items():
                if not g:  # n = 1
                    continue
                chis[str(sh)] = trace(atom_matrix(g, k, ph, q))
            sg = {s: sign(v) for s, v in chis.items()}
            undecided = [s for s, v in sg.items() if v is None]
            binds = (not undecided) and all(v >= 0 for v in sg.values())
            pts.append({"phi": list(phi), "binds": binds if not undecided else None,
                        "neg_blocks": [s for s, v in sg.items() if v == -1],
                        "undecided": undecided,
                        "chi": {s: v.mid().str(12, radius=False) for s, v in chis.items()}})
        nb = sum(1 for p in pts if p["binds"])
        bare = next(p for p in pts if p["phi"] == ["0", "0", "0"])
        rows.append({"k": k, "n": n, "grid_points": len(pts), "binding_points": nb,
                     "bare_binds": bare["binds"], "bare_neg_blocks": bare["neg_blocks"],
                     "bare_chi": bare["chi"], "points": pts})
        log(f"B k={k}: binds at {nb}/{len(pts)} grid points; bare binds={bare['binds']} "
            f"neg blocks {bare['neg_blocks']}")
    return rows


def main():
    kmax_a = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    kmax_b = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    runs = [(7, 1_000_003, (11, 23, 37)), (5, 999_983, (101, 59, 3))]
    log("Part A: normal-form complexity in the full H_{k+1} over F_P")
    a = part_a(kmax_a, runs)
    vals = ["-1", "-0.5", "0", "0.5", "1"]
    grid_small = [tuple(p) for p in itertools.product(vals, repeat=3)]
    grid_large = [("0", "0", "0")] + [tuple(v if j == i else "0" for j in range(3))
                                       for i in range(3) for v in ("-1", "1")]
    log("Part B: Frobenius positivity at q0 (arb, 256 bits)")
    b = part_b(kmax_b, grid_small, grid_large, k_small=6)
    OUT.write_text(json.dumps({"model": "docs/audits/2026-11-21-magic-shells-gamma-gamma-model.md",
                               "q0": Q0_STR, "partA": a, "partB": b}, indent=1))
    log(f"wrote {OUT}")


if __name__ == "__main__":
    main()
