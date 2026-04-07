"""
I₁₀ pairing correction and spectator overcounting fix.

Two systematic errors in the Q-value formula:

1. PAIRING (I₁₀): odd-odd nuclei have weaker chain anchoring than
   even-even nuclei at the same A, because unpaired crossings lack
   the σ² = HA·σ + 1 identity term. The pairing factor corrects for
   the weight difference between even-even and odd-odd/odd-A configurations.

2. SPECTATOR OVERCOUNTING: for heavy nuclei (A > 28), most generators
   don't change crossing type in β⁻ decay. Their log_q ratios add
   noise. Instead of dropping them entirely (which underestimates),
   we weight each generator by the fraction of its crossings that change.

Both corrections are derived from q alone — no fitting.
"""

import math
import sys
sys.path.insert(0, '.')
from q_parameter import Q, Q_INV, Q_ERR, HA, LN_Q, HBAR_Q
from experimental_constants import M_E_MEV

KAPPA_Q = LN_Q * M_E_MEV / 3.0
Z_MARKOV = 1.0 / (math.sqrt(Q) + 1.0/math.sqrt(Q))
S_SKEIN = math.sqrt(Q) - 1.0/math.sqrt(Q)

F_DEG2 = 0.5904
F_PAULI = 0.6382

MAGIC = [2, 8, 20, 28, 50, 82, 126]

def shell_degree(n):
    for i, m in enumerate(MAGIC):
        if n <= m:
            return 2 if i + 1 >= 5 else 1
    return 2

def crossing_coeffs(ti, tj):
    pair = ti + tj
    if pair == 'pp': return (1.0, 0.0)
    elif pair == 'nn': return (1.0, -HA)
    else: return (1.0, -HA / 2.0)

def generator_volumes(z, n):
    a = z + n
    types = ['p'] * z + ['n'] * n
    vols = []
    for i in range(a - 1):
        m = [[1.0, 0.0], [0.0, 1.0]]
        for j in range(i + 1, a):
            c, d = crossing_coeffs(types[i], types[j])
            t = [[c * HA + d, c], [c, d]]
            m = [[m[0][0]*t[0][0]+m[0][1]*t[1][0], m[0][0]*t[0][1]+m[0][1]*t[1][1]],
                 [m[1][0]*t[0][0]+m[1][1]*t[1][0], m[1][0]*t[0][1]+m[1][1]*t[1][1]]]
        vols.append(Z_MARKOV * m[0][0] + m[1][0])
    return vols

def skein_polynomial(z, n):
    """Product of traced volumes = Skein polynomial P(q)."""
    vols = generator_volumes(z, n)
    p = 1.0
    for v in vols:
        p *= v
    return p

# ══════════════════════════════════════════════════════════════════
# I₁₀: PAIRING CORRECTION
# ══════════════════════════════════════════════════════════════════

def parity(z, n):
    """Nuclear parity classification."""
    if z % 2 == 0 and n % 2 == 0: return "even-even"
    elif z % 2 == 1 and n % 2 == 1: return "odd-odd"
    else: return "odd-A"

