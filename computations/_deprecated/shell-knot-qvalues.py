#!/usr/bin/env python3
"""
Q-values using the full shell-construction algorithm from the paper.

The algorithm (shell-construction-rules.md) computes Q via:
  1. Bare transfer matrix Skein polynomial ratio R_bare
  2. Outer shell torus knot correction Delta_shell
  3. T_{3,5} weak vertex contribution Delta_T35
  4. Q = |R_bare + Delta_shell + Delta_T35| * hbar_q * E_cross * mu_0

Key insight: different knot operators bind different shells.
  - T_{2,3} binds 1s and 1p shells (magic 2, 8)
  - T_{2,5} binds 1d and 1f shells (magic 20, 28)
  - T_{2,7} binds 2s-2d shell (magic 50)
  - T_{2,9} + T_{3,4} bind 2f-3p (magic 82)
  - T_{2,9} + T_{3,5} bind 3d-4s (magic 126)
  - T_{3,5} is the weak vertex operator

For small nuclei (A <= 6), the torus knots are trivial because
they have fewer crossings than the knot requires. We check this.

Usage:
    cd computations && python3 shell-knot-qvalues.py
"""
import math
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q, Q_INV as qi, HA as h, HBAR_Q, LN_Q, log_q

z = 1.0 / (q**0.5 + q**(-0.5))
m_e = 0.51099895
E_cross = 0.5 * h  # crossing energy E_x = (q - q^-1)/2

print(f"q        = {q:.10f}")
print(f"h        = {h:.10f}")
print(f"z        = {z:.10f}")
print(f"hbar_q   = {HBAR_Q:.10f}")
print(f"E_cross  = {E_cross:.10f}")
print(f"ln(q)    = {LN_Q:.10f}")


# ══════════════════════════════════════════════════════════════════
#  TORUS KNOT CHEBYSHEV COEFFICIENTS
# ══════════════════════════════════════════════════════════════════

def chebyshev_coeffs(n):
    """Chebyshev crossing coefficients (c_n, d_n) for T_{2,n}.

    Recurrence: c_1 = 1, d_1 = 0
                c_{n+1} = c_n * h + c_n + d_n
                d_{n+1} = c_n
    """
    c, d = 1.0, 0.0
    for _ in range(n - 1):
        c, d = c * h + c + d, c
    return c, d


def torus_knot_markov_trace(n):
    """Markov trace of T_{2,n} = sigma^n in H_2(q).

    tr_M(sigma^n) = z * c_n + d_n (from transfer matrix power).
    Actually: T^n = [[a_n, c_n], [c_n, d_n]] and
    tr_M = z * a_n + (1-z) * d_n for the 2-strand Markov trace.

    For H_2(q): tr_M(sigma^n) = z^n (simplified Markov property).
    Actually more precisely from the transfer matrix chain:
    """
    # Direct computation via the transfer matrix chain
    # T = [[h, 1], [1, 0]] (bare crossing in Markov parameter)
    # T^n gives the chain, trace = z * T^n[0,0] + T^n[1,1]
    a, b = 1.0, 0.0  # Start with [[1, 0], [0, 1]]
    c, d = 0.0, 1.0
    for _ in range(n):
        na = a * h + c
        nb = b * h + d
        nc = a
        nd = b
        a, b, c, d = na, nb, nc, nd
    # Matrix is [[a, b], [c, d]]
    trace = z * a + d
    return trace


print("\n" + "=" * 72)
print("  TORUS KNOT CHEBYSHEV COEFFICIENTS AND MARKOV TRACES")
print("=" * 72)
print(f"  {'n':>3s} | {'c_n':>10s} | {'d_n':>10s} | {'tr_M':>12s} | {'log_q(tr)':>10s}")
print(f"  {'':->55s}")

for n in range(1, 12):
    cn, dn = chebyshev_coeffs(n)
    tr = torus_knot_markov_trace(n)
    lq = log_q(abs(tr)) if abs(tr) > 1e-15 else float('nan')
    print(f"  {n:>3d} | {cn:>10.4f} | {dn:>10.4f} | {tr:>12.6f} | {lq:>+10.4f}")


# ══════════════════════════════════════════════════════════════════
#  MAGIC NUMBER TABLE AND SHELL FUNCTIONS
# ══════════════════════════════════════════════════════════════════

