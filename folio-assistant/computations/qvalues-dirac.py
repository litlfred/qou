"""
Q_Dirac: categorical Dirac operator Q-value.

The Dirac operator D_∇ is FIRST ORDER — it sees the two Hecke
channels separately:

  D_∇ = q⁻¹·∇ + ℏ_q·ι_ξ∇

Eigenvalues of each Hecke generator:
  λ₊ = q    (symmetric channel)
  λ₋ = -q⁻¹ (antisymmetric channel)

The Dirac form decomposes the Q-value into symmetric and
antisymmetric contributions at each generator.  This gives:

1. **Channel separation**: Q = Q_sym + Q_alt
2. **Higher NF**: the full 2×2 matrix structure (not just trace)
3. **Jet bundle tracking**: J¹ values (V̂_i, ΔV̂_i, M_i entries)

The key difference from the Lagrangian (D²):
  - Lagrangian: Q_L ∝ |Σ ln(V̂_d/V̂_p)|    (second order, mixes channels)
  - Dirac:      Q_D ∝ |Σ D_∇(V̂)|          (first order, separates channels)

For β-decay: D_∇ acts on the transition ψ_par → ψ_dau. The Q-value
is the first-order matrix element, not the squared Lagrangian.

Crossing coefficients: CORRECT form (1, -HA) for nn, (1, 0) for pp.
"""

import math
import sys
sys.path.insert(0, '.')
from q_parameter import Q, Q_INV, HA, LN_Q, HBAR_Q
from experimental_constants import M_E_MEV

Z_MARKOV = 1.0 / (math.sqrt(Q) + 1.0 / math.sqrt(Q))  # Markov trace normalization: z_M = 1/(q^½ + q^{-½})
KAPPA = M_E_MEV / 3.0


# ═══════════════════════════════════════════════════════════════
# §1  CORRECT CROSSING COEFFICIENTS
# ═══════════════════════════════════════════════════════════════

def crossing_coeffs(ti, tj):
    """Hecke crossing coefficients T(c,d) = c·σ + d·1.

    pp → σ:              (1,  0)
    nn → σ⁻¹:            (1, −HA)
    pn/np → ½(σ + σ⁻¹): (1, −HA/2)

    All have det T = −1 (unimodular). ✓
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
# §2  GENERATOR DATA: FULL J¹ JET-BUNDLE VALUES
# ═══════════════════════════════════════════════════════════════

def gen_data(z, n):
    """Compute full jet-bundle data at each generator.

    Returns list of dicts with:
      vol:    V̂_i = z_M · M[0,0] + M[1,0]  (traced volume, degree 0)
      mat:    M_i (full 2×2 chain matrix)
      sym:    symmetric eigenvalue contribution: M[0,0] + M[1,1] = tr(M)
      alt:    antisymmetric: M[0,0] - M[1,1] = spread
      m00..m11: individual matrix entries
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
        tr_m = m[0][0] + m[1][1]
        spread = m[0][0] - m[1][1]
        result.append({
            'vol': vol,
            'mat': m,
            'tr': tr_m,         # trace = sym part
            'spread': spread,   # spread = alt part
            'm00': m[0][0], 'm01': m[0][1],
            'm10': m[1][0], 'm11': m[1][1],
        })
    return result


# ═══════════════════════════════════════════════════════════════
# §3  DIRAC DECOMPOSITION: SYM + ALT CHANNELS
# ═══════════════════════════════════════════════════════════════

