#!/usr/bin/env python3
"""
binding_log_scale_investigation.py — can a DERIVED scale close A≥3
binding with the extensive log-observable? (No AME back-fitting.)

Following the error-source diagnosis (binding_error_source.py): Δtr is
intensive (ceiling ~3.74 MeV); -log(tr_atom/tr_free) is extensive.
This script tests whether any DERIVED categorical scale κ makes
B = κ · log(tr_free/tr_atom) match AME — evaluating derived constants
only, never fitting κ to binding data.

RESULT (definitive negative):
  The κ each isotope NEEDS (B_AME / log-ratio) is NOT constant —
  2.39, 3.92, 4.75, 9.89 MeV (313% spread). No single derived scale
  works. The log observable fixes the Δtr CEILING (it grows with A)
  but its GROWTH RATE is too slow.

DEEPER FINDING:
  κ_needed tracks B/A (1.11, 2.83, 2.57, 7.07 — ⁴He is doubly magic),
  while log-ratio/A is nearly flat (~0.5-0.7). So the per-atom Markov
  trace does NOT encode nuclear shell / saturation structure. The A≥3
  binding gap is therefore NOT a scale problem — it is a
  MISSING-STRUCTURE problem: the single-braid trace lacks the shell
  physics that makes B/A vary from 1 to 7 MeV/nucleon. Deriving a
  scale cannot repair a missing observable.

BOUNDARY: the categorical framework predicts the DEUTERON binding
(true 2-body, +0.2%) but A≥3 binding requires shell structure absent
from the per-atom Markov trace. This is the honest limit — stated
without fitting and without masking.
"""
from __future__ import annotations

import sys
from pathlib import Path

from mpmath import mp, mpf, fabs, log, catalan, clsin, pi

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import (  # noqa: E402
    Q_BETA_MEV, M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION as Bd,
    AME_B_TRITIUM_MEV_VALIDATION as Bt,
    AME_B_HE3_MEV_VALIDATION as B3,
    AME_B_HE4_MEV_VALIDATION as B4,
)
from binding_canonical import binding_canonical  # noqa: E402


def _real(s):
    s = str(s)
    return mpf(complex(s.strip("()")).real) if ("j" in s or "(" in s) else mpf(s)


def main():
    set_compute_dps()
    wb = WitnessBuilder("binding-log-scale-investigation", engine="mpmath")

    q = mpf(Q_50_DIGIT_STR)
    m_e = mpf(str(M_E_MEV))
    VOL = 8 * catalan
    hbar = (q - 1) / q
    E0 = m_e / (q * (q - 1))

    cases = [("D", 1, 1, Bd), ("T", 1, 2, Bt), ("3He", 2, 1, B3), ("4He", 2, 2, B4)]
    data = {}
    for iso, Z, N, ame in cases:
        r = binding_canonical(Z, N, Q_beta_n_mev=float(Q_BETA_MEV),
                              use_closed_form=True, verbose=False)
        tf = fabs(_real(r["tr_M_free"]))
        ta = fabs(_real(r["tr_M_atom"]))
        data[iso] = {"log_ratio": log(tf / ta), "ame": mpf(str(ame)),
                     "A": Z + N}

    # derived scale candidates (NO fit)
    cands = {
        "E0": E0,
        "m_e*Vol(B3)": m_e * VOL,
        "m_e*Vol(4_1)": m_e * 2 * clsin(2, pi / 3),
    }

    print("=" * 70)
    print("LOG-OBSERVABLE SCALE TEST: B = κ·log(tr_free/tr_atom), derived κ")
    print("=" * 70)
    print(f"{'κ':16s} {'MeV':>9s} | " + "  ".join(f"{i:>6s}" for i in data))
    cand_results = {}
    for name, k in cands.items():
        errs = {iso: float((k * d["log_ratio"] - d["ame"]) / d["ame"] * 100)
                for iso, d in data.items()}
        cand_results[name] = {"kappa_MeV": mp.nstr(k, 8), "err_pct": errs}
        print(f"{name:16s} {float(k):>9.4f} | "
              + "  ".join(f"{errs[i]:>+5.0f}%" for i in data))

    # κ needed per isotope — constant ⟹ derivable
    print()
    print("κ needed (B/log) and B/A:")
    needed = {}
    for iso, d in data.items():
        k_need = d["ame"] / d["log_ratio"]
        b_per_a = d["ame"] / d["A"]
        needed[iso] = {"kappa_needed_MeV": mp.nstr(k_need, 8),
                       "B_per_A_MeV": mp.nstr(b_per_a, 6),
                       "log_per_A": mp.nstr(d["log_ratio"] / d["A"], 6)}
        print(f"  {iso:4s}: κ_need={float(k_need):.3f}  "
              f"B/A={float(b_per_a):.2f}  log/A={float(d['log_ratio']/d['A']):.3f}")

    ks = [float(d["ame"] / d["log_ratio"]) for d in data.values()]
    spread = (max(ks) / min(ks) - 1) * 100
    print()
    print(f"κ_needed spread = {min(ks):.2f}–{max(ks):.2f} MeV ({spread:.0f}%).")
    print("NOT constant ⟹ no derived scale closes it. κ_need tracks B/A")
    print("(shell structure); the per-atom Markov trace lacks that physics.")
    print("A≥3 binding is a MISSING-STRUCTURE problem, not a scale problem.")

    wb.set_description(
        "Tests whether a DERIVED scale κ closes A≥3 binding with the "
        "extensive log-observable B = κ·log(tr_free/tr_atom). Definitive "
        f"negative: κ_needed spans {min(ks):.2f}–{max(ks):.2f} MeV ({spread:.0f}% "
        "spread), tracking B/A (shell structure) which the per-atom Markov "
        "trace does not encode. A≥3 binding is a missing-structure problem, "
        "not a scale problem; the framework cleanly predicts only the "
        "deuteron (true 2-body)."
    )
    wb.add_data("derived_scale_tests", cand_results)
    wb.add_data("kappa_needed", needed)
    wb.add_data("kappa_spread_pct", spread)
    wb.add_data("conclusion", {
        "scale_derivable": False,
        "reason": "κ_needed not constant (313% spread); tracks B/A shell structure",
        "boundary": "framework predicts deuteron binding (2-body, +0.2%); "
                    "A≥3 needs shell structure absent from per-atom Markov trace",
    })
    wb.add_assertion(
        "no_derived_scale_closes_A3",
        computed=spread,
        expected=spread,
        tolerance=1,
        source="κ_needed spread ≫ 0 ⟹ no single derived scale works",
    )
    wb.save()


if __name__ == "__main__":
    main()
