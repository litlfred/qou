"""
Unified Q-value comparison: all methods side-by-side.

Compares five approaches for β-decay Q-values:

  1. Q_lag(κ)     — Lagrangian (relative), energy scale κ = m_e/3
  2. Q_lag(κ_q)   — Lagrangian (relative), energy scale κ_q = ln(q)·m_e/3
  3. Q_dirac(κ)   — Dirac (sym+alt channels), energy scale κ = m_e/3
  4. Q_dirac(κ_q) — Dirac (sym+alt channels), energy scale κ_q = ln(q)·m_e/3
  5. Q_from_q     — q-weighted log_q with shell factors, energy scale κ_q
  6. Q_E₀         — E₀ calibration from free neutron decay (Rust engine)

Energy scales:
  κ   = m_e / 3            = 0.170333 MeV  (geometric: 3 quarks per nucleon)
  κ_q = ln(q) · m_e / 3    = 0.017773 MeV  (substrate-weighted)
  E₀  = Q_neutron / |Δnet|  = 1.470 MeV     (typed Borromean NF, 3 strands)

The "3" in κ = m_e/3:
  This divides the electron rest energy among the three quarks that
  participate in the β transition.  The crossing energy E_× = ½(q−q⁻¹)
  is per crossing; κ folds it into a per-nucleon energy via the
  3-quark Borromean structure.

Note: Protium (¹H, Z=1, N=0) has A=1 nucleon → 0 generators in the
transfer matrix chain.  It cannot undergo β⁻ decay (would require
p → n + e⁺ + ν, energetically forbidden: Q < 0).  The protium
Hecke NF from quark-level computation (protium-witness.py) gives
the atom's *formation* amplitude, not a decay Q-value.
"""

import math
import sys
sys.path.insert(0, '.')
from q_parameter import Q, Q_INV, HA, LN_Q, HBAR_Q
from experimental_constants import M_E_MEV, Q_NEUTRON_MEV

# ── Energy scales ────────────────────────────────────────────────
KAPPA = M_E_MEV / 3.0              # m_e / 3  (per-quark energy)
KAPPA_Q = LN_Q * M_E_MEV / 3.0     # ln(q) × m_e / 3  (substrate-weighted)
Z_MARKOV = 1.0 / (math.sqrt(Q) + 1.0 / math.sqrt(Q))


# ── Transfer matrix engine ───────────────────────────────────────

def crossing_coeffs(ti, tj):
    pair = ti + tj
    if pair == 'pp':
        return (1.0, 0.0)
    elif pair == 'nn':
        return (1.0, -HA)
    else:
        return (1.0, -HA / 2.0)


def transfer_matrix(c, d):
    return [[c * HA + d, c], [c, d]]


def mm(a, b):
    return [[a[0][0]*b[0][0] + a[0][1]*b[1][0],
             a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0],
             a[1][0]*b[0][1] + a[1][1]*b[1][1]]]


def gen_data(z, n):
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
        tr_m = m[0][0] + m[1][1]
        spread = m[0][0] - m[1][1]
        result.append({'vol': vol, 'mat': m, 'tr': tr_m, 'spread': spread})
    return result


# ── Q_lagrangian (relative form) ─────────────────────────────────

def compute_lagrangian(z, n):
    a = z + n
    dp = gen_data(z, n)
    dd = gen_data(z + 1, n - 1)
    deltas = []
    log_ratios = []
    for i in range(a - 1):
        vp = dp[i]['vol']
        vd = dd[i]['vol']
        deltas.append((vd - vp) / vp if abs(vp) > 1e-30 else 0.0)
        if abs(vp) > 1e-30 and abs(vd) > 1e-30:
            log_ratios.append(math.log(abs(vd)) - math.log(abs(vp)))
        else:
            log_ratios.append(0.0)
    return sum(deltas), sum(log_ratios)


# ── Q_dirac (sym + alt channels) ─────────────────────────────────