def Q_dirac(z, n):
    """Categorical Dirac Q-value with sym/alt channel decomposition.

    The Dirac operator D_∇ = q⁻¹·∇ + ℏ_q·ι_ξ∇ acts on each
    generator's transfer matrix chain.

    Symmetric channel (eigenvalue q):
      Measures the TRACE change: Δtr(M_i) = tr(M_d) - tr(M_p)
      Weight: q⁻¹ (from the ∇ term in D_∇)

    Antisymmetric channel (eigenvalue -q⁻¹):
      Measures the SPREAD change: Δ(M[0,0]-M[1,1])
      Weight: ℏ_q (from the ι_ξ∇ term in D_∇)

    Full jet J¹ tracking:
      - Degree 0: V̂_i  (traced volume)
      - Degree 1: ΔV̂_i (volume change under transition)
      - Matrix:   full M_i entries (higher NF)
    """
    a = z + n
    dp = gen_data(z, n)         # parent
    dd = gen_data(z + 1, n - 1)  # daughter

    # ── Per-generator Dirac matrix elements ──
    dvols = []       # degree 0: volume differences
    d_traces = []    # symmetric: trace differences
    d_spreads = []   # antisymmetric: spread differences
    d_offdiag = []   # off-diagonal: M[0,1] differences (higher NF)
    # Relative forms (normalized by parent)
    rel_vols = []    # δ_vol = ΔV̂/V̂
    rel_traces = []  # δ_tr = Δtr/tr
    rel_spreads = [] # δ_spr = Δspr/spr
    jet_data = []    # full J¹ data

    for i in range(a - 1):
        vp = dp[i]['vol']
        vd = dd[i]['vol']
        dvol = vd - vp
        dvols.append(dvol)
        rel_vols.append(dvol / vp if abs(vp) > 1e-30 else 0.0)

        dtr = dd[i]['tr'] - dp[i]['tr']
        d_traces.append(dtr)
        rel_traces.append(dtr / dp[i]['tr'] if abs(dp[i]['tr']) > 1e-30 else 0.0)

        dspr = dd[i]['spread'] - dp[i]['spread']
        d_spreads.append(dspr)
        rel_spreads.append(dspr / dp[i]['spread'] if abs(dp[i]['spread']) > 1e-30 else 0.0)

        doff = dd[i]['m01'] - dp[i]['m01']
        d_offdiag.append(doff)

        jet_data.append({
            'gen': i,
            'vp': vp, 'vd': vd, 'dvol': dvol,
            'tr_p': dp[i]['tr'], 'tr_d': dd[i]['tr'], 'dtr': dtr,
            'spr_p': dp[i]['spread'], 'spr_d': dd[i]['spread'], 'dspr': dspr,
            'm01_p': dp[i]['m01'], 'm01_d': dd[i]['m01'], 'doff': doff,
        })

    # ── Dirac matrix elements (RELATIVE form) ──
    # D_∇ = q⁻¹·∇ + ℏ_q·ι_ξ∇
    # Symmetric channel: weight q⁻¹, measures relative trace changes
    D_sym = Q_INV * sum(rel_traces)

    # Antisymmetric channel: weight ℏ_q, measures relative spread changes
    D_alt = HBAR_Q * sum(rel_spreads)

    # Full Dirac: D = D_sym + D_alt
    D_full = D_sym + D_alt

    # Free Lagrangian for comparison (degree 0 only)
    L_free = sum(dvols)

    # Log form for comparison
    L_log = 0.0
    for i in range(a - 1):
        vp = dp[i]['vol']
        vd = dd[i]['vol']
        if abs(vp) > 1e-30 and abs(vd) > 1e-30:
            L_log += math.log(abs(vd)) - math.log(abs(vp))

    # ── Deg 1 × deg 1 interaction in Dirac channels (relative) ──
    # Symmetric × symmetric
    int_sym_sym = 0.0
    for i in range(a - 1):
        for j in range(i + 1, a - 1):
            int_sym_sym += rel_traces[i] * rel_traces[j]

    # Antisymmetric × antisymmetric
    int_alt_alt = 0.0
    for i in range(a - 1):
        for j in range(i + 1, a - 1):
            int_alt_alt += rel_spreads[i] * rel_spreads[j]

    # Symmetric × antisymmetric cross-term (both orderings i<j and j<i)
    int_sym_alt = 0.0
    for i in range(a - 1):
        for j in range(i + 1, a - 1):
            int_sym_alt += (rel_traces[i] * rel_spreads[j]
                            + rel_traces[j] * rel_spreads[i])

    return {
        # Q-values with different energy scales
        'D_sym': D_sym,
        'D_alt': D_alt,
        'D_full': D_full,
        'Q_dirac_kappa': abs(D_full) * KAPPA,
        'Q_sym_kappa': abs(D_sym) * KAPPA,
        'Q_alt_kappa': abs(D_alt) * KAPPA,
        # Lagrangian comparisons
        'L_free': L_free,
        'L_log': L_log,
        'Q_free_kappa': abs(L_free) * KAPPA,
        'Q_log_kappa': abs(L_log) * KAPPA,
        # Deg 1×1 interactions
        'int_sym_sym': int_sym_sym,
        'int_alt_alt': int_alt_alt,
        'int_sym_alt': int_sym_alt,
        # Full jet data
        'jet_data': jet_data,
        'n_gens': a - 1,
    }


# ═══════════════════════════════════════════════════════════════
# §4  HIGHER NF FROM MATRIX STRUCTURE
# ═══════════════════════════════════════════════════════════════

