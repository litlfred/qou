"""Exact Wedderburn block weights of the canonical Markov trace.

Resolves the open question flagged on PR #3661/#3670: what is the
closed form of the block weights w_lambda = tr_M(p_lambda) for the
canonical Markov trace on H_n(q) with

    tr_M(1) = 1,   tr_M(x sigma_n) = z tr_M(x),
    z = 1/(q^{1/2} + q^{-1/2}),

Hecke relation sigma^2 = (q - q^{-1}) sigma + 1 (eigenvalues q, -q^{-1})?

Neither of the two forms previously written in the corpus
(dim_q(lambda) d_lambda / [n]_q!  in markov-trace-frobenius-selection-proof,
dim_q^2(lambda) / [n]_q!          in trace-locality-meets-gs-nonlocality-proof)
matches tr_M(e_+) = (z + q^{-1})/(q + q^{-1}) at n = 2.

Method (exact, no floats):
  1. Build the Hoefsmit seminormal representations rho_lambda of
     H_n(q) over Fraction for rational s = q^{1/2} samples,
     self-validated against the braid, far-commutativity, and Hecke
     relations for every generator pair and every lambda |- n.
  2. Build the Hecke algebra product on the T_w basis and evaluate
     the canonical Markov trace by the Ocneanu peel recursion.
  3. Solve  sum_lambda w_lambda chi_lambda(T_w) = tr_M(T_w)  exactly.
  4. Test the candidate closed form (2-variable quantum dimension,
     hook-content shape)

         w_lambda = prod_{cells x} (a s^{2 c(x)} - a^{-1} s^{-2 c(x)})
                                   / (s^{2 h(x)} - s^{-2 h(x)})
                    normalised by D^{|lambda|},
         D = (a - a^{-1})/(s^2 - s^{-2}),

     with a^2 solved exactly from the n = 2 weights, at every
     lambda |- n <= N_MAX and every rational s sample.

Witness: markov-trace-weights-wenzl.witness.json
"""

from __future__ import annotations

import itertools
import json
import os
import subprocess
import sys
import time
from fractions import Fraction
from hashlib import sha256

N_MAX = 5
S_SAMPLES = [Fraction(3, 2), Fraction(7, 5), Fraction(13, 9)]

# ---------------------------------------------------------------- tableaux


def partitions(n):
    if n == 0:
        yield ()
        return
    def helper(n, maxpart):
        if n == 0:
            yield ()
            return
        for first in range(min(n, maxpart), 0, -1):
            for rest in helper(n - first, first):
                yield (first,) + rest
    yield from helper(n, n)


def standard_tableaux(shape):
    """All SYT of the given shape, each as a dict entry -> (row, col)."""
    n = sum(shape)
    def grow(placed, k):
        if k > n:
            yield dict(placed)
            return
        row_len = [0] * len(shape)
        for (r, c) in placed.values():
            row_len[r] = max(row_len[r], c + 1)
        for r in range(len(shape)):
            c = row_len[r]
            if c < shape[r] and (r == 0 or row_len[r - 1] > c):
                placed[k] = (r, c)
                yield from grow(placed, k + 1)
                del placed[k]
    yield from grow({}, 1)


def content(pos):
    r, c = pos
    return c - r


def hooks(shape):
    """Hook length of every cell."""
    cols = [0] * (shape[0] if shape else 0)
    for r, ln in enumerate(shape):
        for c in range(ln):
            cols[c] += 1
    out = {}
    for r, ln in enumerate(shape):
        for c in range(ln):
            out[(r, c)] = (ln - c) + (cols[c] - r) - 1
    return out


# ------------------------------------------------- seminormal representation


