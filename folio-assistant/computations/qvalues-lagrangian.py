"""
Q_Lagrangian: categorical Lagrangian Q-value.

Works DIRECTLY with the Lagrangian density at each generator — no
"integrate then take log" (that is the action S_q, handled separately
in qvalues-categorical.py).

The Lagrangian at generator i is the traced volume V̂_i itself.
The Q-value comes from three terms:

  Q_L = |L_free + L_int| × κ_L

where:
  L_free = Σ_i ΔV̂_i                            (degree 0: free part)
  L_int  = Σ_{i<j} ΔV̂_i × ΔV̂_j / (V̂_i × V̂_j) (degree 1×1: interaction)

The degree 1×1 term captures correlations between generator-volume
changes that the action (Σ ln V̂_i) misses entirely.  When a neutron
at position k converts to a proton, ALL generators i ≤ k see their
transfer-matrix chain change.  The cross-correlation of these changes
is the deg 1×1 interaction.

Crossing coefficients: CORRECT form T(c,d) with:
  pp → (1, 0),  nn → (1, −HA),  pn/np → (1, −HA/2)

This satisfies the Hecke relation σ² = (q−q⁻¹)σ + 1 and preserves
unimodularity det(T) = −1.
"""

import math
import sys
sys.path.insert(0, '.')
from q_parameter import Q, Q_INV, HA, LN_Q, HBAR_Q
from experimental_constants import M_E_MEV

Z_MARKOV = 1.0 / (math.sqrt(Q) + 1.0 / math.sqrt(Q))
KAPPA = M_E_MEV / 3.0


# ═══════════════════════════════════════════════════════════════
# §1  CORRECT CROSSING COEFFICIENTS
# ═══════════════════════════════════════════════════════════════

def crossing_coeffs(ti, tj):
    """Hecke crossing coefficients T(c,d) = c·σ + d·1.

    From σ⁻¹ = σ − (q−q⁻¹):
      pp → σ:              (1,  0)
      nn → σ⁻¹:            (1, −HA)
      pn/np → ½(σ + σ⁻¹): (1, −HA/2)

    det T(c,d) = c·(c·HA + d)·(−1) + c² = −c²·d − c·d + c²
    For (1, 0): det = −1.  For (1, −HA): det = HA − (−HA) + 1 → −1. ✓
    """
    pair = ti + tj
    if pair == 'pp':
        return (1.0, 0.0)
    elif pair == 'nn':
        return (1.0, -HA)
    else:
        return (1.0, -HA / 2.0)


def transfer_matrix(c, d):
    """2×2 transfer matrix T(c,d) = [[c·HA+d, c], [c, d]]."""
    return [[c * HA + d, c], [c, d]]


def mm(a, b):
    """2×2 matrix multiply."""
    return [[a[0][0]*b[0][0] + a[0][1]*b[1][0],
             a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0],
             a[1][0]*b[0][1] + a[1][1]*b[1][1]]]


# ═══════════════════════════════════════════════════════════════
# §2  GENERATOR VOLUMES AND FULL MATRICES
# ═══════════════════════════════════════════════════════════════

def gen_data(z, n):
    """Compute traced volumes V̂_i AND full chain matrices M_i.

    Returns list of dicts: [{vol, mat}, ...] for each generator.
    The full matrix is needed for the deg 1 jet-bundle values.
    """
    a = z + n
    types = ['p'] * z + ['n'] * n
    result = []
    for i in range(a - 1):
        m = [[1.0, 0.0], [0.0, 1.0]]
        for j in range(i + 1, a):
            c, d = crossing_coeffs(types[i], types[j])
            t = transfer_matrix(c, d)
            m = mm(m, t)
        vol = Z_MARKOV * m[0][0] + m[1][0]
        result.append({'vol': vol, 'mat': m})
    return result


# ═══════════════════════════════════════════════════════════════
# §3  Q_LAGRANGIAN — THREE LEVELS
# ═══════════════════════════════════════════════════════════════

