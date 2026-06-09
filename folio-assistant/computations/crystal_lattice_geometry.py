#!/usr/bin/env python3
# polynomial_q_not_applicable: braid-weight geometry toolkit, not a
# Jones-polynomial evaluation.
"""
crystal_lattice_geometry — a general braid-weight toolkit for molecular,
crystal, and lattice geometry from the QOU symmetric-Wedderburn-block rule.

This module consolidates the molecular-bond-angle program
(`prop:symmetric-block-domain-weight`, `conj:h2s-angle-s3-braid-holonomy`)
into one reusable, documented API so anyone working on crystal / lattice /
coordination geometry can build on it. EVERYTHING derives from a single rule
plus two structural inputs — no per-structure fit.

THE RULE (provable; Lean `QOU.Molecular.symmetric_block_domain_weight`):
  On the symmetric (trivial) Wedderburn block that a structure's C_{nv}/point-
  group assembly projector selects, every generator acts as the scalar q, so an
  electron domain that is a braid word of length ℓ has WEIGHT

        w_domain = q ** ℓ .

  Bond orders and lone pairs are the standard words:
        single bond σ        ℓ=1 → q
        double bond σ²        ℓ=2 → q²
        triple bond σ³        ℓ=3 → q³
        lone pair e⁻=σ₀σ₁σ₀   ℓ=3 → q³     (⇒ lone/bond ratio q³/q = q²)

THE TWO STRUCTURAL INPUTS:
  1. domain counts (AX_nE_m / coordination + lone pairs) → the VSEPR geometry;
  2. the hybridisation BASE θ₀ = active-set membership of the self-dual
     s-channel, set by central-atom SIZE (the s–p promotion gap):
        small atom (row 2, small gap) → s active → sp/sp²/sp³ by steric number;
        large atom (row ≥ 3, large gap) → s inert → pure-p (orthogonal-p, 90°),
        with a residual-mixing correction (1/√5)/(n−1)² (the Bring constant).

CHIRALITY (`prop:chirality-residue-mass-term`): a Wedderburn block is a
  chirality cell iff signed Young content c_λ = Σ(j−i) = 0 (q-Dirac kernel
  D_q²=[c_λ]_q²=0). For H₃ this is the (2,1) standard block (the p-orbital block).

Quick start
-----------
    from crystal_lattice_geometry import BraidGeometry
    g = BraidGeometry()                       # uses the substrate q₀
    g.lone_bond_ratio()                       # -> q² ≈ 1.232
    g.predict_angle(n_bond=2, n_lone=2, shell_n=2)   # H₂O  -> ~104.7°
    g.predict_angle(n_bond=2, n_lone=2, shell_n=3)   # H₂S  -> ~92.2°
    g.predict_angle(n_bond=3, n_lone=0, double_bonds=1, shell_n=2)  # C₂H₄
"""
from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import numpy as np

