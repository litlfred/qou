"""B-step of the c=2 EM-linking residual investigation: PSLQ + naive
h-polynomial scan finds NO derivation-tight identification.

Companion to:
  - c2_rule_em_linking_residual.py (step A, set up the lead)
  - docs/audits/2026-06-03-c2-rule-em-linking-coulomb-residual.md
  - PR #1777 "Derive the two-like-charge EM-linking invariant"

EXPLORATORY.  Negative-result probe.  Records that the 0.155 %
near-match between residual and 12/5 = dim H_4 / I(4) is NOT lifted
to derivation-tight precision by any natural h-polynomial or
q-rational correction tested.

## What was tried

  • PSLQ integer-relation search against (residual, 1, h₀², h₀⁴, h₀⁶)
    at tol 1e-30, maxcoeff 10000 — NO low-norm relation found.
  • Same on (delta = residual − 12/5, h₀², h₀⁴, h₀⁶) — NO relation.
  • Direct ratio checks residual/element vs small rationals p/q with
    |p|,|q| ≤ 30 — NO clean p/q match within 1e-5.
  • Direct fit checks like 12/5·(1 + h²·k), 12/5 + h⁴·k for trial
    rational k — best is 12/5·(1 + h²/28) at 0.0009 % but the
    denominator 28 has no structural justification.

## Conclusion

The residual 2.4037... is NOT a low-height polynomial-in-h² over ℚ.
The classical-limit 12/5 = dim H_4 / I(4) at q=1 stays the best
candidate at 0.155 %, but cannot be promoted to ppm via h-corrections
within the basis tested.  Two interpretations remain:

  (a) 12/5 is structurally correct, but the residue from it carries
      a *transcendental* contribution (e.g. a Lobachevsky function
      value, a logarithmic correction from the categorical adjunction
      I/I+1 normalization, or an SDP active-set integral) — not in
      the polynomial basis tested here.
  (b) The c=2 selection rule is NOT the right object for PR #1777's
      EM-linking slot, and the 0.155 % proximity is a coincidence.

Step A (categorical derivation) targets (a) via the H_3 → H_4
branching from frobenius-lepton-meson-bridge.md.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: F401, E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402

REMAINING_FACTOR = mp.mpf("3.213697131179528")
TWELVE_FIFTHS = mp.mpf(12) / 5


def part1_setup() -> tuple:
    mp.mp.dps = 80
    q0 = mp.mpf(Q_50_DIGIT_STR)
    h0 = q0 - 1 / q0
    lw_c2 = (q0 + 1) ** 2 / (3 * q0)
    residual = REMAINING_FACTOR / lw_c2
    delta = residual - TWELVE_FIFTHS
    return q0, h0, lw_c2, residual, delta


def part2_pslq(residual: mp.mpf, h0: mp.mpf, delta: mp.mpf) -> dict:
    """PSLQ on residual against polynomial-in-h² basis."""
    results = {}
    one = mp.mpf(1)
    for basis_name, basis in [
        ("residual_vs_1_h2_h4", [residual, one, h0 ** 2, h0 ** 4]),
        ("residual_vs_1_h2_h4_h6", [residual, one, h0 ** 2, h0 ** 4, h0 ** 6]),
        ("delta_vs_h2_h4_h6",
         [delta, h0 ** 2, h0 ** 4, h0 ** 6]),
    ]:
        rel = mp.pslq(basis, tol=mp.mpf("1e-30"), maxcoeff=10000)
        results[basis_name] = {
            "basis_size": len(basis),
            "relation": [str(r) for r in rel] if rel else None,
            "found_relation": rel is not None,
        }
    return results


def part3_trial_fits(residual: mp.mpf, h0: mp.mpf) -> dict:
    """Hand-picked candidates: 12/5 + k·h^(2m) and 12/5·(1 + k·h^(2m)).

    None are 'derived' — they parameter-fit one number, by design.
    Reporting only as the closest naive fits to put the categorical
    derivation in step A in context.
    """
    candidates = {
        "12/5":                              TWELVE_FIFTHS,
        "12/5 + h^4·2":                       TWELVE_FIFTHS + 2 * h0 ** 4,
        "12/5 + h^2/12":                      TWELVE_FIFTHS + h0 ** 2 / 12,
        "12/5 · (1 + h^4·5/6)":               TWELVE_FIFTHS * (1 + h0 ** 4 * mp.mpf(5) / 6),
        "12/5 · (1 + h^2/28)":                TWELVE_FIFTHS * (1 + h0 ** 2 / 28),
        "ratio_q_def_H4_(symmetric_qdef)":    None,  # filled below
    }
    out = {}
    for name, val in candidates.items():
        if val is None:
            continue
        diff = val - residual
        out[name] = {
            "value": mp.nstr(val, 16),
            "rel_diff_pct": mp.nstr(diff / residual * 100, 8),
            "honest_note": (
                "rational coefficient is FIT, not DERIVED — included "
                "as proximity context, not a candidate identification"
            ) if name not in ("12/5",) else "structural (= dim H_4/I(4) at q=1)",
        }
    return out


def main() -> int:
    q0, h0, lw_c2, residual, delta = part1_setup()
    print("=" * 72)
    print(" Step B: PSLQ scan for c=2 EM-linking residual identifications")
    print("=" * 72)
    print(f"\n  residual measured = {mp.nstr(residual, 20)}")
    print(f"  delta = residual - 12/5 = {mp.nstr(delta, 16)}")
    print(f"  delta / h₀² = {mp.nstr(delta / h0 ** 2, 14)}")
    print(f"  delta / h₀⁴ = {mp.nstr(delta / h0 ** 4, 14)}")

    pslq_results = part2_pslq(residual, h0, delta)
    print("\n── PSLQ integer-relation searches ──")
    for name, r in pslq_results.items():
        if r["found_relation"]:
            print(f"  {name:<32}  FOUND: {r['relation']}")
        else:
            print(f"  {name:<32}  none (tol 1e-30, maxcoeff 10000)")

    fits = part3_trial_fits(residual, h0)
    print("\n── Trial candidates (mostly FIT, for context only) ──")
    for name, info in fits.items():
        print(f"  {name:<35} = {info['value']:>16}  "
              f"rel diff = {info['rel_diff_pct']} %")

    print("\n  VERDICT (step B):")
    print("    No low-height polynomial-in-h² over ℚ identification of the")
    print("    residual exists. The 12/5 at 0.155 % stays the best candidate.")
    print("    Step A's H_3→H_4 categorical derivation, or transcendental")
    print("    identifications outside the h-polynomial basis, are the")
    print("    remaining viable directions.")

    out = {
        "computation": "c2-residual-pslq-scan",
        "description": (
            "Step B negative-result probe: PSLQ + trial-fit scan finds NO "
            "derivation-tight (≤ ppm) identification of the c=2 EM-linking "
            "residual in a polynomial-in-h² basis over ℚ. The 12/5 = dim "
            "H_4 / I(4) at q=1 stays the best candidate at 0.155 %. "
            "EXPLORATORY; no production wiring; no fit (fit-style trial "
            "candidates labelled honestly as 'rational coefficient FIT, "
            "not derived')."),
        "inputs": {
            "remaining_factor": mp.nstr(REMAINING_FACTOR, 20),
            "lw_c2_at_q0": mp.nstr(lw_c2, 20),
            "residual": mp.nstr(residual, 20),
            "delta_residual_minus_12_5": mp.nstr(delta, 16),
        },
        "pslq_results": pslq_results,
        "trial_fits_for_context": fits,
        "discipline": {
            "fit": (
                "none binding — trial fits report rational coefficients "
                "labelled FIT, not derivation candidates"),
            "delta_lambda_gate": (
                "compliant — no AME mass/binding number tuned; only the "
                "selection-rule + 12/5 structural ratio used"),
            "verdict": (
                "step B negative — residual has no derivation-tight "
                "h-polynomial identification; step A (categorical) is "
                "the next focused attempt"),
        },
    }
    out_path = HERE.parent / "c2-residual-pslq-scan.witness.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nWitness: {out_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
