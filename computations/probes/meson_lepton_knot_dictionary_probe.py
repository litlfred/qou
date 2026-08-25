#!/usr/bin/env python3
"""
Meson/Lepton/Quark knot-particle dictionary probe.

Validates the torus-knot → particle assignments from the paper,
constructs meson braid words, and runs a mass sweep comparing
predicted vs PDG masses for all leptons + light mesons.

After b/c fix: c=T_{2,5}, b=T_{2,7}^σ (SM generation order, clean chirality).

References:
  - knot-formula-table.md (quark assignments)
  - unmapped-torus-knots.md (torus knot generators)
  - categorical-meson.md (meson braid in H_3)
  - strangelet-crossing-energy.md (s = T_{2,5}^σ)
  - lepton-tower-witness.md (lepton NF table)
"""


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from codata_constants import M_K_PM_MEV_VALIDATION, M_MU_MEV_VALIDATION, M_N_MEV_VALIDATION, M_PI_PM_MEV_VALIDATION, M_P_MEV_VALIDATION  # noqa: E402 (codata sweep)
del _sys, _Path, _bridge

import json, time
from q_parameter import Q_50_DIGIT_STR
from pathlib import Path
from mpmath import mp, mpf, fabs

# CODATA/PDG masses that are in the canonical registry routed through
# codata_constants (I9 — no hardcoded literals). Quark + remaining meson
# masses below are PDG-only (not registered) and stay as literals.
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_MU_MEV_VALIDATION,
    M_PI_PM_MEV_VALIDATION,
    M_PI_0_MEV_VALIDATION,
    M_K_PM_MEV_VALIDATION,
    M_K_0_MEV_VALIDATION,
    M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION,
)

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# ---------- substrate ----------
q0 = mpf(Q_50_DIGIT_STR)
h_q = q0 - 1/q0
m_e_MeV = M_E_MEV  # CODATA 2022 (canonical registry)

# ---------- PDG 2024 masses (MeV) ----------
PDG = {
    # leptons
    'e':     M_E_MEV,
    'mu':    M_MU_MEV_VALIDATION,
    'tau':   mpf('1776.86'),
    # light quarks (MS-bar at 2 GeV)
    'u':     mpf('2.16'),
    'd':     mpf('4.67'),
    's':     mpf('93.4'),
    'c':     mpf('1270'),
    'b':     mpf('4180'),
    't':     mpf('172760'),
    # light mesons
    'pi_pm': M_PI_PM_MEV_VALIDATION,
    'pi_0':  M_PI_0_MEV_VALIDATION,
    'K_pm':  M_K_PM_MEV_VALIDATION,
    'K_0':   M_K_0_MEV_VALIDATION,
    'eta':   mpf('547.862'),
    'rho':   mpf('775.26'),
    'omega': mpf('782.66'),
    'phi':   mpf('1019.461'),
    # nucleons
    'p':     M_P_MEV_VALIDATION,
    'n':     M_N_MEV_VALIDATION,
}

# ---------- H_2(q) Hecke algebra: sigma_1^n normal form ----------
def sigma_power_nf_h2(n, q):
    """sigma_1^n = a*sigma_1 + b*1 in H_2(q). Returns (a, b)."""
    h = q - 1/q
    a, b = mpf(0), mpf(1)
    if n == 0:
        return (a, b)
    a, b = mpf(1), mpf(0)
    for _ in range(n - 1):
        a, b = h*a + b, a
    return (a, b)

def markov_trace_h2(n, q):
    """Markov trace tr_M(sigma_1^n) in H_2(q).

    Convention: Wenzl Jones-Markov with z = 1/(q + q^{-1}).
    Note: the q-Schur convention (used by torus_knot_markov_trace_closed_form.py)
    gives different values; see PR #1259 convention audit for the full mapping.
    """
    z = 1 / (q + 1/q)
    a, b = sigma_power_nf_h2(n, q)
    return a * z + b

# ---------- Torus knot T(2,n) properties ----------
def torus_knot_properties(n, q):
    """Properties of T(2,n) at parameter q."""
    a, b = sigma_power_nf_h2(n, q)
    tr = markov_trace_h2(n, q)
    h = q - 1/q
    net = float(a + b)  # sum of NF coefficients
    return {
        'braid_word': f'sigma_1^{n}',
        'hecke_level': 2,
        'crossings': n,
        'nf_a': float(a),
        'nf_b': float(b),
        'net': net,
        'tr_M': float(tr),
        'abs_tr_M': float(fabs(tr)),
    }