_HERE = Path(__file__).resolve().parent
for _p in (str(_HERE),
           str(_HERE.parents[1] / "tools" / "pyhecke" / "python"),
           str(_HERE.parents[1] / "tools" / "qou-substrate" / "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

try:
    import _path_bridge  # noqa: F401
    from q_parameter import Q as _Q0
    _SUBSTRATE_Q = float(_Q0)
except Exception:                       # standalone use: fall back to q₀ value
    _SUBSTRATE_Q = 1.1099785828

THETA_SP3 = float(np.degrees(np.arccos(-1.0 / 3.0)))   # 109.471°
THETA_PURE_P = 90.0
INV_SQRT5 = 1.0 / np.sqrt(5.0)                          # Bring / quintic constant
_STERIC_BASE = {2: 180.0, 3: 120.0, 4: THETA_SP3, 5: 90.0, 6: 90.0}


@dataclass
class BraidGeometry:
    """Braid-weight geometry toolkit. `q` defaults to the substrate q₀."""

    q: float = _SUBSTRATE_Q

    # ── weights (the q^ℓ rule) ──────────────────────────────────────
    def domain_weight(self, braid_length: int) -> float:
        """Weight of a domain whose braid word has length ℓ: q**ℓ."""
        return self.q ** braid_length

    def bond_weight(self, bond_order: int = 1) -> float:
        """Bond of order k = k crossings σ^k → q**k (single q, double q², …)."""
        return self.q ** bond_order

    def lone_weight(self) -> float:
        """Lone pair e⁻ = σ₀σ₁σ₀ (ℓ=3) → q³."""
        return self.q ** 3

    def lone_bond_ratio(self) -> float:
        """Derived lone/bond weight ratio q³/q = q² (Lean-proved, no fit)."""
        return self.q ** 2

    # ── chirality (signed Young content) ────────────────────────────
    @staticmethod
    def signed_content(partition) -> int:
        """Signed Young content c_λ = Σ_{(i,j)∈λ}(j−i)."""
        return sum(j - i for i, row in enumerate(partition) for j in range(row))

    def q_dirac_curvature(self, partition) -> float:
        """q-Dirac curvature D_q²(λ) = [c_λ]_q². Zero on chirality cells."""
        c = self.signed_content(partition)
        if c == 0:
            return 0.0
        return ((self.q ** c - self.q ** (-c)) / (self.q - 1.0 / self.q)) ** 2

    def is_chirality_cell(self, partition) -> bool:
        """Chirality cell ⇔ c_λ = 0 ⇔ D_q² = 0 (q-Dirac kernel)."""
        return self.signed_content(partition) == 0

    # ── hybridisation base + residual mixing ────────────────────────
    def hybridises(self, shell_n: int) -> bool:
        """Row-2 (n=2) hybridises (s active); row ≥3 is pure-p (s inert)."""
        return shell_n <= 2

    def hybridisation_base(self, n_bond: int, n_lone: int, shell_n: int) -> float:
        """Base angle θ₀: steric-number sp/sp²/sp³ if hybridised, else pure-p."""
        if self.hybridises(shell_n):
            return _STERIC_BASE.get(n_bond + n_lone, THETA_SP3)
        return THETA_PURE_P

    def bring_residual_mixing(self, shell_n: int) -> float:
        """Residual s-character f_s = (1/√5)/(n−1)² (Bring constant; row ≥3)."""
        if self.hybridises(shell_n):
            return 0.0
        return INV_SQRT5 / (shell_n - 1) ** 2

    # ── geometry ────────────────────────────────────────────────────
    def vsepr_angle(self, n_bond: int, n_lone: int,
                    double_bonds: int = 0, kernel: float = 1.0,
                    restarts: int = 24, seed: int = 0) -> float:
        """Weighted points-on-a-sphere bond–bond angle (Coulomb kernel).

        Bonds weigh q (or q^order for the `double_bonds` heavier ones); lone
        pairs weigh q³. Returns the mean angle among the bonding domains."""
        weights = ([self.q ** 2] * double_bonds
                   + [self.q] * (n_bond - double_bonds)
                   + [self.q ** 3] * n_lone)
        N = len(weights)
        if N < 2:
            return float("nan")
        w = np.asarray(weights)

        def energy(x):
            p = x.reshape(-1, 3)
            p = p / np.maximum(np.linalg.norm(p, axis=1, keepdims=True), 1e-12)
            s = 0.0
            for i in range(N):
                for j in range(i + 1, N):
                    d = np.linalg.norm(p[i] - p[j])
                    if d < 1e-6:
                        return 1e9
                    s += w[i] * w[j] / d ** kernel
            return s

        from scipy.optimize import minimize
        rng = np.random.default_rng(seed)
        best = None
        for _ in range(restarts):
            r = minimize(energy, rng.normal(size=3 * N), method="Nelder-Mead",
                         options={"xatol": 1e-7, "fatol": 1e-11, "maxiter": 7000})
            if best is None or r.fun < best.fun:
                best = r
        p = (best.x.reshape(-1, 3))
        p = p / np.maximum(np.linalg.norm(p, axis=1, keepdims=True), 1e-12)
        if n_bond < 2:
            return float("nan")
        # the X–A–X angle is between the two LIGHTEST (equivalent) bonds — for
        # symmetric cases any pair, for e.g. C₂H₄ the two single bonds (H–C–H)
        light = np.argsort(w[:n_bond])[:2]
        i, j = int(light[0]), int(light[1])
        return float(np.degrees(np.arccos(np.clip(np.dot(p[i], p[j]), -1, 1))))

    def predict_angle(self, n_bond: int, n_lone: int, shell_n: int = 2,
                      double_bonds: int = 0) -> dict:
        """High-level X–A–X bond-angle prediction (no fit).

        Returns a dict with the base, the predicted angle, and the regime."""
        base = self.hybridisation_base(n_bond, n_lone, shell_n)
        if self.hybridises(shell_n):
            # hybridised: q-weighted VSEPR on the sp/sp²/sp³ base
            if n_bond + n_lone >= 4 or double_bonds:
                theta = self.vsepr_angle(n_bond, n_lone, double_bonds)
            else:
                theta = base
            regime = "hybridised (s active)"
        else:
            # pure-p with the Bring (1/√5) residual-mixing correction
            f_s = self.bring_residual_mixing(shell_n)
            theta = THETA_PURE_P + f_s * (THETA_SP3 - THETA_PURE_P)
            regime = "pure-p (s inert) + Bring residual mixing"
        return {"predicted_deg": theta, "base_deg": base, "regime": regime,
                "lone_bond_ratio": self.lone_bond_ratio()}


def _demo():
    g = BraidGeometry()
    print(f"crystal_lattice_geometry — q = {g.q:.5f}")
    print(f"  lone/bond ratio q² = {g.lone_bond_ratio():.4f}")
    print(f"  chirality cells (H₃): "
          f"(3)→{g.is_chirality_cell((3,))}, (2,1)→{g.is_chirality_cell((2,1))}, "
          f"(1,1,1)→{g.is_chirality_cell((1,1,1))}")
    cases = [("CH₄", dict(n_bond=4, n_lone=0, shell_n=2)),
             ("NH₃", dict(n_bond=3, n_lone=1, shell_n=2)),
             ("H₂O", dict(n_bond=2, n_lone=2, shell_n=2)),
             ("C₂H₄ (H–C–H)", dict(n_bond=3, n_lone=0, shell_n=2, double_bonds=1)),
             ("H₂S", dict(n_bond=2, n_lone=2, shell_n=3)),
             ("H₂Se", dict(n_bond=2, n_lone=2, shell_n=4))]
    print("  predictions:")
    for name, kw in cases:
        r = g.predict_angle(**kw)
        print(f"    {name:<14} {r['predicted_deg']:7.2f}°   [{r['regime']}]")


if __name__ == "__main__":
    _demo()