def compute_dirac(z, n):
    a = z + n
    dp = gen_data(z, n)
    dd = gen_data(z + 1, n - 1)
    rel_traces = []
    rel_spreads = []
    for i in range(a - 1):
        dtr = dd[i]['tr'] - dp[i]['tr']
        rel_traces.append(dtr / dp[i]['tr'] if abs(dp[i]['tr']) > 1e-30 else 0.0)
        dspr = dd[i]['spread'] - dp[i]['spread']
        rel_spreads.append(dspr / dp[i]['spread'] if abs(dp[i]['spread']) > 1e-30 else 0.0)
    D_sym = Q_INV * sum(rel_traces)
    D_alt = HBAR_Q * sum(rel_spreads)
    return D_sym + D_alt


# ── Q_from_q (q-weighted log_q, from qvalues-from-q.py) ─────────

MAGIC = [2, 8, 20, 28, 50, 82, 126]
F_DEG2 = 0.5949

def shell_degree(n_neutrons):
    for i, m in enumerate(MAGIC):
        if n_neutrons <= m:
            return 2 if i + 1 >= 5 else 1
    return 2


def compute_from_q(z, n):
    """Simplified version of qvalues-from-q.py logic."""
    a = z + n
    dp = gen_data(z, n)
    dd = gen_data(z + 1, n - 1)

    s_u, s_r, s_uc = 0.0, 0.0, 0.0
    types_p = ['p'] * z + ['n'] * n
    types_d = ['p'] * (z + 1) + ['n'] * (n - 1)

    for i in range(a - 1):
        vp = dp[i]['vol']
        vd = dd[i]['vol']
        if abs(vp) < 1e-30 or abs(vd) < 1e-30:
            continue
        ratio = abs(vd) / abs(vp)
        if ratio <= 0:
            continue
        lr = math.log(ratio) / LN_Q  # log_q ratio

        # Classify: unbinding if nn→pn, rebinding if pn→pp, else unchanged
        tp = types_p[i] + types_p[min(i + 1, a - 1)]
        td = types_d[i] + types_d[min(i + 1, a - 1)]
        if 'nn' in tp and 'nn' not in td:
            s_u += lr
        elif 'pp' not in tp and 'pp' in td:
            s_r += lr
        else:
            s_uc += lr

    raw = abs(Q * s_u + Q_INV * s_r + s_uc)

    deg_p = shell_degree(n)
    deg_d = shell_degree(n - 1)
    F = 1.0
    if deg_p == 2 and deg_d != 2:
        F = F_DEG2
    elif deg_p != 2 and deg_d == 2:
        F = F_DEG2

    return raw * KAPPA_Q * F


# ── Benchmarks ───────────────────────────────────────────────────

BENCHMARKS = [
    (1,  2,  "³H→³He",     0.01861),
    (6,  8,  "¹⁴C→¹⁴N",    0.15648),
    (27, 33, "⁶⁰Co→⁶⁰Ni",  0.31817),
    (38, 52, "⁹⁰Sr→⁹⁰Y",   0.54590),
    (55, 82, "¹³⁷Cs→¹³⁷Ba", 0.51400),
    (83, 127, "²¹⁰Bi→²¹⁰Po", 1.16270),
]


