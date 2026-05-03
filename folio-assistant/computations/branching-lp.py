#!/usr/bin/env python3
# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Symbolic LP via S₃ᴬ branching — all in q.

The Garside matrix element for A nucleons decomposes as a PRODUCT
of per-nucleon factors via the branching S_{3A} → S₃ × ... × S₃.

Each nucleon m chooses a channel c_m ∈ {triv, conf, unconf, sign}.
The total matrix element is: Π_m G_{type(m)}(c_m)
The T_{2,3} eigenvalue is: Π_m λ(c_m)

For Z protons + N neutrons, each configuration is a map
  (nucleon → channel), and the physical state is determined
  by the LP dual selecting the optimal configuration.

All expressions are exact rational functions of q.

Usage:
    cd folio-assistant/computations && python3 branching-lp.py
"""

import sympy as sp
from sympy import cancel, factor, Rational
from itertools import product as cartesian_product
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0_num
from experimental_constants import M_E_MEV, Q_TRITIUM_MEV, Q_NEUTRON_MEV

q = sp.Symbol('q', positive=True)
qi = 1/q
h = q - qi

# ══════════════════════════════════════════════════════════════
#  PER-NUCLEON BUILDING BLOCKS (from symbolic computation)
# ══════════════════════════════════════════════════════════════

# Channel names and T_{2,3} eigenvalues
CHANNELS = ['triv', 'conf', 'unconf', 'sign']
T23_EIGENVALUE = {
    'triv':   q**3,
    'conf':   qi,       # q⁻¹ (min |λ|, confined)
    'unconf': -q,       # -q (unconfined)
    'sign':   -qi**3,   # -q⁻³
}

# Garside ⟨v|Δ₃|v⟩ per channel per nucleon type
G_PROTON = {
    'triv':   (q**2 + 1)**2 / (4*q),
    'conf':   (3*q**2 + 1) / (4*q**3),
    'unconf': -q*(q**2 + 3) / 4,
    'sign':   -(q**2 + 1)**2 / (4*q**3),
}

G_NEUTRON = {
    'triv':   (q**2 + 1)**2 / (4*q**3),
    'conf':   -(q**8 - q**6 - 2*q**4 - 5*q**2 - 1) / (4*q**3*(q**2 + 1)),
    'unconf': -(q**8 + 5*q**6 + 2*q**4 + q**2 - 1) / (4*q**3*(q**2 + 1)),
    'sign':   -(q**2 + 1)**2 / (4*q),
}


def nucleon_factor(nucleon_type, channel):
    """Garside matrix element for one nucleon in a specific channel."""
    if nucleon_type == 'p':
        return G_PROTON[channel]
    else:
        return G_NEUTRON[channel]


# ══════════════════════════════════════════════════════════════
#  A-NUCLEON GARSIDE VIA BRANCHING
# ══════════════════════════════════════════════════════════════

def all_configurations(Z, N):
    """Generate all channel configurations for Z protons + N neutrons.

    Each configuration assigns a channel to each nucleon.
    Returns: list of (config_tuple, eigenvalue, me_parent, me_daughter)

    For beta⁻ decay: one neutron → proton.
    Parent: Z protons + N neutrons
    Daughter: (Z+1) protons + (N-1) neutrons
    """
    A = Z + N
    nucleon_types_par = ['p'] * Z + ['n'] * N
    nucleon_types_dau = ['p'] * (Z+1) + ['n'] * (N-1)

    configs = []
    for config in cartesian_product(CHANNELS, repeat=A):
        # T_{2,3} eigenvalue
        eigval = sp.Integer(1)
        for c in config:
            eigval *= T23_EIGENVALUE[c]
        eigval = cancel(eigval)

        # Parent matrix element
        me_par = sp.Integer(1)
        for m, c in enumerate(config):
            me_par *= nucleon_factor(nucleon_types_par[m], c)
        me_par = cancel(me_par)

        # Daughter matrix element
        me_dau = sp.Integer(1)
        for m, c in enumerate(config):
            me_dau *= nucleon_factor(nucleon_types_dau[m], c)
        me_dau = cancel(me_dau)

        configs.append((config, eigval, me_par, me_dau))

    return configs


def compute_decay_symbolic(Z_par, N_par, name):
    """Compute all channel contributions for a beta decay."""
    A = Z_par + N_par
    n_configs = 4**A

    print(f"\n{'━' * 70}")
    print(f"  {name} (Z={Z_par}, N={N_par}, A={A}, {n_configs} configurations)")
    print(f"{'━' * 70}")

    configs = all_configurations(Z_par, N_par)

    # Group by eigenvalue (configs with same eigenvalue contribute to same channel)
    by_eigval = {}
    for config, eigval, me_par, me_dau in configs:
        # Evaluate eigenvalue numerically for grouping
        eigval_num = complex(eigval.subs(q, q0_num))
        key = round(eigval_num.real, 6)  # round for grouping

        if key not in by_eigval:
            by_eigval[key] = {'eigval': eigval, 'eigval_num': eigval_num,
                              'me_par_sum': sp.Integer(0),
                              'me_dau_sum': sp.Integer(0),
                              'count': 0}
        by_eigval[key]['me_par_sum'] += me_par
        by_eigval[key]['me_dau_sum'] += me_dau
        by_eigval[key]['count'] += 1

    # For each eigenvalue group, compute Δme
    results = []
    print(f"\n  {'λ (T23)':>12s} | {'#configs':>8s} | {'Σme_par':>12s} | {'Σme_dau':>12s} | {'Δme':>12s}")
    print(f"  {'':->65s}")

    for key in sorted(by_eigval.keys()):
        info = by_eigval[key]
        me_par_sum = cancel(info['me_par_sum'])
        me_dau_sum = cancel(info['me_dau_sum'])
        dme = cancel(me_dau_sum - me_par_sum)
        dme_num = float(dme.subs(q, q0_num))
        me_par_num = float(me_par_sum.subs(q, q0_num))
        me_dau_num = float(me_dau_sum.subs(q, q0_num))

        print(f"  {info['eigval_num'].real:>+12.4f} | {info['count']:>8d} | "
              f"{me_par_num:>+12.6f} | {me_dau_num:>+12.6f} | {dme_num:>+12.6f}")

        results.append({
            'eigval': info['eigval'],
            'eigval_num': key,
            'dme': dme,
            'dme_num': dme_num,
            'count': info['count'],
        })

    # Total Δme (summed over ALL configurations)
    total_dme = sp.Integer(0)
    for r in results:
        total_dme += r['dme']
    total_dme = cancel(total_dme)
    total_dme_num = float(total_dme.subs(q, q0_num))

    print(f"\n  Total Σ Δme = {total_dme_num:+.10f}")
    print(f"  Q = |Σ Δme| × m_e = {abs(total_dme_num) * M_E_MEV:.6f} MeV")

    # Factor the total
    total_factored = factor(total_dme)
    total_str = str(total_factored)
    if len(total_str) < 300:
        print(f"  Σ Δme(q) = {total_factored}")
    else:
        print(f"  Σ Δme(q) = [{len(total_str)} chars]")
        # Check (q²-1) factor
        reduced = cancel(total_dme / (q**2 - 1))
        print(f"  Has (q²-1) factor: {cancel(total_dme - (q**2-1)*reduced) == 0}")

    # The min-eigenvalue configuration
    min_eigval_config = min(results, key=lambda r: abs(r['eigval_num']))
    print(f"\n  Min |λ| channel: λ ≈ {min_eigval_config['eigval_num']:.4f}, "
          f"Δme = {min_eigval_config['dme_num']:+.6f}")

    return results, total_dme


# ══════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("SYMBOLIC LP VIA S₃ᴬ BRANCHING")
    print(f"q₀ = {q0_num:.15f}, m_e = {M_E_MEV} MeV")
    print("=" * 70)

    # Free neutron (A=1)
    r_neutron, dme_neutron = compute_decay_symbolic(0, 1, 'n→p (free neutron)')

    # Tritium (A=3)
    r_tritium, dme_tritium = compute_decay_symbolic(1, 2, '³H→³He (tritium)')

    # ⁶He (A=6, 4096 configurations — still fast since each is just a product)
    r_6he, dme_6he = compute_decay_symbolic(2, 4, '⁶He→⁶Li')

    # ══════════════════════════════════════════════════════════
    #  LP: FIND WEIGHTS PER EIGENVALUE CHANNEL
    # ══════════════════════════════════════════════════════════

    print(f"\n{'━' * 70}")
    print(f"  SYMBOLIC LP")
    print(f"{'━' * 70}")

    # The min |λ| channel (all nucleons in 'conf') is the LP optimum.
    # Its Δme for each decay gives Q directly:
    # Q = Δme(conf_all) × m_e × y

    # All-confined config: every nucleon in 'conf' channel
    print("\n  ALL-CONFINED configuration (every nucleon in q⁻¹ channel):")
    for name, Z, N, Q_exp in [('n→p', 0, 1, Q_NEUTRON_MEV),
                                ('³H', 1, 2, Q_TRITIUM_MEV),
                                ('⁶He', 2, 4, 3.508)]:
        A = Z + N
        nucleon_types_par = ['p'] * Z + ['n'] * N
        nucleon_types_dau = ['p'] * (Z+1) + ['n'] * (N-1)

        me_par = sp.Integer(1)
        me_dau = sp.Integer(1)
        eigval = qi**A
        for m in range(A):
            me_par *= nucleon_factor(nucleon_types_par[m], 'conf')
            me_dau *= nucleon_factor(nucleon_types_dau[m], 'conf')

        dme_conf = cancel(me_dau - me_par)
        dme_conf_num = float(dme_conf.subs(q, q0_num))
        Q_conf = abs(dme_conf_num) * M_E_MEV

        print(f"    {name:>5s}: Δme = {dme_conf_num:>+12.8f}, "
              f"Q = {Q_conf:.6f} MeV (exp: {Q_exp:.6f}, "
              f"ratio: {Q_conf/Q_exp:.2f})")

        # Show symbolic expression
        dme_f = factor(dme_conf)
        dme_str = str(dme_f)
        if len(dme_str) < 200:
            print(f"          Δme(q) = {dme_f}")

    print(f"\n  The all-confined Δme is a PRODUCT of per-nucleon factors.")
    print(f"  Each factor is a clean rational function of q.")
    print(f"  Q = |Π_protons G_p(conf) × Π_neutrons G_n(conf) [dau-par]| × m_e")
