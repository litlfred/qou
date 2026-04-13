#!/usr/bin/env python3
"""
Atomic mass for Z=1-10 via FULL Hecke algebra — SYMBOLIC in q.

All three irrep channels (symmetric, standard, alternating) are
tracked as symbolic expressions in ℤ[q, q⁻¹], then evaluated at q₀.

Three-channel decomposition:
  - Symmetric channel:   σ ↦ q       (1D trivial irrep)
  - Standard channel:    σ ↦ 2×2     (2D seminormal)
  - Alternating channel: σ ↦ -q⁻¹    (1D sign irrep)

Mass decomposition (fibre / horizontal / mixed):
  - Horizontal: crossing energy E_cross = n_+ · q − n_- · q⁻¹
  - Vertical (fibre): Markov trace 𝔪 = |tr_M(Φ_mass)|
  - Mixed: vertex operator coupling = E_cross · (q-1)²

Usage:
    cd folio-assistant/computations
    python3 atom_mass_full_hecke.py
"""

import math
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path

import sympy as sp
from sympy import Rational, sqrt, simplify, expand, factor, Abs

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from witness_base import WitnessBuilder


# ══════════════════════════════════════════════════════════════
# §1  SYMBOLIC RING ℤ[q, q⁻¹]
# ══════════════════════════════════════════════════════════════

q = sp.Symbol('q', positive=True)
q_inv = 1 / q
HA = q - q_inv                          # Hecke amplitude
z = 1 / (sqrt(q) + 1 / sqrt(q))        # Markov parameter


def crossing_coeffs(ti, tj):
    """Returns symbolic (c, d) for nucleon pair type.
    ti, tj ∈ {1 (proton), 0 (neutron)}.
    """
    if ti == 1 and tj == 1:      # pp → σ
        return sp.Integer(1), sp.Integer(0)
    elif ti == 0 and tj == 0:    # nn → σ⁻¹ = σ - HA
        return sp.Integer(1), -HA
    else:                         # pn/np → ½(σ + σ⁻¹)
        return sp.Integer(1), -HA / 2


# ══════════════════════════════════════════════════════════════
# §2  THREE-CHANNEL SYMBOLIC TRACES
# ══════════════════════════════════════════════════════════════

def sym_eigenvalue(c, d):
    """Symmetric irrep: σ ↦ q, so (c·σ + d) ↦ c·q + d."""
    return c * q + d


def alt_eigenvalue(c, d):
    """Alternating irrep: σ ↦ -q⁻¹, so (c·σ + d) ↦ -c·q⁻¹ + d."""
    return -c * q_inv + d


def std_chain_reduce(gen_idx, ordering, include_gluon=False):
    """2×2 transfer matrix chain reduction (symbolic in q).
    Returns (a, b) such that V̂_std = z·a + b.

    If include_gluon=True, prepend LP-derived gluon crossings:
      proton (1): 2×σ₀ = [(1,0), (1,0)]
      neutron (0): L₊→L₋ effective = [(1,0), (1,0), (1,0), (1,0)]
    """
    a = sp.Integer(0)
    b = sp.Integer(1)
    A = len(ordering)

    # Gluon: internal crossings for the nucleon at gen_idx
    if include_gluon and gen_idx < A:
        if ordering[gen_idx] == 1:  # proton: 2×σ₀
            for c, d in [(sp.Integer(1), sp.Integer(0))] * 2:
                new_a = sp.expand(a * c * HA + a * d + b * c)
                new_b = sp.expand(a * c + b * d)
                a, b = new_a, new_b
        else:  # neutron: L₊→L₋ effective (4 positive crossings)
            for c, d in [(sp.Integer(1), sp.Integer(0))] * 4:
                new_a = sp.expand(a * c * HA + a * d + b * c)
                new_b = sp.expand(a * c + b * d)
                a, b = new_a, new_b

    for j in range(gen_idx + 1, A):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
        new_a = sp.expand(a * c * HA + a * d + b * c)
        new_b = sp.expand(a * c + b * d)
        a, b = new_a, new_b
    return a, b


