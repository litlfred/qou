"""Q-Dirac-derived linking-weight EXTENDED variants (50 dps).

Per author 'keep exploring' direction, following up on
`q_dirac_linking_weight_probe_50dps.py` BREAKTHROUGH: scheme 6
(Σ D_q²·dim_q V_λ / Σ D_q²) gives NEGATIVE h² coefficient
(a_2_normalized = -0.79, off from -G by 14%).

This probe tests ~12 VARIANTS of Dirac-weighting to find one that
matches -G ≈ -0.916 more precisely (or exactly).

## Variants tested

For weight W(λ) and normalization N:

  linking_weight = Σ_λ W(λ) · dim_q V_λ / N

with:
- W(λ) ∈ {D_q²(λ), 1+D_q²(λ), [c_λ]_q, |c_λ|·[c_λ]_q,
          D_q²(λ)/d_λ, D_q²(λ)·d_λ, regularized 1/(ε+D_q²)}
- N ∈ {Σ_λ W(λ), Σ_λ 1 (= 5), 4 (Family A normalization),
       Σ_λ d_λ (= 10), Σ_λ d_λ² (= 24)}

Some combinations may yield a_2_norm ≈ -G structurally.

## Also evaluates at q_0 for m_p prediction

For the best candidates, compute m_p prediction directly and
compare to CODATA 938.27208816 MeV.

## Cross-references

- q_dirac_linking_weight_probe_50dps.py (parent breakthrough)
- audit 2026-05-25 Path C
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import M_E_MEV, M_P_MEV_VALIDATION  # noqa: E402
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


def classical_dim(p):
    n = sum(p)
    from math import factorial
    pr = 1
    for h in hooks(p):
        pr *= h
    return factorial(n) // pr


def dim_q(p, q):
    n = sum(p)
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
    if len(h_vals) < n:
        raise ValueError("need more pts")
    V = mp.matrix(n, n)
    for i in range(n):
        for j, o in enumerate(even):
            V[i, j] = h_vals[i] ** o
    a = mp.lu_solve(V, mp.matrix(values[:n]))
    return {even[j]: a[j] for j in range(n)}


def main():
    set_compute_dps(50)
    w = WitnessBuilder(
        "q-dirac-linking-weight-extended-50dps",
        engine="python",
    )
    w.set_audit_only(
        "docs/audits/2026-05-25-path-c-categorical-principle-hunt.md",
    )
    w.set_description(
        "Extended q-Dirac variants — 12 weighting+normalization schemes "
        "at H_4 (50 dps). Follows breakthrough where scheme 6 of parent "
        "probe gave NEGATIVE h² coefficient (-0.79 vs target -G = -0.916). "
        "Searches for variant matching -G more precisely."
    )

    print("=" * 78)
    print("Q-Dirac linking-weight EXTENDED variants at H_4 (50 dps)")
    print("=" * 78)

    G = mp.catalan
    target = -G
    print(f"\nTarget h² coefficient: -G = {mp.nstr(-G, 12)}")

    parts = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
    sample_q_strs = ["1.05", "1.08", "1.11", "1.14", "1.17"]
    h_vals = [mp.mpf(qs) - 1 / mp.mpf(qs) for qs in sample_q_strs]

    # Define weights and normalizations
    def W_funcs(q):
        """Return dict name → weight function value(λ)."""
        return {
            "D_q2": lambda p: D_q2(p, q),
            "1+D_q2": lambda p: 1 + D_q2(p, q),
            "[c]_q": lambda p: q_br(content_sum(p), q),
            "|c|·[c]_q²": lambda p: abs(content_sum(p)) * D_q2(p, q),
            "D_q2/d_lam": lambda p: D_q2(p, q) / classical_dim(p),
            "D_q2·d_lam": lambda p: D_q2(p, q) * classical_dim(p),
            "1/(ε+D_q2)": lambda p: 1 / (mp.mpf("0.01") + D_q2(p, q)),
            "exp(-D_q2)": lambda p: mp.exp(-D_q2(p, q)),
            "D_q2 excl kernel": lambda p: (mp.mpf(0) if content_sum(p) == 0
                                            else D_q2(p, q)),
            "[c]_q · d_lam": lambda p: q_br(content_sum(p), q) * classical_dim(p),
            "c²": lambda p: mp.mpf(content_sum(p) ** 2),
            "D_q2 · [c]_q": lambda p: D_q2(p, q) * q_br(content_sum(p), q),
        }

    def N_funcs(weight_funcs, q, weight_name):
        """Return dict name → normalization value."""
        W = weight_funcs[weight_name]
        return {
            "ΣW": sum(W(p) for p in parts),
            "5 (|parts|)": mp.mpf(5),
            "4 (Family A)": mp.mpf(4),
            "Σd_λ=10": mp.mpf(10),
            "Σd_λ²=24": mp.mpf(24),
        }

    results = []
    for w_name in [
        "D_q2", "1+D_q2", "[c]_q", "|c|·[c]_q²",
        "D_q2/d_lam", "D_q2·d_lam", "1/(ε+D_q2)", "exp(-D_q2)",
        "D_q2 excl kernel", "[c]_q · d_lam", "c²", "D_q2 · [c]_q",
    ]:
        for n_name in ["ΣW", "5 (|parts|)", "4 (Family A)", "Σd_λ²=24"]:
            try:
                # Compute lw at each q
                vals = []
                for qs in sample_q_strs:
                    q = mp.mpf(qs)
                    Wf = W_funcs(q)[w_name]
                    Nf = N_funcs(W_funcs(q), q, w_name)[n_name]
                    num = sum(Wf(p) * dim_q(p, q) for p in parts)
                    if abs(Nf) < mp.mpf("1e-40"):
                        continue
                    vals.append(num / Nf)
                if len(vals) < 3:
                    continue
                coeffs = fit_h(vals, h_vals, max_order=4)
                a0 = coeffs[0]
                a2 = coeffs[2]
                if abs(a0) < mp.mpf("1e-30"):
                    continue
                a2_norm = a2 * mp.mpf("2.5") / a0
                delta = a2_norm - target
                results.append({
                    "weight": w_name,
                    "norm": n_name,
                    "a_0": a0,
                    "a_2": a2,
                    "a_2_norm": a2_norm,
                    "delta": delta,
                    "abs_delta": abs(delta),
                })
            except Exception:
                continue

    # Sort by |delta|
    results.sort(key=lambda r: r["abs_delta"])

    print(f"\n{'rank':<6}{'weight':<22}{'norm':<14}{'a_0':<14}{'a_2_norm':<18}{'|Δ vs -G|':<14}")
    for rank, r in enumerate(results[:20], 1):
        marker = " ⭐" if r["abs_delta"] < mp.mpf("0.01") else (
                  "" if r["abs_delta"] > mp.mpf("0.1") else " *")
        print(f"  {rank:<6}{r['weight']:<22}{r['norm']:<14}"
              f"{mp.nstr(r['a_0'], 8):<14}{mp.nstr(r['a_2_norm'], 12):<18}"
              f"{mp.nstr(r['abs_delta'], 8):<14}{marker}")

    # Within 1% match?
    within_1pct = [r for r in results if r["abs_delta"] < mp.mpf("0.01")]
    if within_1pct:
        print(f"\n[FOUND {len(within_1pct)} scheme(s) within 1% of -G]")
        for r in within_1pct:
            print(f"  {r['weight']} / {r['norm']}: |Δ| = {mp.nstr(r['abs_delta'], 8)}")
            # Compute m_p prediction
            q0 = mp.mpf(Q_50_DIGIT_STR)
            qi = 1 / q0
            h2 = (q0 - qi) ** 2
            hbar_q = 1 - qi
            lw_at_q0 = mp.mpf("2.5") + r["a_2_norm"] * h2
            m_e = M_E_MEV
            vol_b3 = 8 * G
            geom_leading = vol_b3 / hbar_q ** 2
            m_p_pred = m_e * geom_leading * lw_at_q0
            m_p_codata = M_P_MEV_VALIDATION
            ppm = (m_p_pred - m_p_codata) / m_p_codata * 1e6
            print(f"    m_p prediction (at a_2_norm = {mp.nstr(r['a_2_norm'], 8)}): "
                  f"{mp.nstr(m_p_pred, 12)} MeV ({mp.nstr(ppm, 6)} ppm)")
    else:
        print(f"\nClosest scheme: '{results[0]['weight']}' / '{results[0]['norm']}' "
              f"at |Δ| = {mp.nstr(results[0]['abs_delta'], 8)}")
        print(f"NO scheme within 1% of -G in this catalog.")

    # Witness
    w.add_parameter("sample_q_strs", sample_q_strs)
    w.add_parameter("target_h2_minus_G", mp.nstr(-G, 25))
    w.add_data("top_20_schemes", [
        {
            "rank": rank,
            "weight": r["weight"],
            "norm": r["norm"],
            "a_0": mp.nstr(r["a_0"], 25),
            "a_2_normalized": mp.nstr(r["a_2_norm"], 25),
            "absolute_delta": mp.nstr(r["abs_delta"], 12),
        }
        for rank, r in enumerate(results[:20], 1)
    ])
    w.add_data("within_1pct_count", len(within_1pct))
    if within_1pct:
        w.add_data("within_1pct", [
            {"weight": r["weight"], "norm": r["norm"],
             "delta": mp.nstr(r["delta"], 12)}
            for r in within_1pct
        ])

    w.add_data("verdict", (
        f"Tested {len(results)} weight/norm combinations. "
        f"{len(within_1pct)} within 1% of -G. "
        f"Closest: '{results[0]['weight']}' / '{results[0]['norm']}' at "
        f"|Δ| = {mp.nstr(results[0]['abs_delta'], 8)}. "
        + ("Found structural candidate(s) — recommend deeper investigation."
           if within_1pct else
           "Negative-a_2 achievable via Dirac weighting, but no exact "
           "-G match in this catalog. Suggests linking_weight involves "
           "additional structure beyond simple Dirac-weighted Wedderburn sums.")
    ))

    w.add_assertion(
        name="extended_prescreen_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source=f"Tested {len(results)} variants; {len(within_1pct)} within 1%.",
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
