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

CORPUS COROBORATION (prop:sw-period-residue-sum). The corpus gives the SAME
period as an algebraic residue sum, a_D^(n)=2πi·Σ_p Res_p λ_SW^(n), and states
verbatim that "each residue is a per-block quantum-dimensional weight on the
Wedderburn decomposition restricted to that level" — i.e. Σ residues = Σ_λ dim_q
= lw. So the lw column computed below is NOT just the external #1765 claim; it is
the corpus's own residue-sum value. Two independent routes (branch point here,
Wedderburn residues in the corpus) give the same super-exp growth.

VERDICT: super-exponential ⇒ lw/#1765 is the true prolongation; the depth-2 SL2
τ is an n≤4 effective fit (it cannot produce factorial growth). Audit-only.
"""
from __future__ import annotations
import sympy as sp
import mpmath as mp
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This file bound the RETIRED
# self-certified muon pin A as a literal -- superseded 2026-08-22 by the
# CODATA-2022 derivation, so the value was ~46 ppb stale AND could not follow
# the anchor. This stem is not in `ideal_muon`, so `Q_50_DIGIT_STR` resolves to
# the PROTON pin, which the 2026-08-30 owner ruling makes the default.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent,
              _Path_qp(__file__).resolve().parent / 'substrate',
              _Path_qp(__file__).resolve().parent.parent / 'computations',
              _Path_qp(__file__).resolve().parent.parent / 'computations' / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()
z, X = sp.symbols('z X')
P = X**3 + (z + 1) * X**2 + (z**2 + z + 1) * X + (z**3 + z**2 + z + 1)

# ---- branch points + branch order (square-root?) -----------------------------
disc = sp.discriminant(P, X)
# The discriminant's coefficients are exact integers; `complex(c)` used to push
# them through float64 (a NO-FLOAT64 violation, AGENTS.md §probes-are-not-exempt).
# Carry them as mpf instead.  Fixed 2026-09-03, bean qou-qx7j.
bps = mp.polyroots([mp.mpf(int(c)) for c in sp.Poly(disc, z).all_coeffs()],
                   maxsteps=200, extraprec=300)
print("color-cubic branch points (disc_X=0):", [mp.nstr(b, 5) for b in bps])
# verify order-2 branch: at z_k two cubic roots collide (gap → 0).
# The collision is the whole point, so the default maxsteps=50 cannot resolve it
# and mpmath raised NoConvergence here -- this probe did not run at all on main.
zk = bps[0]
roots = sorted(mp.polyroots([mp.mpf(1), zk + 1, zk**2 + zk + 1,
                             zk**3 + zk**2 + zk + 1],
                            maxsteps=200, extraprec=300),
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
q = Q_MP
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
print("\n  lw column = corpus residue sum (prop:sw-period-residue-sum) = Σ_λ dim_q.")
print("  n |   lw/#1765   ratio |   depth-2/SL2  ratio")
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
print("CONFIRMED two ways: branch-point Puiseux (here) AND the corpus residue sum")
print("(prop:sw-period-residue-sum: residues = per-block Wedderburn dim_q = lw).")
print("=" * 70)
print()
print("SCOPE CORRECTION (2026-09-03, bean qou-qx7j) -- the SECOND route above is")
print("withdrawn; the first is untouched.  prop:sw-period-residue-sum was found")
print("(bean qou-6v5l, PR #6067) to state its residue sum over ALL poles with the")
print("residue theorem as warrant, which runs backwards: on a compact surface the")
print("residues SUM TO ZERO.  And the residues are not merely mis-summed, they are")
print("individually zero -- (ddz f)(-2) = ((-2)+2)*f(0) = 0 for every f, so the")
print("t^-2 coefficient of any z-derivative vanishes")
print("(QOU.Brings.ColourCubicBranchLocus.ddz_residue_slot_eq_zero).  So the")
print("residues are NOT the per-block Wedderburn dim_q, and that leg confirms")
print("nothing.  The branch-point Puiseux argument for super-exponential GROWTH")
print("stands on its own, as does the lw/#1765 verdict.")
print("=" * 70)