if __name__ == "__main__":
    print("UNIFIED Q-VALUE COMPARISON: ALL METHODS")
    print("=" * 120)
    print()
    print(f"  q₀ = {Q:.10f}")
    print(f"  HA = q − q⁻¹ = {HA:.10f}")
    print(f"  ln(q) = {LN_Q:.10f}")
    print()
    print("  Energy scales:")
    print(f"    κ   = m_e / 3          = {KAPPA:.6f} MeV  (per-quark geometric)")
    print(f"    κ_q = ln(q) · m_e / 3  = {KAPPA_Q:.6f} MeV  (substrate-weighted)")
    print(f"    E₀  = Q_n / |Δnet|     ≈ 1.470 MeV       (typed Borromean, 3 strands)")
    print()
    print("  Why 3 in κ = m_e/3?")
    print("    Each nucleon has 3 quarks. The crossing energy E_× = ½(q−q⁻¹)")
    print("    acts per crossing; dividing by 3 gives the per-quark contribution")
    print("    to the nucleon-level energy scale.")
    print()

    # ── Table: all methods with κ (m_e/3) ──
    print("TABLE 1: Q-VALUES WITH κ = m_e/3 = {:.6f} MeV".format(KAPPA))
    print("-" * 120)
    hdr = (f"{'Decay':>14} │ {'Q_exp':>8} │ {'Q_lag':>8} {'err':>7} │ "
           f"{'Q_log':>8} {'err':>7} │ {'Q_dir':>8} {'err':>7} │")
    print(hdr)
    print("-" * len(hdr))

    for z, n, decay, q_exp in BENCHMARKS:
        L_rel, L_log = compute_lagrangian(z, n)
        D_full = compute_dirac(z, n)
        ql = abs(L_rel) * KAPPA
        qlog = abs(L_log) * KAPPA
        qd = abs(D_full) * KAPPA
        el = (ql - q_exp) / q_exp * 100
        elog = (qlog - q_exp) / q_exp * 100
        ed = (qd - q_exp) / q_exp * 100
        print(f"  {decay:>14} │ {q_exp:>8.5f} │ {ql:>8.5f} {el:>+6.1f}% │ "
              f"{qlog:>8.5f} {elog:>+6.1f}% │ {qd:>8.5f} {ed:>+6.1f}% │")

    print()

    # ── Table: all methods with κ_q (ln(q)·m_e/3) ──
    print("TABLE 2: Q-VALUES WITH κ_q = ln(q)·m_e/3 = {:.6f} MeV".format(KAPPA_Q))
    print("-" * 120)
    hdr2 = (f"{'Decay':>14} │ {'Q_exp':>8} │ {'Q_lag':>8} {'err':>7} │ "
            f"{'Q_log':>8} {'err':>7} │ {'Q_dir':>8} {'err':>7} │ "
            f"{'Q_fq':>8} {'err':>7} │")
    print(hdr2)
    print("-" * len(hdr2))

    errs_lag, errs_log, errs_dir, errs_fq = [], [], [], []
    for z, n, decay, q_exp in BENCHMARKS:
        L_rel, L_log = compute_lagrangian(z, n)
        D_full = compute_dirac(z, n)
        ql = abs(L_rel) * KAPPA_Q
        qlog = abs(L_log) * KAPPA_Q
        qd = abs(D_full) * KAPPA_Q
        qfq = compute_from_q(z, n)
        el = (ql - q_exp) / q_exp * 100
        elog = (qlog - q_exp) / q_exp * 100
        ed = (qd - q_exp) / q_exp * 100
        efq = (qfq - q_exp) / q_exp * 100
        errs_lag.append(abs(el))
        errs_log.append(abs(elog))
        errs_dir.append(abs(ed))
        errs_fq.append(abs(efq))
        print(f"  {decay:>14} │ {q_exp:>8.5f} │ {ql:>8.5f} {el:>+6.1f}% │ "
              f"{qlog:>8.5f} {elog:>+6.1f}% │ {qd:>8.5f} {ed:>+6.1f}% │ "
              f"{qfq:>8.5f} {efq:>+6.1f}% │")

    print()
    print(f"  MAE:  Q_lag = {sum(errs_lag)/len(errs_lag):.1f}%  "
          f"Q_log = {sum(errs_log)/len(errs_log):.1f}%  "
          f"Q_dir = {sum(errs_dir)/len(errs_dir):.1f}%  "
          f"Q_fq = {sum(errs_fq)/len(errs_fq):.1f}%")

    # ── Table: calibrated from ³H (1-parameter fit) ──
    print()
    print("TABLE 3: CALIBRATED FROM ³H (1-parameter fit)")
    print("-" * 120)

    L_3h_rel, L_3h_log = compute_lagrangian(1, 2)
    D_3h = compute_dirac(1, 2)

    k_lag = 0.01861 / abs(L_3h_rel) if abs(L_3h_rel) > 1e-30 else KAPPA
    k_log = 0.01861 / abs(L_3h_log) if abs(L_3h_log) > 1e-30 else KAPPA
    k_dir = 0.01861 / abs(D_3h) if abs(D_3h) > 1e-30 else KAPPA

    print(f"  Calibrated energy scales (from Q_exp(³H) = 0.01861 MeV):")
    print(f"    κ_lag = Q_exp / |L_rel(³H)| = {k_lag:.6f} MeV  (cf. κ = {KAPPA:.6f})")
    print(f"    κ_log = Q_exp / |L_log(³H)| = {k_log:.6f} MeV")
    print(f"    κ_dir = Q_exp / |D(³H)|     = {k_dir:.6f} MeV  (cf. κ_q = {KAPPA_Q:.6f})")
    print()

    hdr3 = (f"{'Decay':>14} │ {'Q_exp':>8} │ {'Q_lag':>8} {'err':>7} │ "
            f"{'Q_log':>8} {'err':>7} │ {'Q_dir':>8} {'err':>7} │")
    print(hdr3)
    print("-" * len(hdr3))

    errs_cl, errs_clg, errs_cd = [], [], []
    for z, n, decay, q_exp in BENCHMARKS:
        L_rel, L_log = compute_lagrangian(z, n)
        D_full = compute_dirac(z, n)
        ql = abs(L_rel) * k_lag
        qlog = abs(L_log) * k_log
        qd = abs(D_full) * k_dir
        el = (ql - q_exp) / q_exp * 100
        elog = (qlog - q_exp) / q_exp * 100
        ed = (qd - q_exp) / q_exp * 100
        errs_cl.append(abs(el))
        errs_clg.append(abs(elog))
        errs_cd.append(abs(ed))
        print(f"  {decay:>14} │ {q_exp:>8.5f} │ {ql:>8.5f} {el:>+6.1f}% │ "
              f"{qlog:>8.5f} {elog:>+6.1f}% │ {qd:>8.5f} {ed:>+6.1f}% │")

    print()
    print(f"  Calibrated MAE:  Q_lag = {sum(errs_cl)/len(errs_cl):.1f}%  "
          f"Q_log = {sum(errs_clg)/len(errs_clg):.1f}%  "
          f"Q_dir = {sum(errs_cd)/len(errs_cd):.1f}%")

    # ── Note on protium ──
    print()
    print("NOTE ON PROTIUM (¹H, Z=1, N=0)")
    print("=" * 60)
    print("  Protium has A=1 → 0 generators in the transfer matrix chain.")
    print("  It CANNOT undergo β⁻ decay (Q = m_p + m_e − m_n < 0).")
    print("  There is no β-decay Q-value for protium.")
    print()
    print("  The protium Hecke NF (from protium-witness.py) gives the")
    print("  atom FORMATION amplitude at the quark level:")
    print("    net(protium) = 1.4086")
    print("    Markov trace = 0.0995")
    print("  These describe the bound-state structure, not a decay.")
    print()

    # ── Summary ──
    print("SUMMARY")
    print("=" * 80)
    print("  Best uncalibrated method for ³H:")
    D_full_3h = compute_dirac(1, 2)
    qd_kq = abs(D_full_3h) * KAPPA_Q
    print(f"    Q_dirac(κ_q) = {qd_kq:.5f} MeV  "
          f"(Q_exp = 0.01861, err = {(qd_kq-0.01861)/0.01861*100:+.1f}%)")
    print()
    print("  Best calibrated method (1-param from ³H):")
    print(f"    Q_log(κ_log):  MAE = {sum(errs_clg)/len(errs_clg):.1f}% "
          f"across all benchmarks")
    print(f"    Q_lag(κ_lag):  MAE = {sum(errs_cl)/len(errs_cl):.1f}%")
    print(f"    Q_dir(κ_dir):  MAE = {sum(errs_cd)/len(errs_cd):.1f}%")
