"""
Parity-dependent Q-value analysis.

Key finding: spectators contribute zero (unchanged generators have
identical parent/daughter volumes). The systematic error correlates
with nuclear parity:
  - even-even parents: small errors (+0.9%)
  - odd-odd parents: systematic overprediction (+6.6% to +8.5%)
  - odd-A parents: mixed signs

The pairing effect enters through the SHELL FACTOR, not through the
volume ratios themselves. The F_deg2 factor was derived from H₃(q)
representation theory (the degree-2 irrep) and applied uniformly.
But the shell factor should depend on the parity transition.

In β⁻ decay:
  odd-odd → even-even: daughter gains pairing energy
  even-even → odd-odd: daughter loses pairing energy
  odd-A → odd-A: pairing unchanged

The pairing energy difference is absorbed into the shell correction.
"""

import math
import sys
sys.path.insert(0, '.')
from q_parameter import Q, Q_INV, HA, LN_Q, S_SKEIN
from experimental_constants import M_E_MEV

KAPPA = M_E_MEV / 3.0
KAPPA_Q = LN_Q * KAPPA
Z_MARKOV = 1.0 / (math.sqrt(Q) + 1.0/math.sqrt(Q))
S_SK = math.sqrt(Q) - 1.0/math.sqrt(Q)
F_DEG2 = 0.5949
F_PAULI = 0.6382
MAGIC = [2, 8, 20, 28, 50, 82, 126]

def shell_degree(n):
    for i, m in enumerate(MAGIC):
        if n <= m: return 2 if i+1 >= 5 else 1
    return 2

def crossing_coeffs(ti, tj):
    pair = ti + tj
    if pair == 'pp': return (1.0, 0.0)
    elif pair == 'nn': return (Q**2, -Q * S_SK)
    else: return ((1.0 + Q**2)/2.0, -Q * S_SK / 2.0)

def generator_volumes(z, n):
    a = z+n; types = ['p']*z + ['n']*n; vols = []
    for i in range(a-1):
        m = [[1.0, 0.0], [0.0, 1.0]]
        for j in range(i+1, a):
            c, d = crossing_coeffs(types[i], types[j])
            t = [[c*HA+d, c], [c, d]]
            m = [[m[0][0]*t[0][0]+m[0][1]*t[1][0], m[0][0]*t[0][1]+m[0][1]*t[1][1]],
                 [m[1][0]*t[0][0]+m[1][1]*t[1][0], m[1][0]*t[0][1]+m[1][1]*t[1][1]]]
        vols.append(Z_MARKOV * m[0][0] + m[1][0])
    return vols

def parity(z, n):
    if z%2==0 and n%2==0: return "ee"
    elif z%2==1 and n%2==1: return "oo"
    else: return "oA"

def transition_type(z, n):
    par_p = parity(z, n)
    par_d = parity(z+1, n-1)
    return f"{par_p}→{par_d}"

BENCHMARKS = [
    (1,  2,  "³H",       0.01861),
    (6,  8,  "¹⁴C",      0.15648),
    (27, 33, "⁶⁰Co",     0.31817),
    (38, 52, "⁹⁰Sr",     0.54590),
    (55, 82, "¹³⁷Cs",    0.51400),
    (83, 127,"²¹⁰Bi",    1.16270),
]

def raw_log_ratio(z, n):
    """Compute ln(P_dau/P_par) = Σ_i ln|V̂_i^dau/V̂_i^par|."""
    a = z + n
    vp = generator_volumes(z, n)
    vd = generator_volumes(z+1, n-1)
    return sum(math.log(abs(vd[i])) - math.log(abs(vp[i]))
               for i in range(a-1)
               if abs(vp[i]) > 1e-30 and abs(vd[i]) > 1e-30)

# ── Pairing from transfer matrix determinants ────────────────────

def det_T(c, d):
    """det T(c,d) = (c·HA+d)·d - c² = c·HA·d + d² - c²"""
    return c * HA * d + d**2 - c**2

