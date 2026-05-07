#!/usr/bin/env python3
"""
Full Borromean transition for beta decay Q-values.

The complete sequence at the converting generator:

  1. UNDO Borromean rings — one per parent shell triplet.
     Each shell groups nucleons in triplets bound by Borromean
     rings. Undoing releases them as FREE degree-k nucleons.

  2. SYMMETRIZE free nucleons via Young symmetrizer P_n(q²).
     The freed nucleons are identical fermions — average over
     their orderings weighted by the Poincaré polynomial of S_n.
     This is the step that breaks conjugation invariance.

  3. INTERTWINE — apply the torus knot operator T_{r,s} for
     the transition (T_{3,5} weak vertex for beta decay,
     composed with the shell's binding knot).

  4. EMIT particles — the electron (T_{2,3} trefoil) and
     neutrino (unknot) are cycled out of the interaction.

  5. REDO Borromean rings — one per daughter shell triplet.
     Re-bind the nucleons into Borromean-linked triplets
     in the daughter configuration.

The key insight: step 2 (symmetrization) means the transition
amplitude is NOT just a conjugation (which would be trace-invariant).
The Young symmetrizer projects onto specific irreps between the
un-ring and re-ring, giving non-trivial corrections.

Usage:
    python3 borromean-full-transition.py
"""

import math
from q_parameter import Q as q, Q_INV as qi, E_CROSS
from experimental_constants import *

HA = q - qi                        # Hecke amplitude q - q⁻¹
Z_m = 1.0 / (q**0.5 + qi**0.5)
kappa = M_E_MEV / 3  # = E_CROSS * M_E_MEV / (3 * E_CROSS), simplified

# ══════════════════════════════════════════════════════════════
# §1  H₃(q) REPRESENTATIONS
# ══════════════════════════════════════════════════════════════

def sigma_std(i):
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

def eval_sign(word):
    r = 1.0
    for _, s in word:
        r *= (-qi) if s > 0 else (-q)
    return r


# ══════════════════════════════════════════════════════════════
# §2  TORUS KNOTS AND BORROMEAN OPERATORS
# ══════════════════════════════════════════════════════════════

def torus_word(r, s):
    if r == 2: return [(0, 1)] * s
    elif r == 3:
        w = []
        for _ in range(s):
            w += [(0, 1), (1, 1)]
        return w
    raise ValueError(f"Unsupported torus knot parameter r={r}; expected 2 or 3")

def torus_inv(r, s):
    return [(g, -sgn) for g, sgn in reversed(torus_word(r, s))]

KNOTS = {
    "T23": (2, 3), "T25": (2, 5), "T27": (2, 7),
    "T35": (3, 5), "T29": (2, 9), "T34": (3, 4),
}

# 3 half-Borromean color tubes
H_OPS = [
    [(0,-1),(1,1),(0,1),(1,-1)],    # h₀₁
    [(1,-1),(0,1),(1,1),(0,-1)],    # h₁₂
    [(0,-1),(1,-1),(0,1),(1,1)],    # h₀₂
]
H_INV = [[(g, -s) for g, s in reversed(h)] for h in H_OPS]


# ══════════════════════════════════════════════════════════════
# §3  YOUNG SYMMETRIZER (Poincaré normalization)
# ══════════════════════════════════════════════════════════════

# For n free nucleons, the Young symmetrizer projects onto
# the symmetric representation. The Poincaré polynomial P_n(q²)
# normalizes the projection.
#
# The symmetrized operator: instead of bare M, use
#   M_sym = Σ_{w∈S_n} q^{2l(w)} ρ(w) M ρ(w⁻¹) / P_n(q²)
#
# For the TRACE, this gives:
#   tr(M_sym) = tr(M)  (trace is already symmetric)
#
# BUT for the IRREP-SPECIFIC traces:
#   tr_λ(M_sym) = δ_{λ,sym} × tr_sym(M)  (projects onto symmetric irrep)
#
# The symmetrization CHANGES the irrep mix:
#   Before: tr_M = (d_sym·χ_sym + d_std·χ_std + d_alt·χ_alt) / D
#   After:  tr_M_sym = χ_sym  (only symmetric survives)
#
# For the Q-value, the symmetrized transition evaluates the
# crossing change using the SYMMETRIC EIGENVALUE q (not z).

def poincare_poly(n, t):
    """P_n(t) = [n]_t! = prod_{k=1}^n (1 + t + ... + t^{k-1})."""
    result = 1.0
    for k in range(1, n + 1):
        result *= sum(t**j for j in range(k))
    return result


# ══════════════════════════════════════════════════════════════
# §4  FULL TRANSITION AMPLITUDE
# ══════════════════════════════════════════════════════════════