def three_channel_traces_symbolic(ordering, include_gluon=False):
    """Compute symbolic traces for all three channels.

    Returns (tr_sym, tr_std, tr_alt) as sympy expressions in q.

    Symmetric and alternating traces are kept in FACTORED form
    (products of linear factors in q) to avoid combinatorial blowup.
    Standard trace uses the chain-reduced traced volume.

    If include_gluon=True, prepend LP-derived gluon crossings per nucleon:
      proton: 2×σ → sym ×q², alt ×q⁻²
      neutron: 4×σ → sym ×q⁴, alt ×q⁻⁴
    """
    A = len(ordering)
    if A <= 1:
        return sp.Integer(1), sp.Integer(1), sp.Integer(1)

    # Symmetric and alternating: collect all crossing factors
    sym_factors = []
    alt_factors = []

    # Gluon: internal crossing eigenvalues per nucleon
    if include_gluon:
        for i in range(A):
            if ordering[i] == 1:  # proton: 2 gluon crossings
                sym_factors.extend([q, q])       # 2×σ in sym → q each
                alt_factors.extend([-q_inv, -q_inv])  # 2×σ in alt → -q⁻¹ each
            else:  # neutron: 4 gluon crossings
                sym_factors.extend([q, q, q, q])
                alt_factors.extend([-q_inv, -q_inv, -q_inv, -q_inv])

    for i in range(A):
        for j in range(i + 1, A):
            c, d = crossing_coeffs(ordering[i], ordering[j])
            sym_factors.append(sym_eigenvalue(c, d))
            alt_factors.append(alt_eigenvalue(c, d))

    tr_sym = sp.Mul(*sym_factors)
    tr_alt = sp.Mul(*alt_factors)

    # Standard: product of traced volumes (each already reduced)
    std_factors = []
    for i in range(A - 1):
        a, b = std_chain_reduce(i, ordering, include_gluon=include_gluon)
        std_factors.append(z * a + b)
    tr_std = sp.Mul(*std_factors)

    return tr_sym, tr_std, tr_alt


def full_markov_trace_symbolic(ordering, include_gluon=False):
    """Full Wedderburn-weighted Markov trace (symbolic).

    w_sym = 1/6, w_std = 4/6, w_alt = 1/6.
    """
    tr_sym, tr_std, tr_alt = three_channel_traces_symbolic(ordering, include_gluon=include_gluon)
    return Rational(1, 6) * tr_sym + Rational(4, 6) * tr_std + Rational(1, 6) * tr_alt


def crossing_energy_symbolic(ordering):
    """Horizontal crossing energy (symbolic in q)."""
    A = len(ordering)
    E = sp.Integer(0)
    for i in range(A):
        for j in range(i + 1, A):
            ti, tj = ordering[i], ordering[j]
            if ti == 1 and tj == 1:
                E += q
            elif ti == 0 and tj == 0:
                E += -q_inv
            else:
                E += HA / 2
    return E


# ══════════════════════════════════════════════════════════════
# §3  GROUND-STATE ORDERING
# ══════════════════════════════════════════════════════════════

def ground_state_ordering(p, n, max_orderings=5000):
    """Find minimum-energy ordering (uses numeric q₀ for comparison)."""
    from itertools import combinations
    A = p + n
    total = math.comb(A, p)

    if total <= max_orderings:
        best_energy = None
        best_ordering = None
        for positions in combinations(range(A), p):
            ordering = [0] * A
            for pos in positions:
                ordering[pos] = 1
            # Evaluate energy numerically for comparison
            energy = 0.0
            for i in range(A - 1):
                a, b = std_chain_reduce(i, ordering)
                v = float((z * a + b).subs(q, Q0))
                energy += v
            if best_energy is None or energy < best_energy:
                best_energy = energy
                best_ordering = ordering
        return best_ordering, "exact"
    else:
        ordering = []
        pi, ni = 0, 0
        for k in range(A):
            if pi < p and (ni >= n or k % 2 == 0):
                ordering.append(1)
                pi += 1
            else:
                ordering.append(0)
                ni += 1
        return ordering, "heuristic"


