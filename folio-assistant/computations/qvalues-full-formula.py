"""
Full Q-value formula with all corrections from the paper:
  1. Bare Skein polynomial ratio (transfer matrix)
  2. Torus knot shell corrections T_{2,n}
  3. Weak vertex T_{3,5}
  4. I₁₀ pairing correction
  5. κ = m_e / cr(T_{2,3}) (algebraically derived)

From shell-construction-rules.md, the formula is:
  Q = |R_bare + Δ_shell + Δ_{T_{3,5}}| × ℏ_q × E_× × μ₀

where:
  R_bare = log_q(P_dau / P_par)  (transfer matrix Skein ratio)
  Δ_shell = Σ [log_q τ(n_dau) - log_q τ(n_par)]  (torus knot shell)
  Δ_{T_{3,5}} = log_q tr(T_{3,5})  (weak vertex)
  ℏ_q × E_× × μ₀ = ℏ_q × (HA/2) × m_e/(3 × HA/2) = ℏ_q × m_e/3

Wait — the paper says ℏ_q × E_× × μ₀, but:
  E_× × μ₀ = (HA/2) × m_e/(3 × HA/2) = m_e/3 = κ
  So the formula is Q = |...| × ℏ_q × κ

The current formula uses κ_q = ln(q) × κ (without ℏ_q).
The paper formula uses ℏ_q × κ.
  ℏ_q = 1 - q⁻¹ ≈ 0.09908
  ln(q) ≈ 0.10434
  Ratio: ℏ_q / ln(q) = 0.9496

These differ by ~5%! Which is correct?
  ℏ_q = 1 - q⁻¹ (algebraic — exact in q)
  ln(q) (transcendental — requires evaluation at q₀)

The algebraic form ℏ_q is more fundamental. Let's test both.
"""

import math
import sys
sys.path.insert(0, '.')
from q_parameter import Q, Q_INV, HA, LN_Q, HBAR_Q, Q_ERR
from experimental_constants import M_E_MEV

# ── Constants from q ─────────────────────────────────────────────
E_CROSS = HA / 2
S_SKEIN = math.sqrt(Q) - 1.0/math.sqrt(Q)
Z_MARKOV = 1.0 / (math.sqrt(Q) + 1.0/math.sqrt(Q))
KAPPA = M_E_MEV / 3.0     # m_e / cr(T_{2,3})
KAPPA_Q = LN_Q * KAPPA     # current formula: ln(q) × κ
KAPPA_H = HBAR_Q * KAPPA   # paper formula: ℏ_q × κ

MAGIC = [2, 8, 20, 28, 50, 82, 126]

# I₁₀ pairing
R_pp = 0.598688; R_nn = 0.471218
delta_pp = 1 - R_pp; delta_nn = 1 - R_nn

def shell_degree(n):
    for i, m in enumerate(MAGIC):
        if n <= m: return 2 if i+1 >= 5 else 1
    return 2

def m_leq(x):
    """Largest magic number ≤ x."""
    for m in reversed(MAGIC):
        if m <= x: return m
    return 0

def m_lt(x):
    """Largest magic number < x."""
    for m in reversed(MAGIC):
        if m < x: return m
    return 0

def n_out(x):
    """Nucleon count in outermost open shell."""
    return x - m_leq(x)

def n_shell(x):
    """Size of the shell containing x."""
    return m_leq(x) - m_lt(x)

def parity(z, n):
    if z%2==0 and n%2==0: return "ee"
    elif z%2==1 and n%2==1: return "oo"
    else: return "oA"

# ── Torus knot Markov trace ─────────────────────────────────────

def markov_trace_T2n(n_occ):
    """Markov trace of σ^n in H_2(q).

    Uses Chebyshev recurrence:
      τ(0) = 1
      τ(1) = z × HA + 1 = z(q - q⁻¹) + 1
      τ(n) = HA × τ(n-1) + τ(n-2)  (from σ² = HA·σ + 1)

    Actually, the traced volume of the chain with n crossings:
      V̂(T_{2,n}) = z × M[0,0] + M[1,0]
    where M = T(1,0)^n (pp crossings).
    """
    if n_occ <= 0:
        return 1.0  # identity
    # Build T(1,0)^n
    m = [[1.0, 0.0], [0.0, 1.0]]
    t_pp = [[HA, 1.0], [1.0, 0.0]]
    for _ in range(n_occ):
        m = [[m[0][0]*t_pp[0][0]+m[0][1]*t_pp[1][0], m[0][0]*t_pp[0][1]+m[0][1]*t_pp[1][1]],
             [m[1][0]*t_pp[0][0]+m[1][1]*t_pp[1][0], m[1][0]*t_pp[0][1]+m[1][1]*t_pp[1][1]]]
    return Z_MARKOV * m[0][0] + m[1][0]

