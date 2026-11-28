"""half_class_3d_index.py — GHRS 3d index at half-longitude peripheral classes.

The DGG index I_K(m,e) of a knot complement counts magnetic flux m in units of
HALF the longitude (for 4₁, DGG eq 4.18's I(2,e) is the GHRS index of the class
e·μ + 1·λ; checked in qbeta_g3_fivetwo_stokes_from_3d_index.py).  For odd m the
class e·μ + (m/2)·λ is not integral, and the GHRS lattice sum needs a
half-integral shift of the edge weights.  This module evaluates it with the
corpus engine's ingredients (borromean_3d_index.J_D/I_D, SnapPy gluing rows):

  I(e, m) = Σ_{k ∈ Z^{n-r} + δ}  q^{Σk} · Π_j J_Δ(t_j),
  t_j = (k·E + e·μ + (m/2)·λ)_{tet j},

where δ ∈ {0,½}^{n-r} is chosen so that each triple t_j has all three entries
of one parity class mod 1, and J_Δ on a triple shifted by s(1,1,1), s ∈ ½Z, uses
the same rule J_Δ(t+s) = (-q^{1/2})^{-s} J_Δ(t) as for integer s (GHHR eq 6),
with the product over tetrahedra required to carry an integer total shift.
Doubled integer arithmetic throughout; exact.
"""
from __future__ import annotations

import importlib.util
import itertools
import os

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("b3", os.path.join(HERE, "borromean_3d_index.py"))
b3 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b3)
b3.log = lambda *a, **k: None


class HalfIndex:
    def __init__(self, manifold):
        self.T = b3.IndexTriangulation(manifold)
        self.n = self.T.n
        self.E = [self.T.edge_rows[i] for i in self.T.basic_edges]
        self.mu, self.lam = self.T.cusp_rows[0], self.T.cusp_rows[1]
        self._delta = {}

    def _triples2(self, k2, e, m):
        """Doubled charges 2·t for doubled edge weights k2 (list over basic edges)."""
        tot = [2 * e * self.mu[j] + m * self.lam[j] for j in range(3 * self.n)]
        for ki, row in zip(k2, self.E):
            if ki:
                for j in range(3 * self.n):
                    tot[j] += ki * row[j]
        return [(tot[3 * j], tot[3 * j + 1], tot[3 * j + 2]) for j in range(self.n)]

    def delta(self, m):
        """δ (doubled, entries 0/1) making every doubled triple single-parity."""
        par = m % 2
        if par in self._delta:
            return self._delta[par]
        for d in itertools.product((0, 1), repeat=len(self.E)):
            if all(a % 2 == b % 2 == c % 2 for a, b, c in self._triples2(list(d), 0, m)):
                self._delta[par] = d
                return d
        raise ValueError(f"no half-shift makes class m={m} single-parity")

    @staticmethod
    def _nu2(t2):
        m2 = min(t2)
        s = sorted((x - m2) // 2 for x in t2)
        return 2 * s[1] * s[2] - m2          # doubled Q-degree: 2(AB) - 2·min

    def index(self, e, m, qmax, rmax=30, empty_stop=4):
        """I(e,m) as {Q-power: int}, Q = q^{1/2}, through q^qmax."""
        hi = 2 * qmax
        d = self.delta(m)
        out = {}
        empty = 0
        for R in range(rmax + 1):
            got = False
            for kk in itertools.product(range(-R, R + 1), repeat=len(self.E)):
                if R and max(abs(v) for v in kk) != R:
                    continue
                k2 = [2 * v + dv for v, dv in zip(kk, d)]
                t2s = self._triples2(k2, e, m)
                K2 = sum(k2)                                  # Q-power of q^{Σk}
                M2 = sum(min(t) for t in t2s)
                if M2 % 2:
                    raise ValueError("odd total half-shift")
                deg2 = 2 * K2 + sum(self._nu2(t) for t in t2s)   # doubled Q-degree
                if deg2 > 2 * hi:
                    continue
                got = True
                prod = {0: 1}
                cap = hi - K2 + M2 // 2
                for t in t2s:
                    m2 = min(t)
                    A, B = sorted((x - m2) // 2 for x in t)[1:]
                    fac = b3.I_D(-A, B, cap)
                    prod = b3._mul(prod, fac, cap)
                sign = -1 if (M2 // 2) % 2 else 1
                for p, c in prod.items():
                    pp = p + K2 - M2 // 2
                    if pp <= hi:
                        out[pp] = out.get(pp, 0) + sign * c
            empty = 0 if got else empty + 1
            if empty >= empty_stop and R > 2 * (abs(e) + abs(m)) + 4:
                break
        return {p: c for p, c in out.items() if c}