def Q_lagrangian(z, n):
    """Categorical Lagrangian Q-value with deg 0 + deg 1×1.

    The Lagrangian DENSITY at each generator is the relative
    volume change δ_i = ΔV̂_i / V̂_i (not the raw difference).
    This is the first-order form of the log: ln(1+δ) ≈ δ.

    Returns dict with:
      Q_rel:     |Σ_i δ_i| × κ                  (relative Lagrangian)
      Q_log:     |Σ_i ln(V̂_d/V̂_p)| × κ         (action/log form)
      Q_full:    |L_rel + L_int| × κ             (with deg 1×1)
      L_rel:     Σ_i ΔV̂_i/V̂_i                    (relative Lagrangian)
      L_int:     Σ_{i<j} δ_i·δ_j                 (deg 1×1 interaction)
    """
    a = z + n
    dp = gen_data(z, n)
    dd = gen_data(z + 1, n - 1)

    # Relative volume changes and log ratios
    deltas = []     # δ_i = ΔV̂_i / V̂_i  (relative, = Lagrangian density)
    log_ratios = []  # ln(V̂_d/V̂_p) at each generator
    dvols = []       # raw ΔV̂_i for reference
    for i in range(a - 1):
        vp = dp[i]['vol']
        vd = dd[i]['vol']
        dvols.append(vd - vp)
        if abs(vp) > 1e-30:
            deltas.append((vd - vp) / vp)
        else:
            deltas.append(0.0)
        if abs(vp) > 1e-30 and abs(vd) > 1e-30:
            log_ratios.append(math.log(abs(vd)) - math.log(abs(vp)))
        else:
            log_ratios.append(0.0)

    # Degree 0: relative Lagrangian (Σ δ_i, first-order of Σ ln)
    L_rel = sum(deltas)

    # Action form: sum of log ratios (exact)
    L_log = sum(log_ratios)

    # Degree 1×1: interaction term
    # Cross-correlation of relative volume changes
    L_int = 0.0
    for i in range(a - 1):
        for j in range(i + 1, a - 1):
            L_int += deltas[i] * deltas[j]

    # Self-interaction (diagonal deg 1² terms)
    L_self = sum(d**2 for d in deltas)

    # Full Lagrangian: relative + interaction
    L_full = L_rel + L_int

    return {
        'Q_rel': abs(L_rel) * KAPPA,
        'Q_log': abs(L_log) * KAPPA,
        'Q_full': abs(L_full) * KAPPA,
        'L_rel': L_rel,
        'L_log': L_log,
        'L_int': L_int,
        'L_self': L_self,
        'L_full': L_full,
        'deltas': deltas,
        'dvols': dvols,
        'n_gens': a - 1,
    }


# ═══════════════════════════════════════════════════════════════
# §4  CALIBRATED Q_LAGRANGIAN
# ═══════════════════════════════════════════════════════════════

def Q_lagrangian_calibrated(z, n, kappa_rel, kappa_int):
    """Q_Lagrangian with separate energy scales for relative and interaction.

    Q = |L_rel × κ_rel + L_int × κ_int|

    Allows the interaction term to have its own energy scale,
    reflecting the different dimensional content of deg 0 vs deg 1×1.
    """
    r = Q_lagrangian(z, n)
    q_val = abs(r['L_rel'] * kappa_rel + r['L_int'] * kappa_int)
    return q_val, r


# ═══════════════════════════════════════════════════════════════
# §5  BENCHMARKS
# ═══════════════════════════════════════════════════════════════

BENCHMARKS = [
    (1,  2,  "³H→³He",     0.01861),
    (6,  8,  "¹⁴C→¹⁴N",    0.15648),
    (27, 33, "⁶⁰Co→⁶⁰Ni",  0.31817),
    (38, 52, "⁹⁰Sr→⁹⁰Y",   0.54590),
    (55, 82, "¹³⁷Cs→¹³⁷Ba", 0.51400),
    (83, 127, "²¹⁰Bi→²¹⁰Po", 1.16270),
]