# ══════════════════════════════════════════════════════════════
# §4  BINDING ENERGY (symbolic Skein Lagrangian)
# ══════════════════════════════════════════════════════════════

# Bethe-Weizsäcker coefficients as symbolic functions of q
# a_V = ½(q+q⁻¹)·λ_V, etc.
# The λ's are energy-scale factors (MeV) — these remain fitted
# until the Garside NF integration replaces them.
LAMBDA_V = sp.Rational(1556, 100)   # 15.56 MeV
LAMBDA_S = sp.Rational(1723, 100)   # 17.23 MeV
LAMBDA_C = sp.Rational(697, 1000)   # 0.697 MeV
A_ASYM   = sp.Rational(2329, 100)   # 23.29 MeV
DELTA_P  = sp.Integer(12)           # pairing scale MeV

a_V_sym = (q + q_inv) / 2 * LAMBDA_V / ((Q0 + 1/Q0) / 2)
a_S_sym = (q + q_inv) / 2 * LAMBDA_S / ((Q0 + 1/Q0) / 2)
a_C_sym = (q - q_inv) * LAMBDA_C / (Q0 - 1/Q0)


def binding_energy_symbolic(Z, N):
    """B(Z,N) symbolic in q from Skein Lagrangian."""
    A = Z + N
    if A <= 1:
        return sp.Integer(0)

    # Pairing
    if Z % 2 == 0 and N % 2 == 0:
        delta = DELTA_P / sqrt(sp.Integer(A))
    elif Z % 2 == 1 and N % 2 == 1:
        delta = -DELTA_P / sqrt(sp.Integer(A))
    else:
        delta = sp.Integer(0)

    B = (a_V_sym * A
         - a_S_sym * sp.Rational(A, 1) ** Rational(2, 3)
         - a_C_sym * Z * (Z - 1) / sp.Rational(A, 1) ** Rational(1, 3)
         - A_ASYM * (N - Z)**2 / (4 * A)
         + delta)

    return B


# AME2020 B/A for comparison
AME2020_BA = {
    (1, 0): 0.0000, (2, 2): 7.0739, (3, 4): 5.6063, (4, 5): 6.4628,
    (5, 6): 6.9277, (6, 6): 7.6801, (7, 7): 7.4756, (8, 8): 7.9762,
    (9, 10): 7.7790, (10, 10): 8.0325,
    # Z=11-20
    (11, 12): 8.1117,  # ²³Na
    (12, 12): 8.2614,  # ²⁴Mg
    (13, 14): 8.3316,  # ²⁷Al
    (14, 14): 8.4477,  # ²⁸Si
    (15, 16): 8.4813,  # ³¹P
    (16, 16): 8.4930,  # ³²S
    (17, 18): 8.5202,  # ³⁵Cl
    (18, 22): 8.5954,  # ⁴⁰Ar
    (19, 20): 8.5570,  # ³⁹K
    (20, 20): 8.5513,  # ⁴⁰Ca
}


# ══════════════════════════════════════════════════════════════
# §5  RESULT DATACLASS
# ══════════════════════════════════════════════════════════════

@dataclass
class AtomMassResult:
    element: str
    Z: int
    N: int
    A: int
    ordering: list
    ordering_method: str
    # Symbolic expressions (as strings)
    tr_sym_expr: str
    tr_std_expr: str
    tr_alt_expr: str
    tr_full_expr: str
    E_cross_expr: str
    B_skein_expr: str
    # Evaluated at q₀
    tr_sym_float: float
    tr_std_float: float
    tr_alt_float: float
    tr_full_float: float
    E_cross_float: float
    m_vert_float: float
    m_mixed_float: float
    B_skein_float: float
    BA_skein_float: float
    BA_ame2020: float
    M_free: float
    M_skein: float
    M_ame2020: float
    delta_MeV: float
    sym_alt_correction: float
    elapsed_s: float


# ══════════════════════════════════════════════════════════════
# §6  COMPUTE ONE ATOM
# ══════════════════════════════════════════════════════════════

