#!/usr/bin/env python3
"""
Q-value with Borromean ring unbind-intertwine-rebind.

The full beta decay transition at each affected crossing:

  1. UNDO Borromean ring on parent shell (h⁻¹ dressing)
  2. INTERTWINE — apply the knot crossing change (nn→pn or pn→pp)
  3. REDO Borromean ring on daughter shell (h dressing)

The 3 color tubes of the exceptional divisor on Σ₄ give 3
half-Borromean operators h₀₁, h₁₂, h₀₂ in H₃(q). Each tube
sees different fiber anisotropy. Average over all 3 BEFORE
computing the Q-value.

Degree matters: un-ringing uses the PARENT shell's knot degree,
re-ringing uses the DAUGHTER shell's knot degree.

Usage:
    python3 borromean-qvalue.py
"""

import math
from q_parameter import Q as q, Q_INV as qi, E_CROSS
from experimental_constants import *

HA = q - qi
S = q**0.5 - qi**0.5
Z_m = 1.0 / (q**0.5 + qi**0.5)
mu_0 = M_E_MEV / (3 * E_CROSS)
kappa = E_CROSS * mu_0  # = m_e/3

# ══════════════════════════════════════════════════════════════
# §1  H₃(q) REPRESENTATIONS
# ══════════════════════════════════════════════════════════════

def sigma_std(i):
    """σ_i in standard (2,1) rep of H₃(q)."""
    if i == 0: return [[q, 0.0], [1.0, -qi]]
    else:      return [[-qi, HA], [0.0, q]]

def sigma_inv_std(i):
    s = sigma_std(i)
    return [[s[0][0] - HA, s[0][1]], [s[1][0], s[1][1] - HA]]

