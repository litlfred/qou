#!/usr/bin/env python3
"""
Categorical derivation attempt for α — bottom-up from H_9(q) structure.

Tighter fitted value: α = 339.4 MeV (16-atom panel, residual σ = 0.76).

This is a BOTTOM-UP derivation: NOT pattern-matching α to AME data
(that's the fit), but COMPUTING α from the framework's structures
at the level-3 Wedderburn algebra H_9(q).

The hypothesis: Term 6 lives in the level-3 spectral-sequence
stratum E_∞^(3,*), supported on H_9(q) Wedderburn blocks. The
natural conversion to MeV uses m_e (CAL-0). The numerical
coefficient comes from:

  α = m_e · (some structural factor at H_9(q))

Candidate structural factors enumerated WITHOUT searching against
α:

  S1: m_e · [9]_q!/[6]_q!   (top-three q-int product at H_9)
  S2: m_e · Σ_λ⊢9 dim_q(λ)² (q-Plancherel total weight)
  S3: m_e · [9]_q · z^{-3}  (level-3 prefactor inverse)
  S4: m_e · Σ_λ⊢9 dim_q(λ)  (total q-dimension)

Compute each and report % error vs α_fit. The fit uncertainty
is now ~3% (16 atoms); a categorical match needs to land within
this window.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import q0, z_mark
from enumerate_self_conjugate_partitions import all_self_conjugate_partitions


def q_int(k):
    return float((q0 ** k - q0 ** (-k)) / (q0 - q0 ** (-1)))


def q_fact(k):
    return float(np.prod([q_int(i) for i in range(1, k + 1)]) if k > 0 else 1.0)


def q_dim(lam):
    if not lam:
        return 1.0
    n = sum(lam)
    nfac = q_fact(n)
    rows = len(lam)
    hp = 1.0
    for i in range(rows):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            hp *= q_int(arm + leg + 1)
    return nfac / hp


def all_partitions(n: int) -> list:
    out = []
    def gen(rem, cap, prefix):
        if rem == 0:
            out.append(tuple(prefix)); return
        for k in range(min(cap, rem), 0, -1):
            gen(rem - k, k, prefix + [k])
    gen(n, n, [])
    return out


M_E_MEV = 0.51099895
ALPHA_FIT = 339.4326  # from 16-atom scaling probe
ALPHA_FIT_UNCERT_PCT = 3   # tighter window


def main():
    print("=" * 88)
    print("Categorical derivation attempt for α")
    print("=" * 88)
    print(f"  q_0  = {float(q0):.6f}")
    print(f"  m_e  = {M_E_MEV} MeV")
    print(f"  z    = {float(z_mark):.6f}")
    print()
    print(f"  TARGET (16-atom fit): α = {ALPHA_FIT:.4f} MeV  (~±{ALPHA_FIT_UNCERT_PCT}% uncert)")
    print(f"  Window for 'categorical match': "
          f"{ALPHA_FIT * (1 - ALPHA_FIT_UNCERT_PCT / 100):.1f} – "
          f"{ALPHA_FIT * (1 + ALPHA_FIT_UNCERT_PCT / 100):.1f} MeV")
    print()

    # Pre-compute structural objects at H_9(q)
    parts_9 = all_partitions(9)
    sc_9 = all_self_conjugate_partitions(9)
    dim_q_total = sum(q_dim(lam) ** 2 for lam in parts_9)
    dim_q_sum = sum(q_dim(lam) for lam in parts_9)
    sc_dim_q_total = sum(q_dim(tuple(lam)) ** 2 for lam in sc_9)
    sc_dim_q_sum = sum(q_dim(tuple(lam)) for lam in sc_9)

    print(f"  H_9(q) structural quantities:")
    print(f"    [9]_q!                 = {q_fact(9):.4f}")
    print(f"    [9]_q! / [6]_q!        = {q_fact(9) / q_fact(6):.4f}")
    print(f"    Σ_{{λ⊢9}} dim_q(λ)²    = {dim_q_total:.4f}")
    print(f"    Σ_{{λ⊢9}} dim_q(λ)     = {dim_q_sum:.4f}")
    print(f"    Σ_{{self-conj}} dim_q² = {sc_dim_q_total:.4f}")
    print(f"    z^{-3}                = {1 / float(z_mark) ** 3:.4f}")
    print()

    candidates = []

    def cand(name: str, value: float):
        err = (value - ALPHA_FIT) / ALPHA_FIT * 100
        candidates.append({"name": name, "value": value, "err_pct": err})

    cand("m_e · [9]_q! / [6]_q!",          M_E_MEV * q_fact(9) / q_fact(6))
    cand("m_e · Σ_{λ⊢9} dim_q(λ)²",        M_E_MEV * dim_q_total)
    cand("m_e · Σ_{λ⊢9} dim_q(λ)",         M_E_MEV * dim_q_sum)
    cand("m_e · Σ_{self-conj} dim_q²",     M_E_MEV * sc_dim_q_total)
    cand("m_e · [9]_q · z^{-3}",
         M_E_MEV * q_int(9) * (1 / float(z_mark) ** 3))
    cand("m_e · [9]_q!/[6]_q! · z^{-3}",
         M_E_MEV * (q_fact(9) / q_fact(6)) * (1 / float(z_mark) ** 3))
    cand("m_e · Σ dim_q² / [9]_q!",
         M_E_MEV * dim_q_total / q_fact(9))
    cand("m_e · [7]_q · [8]_q · [9]_q",
         M_E_MEV * q_int(7) * q_int(8) * q_int(9))
    cand("m_e · [9]_q²",                   M_E_MEV * q_int(9) ** 2)
    cand("m_e · [9]_q! · z^3 / [3]_q!^3",
         M_E_MEV * q_fact(9) * float(z_mark) ** 3 / q_fact(3) ** 3)

    candidates.sort(key=lambda c: abs(c["err_pct"]))
    print(f"  {'expression':<48} {'value (MeV)':>12} {'% err':>10}")
    print("  " + "-" * 76)
    for c in candidates:
        marker = "★" if abs(c["err_pct"]) < ALPHA_FIT_UNCERT_PCT else (
            "✓" if abs(c["err_pct"]) < 10 else " ")
        print(f"  {marker} {c['name']:<46} {c['value']:>12.4f} "
              f"{c['err_pct']:>+10.4f}")

    in_window = [c for c in candidates
                  if abs(c["err_pct"]) < ALPHA_FIT_UNCERT_PCT]
    print()
    if in_window:
        print(f"  {len(in_window)} expression(s) within ±{ALPHA_FIT_UNCERT_PCT}% fit window:")
        for c in in_window:
            print(f"    {c['name']}: {c['value']:.4f} MeV ({c['err_pct']:+.2f}%)")
    else:
        print(f"  NO expression matches within ±{ALPHA_FIT_UNCERT_PCT}% window.")
        print(f"  α = 339.4 MeV is NOT cleanly derivable from these candidate structures.")

    print()
    print(f"  HONEST CONCLUSION:")
    if in_window and len(in_window) == 1:
        print(f"    Single match within window: {in_window[0]['name']}.")
        print(f"    But: still pattern-search across many candidates;")
        print(f"    a true derivation would PRODUCE this expression from the framework,")
        print(f"    not select it post-hoc.")
    elif in_window:
        print(f"    Multiple matches → search-space-narrow but inconclusive.")
        print(f"    Tighter fit (more atoms) and/or first-principles derivation needed.")
    else:
        print(f"    No clean match. α remains an empirical parameter.")
        print(f"    The Term6/A³ shape is structurally derived; α is calibrated.")

    out = {
        "computation": "alpha-categorical-derivation-attempt",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "alpha_fit_MeV": ALPHA_FIT,
        "fit_uncert_pct": ALPHA_FIT_UNCERT_PCT,
        "structural_quantities": {
            "q_fact_9":      q_fact(9),
            "q_fact_9_over_6": q_fact(9) / q_fact(6),
            "dim_q_total":   dim_q_total,
            "dim_q_sum":     dim_q_sum,
            "sc_dim_q_total": sc_dim_q_total,
            "z_minus_3":     1 / float(z_mark) ** 3,
        },
        "candidates": candidates,
        "in_window": in_window,
        "interpretation": (
            "Candidate categorical expressions for α from H_9(q) "
            "structures. Search bottom-up (compute candidates from "
            "framework objects, then check vs fit) — but this is "
            "STILL pattern matching. A real derivation would predict "
            "α before the fit, not select among many candidates."
        ),
    }
    p_out = (Path(__file__).parent.parent.parent
             / "docs/audits/2026-05-02-alpha-categorical-derivation.witness.json")
    p_out.write_text(json.dumps(out, indent=2, default=str))
    print()
    print(f"Witness: {p_out.relative_to(Path(__file__).parent.parent.parent)}")


if __name__ == "__main__":
    main()