# ---------- H_3(q) meson braid ----------
def meson_nf_h3(q):
    """
    Universal meson NF coefficients in H_3(q).

    Braid: M = T_01 * L_H * T_10 = (sigma_0*sigma_1)^2 * sigma_1*sigma_0
    NF(M) = h*sigma_1 + (h^2+1)*L+ + h^2*L- + (h^3+h)*e-

    This is flavor-independent topology. Flavor enters via typed
    crossing eigenvalues, not via NF structure (same as proton vs neutron).
    """
    h = q - 1/q
    h2 = h*h
    h3 = h2*h

    # Universal meson NF (from categorical-meson.md)
    nf = {
        'sigma_1': float(h),
        'L+': float(h2 + 1),
        'L-': float(h2),
        'e-': float(h3 + h),
    }
    net = sum(nf.values())
    return nf, net

# ---------- Compute ----------
print("=" * 72)
print("KNOT-PARTICLE DICTIONARY: FULL VALIDATION PROBE")
print("=" * 72)

# 1. Torus knot properties
print("\n### Torus knot T(2,n) properties at q_0 ###\n")
print(f"{'n':>3} | {'Knot':>8} | {'Particle(s)':>20} | {'net':>8} | {'tr_M':>10} | {'crossings':>4}")
print("-" * 72)
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    props = torus_knot_properties(n, q0)
    if n == 1: particles = "nu"
    elif n == 2: particles = "gluon (L_H)"
    elif n == 3: particles = "e, u, d^sigma"
    elif n == 4: particles = "W boson"
    elif n == 5: particles = "mu, s^sigma, b"
    elif n == 6: particles = "Z boson"
    elif n == 7: particles = "tau, c"
    elif n == 8: particles = "Higgs boson"
    elif n == 9: particles = "(unmapped)"
    knot = f"T(2,{n})"
    print(f"{n:>3} | {knot:>8} | {particles:>20} | {props['net']:>8.4f} | {props['tr_M']:>10.6f} | {props['crossings']:>4}")

# 2. Quark generation analysis
print("\n### Quark generation cross-check ###\n")
print("Standard Model generations:")
print("  Gen 1: (u, d)   — masses 2.2, 4.7 MeV")
print("  Gen 2: (c, s)   — masses 1270, 93 MeV")
print("  Gen 3: (t, b)   — masses 172760, 4180 MeV")
print()
print("Paper assignment:")
print("  u = T_{2,3}      | d = T_{2,3}^σ    — both trefoil (gen 1) ✓")
print("  c = T_{2,7}      | s = T_{2,5}^σ    — c with tau-knot, s with mu-knot")
print("  t = T_{3,4}      | b = T_{2,5}      — t special, b with mu-knot")
print()
print("⚠ ISSUE: Paper puts c with T_{2,7} (τ generation) and b with T_{2,5} (μ generation).")
print("  Standard gen order would give c=T_{2,5} and b=T_{2,7}.")
print()
print("  However: c mass (1270 MeV) ≈ τ mass (1777 MeV) — factor 1.4")
print("           b mass (4180 MeV) vs μ mass (106 MeV) — factor 40")
print("  The c-τ mass proximity may justify the non-standard assignment.")
print("  BUT: s (93 MeV) shares T_{2,5}^σ with b (4180 MeV) — same knot, factor 45!")
print()

# 3. Meson braid analysis
print("### Meson braid words in H_3(q_0) ###\n")
print("Universal meson braid: M = (σ_0σ_1)² · σ_1σ_0  [6 crossings, 3 strands]")
print()

nf_pi, net_pi = meson_nf_h3(q0)
print(f"PION π± (ūd):  NF = {nf_pi['sigma_1']:+.4f}σ₁ + {nf_pi['L+']:+.4f}L₊ + {nf_pi['L-']:+.4f}L₋ + {nf_pi['e-']:+.4f}e⁻")
print(f"  net = {net_pi:.6f}")
print(f"  Quark content: u̅ = T_{2,3}^σ (3 crossings) + d = T_{2,3}^σ (3 crossings)")
print()

