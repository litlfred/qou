"""Particle-indexed Gram: nucleons as nodes (issue #7895, round 5).

Question.  The strand Gram (strand_gram_jucys_murphy_probe) indexes nodes by the
strands of ONE braid.  Here the nodes are separate particles: nucleon blocks
x_i (the 11-letter per-nucleon word of build_atom_nf) on disjoint strand
windows 3i..3i+2 of H_{3A}(q).  Is there any Gram "nearness" between them, and
where does it come from?

Structural fact (corpus, Lean, sorry-free):
QOU.MathlibExt.BraidedBlockShiftTrace.tr_blockProd -- a Markov trace is
multiplicative over disjoint consecutive strand windows, and a block's trace
does not depend on its offset (tr_wordVal_shift).  Hence with no bond letter,
tr(x_i^T x_j) = tr(x_i) tr(x_j) for i != j: the connected Gram vanishes and the
particle geometry is a regular simplex fixed by species alone, at every q and
every N.  Nearness can only come from letters that straddle two windows.

Construction (stated, a choice, not derived).  A nucleus braid beta is a
product of bond letters; per the owner's one-rule ruling (2026-11-15) the bond
letter is the gamma-gamma unit V placed across the junction,
B_i = sigma_{3i+1} sigma_{3i+2}^{-1}.  P = beta^T beta is positive in every
Wedderburn block, so <a,b>_beta = tr(a^T P b)/tr(P) is a positive semidefinite
form (a state).  Particle covariance K_ij = <x_i,x_j> - <x_i,1><1,x_j>,
correlation rho_ij = K_ij / sqrt(K_ii K_jj).  Transpose = word reversal (the
Hoefsmit seminormal sigma_g are symmetric).

Reported: (1) factorisation check with no bonds (connected Gram = 0); (2)
rho for bonded chains A = 2, 3, 4 under N = 2 (convention D) and A = 2, 3 under
N = 3; whether a pair with no bond letter between it is correlated.
Mathematics only; no physical value.  mpmath, sparse exact-order traces.
"""
from __future__ import annotations

import sys
import time
from itertools import combinations
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python", "computations/substrate",
           "computations/hecke", "computations", "computations/probes"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from hoefsmit_mpmath import BlockCacheMP, seminormal_matrices_mp, chi_lambda_of_word_sparse_mp  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from y_lambda_su_n import y_lambda_su_n, partitions_of  # noqa: E402
from gamma_gamma_aggregator_convexity_probe import nucleon_block  # noqa: E402

DPS = 40
set_compute_dps(DPS)
TOL = mp.mpf("1e-30")


class Tracer:
    def __init__(self, n, q, N):
        self.n = n
        cache = BlockCacheMP(q, q - 1 / q)
        y = {tuple(k): mp.mpf(v) for k, v in y_lambda_su_n(n, q, N).items()}
        self.blocks = []
        for lam in partitions_of(n):
            lam = tuple(lam)
            if abs(y[lam]) <= TOL:
                continue
            sig, dim, _ = seminormal_matrices_mp(lam, cache=cache)
            self.blocks.append((y[lam], sig, dim))

    def tr(self, word):
        return mp.fsum(yl * chi_lambda_of_word_sparse_mp(sig, dim, word, self.n - 1)
                       for yl, sig, dim in self.blocks)


def rev(w):
    return list(reversed(w))


def V(g, h):
    """gamma-gamma unit V = sigma_g sigma_{g+1}^{-1}."""
    return [(mp.mpf(1), mp.mpf(0), g), (mp.mpf(1), -h, g + 1)]


# Bond words across the junction generator sigma_{3i+2} between windows i, i+1.
# Window i owns generators 3i, 3i+1; window i+1 owns 3i+3, 3i+4.
BOND_TYPES = {
    "V_left":  lambda i, h: V(3 * i + 1, h),                       # gens 3i+1, 3i+2
    "V_right": lambda i, h: V(3 * i + 2, h),                       # gens 3i+2, 3i+3
    "V_left^3": lambda i, h: V(3 * i + 1, h) * 3,                  # still two generators
    "V_left.V_right": lambda i, h: V(3 * i + 1, h) + V(3 * i + 2, h),   # = s_{3i+1} s_{3i+3}^{-1}
    "V_right.V_left": lambda i, h: V(3 * i + 2, h) + V(3 * i + 1, h),   # spans 3i+1..3i+3
}


def bond(i, h, kind):
    return BOND_TYPES[kind](i, h)


