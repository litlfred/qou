#!/usr/bin/env python3
"""per_braid_tower.py — convergent per-braid brane tower for nuclear binding.

Implements the CONVERGENT per-braid form of `prop:per-braid-mass-tower`
(folio/quantum-observable-universe/mass-theory/per-braid-mass-tower.md),
replacing the DIVERGENT per-generator `binding_3A_tower` / `mass_from_tower`
(deuteron B ≈ 6.9M MeV — the superseded `prop:mass-endomorphism-tower`
Φ_q-of-per-generator-product form).

Mass functional (binding context → symmetric Li_2^q, bar-invariant, per
`_li_2_q_util.py` + cheat-sheet §4):

    𝔪(W) = |tr_M(W)|                                    [n=0 descended]
          + Σ_{ξ∈S₁} g(|tr_M(ξ)|)                         [singletons]
          + z² · Σ_{(ξ,ξ')∈S₂} g(|tr_M(ξ ξ')|)            [pairs]
          + (higher jet levels, O(ℏ_q²) tail)

with z = 1/(q^{1/2}+q^{-1/2}). The dilogarithm sign is DERIVED from the
categorical action (not chosen) — `bar-parity-split.md`:
  * binding = bar-EVEN (cosh, σ-fixed) part of the trace; Li_2^q is already
    bar-symmetric ([n]_q is q↦q⁻¹-invariant) ⇒ it sits in the binding channel;
  * the argument sign is the Hecke ANTISYMMETRIC eigenvalue −q⁻¹ (antipode
    S(σ)=σ⁻¹, Hecke (σ−q)(σ+q⁻¹)=0), so the canonical term is
        g(x) = −Li_2^q(−x).
  The bare +Li_2^q(+x) (compute_t2_t3_from_vols helper) is NOT the binding
  projection; it is retained here only as a cross-check (`pos_arg`).

Binding is the difference B = E₀·(𝔪_free − 𝔪_atom): the SINGLETON
(per-nucleon) terms CANCEL identically (the nucleons are unchanged
bound-vs-free), so only the descended Δtr_M and the PAIR terms survive. The
A=2 pair is INCLUDED — the ℓ=0 descended functional |tr_M(W)| and the ℓ=2
pair functional z²·g(|tr_M(W)|) are DISTINCT functionals of the same braid,
not a double-count (the prop's double-count carve-out is about repeating the
|tr_M| descended product per level, not the dilog pair term).

    B_can⁰  = E₀·Δtr_M = E₀·(|tr_M_free| − |tr_M_atom|)   [level 0, headline]
    B_tower = B_can⁰ + E₀·z²·Σ_pairs (g(tr_free_pair) − g(tr_atom_pair))

PURE Markov trace × m_e (E₀ = m_e/(q₀(q₀−1))). Zero AME, zero CODATA
nucleon mass; only CAL-1 (m_e unit) + CAL-2 (q₀).

CONVERGENCE CAVEAT (the open implementation item). The prop requires each
sub-braid trace via the proper H_{3A} Schur–Weyl path so that
|tr_M(ξ)| < q₀ (the Li_2^q radius). For A ≥ 3 the nucleon-PAIR sub-braids
must therefore be evaluated as χ^λ(ξ) for λ ⊢ 3A in the AMBIENT algebra —
NOT as an isolated H₆ trace, whose free value tr_p² ≈ 1.134 > q₀ ≈ 1.110
diverges. The deuteron (A=2) is the one case where the single pair IS the
whole atom, so its ambient trace is well-defined and this script is exact;
the A ≥ 3 ambient-pair path is the open build (see the module's audit doc).

Usage:
    python3 per_braid_tower.py        # deuteron tower, both sign conventions
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
warnings.filterwarnings("ignore")

import mpmath as mp  # noqa: E402

from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import M_E_MEV as M_E  # noqa: E402
from _li_2_q_util import li_2_q  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402


def _consts(dps: int = 50):
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    q = mp.mpf(str(Q0))
    me = mp.mpf(str(M_E))
    qi = mp.mpf(1) / q
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(me, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    # convention D (owner ruling 2026-08-15, reaffirmed 2026-08-23):
    #   z_D = q^3/(q^2+1).  Was z_C = 1/(sqrt q + sqrt(1/q)), excised.
    # The pair augmentation below is exactly z^2, so this scales it by
    # (z_D/z_C)^2 = 1.505637 -- and it overshoots; see the commit message.
    z = q ** 3 / (q ** 2 + 1)
    return q, qi, me, E0, z


def deuteron_tower(dps: int = 50) -> dict:
    """Exact deuteron (A=2) per-braid tower — the single pair = whole atom,
    so the ambient trace is well-defined. Reports level-0 B_can⁰ and the
    n=0 pair-augmented B_tower under both documented Li_2^q sign conventions
    (the `_li_2_q_util` docstring carries both: outer-minus/negative-arg vs
    bare-positive)."""
    q, qi, me, E0, z = _consts(dps)
    z2 = z * z
    ta, tf, _, _ = tr_m_atom_zn(1, 1, dps=dps)
    ta, tf = mp.mpf(ta), mp.mpf(tf)
    dtr = tf - ta
    B0 = E0 * dtr

    def g_neg(x):                       # g(x) = −Li_2^q(−x)  (lines 34–41)
        return -li_2_q(-x, q, qi)

    def g_pos(x):                       # g(x) = +Li_2^q(+x)  (line 141 impl)
        return li_2_q(x, q, qi)

    out = {
        "q0": str(q), "E0_MeV": float(E0), "z2": float(z2),
        "hbar_q_sq_tail": float((1 - qi) ** 2),
        "tr_M_free": float(tf), "tr_M_atom": float(ta), "Delta_tr": float(dtr),
        "B_can0_MeV": float(B0),
    }
    for name, g in (("neg_arg", g_neg), ("pos_arg", g_pos)):
        pair = z2 * (g(tf) - g(ta))
        out[f"pair_corr_MeV_{name}"] = float(E0 * pair)
        out[f"B_tower_MeV_{name}"] = float(E0 * (dtr + pair))
    return out


if __name__ == "__main__":
    r = deuteron_tower()
    B_AME = 2.224573
    print(f"Deuteron per-braid brane tower  (E₀={r['E0_MeV']:.4f} MeV, "
          f"z²={r['z2']:.5f}, ℏ_q² tail={r['hbar_q_sq_tail']:.5f}/level)")
    print(f"  tr_M_free={r['tr_M_free']:.6f}  tr_M_atom={r['tr_M_atom']:.6f}  "
          f"Δtr={r['Delta_tr']:.6f}")
    print(f"  B_can⁰ = E₀·Δtr            = {r['B_can0_MeV']:.4f} MeV   "
          f"err={B_AME / r['B_can0_MeV']:.3f}  ({(r['B_can0_MeV'] / B_AME - 1) * 100:+.1f}%)")
    for name in ("neg_arg", "pos_arg"):
        bt = r[f"B_tower_MeV_{name}"]
        print(f"  B_tower [{name}] = B_can⁰ + {r[f'pair_corr_MeV_{name}']:+.4f} "
              f"= {bt:.4f} MeV   err={B_AME / bt:.3f}  ({(bt / B_AME - 1) * 100:+.1f}%)")
    print(f"  B_AME = {B_AME} MeV   → the n=0 pair term ADDS binding under "
          f"both conventions (deuteron is already over-bound at level 0).")
