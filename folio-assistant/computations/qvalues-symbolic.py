"""
Symbolic Q-value derivation: keep q symbolic as long as possible.

The transfer matrix chain is exact in ℤ[q^½, q^{-½}].
We compute V̂_i(q) symbolically, form the log ratio, and only
evaluate at q₀ for the final Q-value.

Derivation chain (symbolic):
  1. Crossing weights (c, d) ∈ ℤ[q, q⁻¹]       — exact
  2. Transfer matrix T(c,d) ∈ M₂(ℤ[q, q⁻¹])     — exact
  3. Chain matrix M_i = ∏_j T(i,j) ∈ M₂(ℤ[q^½, q^{-½}])  — exact
  4. Traced volume V̂_i = z·M[0,0] + M[1,0] ∈ ℚ(q^½)  — exact
  5. Volume ratio V̂_i^dau / V̂_i^par ∈ ℚ(q^½)  — exact
  6. log_q(ratio) — transcendental: evaluate at q₀

Each step is in ℤ[t, t⁻¹] where t = q^½, until step 6.
Note: the Markov parameter z = 1/(√q + 1/√q) introduces q^½,
so steps 3–5 live in ℤ[q^½, q^{-½}], not in ℤ[q, q⁻¹].

Crossing weight convention (Hecke inverse σ⁻¹ = σ − h, h = q − q⁻¹):
  pp → σ:          c = 1,   d = 0
  nn → σ⁻¹:        c = 1,   d = −h
  pn → ½(σ+σ⁻¹): c = 1,   d = −h/2
"""

import sympy as sp
from sympy import sqrt, Rational, log, symbols, simplify, factor
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from q_parameter import Q as Q_NUM, Q_ERR, HBAR_Q, VOL_FIGURE_EIGHT, MASS_RATIO_MU_E
from experimental_constants import M_E_MEV

# ── Symbolic setup ───────────────────────────────────────────────
q = symbols('q', positive=True)

# Derived quantities (exact in ℚ(q))
q_inv = 1/q
HA_sym = q - q_inv                    # Hecke amplitude h = q − q⁻¹
z_sym = 1 / (sqrt(q) + 1/sqrt(q))     # Markov parameter (introduces q^½)

# Energy scale: κ_q = ln(q) × m_e/3  — transcendental in q
# We keep it symbolic as log(q) * m_e/3 until final eval
m_e = Rational(M_E_MEV).limit_denominator(10**10)

# ── Crossing weights (exact in ℤ[q, q⁻¹]) ──────────────────────

def crossing_coeffs_sym(type_i, type_j):
    """Hecke weights (c, d) where T(c,d) = c·σ + d·1.

    From σ⁻¹ = σ − h  (h = q − q⁻¹):
      pp → σ:          c = 1,   d = 0
      nn → σ⁻¹:        c = 1,   d = −h
      pn → ½(σ+σ⁻¹): c = 1,   d = −h/2
    """
    pair = type_i + type_j
    if pair == 'pp':
        return (sp.Integer(1), sp.Integer(0))
    elif pair == 'nn':
        return (sp.Integer(1), -HA_sym)
    else:  # pn or np
        return (sp.Integer(1), -HA_sym / 2)

# ── Transfer matrix (exact in ℚ(q^½)) ───────────────────────────

def transfer_matrix_sym(c, d):
    """2×2 transfer matrix T(c,d) over ℚ(q^½)."""
    return sp.Matrix([
        [c * HA_sym + d, c],
        [c,              d]
    ])

def generator_volumes_sym(z_val, n_val, simplify_each=True):
    """Symbolic traced volumes V̂_i(q) for nucleus (Z, N).

    Returns list of (V̂_i, M_i) pairs where V̂_i ∈ ℚ(q^½) and
    M_i ∈ M₂(ℚ(q^½)).
    """
    a = z_val + n_val
    types = ['p'] * z_val + ['n'] * n_val
    results = []

    for i in range(a - 1):
        M = sp.eye(2)
        for j in range(i + 1, a):
            c, d = crossing_coeffs_sym(types[i], types[j])
            T = transfer_matrix_sym(c, d)
            M = M * T
            if simplify_each:
                M = sp.simplify(M)

        # V̂_i = z·M[0,0] + M[1,0]
        vol = z_sym * M[0, 0] + M[1, 0]
        if simplify_each:
            vol = sp.simplify(vol)
        results.append((vol, M))

    return results

# ── Benchmark nuclei ─────────────────────────────────────────────

BENCHMARKS = [
    (1,  2,  "³H→³He",      0.01861, 0.00001),
    (6,  8,  "¹⁴C→¹⁴N",     0.15648, 0.00004),
]

# Shell factors
F_DEG2_sym = sp.Rational(369, 625)  # 0.5904 = 5904/10000 = 369/625
F_PAULI_sym = sp.Rational(6382, 10000)
MAGIC = [2, 8, 20, 28, 50, 82, 126]

def shell_degree(n_neutrons):
    for i, m in enumerate(MAGIC):
        if n_neutrons <= m:
            return 2 if i + 1 >= 5 else 1
    return 2

