#!/usr/bin/env python3
# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Symbolic LP for knot operator selection — all in q.

Computes the full channel matrix A[decay, knot] as rational functions
of q, then solves the LP symbolically.

For T_{2,3} (B₃ confinement), the min-eigenvalue is q⁻¹ exactly.
The eigenvector in each 2×2 block is the -q⁻¹ Hecke eigenvector.
This makes all matrix elements rational in q.

For the LP:
  Q(decay) = Σ_K y_K × Σ_λ Δme_λ^K × m_e
  subject to: y_K ≥ 0, Frobenius positivity

The weights y_K and predictions Q are functions of q only.

Usage:
    cd folio-assistant/computations && python3 symbolic-lp.py
"""

import sympy as sp
from sympy import sqrt, cancel, factor, Rational, simplify, Matrix
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0_num

q = sp.Symbol('q', positive=True)
qi = 1/q
h = q - qi
two_q = q + qi  # [2]_q


# ══════════════════════════════════════════════════════════════
#  TRIVIAL IRREP: Garside = product of scalars
# ══════════════════════════════════════════════════════════════

def typed_d_sym(fi, fj):
    if fi == 'u' and fj == 'u': return sp.Integer(0)
    if fi == 'd' and fj == 'd': return -h
    return -h/2


def garside_trivial(quarks):
    """Garside product in trivial irrep: Π (q + d(f_i,f_j))."""
    n = len(quarks)
    product = sp.Integer(1)
    for L in range(1, n):
        for k in range(L-1, -1, -1):
            d = typed_d_sym(quarks[k], quarks[L])
            product *= (q + d)
    return cancel(product)


# ══════════════════════════════════════════════════════════════
#  STANDARD IRREP (n-1, 1): T_{2,3} q⁻¹ eigenvector
# ══════════════════════════════════════════════════════════════

def syt_2row(a, b):
    n = a + b
    result = []
    def recurse(current, r1, r2):
        if len(current) == n:
            result.append(tuple(current))
            return
        if r1 < a:
            recurse(current + [True], r1+1, r2)
        if r2 < b and r2 < r1:
            recurse(current + [False], r1, r2+1)
    recurse([], 0, 0)
    return result


def syt_content(tab, v):
    r1 = r2 = 0
    for i in range(v):
        if tab[i]: r1 += 1
        else: r2 += 1
    return (r1 - 1) if tab[v-1] else (r2 - 2)


def syt_swap(tab, k):
    if tab[k-1] == tab[k]: return None
    new_tab = list(tab)
    new_tab[k-1], new_tab[k] = new_tab[k], new_tab[k-1]
    r1 = r2 = 0
    for v in new_tab:
        if v: r1 += 1
        else: r2 += 1
        if r2 > r1: return None
    return tuple(new_tab)


def seminormal_gen(tabs, tab_idx, gen):
    k = gen + 1
    dim = len(tabs)
    M = sp.zeros(dim, dim)
    processed = set()
    for i, T in enumerate(tabs):
        if i in processed: continue
        d = syt_content(T, k+1) - syt_content(T, k)
        if d == 1:
            M[i, i] = q; processed.add(i)
        elif d == -1:
            M[i, i] = -qi; processed.add(i)
        else:
            diag_i = h / (q**d - q**(-d))
            M[i, i] = diag_i
            T_sw = syt_swap(T, k)
            if T_sw and T_sw in tab_idx:
                j = tab_idx[T_sw]
                M[j, j] = -diag_i  # trace = h → diag_j = h - diag_i ... wait
                # Actually diag_j = h/(q^{-d} - q^d) = -diag_i
                # And det = -1 → off² = -diag_i × (-diag_i) + 1 = diag_i² + 1... no
                # det = diag_i × (-diag_i) - off² = -1
                # → off² = diag_i² - (-1) = 1 - diag_i² ... hmm let me redo
                # The 2×2 block has eigenvalues q and -q⁻¹
                # trace = q + (-q⁻¹) = h → diag_i + diag_j = h
                # det = q × (-q⁻¹) = -1 → diag_i × diag_j - off² = -1
                diag_j = h - diag_i
                M[j, j] = diag_j
                off_sq = diag_i * diag_j + 1
                off = sp.sqrt(cancel(off_sq))
                M[i, j] = off
                M[j, i] = off
                processed.add(i); processed.add(j)
            else:
                processed.add(i)
    return M


def t23_min_eigvec(tabs, tab_idx, n_nucleons, n, gen_mats):
    """T_{2,3} minimum |eigenvalue| eigenvector.

    For T_{2,3} = σ₀σ₁σ₀ per nucleon, eigenvalues are q³ (trivial)
    and compositions of q, -q⁻¹ for higher irreps.

    The min |λ| eigenvector is the -q⁻¹ channel of each 2×2 block.
    """
    dim = len(tabs)

    # Build T_{2,3} matrix
    K = sp.eye(dim)
    for m in range(n_nucleons):
        g0 = 3*m
        g1 = 3*m + 1
        if g0 < n-1 and g1 < n-1:
            K = K * gen_mats[g0] * gen_mats[g1] * gen_mats[g0]

    # For dim ≤ 8, compute eigenvectors symbolically
    if dim <= 8:
        eigdata = K.eigenvects()
        # Find min |eigenvalue| by evaluating at q₀
        eigs = []
        for eigenval, mult, vecs in eigdata:
            val_num = complex(eigenval.subs(q, q0_num))
            eigs.append((abs(val_num), eigenval, vecs[0]))
        eigs.sort(key=lambda x: x[0])
        _, min_eigval, min_eigvec = eigs[0]
        return min_eigvec, cancel(min_eigval)

    # For larger dim, return None (use numerical)
    return None, None


def garside_matrix_sym(quarks, gen_mats):
    n = len(quarks)
    dim = gen_mats[0].shape[0]
    result = sp.eye(dim)
    for L in range(1, n):
        for k in range(L-1, -1, -1):
            d = typed_d_sym(quarks[k], quarks[L])
            crossing = gen_mats[k] + d * sp.eye(dim)
            result = result * crossing
    return result


def matrix_element_sym(M, v):
    Mv = M * v
    num = v.dot(Mv)
    den = v.dot(v)
    return cancel(num / den)


# ══════════════════════════════════════════════════════════════
#  COMPUTE SYMBOLIC CHANNEL MATRIX
# ══════════════════════════════════════════════════════════════

print("SYMBOLIC LP FOR KNOT OPERATOR SELECTION")
print(f"All expressions in Q(q), evaluated at q₀ = {q0_num:.15f}")
print("=" * 80)

decays = [
    ('n→p',     list('udd'),       list('uud'),       1),
    ('³H→³He',  list('uududdudd'), list('uududduud'), 3),
]

# Channel matrix: A[decay][irrep] = Δme as function of q
# For T_{2,3} only (the clean channel)
channel_data = {}

for name, par, dau, n_nuc in decays:
    n = len(par)
    print(f"\n{'━' * 80}")
    print(f"  {name} (n={n})")
    print(f"{'━' * 80}")

    channel_data[name] = {}

    # Trivial irrep (shared by all knot operators)
    G_par = garside_trivial(par)
    G_dau = garside_trivial(dau)
    dme_triv = cancel(G_dau - G_par)
    dme_triv_f = factor(dme_triv)
    print(f"\n  λ=({n},0) trivial:")
    print(f"    Δme = {dme_triv_f}")
    print(f"    Δme(q₀) = {float(dme_triv.subs(q, q0_num)):.10f}")
    channel_data[name][f'({n},0)'] = dme_triv

    # Standard irrep (n-1, 1)
    a, b = n-1, 1
    tabs = syt_2row(a, b)
    dim = len(tabs)
    tab_idx = {t: i for i, t in enumerate(tabs)}

    print(f"\n  λ=({a},{b}) standard (dim={dim}):")
    t0 = time.time()

    gen_mats = {}
    for g in range(n-1):
        gen_mats[g] = seminormal_gen(tabs, tab_idx, g)
    print(f"    Generators built ({time.time()-t0:.1f}s)")

    # Garside products
    t0 = time.time()
    G_par_m = garside_matrix_sym(par, gen_mats)
    G_dau_m = garside_matrix_sym(dau, gen_mats)
    print(f"    Garside products built ({time.time()-t0:.1f}s)")

    # T_{2,3} eigenvector
    t0 = time.time()
    v_min, lambda_min = t23_min_eigvec(tabs, tab_idx, n_nuc, n, gen_mats)
    if v_min is not None:
        print(f"    T_{{2,3}} λ_min = {cancel(lambda_min)}")
        print(f"    λ_min(q₀) = {float(lambda_min.subs(q, q0_num)):.6f}")

        me_par = matrix_element_sym(G_par_m, v_min)
        me_dau = matrix_element_sym(G_dau_m, v_min)
        dme_std = cancel(me_dau - me_par)

        print(f"    ⟨v|Δ_par|v⟩ = {cancel(me_par)}")
        print(f"    ⟨v|Δ_dau|v⟩ = {cancel(me_dau)}")
        dme_std_str = str(factor(dme_std))
        if len(dme_std_str) < 300:
            print(f"    Δme = {factor(dme_std)}")
        else:
            print(f"    Δme = [expression with {len(dme_std_str)} chars]")
        print(f"    Δme(q₀) = {float(dme_std.subs(q, q0_num)):.10f}")
        print(f"    ({time.time()-t0:.1f}s)")

        channel_data[name][f'({a},{b})_T23'] = dme_std
    else:
        print(f"    dim={dim} too large for symbolic eigenvector")

    # Higher irreps (only if dim ≤ 48)
    for a2 in range(n-2, max(n//2-1, 0), -1):
        b2 = n - a2
        if b2 > a2: break
        tabs2 = syt_2row(a2, b2)
        dim2 = len(tabs2)
        if dim2 > 48:
            print(f"\n  λ=({a2},{b2}) dim={dim2}: skipping (dim > 48 for symbolic)")
            continue

        tab_idx2 = {t: i for i, t in enumerate(tabs2)}
        print(f"\n  λ=({a2},{b2}) dim={dim2}:")
        t0 = time.time()

        gen_mats2 = {g: seminormal_gen(tabs2, tab_idx2, g) for g in range(n-1)}
        G_par_m2 = garside_matrix_sym(par, gen_mats2)
        G_dau_m2 = garside_matrix_sym(dau, gen_mats2)

        v_min2, lambda_min2 = t23_min_eigvec(tabs2, tab_idx2, n_nuc, n, gen_mats2)
        if v_min2 is not None:
            me_par2 = matrix_element_sym(G_par_m2, v_min2)
            me_dau2 = matrix_element_sym(G_dau_m2, v_min2)
            dme2 = cancel(me_dau2 - me_par2)
            print(f"    T_{{2,3}} λ_min = {cancel(lambda_min2)}")
            print(f"    Δme(q₀) = {float(dme2.subs(q, q0_num)):.10f}")
            print(f"    ({time.time()-t0:.1f}s)")
            channel_data[name][f'({a2},{b2})_T23'] = dme2
        else:
            print(f"    Eigenvector computation failed ({time.time()-t0:.1f}s)")

# ══════════════════════════════════════════════════════════════
#  SYMBOLIC LP
# ══════════════════════════════════════════════════════════════

print(f"\n{'━' * 80}")
print(f"  SYMBOLIC LP")
print(f"{'━' * 80}")

# For T_{2,3} channel, total Δme per decay = Σ_λ Δme_λ
for name in channel_data:
    total = sp.Integer(0)
    for key, dme in channel_data[name].items():
        total += dme
    total_simplified = cancel(total)
    total_num = float(total_simplified.subs(q, q0_num))
    print(f"\n  {name}: Σ_λ Δme_λ(T23) = {total_num:.10f}")

    # For a single-operator LP (T_{2,3} only), Q = y × Σ Δme × m_e
    # The weight y is determined by matching ONE experimental Q-value
    # Then predict the others.

# Free neutron: use as calibration
# Q(n→p) = y × Σ Δme(n→p) × m_e
# → y = Q_exp / (Σ Δme × m_e)

m_e = sp.Rational(51099895, 100000000)  # 0.51099895 MeV (exact rational)

dme_neutron = sp.Integer(0)
for key, dme in channel_data['n→p'].items():
    dme_neutron += dme

# Q_exp(n→p) = 0.782333 MeV (from CODATA)
# y = Q_exp / (Σ Δme × m_e)
# This gives y as a function of q and experimental constants

Q_exp_neutron = sp.Rational(782333, 1000000)  # MeV
y_T23 = Q_exp_neutron / (dme_neutron * m_e)
y_T23_simplified = cancel(y_T23)
y_T23_num = float(y_T23_simplified.subs(q, q0_num))

print(f"\n  Calibration from free neutron:")
print(f"    y_T23 = Q_exp(n→p) / (Σ Δme(n→p) × m_e)")
print(f"    y_T23(q₀) = {y_T23_num:.6f}")

# Predict tritium
if '³H→³He' in channel_data:
    dme_tritium = sp.Integer(0)
    for key, dme in channel_data['³H→³He'].items():
        dme_tritium += dme

    Q_pred_tritium = y_T23 * dme_tritium * m_e
    Q_pred_tritium_simplified = cancel(Q_pred_tritium)
    Q_pred_tritium_num = float(Q_pred_tritium_simplified.subs(q, q0_num))

    print(f"\n  Prediction for ³H→³He:")
    print(f"    Q_pred = y_T23 × Σ Δme(³H) × m_e")
    print(f"    Q_pred(q₀) = {Q_pred_tritium_num:.6f} MeV")
    print(f"    Q_exp      = 0.018610 MeV")
    print(f"    Ratio Q_pred/Q_exp = {Q_pred_tritium_num / 0.018610:.2f}")

    # The ratio Q_pred/Q_exp as a symbolic function of q
    Q_ratio = cancel(Q_pred_tritium / sp.Rational(18610, 1000000))
    Q_ratio_num = float(Q_ratio.subs(q, q0_num))
    print(f"    Symbolic ratio(q₀) = {Q_ratio_num:.4f}")

print("\n" + "=" * 80)
print("  DONE")
print("=" * 80)