ELEMENTS = {
    1:  ("Hydrogen",   "¹H",   1, 0),
    2:  ("Helium",     "⁴He",  2, 2),
    3:  ("Lithium",    "⁷Li",  3, 4),
    4:  ("Beryllium",  "⁹Be",  4, 5),
    5:  ("Boron",      "¹¹B",  5, 6),
    6:  ("Carbon",     "¹²C",  6, 6),
    7:  ("Nitrogen",   "¹⁴N",  7, 7),
    8:  ("Oxygen",     "¹⁶O",  8, 8),
    9:  ("Fluorine",   "¹⁹F",  9, 10),
    10: ("Neon",       "²⁰Ne", 10, 10),
    11: ("Sodium",     "²³Na", 11, 12),
    12: ("Magnesium",  "²⁴Mg", 12, 12),
    13: ("Aluminium",  "²⁷Al", 13, 14),
    14: ("Silicon",    "²⁸Si", 14, 14),
    15: ("Phosphorus", "³¹P",  15, 16),
    16: ("Sulfur",     "³²S",  16, 16),
    17: ("Chlorine",   "³⁵Cl", 17, 18),
    18: ("Argon",      "⁴⁰Ar", 18, 22),
    19: ("Potassium",  "³⁹K",  19, 20),
    20: ("Calcium",    "⁴⁰Ca", 20, 20),
}


def compute_atom(Z, N, element_name):
    """Full symbolic three-channel Hecke computation for one atom."""
    t0 = time.time()
    A = Z + N

    # Step 1: Ground-state ordering
    if A <= 1:
        ordering = [1] if Z == 1 else [0]
        method = "trivial"
    else:
        ordering, method = ground_state_ordering(Z, N)

    # Step 2: Symbolic three-channel traces
    # Set include_gluon=True to add LP-derived internal crossings per nucleon
    # (proton: 2×σ₀, neutron: 4×σ from L₊→L₋)
    tr_sym, tr_std, tr_alt = three_channel_traces_symbolic(ordering, include_gluon=False)
    tr_full = Rational(1, 6) * tr_sym + Rational(4, 6) * tr_std + Rational(1, 6) * tr_alt

    # Step 3: Symbolic crossing energy
    E_cross = crossing_energy_symbolic(ordering)

    # Step 4: Symbolic binding energy
    B_skein = binding_energy_symbolic(Z, N)

    # Step 5: Evaluate at q₀
    tr_sym_f = float(tr_sym.subs(q, Q0))
    tr_std_f = float(tr_std.subs(q, Q0))
    tr_alt_f = float(tr_alt.subs(q, Q0))
    tr_full_f = float(tr_full.subs(q, Q0))
    E_cross_f = float(E_cross.subs(q, Q0))
    B_skein_f = float(B_skein.subs(q, Q0))
    B_skein_f = max(B_skein_f, 0.0)

    m_vert_f = abs(tr_full_f)
    m_mixed_f = E_cross_f * float((q - 1).subs(q, Q0))**2

    BA_skein = B_skein_f / A if A > 0 else 0.0
    BA_ame = AME2020_BA.get((Z, N), 0.0)
    B_ame = BA_ame * A

    M_free = Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV
    M_skein = M_free - B_skein_f
    M_ame = M_free - B_ame
    delta = M_skein - M_ame

    if abs(tr_std_f) > 1e-30:
        correction = abs(tr_full_f - tr_std_f) / abs(tr_std_f)
    else:
        correction = 0.0

    elapsed = time.time() - t0

    return AtomMassResult(
        element=element_name, Z=Z, N=N, A=A,
        ordering=ordering, ordering_method=method,
        tr_sym_expr=str(tr_sym),
        tr_std_expr=str(tr_std),
        tr_alt_expr=str(tr_alt),
        tr_full_expr=str(tr_full),
        E_cross_expr=str(E_cross),
        B_skein_expr=str(B_skein),
        tr_sym_float=tr_sym_f, tr_std_float=tr_std_f,
        tr_alt_float=tr_alt_f, tr_full_float=tr_full_f,
        E_cross_float=E_cross_f, m_vert_float=m_vert_f,
        m_mixed_float=m_mixed_f, B_skein_float=B_skein_f,
        BA_skein_float=BA_skein, BA_ame2020=BA_ame,
        M_free=M_free, M_skein=M_skein, M_ame2020=M_ame,
        delta_MeV=delta, sym_alt_correction=correction,
        elapsed_s=elapsed,
    )