def mm(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def tr(A): return A[0][0] + A[1][1]
def eye(): return [[1.0, 0.0], [0.0, 1.0]]

def eval_word(word):
    M = eye()
    for g, s in word:
        M = mm(M, sigma_std(g) if s > 0 else sigma_inv_std(g))
    return M

def eval_triv(word):
    r = 1.0
    for _, s in word:
        r *= q if s > 0 else qi
    return r

# ══════════════════════════════════════════════════════════════
# §2  BORROMEAN HALF-OPERATORS AND THEIR INVERSES
# ══════════════════════════════════════════════════════════════

# 3 half-Borromean operators (color tubes of exceptional divisor)
H_OPS = {
    'h01': [(0,-1),(1,1),(0,1),(1,-1)],    # σ₀⁻¹σ₁σ₀σ₁⁻¹
    'h12': [(1,-1),(0,1),(1,1),(0,-1)],    # σ₁⁻¹σ₀σ₁σ₀⁻¹
    'h02': [(0,-1),(1,-1),(0,1),(1,1)],    # σ₀⁻¹σ₁⁻¹σ₀σ₁ (conjugated)
}

# Inverses: reverse word, flip signs
H_INV = {k: [(g, -s) for g, s in reversed(v)] for k, v in H_OPS.items()}

# ══════════════════════════════════════════════════════════════
# §3  SHELL STRUCTURE AND KNOT DEGREES
# ══════════════════════════════════════════════════════════════

MAGIC = [2, 8, 20, 28, 50, 82, 126]
NEXT_SHELL_SIZE = 58  # 184 - 126, predicted next magic number gap
SHELL_KNOTS = {
    1: ('T23', 2, 3, 1),   # (name, r, s, degree)
    2: ('T25', 2, 5, 1),
    3: ('T27', 2, 7, 1),
    4: ('T35', 3, 5, 1),
    5: ('T29', 2, 9, 2),
    6: ('T34', 3, 4, 2),
    7: ('T29', 2, 9, 2),   # degree tower continuation
}

def neutron_shell(N):
    """Returns (shell_num, occupancy, shell_size, is_magic)."""
    prev = 0
    for i, m in enumerate(MAGIC):
        if N <= m:
            return i + 1, N - prev, m - prev, (N == m)
        prev = m
    return len(MAGIC) + 1, N - MAGIC[-1], NEXT_SHELL_SIZE, False

def proton_shell(Z):
    """Same shell structure for protons."""
    return neutron_shell(Z)

def shell_degree(shell_num):
    return SHELL_KNOTS.get(shell_num, ('T29', 2, 9, 2))[3]


# ══════════════════════════════════════════════════════════════
# §4  THE TRANSITION: UNDO-INTERTWINE-REDO
# ══════════════════════════════════════════════════════════════

def borromean_transition_trace(crossing_change, parent_deg, daughter_deg):
    """Compute the 3-color-averaged standard rep trace for a single
    crossing change, with Borromean un-ring and re-ring.

    crossing_change: the explicit bare Hecke word for the crossing change,
      evaluated exactly as passed by the caller, e.g. [(1, 1)] for σ₁.
      Any scalar prefactor or linear-combination interpretation must be
      applied by the caller before or after this trace computation.

    parent_deg: degree of the parent shell (1 or 2)
    daughter_deg: degree of the daughter shell (1 or 2)

    The full dressed operator for color tube k:
      h_k⁻¹(parent_deg) · crossing_change · h_k(daughter_deg)

    For degree 1: use h_k directly
    For degree 2: use h_k² (compose twice — degree-2 binding)

    Returns the 3-tube averaged standard rep trace.
    """
    traces = []
    for name in ['h01', 'h12', 'h02']:
        h = H_OPS[name]
        h_inv = H_INV[name]

        # Build the un-ring operator (parent shell degree)
        # Degree 1: h⁻¹ once
        # Degree 2: h⁻¹ composed twice (h⁻² = (h⁻¹)²)
        undo = h_inv * parent_deg

        # Build the re-ring operator (daughter shell degree)
        redo = h * daughter_deg

        # Full dressed transition: undo · change · redo
        full_word = undo + crossing_change + redo
        M = eval_word(full_word)
        traces.append(tr(M))

    return sum(traces) / 3


# ══════════════════════════════════════════════════════════════
# §5  TRANSFER MATRIX WITH BORROMEAN DRESSING
# ══════════════════════════════════════════════════════════════

def crossing_coeffs(ti, tj):
    """Crossing coefficients (c, d) for T(c,d) = c·σ + d·𝟙.

    From the Hecke inverse relation σ⁻¹ = σ − (q − q⁻¹):
      pp → σ:          c = 1,   d = 0
      nn → σ⁻¹:        c = 1,   d = −HA
      pn → ½(σ+σ⁻¹): c = 1,   d = −HA/2
    """
    if ti == 'p' and tj == 'p': return 1.0, 0.0
    elif ti == 'n' and tj == 'n': return 1.0, -HA
    else: return 1.0, -HA / 2.0

def T_mat(c, d):
    return [[c * HA + d, c], [c, d]]

def mat_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def compute_gen_vol(types, i):
    A = len(types)
    M = [[1, 0], [0, 1]]
    for j in range(i + 1, A):
        c, d = crossing_coeffs(types[i], types[j])
        M = mat_mul(M, T_mat(c, d))
    return Z_m * M[0][0] + M[1][0]


def Q_borromean(Z, N):
    """Full Q-value with Borromean un-ring / re-ring.

    For each generator:
    1. Classify crossings as unbind (nn→pn) or rebind (pn→pp)
    2. For unbind: undo parent Borromean, apply change, redo daughter Borromean
    3. For rebind: undo parent Borromean, apply change, redo daughter Borromean
    4. Weight unbind by q, rebind by q⁻¹ (Gröbner--Shirshov direction)
    5. Apply shell knot correction for degree-2 shells
    """
    par_types = ['p'] * Z + ['n'] * N
    dau_types = ['p'] * (Z + 1) + ['n'] * (N - 1)
    A = Z + N

    # Shell info
    par_n_sh, _, _, _ = neutron_shell(N)
    dau_n_sh, _, _, _ = neutron_shell(N - 1)
    par_p_sh, _, _, _ = proton_shell(Z)
    dau_p_sh, _, _, _ = proton_shell(Z + 1)

    par_n_deg = shell_degree(par_n_sh)
    dau_n_deg = shell_degree(dau_n_sh)
    par_p_deg = shell_degree(par_p_sh)
    dau_p_deg = shell_degree(dau_p_sh)

    # The nn→pn transition: neutron UNBINDS from neutron shell
    #   Parent shell: neutron shell (degree par_n_deg)
    #   Daughter: the remaining neutrons stay in same shell
    unbind_parent_deg = par_n_deg
    unbind_daughter_deg = dau_n_deg  # neutron shell after losing one

    # The pn→pp transition: proton REBINDS into proton shell
    #   Parent shell: proton was in proton shell (degree par_p_deg)
    #   Daughter: proton shell gains one
    rebind_parent_deg = par_p_deg
    rebind_daughter_deg = dau_p_deg

    # Compute the Borromean correction factors
    # The crossing change operator (nn→pn or pn→pp) is ½HA at gen 1
    # In H₃(q), use gen 1 for the crossing change
    change_word = [(1, 1)]  # σ₁ represents the crossing change direction

    # Unbind: undo parent neutron Borromean, change, redo daughter neutron Borromean
    F_unbind_borr = borromean_transition_trace(
        change_word, unbind_parent_deg, unbind_daughter_deg)
    # Bare (undressed) trace for normalization
    F_bare = tr(eval_word(change_word))
    R_unbind = F_unbind_borr / F_bare if abs(F_bare) > 1e-10 else 1.0

    # Rebind: undo parent proton Borromean, change, redo daughter proton Borromean
    F_rebind_borr = borromean_transition_trace(
        change_word, rebind_parent_deg, rebind_daughter_deg)
    R_rebind = F_rebind_borr / F_bare if abs(F_bare) > 1e-10 else 1.0

    # Decompose Q into unbind/rebind
    ln_unbind = 0.0
    ln_rebind = 0.0
    ln_unchanged = 0.0

    for i in range(A - 1):
        Vp = compute_gen_vol(par_types, i)
        Vd = compute_gen_vol(dau_types, i)
        if abs(Vp) < 1e-30 or abs(Vd) < 1e-30:
            continue
        lr = math.log(abs(Vd)) - math.log(abs(Vp))

        changed = [(par_types[i] + par_types[j], dau_types[i] + dau_types[j])
                    for j in range(i + 1, A)
                    if par_types[i] + par_types[j] != dau_types[i] + dau_types[j]]

        if not changed:
            ln_unchanged += lr
        else:
            nu = sum(1 for pp, _ in changed if pp == 'nn')
            nr = sum(1 for _, dp in changed if dp == 'pp')
            t = nu + nr
            if nr == 0:
                ln_unbind += lr
            elif nu == 0:
                ln_rebind += lr
            else:
                ln_unbind += lr * nu / t
                ln_rebind += lr * nr / t

    ln_total = ln_unbind + ln_rebind + ln_unchanged

    # Apply Borromean ratios and q-weighting
    # The Borromean ratio modifies the WEIGHT of each part
    ln_dressed = (q * abs(R_unbind) * ln_unbind
                  + qi * abs(R_rebind) * ln_rebind
                  + ln_unchanged)

    Q_bare = abs(ln_total) * kappa
    Q_qwt = abs(q * ln_unbind + qi * ln_rebind + ln_unchanged) * kappa
    Q_borr = abs(ln_dressed) * kappa

    return {
        'Q_bare': Q_bare,
        'Q_qwt': Q_qwt,
        'Q_borr': Q_borr,
        'ln_unbind': ln_unbind,
        'ln_rebind': ln_rebind,
        'ln_unchanged': ln_unchanged,
        'R_unbind': R_unbind,
        'R_rebind': R_rebind,
        'unbind_degs': (unbind_parent_deg, unbind_daughter_deg),
        'rebind_degs': (rebind_parent_deg, rebind_daughter_deg),
    }


# ══════════════════════════════════════════════════════════════
# §6  VERIFICATION
# ══════════════════════════════════════════════════════════════

nuclei = [
    (1,   2,   "³H",    Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR),
    (6,   8,   "¹⁴C",   Q_C14_MEV, Q_C14_MEV_ERR),
    (27,  33,  "⁶⁰Co",  Q_CO60_MEV, Q_CO60_MEV_ERR),
    (38,  52,  "⁹⁰Sr",  Q_SR90_MEV, Q_SR90_MEV_ERR),
    (55,  82,  "¹³⁷Cs", Q_CS137_MEV, Q_CS137_MEV_ERR),
    (83,  127, "²¹⁰Bi", Q_BI210_MEV, Q_BI210_MEV_ERR),
]

print("═" * 100)
print("Q-VALUE: BORROMEAN UNBIND-INTERTWINE-REBIND")
print("  1. Undo parent Borromean ring (h⁻ⁿ, n=degree)")
print("  2. Apply crossing change (intertwine)")
print("  3. Redo daughter Borromean ring (hⁿ, n=degree)")
print("  + q·unbind + q⁻¹·rebind Gröbner--Shirshov weighting")
print("═" * 100)
print()
print(f"  q = {q:.10f}")
print()

# Show the Borromean ratios for each shell degree combination
print("Shell degree transitions and Borromean ratios:")
change_word = [(1, 1)]
F_bare = tr(eval_word(change_word))
for pd, dd in [(1, 1), (1, 2), (2, 1), (2, 2)]:
    F = borromean_transition_trace(change_word, pd, dd)
    R = F / F_bare
    print(f"  d{pd}→d{dd}: F_borr = {F:+.6f}, R = F/bare = {abs(R):.6f}")
print()

header = (f"  {'Nuc':>5} │ {'deg':>7} │ {'R_unb':>6} {'R_reb':>6} │"
          f" {'Q_bare':>8} │ {'Q_qwt':>8} │ {'Q_borr':>8} │"
          f" {'Q_exp':>8} │ {'err_qwt':>7} │ {'err_borr':>8}")
print(header)
print("  " + "─" * 95)

errors_qwt = []
errors_borr = []
for Z, N, name, Q_exp, Q_err in nuclei:
    r = Q_borromean(Z, N)
    eq = (r['Q_qwt'] - Q_exp) / Q_exp * 100
    eb = (r['Q_borr'] - Q_exp) / Q_exp * 100
    errors_qwt.append(eq)
    errors_borr.append(eb)

    ud = f"d{r['unbind_degs'][0]}→d{r['unbind_degs'][1]}"
    rd = f"d{r['rebind_degs'][0]}→d{r['rebind_degs'][1]}"
    deg_str = f"{ud}/{rd}"

    m = '◀' if abs(eb) < 1 else ('·' if abs(eb) < 5 else ' ')
    print(f"  {name:>5} │ {deg_str:>7} │ {abs(r['R_unbind']):>6.3f} {abs(r['R_rebind']):>6.3f} │"
          f" {r['Q_bare']:>8.5f} │ {r['Q_qwt']:>8.5f} │ {r['Q_borr']:>8.5f} │"
          f" {Q_exp:>8.5f} │ {eq:>+6.1f}% │ {eb:>+7.1f}%{m}")

print()
mae_q = sum(abs(e) for e in errors_qwt) / len(errors_qwt)
mae_b = sum(abs(e) for e in errors_borr) / len(errors_borr)
rms_q = math.sqrt(sum(e**2 for e in errors_qwt) / len(errors_qwt))
rms_b = math.sqrt(sum(e**2 for e in errors_borr) / len(errors_borr))
print(f"  q-weighted only:  MAE = {mae_q:.1f}%, RMS = {rms_q:.1f}%")
print(f"  + Borromean:      MAE = {mae_b:.1f}%, RMS = {rms_b:.1f}%")