def seminormal_rep(shape, q):
    """Matrices rho(sigma_k), k = 1..n-1, on the SYT basis (exact Fractions).

    Convention: sigma^2 = (q - q^{-1}) sigma + 1.
    On the (T, s_k T) plane with axial distance d = c(k+1) - c(k):
      diagonal  a1 = (q - q^{-1})/(1 - q^{-2d}),
                a2 = (q - q^{-1})/(1 - q^{ 2d}),
      off-diag  b = 1, c = a1*a2 + 1   (so det = -1, trace = q - q^{-1}).
    Same row (d = 1): eigenvalue q; same column (d = -1): eigenvalue -1/q.
    """
    tabs = list(standard_tableaux(shape))
    index = {tuple(sorted(t.items())): i for i, t in enumerate(tabs)}
    n = sum(shape)
    qi = 1 / q
    mats = {}
    dim = len(tabs)
    for k in range(1, n):
        M = [[Fraction(0)] * dim for _ in range(dim)]
        for i, T in enumerate(tabs):
            d = content(T[k + 1]) - content(T[k])
            if d == 1:
                M[i][i] += q
                continue
            if d == -1:
                M[i][i] += -qi
                continue
            Ts = dict(T)
            Ts[k], Ts[k + 1] = T[k + 1], T[k]
            j = index[tuple(sorted(Ts.items()))]
            qd = q ** (2 * d)
            a1 = (q - qi) / (1 - 1 / qd)
            if i < j:
                a2 = (q - qi) / (1 - qd)
                M[i][i] += a1
                M[i][j] += 1
                M[j][i] += a1 * a2 + 1
                M[j][j] += a2
        mats[k] = M
    return tabs, mats


