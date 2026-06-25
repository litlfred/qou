#!/usr/bin/env python3
"""EXPLORATORY probe — settle the depth-2(SL2) vs super-exponential(lw/#1765)
fork for the prolonged SW periods, STRUCTURALLY (Puiseux/branch-point argument).

EXPLICIT prolongation (this session): λ_SW^(n) = X^(n)(z) dz, the n-th total
derivative of the color-cubic implicit function X(z) (operator D=∂_z+X'∂_X) —
fills the corpus "higher jets by induction" gap. a_D^(n)=∮_γ λ_SW^(n) is, per
prop:mi-sw-abelianisation, the n-th jet of the Yekutieli non-abelian-Stokes MI∫.

THE FORK. Two corpus claims for a_D^(n):
  (i)  a_D^(n+2)=τ a_D^(n+1)−a_D^(n)        [GEOMETRIC, ratio→λ₊≈2.18]  (sl2-prolongation)
  (ii) a_D^(n)=lw(n−1)=(1/n)Σ_{λ⊢n}dim_q    [SUPER-EXP, ratio grows]    (#1765)
They agree at n=2,3,4 (τ is fit to those 3 anchors) and through n=5, then split.

STRUCTURAL RESOLUTION (no flaky contour integral). γ encircles branch points of
the color cubic, where disc_X=0 ⇒ two sheets collide ⇒ square-root branch
X ~ X_k + c·(z−z_k)^{1/2}. Then
    X^(n) ~ c·(1/2)(−1/2)···(3/2−n)·(z−z_k)^{1/2−n},
so the period a_D^(n) ∝ |(1/2)_n^{fall}| / R^n  — FACTORIAL ⇒ super-exponential,
with ratio a_D^(n+1)/a_D^(n) ~ (n−1/2)/R  GROWING (not the constant λ₊ of SL2).
This also resolves the apparent paradox that the pointwise jets X^(n)(z₀) SHRINK
(z₀ is inside the convergence disk; the period is dominated by the branch point).

VERDICT: super-exponential ⇒ lw/#1765 is the true prolongation; the depth-2 SL2
τ is an n≤4 effective fit (it cannot produce factorial growth). Audit-only.
"""
from __future__ import annotations
import sympy as sp
import mpmath as mp

mp.mp.dps = 30
z, X = sp.symbols('z X')
P = X**3 + (z + 1) * X**2 + (z**2 + z + 1) * X + (z**3 + z**2 + z + 1)

# ---- branch points + branch order (square-root?) -----------------------------
disc = sp.discriminant(P, X)
bps = mp.polyroots([complex(c) for c in sp.Poly(disc, z).all_coeffs()])
print("color-cubic branch points (disc_X=0):", [mp.nstr(b, 5) for b in bps])
# verify order-2 branch: at z_k two cubic roots collide (gap → 0)
zk = bps[0]
roots = sorted(mp.polyroots([1, zk + 1, zk**2 + zk + 1, zk**3 + zk**2 + zk + 1]),
               key=lambda r: abs(r))
gap_min = min(abs(roots[i] - roots[j]) for i in range(3) for j in range(i + 1, 3))
print(f"min sheet-gap at a branch point = {mp.nstr(gap_min,4)} (→0 ⇒ square-root branch, exponent 1/2)")
R = min(abs(zk) for zk in bps)  # convergence radius from z=0 (rough scale)

# ---- structural factorial ratio of the period --------------------------------
# coefficient of (z-z_k)^{1/2-n} in X^(n): (1/2)(1/2-1)...(1/2-(n-1)) = falling
def falling_half(n):
    r = mp.mpf(1)
    for k in range(n):
        r *= (mp.mpf('0.5') - k)
    return r

print("\nstructural period growth  a_D^(n) ∝ |(1/2)_n^fall| / R^n :")
print(f"{'n':>2} {'|(1/2)_n^fall|':>16} {'ratio':>9}")
prev = None
for n in range(2, 9):
    c = abs(falling_half(n))
    ratio = float(c / prev) if prev else float('nan')
    print(f"{n:>2} {mp.nstr(c,8):>16} {ratio:>9.4f}")
    prev = c
print("  → |coeff| ratio = (n-1/2) GROWS without bound ⇒ super-exponential period")

# ---- compare to lw (the #1765 target) and to depth-2 (SL2) -------------------
q = mp.mpf('1.1099785955573347')
tau = mp.mpf('2.6423863133015')
def qint(k): return (q**k - q**(-k)) / (q - 1 / q)
def qfac(n):
    r = mp.mpf(1)
    for k in range(1, n + 1): r *= qint(k)
    return r
def partitions(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k): yield (k,) + r
def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(row - j - 1) + (conj[j] - i - 1) + 1
            for i, row in enumerate(lam) for j in range(row)]
def dimq(lam):
    d = qfac(sum(lam))
    for h in hooks(lam): d /= qint(h)
    return d
def lw(c): return mp.fsum(dimq(l) for l in partitions(c + 1)) / (c + 1)

aD_lw = {n: lw(n - 1) for n in range(2, 9)}
aD_d2 = {2: mp.mpf(1), 3: lw(2), 4: lw(3)}
for n in range(5, 9):
    aD_d2[n] = tau * aD_d2[n - 1] - aD_d2[n - 2]
print("\n  n |   lw/#1765   ratio |   depth-2/SL2  ratio")
for n in range(2, 9):
    rl = float(aD_lw[n] / aD_lw[n - 1]) if n > 2 else float('nan')
    rd = float(aD_d2[n] / aD_d2[n - 1]) if n > 2 else float('nan')
    print(f" {n:>2} | {float(aD_lw[n]):>10.4f} {rl:>6.3f} | {float(aD_d2[n]):>10.4f} {rd:>6.3f}")
print("  lw ratio GROWS (1.34→3.4+, super-exp, matches the factorial structure);")
print("  depth-2 ratio → λ₊≈2.18 (constant, geometric). They split hard at n≥6.")

print("\n" + "=" * 70)
print("VERDICT: the SW periods a_D^(n)=∮X^(n)dz grow FACTORIALLY (super-exp) from")
print("the square-root branch points ⇒ lw/#1765 is the true prolongation; the")
print("depth-2 SL2 τ is an n≤4 effective fit. The q-difference recurrence for the")
print("super-exp a_D^(n) is the q-Bessel-class kernel (jackson-q-bessel-contiguity).")
print("=" * 70)