def full_transition_ratio(n_shell_knot, p_shell_knot, n_free):
    """Compute the 3-color-averaged transition ratio for the full sequence.

    n_shell_knot: name of parent neutron shell knot (e.g. "T29")
    p_shell_knot: name of daughter proton shell knot (e.g. "T35")
    n_free: number of free nucleons after un-ringing parent shell

    The sequence for each color tube k:
      1. Undo parent Borromean: h_k⁻¹
      2. Undo parent shell knot: T_n⁻¹
      3. Symmetrize free nucleons: project onto symmetric irrep
         → evaluates subsequent operators at eigenvalue q (not z)
      4. Apply intertwining (T_{3,5} weak vertex)
      5. Redo daughter shell knot: T_p
      6. Redo daughter Borromean: h_k

    Since symmetrization projects onto the symmetric irrep,
    the effective operator after step 3 uses eigenvalue q.
    Steps 1-2 use the standard rep (mixed irreps).
    Steps 4-6 use the symmetric eigenvalue q.

    The ratio is:
      R = avg_k[ tr_std(h_k⁻¹ · T_n⁻¹) × χ_sym(T_{3,5}) × χ_sym(T_p · h_k) ]
          / [ tr_std(identity) × χ_sym(T_{3,5}) ]

    Simplifying: the T_{3,5} cancels in the ratio. What matters is:
      R = avg_k[ tr_std(h_k⁻¹ · T_n⁻¹) × eval_triv(T_p · h_k) ]
          / [ 2 × 1 ]  (tr_std(I) = 2, eval_triv(I) = 1)
    """
    nr, ns = KNOTS[n_shell_knot]
    pr, ps = KNOTS[p_shell_knot]

    # T_{3,5} weak vertex
    T35 = torus_word(3, 5)

    traces = []
    for k in range(3):
        h = H_OPS[k]
        h_inv = H_INV[k]

        # UNDO side: h_k⁻¹ · T_n⁻¹ (in standard rep, mixed irreps)
        undo_word = h_inv + torus_inv(nr, ns)
        undo_tr = tr(eval_word(undo_word))

        # SYMMETRIZE: projects onto symmetric irrep
        # After this, everything evaluates at eigenvalue q
        # So the REDO side uses trivial (symmetric) rep evaluation

        # INTERTWINE: T_{3,5} in symmetric rep = q^{crossings}
        T35_sym = eval_triv(T35)

        # REDO side: T_p · h_k (in symmetric rep = trivial rep)
        redo_word = torus_word(pr, ps) + h
        redo_sym = eval_triv(redo_word)

        # Full amplitude = undo_std × T35_sym × redo_sym
        amp = undo_tr * T35_sym * redo_sym
        traces.append(amp)

    avg = sum(traces) / 3

    # Bare: no dressing, just T_{3,5}
    # In the mixed (standard) rep for undo, symmetric for redo:
    bare = 2.0 * eval_triv(T35)  # tr_std(I)=2, eval_triv(I)=1

    return avg / bare if abs(bare) > 1e-10 else 1.0, traces


# ══════════════════════════════════════════════════════════════
# §5  SHELL STRUCTURE
# ══════════════════════════════════════════════════════════════

MAGIC = [2, 8, 20, 28, 50, 82, 126]
NEXT_SHELL_SIZE = 58  # 184 - 126, predicted next magic number gap
SHELL_KNOT_MAP = {1: "T23", 2: "T25", 3: "T27", 4: "T35", 5: "T29", 6: "T34", 7: "T29"}

def get_shell(X):
    prev = 0
    for i, m in enumerate(MAGIC):
        if X <= m:
            return i + 1, X - prev, m - prev, (X == m)
        prev = m
    return len(MAGIC) + 1, X - MAGIC[-1], NEXT_SHELL_SIZE, False


# ══════════════════════════════════════════════════════════════
# §6  TRANSFER MATRIX Q-VALUE
# ══════════════════════════════════════════════════════════════

def crossing_coeffs(ti, tj):
    if ti == 'p' and tj == 'p': return 1.0, 0.0
    elif ti == 'n' and tj == 'n': return 1.0, -HA
    else: return 1.0, -HA / 2

def T_mat(c, d):
    return [[c * HA + d, c], [c, d]]

def mat_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def gen_vol(types, i):
    A = len(types)
    M = [[1, 0], [0, 1]]
    for j in range(i + 1, A):
        c, d = crossing_coeffs(types[i], types[j])
        M = mat_mul(M, T_mat(c, d))
    return Z_m * M[0][0] + M[1][0]


# ══════════════════════════════════════════════════════════════
# §7  COMPUTE ALL NUCLEI
# ══════════════════════════════════════════════════════════════

nuclei = [
    (1,   2,   "3H",    Q_TRITIUM_MEV),
    (6,   8,   "14C",   Q_C14_MEV),
    (27,  33,  "60Co",  Q_CO60_MEV),
    (38,  52,  "90Sr",  Q_SR90_MEV),
    (55,  82,  "137Cs", Q_CS137_MEV),
    (83,  127, "210Bi", Q_BI210_MEV),
]