def pairing_energy_from_det(z, n):
    """Estimate pairing energy from transfer matrix determinant ratios.

    For each generator chain, the product of determinants gives the
    total signed area of the chain in phase space. Paired crossings
    (adjacent same-type) have different determinant products than unpaired.

    The pairing energy is related to the determinant ratio of the
    full chain for even-even vs odd-odd configurations.
    """
    a = z + n
    types = ['p']*z + ['n']*n
    types_ee = ['p']*((z+1)//2*2) + ['n']*(a - (z+1)//2*2)  # nearest ee

    det_prod = 1.0
    det_prod_ee = 1.0
    for i in range(a-1):
        for j in range(i+1, a):
            c, d = crossing_coeffs(types[i], types[j])
            det_prod *= det_T(c, d)
            c2, d2 = crossing_coeffs(types_ee[i] if i < len(types_ee) else 'n',
                                      types_ee[j] if j < len(types_ee) else 'n')
            det_prod_ee *= det_T(c2, d2)

    return det_prod, det_prod_ee

# ── What F factor makes each prediction exact? ──────────────────

def reverse_engineer_f(z, n, q_exp):
    """What F factor would make the prediction match experiment?"""
    a = z + n
    vp = generator_volumes(z, n)
    vd = generator_volumes(z+1, n-1)

    # Base formula without F
    types_p = ['p']*z + ['n']*n
    types_d = ['p']*(z+1) + ['n']*(n-1)
    lu, lr, luc = 0.0, 0.0, 0.0
    for i in range(a-1):
        if abs(vp[i]) < 1e-30 or abs(vd[i]) < 1e-30: continue
        lratio = (math.log(abs(vd[i])) - math.log(abs(vp[i]))) / LN_Q
        changed = [j for j in range(i+1, a)
                   if types_p[i]+types_p[j] != types_d[i]+types_d[j]]
        if not changed:
            luc += lratio
        else:
            nu = sum(1 for j in changed if types_p[i]=='n' and types_p[j]=='n')
            nr = sum(1 for j in changed if types_d[i]=='p' and types_d[j]=='p')
            t = nu + nr
            if nr==0: lu += lratio
            elif nu==0: lr += lratio
            else: lu += lratio*nu/t; lr += lratio*nr/t

    q_raw = abs(Q*lu + Q_INV*lr + luc) * KAPPA_Q
    if q_raw < 1e-30: return float('inf')
    return q_exp / q_raw

# ── Parity-dependent F from Hecke eigenvalue ratios ─────────────

def hecke_pairing_ratio():
    """The pairing correction from Hecke algebra eigenvalue structure.

    For paired crossings (even occupancy), σ² = HA·σ + 1 creates both
    eigenvalue channels. The symmetric eigenvalue is q, the antisymmetric
    is -q⁻¹. The pairing energy is the ratio of their contributions
    to the traced volume:

    V̂(paired) / V̂(unpaired) involves the identity term (from σ²=HA·σ+1)
    versus the pure σ term.

    For a single pp crossing: T(1,0), eigenvalues q and -q⁻¹.
    Traced volume = z·(q-q⁻¹) + 1 = z·HA + 1.

    For a paired pp crossing: T(1,0)², eigenvalues q² and q⁻².
    Matrix T² = [[HA²+1, HA], [HA, 1]].
    Traced volume = z·(HA²+1) + HA.

    The ratio V̂(paired)/V̂(unpaired)² measures the pairing gain.
    """
    # T_pp = [[HA, 1], [1, 0]]
    # T_pp² = [[HA²+1, HA], [HA, 1]]
    z = Z_MARKOV
    v_single = z * HA + 1
    v_paired = z * (HA**2 + 1) + HA
    v_sq = v_single**2

    print(f"  V̂(single pp): z·HA + 1 = {v_single:.6f}")
    print(f"  V̂(paired pp): z·(HA²+1) + HA = {v_paired:.6f}")
    print(f"  V̂(single)² = {v_sq:.6f}")
    print(f"  V̂(paired) / V̂(single)² = {v_paired/v_sq:.6f}")
    print(f"  √(V̂(paired)/V̂(single)²) = {math.sqrt(v_paired/v_sq):.6f}")

    # For nn crossing:
    c_nn, d_nn = Q**2, -Q * S_SK
    v_nn = z * (c_nn * HA + d_nn) + c_nn
    # T_nn² = T(c,d) · T(c,d)
    t00 = (c_nn*HA + d_nn)**2 + c_nn**2
    t10 = c_nn*(c_nn*HA + d_nn) + c_nn*d_nn
    v_nn_paired = z * t00 + t10
    v_nn_sq = v_nn**2

    print(f"\n  V̂(single nn): {v_nn:.6f}")
    print(f"  V̂(paired nn): {v_nn_paired:.6f}")
    print(f"  V̂(single nn)² = {v_nn_sq:.6f}")
    print(f"  V̂(paired nn) / V̂(single)² = {v_nn_paired/v_nn_sq:.6f}")

    return v_paired / v_sq, v_nn_paired / v_nn_sq


if __name__ == "__main__":
    print("=" * 90)
    print("PARITY-DEPENDENT Q-VALUE ANALYSIS")
    print("=" * 90)

    # 1. Show what F factor each nucleus needs
    print("\n── Reverse-engineered F factors ──")
    print(f"{'Nuc':>8} {'Trans':>8} {'F_needed':>10} {'F_used':>8} {'Ratio':>8} {'Shell':>6}")
    print("-" * 60)
    for z, n, nuc, q_exp in BENCHMARKS:
        f_needed = reverse_engineer_f(z, n, q_exp)
        deg = shell_degree(n)
        f_used = F_DEG2 if deg >= 2 else 1.0
        if n in MAGIC and deg >= 2: f_used *= F_PAULI
        trans = transition_type(z, n)
        ratio = f_needed / f_used if f_used > 0 else float('inf')
        print(f"{nuc:>8} {trans:>8} {f_needed:>10.4f} {f_used:>8.4f} {ratio:>8.4f} {deg:>6}")

    # 2. Pairing analysis from Hecke eigenvalues
    print("\n── Hecke pairing ratios ──")
    pp_pair, nn_pair = hecke_pairing_ratio()

    # 3. Check if the odd-odd error is consistent across nuclei
    print("\n── Error by parity transition ──")
    by_trans = {}
    for z, n, nuc, q_exp in BENCHMARKS:
        trans = transition_type(z, n)
        raw = raw_log_ratio(z, n)
        q_base = abs(raw) * KAPPA
        deg = shell_degree(n)
        f = F_DEG2 if deg >= 2 else 1.0
        if n in MAGIC and deg >= 2: f *= F_PAULI
        q_pred = q_base * f
        err = (q_pred - q_exp) / q_exp * 100
        if trans not in by_trans:
            by_trans[trans] = []
        by_trans[trans].append((nuc, err, z, n))

    for trans, entries in sorted(by_trans.items()):
        print(f"\n  {trans}:")
        for nuc, err, z, n in entries:
            a = z + n
            print(f"    {nuc:>8} (A={a:>3}): {err:>+6.1f}%")

    # 4. The converting nucleon's local environment
    print("\n── Converting nucleon local analysis ──")
    for z, n, nuc, q_exp in BENCHMARKS:
        a = z + n
        types_p = ['p']*z + ['n']*n
        # Position of converting nucleon
        conv_pos = z  # the first neutron becomes a proton
        # Count how many of each crossing type the converting nucleon has
        n_pp = sum(1 for j in range(a) if j != conv_pos and types_p[j] == 'p')
        n_nn = sum(1 for j in range(a) if j != conv_pos and types_p[j] == 'n')
        n_pp_after = n_pp + 1  # gains one pp crossing (itself)
        n_nn_after = n_nn - 1  # loses one nn crossing
        # Parity of the converting nucleon's crossings
        is_paired_before = (n_nn % 2 == 0)  # even nn crossings = paired
        is_paired_after = (n_pp_after % 2 == 0)  # even pp crossings = paired
        print(f"  {nuc:>8}: conv at {conv_pos}, "
              f"nn_before={n_nn} ({'paired' if is_paired_before else 'UNPAIRED'}), "
              f"pp_after={n_pp_after} ({'paired' if is_paired_after else 'UNPAIRED'})")

    # 5. Try parity-dependent F correction
    print("\n── Test: parity-dependent shell factor ──")
    # For oo→ee: the daughter gains pairing. The F factor should be SMALLER
    # (the Q-value is reduced because the parent is weaker than what the
    # transfer matrix predicts for an "average" nucleus).
    #
    # From the reverse-engineered ratios:
    # oo→ee transitions need F_needed/F_used ≈ 0.93
    # ee→oo transitions need F_needed/F_used ≈ 1.0 (no correction)
    #
    # The pairing correction is: for odd-odd parents, multiply by
    # the ratio of V̂(unpaired)/V̂(paired) ≈ 0.93.

    # Compute the average correction needed for oo→ee
    oo_ratios = []
    for z, n, nuc, q_exp in BENCHMARKS:
        f_needed = reverse_engineer_f(z, n, q_exp)
        deg = shell_degree(n)
        f_used = F_DEG2 if deg >= 2 else 1.0
        if n in MAGIC and deg >= 2: f_used *= F_PAULI
        trans = transition_type(z, n)
        if trans == "oo→ee":
            oo_ratios.append(f_needed / f_used)

    if oo_ratios:
        avg_oo = sum(oo_ratios) / len(oo_ratios)
        print(f"  Average F correction for oo→ee: {avg_oo:.4f}")
        print(f"  (Would need to derive this from q — NOT a fit)")

    # 6. Try the Skein ratio formula with parity correction
    print("\n── Skein ratio + oo correction ──")
    # Test: multiply oo→ee Q-values by 0.93 (to see if pattern holds)
    # THIS IS EXPLORATORY — the actual correction must come from q
    for test_corr in [1.0, 0.95, 0.93, 0.90]:
        errs = []
        for z, n, nuc, q_exp in BENCHMARKS:
            raw = raw_log_ratio(z, n)
            q_base = abs(raw) * KAPPA
            deg = shell_degree(n)
            f = F_DEG2 if deg >= 2 else 1.0
            if n in MAGIC and deg >= 2: f *= F_PAULI
            trans = transition_type(z, n)
            corr = test_corr if trans == "oo→ee" else 1.0
            q_pred = q_base * f * corr
            err = (q_pred - q_exp) / q_exp * 100
            errs.append(abs(err))
        mae = sum(errs) / len(errs)
        print(f"  oo_corr = {test_corr:.2f}: MAE = {mae:.1f}%")