MAGIC = [0, 2, 8, 20, 28, 50, 82, 126]

# Shell binding knots (from torus-knot-shell-binding.md Table iv)
SHELL_KNOTS = {
    (0, 2):   'T_{2,3}',    # 1s shell, size 2
    (2, 8):   'T_{2,3}',    # 1p shell, size 6
    (8, 20):  'T_{2,5}',    # 1d shell, size 12
    (20, 28): 'T_{2,5}+T_{3,4}',  # 1f shell, size 8
    (28, 50): 'T_{2,7}',    # 2s-2d, size 22
    (50, 82): 'T_{2,9}+T_{3,4}',  # 2f-3p, size 32
    (82, 126): 'T_{2,9}+T_{3,5}', # 3d-4s, size 44
}


def m_leq(X):
    """Largest magic number <= X."""
    return max(m for m in MAGIC if m <= X)


def m_lt(X):
    """Largest magic number strictly < X."""
    return max(m for m in MAGIC if m < X)


def n_out(X):
    """Nucleons in outermost open shell."""
    return X - m_leq(X)


def n_shell(X):
    """Size of the shell containing X."""
    return m_leq(X) - m_lt(X) if m_leq(X) > 0 else 2  # 1s shell size = 2


def shell_info(X):
    """Full shell information for nucleon count X."""
    magic = X in MAGIC and X > 0
    ml = m_leq(X)
    mlt = m_lt(X)
    nout = n_out(X)
    ns = n_shell(X)
    return {
        'X': X, 'magic': magic,
        'm_leq': ml, 'm_lt': mlt,
        'n_out': nout, 'n_shell': ns,
        'shell_range': (mlt, ml),
    }


# ══════════════════════════════════════════════════════════════════
#  BARE SKEIN POLYNOMIAL (from transfer matrix chain)
# ══════════════════════════════════════════════════════════════════

def bare_skein_polynomial(Z, N):
    """Bare Skein polynomial P(q) for naive ordering [ppp...nnn...].

    Crossing coefficients:
      pp: (c, d) = (1, 0)       → identity (trivial crossing)
      nn: (c, d) = (1, -h)      → Hecke relation T_nn = T_pp^{-1}
      mix: (c, d) = (1, -h/2)   → average crossing
    """
    A = Z + N
    ordering = [1] * Z + [0] * N  # naive: all protons first

    # Product of vertex volumes
    log_P = 0.0
    for gen in range(A - 1):
        a, b = 0.0, 1.0
        for j in range(gen + 1, A):
            ti, tj = ordering[gen], ordering[j]
            if ti == 1 and tj == 1:
                d = 0.0
            elif ti == 0 and tj == 0:
                d = -h
            else:
                d = -h / 2
            new_a = a * h + a * d + b
            new_b = a + b * d
            a, b = new_a, new_b
        V = z * a + b
        if abs(V) < 1e-300:
            return float('nan')
        log_P += math.log(abs(V))
    return log_P


# ══════════════════════════════════════════════════════════════════
#  FULL Q-VALUE ALGORITHM (shell-construction-rules.md)
# ══════════════════════════════════════════════════════════════════

