"""
Full categorical Q-value: the PRIMARY definition.

Q_q := S_q(N_par) - S_q(N_dau) - S_q(e) + δ_q

where S_q(K) = tr_τ(ρ(β_K)) is the categorical action (Markov trace
of the braid representation). This is the Skein polynomial ∏V̂_i.

No F_shell. No F_I10. No q-weighting. No empirical corrections.
Everything from q and the categorical action.

The three terms:
  1. ln P_par - ln P_dau     (Skein polynomial ratio = ∏V̂_i ratio)
  2. -ln J(T_{2,3}, q)       (electron Jones polynomial)
  3. (∂ln P/∂q) × Δq_eff    (q-anomaly from self-deformation)

The neutrino term vanishes: S_q(unknot) = 1, ln(1) = 0.
"""

import math
import sys
sys.path.insert(0, '.')
from q_parameter import Q, Q_INV, HA, LN_Q, HBAR_Q, Q_ERR
from experimental_constants import M_E_MEV

# ═══════════════════════════════════════════════════════════════
# §1  CONSTANTS FROM q
# ═══════════════════════════════════════════════════════════════

S_SK = math.sqrt(Q) - 1.0 / math.sqrt(Q)
Z_MARKOV = 1.0 / (math.sqrt(Q) + 1.0 / math.sqrt(Q))
KAPPA = M_E_MEV / 3.0  # m_e / cr(T_{2,3})


# ═══════════════════════════════════════════════════════════════
# §2  S_q(e) — ELECTRON CATEGORICAL ACTION
# ═══════════════════════════════════════════════════════════════

def jones_trefoil(q):
    """Jones polynomial of the right-hand trefoil T_{2,3} at q.

    J(T_{2,3}, q) = -q^{-4} + q^{-3} + q^{-1}

    This is the standard Jones polynomial in the Skein variable q.
    The electron IS the trefoil — its categorical action is J.
    """
    return -q**(-4) + q**(-3) + q**(-1)


def S_q_electron():
    """ln|S_q(e)| = ln|J(T_{2,3}, q₀)|."""
    j = jones_trefoil(Q)
    return math.log(abs(j))


# ═══════════════════════════════════════════════════════════════
# §3  S_q(N) — NUCLEAR CATEGORICAL ACTION
# ═══════════════════════════════════════════════════════════════

def crossing_coeffs(ti, tj):
    pair = ti + tj
    if pair == 'pp':
        return (1.0, 0.0)
    elif pair == 'nn':
        return (Q**2, -Q * S_SK)
    else:
        return ((1.0 + Q**2) / 2.0, -Q * S_SK / 2.0)


def S_q_nucleus(z, n):
    """Categorical action S_q(N) = ln|∏ V̂_i| for nucleus (Z, N).

    The Skein polynomial P(q) = ∏_i V̂_i(q) IS the Markov trace
    of the nuclear braid representation. Its log is the action.

    Returns ln|P(q)|.
    """
    a = z + n
    types = ['p'] * z + ['n'] * n
    ln_P = 0.0
    for i in range(a - 1):
        m = [[1.0, 0.0], [0.0, 1.0]]
        for j in range(i + 1, a):
            c, d = crossing_coeffs(types[i], types[j])
            t = [[c * HA + d, c], [c, d]]
            m = [[m[0][0]*t[0][0] + m[0][1]*t[1][0],
                  m[0][0]*t[0][1] + m[0][1]*t[1][1]],
                 [m[1][0]*t[0][0] + m[1][1]*t[1][0],
                  m[1][0]*t[0][1] + m[1][1]*t[1][1]]]
        vol = Z_MARKOV * m[0][0] + m[1][0]
        ln_P += math.log(abs(vol))
    return ln_P


# ═══════════════════════════════════════════════════════════════
# §4  δ_q — THE q-ANOMALY (SELF-DEFORMATION)
# ═══════════════════════════════════════════════════════════════

def delta_q_correction(z, n):
    """The q-anomaly from self-deformation.

    Δq_eff = (A-1)/A² × ℏ_q²

    The correction to Q is:
      δ_q = (∂ ln P / ∂q) × Δq_eff

    We compute ∂ln P/∂q numerically: finite difference.
    """
    a = z + n
    dq_eff = (a - 1) / a**2 * HBAR_Q**2

    # Numerical derivative of S_q(par) - S_q(dau) w.r.t. q
    # Use central difference with step h
    h = Q_ERR * 100  # ~1.4e-7
    # Save globals, perturb
    import copy

    def Q_at(q_val):
        """Compute ln P_par - ln P_dau at a given q."""
        q_old = Q
        ha = q_val - 1.0 / q_val
        s = math.sqrt(q_val) - 1.0 / math.sqrt(q_val)
        zm = 1.0 / (math.sqrt(q_val) + 1.0 / math.sqrt(q_val))

        def _crossing(ti, tj):
            pair = ti + tj
            if pair == 'pp': return (1.0, 0.0)
            elif pair == 'nn': return (q_val**2, -q_val * s)
            else: return ((1.0 + q_val**2) / 2.0, -q_val * s / 2.0)

        def _ln_P(zz, nn):
            a = zz + nn
            types = ['p'] * zz + ['n'] * nn
            lp = 0.0
            for i in range(a - 1):
                m = [[1.0, 0.0], [0.0, 1.0]]
                for j in range(i + 1, a):
                    c, d = _crossing(types[i], types[j])
                    t = [[c*ha+d, c], [c, d]]
                    m = [[m[0][0]*t[0][0]+m[0][1]*t[1][0],
                          m[0][0]*t[0][1]+m[0][1]*t[1][1]],
                         [m[1][0]*t[0][0]+m[1][1]*t[1][0],
                          m[1][0]*t[0][1]+m[1][1]*t[1][1]]]
                vol = zm * m[0][0] + m[1][0]
                lp += math.log(abs(vol))
            return lp

        return _ln_P(z, n) - _ln_P(z + 1, n - 1)

    # Central difference
    dSdq = (Q_at(Q + h) - Q_at(Q - h)) / (2 * h)

    return dq_eff * dSdq, dq_eff, dSdq