if __name__ == "__main__":
    print("=" * 80)
    print("SYMBOLIC Q-VALUE DERIVATION")
    print("All quantities exact in ℚ(q^½) until final evaluation at q₀")
    print("=" * 80)
    print()

    # Show the symbolic crossing weights
    print("Step 1: Crossing weights (exact in ℤ[q, q⁻¹], from σ⁻¹ = σ − h)")
    print(f"  pp → σ:          c = 1,   d = 0")
    print(f"  nn → σ⁻¹:        c = 1,   d = −h  (h = q−q⁻¹)")
    print(f"  pn → ½(σ+σ⁻¹): c = 1,   d = −h/2")
    print()

    print("Step 2: Transfer matrix T(c,d) = [[c·(q-q⁻¹)+d, c], [c, d]]")
    print()

    for z_val, n_val, name, q_exp, q_exp_err in BENCHMARKS:
        a = z_val + n_val
        print(f"\n{'='*80}")
        print(f"Nucleus: {name}  (Z={z_val}, N={n_val}, A={a})")
        print(f"{'='*80}")

        # Parent symbolic volumes
        print(f"\nStep 3: Parent ({z_val},{n_val}) chain matrices (exact):")
        par_results = generator_volumes_sym(z_val, n_val)
        for i, (vol, M) in enumerate(par_results):
            print(f"  σ_{i}: M_{i} = {M}")
            print(f"       V̂_{i}(q) = {vol}")

        # Daughter symbolic volumes
        z_dau, n_dau = z_val + 1, n_val - 1
        print(f"\nStep 4: Daughter ({z_dau},{n_dau}) chain matrices (exact):")
        dau_results = generator_volumes_sym(z_dau, n_dau)
        for i, (vol, M) in enumerate(dau_results):
            print(f"  σ_{i}: V̂_{i}(q) = {vol}")

        # Volume ratios (exact)
        print(f"\nStep 5: Volume ratios V̂_dau/V̂_par (exact in ℚ(q^½)):")
        types_p = ['p'] * z_val + ['n'] * n_val
        types_d = ['p'] * z_dau + ['n'] * n_dau

        ratios = []
        for i in range(a - 1):
            vol_p = par_results[i][0]
            vol_d = dau_results[i][0]
            ratio = sp.simplify(vol_d / vol_p)
            ratios.append(ratio)
            print(f"  R_{i}(q) = V̂_{i}^dau / V̂_{i}^par = {ratio}")

        # Classify generators
        print(f"\nStep 6: Generator classification:")
        lu_terms, lr_terms, luc_terms = [], [], []
        for i in range(a - 1):
            changed = []
            for j in range(i + 1, a):
                pair_p = types_p[i] + types_p[j]
                pair_d = types_d[i] + types_d[j]
                if pair_p != pair_d:
                    changed.append((j, pair_p, pair_d))

            if not changed:
                luc_terms.append(i)
                print(f"  σ_{i}: UNCHANGED")
            else:
                changes_str = ", ".join(f"({j}: {pp}→{pd})" for j, pp, pd in changed)
                print(f"  σ_{i}: CHANGED [{changes_str}]")
                # Classify as unbind or rebind
                nu = sum(1 for j, pp, pd in changed if pp == 'nn')
                nr = sum(1 for j, pp, pd in changed if pd == 'pp')
                if nr == 0:
                    lu_terms.append(i)
                elif nu == 0:
                    lr_terms.append(i)
                else:
                    lu_terms.append(i)  # mixed: assign to unbind for light nuclei

        # Evaluate at q₀
        print(f"\nStep 7: Evaluate at q₀ = {Q_NUM:.10f}")
        ln_q_num = math.log(Q_NUM)
        kappa_q_num = ln_q_num * M_E_MEV / 3.0

        lu_sum, lr_sum, luc_sum = 0.0, 0.0, 0.0
        for i in range(a - 1):
            ratio_num = float(ratios[i].subs(q, Q_NUM))
            lratio = math.log(abs(ratio_num)) / ln_q_num

            if i in lu_terms:
                lu_sum += lratio
            elif i in lr_terms:
                lr_sum += lratio
            else:
                luc_sum += lratio

        q_qwt = abs(Q_NUM * lu_sum + (1/Q_NUM) * lr_sum + luc_sum) * kappa_q_num
        deg = shell_degree(n_val)
        f = float(F_DEG2_sym) if deg >= 2 else 1.0
        if n_val in MAGIC and deg >= 2:
            f *= float(F_PAULI_sym)

        q_pred = q_qwt * f
        err_pct = (q_pred - q_exp) / q_exp * 100.0

        print(f"  Σ_unbind  = {lu_sum:+.6f}")
        print(f"  Σ_rebind  = {lr_sum:+.6f}")
        print(f"  Σ_unchanged = {luc_sum:+.6f}")
        print(f"  q·Σ_u + q⁻¹·Σ_r + Σ_uc = {Q_NUM*lu_sum + (1/Q_NUM)*lr_sum + luc_sum:+.6f}")
        print(f"  Q_qwt = {q_qwt:.6f} MeV")
        print(f"  F_shell = {f:.4f}")
        print(f"  Q_pred ≈ {q_pred:.5f} MeV")
        print(f"  Q_exp  ≈ {q_exp:.5f} ± {q_exp_err} MeV")
        print(f"  Error  = {err_pct:+.1f}%")

        # Show symbolic ratio evaluated
        print(f"\n  Symbolic check: R_0(q₀) = {float(ratios[0].subs(q, Q_NUM)):.10f}")

    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    print()
    print("The transfer matrix chain M_i(q) and traced volumes V̂_i(q) are")
    print("exact in ℚ(q^½) — no approximation until log evaluation at q₀.")
    print()
    print("The symbolic volume ratios show:")
    print("  - For ³H: ratio is a simple rational function of q")
    print("  - For ¹⁴C: ratio involves higher powers of q (longer chains)")
    print()
    print("The transcendental step is ONLY: log_q(V̂_dau/V̂_par),")
    print("which maps a rational function of q to a real number.")
    print("Everything before this is algebraic in q.")