def compute_Q_shell(Z, N, verbose=True):
    """Full Q-value computation following shell-construction-rules.md.

    Steps:
      0. Magic number table
      1. Outer shell occupancies
      2. Torus knot traces
      3. Bare Skein polynomial ratio
      4. Outer shell correction
      5. T_{3,5} weak vertex
      6. Inner shell dressing (cancels)
      7. Q = |R_bare + Delta_shell + Delta_T35| * hbar_q * E_cross * mu_0
    """
    A = Z + N

    # Step 0-1: Shell info for parent and daughter
    par_p = shell_info(Z)
    par_n = shell_info(N)
    dau_p = shell_info(Z + 1)
    dau_n = shell_info(N - 1)

    if verbose:
        print(f"\n  Step 0-1: Shell occupancies")
        print(f"    Parent  Z={Z}: n_out={par_p['n_out']}, n_shell={par_p['n_shell']}, magic={par_p['magic']}")
        print(f"    Parent  N={N}: n_out={par_n['n_out']}, n_shell={par_n['n_shell']}, magic={par_n['magic']}")
        print(f"    Daughter Z+1={Z+1}: n_out={dau_p['n_out']}, n_shell={dau_p['n_shell']}, magic={dau_p['magic']}")
        print(f"    Daughter N-1={N-1}: n_out={dau_n['n_out']}, n_shell={dau_n['n_shell']}, magic={dau_n['magic']}")

    # Step 2: Torus knot traces
    # For each shell occupancy, compute tr_M(T_{2,n})
    def shell_trace(info):
        if info['magic']:
            # Use full closed shell trace
            return torus_knot_markov_trace(info['n_shell'])
        elif info['n_out'] == 0:
            return 1.0  # no outer shell nucleons
        else:
            return torus_knot_markov_trace(info['n_out'])

    tau_par_p = shell_trace(par_p)
    tau_par_n = shell_trace(par_n)
    tau_dau_p = shell_trace(dau_p)
    tau_dau_n = shell_trace(dau_n)

    if verbose:
        print(f"\n  Step 2: Torus knot traces")
        print(f"    tau(par_p) = tr_M(T_{{2,{par_p['n_out'] if not par_p['magic'] else par_p['n_shell']}}}) = {tau_par_p:.6f}")
        print(f"    tau(par_n) = tr_M(T_{{2,{par_n['n_out'] if not par_n['magic'] else par_n['n_shell']}}}) = {tau_par_n:.6f}")
        print(f"    tau(dau_p) = tr_M(T_{{2,{dau_p['n_out'] if not dau_p['magic'] else dau_p['n_shell']}}}) = {tau_dau_p:.6f}")
        print(f"    tau(dau_n) = tr_M(T_{{2,{dau_n['n_out'] if not dau_n['magic'] else dau_n['n_shell']}}}) = {tau_dau_n:.6f}")

    # Step 3: Bare Skein polynomial ratio
    log_P_par = bare_skein_polynomial(Z, N)
    log_P_dau = bare_skein_polynomial(Z + 1, N - 1)
    R_bare = (log_P_dau - log_P_par) / LN_Q  # convert to log_q

    if verbose:
        print(f"\n  Step 3: Bare Skein polynomial ratio")
        print(f"    log P_par = {log_P_par:.6f}")
        print(f"    log P_dau = {log_P_dau:.6f}")
        print(f"    R_bare = log_q(P_dau/P_par) = {R_bare:.4f}")

    # Step 4: Outer shell correction
    def safe_log_q(x):
        if abs(x) < 1e-15:
            return 0.0
        return log_q(abs(x))

    Delta_p = safe_log_q(tau_dau_p) - safe_log_q(tau_par_p)
    Delta_n = safe_log_q(tau_dau_n) - safe_log_q(tau_par_n)
    Delta_shell = Delta_p + Delta_n

    if verbose:
        print(f"\n  Step 4: Outer shell correction")
        print(f"    Delta_p = log_q(tau_dau_p) - log_q(tau_par_p) = {Delta_p:+.4f}")
        print(f"    Delta_n = log_q(tau_dau_n) - log_q(tau_par_n) = {Delta_n:+.4f}")
        print(f"    Delta_shell = {Delta_shell:+.4f}")

    # Step 5: Weak vertex — GATED BY RECEPTIVITY
    # T_{3,5} needs 10 crossings → A >= 11
    # T_{2,9} needs 9 crossings → A >= 10
    # T_{2,7} needs 7 crossings → A >= 8
    # T_{2,5} needs 5 crossings → A >= 6
    # T_{2,3} needs 3 crossings → A >= 4
    # Bare: A < 4 → no torus knot, just bare crossing
    #
    # The weak vertex is the LARGEST receptive knot.
    # From the paper: T_{3,5} is the weak force knot.
    # For smaller nuclei, the decay goes through a smaller knot.

    WEAK_KNOTS = [
        (10, -3.370, 'T_{3,5}'),   # 10 crossings
        (9,  log_q(torus_knot_markov_trace(9)), 'T_{2,9}'),
        (7,  log_q(torus_knot_markov_trace(7)), 'T_{2,7}'),
        (5,  log_q(torus_knot_markov_trace(5)), 'T_{2,5}'),
        (3,  log_q(torus_knot_markov_trace(3)), 'T_{2,3}'),
    ]

    Delta_weak = 0.0
    weak_name = 'none (bare)'
    for n_cross, delta, name_k in WEAK_KNOTS:
        if A - 1 >= n_cross:
            Delta_weak = delta
            weak_name = name_k
            break

    if verbose:
        print(f"\n  Step 5: Weak vertex (receptivity-gated)")
        print(f"    A-1 = {A-1} generators")
        print(f"    Largest receptive weak knot: {weak_name}")
        print(f"    Delta_weak = {Delta_weak:.4f}")

    # Step 7: Q-value
    # mu_0 = m_e / (3 * E_cross)
    mu_0 = m_e / (3 * E_cross)
    total = R_bare + Delta_shell + Delta_weak
    Q = abs(total) * HBAR_Q * E_cross * mu_0

    if verbose:
        print(f"\n  Step 7: Q-value")
        print(f"    R_bare + Delta_shell + Delta_weak = {total:+.4f}")
        print(f"    mu_0 = m_e / (3*E_cross) = {mu_0:.6f}")
        print(f"    Q = |total| * hbar_q * E_cross * mu_0 = {Q:.6f} MeV")

    return {
        'Z': Z, 'N': N, 'A': A,
        'R_bare': R_bare,
        'Delta_shell': Delta_shell,
        'Delta_weak': Delta_weak,
        'weak_knot': weak_name,
        'total': total, 'Q': Q,
        'mu_0': mu_0,
        'par_p': par_p, 'par_n': par_n,
        'dau_p': dau_p, 'dau_n': dau_n,
    }


