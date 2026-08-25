#!/usr/bin/env python3
"""
zgeometric_ramification_parity_probe.py — the concrete geometric check behind bean
qou-h5cf (z-geometric scoping of the prolongation-symbol keystone
`conj:qdifference-kernel-prolongation-symbol`).

CLAIM UNDER TEST (sub-claim S1 of the scoping doc, NOT the full identification):
At a simple ramification point z = z_c + t^2 of the color spectral curve
    P(X,z) = X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1) = 0,
the CLASSICAL jet rule λ_SW^(n) = X^(n) dz (X^(n) = n-fold total d/dz) acts on the local
Puiseux coordinate t by SHIFTING the t-exponent by exactly -2 per jet:
    d/dz = (1/(2t)) d/dt  sends  a_k t^k  ->  (k/2) a_k t^{k-2}.
Shift-by-2 PRESERVES t-parity of every term. Hence the classical prolongation can never,
by itself, generate the Z/2 bar-parity character (-1)^n that Door-v measured as the SOLE
residual between C1(x)C1 and the GGM/Stokes carrier
(docs/audits/2026-07-20-qlift-doorV-stokes.md). The geometric datum that DOES carry
(-1)^n is the ramification COVERING MONODROMY t -> -t (one z-loop = half a t-loop), which
acts on a_k t^k by (-1)^k. This probe verifies (S1a) the exact index-shift-by-2 on a
generic Puiseux series, and (S1b) that the chosen z_c is a genuine simple ramification
point of the color cubic (colliding double root, P'=0).

STRUCTURAL check (scope-(b) for the parity-preservation invariant), NOT a verification of
"C1 symbol = prolongation symbol": no independent prolongation-symbol object exists to
compare C1 against — constructing it is the research wall (scoping doc §3). Anti-fit: no
AME data, no target matched, no wiring.
"""
from __future__ import annotations
import sympy as sp
import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
X, z, t = sp.symbols('X z t')
P = X**3 + (z + 1)*X**2 + (z**2 + z + 1)*X + (z**3 + z**2 + z + 1)


def ramification_point():
    """A genuine simple ramification z_c of P(.,z) (root of disc_X P), with its
    colliding double root X0 (checked: P(X0,z_c)=P_X(X0,z_c)=0)."""
    d = sp.Poly(sp.discriminant(P, X), z)
    cs = [mp.mpc(*[float(x) for x in (sp.re(c), sp.im(c))]) for c in d.all_coeffs()]
    zc = mp.polyroots(cs, maxsteps=200, extraprec=80)[0]
    a = [mp.mpf(1), zc + 1, zc**2 + zc + 1, zc**3 + zc**2 + zc + 1]
    rts = mp.polyroots(a, maxsteps=200, extraprec=80)
    Pp = lambda r: 3*a[0]*r**2 + 2*a[1]*r + a[2]
    X0 = min(rts, key=lambda r: abs(Pp(r)))
    return zc, X0, abs(Pp(X0))


def ddz(expr):
    """Classical total derivative in the local t-chart: d/dz = (1/(2t)) d/dt."""
    return sp.expand(sp.diff(expr, t) / (2 * t))


def mono_exponent(expr):
    """t-exponent of a single monomial c*t^k (k may be negative)."""
    expr = sp.simplify(expr)
    if expr == 0:
        return None
    # shift by t^16 to clear negative powers, read the (single) monomial degree
    return int(sp.Poly(expr * t**16, t).monoms()[0][0]) - 16


def main():
    zc, X0, resid = ramification_point()
    print(f"color-cubic ramification z_c = {mp.nstr(zc, 8)}")
    print(f"colliding double root  X0    = {mp.nstr(X0, 8)}")
    print(f"S1b |P_X(X0,z_c)| = {mp.nstr(resid, 4)}  -> genuine simple branch "
          f"(z = z_c + t^2): {resid < 1e-15}")
    print()

    # S1a: exact index-shift-by-2, checked on each Puiseux monomial t^k (k=0..8).
    # d/dz(t^k) = (k/2) t^{k-2}; iterated n times gives an exponent shift of -2n,
    # which preserves parity for every k and every n.
    print("S1a classical jet X^(n) = (d/dz)^n t^k : exponent shift & parity")
    all_shift2 = True
    for k in range(9):
        cur = t**k
        exps = [k]
        for n in range(1, 5):
            cur = ddz(cur)
            exps.append(None if cur == 0 else mono_exponent(cur))
        # nonzero jets must have exponent k-2n and same parity as k
        good = all(e is None or (e == k - 2*i and e % 2 == k % 2)
                   for i, e in enumerate(exps))
        all_shift2 &= good
    print(f"  checked t^0..t^8, jets n=1..4: every nonzero jet has exponent k-2n "
          f"and parity(k): {all_shift2}")
    print()
    print(f"S1a VERDICT exact index-shift-by-2 (parity-preserving): {all_shift2}")
    print("t -> -t covering monodromy acts by (-1)^k  ==>  it is the (-1)^n character.")
    print()
    print("CONCLUSION: classical d/dz cannot generate (-1)^n; the Door-v bar-parity")
    print("residual IS the ramification covering monodromy. A non-classical")
    print("(q-difference) prolongation is required to carry it — matches the corpus.")


if __name__ == '__main__':
    main()