def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    out = [[Fraction(0)] * p for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        for k in range(m):
            a = Ai[k]
            if a:
                Bk = B[k]
                oi = out[i]
                for j in range(p):
                    oi[j] += a * Bk[j]
    return out


def validate_rep(shape, q, mats, dim):
    """Assert Hecke quadratic, braid, and far-commutativity relations."""
    qi = 1 / q
    ident = [[Fraction(int(i == j)) for j in range(dim)] for i in range(dim)]
    ks = sorted(mats)
    for k in ks:
        M = mats[k]
        lhs = mat_mul(M, M)
        rhs = [[(q - qi) * M[i][j] + ident[i][j] for j in range(dim)] for i in range(dim)]
        assert lhs == rhs, f"Hecke relation fails: shape={shape}, k={k}"
    for k in ks:
        for l in ks:
            if l == k + 1:
                lhs = mat_mul(mat_mul(mats[k], mats[l]), mats[k])
                rhs = mat_mul(mat_mul(mats[l], mats[k]), mats[l])
                assert lhs == rhs, f"braid relation fails: shape={shape}, k={k}"
            if l > k + 1:
                assert mat_mul(mats[k], mats[l]) == mat_mul(mats[l], mats[k]), \
                    f"far-commutativity fails: shape={shape}, ({k},{l})"


# --------------------------------------------------------- Hecke algebra H_n


def permutations_words(n):
    """Every w in S_n as (permutation tuple) -> one reduced word."""
    def perm_of_word(word):
        p = list(range(n))
        for k in word:
            p[k - 1], p[k] = p[k], p[k - 1]
        return tuple(p)
    seen = {tuple(range(n)): ()}
    frontier = [()]
    while frontier:
        new = []
        for word in frontier:
            for k in range(1, n):
                w2 = word + (k,)
                p = perm_of_word(w2)
                if p not in seen:
                    seen[p] = w2
                    new.append(w2)
        frontier = new
    return seen  # perm -> reduced word


class Hecke:
    """H_n(q) on the T_w basis, exact coefficients."""

    def __init__(self, n, q):
        self.n, self.q, self.qi = n, q, 1 / q
        self.words = permutations_words(n)          # perm -> reduced word
        self.perm_by_word = {w: p for p, w in self.words.items()}

    def right_mul_gen(self, elt, k):
        """elt * T_{sigma_k}; elt is dict perm -> coeff."""
        out = {}
        for p, c in elt.items():
            lp = list(p)
            longer = lp[k - 1] < lp[k]
            lp[k - 1], lp[k] = lp[k], lp[k - 1]
            p2 = tuple(lp)
            if longer:
                out[p2] = out.get(p2, Fraction(0)) + c
            else:
                # T_w T_k = (q - q^-1) T_w + T_{w s_k}   (length drops)
                out[p] = out.get(p, Fraction(0)) + c * (self.q - self.qi)
                out[p2] = out.get(p2, Fraction(0)) + c
        return {p: c for p, c in out.items() if c}

    def basis_elt(self, word):
        elt = {tuple(range(self.n)): Fraction(1)}
        for k in word:
            elt = self.right_mul_gen(elt, k)
        return elt


def markov_trace(n, q, hecke_cache):
    """tr_M(T_w) for every w in S_n, by the Ocneanu peel recursion."""
    s2 = q            # q = s^2; z = 1/(s + 1/s) with s = sqrt(q): needs s!
    raise RuntimeError("use markov_trace_s")


def markov_trace_s(n, s, hecke_by_level):
    """tr values, exact in s (q = s^2, z = 1/(s + 1/s))."""
    q = s * s
    z = 1 / (s + 1 / s)
    tr = {1: {(0,): Fraction(1)}}
    # represent perms at each level m as tuples of length m
    tr_level = {1: {tuple([0]): Fraction(1)}}
    for m in range(2, n + 1):
        H = hecke_by_level[m]
        Hprev = hecke_by_level[m - 1]
        prev = tr_level[m - 1]
        cur = {}

        def embed(p):  # S_{m-1} perm -> S_m perm
            return tuple(list(p) + [m - 1])

        def tr_elt_prev(elt):
            """trace of an H_{m-1} element given as perm->coeff (level m-1)."""
            return sum(c * prev[p] for p, c in elt.items())

        for p, word in H.words.items():
            top = [i for i, k in enumerate(word) if k == m - 1]
            if not top:
                # w in S_{m-1}
                cur[p] = prev[p[:-1]]
                continue
            if len(top) == 1:
                i = top[0]
                x_word, y_word = word[:i], word[i + 1:]
                # tr(T_x T_{m-1} T_y) = z tr_{m-1}(T_y T_x)
                elt = Hprev.basis_elt(y_word + x_word)
                cur[p] = z * tr_elt_prev(elt)
                continue
            # more than one occurrence of the top generator in this reduced
            # word: rewrite via Hecke arithmetic — compute T_w explicitly as
            # a product and peel linearly. Fall back: multiply out in H_m
            # then use linearity over basis elements already computed.
            cur[p] = None
        # second pass for the |top| > 1 leftovers via linear extension:
        # T_w = T_{w'} T_k for the last letter k; use tr linearity on the
        # product expansion (both terms have strictly fewer top letters
        # after reduction, or are already resolved).
        changed = True
        while changed:
            changed = False
            for p, word in H.words.items():
                if cur[p] is not None:
                    continue
                *init, k = word
                elt = H.basis_elt(tuple(init))       # resolved shorter word
                expanded = H.right_mul_gen(elt, k)   # dict perm -> coeff
                if all(cur[pp] is not None or pp == p for pp in expanded):
                    # solve: tr(T_w) appears with coeff of p in expanded
                    # expanded == T_w exactly (basis element), so all
                    # component perms have known traces except possibly p
                    # itself with coefficient 1.
                    total = Fraction(0)
                    ok = True
                    for pp, c in expanded.items():
                        if pp == p:
                            continue
                        if cur[pp] is None:
                            ok = False
                            break
                        total += c * cur[pp]
                    if not ok:
                        continue
                    # expanded = 1 * T_p + (rest): tr(T_p) needs tr of
                    # the full product, which is NOT directly known here.
                    # This branch is unreachable for reduced words chosen
                    # by BFS (their last letter yields |top| <= 1 after
                    # the split) — assert loudly if hit.
                    raise AssertionError(
                        f"unresolvable word {word} at level {m}")
        tr_level[m] = cur
    return tr_level[n], q, z


# ------------------------------------------------------------------- solve


def solve_weights(n, s):
    hecke_by_level = {m: Hecke(m, s * s) for m in range(1, n + 1)}
    tr, q, z = markov_trace_s(n, s, hecke_by_level)
    H = hecke_by_level[n]
    shapes = [sh for sh in partitions(n)]
    chars = {}
    for sh in shapes:
        tabs, mats = seminormal_rep(sh, q)
        validate_rep(sh, q, mats, len(tabs))
        chars[sh] = {}
        for p, word in H.words.items():
            dim = len(tabs)
            M = [[Fraction(int(i == j)) for j in range(dim)] for i in range(dim)]
            for k in word:
                M = mat_mul(M, mats[k])
            chars[sh][p] = sum(M[i][i] for i in range(dim))
    # least-structure exact solve: pick #shapes independent equations
    perms = list(H.words)
    import itertools as it
    rows, rhs, used = [], [], []
    for p in perms:
        cand = [chars[sh][p] for sh in shapes]
        test = rows + [cand]
        if exact_rank(test) > len(rows):
            rows.append(cand)
            rhs.append(tr[p])
            used.append(p)
        if len(rows) == len(shapes):
            break
    sol = exact_solve(rows, rhs)
    # verify against EVERY basis element
    for p in perms:
        assert sum(sol[i] * chars[sh][p] for i, sh in enumerate(shapes)) == tr[p], \
            f"weight solution fails to reproduce tr on {p}"
    return dict(zip(shapes, sol)), q, z


def exact_rank(rows):
    m = [row[:] for row in rows]
    rank = 0
    cols = len(m[0]) if m else 0
    for c in range(cols):
        piv = next((r for r in range(rank, len(m)) if m[r][c] != 0), None)
        if piv is None:
            continue
        m[rank], m[piv] = m[piv], m[rank]
        pv = m[rank][c]
        m[rank] = [x / pv for x in m[rank]]
        for r in range(len(m)):
            if r != rank and m[r][c] != 0:
                f = m[r][c]
                m[r] = [a - f * b for a, b in zip(m[r], m[rank])]
        rank += 1
    return rank


def exact_solve(rows, rhs):
    n = len(rows)
    aug = [rows[i][:] + [rhs[i]] for i in range(n)]
    for c in range(n):
        piv = next(r for r in range(c, n) if aug[r][c] != 0)
        aug[c], aug[piv] = aug[piv], aug[c]
        pv = aug[c][c]
        aug[c] = [x / pv for x in aug[c]]
        for r in range(n):
            if r != c and aug[r][c] != 0:
                f = aug[r][c]
                aug[r] = [a - f * b for a, b in zip(aug[r], aug[c])]
    return [aug[i][n] for i in range(n)]


# --------------------------------------------------------- candidate formula


def candidate_weight(shape, s, a2):
    """w_lambda = prod_cells (a s^{2c} - a^{-1} s^{-2c})
                            / (s^{2h} - s^{-2h}),  divided by D^{|lambda|},
       expressed purely in a^2 (so no square roots needed):
       each cell factor / D  =  (a2 s^{2c} - s^{-2c}) (s^2 - s^{-2})
                                / ((a2 - 1)(s^{2h} - s^{-2h})).
    """
    hk = hooks(shape)
    out = Fraction(1)
    for pos, h in hk.items():
        c = content(pos)
        num = (a2 * s ** (2 * c) - s ** (-2 * c)) * (s ** 2 - s ** (-2))
        den = (a2 - 1) * (s ** (2 * h) - s ** (-2 * h))
        out *= num / den
    return out


def final_weight(shape, q, z, z_neg):
    """The identified closed form, square-root-free:

       w_lambda = prod_{cells x} (z q^{c(x)} - z_- q^{-c(x)})
                                 / (q^{h(x)} - q^{-h(x)}),

       with z_- = z - (q - q^{-1}) the negative-crossing loop value.
    """
    hk = hooks(shape)
    out = Fraction(1)
    for pos, h in hk.items():
        c = content(pos)
        out *= (z * q ** c - z_neg * q ** (-c)) / (q ** h - q ** (-h))
    return out


def main():
    t0 = time.time()
    results = {}
    all_match = True
    for s in S_SAMPLES:
        weights_by_n = {}
        for n in range(2, N_MAX + 1):
            w, q, z = solve_weights(n, s)
            weights_by_n[n] = w
            print(f"s={s} n={n}: solved {len(w)} block weights "
                  f"[{time.time()-t0:.1f}s]", flush=True)
        # fit a^2 from n=2:  w2/w11 = (a2 s^2 - s^-2)/(a2 s^-2 - s^2)
        w2 = weights_by_n[2][(2,)]
        w11 = weights_by_n[2][(1, 1)]
        r = w2 / w11
        a2 = (s ** (-2) - r * s ** 2) / (s ** 2 - r * s ** (-2))
        # identified closed form: a^2 = z / z_-  with z_- = z - (q - q^{-1})
        q = s * s
        z = 1 / (s + 1 / s)
        z_neg = z - (q - 1 / q)
        a2_closed = z / z_neg
        sample = {
            "s": str(s),
            "a2_fitted": str(a2),
            "a2_closed_form_z_over_z_minus": str(a2_closed),
            "a2_matches_closed_form": a2 == a2_closed,
            "per_lambda": {},
        }
        all_match = all_match and (a2 == a2_closed)
        for n in range(2, N_MAX + 1):
            for sh, w in weights_by_n[n].items():
                pred = final_weight(sh, q, z, z_neg)
                ok = (pred == w)
                all_match = all_match and ok
                sample["per_lambda"][str(sh)] = {
                    "weight": str(w), "formula": str(pred), "match": ok}
        results[str(s)] = sample
        print(f"s={s}: a2={a2}  a2==z/z_-: {a2 == a2_closed}", flush=True)

    n_checked = sum(len(v["per_lambda"]) for v in results.values())
    verdict = ("closed form CONFIRMED exactly at all sampled rational s, "
               "all lambda |- n <= %d" % N_MAX) if all_match else \
              "closed form REFUTED at some sample (see per_lambda)"
    print(verdict)

    here = os.path.dirname(os.path.abspath(__file__))
    src = open(os.path.abspath(__file__), "rb").read()
    try:
        sha = subprocess.run(
            ["git", "log", "-1", "--format=%H", "--",
             os.path.abspath(__file__)],
            capture_output=True, text=True, cwd=here).stdout.strip()
    except Exception:
        sha = ""
    witness = {
        "$schema": "witness/v1",
        "computation": "markov-trace-weights-wenzl",
        "description": (
            "Exact block weights of the canonical Markov trace "
            "(tr(1)=1, tr(x sigma_n)=z tr(x), z=1/(q^{1/2}+q^{-1/2})) on "
            "H_n(q), n<=%d, at rational s=q^{1/2} samples; identified "
            "hook-content closed form w_lambda = prod_cells "
            "(z q^{c} - z_- q^{-c})/(q^{h} - q^{-h}) with "
            "z_- = z - (q - q^{-1}), equivalently the Ocneanu/HOMFLY "
            "quantum-dimension form at framing parameter a^2 = z/z_-, "
            "tested for exact equality." % N_MAX),
        "inputs": {"N_MAX": N_MAX, "s_samples": [str(x) for x in S_SAMPLES]},
        "results": results,
        "n_lambda_checked": n_checked,
        "all_match": all_match,
        "verdict": verdict,
        "scriptHash": sha256(src).hexdigest()[:12],
        "scriptCommitSha": sha,
    }
    out = os.path.join(here, "markov-trace-weights-wenzl.witness.json")
    with open(out, "w") as fh:
        json.dump(witness, fh, indent=2)
        fh.write("\n")
    print("witness written:", out)
    return 0 if all_match else 1


if __name__ == "__main__":
    sys.exit(main())