print("=" * 110)
print("FULL BORROMEAN TRANSITION: UNBIND -> SYMMETRIZE -> INTERTWINE -> REBIND")
print()
print("  1. Undo Borromean h_k^-1 + parent shell T_n^-1  [standard rep]")
print("  2. Young symmetrize freed nucleons              [projects to sym irrep]")
print("  3. Apply T_{3,5} weak vertex                    [symmetric eigenvalue q]")
print("  4. Redo daughter shell T_p + Borromean h_k       [symmetric eigenvalue q]")
print("  Average over 3 color tubes")
print("=" * 110)
print()

# Show the ratio matrix
print("Transition ratios R(n_knot -> p_knot) with symmetrization:")
print()
knot_names = list(KNOTS.keys())
header = "  par\\dau"
for dn in knot_names:
    header += f"  {dn:>8}"
print(header)
print("  " + "-" * (9 + 10 * len(knot_names)))

ratio_table = {}
for nk in knot_names:
    row = f"  {nk:>7}"
    for pk in knot_names:
        R, _ = full_transition_ratio(nk, pk, 3)
        ratio_table[(nk, pk)] = R
        row += f"  {R:>+8.4f}"
    print(row)

print()
print("Key: off-diagonal entries show cross-shell corrections.")
print("Diagonal entries show SAME-shell correction (no longer = 1!).")
print()

# Show individual tube traces for a few transitions
for nk, pk in [("T23", "T23"), ("T29", "T29"), ("T29", "T35"), ("T34", "T34"), ("T34", "T29")]:
    R, tubes = full_transition_ratio(nk, pk, 3)
    print(f"  {nk}->{pk}: tubes=[{tubes[0]:+.4f}, {tubes[1]:+.4f}, {tubes[2]:+.4f}], avg R={R:+.4f}")

print()

# ── Q-VALUES ──
print("=" * 110)
print("Q-VALUE TABLE: PREDICTED vs OBSERVED")
print("=" * 110)
print()

print(f"  {'Nuc':>6} | {'n_knot':>6} {'p_knot':>6} | {'R':>8} |"
      f" {'Q_bare':>8} {'Q_qwt':>8} {'Q_full':>8} {'Q_exp':>8} | {'err_q':>7} {'err_f':>7}")
print("  " + "-" * 100)

errors_q = []
errors_f = []
for Z, N, name, Q_exp in nuclei:
    par = ['p'] * Z + ['n'] * N
    dau = ['p'] * (Z + 1) + ['n'] * (N - 1)
    A = Z + N

    # Decompose into unbind/rebind
    ln_u = ln_r = ln_unc = 0.0
    for i in range(A - 1):
        Vp = gen_vol(par, i)
        Vd = gen_vol(dau, i)
        if abs(Vp) < 1e-30 or abs(Vd) < 1e-30:
            continue
        lr = math.log(abs(Vd)) - math.log(abs(Vp))
        changed = [(par[i]+par[j], dau[i]+dau[j])
                    for j in range(i+1, A)
                    if par[i]+par[j] != dau[i]+dau[j]]
        if not changed:
            ln_unc += lr
        else:
            nu = sum(1 for pp, _ in changed if pp == 'nn')
            nr = sum(1 for _, dp in changed if dp == 'pp')
            t = nu + nr
            if t == 0:
                ln_unc += lr
            elif nr == 0:
                ln_u += lr
            elif nu == 0:
                ln_r += lr
            else:
                ln_u += lr * nu / t
                ln_r += lr * nr / t

    # Shell knots
    n_sh = get_shell(N)[0]
    p_sh = get_shell(Z + 1)[0]
    nk = SHELL_KNOT_MAP.get(n_sh, "T29")
    pk = SHELL_KNOT_MAP.get(p_sh, "T29")

    R = ratio_table.get((nk, pk), 1.0)

    Q_bare = abs(ln_u + ln_r + ln_unc) * kappa
    ln_qwt = q * ln_u + qi * ln_r + ln_unc
    Q_qwt = abs(ln_qwt) * kappa
    Q_full = abs(R) * Q_qwt

    eq = (Q_qwt - Q_exp) / Q_exp * 100
    ef = (Q_full - Q_exp) / Q_exp * 100
    errors_q.append(eq)
    errors_f.append(ef)

    mq = "<" if abs(eq) < 1 else ("." if abs(eq) < 5 else " ")
    mf = "<" if abs(ef) < 1 else ("." if abs(ef) < 5 else " ")

    print(f"  {name:>6} | {nk:>6} {pk:>6} | {R:>+8.4f} |"
          f" {Q_bare:>8.5f} {Q_qwt:>8.5f} {Q_full:>8.5f} {Q_exp:>8.5f} | {eq:>+6.1f}%{mq} {ef:>+6.1f}%{mf}")

print()
mae_q = sum(abs(e) for e in errors_q) / len(errors_q)
mae_f = sum(abs(e) for e in errors_f) / len(errors_f)
rms_f = math.sqrt(sum(e**2 for e in errors_f) / len(errors_f))
print(f"  q-weighted only:  MAE = {mae_q:.1f}%")
print(f"  + Borromean full: MAE = {mae_f:.1f}%, RMS = {rms_f:.1f}%")