# ══════════════════════════════════════════════════════════════════
#  CHECK: ARE HIGHER KNOTS TRIVIAL ON SMALL NUCLEI?
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  CHECK: KNOT RECEPTIVITY BY NUCLEUS SIZE")
print("=" * 72)
print("  A nucleus is 'receptive' to knot T_{2,n} if it has")
print("  enough crossings to support the knot. For T_{2,n},")
print("  the minimum A is n+1 (need n consecutive crossings).")
print()

nuclei_check = [
    (1, 2, '3H'),
    (2, 1, '3He'),
    (2, 2, '4He'),
    (2, 4, '6He'),
    (3, 3, '6Li'),
    (6, 8, '14C'),
    (7, 7, '14N'),
    (27, 33, '60Co'),
    (28, 32, '60Ni'),
]

knots_check = [
    ('T_{2,3}', 3),
    ('T_{2,5}', 5),
    ('T_{2,7}', 7),
    ('T_{2,9}', 9),
    ('T_{3,4}', 8),
    ('T_{3,5}', 10),
]

print(f"  {'Nucleus':>8s} | {'A':>3s} | ", end='')
for name, _ in knots_check:
    print(f" {name:>8s}", end='')
print()
print(f"  {'':->70s}")

for Z, N, name in nuclei_check:
    A = Z + N
    print(f"  {name:>8s} | {A:>3d} | ", end='')
    for kname, crossings in knots_check:
        # Receptive if A-1 >= crossings (need crossings generators)
        receptive = (A - 1) >= crossings
        # Also check: is this knot relevant to the shell?
        # The shell containing Z or N determines which knot binds
        shell_p = shell_info(Z)
        shell_n = shell_info(N)
        print(f" {'  YES' if receptive else '   no':>8s}", end='')
    print()


# ══════════════════════════════════════════════════════════════════
#  COMPUTE Q-VALUES FOR BENCHMARK DECAYS
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  Q-VALUES: FULL SHELL-CONSTRUCTION ALGORITHM")
print("=" * 72)

benchmarks = [
    (1, 2, 0.018592, '3H->3He'),
    (2, 4, 3.508, '6He->6Li'),
    (6, 8, 0.156476, '14C->14N'),
    (27, 33, 2.823, '60Co->60Ni'),
    (19, 21, 1.312, '40K->40Ca'),
    (38, 52, 0.546, '90Sr->90Y'),
]

results = []
for Z, N, Q_exp, name in benchmarks:
    print(f"\n{'━' * 72}")
    print(f"  {name}: (Z={Z}, N={N}) -> (Z+1={Z+1}, N-1={N-1})")
    print(f"{'━' * 72}")

    r = compute_Q_shell(Z, N)
    r['name'] = name
    r['Q_exp'] = Q_exp
    r['err'] = (r['Q'] / Q_exp - 1) * 100

    print(f"\n  RESULT: Q_pred = {r['Q']:.6f} MeV, Q_exp = {Q_exp:.6f} MeV, Error = {r['err']:+.1f}%")
    results.append(r)


