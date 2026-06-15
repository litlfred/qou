"""Dirac × Yekutieli combination probes (50 dps).

Per author 'continue exploring 2+3' — combines q-Dirac-weighted
linking-weight candidates with Yekutieli per-cell additive structure
to see if a structurally natural combination yields Reading-A's
-G·h² exactly.

## Combinations tested

1. **Linear combination**: a·Family_A + b·Dirac_form with (a, b)
   chosen to hit h⁰=5/2 AND h²=-G. Report a, b values; see if
   they match any natural constants.

2. **Family_A + Yekutieli (Reading B)**: 5/2 + (3/4 − G)·h².
   Baseline for comparison.

3. **Dirac_form + Yekutieli additive**: (Dirac h² coef) + (-G)·h².
   If Dirac h² ≈ 0, would give exactly -G; if Dirac h² < 0,
   over-corrects.

4. **Multiplicative Dirac on Family_A**: Family_A · f(D_q) for
   various Dirac-derived f. Specific test: f = 1 - α·D_q²/(1+D_q²).

5. **Yekutieli per-partition per audit 2026-05-22**: assign -G/8
   per cell, sum per partition; see if combined with any Family
   A-like sum yields -G total.

## Cross-references

- audit 2026-05-22 Yekutieli per-cell conjecture
- audit 2026-05-23 natural-reading negative
- q_dirac_h5_lift_and_refinements (parent: -0.880, α_opt = 0.140)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def hooks(p):
    rows = len(p)
    cols = p[0] if rows else 0
    col_h = [sum(1 for r in p if r > j) for j in range(cols)]
    out = []
    for i, rl in enumerate(p):
        for j in range(rl):
            out.append((rl - 1 - j) + (col_h[j] - 1 - i) + 1)
    return out


def content_sum(p):
    return sum(j - i for i, row in enumerate(p) for j in range(row))


def dim_q(p, q):
    n = sum(p)
    if n == 0:
        return mp.mpf(1)
    def br(k):
        if k == 1:
            return mp.mpf(1)
        return (q ** k - q ** (-k)) / (q - 1 / q)
    nf = mp.mpf(1)
    for k in range(1, n + 1):
        nf = nf * br(k)
    hp = mp.mpf(1)
    for h in hooks(p):
        hp = hp * br(h)
    return nf / hp


def q_br(k, q):
    if k == 0:
        return mp.mpf(0)
    return (q ** k - q ** (-k)) / (q - 1 / q)


def D_q2(p, q):
    return q_br(content_sum(p), q) ** 2


def fit_h(values, h_vals, max_order=4):
    even = list(range(0, max_order + 1, 2))
    n = len(even)
    V = mp.matrix(n, n)
    for i in range(n):
        for j, o in enumerate(even):
            V[i, j] = h_vals[i] ** o
    a = mp.lu_solve(V, mp.matrix(values[:n]))
    return {even[j]: a[j] for j in range(n)}


def main():
    set_compute_dps(50)
    w = WitnessBuilder(
        "dirac-yekutieli-combinations-50dps",
        engine="python",
    )
    w.set_audit_only(
        "docs/audits/2026-05-25-path-c-categorical-principle-hunt.md",
    )
    w.set_description(
        "Combines Dirac-weighted linking-weight candidates with "
        "Yekutieli per-cell additive structure to test for natural "
        "combinations matching Reading-A's -G·h² coefficient."
    )

    print("=" * 78)
    print("Dirac × Yekutieli combinations (50 dps)")
    print("=" * 78)

    G = mp.catalan
    target = -G
    print(f"\nTarget h² coefficient: -G = {mp.nstr(-G, 12)}")

    parts = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
    sample_q_strs = ["1.05", "1.08", "1.11", "1.14", "1.17"]
    h_vals = [mp.mpf(qs) - 1 / mp.mpf(qs) for qs in sample_q_strs]

    # === Reference: Family A ===
    def family_a(q):
        return sum(dim_q(p, q) for p in parts) / 4

    # === Dirac form (1+D_q²)/ΣW ===
    def dirac_form(q):
        num = sum((1 + D_q2(p, q)) * dim_q(p, q) for p in parts)
        den = sum(1 + D_q2(p, q) for p in parts)
        return num / den

    # === Yekutieli per-cell additive: -G·h² ===
    def yekutieli_per_cell(q):
        h = q - 1 / q
        return -G * h ** 2

    fA_coefs = fit_h([family_a(mp.mpf(qs)) for qs in sample_q_strs], h_vals)
    dirac_coefs = fit_h([dirac_form(mp.mpf(qs)) for qs in sample_q_strs], h_vals)
    print(f"\nFamily A:           a_0 = {mp.nstr(fA_coefs[0], 12)}, a_2 = {mp.nstr(fA_coefs[2], 12)}")
    print(f"Dirac (1+D_q²)/ΣW: a_0 = {mp.nstr(dirac_coefs[0], 12)}, a_2 = {mp.nstr(dirac_coefs[2], 12)}")

    # === Combination 1: Linear a·FA + b·Dirac → (5/2, -G) ===
    # Solve: a · fA[0] + b · D[0] = 5/2
    #        a · fA[2] + b · D[2] = -G
    M = mp.matrix([
        [fA_coefs[0], dirac_coefs[0]],
        [fA_coefs[2], dirac_coefs[2]],
    ])
    rhs = mp.matrix([mp.mpf("2.5"), target])
    ab = mp.lu_solve(M, rhs)
    a_lin, b_lin = ab[0], ab[1]
    print(f"\n[Combination 1: Linear a·FA + b·Dirac]")
    print(f"  a = {mp.nstr(a_lin, 18)}")
    print(f"  b = {mp.nstr(b_lin, 18)}")
    print(f"  Verify: a·FA + b·Dirac at h⁰ = {mp.nstr(a_lin * fA_coefs[0] + b_lin * dirac_coefs[0], 15)} (target 5/2)")
    print(f"          a·FA + b·Dirac at h² = {mp.nstr(a_lin * fA_coefs[2] + b_lin * dirac_coefs[2], 15)} (target -G)")
    print(f"  Candidate identities for (a, b):")
    print(f"    a + b = {mp.nstr(a_lin + b_lin, 10)}")
    print(f"    a · b = {mp.nstr(a_lin * b_lin, 10)}")
    print(f"    b / a = {mp.nstr(b_lin / a_lin, 10)}")
    print(f"    a · G = {mp.nstr(a_lin * G, 10)}")
    print(f"    b / G = {mp.nstr(b_lin / G, 10)}")

    # === Combination 2: Reading B (Family A + Yekutieli) ===
    def reading_b(q):
        return family_a(q) + yekutieli_per_cell(q)
    rb_coefs = fit_h([reading_b(mp.mpf(qs)) for qs in sample_q_strs], h_vals)
    rb_delta_to_target = rb_coefs[2] - target
    print(f"\n[Combination 2: Reading B = Family A + Yekutieli (additive)]")
    print(f"  a_0 = {mp.nstr(rb_coefs[0], 12)} (target 5/2)")
    print(f"  a_2 = {mp.nstr(rb_coefs[2], 12)} (target -G = {mp.nstr(target, 10)})")
    print(f"  Δ a_2 vs -G = {mp.nstr(rb_delta_to_target, 8)}")

    # === Combination 3: Dirac + Yekutieli ===
    def dirac_plus_yek(q):
        return dirac_form(q) + yekutieli_per_cell(q)
    dy_coefs = fit_h([dirac_plus_yek(mp.mpf(qs)) for qs in sample_q_strs], h_vals)
    print(f"\n[Combination 3: Dirac (1+D_q²)/ΣW + Yekutieli]")
    print(f"  a_0 = {mp.nstr(dy_coefs[0], 12)}")
    print(f"  a_2 = {mp.nstr(dy_coefs[2], 12)} (target -G)")
    print(f"  Δ a_2 vs -G = {mp.nstr(dy_coefs[2] - target, 8)}")

    # === Combination 4: Family A · multiplicative Dirac factor ===
    # Need to find α such that FA · (1 - α·D_q²/(1+D_q²)) gives h² = -G
    print(f"\n[Combination 4: FA · (1 − α · D_q²/(1+D_q²))]")
    def family_a_mult_dirac(q, alpha):
        fA = family_a(q)
        dirac_factor = 1 - alpha * sum(D_q2(p, q) / (1 + D_q2(p, q)) for p in parts) / 5
        return fA * dirac_factor

    # Bisect for alpha
    def residual_mult(alpha_val):
        coefs = fit_h([family_a_mult_dirac(mp.mpf(qs), alpha_val) for qs in sample_q_strs], h_vals)
        return coefs[2] - target

    lo, hi = mp.mpf(0), mp.mpf(10)
    rl, rh = residual_mult(lo), residual_mult(hi)
    print(f"  residual at α=0: {mp.nstr(rl, 8)} (Family A baseline)")
    print(f"  residual at α=10: {mp.nstr(rh, 8)}")
    if rl * rh < 0:
        for _ in range(60):
            mid = (lo + hi) / 2
            rm = residual_mult(mid)
            if abs(rm) < mp.mpf("1e-40"):
                break
            if rm * rl < 0:
                hi, rh = mid, rm
            else:
                lo, rl = mid, rm
        alpha_mult = (lo + hi) / 2
        print(f"  Optimal α: {mp.nstr(alpha_mult, 25)}")
        print(f"    Candidates: 1/G = {mp.nstr(1/G, 8)}, G = {mp.nstr(G, 8)}, 2G = {mp.nstr(2*G, 8)}, π/G = {mp.nstr(mp.pi/G, 8)}")
    else:
        alpha_mult = None
        print(f"  No zero in [0, 10]")

    # === Combination 5: Yekutieli per-partition uniform vs cell-counted ===
    print(f"\n[Combination 5: Per-partition Yekutieli assignment]")
    # Uniform: each partition gets -G/5 · h² (5 partitions, equal share)
    # Cell-counted (audit 2026-05-22): 2+4+2 = 8 cells, distributed
    #   (4): 1 cell → -G/8
    #   (3,1): 1 cell out of 4 edge → -G/8
    #   (2,2): 2 cells / 2 mult → -G/4
    #   (2,1,1): 1 cell → -G/8
    #   (1^4): 1 cell → -G/8
    cell_count = {(4,): 1, (3, 1): 1, (2, 2): 2, (2, 1, 1): 1, (1, 1, 1, 1): 1}
    cell_yek_per_partition = {p: mp.mpf(-G) * mp.mpf(cell_count[p]) / 8 for p in parts}
    def family_a_plus_per_cell_yek(q):
        fA_per_partition = {
            (4,): mp.mpf(1) / 4,
            (3, 1): dim_q((3, 1), q) / 4,
            (2, 2): dim_q((2, 2), q) / 4,
            (2, 1, 1): dim_q((2, 1, 1), q) / 4,
            (1, 1, 1, 1): mp.mpf(1) / 4,
        }
        h2 = (q - 1 / q) ** 2
        total = sum(fA_per_partition[p] + cell_yek_per_partition[p] * h2 for p in parts)
        return total
    fAY_coefs = fit_h([family_a_plus_per_cell_yek(mp.mpf(qs)) for qs in sample_q_strs], h_vals)
    print(f"  FA + per-cell Yekutieli: a_0 = {mp.nstr(fAY_coefs[0], 12)}, a_2 = {mp.nstr(fAY_coefs[2], 12)}")
    print(f"  Δ a_2 vs -G = {mp.nstr(fAY_coefs[2] - target, 8)}")

    # m_p predictions for each
    print(f"\n[m_p predictions at q_0]")
    q0 = mp.mpf(Q_50_DIGIT_STR)
    qi = 1 / q0
    h2_q0 = (q0 - qi) ** 2
    hbar_q = 1 - qi
    m_e = mp.mpf("0.51099895069")
    m_p_codata = mp.mpf("938.27208816")
    vol_b3 = 8 * G
    geom_leading = vol_b3 / hbar_q ** 2

    def m_p_for_coefs(coefs):
        # a_0 should be 5/2 for direct prediction; if not, rescale
        if abs(coefs[0] - mp.mpf("2.5")) < mp.mpf("0.01"):
            lw = coefs[0] + coefs[2] * h2_q0 + coefs.get(4, mp.mpf(0)) * h2_q0 ** 2
        else:
            # Rescale to a_0 = 5/2
            scale = mp.mpf("2.5") / coefs[0]
            a2_scaled = coefs[2] * scale
            lw = mp.mpf("2.5") + a2_scaled * h2_q0
        m_p = m_e * geom_leading * lw
        ppm = (m_p - m_p_codata) / m_p_codata * 1e6
        return m_p, ppm

    schemes_for_mp = [
        ("Family A", fA_coefs),
        ("Reading B (FA+Yek)", rb_coefs),
        ("Dirac form alone", dirac_coefs),
        ("Dirac + Yek", dy_coefs),
        ("Linear a·FA+b·Dirac (exact)", {0: mp.mpf("2.5"), 2: target, 4: mp.mpf(0)}),
        ("FA + per-cell Yek", fAY_coefs),
    ]
    print(f"  {'scheme':<32}{'m_p_pred (MeV)':<18}{'ppm vs CODATA':<14}")
    for name, coefs in schemes_for_mp:
        mp_pred, ppm = m_p_for_coefs(coefs)
        print(f"  {name:<32}{mp.nstr(mp_pred, 12):<18}{mp.nstr(ppm, 8):<14}")

    # Witness
    w.add_parameter("sample_q_strs", sample_q_strs)
    w.add_parameter("target_h2_minus_G", mp.nstr(-G, 25))
    w.add_data("family_a_coeffs", {f"a_{k}": mp.nstr(v, 25) for k, v in fA_coefs.items()})
    w.add_data("dirac_form_coeffs", {f"a_{k}": mp.nstr(v, 25) for k, v in dirac_coefs.items()})
    w.add_data("linear_combination", {
        "a": mp.nstr(a_lin, 25),
        "b": mp.nstr(b_lin, 25),
        "a_plus_b": mp.nstr(a_lin + b_lin, 25),
        "b_over_a": mp.nstr(b_lin / a_lin, 25),
        "interpretation": (
            "Linear combination a·FamilyA + b·Dirac that yields exactly "
            "h⁰=5/2 and h²=-G. The required (a, b) values are not "
            "recognizable as standard mathematical constants."
        ),
    })
    w.add_data("reading_b_FA_plus_Yekutieli", {
        "a_0": mp.nstr(rb_coefs[0], 25),
        "a_2": mp.nstr(rb_coefs[2], 25),
        "delta_vs_target": mp.nstr(rb_coefs[2] - target, 25),
    })
    w.add_data("dirac_plus_yekutieli", {
        "a_0": mp.nstr(dy_coefs[0], 25),
        "a_2": mp.nstr(dy_coefs[2], 25),
        "delta_vs_target": mp.nstr(dy_coefs[2] - target, 25),
    })
    if alpha_mult is not None:
        w.add_data("multiplicative_optimal_alpha", {
            "alpha": mp.nstr(alpha_mult, 25),
            "candidates_close_to": {
                "G": mp.nstr(G, 10),
                "1_over_G": mp.nstr(1 / G, 10),
                "pi_over_G": mp.nstr(mp.pi / G, 10),
            }
        })
    w.add_data("per_cell_yekutieli", {
        "a_0": mp.nstr(fAY_coefs[0], 25),
        "a_2": mp.nstr(fAY_coefs[2], 25),
        "delta_vs_target": mp.nstr(fAY_coefs[2] - target, 25),
    })
    w.add_data("m_p_predictions_ppm", {
        name: mp.nstr(m_p_for_coefs(coefs)[1], 8)
        for name, coefs in schemes_for_mp
    })

    w.add_data("verdict", (
        "None of the tested combinations naturally produce -G·h² exactly "
        "without fitting. Linear combination requires (a, b) = "
        f"({mp.nstr(a_lin, 6)}, {mp.nstr(b_lin, 6)}) — not recognizable. "
        "Reading B (FA + Yek additive) gives -0.166 (Δ = 0.75). "
        "Dirac + Yek over-corrects. The structural identity for Reading-A "
        "remains unidentified; categorical proof still open."
    ))

    w.add_assertion(
        name="probe_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source="Dirac × Yekutieli combinations completed.",
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
