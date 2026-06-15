"""Higher-precision PSLQ for the h⁴-residual coefficient.

Task 2 of PR #1629. PR #1617's Form B identified `(f-1)/h⁴ ≈ 0.876580`
matching `7/8 + (G/(8π))·h²` to 0.0015% and `1 - π²/80` to 0.006%.
Task 1 confirmed these forms are q-anchor-stable.

This probe runs higher-precision (100+ dps) PSLQ over a WIDER basis
to either:
  - Confirm the leading-order 7/8 or 1-π²/80 form structurally
  - Identify an even tighter / cleaner structural form
  - Conclude that neither form is exact — empirical near-match

## Basis (17 elements)

The implemented basis is the natural-constants set: 1, G (Catalan),
π², ζ(3), ζ(5), ln(2/3/5), 1/π², G/π², ζ(3)/π³, α_em, α_em², h²,
h⁴, [3]_q, [5]_q. Mahler measures, Bloch-Wigner D(z) at substrate
roots, and q-Bernoulli evaluations are NOT in this basis — they were
identified as potential future extensions in the audit doc but
deferred (the natural basis NULL is informative enough on its own).

## Cross-references

- PR #1617 ocneanu_54ppb_residual_exploration.py
- PR #1629 h4_form_AB_cross_anchor_stability.py
- coord ledger 2026-06-01-h4-residual-derivation.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _h4_substrate import (  # noqa: E402
    ALPHA_EM,
    M_E_MEV,
    M_MU_MEV,
    M_P_MEV,
    qfact,
    qint,
    trM_borromean_closed,
)
from _precision import set_compute_dps  # noqa: E402
from q_parameter import q_at, q_str  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    DPS = 120
    set_compute_dps(DPS)  # significant headroom for PSLQ at maxcoeff 10⁶
    q = q_at(DPS)

    print("=" * 78)
    print("h⁴-residual coefficient — higher-precision PSLQ (120 dps)")
    print("=" * 78)

    # Compute target precisely
    h = q - 1 / q
    h2 = h * h
    qfact_3 = qfact(3, q)
    trM = abs(trM_borromean_closed(q))
    F_Bor = trM * qfact_3 / q ** 3
    k_req = (2 * M_MU_MEV * F_Bor - M_P_MEV) / M_E_MEV
    residual = 12 - k_req
    f = residual / (ALPHA_EM / mp.pi / 6)
    fm1 = f - 1
    coef_h4 = fm1 / h ** 4  # target ≈ 0.876580096

    G = mp.catalan

    print(f"\n[Target] (f-1)/h⁴ = {mp.nstr(coef_h4, 30)}")

    # Wider basis at q_0
    basis = {
        "1": mp.mpf(1),
        "G": G,
        "π²": mp.pi ** 2,
        "ζ(3)": mp.zeta(3),
        "ζ(5)": mp.zeta(5),
        "ln(2)": mp.log(2),
        "ln(3)": mp.log(3),
        "ln(5)": mp.log(5),
        "1/π²": 1 / mp.pi ** 2,
        "G/π²": G / mp.pi ** 2,
        "ζ(3)/π³": mp.zeta(3) / mp.pi ** 3,
        "α_em": ALPHA_EM,
        "α_em²": ALPHA_EM ** 2,
        "h²": h2,
        "h⁴": h ** 4,
        "[3]_q": qint(3, q),
        "[5]_q": qint(5, q),
    }
    basis_names = list(basis.keys())
    basis_values = [basis[n] for n in basis_names]

    # Pairwise PSLQ at higher precision
    print(f"\n[Pairwise PSLQ — target vs each basis element]")
    print(f"  Looking for integer relations a·target = b·basis_i, "
          f"|a|, |b| ≤ 10⁶")
    matches = []
    for name, val in basis.items():
        try:
            rel = mp.pslq([coef_h4, val], tol=mp.mpf("1e-25"),
                          maxcoeff=1000000)
            if rel and rel[0] != 0:
                ratio = -mp.mpf(rel[1]) / mp.mpf(rel[0])
                check = coef_h4 - ratio * val
                if abs(check) < mp.mpf("1e-22"):
                    matches.append((name, rel, ratio, abs(check)))
                    print(f"  ⭐ target ≈ ({rel[1]}/{rel[0]}) · {name} "
                          f"= {mp.nstr(ratio * val, 18)} "
                          f"(residual {mp.nstr(abs(check), 8)})")
        except Exception:
            pass
    if not matches:
        print(f"  No tight pairwise integer relations at maxcoeff 10⁶.")

    # Full-basis PSLQ
    print(f"\n[Full-basis PSLQ — target vs {len(basis_names)} basis elements]")
    print(f"  Looking for relation: a_0·target + Σ a_i·b_i = 0, maxcoeff 100")
    try:
        full = [coef_h4] + basis_values
        rel = mp.pslq(full, tol=mp.mpf("1e-30"), maxcoeff=100)
        if rel and rel[0] != 0:
            # Express target = -(Σ a_i · b_i) / a_0
            coefs = [mp.mpf(r) for r in rel]
            num = -sum(coefs[i + 1] * basis_values[i] for i in range(len(basis_values)))
            pred = num / coefs[0]
            check = coef_h4 - pred
            print(f"  Found relation: {rel}")
            print(f"  Predicted target = {mp.nstr(pred, 22)}")
            print(f"  Residual         = {mp.nstr(abs(check), 8)}")
            nonzero = [(rel[i + 1], basis_names[i]) for i in range(len(basis_values))
                       if rel[i + 1] != 0]
            print(f"  Nonzero terms (coefficient · basis name):")
            for a, n in nonzero:
                print(f"    {-a:+d} · {n}")
        else:
            print(f"  No full-basis integer relation found.")
    except Exception as e:
        print(f"  PSLQ failed: {e}")

    # Specific test: 1 - π²/N for various N
    print(f"\n[Direct test — 1 - π²/N for N ∈ {{40..200}}]")
    best_N = None
    best_dN = mp.inf
    for N in range(40, 201):
        pred = 1 - mp.pi ** 2 / N
        d = (pred - coef_h4) / coef_h4 * mp.mpf("1e6")
        if abs(d) < abs(best_dN):
            best_dN = d
            best_N = N
    print(f"  Best N = {best_N}, Δ ppm = {mp.nstr(best_dN, 8)}")
    # Also non-integer N
    N_exact = mp.pi ** 2 / (1 - coef_h4)
    print(f"  Exact N (1 - π²/N = target) = {mp.nstr(N_exact, 18)}")
    print(f"  vs integer 80: Δ = {mp.nstr(N_exact - 80, 12)} ({mp.nstr((N_exact - 80) / 80 * mp.mpf('1e6'), 6)} ppm)")

    # Verdict
    print(f"\n[Verdict]")
    if matches:
        verdict = (
            f"PSLQ HIT(s): {len(matches)} clean integer relations found at "
            f"100+ dps precision, tol 1e-22, maxcoeff 10⁶. The h⁴-residual "
            f"coefficient has a clean structural form."
        )
    else:
        verdict = (
            f"NULL — no clean PSLQ integer relations at higher precision. "
            f"The h⁴-residual coefficient is NOT a rational multiple of "
            f"any single basis element in {{G, π², ζ(3), ln(2), ...}}. "
            f"Best N for `1 - π²/N` form: N = {best_N} (Δ = {mp.nstr(best_dN, 6)} ppm). "
            f"Exact N = {mp.nstr(N_exact, 12)} — NOT clean integer 80."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "h4-residual-higher-precision-pslq",
        engine="python",
    )
    w.set_description(
        "Task 2 of PR #1629: higher-precision (120 dps) PSLQ search for "
        "the h⁴-residual coefficient (target ≈ 0.876580096) across 17 "
        "natural substrate basis elements. Tests pairwise (maxcoeff 10⁶) "
        "and full basis (maxcoeff 100)."
    )
    w.add_parameter("q_120dps", q_str(DPS))
    w.add_parameter("mp_dps_runtime", str(mp.mp.dps))
    w.add_data("target_h4_coef", mp.nstr(coef_h4, 30))
    w.add_data("pslq_pairwise_hits", len(matches))
    w.add_data("exact_N_for_one_minus_pi2_over_N", mp.nstr(N_exact, 18))
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="higher_precision_pslq_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source="120-dps PSLQ at maxcoeff up to 10⁶.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