def analyse(tracer, species, bonds, h, log, kind="V_left"):
    A = len(species)
    x = [nucleon_block(s, h, 3 * i) for i, s in enumerate(species)]
    beta = [l for b in bonds for l in bond(b, h, kind)]
    P = rev(beta) + beta
    trP = tracer.tr(P)
    m = [tracer.tr(P + x[i]) / trP for i in range(A)]          # <1, x_i>
    mt = [tracer.tr(rev(x[i]) + P) / trP for i in range(A)]    # <x_i, 1>
    K = [[None] * A for _ in range(A)]
    for i in range(A):
        for j in range(i, A):
            g = tracer.tr(rev(x[i]) + P + x[j]) / trP
            K[i][j] = g - mt[i] * m[j]
            if j != i:
                K[j][i] = tracer.tr(rev(x[j]) + P + x[i]) / trP - mt[j] * m[i]
    rho = [[K[i][j] / mp.sqrt(K[i][i] * K[j][j]) for j in range(A)] for i in range(A)]
    asym = max(abs(K[i][j] - K[j][i]) for i in range(A) for j in range(A))
    log(f"    species {''.join(species)} bonds {bonds} ({kind}): trP = {mp.nstr(trP, 10)}, "
        f"max|K-K^T| = {mp.nstr(asym, 3)}")
    for i, j in combinations(range(A), 2):
        bonded = any(b == i and i + 1 == j for b in bonds)
        log(f"      rho({i},{j}) = {mp.nstr(rho[i][j], 12):>18}   {'bond' if bonded else 'no bond letter'}")
    return {"species": "".join(species), "bonds": bonds, "bond_type": kind, "trP": fmt(trP),
            "K": [[fmt(v) for v in r] for r in K], "rho": [[fmt(v) for v in r] for r in rho],
            "K_asymmetry": fmt(asym)}


def main() -> int:
    t0 = time.time()
    mp.mp.dps = DPS
    q = Q_MP
    h = q - 1 / q

    def log(s):
        print(s, flush=True)

    out = {}
    # (1) factorisation with no bonds
    fac = []
    for N in (2, 3):
        T = Tracer(6, q, N)
        xp, xn = nucleon_block("p", h, 0), nucleon_block("n", h, 3)
        lhs = T.tr(rev(xp) + xn)
        rhs = T.tr(xp) * T.tr(xn)
        dev = abs(lhs - rhs)
        fac.append({"N": N, "tr_xpT_xn": fmt(lhs), "tr_xp_tr_xn": fmt(rhs), "deviation": fmt(dev)})
        log(f"N={N}: tr(x_p^T x_n) = {mp.nstr(lhs, 15)}, tr(x_p)tr(x_n) = {mp.nstr(rhs, 15)}, |diff| = {mp.nstr(dev, 3)}")
    out["factorisation"] = fac

    runs = []
    plan = [(2, 6, [("p", "n")]), (2, 9, [("p", "n", "p")]), (3, 6, [("p", "n")]), (3, 9, [("p", "n", "p")]),
            (2, 12, [("p", "n", "p", "n")])]
    for N, n, specs in plan:
        A = n // 3
        log(f"\nN = {N}, A = {A} (H_{n}), wall {time.time() - t0:.0f} s")
        T = Tracer(n, q, N)
        for sp in specs:
            r = analyse(T, sp, [], h, log)
            r.update({"N": N, "A": A})
            runs.append(r)
            for kind in BOND_TYPES:
                if A == 4 and kind != "V_right.V_left":
                    continue
                r = analyse(T, sp, list(range(A - 1)), h, log, kind)
                r.update({"N": N, "A": A})
                runs.append(r)
    out["runs"] = runs
    log(f"\nwall {time.time() - t0:.0f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("particle-gram-bond-locality-probe", engine="python", start_time=t0)
    wb.set_description("Particle-indexed Gram of nucleon blocks on disjoint strand windows: "
                       "factorisation with no bonds; correlation under the state of a gamma-gamma "
                       "bond chain, N=2 (convention D) and N=3, proton pin. Mathematics only.")
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_parameter("dps", DPS)
    wb.add_data("factorisation", fac)
    wb.add_data("runs", runs)
    for f in fac:
        wb.add_assertion(name=f"disjoint_blocks_factorise_N{f['N']}", computed=f["deviation"], expected="0",
                         tolerance="1e-30", source="QOU.MathlibExt.BraidedBlockShiftTrace.tr_blockProd")
    for r in runs:
        if not r["bonds"]:
            mx = max(abs(mp.mpf(r["rho"][i][j])) for i in range(r["A"]) for j in range(r["A"]) if i != j)
            wb.add_assertion(name=f"unbonded_connected_gram_zero_N{r['N']}_A{r['A']}", computed=fmt(mx),
                             expected="0", tolerance="1e-25", source="tr_blockProd (no straddling letter)")
    path = wb.save()
    print(f"witness -> {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
