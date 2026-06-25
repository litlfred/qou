#!/usr/bin/env python3
"""EXPLORATORY probe — settle the depth-2 (SL2) vs super-exponential (lw/#1765) fork.

The prolonged SW periods a_D^(n) = ∮ λ_SW^(n) appear under TWO incompatible
corpus claims:
  (i)  sl2-prolongation-recurrence:  a_D^(n+2) = τ a_D^(n+1) − a_D^(n)   [GEOMETRIC, λ₊≈2.18]
  (ii) #1765 identity:               a_D^(n) = lw(n−1) = (1/n)Σ_{λ⊢n} dim_q  [SUPER-EXP]
They agree at n=2,3,4 (τ is fit to those anchors) and through n=5, then split.

This probe makes λ_SW^(n) = X^(n)(z) dz explicit (iterated implicit derivative
of the color cubic) and numerically integrates the periods over a branch cycle,
then asks: do |a_D^(n)| grow GEOMETRICALLY (→ depth-2/SL2 is the true structure)
or SUPER-EXPONENTIALLY (→ lw/#1765 is the true structure; SL2 is an n≤4 fit)?

No production change; audit-only.
"""
from __future__ import annotations
import sympy as sp
import mpmath as mp

mp.mp.dps = 30
NMAX = 7

# ---- color cubic P(X,z)=0 (mi-sw-abelianisation-cartan) and the jets X^(n) ----
z, X = sp.symbols('z X')
P = X**3 + (z + 1) * X**2 + (z**2 + z + 1) * X + (z**3 + z**2 + z + 1)
Pz, PX = sp.diff(P, z), sp.diff(P, X)
Xp = sp.cancel(-Pz / PX)                      # X'(z)
D = lambda f: sp.cancel(sp.diff(f, z) + sp.diff(f, X) * Xp)   # total derivative
jets = [X, Xp]                                # X^(0)=X, X^(1)=X'
for n in range(2, NMAX + 1):
    jets.append(sp.cancel(D(jets[-1])))       # X^(n) = D(X^(n-1))
jet_f = [sp.lambdify((X, z), j, 'mpmath') for j in jets]

# ---- branch points: disc_X(P)=0 ----
disc = sp.discriminant(P, X)
bps = [mp.mpc(r) for r in mp.polyroots([complex(c) for c in
       sp.Poly(disc, z).all_coeffs()])]
print("branch points z_k:", [mp.nstr(b, 6) for b in bps])

# ---- pick the two closest branch points; cycle = circle around their midpoint ----
pairs = [(i, j, abs(bps[i] - bps[j])) for i in range(len(bps))
         for j in range(i + 1, len(bps))]
i, j, _ = min(pairs, key=lambda t: t[2])
center = (bps[i] + bps[j]) / 2
radius = abs(bps[i] - bps[j]) * mp.mpf('0.75')   # enclose just this pair
print(f"cycle: center={mp.nstr(center,6)} radius={mp.nstr(radius,6)} "
      f"(around branch pair {i},{j})")


def sheet_root(zc, prev):
    """Pick the cubic root in X nearest to `prev` (sheet continuity)."""
    roots = mp.polyroots([1, zc + 1, zc**2 + zc + 1, zc**3 + zc**2 + zc + 1])
    return min(roots, key=lambda r: abs(r - prev))


def period(n, steps=4000):
    """∮_γ X^(n)(z) dz with sheet tracking around the chosen branch cycle."""
    # seed the sheet at t=0
    z0 = center + radius
    Xc = mp.polyroots([1, z0 + 1, z0**2 + z0 + 1, z0**3 + z0**2 + z0 + 1])[0]
    total = mp.mpf(0)
    for k in range(steps):
        t0, t1 = mp.mpf(k) / steps, mp.mpf(k + 1) / steps
        za = center + radius * mp.e**(2j * mp.pi * t0)
        zb = center + radius * mp.e**(2j * mp.pi * t1)
        Xc = sheet_root(za, Xc)
        val = jet_f[n](Xc, za)
        dz = zb - za
        total += val * dz
    return total


print()
print(f"{'n':>2} {'|a_D^(n)| (period)':>22} {'ratio':>10}   "
      f"{'lw(n-1)':>10} {'depth2':>10}")
# reference sequences
q = mp.mpf('1.1099785955573347')
tau = mp.mpf('2.6423863133015')
lw = {1: mp.mpf(1), 2: (q + 1)**2 / (3 * q),
      3: (3 * q**2 + 4 + 3 / q**2) / 4}
d2 = {2: mp.mpf(1), 3: lw[2], 4: lw[3]}
for n in range(2, 8):
    d2[n] = tau * d2.get(n - 1, 0) - d2.get(n - 2, 0) if n >= 4 else d2.get(n, None)
periods, prev = [], None
for n in range(0, NMAX + 1):
    pv = abs(period(n))
    ratio = float(pv / prev) if prev else float('nan')
    lwv = float((1.0 / n) * 0) if n == 0 else ''
    print(f"{n:>2} {mp.nstr(pv, 10):>22} {ratio:>10.4f}")
    periods.append(float(pv)); prev = pv if pv > 0 else prev

print()
ratios = [periods[k + 1] / periods[k] for k in range(2, len(periods) - 1)
          if periods[k] > 1e-25]
geom = all(abs(r - ratios[0]) < 0.3 * ratios[0] for r in ratios) if ratios else False
print(f"period ratios (n≥2): {[round(r,3) for r in ratios]}")
print(f"GEOMETRIC (constant ratio ~λ₊=2.18 ⇒ depth-2/SL2)? {geom}")
print(f"SUPER-EXPONENTIAL (growing ratio ⇒ lw/#1765, SL2 is n≤4 fit)? "
      f"{not geom and len(ratios) >= 2 and ratios[-1] > ratios[0] * 1.3}")
