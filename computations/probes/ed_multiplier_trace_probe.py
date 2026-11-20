"""Trace the selected word along the ED approach angle gamma, H_3 gamma-gamma
family V^k, proton pin, convention D (same data as
computations/probes/collision_gradient_lagrangian_probe.py).  mpmath only.

mu(gamma) = w(gamma) * mu_star on the (2,1) channel (mu_(3) = 0), with
  peak:   w = p_n(gamma)        = cos(gamma/2)^(2n)
  kernel: w = K_n(gamma) = (n+1) cos(gamma/2)^(2n)
Selected word = argmin_k 2k - mu * chi_(2,1)(V^k)  (chi_(3) = 1 is constant).
"""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
for p in ("tools/pyhecke/python", "tools/qou-substrate/python", "computations/substrate",
          "computations/hecke", "computations", "computations/probes"):
    sys.path.insert(0, str(ROOT / p))
import mpmath as mp
from _precision import set_compute_dps
from hoefsmit_mpmath import BlockCacheMP, seminormal_matrices_mp
from q_parameter import Q_50_DIGIT_STR, Q_MP
from gamma_gamma_h3_psd_selector_probe import vertex_pow, word_image, trace

set_compute_dps(60); mp.mp.dps = 60
q = Q_MP; h = q - 1 / q
cache = BlockCacheMP(q, h)
sig, dim, _ = seminormal_matrices_mp((2, 1), cache=cache)

def chi(k):
    return trace(word_image(sig, dim, vertex_pow(0, k, h)), dim)

def analyse(kmax):
    ks = list(range(1, kmax + 1))
    x = {k: chi(k) for k in ks}
    c = {k: mp.mpf(2 * k) for k in ks}
    feas = [k for k in ks if x[k] >= 0]
    kstar = min(feas, key=lambda k: c[k])
    # mu* = best crossing edge (one binding row), as in the source probe
    cross = lambda a, b: (c[a] * x[b] - c[b] * x[a]) / (x[b] - x[a])
    _, a, b = min((cross(a, b), a, b) for a in ks if x[a] < 0 for b in feas)
    mu = (c[b] - c[a]) / (x[b] - x[a])
    # upper end of the V^kstar cell along mu > mu*
    ups = [(c[j] - c[kstar]) / (x[j] - x[kstar]) for j in ks if x[j] > x[kstar]]
    mu_up = min(ups) if ups else mp.inf
    dom = all(x[j] < x[kstar] for j in ks if j != kstar)
    return ks, x, c, kstar, mu, a, b, mu_up, dom

def sel(ks, x, c, m):
    vals = sorted((c[k] - m * x[k], k) for k in ks)
    tie = abs(vals[0][0] - vals[1][0]) < mp.mpf("1e-40")
    return vals[0][1], tie

for kmax in (10, 60):
    ks, x, c, kstar, mu, a, b, mu_up, dom = analyse(kmax)
    print(f"kmax={kmax}: ILP k*={kstar}, mu*={mp.nstr(mu, 20)} (wall V^{a}|V^{b}); "
          f"V^{kstar} dominant reading: {dom}; V^{kstar} cell = (mu*, {mp.nstr(mu_up, 12)})"
          f" = (1, {mp.nstr(mu_up / mu, 12)}) * mu*")
    if kmax == 60 and not dom:
        top = max(ks, key=lambda k: x[k])
        print(f"   largest reading at kmax=60: V^{top}, chi={mp.nstr(x[top], 15)} vs chi(V^{kstar})={mp.nstr(x[kstar], 15)}")

ks, x, c, kstar, mu, a, b, mu_up, dom = analyse(10)
print()
for n in (3, 10, 100):
    N = mp.mpf(n)
    gs = 2 * mp.acos((N + 1) ** (-1 / (2 * N)))           # exact K_n = 1
    lean_in = 2 / mp.sqrt(N + 1)                            # (n+1) g^2 < 4
    lean_out = (32 / (N - 1)) ** mp.mpf("0.25")             # 32 < (n-1) g^4
    print(f"n={n:3d}: switch angle K_n(g)=1 at g_s = {mp.nstr(gs, 15)} rad"
          f"  (sqrt(4 ln(n+1)/n) = {mp.nstr(mp.sqrt(4 * mp.log(N + 1) / N), 6)});"
          f" Lean inner {mp.nstr(lean_in, 6)}, Lean outer {mp.nstr(lean_out, 6)}"
          f"{'' if lean_out <= mp.pi else ' (> pi: vacuous)'}")
    seq_k, seq_p = [], []
    for i in range(0, 41):
        g = mp.pi * i / 40
        p = mp.cos(g / 2) ** (2 * n)
        sk, tk = sel(ks, x, c, (N + 1) * p * mu)
        sp, tp = sel(ks, x, c, p * mu)
        seq_k.append(f"{sk}{'*' if tk else ''}"); seq_p.append(f"{sp}{'*' if tp else ''}")
    print("   kernel  word on g = 0..pi step pi/40:", " ".join(seq_k))
    print("   peak    word on g = 0..pi step pi/40:", " ".join(seq_p))
    print(f"   K_n(0) mu* = {mp.nstr((N + 1) * mu, 10)} vs cell top {mp.nstr(mu_up, 10)}")
print("\n'*' = tie (wall).")