def log_q(x):
    """log_q(x) = ln(x) / ln(q)."""
    if x <= 0: return 0.0
    return math.log(x) / LN_Q

# ── Weak vertex ──────────────────────────────────────────────────

def weak_vertex_T35():
    """log_q of Markov trace of T_{3,5} in H_3(q).

    T_{3,5} = (σ₁σ₂)^5 in B₃. The Markov trace involves the
    full H₃(q) representation. Computed from the paper's value.
    """
    # From shell-construction-rules.md: Δ_{T_{3,5}} = -3.370
    # Let's verify from the 6×6 transfer matrix...
    # For now use the paper's value and note it should be derived
    return -3.370

# ── Transfer matrix Skein ratio ──────────────────────────────────

def crossing_coeffs(ti, tj):
    pair = ti + tj
    if pair == 'pp': return (1.0, 0.0)
    elif pair == 'nn': return (Q**2, -Q * S_SKEIN)
    else: return ((1.0 + Q**2)/2.0, -Q * S_SKEIN / 2.0)

def skein_polynomial(z, n):
    """Product of traced volumes ∏ V̂_i."""
    a = z + n
    types = ['p']*z + ['n']*n
    product = 1.0
    for i in range(a-1):
        m = [[1.0, 0.0], [0.0, 1.0]]
        for j in range(i+1, a):
            c, d = crossing_coeffs(types[i], types[j])
            t = [[c*HA+d, c], [c, d]]
            m = [[m[0][0]*t[0][0]+m[0][1]*t[1][0], m[0][0]*t[0][1]+m[0][1]*t[1][1]],
                 [m[1][0]*t[0][0]+m[1][1]*t[1][0], m[1][0]*t[0][1]+m[1][1]*t[1][1]]]
        vol = Z_MARKOV * m[0][0] + m[1][0]
        product *= vol
    return product

def R_bare(z, n):
    """log_q(P_dau / P_par) — bare Skein polynomial ratio."""
    p_par = skein_polynomial(z, n)
    p_dau = skein_polynomial(z+1, n-1)
    if abs(p_par) < 1e-300 or abs(p_dau) < 1e-300:
        return 0.0
    return log_q(abs(p_dau)) - log_q(abs(p_par))

# ── Full Q-value ─────────────────────────────────────────────────

def Q_full(z, n):
    """Full Q-value with all corrections."""
    a = z + n

    # Step 1: Outer shell occupancies
    np_par = n_out(z);     nn_par = n_out(n)
    np_dau = n_out(z+1);   nn_dau = n_out(n-1)

    # For magic closures, use full shell size
    np_par_eff = n_shell(z) if np_par == 0 and z in MAGIC else np_par
    nn_par_eff = n_shell(n) if nn_par == 0 and n in MAGIC else nn_par
    np_dau_eff = n_shell(z+1) if np_dau == 0 and (z+1) in MAGIC else np_dau
    nn_dau_eff = n_shell(n-1) if nn_dau == 0 and (n-1) in MAGIC else nn_dau

    # Step 2: Torus knot traces
    tau_p_par = markov_trace_T2n(np_par_eff)
    tau_n_par = markov_trace_T2n(nn_par_eff)
    tau_p_dau = markov_trace_T2n(np_dau_eff)
    tau_n_dau = markov_trace_T2n(nn_dau_eff)

    # Step 3: Bare ratio
    r_bare = R_bare(z, n)

    # Step 4: Shell correction
    delta_shell = (log_q(tau_p_dau) - log_q(tau_p_par)) + \
                  (log_q(tau_n_dau) - log_q(tau_n_par))

    # Step 5: Weak vertex
    delta_weak = weak_vertex_T35()

    # Step 7: Q-value (paper formula)
    q_paper = abs(r_bare + delta_shell + delta_weak) * KAPPA_H

    # Also compute with current formula (for comparison)
    q_current = abs(r_bare) * KAPPA_Q  # without shell/weak corrections

    # I₁₀ pairing
    deg = shell_degree(n)
    f_deg = 0.5904 if deg >= 2 else 1.0
    if n in MAGIC and deg >= 2: f_deg *= 0.6382
    par = parity(z, n); par_d = parity(z+1, n-1)
    f_i10 = 1.0
    if deg >= 2 and par == "oo" and par_d == "ee":
        f_i10 = (1 - delta_pp/z) * (1 - delta_nn/n)
    elif deg >= 2 and par == "oA":
        f_i10 = (1 - delta_pp/(2*z)) if z%2==1 else (1 - delta_nn/(2*n))

    q_current_i10 = q_current * f_deg * f_i10

    return {
        'r_bare': r_bare,
        'delta_shell': delta_shell,
        'delta_weak': delta_weak,
        'q_paper': q_paper,
        'q_current': q_current_i10,
        'np_par': np_par_eff, 'nn_par': nn_par_eff,
        'np_dau': np_dau_eff, 'nn_dau': nn_dau_eff,
        'tau_p': (tau_p_par, tau_p_dau),
        'tau_n': (tau_n_par, tau_n_dau),
    }


