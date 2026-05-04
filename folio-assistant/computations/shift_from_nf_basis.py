#!/usr/bin/env python3
"""Symbolic-q NF computation: shift contribution per nucleon from 6-knot operator basis.

For β_p, β_n ∈ H_3(q) (per-nucleon intra-nucleon braids), reduce
symbolically to the 6-element NF basis

    NF_BASIS = [γ, σ₀, σ₁, L₊ = σ₀σ₁, L₋ = σ₁σ₀, e⁻ = σ₀σ₁σ₀]

obtaining categorical coefficients c_b(q) ∈ ℤ[q, q⁻¹] (or rational
extensions thereof, but morally Habiro-ring elements).  The Markov
trace decomposes as

    tr_M(β) = Σ_b c_b(q) · TR_M_SYM[b],
    TR_M_SYM = [1, z, z, z², z², z³],   z = u/(1+u²)

so the u-shift exponent of D(u) for β is determined by the maximum
u-pole of c_b(q²) · TR_M_SYM[b] over the 6 basis elements.

Compute:
  1. Symbolic NF coefficients c_b(q) for β_p and β_n in H_3.
  2. shift_NF(β_p), shift_NF(β_n) at the H_3 level.
  3. Compose deuteron β_p ⋆_avg β_n in H_6 and predict shift.
  4. Compare to empirical 40 = 18·1 + 21·1 + 1.

CAUTION: NF coefficients are in PRIMAL basis.  LP shadow prices
y_*[i] live in DUAL basis (Gram-inverted).  When connecting to the
operator-selection LP for cross-partition cancellation Δ_cross, use
the Gram-inverse to translate.

Reference blocks:
  - prop:atom-knot-mass-derivation
  - prop:operator-selection-lp
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hecke_core_symbolic import (  # noqa: E402
    NF_BASIS, NF_NAMES, TR_M_SYM, hm_sym, q, h,
)


def build_nucleon_nf_sym_atomic(quarks):
    """Symbolic NF for a nucleon using `atomic_braid_to_crossings`'s
    11-generator-per-nucleon convention (NOT the 9-generator
    hecke_core.build_nucleon_nf).

    The two conventions differ:
    - hecke_core: B₃ + 3 quark pairs = 9 generators
    - atomic_braid: 7 at gen_idx 0 + 4 at gen_idx 1 = 11 generators

    The atomic-braid convention is what produces empirical shift = 20
    (proton standalone) / 40 (deuteron).  This function mirrors that.

    quarks: list of 'u'/'d' (length 3, e.g. ['u','u','d'] proton).
    Returns: list of 6 sympy expressions = NF coordinates in H_3.
    """
    # Identity in NF basis
    nf = [sp.Integer(1)] + [sp.Integer(0)] * 5
    # Per-nucleon convention (matches mass_endomorphism.proton_cross /
    # neutron_cross via the (c, d) = (1, 0)/(1, -h)/(1, -h/2) pattern).
    qcounts = {'u': quarks.count('u'), 'd': quarks.count('d')}
    is_proton = qcounts['u'] == 2 and qcounts['d'] == 1
    is_neutron = qcounts['u'] == 1 and qcounts['d'] == 2

    if is_proton:
        # gen_idx 0: 3 σ + 1 σ (uu) + 1 averaged (ud) + 2 σ = 7 ops
        gen0 = [(sp.Integer(1), sp.Integer(0))] * 3 + \
               [(sp.Integer(1), sp.Integer(0))] + \
               [(sp.Integer(1), -h / 2)] + \
               [(sp.Integer(1), sp.Integer(0))] * 2
        # gen_idx 1: 3 σ⁻¹ + 1 averaged (ud) = 4 ops
        gen1 = [(sp.Integer(1), -h)] * 3 + [(sp.Integer(1), -h / 2)]
    elif is_neutron:
        # gen_idx 0: 3 σ + 1 σ⁻¹ (dd) + 1 averaged (ud) + 2 σ = 7 ops
        gen0 = [(sp.Integer(1), sp.Integer(0))] * 3 + \
               [(sp.Integer(1), -h)] + \
               [(sp.Integer(1), -h / 2)] + \
               [(sp.Integer(1), sp.Integer(0))] * 2
        # gen_idx 1: 3 σ⁻¹ + 1 averaged (ud) = 4 ops
        gen1 = [(sp.Integer(1), -h)] * 3 + [(sp.Integer(1), -h / 2)]
    else:
        raise ValueError(f"unsupported quark content: {quarks}")

    # Apply gen_idx 0 ops, then gen_idx 1 ops (matches the order in
    # atomic_braid_to_crossings).
    for c, d in gen0:
        nf = hm_sym(nf, c, d, 0)
    for c, d in gen1:
        nf = hm_sym(nf, c, d, 1)
    return [sp.cancel(c) for c in nf]


def build_nucleon_nf_sym(quarks):
    """Symbolic NF mirroring `hecke_core.build_nucleon_nf` (9 generators).

    Kept for legacy comparison; the atomic-braid-to-crossings
    convention uses build_nucleon_nf_sym_atomic instead.
    """
    nf = [sp.Integer(1)] + [sp.Integer(0)] * 5
    for _ in range(3):
        nf = hm_sym(nf, sp.Integer(1), sp.Integer(0), 0)
        nf = hm_sym(nf, sp.Integer(1), -h, 1)
    pairs = [(0, 1, 0), (0, 2, 0), (1, 2, 1)]
    for i, j, gen in pairs:
        qi, qj = quarks[i], quarks[j]
        if qi == qj == 'u':
            nf = hm_sym(nf, sp.Integer(1), sp.Integer(0), gen)
        elif qi == qj == 'd':
            nf = hm_sym(nf, sp.Integer(1), -h, gen)
        else:
            nf = hm_sym(nf, sp.Integer(1), -h / 2, gen)
    return [sp.cancel(c) for c in nf]


def u_shift_of_q_expr(expr_q):
    """Compute u-shift exponent: substitute q = u², reduce, find min
    u-power in the numerator (after sp.together).  shift = −min if min < 0.
    Returns (shift, debug_info)."""
    u = sp.Symbol('u', positive=True, real=True)
    expr_u = sp.together(expr_q.subs(q, u ** 2))
    if expr_u == 0:
        return 0, {"is_zero": True}
    num, den = sp.fraction(expr_u)
    num_poly = sp.Poly(sp.expand(num), u)
    den_poly = sp.Poly(sp.expand(den), u)
    if not num_poly.monoms():
        return 0, {"num_zero": True}
    num_min = min(int(m[0]) for m in num_poly.monoms())
    num_max = num_poly.degree()
    den_min = min(int(m[0]) for m in den_poly.monoms()) if den_poly.monoms() else 0
    den_max = den_poly.degree() if den_poly.monoms() else 0
    # Effective u-power range of expr_u: [num_min - den_max, num_max - den_min]
    eff_min = num_min - den_max
    eff_max = num_max - den_min
    return -eff_min if eff_min < 0 else 0, {
        "num_u_range": (num_min, num_max),
        "den_u_range": (den_min, den_max),
        "eff_u_range": (eff_min, eff_max),
    }


def shift_from_nf(nf_list):
    """Compute u-shift of tr_M(β) where β has NF coefficients nf_list.

    tr_M = Σ c_b · TR_M_SYM[b]; shift = u-shift of this combined expression.
    """
    tr_q = sum(nf_list[i] * TR_M_SYM[i] for i in range(6))
    tr_q_simplified = sp.cancel(tr_q)
    shift, debug = u_shift_of_q_expr(tr_q_simplified)
    return shift, tr_q_simplified, debug


def main() -> int:
    print("=" * 76)
    print("Symbolic-q NF computation — shift from 6 fundamental knot operators")
    print("=" * 76)
    print()

    print("Per-nucleon NF coefficients (in basis {γ, σ₀, σ₁, L₊, L₋, e⁻}):")
    print()

    proton_nf = build_nucleon_nf_sym_atomic(['u', 'u', 'd'])
    neutron_nf = build_nucleon_nf_sym_atomic(['u', 'd', 'd'])

    print("β_p (proton, uud):")
    for i, c in enumerate(proton_nf):
        c_simp = sp.cancel(c)
        print(f"  c_{NF_NAMES[i]:>3}(q) = {c_simp}")
    print()
    print("β_n (neutron, udd):")
    for i, c in enumerate(neutron_nf):
        c_simp = sp.cancel(c)
        print(f"  c_{NF_NAMES[i]:>3}(q) = {c_simp}")
    print()

    print("──")
    shift_p, tr_p, debug_p = shift_from_nf(proton_nf)
    print(f"shift_NF(β_p) at H_3 level = {shift_p}")
    print(f"  tr_M(β_p) = {tr_p}")
    print(f"  debug: {debug_p}")
    print()
    shift_n, tr_n, debug_n = shift_from_nf(neutron_nf)
    print(f"shift_NF(β_n) at H_3 level = {shift_n}")
    print(f"  tr_M(β_n) = {tr_n}")
    print(f"  debug: {debug_n}")
    print()
    print("Empirical (from existing witnesses):")
    print(f"  shift(proton standalone, H_3, include_inter=False) = 20")
    print(f"  shift(neutron standalone, H_3, include_inter=False) = 16")
    print(f"  shift(proton in deuteron, H_6) = 18  (different — embedding effect)")
    print(f"  shift(neutron in deuteron, H_6) = 21")

    out = {
        "computation": "shift-from-nf-basis",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Symbolic-q NF reduction of per-nucleon braids β_p, β_n in "
            "H_3(q) = 6-dimensional Hecke algebra of B_3.  Decomposes "
            "each nucleon into the 6 fundamental knot operators (NF "
            "basis: γ, σ₀, σ₁, L₊, L₋, e⁻) with categorical coefficients "
            "c_b(q) ∈ Habiro ring.  Computes shift_NF(β_p), shift_NF(β_n) "
            "from the trace decomposition tr_M = Σ c_b · TR_M_SYM[b].  "
            "These are the H_3-context shifts; the embedded H_(3A)-context "
            "shifts (18 for p, 21 for n) require Littlewood-Richardson "
            "branching analysis."
        ),
        "nf_basis_names": NF_NAMES,
        "tr_m_symbolic": [str(t) for t in TR_M_SYM],
        "proton_nf_symbolic": [str(sp.cancel(c)) for c in proton_nf],
        "neutron_nf_symbolic": [str(sp.cancel(c)) for c in neutron_nf],
        "shift_proton_h3": shift_p,
        "shift_neutron_h3": shift_n,
        "tr_proton_h3": str(tr_p),
        "tr_neutron_h3": str(tr_n),
        "empirical_shift_proton_h3_standalone": 20,
        "empirical_shift_neutron_h3_standalone": 16,
        "empirical_shift_proton_in_deuteron_h6": 18,
        "empirical_shift_neutron_in_deuteron_h6": 21,
        "caveat": (
            "Predictions may differ from empirical due to (a) the "
            "embedded-vs-standalone H-context shift difference and "
            "(b) cross-partition cancellation Δ_cross from "
            "Ocneanu-weight cancellation across active LP channels."
        ),
    }
    out_path = HERE / "shift-from-nf-basis.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print()
    print(f"Witness: {out_path}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