# ══════════════════════════════════════════════════════════════════
#  ALSO: Q = |sum dV| * z^2 * m_e (vertex volume formula)
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  COMPARISON: VERTEX VOLUME FORMULA")
print("=" * 72)


def find_ground_state(Z, N):
    from itertools import combinations
    A = Z + N
    best_Phi = float('inf')
    best_ord = None
    for pp in combinations(range(A), Z):
        o = [0] * A
        for p in pp:
            o[p] = 1
        Phi = 0.0
        ok = True
        for gen in range(A - 1):
            a, b = 0.0, 1.0
            for j in range(gen + 1, A):
                ti, tj = o[gen], o[j]
                if ti == 1 and tj == 1:
                    d = 0.0
                elif ti == 0 and tj == 0:
                    d = -h
                else:
                    d = -h / 2
                new_a = a * h + a * d + b
                new_b = a + b * d
                a, b = new_a, new_b
            V = z * a + b
            if abs(V) < 1e-300:
                ok = False
                break
            Phi += math.log(abs(V))
        if ok and Phi < best_Phi:
            best_Phi = Phi
            best_ord = o[:]
    return best_ord, best_Phi


def chain_V(ordering, gen):
    A = len(ordering)
    a, b = 0.0, 1.0
    for j in range(gen + 1, A):
        ti, tj = ordering[gen], ordering[j]
        if ti == 1 and tj == 1:
            d = 0.0
        elif ti == 0 and tj == 0:
            d = -h
        else:
            d = -h / 2
        new_a = a * h + a * d + b
        new_b = a + b * d
        a, b = new_a, new_b
    return z * a + b


E_gram = z**2 * m_e

for r in results:
    Z, N = r['Z'], r['N']
    A = Z + N
    Q_exp = r['Q_exp']

    if A > 20:
        print(f"  {r['name']:>12s} | A={A:>3d} (skipped, too large for exhaustive GS)")
        continue

    gs_par, _ = find_ground_state(Z, N)
    gs_dau, _ = find_ground_state(Z + 1, N - 1)

    V_par = [chain_V(gs_par, i) for i in range(A - 1)]
    V_dau = [chain_V(gs_dau, i) for i in range(A - 1)]

    sum_dV = sum(V_dau[i] - V_par[i] for i in range(A - 1))
    Q_vv = abs(sum_dV) * E_gram
    err_vv = (Q_vv / Q_exp - 1) * 100

    print(f"  {r['name']:>12s} | Q_vv={Q_vv:.6f} | Q_shell={r['Q']:.6f} | Q_exp={Q_exp:.6f} | err_vv={err_vv:+.1f}% err_shell={r['err']:+.1f}%")


# ══════════════════════════════════════════════════════════════════
#  SUMMARY
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  SUMMARY TABLE")
print("=" * 72)

print(f"\n  {'Decay':>12s} | {'Q_exp':>8s} | {'Q_shell':>8s} | {'err':>7s} | {'R_bare':>8s} | {'D_shell':>8s} | {'D_weak':>7s} | {'knot':>8s}")
print(f"  {'':->85s}")
for r in results:
    print(f"  {r['name']:>12s} | {r['Q_exp']:>8.4f} | {r['Q']:>8.4f} | {r['err']:>+6.1f}% | {r['R_bare']:>+8.2f} | {r['Delta_shell']:>+8.2f} | {r['Delta_weak']:>+7.2f} | {r['weak_knot']:>8s}")


# Witness
witness = {
    'name': 'shell-knot-qvalues',
    'timestamp': datetime.now(timezone.utc).isoformat(),
    'q': q, 'hbar_q': HBAR_Q, 'E_cross': E_cross,
    'results': [{
        'name': r['name'], 'Z': r['Z'], 'N': r['N'],
        'Q_pred': r['Q'], 'Q_exp': r['Q_exp'], 'err': r['err'],
        'R_bare': r['R_bare'], 'Delta_shell': r['Delta_shell'],
        'Delta_weak': r['Delta_weak'],
        'weak_knot': r['weak_knot'],
    } for r in results],
}
out = Path(__file__).with_suffix('.witness.json')
out.write_text(json.dumps(witness, indent=2, default=float))
print(f"\n  Witness: {out.name}")