def pairing_factor(z, n):
    """Compute the pairing correction factor from the Skein polynomial.

    For even-even: no correction (reference)
    For odd-odd: P(even-even at same A) / P(odd-odd) captures the
                 weight enhancement from paired σ² reductions.
    For odd-A: intermediate — one unpaired nucleon type.

    The ratio |P_ee/P_oo| at the same A gives the relative binding
    strength from pairing. In the Q-value, this enters as a multiplicative
    correction because the decay changes the pairing structure.
    """
    a = z + n
    par = parity(z, n)

    if par == "even-even":
        return 1.0, "ee→ee or ee ref"

    # Find the nearest even-even isobar at the same A
    z_ee = (a // 2)  # round to nearest even Z
    if z_ee % 2 == 1:
        z_ee += 1
    n_ee = a - z_ee
    if n_ee < 0 or z_ee > a:
        return 1.0, "no ee isobar"

    p_actual = abs(skein_polynomial(z, n))
    p_ee = abs(skein_polynomial(z_ee, n_ee))

    if p_actual < 1e-30:
        return 1.0, "zero polynomial"

    ratio = p_ee / p_actual
    return ratio, f"P({z_ee},{n_ee})/P({z},{n})"


# ══════════════════════════════════════════════════════════════════
# SPECTATOR WEIGHTING
# ══════════════════════════════════════════════════════════════════

def changed_fraction(i, a, types_p, types_d):
    """Fraction of crossings at generator i that change type in β⁻ decay.

    Generator σ_i connects nucleon i to nucleons j > i.
    For each j, the crossing type may or may not change.
    Returns (n_changed, n_total, fraction).
    """
    n_changed = 0
    n_total = 0
    for j in range(i + 1, a):
        pair_p = types_p[i] + types_p[j]
        pair_d = types_d[i] + types_d[j]
        n_total += 1
        if pair_p != pair_d:
            n_changed += 1
    frac = n_changed / n_total if n_total > 0 else 0.0
    return n_changed, n_total, frac


def predict_q_value_corrected(z_par, n_par):
    """Q-value prediction with I₁₀ pairing + spectator weighting.

    Three improvements over the base formula:
    1. Each generator's contribution is weighted by its changed fraction
    2. Pairing correction for odd-odd → even-even transitions
    3. Shell degree factor (unchanged)
    """
    a = z_par + n_par
    z_dau, n_dau = z_par + 1, n_par - 1

    types_p = ['p'] * z_par + ['n'] * n_par
    types_d = ['p'] * z_dau + ['n'] * n_dau

    vp = generator_volumes(z_par, n_par)
    vd = generator_volumes(z_dau, n_dau)

    # Base formula (unchanged generators get full weight)
    lu_base, lr_base, luc_base = 0.0, 0.0, 0.0
    # Spectator-weighted formula
    lu_wt, lr_wt, luc_wt = 0.0, 0.0, 0.0

    for i in range(a - 1):
        if abs(vp[i]) < 1e-30 or abs(vd[i]) < 1e-30:
            continue

        lratio = (math.log(abs(vd[i])) - math.log(abs(vp[i]))) / LN_Q
        n_ch, n_tot, frac = changed_fraction(i, a, types_p, types_d)

        # Weight by changed fraction (spectator fix)
        w = max(frac, 0.0)

        changed = []
        for j in range(i + 1, a):
            pair_p = types_p[i] + types_p[j]
            pair_d = types_d[i] + types_d[j]
            if pair_p != pair_d:
                changed.append(j)

        if not changed:
            luc_base += lratio
            # Spectator: unchanged generators get zero weight
            # (their volume changes are purely from index relabeling)
        else:
            nu = sum(1 for j in changed if types_p[i] == 'n' and types_p[j] == 'n')
            nr = sum(1 for j in changed if types_d[i] == 'p' and types_d[j] == 'p')
            t = nu + nr
            if nr == 0:
                lu_base += lratio
                lu_wt += lratio * w
            elif nu == 0:
                lr_base += lratio
                lr_wt += lratio * w
            else:
                lu_base += lratio * nu / t
                lr_base += lratio * nr / t
                lu_wt += lratio * nu / t * w
                lr_wt += lratio * nr / t * w

    # Base Q (current formula)
    q_base = abs(Q * lu_base + Q_INV * lr_base + luc_base) * KAPPA_Q

    # Spectator-weighted Q
    q_weighted = abs(Q * lu_wt + Q_INV * lr_wt) * KAPPA_Q

    # Shell factor
    deg = shell_degree(n_par)
    f = F_DEG2 if deg >= 2 else 1.0
    if n_par in MAGIC and deg >= 2:
        f *= F_PAULI

    # Pairing correction
    par_par = parity(z_par, n_par)
    par_dau = parity(z_dau, n_dau)

    # The pairing correction applies when the decay changes parity class
    # β⁻: (Z,N) → (Z+1,N-1)
    # odd-odd → even-even: daughter is more tightly bound (pairing gain)
    # even-even → odd-odd: daughter loses pairing (not physical for β⁻)
    p_corr = 1.0
    p_desc = ""
    if par_par == "odd-odd" and par_dau == "even-even":
        # Parent is weaker (odd-odd), daughter stronger (even-even)
        # The Q-value should be REDUCED because the base formula
        # doesn't account for the parent's weaker binding
        p_factor_par, _ = pairing_factor(z_par, n_par)
        p_factor_dau, _ = pairing_factor(z_dau, n_dau)
        # The correction: the base volumes already capture the difference,
        # but the *shell factor* needs adjustment for odd-odd parents
        p_corr = 1.0 / p_factor_par  # reduce prediction for odd-odd parent
        p_desc = f"1/{p_factor_par:.4f}"
    elif par_par == "odd-A":
        # One unpaired: intermediate correction
        p_factor, _ = pairing_factor(z_par, n_par)
        p_corr = 1.0 / math.sqrt(p_factor)
        p_desc = f"1/√{p_factor:.4f}"

    q_base_corr = q_base * f
    q_wt_corr = q_weighted * f
    q_paired = q_base * f * p_corr
    q_combined = q_weighted * f * p_corr

    return {
        'q_base': q_base_corr,
        'q_weighted': q_wt_corr,
        'q_paired': q_paired,
        'q_combined': q_combined,
        'f': f,
        'p_corr': p_corr,
        'p_desc': p_desc,
        'par_par': par_par,
        'par_dau': par_dau,
        'log_q_total': lu_base + lr_base + luc_base,
        'lu': lu_base, 'lr': lr_base, 'luc': luc_base,
        'lu_wt': lu_wt, 'lr_wt': lr_wt,
    }


# ══════════════════════════════════════════════════════════════════
# BENCHMARKS
# ══════════════════════════════════════════════════════════════════

BENCHMARKS = [
    (1,  2,  "³H→³He",       0.01861, 0.00001),
    (6,  8,  "¹⁴C→¹⁴N",      0.15648, 0.00004),
    (27, 33, "⁶⁰Co→⁶⁰Ni",    0.31817, 0.00013),
    (38, 52, "⁹⁰Sr→⁹⁰Y",     0.54590, 0.00007),
    (55, 82, "¹³⁷Cs→¹³⁷Ba",   0.51400, 0.00021),
    (83, 127,"²¹⁰Bi→²¹⁰Po",   1.16270, 0.00006),
]

if __name__ == "__main__":
    print("=" * 100)
    print("I₁₀ PAIRING CORRECTION + SPECTATOR WEIGHTING")
    print("=" * 100)

    # First: show pairing factors for each benchmark
    print("\n── Pairing analysis ──")
    print(f"{'Nucleus':>10} {'Parity':>10} {'P(Z,N)':>12} {'P(ee)':>12} {'Ratio':>8} {'Daughter':>10}")
    print("-" * 70)
    for z, n, name, _, _ in BENCHMARKS:
        par = parity(z, n)
        p = abs(skein_polynomial(z, n))
        p_f, desc = pairing_factor(z, n)
        par_d = parity(z+1, n-1)
        print(f"{name:>10} {par:>10} {p:>12.4e} {p*p_f:>12.4e} {p_f:>8.4f} {par_d:>10}")

    # Second: show changed fractions for a heavy nucleus
    print(f"\n── Spectator analysis for ⁶⁰Co (Z=27, N=33, A=60) ──")
    z, n = 27, 33
    a = z + n
    types_p = ['p'] * z + ['n'] * n
    types_d = ['p'] * (z+1) + ['n'] * (n-1)
    n_fully_changed = 0
    n_partial = 0
    n_unchanged = 0
    for i in range(a - 1):
        nc, nt, frac = changed_fraction(i, a, types_p, types_d)
        if frac == 0.0:
            n_unchanged += 1
        elif frac == 1.0:
            n_fully_changed += 1
        else:
            n_partial += 1
    print(f"  Generators: {a-1} total")
    print(f"  Fully changed:  {n_fully_changed}")
    print(f"  Partially changed: {n_partial}")
    print(f"  Unchanged: {n_unchanged}")
    print(f"  → {n_unchanged} spectator generators contribute noise")

    # Third: compare all approaches
    print(f"\n── Q-value comparison (4 approaches) ──")
    header = f"{'Decay':>14} {'Base':>8} {'Spec.wt':>8} {'Pair':>8} {'Both':>8} {'Q_exp':>8} {'err_b':>7} {'err_s':>7} {'err_p':>7} {'err_c':>7}"
    print(header)
    print("-" * len(header))

    errs = {'base': [], 'wt': [], 'pair': [], 'comb': []}
    for z, n, name, q_exp, q_err in BENCHMARKS:
        r = predict_q_value_corrected(z, n)
        e_b = (r['q_base'] - q_exp) / q_exp * 100
        e_w = (r['q_weighted'] - q_exp) / q_exp * 100
        e_p = (r['q_paired'] - q_exp) / q_exp * 100
        e_c = (r['q_combined'] - q_exp) / q_exp * 100
        errs['base'].append(abs(e_b))
        errs['wt'].append(abs(e_w))
        errs['pair'].append(abs(e_p))
        errs['comb'].append(abs(e_c))

        mark_b = "◀" if abs(e_b) < 5 else " "
        mark_w = "◀" if abs(e_w) < 5 else " "
        mark_p = "◀" if abs(e_p) < 5 else " "
        mark_c = "◀" if abs(e_c) < 5 else " "

        print(f"{name:>14} {r['q_base']:>8.5f} {r['q_weighted']:>8.5f} {r['q_paired']:>8.5f} {r['q_combined']:>8.5f} {q_exp:>8.5f} {e_b:>+6.1f}%{mark_b}{e_w:>+6.1f}%{mark_w}{e_p:>+6.1f}%{mark_p}{e_c:>+6.1f}%{mark_c}")

    print()
    for key, label in [('base', 'Base'), ('wt', 'Spectator-weighted'),
                       ('pair', 'Pairing only'), ('comb', 'Pairing + spectator')]:
        mae = sum(errs[key]) / len(errs[key])
        rms = math.sqrt(sum(e**2 for e in errs[key]) / len(errs[key]))
        print(f"  {label:>25}: MAE = {mae:.1f}%, RMS = {rms:.1f}%")

    # Detail on pairing corrections applied
    print(f"\n── Pairing corrections applied ──")
    for z, n, name, _, _ in BENCHMARKS:
        r = predict_q_value_corrected(z, n)
        if r['p_corr'] != 1.0:
            print(f"  {name}: {r['par_par']}→{r['par_dau']}, p_corr = {r['p_desc']} = {r['p_corr']:.4f}")
        else:
            print(f"  {name}: {r['par_par']}→{r['par_dau']}, no correction needed")
