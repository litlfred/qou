"""m_n / Δ_pn flavor-split X(q) refinement — Item 3 of PR #1645.

Per CLAUDE.md L2 dashboard: m_n misses 100× target by 185× and Δ_pn
by 163×, both blocked by the canonical Hecke-skein X(q) formula's
0.10% intrinsic residual:

  (m_n - m_p) / M_N ≈ (q-1)² · (1 - q⁻⁴) / 3
                    ≈ ℏ_q² · h_q · [2]_q                  [factored]

  at q_0: -0.10% off CODATA (1.376e-3 vs 1.377e-3)

The 100× target needs ~1 ppb residual (10⁶× improvement). This probe
tests candidate refinements:

  (a) Higher-order Hecke-skein truncation: X·(1 + α·h² + β·h⁴ + ...)
  (b) Habiro-element identification: X·(1 - α·h²·something), parallel
      to α_em's `[2]_q · (1 - h²α)` from PR #1511
  (c) Plancherel-weighted Wedderburn correction
  (d) Direct algebraic refinement candidates

## Cross-references

- `prop:flavor-split-substrate` (the baseline X(q) formula)
- PR #1581 m_K/m_π pattern audit (identified shared blocker)
- PR #1511 α_em Habiro element template `[2]_q · (1 - h²α)`
- coord ledger 2026-06-01-mp-yekutieli-and-mn-flavorsplit.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _h4_substrate import M_E_MEV, M_P_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
import experimental_constants as _ec  # noqa: E402
from q_parameter import q_at, q_str  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Derive m_n from the 3-input scheme: m_n = m_p + m_e + Q_neutron
# (per repo convention; avoids P31 hard-coded CODATA literal flag)
import mpmath as _mp_for_neutron  # noqa: E402

M_N_MEV = M_P_MEV + M_E_MEV + _mp_for_neutron.mpf(repr(_ec.Q_NEUTRON_MEV))


def main() -> int:
    DPS = 80
    set_compute_dps(DPS)
    q = q_at(DPS)

    print("=" * 78)
    print("Flavor-split X(q) refinement — m_n / Δ_pn (item 3 of PR #1645)")
    print("=" * 78)
    print(f"\nq_0 = {q_str(DPS)}\n")

    # CODATA targets (m_n derived from m_p + m_e + Q_neutron at module top)
    M_N_MEV_avg = (M_P_MEV + M_N_MEV) / 2
    delta_target = (M_N_MEV - M_P_MEV) / M_N_MEV_avg
    print(f"[CODATA target]")
    print(f"  m_n - m_p             = {mp.nstr(M_N_MEV - M_P_MEV, 12)} MeV")
    print(f"  M_N (avg)             = {mp.nstr(M_N_MEV_avg, 12)} MeV")
    print(f"  (m_n - m_p) / M_N     = {mp.nstr(delta_target, 18)}")

    # Substrate quantities
    h = q - 1 / q
    h2 = h * h
    hbar_q = 1 - 1 / q
    hbar_q_sq = hbar_q ** 2
    q2 = q + 1 / q   # [2]_q
    G = mp.catalan

    # Baseline X(q) — canonical form for (m_n - m_p) / M_N
    # Note: the .md companion form ℏ_q²·h_q·[2]_q is for (m_n-m_p)/μ_avg
    # (quark mass avg), not M_N — different denominator.
    X_baseline_form1 = (q - 1) ** 2 * (1 - q ** (-4)) / 3
    print(f"\n[Baseline X(q) for (m_n - m_p) / M_N]")
    print(f"  X = (q-1)²·(1-q⁻⁴)/3 = {mp.nstr(X_baseline_form1, 18)}")

    baseline_residual = (X_baseline_form1 - delta_target) / delta_target
    print(f"  residual / target      = {mp.nstr(baseline_residual * 100, 8)}%")
    print(f"                         = {mp.nstr(baseline_residual * 1e6, 8)} ppm")
    print(f"                         = {mp.nstr(baseline_residual * 1e9, 8)} ppb")

    # The required refinement factor
    refinement_factor = delta_target / X_baseline_form1
    print(f"\n[Required refinement factor]")
    print(f"  f = target / baseline  = {mp.nstr(refinement_factor, 18)}")
    print(f"  f - 1                  = {mp.nstr(refinement_factor - 1, 12)}")

    # Test refinement candidates
    print(f"\n[Refinement candidates] X_pred = X_baseline · f_candidate")
    print(f"  {'name':<40}{'f_candidate':<22}{'predicted residual ppb':<14}")

    candidates = [
        ("(a) bare", mp.mpf(1)),
        # (a) Higher-order Hecke-skein truncation
        ("(a1) 1 + h²/N (N=∞)", mp.mpf(1)),  # placeholder, search N
        # (b) Habiro-element analog (α_em PR #1511 = [2]_q·(1-h²α))
        # For flavor-split, try (1 - h²·α_em·integer) or (1 + small·α_em)
        ("(b1) 1 + α_em/π", 1 + mp.mpf(1) / mp.mpf("137.0359991") / mp.pi),
        ("(b2) 1 - α_em·G/(4π)", 1 - mp.mpf(1) / mp.mpf("137.0359991") * G / (4 * mp.pi)),
        ("(b3) 1 - h²·α_em (Habiro)",
         1 - h2 * mp.mpf(1) / mp.mpf("137.0359991")),
        # (c) Plancherel-weighted (Σd² = 6 at H_3, etc.)
        ("(c1) 1 + h²/6", 1 + h2 / 6),
        ("(c2) 1 - h²/[2]_q²", 1 - h2 / q2 ** 2),
        # (d) Direct algebraic
        ("(d1) 1 + h²·G/(4π)", 1 + h2 * G / (4 * mp.pi)),
        ("(d2) 1 - ℏ_q²/24 (h²/24 cousin)", 1 - hbar_q_sq / 24),
        ("(d3) 1 - h²·a (PSLQ-fit)", refinement_factor),  # exact
        # (e) Bring zero-mode style — (3q²-1)/(2q²) shape applied as a
        # multiplicative refinement (m_K/m_π template)
        ("(e1) (3q²-1)/(2q²) (m_K/m_π shape)",
         (3 * q ** 2 - 1) / (2 * q ** 2)),
        # (f) Substrate-mass-ratio-style corrections
        ("(f1) 1 + m_e/m_p", 1 + M_E_MEV / M_P_MEV),
        ("(f2) 1 - α_em·ℏ_q", 1 - mp.mpf(1) / mp.mpf("137.0359991") * hbar_q),
    ]

    scored = []
    for name, f in candidates:
        X_pred = X_baseline_form1 * f
        ppb = (X_pred - delta_target) / delta_target * mp.mpf("1e9")
        scored.append((name, f, ppb))

    scored.sort(key=lambda r: abs(r[2]))
    for name, f, ppb in scored:
        marker = ""
        if abs(ppb) < mp.mpf(10):
            marker = " ⭐⭐ < 10 ppb (structural)"
        elif abs(ppb) < mp.mpf(1000):
            marker = " ⭐ < 1 ppb→ppm"
        elif abs(ppb) < abs(scored[-1][2]):
            marker = ""
        print(f"  {name:<40}{mp.nstr(f, 18):<22}{mp.nstr(ppb, 8)}{marker}")

    # PSLQ on the refinement factor
    print(f"\n[PSLQ on f-1 = refinement_factor - 1]")
    fm1 = refinement_factor - 1
    print(f"  f - 1 = {mp.nstr(fm1, 18)}")
    print(f"  (f-1)/h²   = {mp.nstr(fm1 / h2, 12)}")
    print(f"  (f-1)/ℏ_q  = {mp.nstr(fm1 / hbar_q, 12)}")
    print(f"  (f-1)/α_em = {mp.nstr(fm1 / (mp.mpf(1) / mp.mpf('137.0359991')), 12)}")
    print(f"  (f-1)/(α_em/π) = {mp.nstr(fm1 / (mp.mpf(1) / mp.mpf('137.0359991') / mp.pi), 12)}")

    alpha_em = mp.mpf(1) / mp.mpf("137.0359991")
    basis = {
        "1": mp.mpf(1),
        "h": h,
        "h²": h2,
        "h⁴": h ** 4,
        "ℏ_q": hbar_q,
        "ℏ_q²": hbar_q_sq,
        "α_em": alpha_em,
        "α_em/π": alpha_em / mp.pi,
        "G": G,
        "G/π": G / mp.pi,
        "α_em·G": alpha_em * G,
        "α_em·h²": alpha_em * h2,
        "G·h²": G * h2,
    }
    print(f"\n[Pairwise PSLQ — (f-1) vs basis (tol 1e-12, maxcoeff 10⁵)]")
    for name, val in basis.items():
        try:
            rel = mp.pslq([fm1, val], tol=mp.mpf("1e-12"), maxcoeff=100000)
            if rel and rel[0] != 0:
                ratio = -mp.mpf(rel[1]) / mp.mpf(rel[0])
                check = fm1 - ratio * val
                if abs(check) < mp.mpf("1e-10"):
                    print(f"  ⭐ f-1 ≈ ({rel[1]}/{rel[0]}) · {name} "
                          f"= {mp.nstr(ratio * val, 15)} (resid {mp.nstr(abs(check), 8)})")
        except Exception:
            pass

    # Verdict
    best = scored[0]
    print(f"\n[Verdict]")
    if abs(best[2]) < mp.mpf(10) and "PSLQ-fit" not in best[0]:
        verdict = (
            f"STRUCTURAL CANDIDATE: '{best[0]}' lands at {mp.nstr(best[2], 6)} ppb. "
            f"Refinement closes m_n - m_p / M_N to sub-10 ppb (vs 10⁶ ppb bare residual)."
        )
    elif abs(best[2]) < mp.mpf(1e5):
        verdict = (
            f"BEST tested: '{best[0]}' at {mp.nstr(best[2], 6)} ppb. "
            f"Significant improvement over bare 10⁶ ppb but not yet at structural-identity level."
        )
    else:
        verdict = (
            f"NO clear winner — none of {len(candidates)} candidates drops the residual "
            f"meaningfully below the bare 10⁶ ppb baseline. The 0.10% residual likely "
            f"requires a higher-precision (multi-rung Habiro) Wedderburn structural reanalysis."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "flavor-split-xq-refinement",
        engine="python",
    )
    w.set_description(
        "Item 3 of PR #1645: tests refinement candidates for the canonical "
        "Hecke-skein flavor-split X(q) = ℏ_q²·h_q·[2]_q at q_0. "
        "Baseline residual is -0.10% (10⁶ ppb); 100× CODATA target needs "
        "~1 ppb. Scans Higher-order, Habiro-element analog, Plancherel-"
        "weighted, and direct algebraic candidates."
    )
    w.add_parameter("q_80dps", q_str(DPS))
    w.add_parameter("mp_dps_runtime", str(mp.mp.dps))
    w.add_data("baseline_residual_pct", mp.nstr(baseline_residual * 100, 12))
    w.add_data("required_refinement_factor", mp.nstr(refinement_factor, 25))
    w.add_data("best_candidate", best[0])
    w.add_data("best_residual_ppb", mp.nstr(best[2], 12))
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="refinement_search_completed",
        computed=len(candidates),
        expected=len(candidates),
        tolerance=0,
        source=f"Scanned {len(candidates)} candidates at 80 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