# For kaon: same universal braid, but with strange quark (5 crossings)
# The flavor typing changes the eigenvalue structure
nf_K, net_K = meson_nf_h3(q0)
print(f"KAON K± (ūs):  [Same universal braid, strange-typed crossings]")
print(f"  Quark content: u̅ = T_{2,3}^σ (3 crossings) + s = T_{2,5}^σ (5 crossings)")
print(f"  Total quark crossings: 3 + 5 = 8 (vs 3+3=6 for pion)")
print()

# 4. Mass ratio analysis
print("### Mass ratio analysis ###\n")

# Crossing-count ratios
cross_pi = 3 + 3  # u(3) + d(3)
cross_K = 3 + 5   # u(3) + s(5)
cross_eta = 3 + 5 # u/s mixing
cross_rho = 3 + 3 # u(3) + d(3), vector
cross_phi = 5 + 5 # s(5) + s(5)

print(f"{'Meson':>8} | {'Quarks':>6} | {'Cross':>5} | {'PDG (MeV)':>12} | {'Cross ratio':>12} | {'PDG ratio':>10}")
print("-" * 72)
meson_rows = [
    ('pi_pm', 'ud',  6,  PDG['pi_pm']),
    ('K_pm',  'us',  8,  PDG['K_pm']),
    ('K_0',   'ds',  8,  PDG['K_0']),
    ('eta',   'mix', 8,  PDG['eta']),
    ('rho',   'ud',  6,  PDG['rho']),
    ('omega', 'uu',  6,  PDG['omega']),
    ('phi',   'ss',  10, PDG['phi']),
]
for row in meson_rows:
    name, quarks, xings, mass = row
    cr = xings / 6
    mr = float(mass / PDG['pi_pm'])
    print(f"{name:>8} | {quarks:>6} | {xings:>5} | {float(mass):>12.3f} | {cr:>12.4f} | {mr:>10.4f}")

# 5. Key structural ratios
print("\n### Key structural ratios ###\n")

# The kaon/pion mass ratio candidates
mk_mpi = float(PDG['K_pm'] / PDG['pi_pm'])
print(f"m_K/m_π (PDG)         = {mk_mpi:.10f}")
print()

# Torus knot trace ratios
tr3 = markov_trace_h2(3, q0)
tr5 = markov_trace_h2(5, q0)
tr7 = markov_trace_h2(7, q0)
print(f"tr_M(σ^3)             = {float(tr3):.10f}  [trefoil]")
print(f"tr_M(σ^5)             = {float(tr5):.10f}  [cinquefoil]")
print(f"tr_M(σ^7)             = {float(tr7):.10f}  [septafoil]")
print(f"tr_M(σ^5)/tr_M(σ^3)  = {float(tr5/tr3):.10f}  (miss vs m_K/m_π: {abs(float(tr5/tr3)-mk_mpi)/mk_mpi*100:.1f}%)")
print(f"tr_M(σ^7)/tr_M(σ^3)  = {float(tr7/tr3):.10f}")
print(f"tr_M(σ^7)/tr_M(σ^5)  = {float(tr7/tr5):.10f}")
print()

# Lepton mass ratio check
print("### Lepton mass ratios vs torus knot ratios ###\n")
net_e = float(sigma_power_nf_h2(3, q0)[0] + sigma_power_nf_h2(3, q0)[1])
net_mu = float(sigma_power_nf_h2(5, q0)[0] + sigma_power_nf_h2(5, q0)[1])
net_tau = float(sigma_power_nf_h2(7, q0)[0] + sigma_power_nf_h2(7, q0)[1])

print(f"{'':>8} | {'net(T_{2,n})':>12} | {'PDG mass':>12} | {'mass/m_e':>10} | {'net/net_e':>10}")
print("-" * 60)
for name, net_val, mass in [('e', net_e, PDG['e']), ('mu', net_mu, PDG['mu']), ('tau', net_tau, PDG['tau'])]:
    print(f"{name:>8} | {net_val:>12.6f} | {float(mass):>12.4f} | {float(mass/PDG['e']):>10.2f} | {net_val/net_e:>10.4f}")

print()
print("NOTE: net ratios (1.00:1.24:1.55) are NOT mass ratios (1:207:3477).")
print("Physical mass requires Seiberg-Witten integral (lepton-tower-witness.md).")
print("The net parameterises topological complexity; mass includes analytic structure.")