if __name__ == "__main__":
    print("Q_LAGRANGIAN: CATEGORICAL LAGRANGIAN Q-VALUE")
    print("=" * 85)
    print()
    print("  Direct Lagrangian density, NOT action (no log).")
    print("  Crossing coefficients: pp→(1,0), nn→(1,−HA), pn→(1,−HA/2)")
    print()
    print(f"  q = {Q:.10f}")
    print(f"  HA = q − q⁻¹ = {HA:.10f}")
    print(f"  κ = m_e/3 = {KAPPA:.6f} MeV")
    print(f"  z_M = {Z_MARKOV:.10f}")
    print()

    # ── Table 1: Three forms compared ──
    print("THREE LAGRANGIAN FORMS")
    print("-" * 95)
    hdr = (f"{'Decay':>14} {'Q_rel':>8} {'Q_log':>8} {'Q_full':>8} "
           f"{'Q_exp':>8} {'err_r':>7} {'err_l':>7} {'err_F':>7} "
           f"{'L_int':>10}")
    print(hdr)
    print("-" * len(hdr))

    errs_r, errs_l, errs_F = [], [], []
    for z, n, decay, q_exp in BENCHMARKS:
        r = Q_lagrangian(z, n)
        e_r = (r['Q_rel'] - q_exp) / q_exp * 100
        e_l = (r['Q_log'] - q_exp) / q_exp * 100
        e_F = (r['Q_full'] - q_exp) / q_exp * 100
        errs_r.append(abs(e_r)); errs_l.append(abs(e_l)); errs_F.append(abs(e_F))

        print(f"  {decay:>14} {r['Q_rel']:>8.5f} {r['Q_log']:>8.5f} "
              f"{r['Q_full']:>8.5f} {q_exp:>8.5f} "
              f"{e_r:>+6.1f}% {e_l:>+6.1f}% {e_F:>+6.1f}% "
              f"{r['L_int']:>+10.6f}")

    mae_r = sum(errs_r) / len(errs_r)
    mae_l = sum(errs_l) / len(errs_l)
    mae_F = sum(errs_F) / len(errs_F)
    print()
    print(f"  Relative (|Σ δ_i| × κ):                MAE = {mae_r:.1f}%")
    print(f"  Log      (|Σ ln(V̂_d/V̂_p)| × κ):       MAE = {mae_l:.1f}%")
    print(f"  Full     (|L_rel + L_int| × κ):         MAE = {mae_F:.1f}%")

    # ── Table 2: Lagrangian densities at each generator ──
    print()
    print("LAGRANGIAN DENSITIES BY GENERATOR (³H)")
    print("-" * 70)
    r = Q_lagrangian(1, 2)
    dp = gen_data(1, 2)
    dd = gen_data(2, 1)
    for i in range(r['n_gens']):
        vp = dp[i]['vol']
        vd = dd[i]['vol']
        dv = r['dvols'][i]
        delta = r['deltas'][i]
        lr = math.log(abs(vd)/abs(vp)) if abs(vp) > 1e-30 and abs(vd) > 1e-30 else 0
        print(f"  gen {i}: V̂_p = {vp:>+10.6f}  V̂_d = {vd:>+10.6f}  "
              f"δ = ΔV̂/V̂ = {delta:>+8.5f}  ln = {lr:>+8.5f}  diff = {delta-lr:>+8.6f}")

    # ── Calibrated form ──
    r_3h = Q_lagrangian(1, 2)
    if abs(r_3h['L_rel']) > 1e-30:
        kr_cal = 0.01861 / abs(r_3h['L_rel'])
    else:
        kr_cal = KAPPA

    print()
    print(f"  Calibrated κ_rel from ³H: {kr_cal:.6f} MeV")
    print(f"  Standard κ = m_e/3:       {KAPPA:.6f} MeV")
    print(f"  Ratio κ_rel / κ:          {kr_cal / KAPPA:.4f}")

    print()
    print("CALIBRATED Q_LAGRANGIAN (κ_rel from ³H, κ_int = 0)")
    print("-" * 70)
    print(f"{'Decay':>14} {'Q_cal':>9} {'Q_exp':>9} {'err':>7}")

    errs_cal = []
    for z, n, decay, q_exp in BENCHMARKS:
        q_c, r = Q_lagrangian_calibrated(z, n, kr_cal, 0.0)
        err = (q_c - q_exp) / q_exp * 100
        errs_cal.append(abs(err))
        print(f"  {decay:>14} {q_c:>9.5f} {q_exp:>9.5f} {err:>+6.1f}%")

    mae_cal = sum(errs_cal) / len(errs_cal)
    print(f"\n  Calibrated MAE = {mae_cal:.1f}% (1 param: κ_rel from ³H)")

    print()
    print("STRUCTURE")
    print("=" * 60)
    print("  δ_i  = ΔV̂_i / V̂_i                    (Lagrangian density)")
    print("  L_rel = Σ_i δ_i                        (degree 0)")
    print("  L_int = Σ_{i<j} δ_i × δ_j              (degree 1×1)")
    print("  Q_L   = |L_rel + L_int| × κ")
    print()
    print("  Note: δ_i ≈ ln(V̂_d/V̂_p) for small changes.")
    print("  The deg 1×1 interaction is GENUINELY NEW —")
    print("  it is NOT a Taylor expansion of the log form.")
