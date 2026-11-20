"""Strand-indexed Gram matrix from Jucys-Murphy elements (issue #7895, option B).

Particles = strands.  The JM element L_k = sigma_{k-1}...sigma_1 sigma_1...sigma_{k-1}
is diagonal in the Hoefsmit seminormal basis with eigenvalue q^(2 c_T(k)) on the
tableau T (c = content of the box holding k).  The trace form gives the strand
Gram matrix

    G_kl = tau(L_k L_l) = sum_lambda y_lambda sum_T q^(2 c_T(k)) q^(2 c_T(l)),

a Gram matrix of the vectors v_k = (sqrt(y_lambda) q^(2 c_T(k)))_{lambda,T}, so PSD
and a Euclidean distance (Lean GramNearness).  Reported: the JM eigenvalue check
against the Hoefsmit matrices (n = 3, 4), the rank (embedding dimension) and the
strand distances under N = 2 (convention D) and N = 3, and their q -> 1 collapse.
Mathematics only; no physical value.  mpmath 60 dps.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python", "computations/substrate",
           "computations/hecke", "computations", "computations/probes"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from hoefsmit_mpmath import BlockCacheMP, seminormal_matrices_mp  # noqa: E402
from hecke_characters import standard_young_tableaux  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from y_lambda_su_n import y_lambda_su_n, partitions_of  # noqa: E402

DPS = 60
set_compute_dps(DPS)
TOL = mp.mpf("1e-40")


def jm_check(n, q):
    """max |rho(L_k) - diag(q^(2c))| over shapes of n, via Hoefsmit matrices."""
    cache = BlockCacheMP(q, q - 1 / q)
    dev = mp.mpf(0)
    for lam in partitions_of(n):
        lam = tuple(lam)
        sig, dim, syts = seminormal_matrices_mp(lam, cache=cache)
        _, cells, contents = standard_young_tableaux(lam)
        for k in range(1, n + 1):
            L = mp.eye(dim)
            for g in range(k - 2, -1, -1):
                L = L * sig[g]
            for g in range(0, k - 1):
                L = L * sig[g]
            # L_k = s_{k-1}...s_1 s_1...s_{k-1}: build as product in that order
            L = mp.eye(dim)
            for g in list(range(k - 2, -1, -1)) + list(range(0, k - 1)):
                L = L * sig[g]
            for i in range(dim):
                c = contents[syts[i][k]]
                for jx in range(dim):
                    target = q ** (2 * c) if i == jx else 0
                    dev = max(dev, abs(L[i, jx] - target))
    return dev


def strand_vectors(n, q, N):
    y = {tuple(k): mp.mpf(v) for k, v in y_lambda_su_n(n, q, N).items()}
    vecs = [[] for _ in range(n)]
    for lam in partitions_of(n):
        lam = tuple(lam)
        if y[lam] <= TOL:
            continue
        syts, cells, contents = standard_young_tableaux(lam)
        s = mp.sqrt(y[lam])
        for T in syts:
            for k in range(1, n + 1):
                vecs[k - 1].append(s * q ** (2 * contents[T[k]]))
    return vecs


def gram_rank_and_dist(vecs):
    n = len(vecs)
    G = mp.matrix(n, n)
    for a in range(n):
        for b in range(n):
            G[a, b] = mp.fsum(x * z for x, z in zip(vecs[a], vecs[b]))
    ev = mp.eigsy(G)[0]
    top = max(abs(e) for e in ev)
    rank = sum(1 for e in ev if abs(e) > top * mp.mpf("1e-30"))
    D = [[mp.sqrt(max(G[a, a] + G[b, b] - 2 * G[a, b], 0)) for b in range(n)] for a in range(n)]
    return rank, D, sorted(ev, reverse=True)


def centred_spectrum(vecs):
    """Eigenvalues of the doubly centred Gram (Schoenberg -1/2 J D^2 J) and the
    participation ratio (sum ev)^2 / sum ev^2 = effective embedding dimension."""
    n = len(vecs)
    dim = len(vecs[0])
    mean = [mp.fsum(v[t] for v in vecs) / n for t in range(dim)]
    cen = [[v[t] - mean[t] for t in range(dim)] for v in vecs]
    G = mp.matrix(n, n)
    for a in range(n):
        for b in range(n):
            G[a, b] = mp.fsum(x * z for x, z in zip(cen[a], cen[b]))
    ev = sorted([e for e in mp.eigsy(G)[0]], reverse=True)
    ev = [e if e > 0 else mp.mpf(0) for e in ev]
    pr = mp.fsum(ev) ** 2 / mp.fsum(e * e for e in ev)
    return ev, pr


def main() -> int:
    t0 = time.time()
    mp.mp.dps = DPS
    q = Q_MP
    dev3, dev4 = jm_check(3, q), jm_check(4, q)
    print(f"JM eigenvalue check vs Hoefsmit: n=3 {mp.nstr(dev3, 3)}, n=4 {mp.nstr(dev4, 3)}")
    rows = []
    for N in (2, 3):
        print(f"\nN = {N}")
        print(f"{'n':>3} {'rank':>5}  d(1,2)/log q   d(1,n)/log q   top eigenvalues")
        for n in range(2, 9):
            vecs = strand_vectors(n, q, N)
            rank, D, ev = gram_rank_and_dist(vecs)
            lq = mp.log(q)
            rows.append({"N": N, "n": n, "rank": rank,
                         "d12_over_logq": fmt(D[0][1] / lq), "d1n_over_logq": fmt(D[0][n - 1] / lq),
                         "eigenvalues": [fmt(e) for e in ev]})
            print(f"{n:3d} {rank:5d}  {mp.nstr(D[0][1] / lq, 8):>12}   {mp.nstr(D[0][n - 1] / lq, 8):>12}   "
                  + ", ".join(mp.nstr(e, 4) for e in ev[:4]))
    # effective dimension of the strand configuration, by q regime
    print("\nEffective embedding dimension (participation ratio of the centred Gram), n = 8:")
    eff = []
    for qs in ("1.01", "1.05", Q_50_DIGIT_STR, "1.3", "1.6", "2", "3"):
        qq = mp.mpf(qs)
        for N in (2, 3):
            ev, pr = centred_spectrum(strand_vectors(8, qq, N))
            eff.append({"q": qs[:12], "N": N, "participation_ratio": fmt(pr),
                        "top_centred_eigenvalues": [fmt(e) for e in ev[:4]]})
            print(f"  q={qs[:10]:>10} N={N}: PR = {mp.nstr(pr, 6)}   top centred ev ratios "
                  + ", ".join(mp.nstr(e / ev[0], 3) for e in ev[:4]))

    # q -> 1 collapse
    q1 = 1 + mp.mpf("1e-20")
    _, D1, _ = gram_rank_and_dist(strand_vectors(5, q1, 2))
    dmax1 = max(max(r) for r in D1)
    r1 = int(dmax1 < mp.mpf("1e-18"))
    print(f"\nq = 1 + 1e-20, n = 5, N = 2: max strand distance {mp.nstr(dmax1, 3)} (collapse to a point as q -> 1)")
    print(f"  wall {time.time() - t0:.1f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("strand-gram-jucys-murphy-probe", engine="python", start_time=t0)
    wb.set_description("Strand-indexed Gram matrix tau(L_k L_l) of Jucys-Murphy elements under the "
                       "N=2 (convention D) and N=3 Markov traces at the proton pin: rank (embedding "
                       "dimension) and strand distances; collapse at q=1. Mathematics only.")
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_parameter("dps", DPS)
    wb.add_data("rows", rows)
    wb.add_data("q_near_one_n5_max_distance", fmt(dmax1))
    wb.add_data("effective_dimension_n8", eff)
    wb.add_assertion(name="jm_diagonal_n3", computed=fmt(dev3), expected="0", tolerance="1e-45",
                     source="JM elements act by q^(2 content) in the seminormal basis")
    wb.add_assertion(name="jm_diagonal_n4", computed=fmt(dev4), expected="0", tolerance="1e-45",
                     source="JM elements act by q^(2 content) in the seminormal basis")
    wb.add_assertion(name="q_to_one_collapses_to_a_point", computed=str(r1), expected="1",
                     tolerance="0", source="q^(2c) -> 1 for every content as q -> 1")
    out = wb.save()
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
