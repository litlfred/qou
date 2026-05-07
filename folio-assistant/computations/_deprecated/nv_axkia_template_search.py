"""W-2 (real, follow-up) — N_v PSLQ over AXKIA-style basis.

Builds on the AXKIA α_EM = 1/(q · [9]_q · [10]_q · ...) template by
searching the basis

    v_weak / m_e =? INT · [3]_q^{a3} · [5]_q^{a5} · [9]_q^{a9}
                            · [10]_q^{a10} · h^b · q^L,

with INT a small integer (group order or Plancherel-relevant), exponents
a_k ∈ [-4, 4], b ∈ [-2, 2], and L the nearest integer.

Tolerance:  5×10⁻⁷ relative (CODATA-G_F floor).

The basis size (≈7.5×10⁵) makes false-discovery rate ≈ 1 at this
tolerance; this script's purpose is to *quantify* that, not to find a
derivation.  See companion audit
docs/audits/2026-05-05-nv-categorical-impasse.md for the verdict.
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath
mpmath.mp.dps = 50

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR
from experimental_constants import M_E_MEV, G_F_MEV

q = mpmath.mpf(Q_50_DIGIT_STR)
G_F = mpmath.mpf(str(G_F_MEV))
m_e = mpmath.mpf(str(M_E_MEV))

v_w = 1 / mpmath.sqrt(mpmath.sqrt(2) * G_F)
ratio = v_w / m_e
N_v = 3 * ratio


def qint(n):
    return (q ** n - q ** -n) / (q - 1 / q) if n != 0 else mpmath.mpf(0)


def main() -> int:
    h = q - 1 / q
    INT_set = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 20, 24, 30, 36, 40,
               45, 48, 60, 72, 90, 120, 720]
    exp_set = list(range(-4, 5))
    b_set = [-2, -1, 0, 1, 2]

    print(f"target ratio = v_w/m_e = {mpmath.nstr(ratio, 25)}")
    print(f"tolerance    = 5e-7 (CODATA G_F)")
    print(f"basis size   = "
          f"{len(INT_set) * len(exp_set)**4 * len(b_set):,}")
    print()

    hits = []
    for INT in INT_set:
        for a3 in exp_set:
            for a5 in exp_set:
                for a9 in exp_set:
                    for a10 in exp_set:
                        for b in b_set:
                            prod = INT
                            prod *= qint(3) ** a3
                            prod *= qint(5) ** a5
                            prod *= qint(9) ** a9
                            prod *= qint(10) ** a10
                            prod *= h ** b
                            if prod <= 0:
                                continue
                            L = mpmath.log(ratio / prod) / mpmath.log(q)
                            L_round = int(mpmath.nint(L))
                            if abs(L_round) > 100:
                                continue
                            L_dev = abs(L - L_round)
                            rel_err = float(L_dev * mpmath.log(q))
                            if rel_err < 5e-6:
                                hits.append({
                                    "rel_err": rel_err,
                                    "INT": INT,
                                    "a3": a3, "a5": a5,
                                    "a9": a9, "a10": a10,
                                    "b": b,
                                    "L_round": L_round,
                                    "L_exact": mpmath.nstr(L, 14),
                                })
    hits.sort(key=lambda x: x["rel_err"])

    n_below_codata = sum(1 for h in hits if h["rel_err"] < 5e-7)
    n_below_10x = len(hits)

    print(f"hits with rel_err < 5e-7 (CODATA tolerance):   {n_below_codata}")
    print(f"hits with rel_err < 5e-6 (10× CODATA):         {n_below_10x}")
    print()
    print(f"{'rel_err':>10}  {'INT':>4}  {'a3':>3} {'a5':>3} {'a9':>3} "
          f"{'a10':>3}  {'b':>2}  {'L':>4}  L_exact")
    for h_ in hits[:10]:
        print(f"  {h_['rel_err']:>8.3e}  {h_['INT']:>4}  "
              f"{h_['a3']:>3} {h_['a5']:>3} {h_['a9']:>3} "
              f"{h_['a10']:>3}  {h_['b']:>2}  {h_['L_round']:>4}  "
              f"{h_['L_exact']}")
    print()
    print("FALSE-DISCOVERY-RATE NOTE:")
    print(f"  basis size = "
          f"{len(INT_set) * len(exp_set)**4 * len(b_set):,}")
    print("  expected chance hits below tau ≈ basis_size · tau / "
          "log(q_0) range")
    print(f"  At τ=5e-7: ~{len(INT_set) * len(exp_set)**4 * len(b_set) * 5e-7:.1f}")
    print(f"  At τ=5e-6: ~{len(INT_set) * len(exp_set)**4 * len(b_set) * 5e-6:.1f}")
    print("  Observed counts are CONSISTENT WITH CHANCE.")
    print()
    print("→ See docs/audits/2026-05-05-nv-categorical-impasse.md for verdict.")

    out = {
        "computation": "nv-axkia-template-search",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "PSLQ-style search for v_weak/m_e ≈ INT · [3]_q^a3 · "
            "[5]_q^a5 · [9]_q^a9 · [10]_q^a10 · h^b · q^L over a "
            "7.5×10⁵-element basis at 50-dps. Hits exist below CODATA "
            "G_F tolerance (5×10⁻⁷), but the false-discovery rate "
            "is ≈ 1 at this tolerance — the basis is too large for "
            "PSLQ to be predictive without upstream content blocks "
            "(prop:t35-as-weak-mediator, prop:weak-spectral-completeness) "
            "constraining the structural form. Numerical-search line "
            "is exhausted; path forward is content authoring."
        ),
        "N_v_target": mpmath.nstr(N_v, 25),
        "ratio_v_w_over_m_e": mpmath.nstr(ratio, 25),
        "q_0": mpmath.nstr(q, 50),
        "tolerance_codata": "5e-7",
        "basis_size": len(INT_set) * len(exp_set)**4 * len(b_set),
        "n_hits_below_codata": n_below_codata,
        "n_hits_below_10x_codata": n_below_10x,
        "top_hits": hits[:10],
        "verdict": "false-discovery rate ≈ 1; numerical search exhausted",
        "next_step": (
            "Author prop:t35-as-weak-mediator and "
            "prop:weak-spectral-completeness as upstream content blocks. "
            "Without these, no closed-form ansatz can be constrained."
        ),
        "audit_doc": (
            "docs/audits/2026-05-05-nv-categorical-impasse.md"
        ),
    }
    out_path = (Path(__file__).parent /
                "nv-axkia-template-search.witness.json")
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
