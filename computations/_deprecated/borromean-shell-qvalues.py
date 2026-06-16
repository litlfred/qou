#!/usr/bin/env python3
"""
Q-values with Borromean volume and doubly-magic torus operators.

Key insight from the paper:
  - 6He has Z=2 (magic proton shell closure)
  - The proton shell closure means a T_{2,3} torus knot binds the 1s shell
  - Additionally, the 4He core is DOUBLY MAGIC (Z=2, N=2)
  - Doubly-magic nuclei have TWO torus operators (one per nucleon type)
  - The Borromean link Vol = 7.3277 enters for halo nuclei

For 6He -> 6Li:
  - Parent 6He: Z=2 (magic, 1s closed), N=4 (4 in 1p shell)
  - 4He core is doubly magic → both Z and N shells closed
  - Two extra halo neutrons Borromean-linked to the core
  - Decay breaks the Z=2 magic closure

The Borromean volume contribution:
  Vol(Borromean) = 7.3277
  Borromean binding ≈ Vol(B_3) / hbar_q^2 (in mass units)

Usage:
    cd computations && python3 borromean-shell-qvalues.py
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
E_cross = 0.5 * h
mu_0 = m_e / (3 * E_cross)

# Borromean rings volume (from SnapPy / building-block-knots.md)
VOL_BORROMEAN = 7.327724753
VOL_FIGURE_EIGHT = 2.029883212819307

print(f"q        = {q:.10f}")
print(f"h        = {h:.10f}")
print(f"hbar_q   = {HBAR_Q:.10f}")
print(f"hbar_q^2 = {HBAR_Q**2:.10f}")
print(f"E_cross  = {E_cross:.10f}")
print(f"mu_0     = {mu_0:.6f}")
print(f"z        = {z:.10f}")
print(f"ln(q)    = {LN_Q:.10f}")

# ══════════════════════════════════════════════════════════════════
#  BORROMEAN BINDING ENERGY
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  BORROMEAN BINDING ENERGY SCALES")
print("=" * 72)

# The mass mechanism: m = Vol / hbar_q^2 (in units where mu_0 = 1)
# Vol(4_1) / hbar_q^2 = m_mu / m_e (by definition of q)
borromean_mass_ratio = VOL_BORROMEAN / HBAR_Q**2
figure_eight_mass_ratio = VOL_FIGURE_EIGHT / HBAR_Q**2

print(f"\n  Vol(Borromean) = {VOL_BORROMEAN:.6f}")
print(f"  Vol(4_1)       = {VOL_FIGURE_EIGHT:.6f}")
print(f"  Ratio Vol(B)/Vol(4_1) = {VOL_BORROMEAN / VOL_FIGURE_EIGHT:.6f}")
print(f"\n  Vol(B) / hbar_q^2 = {borromean_mass_ratio:.4f} (mass ratio)")
print(f"  Vol(4_1) / hbar_q^2 = {figure_eight_mass_ratio:.4f} = m_mu/m_e (by construction)")

# Borromean binding in MeV:
# The crossing energy scale is E_cross = h/2
# The Borromean volume gives a binding energy:
#   E_borromean = Vol(B) * E_cross / hbar_q^2 * m_e ... various formulas

# Let's try the direct mass formula: E = Vol / hbar_q^2 * m_e
E_borromean_direct = borromean_mass_ratio * m_e
print(f"\n  E_borromean (direct) = Vol(B)/hbar_q^2 * m_e = {E_borromean_direct:.4f} MeV")
print(f"  6He Q_exp = 3.508 MeV")
print(f"  Ratio E_borromean/Q_exp = {E_borromean_direct / 3.508:.4f}")

# Borromean binding per nucleon
E_borr_per_nucleon = E_borromean_direct / 3  # 3 components in Borromean link
print(f"  E_borromean per component = {E_borr_per_nucleon:.4f} MeV")

# Log_q of Borromean volume
log_q_borr = log_q(VOL_BORROMEAN)
print(f"  log_q(Vol(B)) = {log_q_borr:.4f}")

# The Borromean link has 6 crossings → 6 * E_cross
E_borr_crossing = 6 * E_cross * m_e
print(f"  6 crossings * E_cross * m_e = {E_borr_crossing:.4f} MeV")

# Milnor invariant mu_bar(123) = 1 for Borromean
# Triple linking number contribution
print(f"\n  Milnor triple linking mu_bar(123) = 1")
print(f"  This is the 3-body correlation not captured by pairwise crossings")


# ══════════════════════════════════════════════════════════════════
#  TORUS KNOT TRACES (reuse from shell-knot-qvalues)
# ══════════════════════════════════════════════════════════════════

def torus_knot_markov_trace(n):
    """Markov trace of T_{2,n} = sigma^n in H_2(q)."""
    a, b = 1.0, 0.0
    c, d = 0.0, 1.0
    for _ in range(n):
        na = a * h + c
        nb = b * h + d
        nc = a
        nd = b
        a, b, c, d = na, nb, nc, nd
    return z * a + d


def bare_skein_log(Z, N):
    """Log of bare Skein polynomial for naive ordering."""
    A = Z + N
    ordering = [1] * Z + [0] * N
    log_P = 0.0
    for gen in range(A - 1):
        a, b = 0.0, 1.0
        for j in range(gen + 1, A):
            ti, tj = ordering[gen], ordering[j]
            if ti == 1 and tj == 1:
                d_val = 0.0
            elif ti == 0 and tj == 0:
                d_val = -h
            else:
                d_val = -h / 2
            new_a = a * h + a * d_val + b
            new_b = a + b * d_val
            a, b = new_a, new_b
        V = z * a + b
        if abs(V) < 1e-300:
            return float('nan')
        log_P += math.log(abs(V))
    return log_P


MAGIC = [0, 2, 8, 20, 28, 50, 82, 126]


def m_leq(X):
    return max(m for m in MAGIC if m <= X)


def m_lt(X):
    return max(m for m in MAGIC if m < X)


def n_out(X):
    return X - m_leq(X)


def n_shell(X):
    return m_leq(X) - m_lt(X) if m_leq(X) > 0 else 2


# ══════════════════════════════════════════════════════════════════
#  ENHANCED Q-VALUE WITH BORROMEAN + DOUBLY-MAGIC TORUS
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  ENHANCED Q-VALUE ALGORITHM")
print("=" * 72)
print("  Additions to shell-construction algorithm:")
print("  (a) Doubly-magic nuclei get TWO torus operators")
print("  (b) Borromean halo nuclei get Vol(B_3) correction")
print("  (c) Weak vertex gated by receptivity")


def is_doubly_magic(Z, N):
    return Z in MAGIC and Z > 0 and N in MAGIC and N > 0


def count_core_nucleons(Z, N):
    """Count nucleons in the doubly-magic core."""
    z_core = m_leq(Z)
    n_core = m_leq(N)
    if z_core > 0 and n_core > 0:
        return z_core + n_core
    return 0


def is_halo(Z, N):
    """Check if nucleus is a genuine Borromean halo.

    True halos: light nuclei with a small doubly-magic core + few
    loosely bound nucleons. Known halos: 6He, 8He, 11Li, 11Be.
    NOT halos: 14C, 60Ni, 40Ca (these are normal shell-filling nuclei).

    Criterion: the doubly-magic core is 4He (Z=2, N=2) and extra
    nucleons are <= 4, with A <= 12.
    """
    z_core = m_leq(Z)
    n_core = m_leq(N)
    A = Z + N
    extra = A - (z_core + n_core)
    # Only 4He core halos for now (the Borromean halo nuclei)
    return (z_core == 2 and n_core == 2 and extra <= 4 and extra > 0 and A <= 12)


def compute_Q_enhanced(Z, N, Q_exp=None, verbose=True):
    """Enhanced Q-value with Borromean and doubly-magic corrections."""
    A = Z + N

    # Magic status
    par_dm = is_doubly_magic(Z, N)
    dau_dm = is_doubly_magic(Z + 1, N - 1)
    par_halo = is_halo(Z, N)
    dau_halo = is_halo(Z + 1, N - 1)

    # Shell info
    par_z_magic = Z in MAGIC and Z > 0
    par_n_magic = N in MAGIC and N > 0
    dau_z_magic = (Z + 1) in MAGIC and (Z + 1) > 0
    dau_n_magic = (N - 1) in MAGIC and (N - 1) > 0

    if verbose:
        print(f"\n{'━' * 72}")
        print(f"  Z={Z}, N={N} (A={A}) -> Z={Z+1}, N={N-1}")
        print(f"  Parent:   Z-magic={par_z_magic}, N-magic={par_n_magic}, doubly={par_dm}, halo={par_halo}")
        print(f"  Daughter: Z-magic={dau_z_magic}, N-magic={dau_n_magic}, doubly={dau_dm}, halo={dau_halo}")

    # Step 3: Bare Skein polynomial ratio
    log_P_par = bare_skein_log(Z, N)
    log_P_dau = bare_skein_log(Z + 1, N - 1)
    R_bare = (log_P_dau - log_P_par) / LN_Q

    if verbose:
        print(f"\n  R_bare = {R_bare:+.4f}")

    # Step 4: Outer shell correction (torus knot traces)
    def get_tau(X, is_magic):
        if is_magic:
            return torus_knot_markov_trace(n_shell(X))
        elif n_out(X) > 0:
            return torus_knot_markov_trace(n_out(X))
        else:
            return 1.0

    tau_pp = get_tau(Z, par_z_magic)
    tau_pn = get_tau(N, par_n_magic)
    tau_dp = get_tau(Z + 1, dau_z_magic)
    tau_dn = get_tau(N - 1, dau_n_magic)

    Delta_p = log_q(abs(tau_dp)) - log_q(abs(tau_pp))
    Delta_n = log_q(abs(tau_dn)) - log_q(abs(tau_pn))
    Delta_shell = Delta_p + Delta_n

    if verbose:
        print(f"  Delta_p = {Delta_p:+.4f} (tau: {tau_pp:.4f} -> {tau_dp:.4f})")
        print(f"  Delta_n = {Delta_n:+.4f} (tau: {tau_pn:.4f} -> {tau_dn:.4f})")
        print(f"  Delta_shell = {Delta_shell:+.4f}")

    # Step 4b: Doubly-magic correction
    # If parent or daughter is doubly-magic, the SECOND torus operator
    # contributes an additional shell correction
    Delta_dm = 0.0
    if par_dm and not dau_dm:
        # Parent is doubly magic, daughter is not
        # The double closure gives extra binding that is LOST
        # Both shells close simultaneously → product of torus knot traces
        z_shell = n_shell(Z)
        n_shell_val = n_shell(N)
        tau_z = torus_knot_markov_trace(z_shell)
        tau_n = torus_knot_markov_trace(n_shell_val)
        Delta_dm = -log_q(abs(tau_z * tau_n))
        if verbose:
            print(f"  DOUBLY-MAGIC parent: shells {z_shell}+{n_shell_val}")
            print(f"    tau_z * tau_n = {tau_z:.4f} * {tau_n:.4f} = {tau_z*tau_n:.4f}")
            print(f"    Delta_dm = {Delta_dm:+.4f} (lost double closure)")
    elif dau_dm and not par_dm:
        # Daughter is doubly magic, parent is not
        # Double closure is GAINED
        z_shell = n_shell(Z + 1)
        n_shell_val = n_shell(N - 1)
        tau_z = torus_knot_markov_trace(z_shell)
        tau_n = torus_knot_markov_trace(n_shell_val)
        Delta_dm = +log_q(abs(tau_z * tau_n))
        if verbose:
            print(f"  DOUBLY-MAGIC daughter: shells {z_shell}+{n_shell_val}")
            print(f"    tau_z * tau_n = {tau_z:.4f} * {tau_n:.4f} = {tau_z*tau_n:.4f}")
            print(f"    Delta_dm = {Delta_dm:+.4f} (gained double closure)")

    # Step 4c: Borromean correction for halo nuclei
    # The Borromean link (3 components, 6 crossings, Vol = 7.3277)
    # contributes through BOTH crossing energy AND volume.
    # For halo nuclei with a 4He core, the halo neutrons are
    # Borromean-linked. The binding comes from:
    #   (a) 6 crossings at E_cross each
    #   (b) Volume/hbar_q^2 mass contribution
    #   (c) Milnor triple linking (3-body correlation)
    #
    # The Q-value gets the DIFFERENCE in Borromean binding.
    # If parent is halo and daughter is not: binding RELEASED.
    # If both are halo: partial cancellation.
    Delta_borr = 0.0
    borr_desc = ''
    if par_halo != dau_halo:
        # Borromean structure changes
        # Use log_q(Vol(B_3)) as the correction magnitude
        sign = +1 if par_halo else -1
        Delta_borr = sign * log_q(VOL_BORROMEAN)
        borr_desc = f"{'released' if par_halo else 'gained'}"
        if verbose:
            print(f"  HALO {'parent' if par_halo else 'daughter'}: Borromean binding {borr_desc}")
            print(f"    log_q(Vol(B_3)) = {log_q(VOL_BORROMEAN):+.4f}")
            print(f"    Delta_borr = {Delta_borr:+.4f}")
    elif par_halo and dau_halo:
        # Both halo — partial cancellation depending on structure change
        # Parent halo neutrons: n_extra_par = N - m_leq(N)
        # Daughter halo: configuration changes (one n -> p)
        n_halo_par = (Z + N) - count_core_nucleons(Z, N)
        n_halo_dau = (Z + 1 + N - 1) - count_core_nucleons(Z + 1, N - 1)

        # The Borromean structure persists but the linking changes
        # because the nucleon type changes (n -> p breaks one link)
        # Contribution: proportional to halo change
        if n_halo_par != n_halo_dau:
            Delta_borr = (n_halo_dau - n_halo_par) / 3.0 * log_q(VOL_BORROMEAN)
            borr_desc = f"halo change {n_halo_par}->{n_halo_dau}"
        else:
            borr_desc = 'both halo, cancels'
        if verbose:
            print(f"  Both parent and daughter are halo")
            print(f"    Halo nucleons: {n_halo_par} -> {n_halo_dau}")
            print(f"    Delta_borr = {Delta_borr:+.4f} ({borr_desc})")

    # Step 5: Weak vertex (receptivity-gated)
    WEAK_KNOTS = [
        (10, -3.370, 'T_{3,5}'),
        (9, log_q(torus_knot_markov_trace(9)), 'T_{2,9}'),
        (7, log_q(torus_knot_markov_trace(7)), 'T_{2,7}'),
        (5, log_q(torus_knot_markov_trace(5)), 'T_{2,5}'),
        (3, log_q(torus_knot_markov_trace(3)), 'T_{2,3}'),
    ]

    Delta_weak = 0.0
    weak_name = 'none'
    for n_cross, delta, name_k in WEAK_KNOTS:
        if A - 1 >= n_cross:
            Delta_weak = delta
            weak_name = name_k
            break

    if verbose:
        print(f"  Weak vertex: {weak_name} (Delta = {Delta_weak:+.4f})")

    # Step 7: Total
    total = R_bare + Delta_shell + Delta_dm + Delta_borr + Delta_weak
    Q = abs(total) * HBAR_Q * E_cross * mu_0

    err = (Q / Q_exp - 1) * 100 if Q_exp else None

    if verbose:
        print(f"\n  TOTAL = R_bare + D_shell + D_dm + D_borr + D_weak")
        print(f"        = {R_bare:+.4f} + {Delta_shell:+.4f} + {Delta_dm:+.4f} + {Delta_borr:+.4f} + {Delta_weak:+.4f}")
        print(f"        = {total:+.4f}")
        print(f"  Q = |{total:.4f}| * {HBAR_Q:.6f} * {E_cross:.6f} * {mu_0:.6f}")
        print(f"  Q = {Q:.6f} MeV")
        if Q_exp:
            print(f"  Q_exp = {Q_exp:.6f} MeV")
            print(f"  Error = {err:+.1f}%")

    return {
        'Z': Z, 'N': N, 'A': A, 'Q': Q, 'Q_exp': Q_exp, 'err': err,
        'R_bare': R_bare, 'Delta_shell': Delta_shell,
        'Delta_dm': Delta_dm, 'Delta_borr': Delta_borr,
        'Delta_weak': Delta_weak, 'weak_knot': weak_name,
        'total': total,
        'par_dm': par_dm, 'dau_dm': dau_dm,
        'par_halo': par_halo, 'dau_halo': dau_halo,
    }


# ══════════════════════════════════════════════════════════════════
#  RUN BENCHMARKS
# ══════════════════════════════════════════════════════════════════

benchmarks = [
    (1, 2, 0.018592, '3H->3He'),
    (2, 4, 3.508, '6He->6Li'),
    (6, 8, 0.156476, '14C->14N'),
    (27, 33, 2.823, '60Co->60Ni'),
    (19, 21, 1.312, '40K->40Ca'),
    (38, 52, 0.546, '90Sr->90Y'),
    (55, 82, 0.514, '137Cs->137Ba'),
]

results = []
for Z, N, Q_exp, name in benchmarks:
    r = compute_Q_enhanced(Z, N, Q_exp)
    r['name'] = name
    results.append(r)


# ══════════════════════════════════════════════════════════════════
#  SUMMARY
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  SUMMARY TABLE")
print("=" * 72)

print(f"\n  {'Decay':>12s} | {'Q_exp':>7s} | {'Q_pred':>7s} | {'err':>7s} | {'R':>6s} | {'D_sh':>6s} | {'D_dm':>6s} | {'D_B':>6s} | {'D_wk':>6s} | {'knot':>6s}")
print(f"  {'':->95s}")
for r in results:
    print(f"  {r['name']:>12s} | {r['Q_exp']:>7.3f} | {r['Q']:>7.3f} | {r['err']:>+6.1f}% | {r['R_bare']:>+6.1f} | {r['Delta_shell']:>+6.1f} | {r['Delta_dm']:>+6.1f} | {r['Delta_borr']:>+6.1f} | {r['Delta_weak']:>+6.1f} | {r['weak_knot']:>6s}")

# MAE for receptive nuclei (A >= 14)
receptive = [r for r in results if r['A'] >= 14]
if receptive:
    mae = sum(abs(r['err']) for r in receptive) / len(receptive)
    print(f"\n  MAE (A >= 14, T_{{3,5}} receptive): {mae:.1f}%")

all_mae = sum(abs(r['err']) for r in results) / len(results)
print(f"  MAE (all): {all_mae:.1f}%")

# Witness
witness = {
    'name': 'borromean-shell-qvalues',
    'timestamp': datetime.now(timezone.utc).isoformat(),
    'q': q, 'Vol_Borromean': VOL_BORROMEAN,
    'results': [{k: v for k, v in r.items()} for r in results],
}
out = Path(__file__).with_suffix('.witness.json')
out.write_text(json.dumps(witness, indent=2, default=float))
print(f"\n  Witness: {out.name}")