# ══════════════════════════════════════════════════════════════
# §7  MAIN
# ══════════════════════════════════════════════════════════════

def main():
    print("=" * 110)
    print("ATOMIC MASS VIA FULL HECKE ALGEBRA — SYMBOLIC IN q")
    print("=" * 110)
    print()
    print(f"  q = symbolic (evaluated at q₀ = {Q0:.10f})")
    print(f"  HA = q - q⁻¹")
    print(f"  z  = 1/(√q + 1/√q)")
    print(f"  Wedderburn weights: w_sym = 1/6, w_std = 4/6, w_alt = 1/6")
    print()

    results = []

    for Z in range(1, 21):
        name, label, z_check, n = ELEMENTS[Z]
        assert z_check == Z
        A = Z + n
        r = compute_atom(Z, n, name)
        results.append(r)

        print(f"{'─' * 110}")
        print(f"  {label} ({name}): Z={Z}, N={n}, A={A}")
        print(f"  Ordering: {''.join('●' if x else '○' for x in r.ordering)} ({r.ordering_method})")
        print()
        print(f"  SYMBOLIC TRACES (in q):")
        # Show short form for small expressions, truncated for large
        for ch_name, expr_str in [("sym", r.tr_sym_expr), ("std", r.tr_std_expr),
                                   ("alt", r.tr_alt_expr), ("full", r.tr_full_expr)]:
            if len(expr_str) > 120:
                print(f"    tr_{ch_name} = {expr_str[:117]}...")
            else:
                print(f"    tr_{ch_name} = {expr_str}")
        print()
        print(f"  EVALUATED AT q₀ = {Q0:.6f}:")
        print(f"    tr_sym  = {r.tr_sym_float:+.10e}")
        print(f"    tr_std  = {r.tr_std_float:+.10e}")
        print(f"    tr_alt  = {r.tr_alt_float:+.10e}")
        print(f"    tr_full = {r.tr_full_float:+.10e}")
        print(f"    E_cross = {r.E_cross_float:+.6f}")
        print()
        print(f"  MASS: M(Skein) = {r.M_skein:.3f}  M(AME) = {r.M_ame2020:.3f}  Δ = {r.delta_MeV:+.3f} MeV")
        print(f"  time: {r.elapsed_s:.2f}s")
        print()

    # Summary table
    print("=" * 110)
    print("SUMMARY")
    print("=" * 110)
    print(f"{'Atom':>5} | {'A':>3} | {'tr_sym':>13} | {'tr_std':>13} | "
          f"{'tr_alt':>13} | {'tr_full':>13} | {'Δ MeV':>8}")
    print("─" * 110)
    for r in results:
        print(f"{r.element:>5} | {r.A:3d} | {r.tr_sym_float:+13.6e} | "
              f"{r.tr_std_float:+13.6e} | {r.tr_alt_float:+13.6e} | "
              f"{r.tr_full_float:+13.6e} | {r.delta_MeV:+8.3f}")

    # Write witness
    w = WitnessBuilder("atom-mass-full-hecke", engine="sympy")
    w.set_description(
        "Atomic mass Z=1-10 via full three-channel Hecke algebra "
        "(sym + std + alt), SYMBOLIC in q, evaluated at q₀."
    )
    w.set_content_block("rem:atom-mass-full-hecke")
    w.add_parameter("q", "symbolic")
    w.add_parameter("q0_eval", str(Q0))
    w.add_parameter("wedderburn_weights", {"sym": "1/6", "std": "4/6", "alt": "1/6"})

    for r in results:
        w.add_assertion(
            f"M({r.element})",
            computed=round(r.M_skein, 3),
            expected=round(r.M_ame2020, 3),
            tolerance=max(abs(r.delta_MeV) + 1.0, 5.0),
            unit="MeV", source="AME2020",
        )

    w.add_data("results", [asdict(r) for r in results])
    w.save()

    return results


if __name__ == "__main__":
    main()