# ═══════════════════════════════════════════════════════════════
# §5  FULL CATEGORICAL Q
# ═══════════════════════════════════════════════════════════════

def Q_categorical(z, n):
    """Full categorical Q-value.

    Q_q = |S_q(par) - S_q(dau) - S_q(e)| × κ + δ_q × κ

    In log space:
      Q_q = |ln P_par - ln P_dau - ln J(T_{2,3})| × κ
            + (∂(ln P_par - ln P_dau)/∂q) × Δq_eff × κ
    """
    # Term 1: nuclear action difference
    ln_P_par = S_q_nucleus(z, n)
    ln_P_dau = S_q_nucleus(z + 1, n - 1)
    delta_S = ln_P_par - ln_P_dau  # should be negative (daughter more bound)

    # Term 2: electron action
    ln_J_e = S_q_electron()

    # Term 3: q-anomaly
    dq_corr, dq_eff, dSdq = delta_q_correction(z, n)

    # Full categorical Q (no F_shell, no F_I10, no q-weighting)
    Q_cat = abs(delta_S - ln_J_e) * KAPPA + dq_corr * KAPPA

    # For comparison: the bare Skein ratio (no electron, no anomaly)
    Q_bare = abs(delta_S) * KAPPA

    # For comparison: with electron but no anomaly
    Q_with_e = abs(delta_S - ln_J_e) * KAPPA

    return {
        'Q_cat': Q_cat,
        'Q_bare': Q_bare,
        'Q_with_e': Q_with_e,
        'delta_S': delta_S,
        'ln_J_e': ln_J_e,
        'dq_corr': dq_corr,
        'dq_eff': dq_eff,
        'dSdq': dSdq,
    }


# ═══════════════════════════════════════════════════════════════
# §6  BENCHMARKS
# ═══════════════════════════════════════════════════════════════

BENCHMARKS = [
    (1,  2,  "3H",    0.01861, 0.00001),
    (6,  8,  "14C",   0.15648, 0.00004),
    (27, 33, "60Co",  0.31817, 0.00013),
    (38, 52, "90Sr",  0.54590, 0.00007),
    (55, 82, "137Cs", 0.51400, 0.00021),
    (83, 127, "210Bi", 1.16270, 0.00006),
]

if __name__ == "__main__":
    print("FULL CATEGORICAL Q-VALUE")
    print("Q_q = |S_q(par) - S_q(dau) - S_q(e)| x kappa + delta_q x kappa")
    print("=" * 90)
    print()
    print(f"  S_q(e) = ln|J(T_{{2,3}}, q)| = {S_q_electron():.6f}")
    print(f"  J(T_{{2,3}}, q₀) = {jones_trefoil(Q):.6f}")
    print(f"  kappa = m_e / 3 = {KAPPA:.6f} MeV")
    print(f"  hbar_q = {HBAR_Q:.6f}")
    print()

    header = (f"{'Nuc':>6} {'Q_bare':>8} {'Q_+e':>8} {'Q_cat':>8} "
              f"{'Q_exp':>8} {'err_b':>7} {'err_e':>7} {'err_c':>7} "
              f"{'dq_eff':>10} {'dS/dq':>8}")
    print(header)
    print("-" * len(header))

    errs_b, errs_e, errs_c = [], [], []
    for z, n, nuc, q_exp, dq_exp in BENCHMARKS:
        r = Q_categorical(z, n)
        e_b = (r['Q_bare'] - q_exp) / q_exp * 100
        e_e = (r['Q_with_e'] - q_exp) / q_exp * 100
        e_c = (r['Q_cat'] - q_exp) / q_exp * 100
        errs_b.append(abs(e_b))
        errs_e.append(abs(e_e))
        errs_c.append(abs(e_c))

        print(f"{nuc:>6} {r['Q_bare']:>8.5f} {r['Q_with_e']:>8.5f} {r['Q_cat']:>8.5f} "
              f"{q_exp:>8.5f} {e_b:>+6.1f}% {e_e:>+6.1f}% {e_c:>+6.1f}% "
              f"{r['dq_eff']:>10.6f} {r['dSdq']:>+8.2f}")

    print()
    mae_b = sum(errs_b) / len(errs_b)
    mae_e = sum(errs_e) / len(errs_e)
    mae_c = sum(errs_c) / len(errs_c)
    print(f"  Bare (|ln P ratio| x kappa):           MAE = {mae_b:.1f}%")
    print(f"  + electron (-ln J(T_{{2,3}})):           MAE = {mae_e:.1f}%")
    print(f"  + q-anomaly (full categorical):        MAE = {mae_c:.1f}%")
    print()
    print("  No F_shell, no F_I10, no q-weighting.")
    print("  Pure categorical action difference.")