BENCHMARKS = [
    (1,  2,  "³H",      0.01861, 0.00001),
    (6,  8,  "¹⁴C",     0.15648, 0.00004),
    (27, 33, "⁶⁰Co",    0.31817, 0.00013),
    (38, 52, "⁹⁰Sr",    0.54590, 0.00007),
    (55, 82, "¹³⁷Cs",   0.51400, 0.00021),
    (83, 127,"²¹⁰Bi",   1.16270, 0.00006),
]

if __name__ == "__main__":
    print("=" * 95)
    print("FULL Q-VALUE FORMULA: bare + torus knot + weak vertex + I₁₀")
    print("=" * 95)
    print(f"\n  κ = m_e / cr(T_{{2,3}}) = {KAPPA:.6f} MeV")
    print(f"  κ_q = ln(q) × κ = {KAPPA_Q:.6f} MeV  (current formula)")
    print(f"  κ_h = ℏ_q × κ = {KAPPA_H:.6f} MeV  (paper formula)")
    print(f"  Ratio ℏ_q/ln(q) = {HBAR_Q/LN_Q:.4f}")
    print(f"  Δ_{{T_{{3,5}}}} = {weak_vertex_T35():.3f}")

    print(f"\n{'Nuc':>7} {'R_bare':>8} {'Δ_shell':>8} {'Δ_weak':>7} {'Q_paper':>8} {'Q_curr':>8} {'Q_exp':>8} {'±δ':>7} {'err_p':>7} {'err_c':>7}")
    print("-" * 90)

    errs_p, errs_c = [], []
    for z, n, nuc, q_exp, dq in BENCHMARKS:
        r = Q_full(z, n)
        e_p = (r['q_paper'] - q_exp) / q_exp * 100
        e_c = (r['q_current'] - q_exp) / q_exp * 100
        errs_p.append(abs(e_p))
        errs_c.append(abs(e_c))
        mark_p = "◀" if abs(e_p) < 5 else " "
        mark_c = "◀" if abs(e_c) < 5 else " "
        print(f"{nuc:>7} {r['r_bare']:>+8.3f} {r['delta_shell']:>+8.3f} {r['delta_weak']:>+7.3f} "
              f"{r['q_paper']:>8.5f} {r['q_current']:>8.5f} {q_exp:>8.5f} {dq:>7.5f} "
              f"{e_p:>+6.1f}%{mark_p}{e_c:>+6.1f}%{mark_c}")

        # Show shell details
        print(f"        shells: p({r['np_par']}→{r['np_dau']}) n({r['nn_par']}→{r['nn_dau']})  "
              f"τ_p=({r['tau_p'][0]:.3f}→{r['tau_p'][1]:.3f}) τ_n=({r['tau_n'][0]:.3f}→{r['tau_n'][1]:.3f})")

    mae_p = sum(errs_p)/len(errs_p); mae_c = sum(errs_c)/len(errs_c)
    print(f"\n  Paper formula:   MAE = {mae_p:.1f}%")
    print(f"  Current formula: MAE = {mae_c:.1f}% (with I₁₀)")