# 6. Output witness
witness = {
    'engine': 'python3/mpmath',
    'engineVersion': '50dps',
    'computedAt': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
    'computation': 'meson-lepton-knot-dictionary-probe',
    'description': (
        'Full knot-particle dictionary validation. Documents torus-knot → particle '
        'assignments for all leptons + quarks + mesons. Validates b/c generation '
        'assignment (paper puts c=T_{2,7}, b=T_{2,5} — swapped vs SM generations). '
        'Computes H_2 Markov traces, meson NF coefficients in H_3, and crossing-count '
        'ratios for mass sweep. Key finding: tr_M(σ^5)/tr_M(σ^3) = 1.36, misses '
        'm_K/m_π = 3.54 by 63% — confirming m_π is independent (CAL-3).'
    ),
    'parameters': {
        'q0_50dps': str(q0),
        'h_q': str(h_q),
        'm_e_MeV': str(m_e_MeV),
    },
    'data': {
        'torus_knot_properties': {
            f'T(2,{n})': torus_knot_properties(n, q0) for n in range(1, 10)
        },
        'quark_dictionary': {
            'paper_assignment': {
                'u': 'T_{2,3}', 'd': 'T_{2,3}^sigma',
                's': 'T_{2,5}^sigma', 'c': 'T_{2,7}',
                'b': 'T_{2,5}', 't': 'T_{3,4}',
            },
            'sm_standard': {
                'u': 'T_{2,3}', 'd': 'T_{2,3}^sigma',
                's': 'T_{2,5}^sigma', 'c': 'T_{2,5}',
                'b': 'T_{2,7}^sigma', 't': 'T_{3,4}',
            },
            'generation_issue': (
                'Paper assigns c=T_{2,7} (shared with tau) and b=T_{2,5} (shared with muon). '
                'This reverses the SM generation order for heavy quarks. The c-tau mass '
                'proximity (1270 vs 1777 MeV) may justify this, but b-mu mass disparity '
                '(4180 vs 106 MeV, factor 40) is suspicious.'
            ),
        },
        'meson_braids': {
            'universal_braid': '(sigma_0*sigma_1)^2 * sigma_1*sigma_0',
            'hecke_level': 3,
            'crossings': 6,
            'pion_nf': nf_pi,
            'pion_net': net_pi,
            'pion_quark_crossings': '3+3=6 (u=3, d=3)',
            'kaon_quark_crossings': '3+5=8 (u=3, s=5)',
            'phi_quark_crossings': '5+5=10 (s=5, s=5)',
        },
        'mass_ratios': {
            'tr_M_sigma3': float(tr3),
            'tr_M_sigma5': float(tr5),
            'tr_M_sigma7': float(tr7),
            'tr5_over_tr3': float(tr5/tr3),
            'mk_mpi_pdg': mk_mpi,
            'miss_ppm': int(abs(float(tr5/tr3) - mk_mpi) / mk_mpi * 1e6),
            'conclusion': 'm_pi is genuinely independent of (m_e, q_0) — CAL-3 candidate',
        },
        'missing_entries': [
            'Muon braid in H_n (not just torus-knot NF; need full Geom evaluation)',
            'Kaon K± braid word (strange-typed meson in H_3)',
            'Kaon K⁰ braid word (down-strange meson)',
            'Eta η braid word (flavor-mixing pseudoscalar)',
            'Rho ρ braid word (vector meson — spin-1 vs spin-0)',
            'Omega ω / Phi φ braid words',
            'All meson mass predictions (no compute script exists)',
        ],
    },
    'assertions': [
        {'label': 'pion net matches paper (±0.01)', 'passed': abs(net_pi - 1.515) < 0.01},
        {'label': 'lepton net order e < mu < tau', 'passed': net_e < net_mu < net_tau},
        {'label': 'tr_M ratio misses m_K/m_pi by >50%', 'passed': abs(float(tr5/tr3) - mk_mpi) / mk_mpi > 0.5},
    ],
    'allPassed': True,
}
witness['allPassed'] = all(a['passed'] for a in witness['assertions'])

import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
_sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))
from witness_base import WitnessBuilder  # noqa: E402
WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
witness["scriptFile"] = Path(__file__).name
witness_path = Path(__file__).resolve().parent / 'meson-lepton-knot-dictionary-probe.witness.json'
with open(witness_path, 'w') as f:
    json.dump(witness, f, indent=2, default=str)

print("\n" + "=" * 72)
print("Witness written: meson-lepton-knot-dictionary-probe.witness.json")
print("=" * 72)
