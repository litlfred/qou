#!/usr/bin/env python3
"""
Test the corrected Kashaev limit Li_2^q(-V) in the 6-term mass formula.

Per the kashaev-integration-identity probe, the Briggs-Klein integration

  ∫_0^V (ln_q(1+t)/t) dt = -Li_2^q(-V)   (q-deformed dilogarithm)

is NOT Φ_q(V) and NOT α·ln|V| — it's the q-deformed dilogarithm.

This probe replaces T2 = Σ_i Φ_q(|V̂_i|) with the corrected form

  T2_corrected = Σ_i (-Li_2^q(-|V̂_i|))

using the actual integration value.  Tests whether this restores
both Markov-invariance AND empirical accuracy.

Compares three forms:
  - brane:        T2 = Σ Φ_q(|V_i|)   (legacy, gives -737 MeV pathology)
  - paper:        M = const + α·Σ ln|V_i|  (atomic-braid-mass; 0.19% works)
  - li2q-corrected: T2 = Σ (-Li_2^q(-|V_i|))  (actual Kashaev integration)

If li2q-corrected matches paper-formula in accuracy: confirms both
derivations resolve to the same numerical answer via Li_2^q.

If li2q-corrected fails: shows atomic-braid-mass's α·Σ ln|V| is a
distinct heuristic, not the Kashaev specialisation result, and a
different reconciliation is needed.

Output: li2q-six-term-probe.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from q_parameter import Q as Q0_FLOAT, Q_MP  # noqa: E402
from hecke_core import (  # noqa: E402
    atom_per_generator_volumes, h as h_val, z as z_mark,
)

Q0 = Q_MP
M_E_MEV = 0.51099895
M_P_MEV = 938.27208816
M_N_MEV = 939.56542052
G_CATALAN = float(mp.catalan)
ALPHA = M_E_MEV * 8 * G_CATALAN  # m_e · 8G ≈ 3.7445 MeV


def q_integer(n: int, q: mp.mpf = Q0) -> mp.mpf:
    """[n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    if n == 0:
        return mp.mpf(0)
    if abs(q - 1) < mp.mpf("1e-30"):
        return mp.mpf(n)
    return (q ** n - q ** (-n)) / (q - 1 / q)


def ln_q_series(x: mp.mpf, q: mp.mpf = Q0, max_n: int = 200) -> mp.mpf:
    """ln_q(1 + t) = Σ_{n≥1} (-1)^(n+1) t^n / [n]_q,  x = 1 + t."""
    t = x - 1
    if abs(t) >= 1:
        return mp.mpf("nan")
    total = mp.mpf(0)
    for n in range(1, max_n + 1):
        qint_n = q_integer(n, q)
        if abs(qint_n) < mp.mpf("1e-300"):
            continue
        term = (-1) ** (n + 1) * t ** n / qint_n
        total += term
        if abs(term) < mp.mpf("1e-40"):
            break
    return total


def kashaev_integration(V: mp.mpf, q: mp.mpf = Q0) -> mp.mpf:
    """∫_0^V (ln_q(1+t)/t) dt = -Li_2^q(-V) (q-dilogarithm)."""
    def integrand(t):
        if abs(t) < mp.mpf("1e-50"):
            return mp.mpf(1)  # limit ln_q(1+t)/t → 1 as t → 0
        return ln_q_series(1 + mp.mpf(t), q) / mp.mpf(t)
    return mp.quad(integrand, [0, V])


def predict_atom_three_forms(Z: int, N: int) -> dict:
    """Compute M_pred under three alternatives for the brane tower."""
    constituent = Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV

    vols = atom_per_generator_volumes(Z, N, include_inter=(Z + N >= 2))
    abs_vols = []
    for v in vols:
        x = v["full"] if isinstance(v, dict) else v
        abs_vols.append(abs(mp.mpf(x)))

    # Form 1 (paper-formula working form): correction = α · Σ ln|V_i|
    sum_log = sum(mp.log(v) for v in abs_vols if v > 0)
    correction_paper = float(ALPHA) * float(sum_log)

    # Form 3 (li2q-corrected): correction = α · Σ (-Li_2^q(-|V_i|))
    sum_li2q = mp.mpf(0)
    li2q_vals = []
    for v in abs_vols:
        if v >= 1:
            # Series diverges at |V| = 1; clip slightly inside radius
            v_eff = mp.mpf("0.99999")
        else:
            v_eff = v
        try:
            li_val = -kashaev_integration(v_eff)
            # NOTE: Li_2^q(-V) = -∫... so -Li_2^q(-V) = ∫... = positive
            # Wait: ∫ = -Li_2^q(-V), so -Li_2^q(-V) IS the integral itself.
            # Use the integral value directly (positive for V ∈ (0, 1)).
            li_val = kashaev_integration(v_eff)  # = -Li_2^q(-V) = positive
            sum_li2q += li_val
            li2q_vals.append(float(li_val))
        except Exception:
            li2q_vals.append(None)
    correction_li2q = float(ALPHA) * float(sum_li2q)

    # Predictions
    M_paper = constituent + correction_paper
    M_li2q  = constituent - correction_li2q  # binding subtracts from free constituent

    return {
        "Z": Z, "N": N, "A": Z + N,
        "constituent_MeV": constituent,
        "abs_vols_per_gen": [float(v) for v in abs_vols],
        "sum_log_V": float(sum_log),
        "sum_li2q": float(sum_li2q),
        "correction_paper_MeV": correction_paper,
        "correction_li2q_MeV": correction_li2q,
        "M_pred_paper": M_paper,
        "M_pred_li2q_subtract": M_li2q,
        "M_pred_li2q_add": constituent + correction_li2q,
        "li2q_per_gen": li2q_vals,
    }


# AME data
ATOMS = [
    ("p",   1, 0,    938.78308711),
    ("n",   0, 1,    939.56542052),
    ("D",   1, 1,   1876.12393),
    ("T",   1, 2,   2809.43215),
    ("3He", 2, 1,   2809.41347),
    ("4He", 2, 2,   3728.40133),
]


def main() -> int:
    print("=" * 100)
    print("  Li_2^q corrected Kashaev limit — does it reproduce atomic-braid-mass?")
    print(f"  q_0 = {float(Q0):.10f},  α = m_e · 8G = {ALPHA:.6f} MeV")
    print("=" * 100)

    print(f"\n  {'atom':<6} {'A':>3} {'n_gen':>5}  "
          f"{'Σ ln|V|':>10}  {'α·Σ ln|V|':>12}  "
          f"{'Σ -Li_2^q':>11}  {'α·Σ Li_2^q':>13}")
    print("  " + "-" * 80)
    rows = []
    for label, Z, N, M_AME in ATOMS:
        try:
            r = predict_atom_three_forms(Z, N)
        except Exception as exc:
            print(f"  {label:<6}: ERROR {type(exc).__name__}: {exc}")
            continue
        print(f"  {label:<6} {Z+N:>3} {len(r['abs_vols_per_gen']):>5}  "
              f"{r['sum_log_V']:>+10.4f}  {r['correction_paper_MeV']:>+12.4f}  "
              f"{r['sum_li2q']:>+11.4f}  {r['correction_li2q_MeV']:>+13.4f}")
        # Compare predictions
        m_paper_err = (r["M_pred_paper"] - M_AME) / M_AME * 100
        m_li2q_sub_err = (r["M_pred_li2q_subtract"] - M_AME) / M_AME * 100
        m_li2q_add_err = (r["M_pred_li2q_add"] - M_AME) / M_AME * 100
        rows.append({
            "atom": label, **r, "M_AME_MeV": M_AME,
            "err_paper_pct": m_paper_err,
            "err_li2q_subtract_pct": m_li2q_sub_err,
            "err_li2q_add_pct": m_li2q_add_err,
        })

    # Summary
    print("\n  Mass predictions (% error vs CODATA):")
    print(f"  {'atom':<6}  {'paper':>10}  {'li2q (-)':>10}  {'li2q (+)':>10}")
    print("  " + "-" * 50)
    for r in rows:
        print(f"  {r['atom']:<6}  {r['err_paper_pct']:>+9.4f}%  "
              f"{r['err_li2q_subtract_pct']:>+9.4f}%  "
              f"{r['err_li2q_add_pct']:>+9.4f}%")

    # Stats on T, 3He, 4He
    pred_rows = [r for r in rows if r["atom"] not in ("p", "n", "D")]
    if pred_rows:
        for label, key in [("paper", "err_paper_pct"),
                            ("li2q (-)", "err_li2q_subtract_pct"),
                            ("li2q (+)", "err_li2q_add_pct")]:
            errs = [abs(r[key]) for r in pred_rows]
            print(f"\n  {label:<10}: mean |M_err| = {sum(errs)/len(errs):.4f}%, "
                  f"max = {max(errs):.4f}%")

    # Verdict
    print("\n  Verdict:")
    print("    paper (α·Σ ln|V|) is the working empirical form.")
    print("    li2q (-Li_2^q(-V)) is the literal Kashaev integration.")
    print("    If they match in accuracy: the two derivations are consistent.")
    print("    If they differ substantially: paper's α·ln|V| is a distinct")
    print("    heuristic that doesn't come from the literal integration.")

    witness = {
        "computation": "li2q-six-term-probe",
        "description": (
            "Tests whether the corrected Kashaev integration value "
            "(-Li_2^q(-V), the q-dilogarithm) reproduces atomic-braid-mass's "
            "successful α·Σ ln|V_i| form when used in the 6-term framework. "
            "Resolves the question of whether prop:atomic-braid-mass and "
            "prop:mass-endomorphism-tower are consistent derivations under "
            "the corrected Kashaev limit."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "alpha_MeV": ALPHA,
        "rows": rows,
    }
    out = HERE / "li2q-six-term-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