def higher_nf(z, n):
    """Higher normal form: full matrix invariants, not just trace.

    At each generator, the chain matrix M_i is 2×2. Its invariants:
      det(M_i) = (-1)^{chain_length}  (unimodularity)
      tr(M_i)                          (symmetric NF)
      M[0,0] - M[1,1]                 (antisymmetric NF)
      M[0,1] + M[1,0]                 (off-diagonal NF)

    The "degree 0" Q uses only V̂ = z_M·M[0,0] + M[1,0] (one scalar).
    The "higher NF" uses all four matrix invariants.
    """
    a = z + n
    dp = gen_data(z, n)
    dd = gen_data(z + 1, n - 1)

    nf_data = []
    for i in range(a - 1):
        mp = dp[i]['mat']
        md = dd[i]['mat']

        det_p = mp[0][0]*mp[1][1] - mp[0][1]*mp[1][0]
        det_d = md[0][0]*md[1][1] - md[0][1]*md[1][0]

        offdiag_p = mp[0][1] + mp[1][0]
        offdiag_d = md[0][1] + md[1][0]

        nf_data.append({
            'gen': i,
            'det_p': det_p, 'det_d': det_d,
            'tr_p': dp[i]['tr'], 'tr_d': dd[i]['tr'],
            'spr_p': dp[i]['spread'], 'spr_d': dd[i]['spread'],
            'off_p': offdiag_p, 'off_d': offdiag_d,
            'vol_p': dp[i]['vol'], 'vol_d': dd[i]['vol'],
        })

    return nf_data


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
    print("Q_DIRAC: CATEGORICAL DIRAC OPERATOR Q-VALUE")
    print("=" * 90)
    print()
    print("  D_∇ = q⁻¹·∇ + ℏ_q·ι_ξ∇")
    print(f"  q   = {Q:.10f}")
    print(f"  q⁻¹ = {Q_INV:.10f}")
    print(f"  ℏ_q = {HBAR_Q:.10f}")
    print(f"  HA  = {HA:.10f}")
    print(f"  κ   = {KAPPA:.6f} MeV")
    print()
    print("  Crossing coefficients: pp→(1,0), nn→(1,−HA), pn→(1,−HA/2)")
    print()

    # ── Table 1: Dirac vs Lagrangian vs Log ──
    print("DIRAC DECOMPOSITION: SYM + ALT CHANNELS")
    print("-" * 95)
    hdr = (f"{'Decay':>14} {'D_sym':>9} {'D_alt':>9} {'D_full':>9} "
           f"{'Q_D':>8} {'Q_exp':>8} {'err_D':>7} {'err_L':>7}")
    print(hdr)
    print("-" * len(hdr))

    errs_d, errs_l = [], []
    for z, n, decay, q_exp in BENCHMARKS:
        r = Q_dirac(z, n)
        e_d = (r['Q_dirac_kappa'] - q_exp) / q_exp * 100
        e_l = (r['Q_log_kappa'] - q_exp) / q_exp * 100
        errs_d.append(abs(e_d)); errs_l.append(abs(e_l))

        print(f"  {decay:>14} {r['D_sym']:>+9.4f} {r['D_alt']:>+9.4f} "
              f"{r['D_full']:>+9.4f} {r['Q_dirac_kappa']:>8.5f} "
              f"{q_exp:>8.5f} {e_d:>+6.1f}% {e_l:>+6.1f}%")

    mae_d = sum(errs_d) / len(errs_d)
    mae_l = sum(errs_l) / len(errs_l)
    print()
    print(f"  Dirac (|D_full| × κ):     MAE = {mae_d:.1f}%")
    print(f"  Log   (|Σ ln ratio| × κ): MAE = {mae_l:.1f}%")

    # ── Table 2: Sym/Alt ratio ──
    print()
    print("SYM / ALT CHANNEL RATIO")
    print("-" * 60)
    for z, n, decay, q_exp in BENCHMARKS:
        r = Q_dirac(z, n)
        ratio = abs(r['D_sym'] / r['D_alt']) if abs(r['D_alt']) > 1e-30 else float('inf')
        pct_sym = abs(r['D_sym']) / (abs(r['D_sym']) + abs(r['D_alt'])) * 100
        print(f"  {decay:>14}: |D_sym/D_alt| = {ratio:>8.2f}  "
              f"({pct_sym:>5.1f}% sym, {100-pct_sym:>5.1f}% alt)")

    # ── Table 3: Deg 1×1 interaction in Dirac channels ──
    print()
    print("DEG 1×1 INTERACTION IN DIRAC CHANNELS")
    print("-" * 75)
    hdr2 = f"{'Decay':>14} {'sym×sym':>10} {'alt×alt':>10} {'sym×alt':>10} {'total':>10}"
    print(hdr2)
    print("-" * len(hdr2))
    for z, n, decay, q_exp in BENCHMARKS:
        r = Q_dirac(z, n)
        total_int = r['int_sym_sym'] + r['int_alt_alt'] + r['int_sym_alt']
        print(f"  {decay:>14} {r['int_sym_sym']:>+10.4f} "
              f"{r['int_alt_alt']:>+10.4f} {r['int_sym_alt']:>+10.4f} "
              f"{total_int:>+10.4f}")

    # ── Table 4: J¹ jet data for ³H ──
    print()
    print("J¹ JET BUNDLE DATA: ³H→³He")
    print("-" * 90)
    r = Q_dirac(1, 2)
    print(f"{'gen':>4} {'V̂_p':>9} {'V̂_d':>9} {'ΔV̂':>9} "
          f"{'tr_p':>8} {'tr_d':>8} {'Δtr':>8} "
          f"{'spr_p':>8} {'spr_d':>8} {'Δspr':>8}")
    print("-" * 90)
    for jd in r['jet_data']:
        print(f"  {jd['gen']:>3} {jd['vp']:>+9.5f} {jd['vd']:>+9.5f} "
              f"{jd['dvol']:>+9.5f} "
              f"{jd['tr_p']:>+8.4f} {jd['tr_d']:>+8.4f} {jd['dtr']:>+8.4f} "
              f"{jd['spr_p']:>+8.4f} {jd['spr_d']:>+8.4f} {jd['dspr']:>+8.4f}")

    # ── Table 5: Higher NF for ³H ──
    print()
    print("HIGHER NF (FULL MATRIX INVARIANTS): ³H→³He")
    print("-" * 80)
    nf = higher_nf(1, 2)
    print(f"{'gen':>4} {'det_p':>8} {'det_d':>8} {'tr_p':>8} {'tr_d':>8} "
          f"{'off_p':>8} {'off_d':>8}")
    for row in nf:
        print(f"  {row['gen']:>3} {row['det_p']:>+8.4f} {row['det_d']:>+8.4f} "
              f"{row['tr_p']:>+8.4f} {row['tr_d']:>+8.4f} "
              f"{row['off_p']:>+8.4f} {row['off_d']:>+8.4f}")

    # ── Calibrated Dirac ──
    r_3h = Q_dirac(1, 2)
    if abs(r_3h['D_full']) > 1e-30:
        kappa_D = 0.01861 / abs(r_3h['D_full'])
    else:
        kappa_D = KAPPA

    print()
    print(f"CALIBRATED Q_DIRAC (κ_D from ³H)")
    print(f"  κ_D = {kappa_D:.6f} MeV  (compare κ = {KAPPA:.6f})")
    print("-" * 70)
    print(f"{'Decay':>14} {'Q_D':>9} {'Q_exp':>9} {'err':>7}")

    errs_cal = []
    for z, n, decay, q_exp in BENCHMARKS:
        r = Q_dirac(z, n)
        q_d = abs(r['D_full']) * kappa_D
        err = (q_d - q_exp) / q_exp * 100
        errs_cal.append(abs(err))
        print(f"  {decay:>14} {q_d:>9.5f} {q_exp:>9.5f} {err:>+6.1f}%")

    mae_cal = sum(errs_cal) / len(errs_cal)
    print(f"\n  Calibrated Dirac MAE = {mae_cal:.1f}% (1 param: κ_D from ³H)")

    print()
    print("STRUCTURE")
    print("=" * 70)
    print("  D_∇ = q⁻¹·∇ + ℏ_q·ι_ξ∇")
    print("  Q_D = |D_sym + D_alt| × κ_D")
    print("    D_sym = q⁻¹ × Σ_i (Δtr_i / tr_i)   (relative symmetric)")
    print("    D_alt = ℏ_q × Σ_i (Δspr_i / spr_i)  (relative antisymmetric)")
    print()
    print("  Jet bundle J¹ tracks: (V̂_i, tr_i, spr_i, off_i)")
    print("  Higher NF: full 2×2 matrix invariants at each generator")
    print("  Deg 1×1 interaction: sym×sym + alt×alt + sym×alt cross-terms")
