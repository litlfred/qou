#!/usr/bin/env python3
"""qbeta_ck_truncation_order_analysis.py — canonical reference for the
Q_β precision-ladder as a TRUNCATION ORDER of a convergent series.

PURPOSE (stop the four-session flip-flop).

The Q_β categorical precision ladder
    Q_β(q) = Q_base · Π_{k≥2} (1 + c_k · u^k),   u = b·ℏ_q²
has been repeatedly wired (#1452) and un-wired (#1479) at k≥3 because
two facts were conflated:

  FACT A (wiring camp):    N=3 DOES beat the experimental 100× target
                           (residual 6.0 ppb < 7.8 ppb target).
  FACT B (discipline camp): c_3 = -2 is NOT a Taylor-EXACT derivation
                           (it is a q₀-dependent near-match: -2.0097
                           at muon-pin q₀, -2.0693 at m_p-pin q₀ — a
                           3.47% m_p-pin swing, 2.98% cross-anchor
                           swing — see Part D computed values).

BOTH ARE TRUE. The flip-flop comes from treating "wire c_k?" as a
binary decision instead of recognising:

  1. N is a TRUNCATION ORDER chosen by target precision (this script's
     N(ε) formula), NOT a yes/no canonicity gate.
  2. The c_k are the Taylor coefficients of a Q_β Habiro element. Until
     that element is identified (cf. the α_EM Habiro element
     [2]_q·(1-h²α), PR #1511), the c_k for k≥3 are NEAR-MATCHES with a
     precision floor — they cannot be credited as derivations, but the
     truncated series still beats the EXPERIMENTAL target at N=3.
  3. Honest reporting is TIERED (proved / near-match / fitted), not
     binary wired/dropped.

WHAT THIS SCRIPT ESTABLISHES (pinned in the witness):

  Part A. The ladder step u = b·ℏ_q² ≈ 0.00852, so 1/u ≈ 117 and each
          rung gains log10(1/u) ≈ 2.07 decimal digits.

  Part B. N(ε) formula:  N ≥ log10(1/ε)/2.07 − 1.  Tabulated for the
          100× target, 1 ppb, 1 ppt, 1 ppQ.

  Part C. Per-rung term sizes |c_k·u^k| and cumulative residual vs the
          CODATA Q_AME central value.

  Part D. FLOOR DIAGNOSIS — the q₀-stability test. The true Taylor
          coefficient of a convergent series is q₀-anchor-independent.
          The c_k near-matches swing across q₀ anchors; the script
          quantifies the swing and shows the N=4→N=5 non-monotonicity
          (the experimental signature that c_k≥3 are near-matches, not
          exact).

  Part E. The Habiro fix — the resolution is to identify the Q_β Habiro
          element so the c_k become exact (parallel α_EM PR #1511); the
          truncated series then converges monotonically and N(ε) is
          rigorous to arbitrary precision.

NO FITTING. The c_k used are the framework's stated canonical forms
(c_2=-1 PROVED, c_3=J_Hopf(q=1)=-2, c_4=c_3·b⁴, c_5=c_3²·3+b); the
analysis quantifies their near-match status honestly — it does not
tune them.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
import time
from pathlib import Path

import mpmath as mp
from mpmath import mpf, log10, ceil

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402


def load_q_data():
    import json
    # Witness lives in parent computations/ dir (path drift from Phase 4
    # qbeta/ subdir refactor).
    with open(HERE.parent / "q-beta-operator-valued-N3.witness.json",
              encoding="utf-8") as f:
        d = json.load(f)["data"]
    return {
        "q0": mpf(d["q_0_50dps"]),
        "b": mpf(d["hoefsmit_b"]),
        "Q_N2": mpf(d["Q_N2"]),
        "Q_AME": mpf(d["Q_AME"]),
    }


def main() -> int:
    t0 = time.monotonic()
    wb = WitnessBuilder("qbeta-ck-truncation-order-analysis", engine="mpmath",
                        start_time=t0)
    wb.set_description(
        "Canonical reference framing the Q_β precision ladder as a "
        "TRUNCATION ORDER of a convergent series Q_β = Q_base·Π(1+c_k·u^k), "
        "u = b·ℏ_q² ≈ 0.00852. Establishes the N(ε) formula "
        "(N ≥ log10(1/ε)/2.07 − 1), per-rung term sizes, the q₀-stability "
        "floor diagnosis (c_k≥3 are q₀-dependent near-matches, not "
        "Taylor-exact), and the Habiro-element fix (parallel α_EM #1511). "
        "Written to stop the recurring c_k wire/un-wire flip-flop by "
        "separating 'N = truncation order chosen by precision' from "
        "'c_k canonicity tier (proved/near-match/fitted)'."
    )
    wb.set_content_block("prop:q-beta-categorical-precision-ladder")

    data = load_q_data()
    q0, b, Q_N2, Q_AME = data["q0"], data["b"], data["Q_N2"], data["Q_AME"]
    hbar_q = (q0 - 1) / q0
    u = b * hbar_q**2

    digits_per_rung = -log10(u)

    print("=" * 76)
    print(" Q_β PRECISION LADDER — truncation-order analysis (canonical reference)")
    print("=" * 76)
    print()

    # ── Part A: ladder step ─────────────────────────────────────
    print("  PART A: ladder step u = b·ℏ_q²")
    print(f"    b (Hoefsmit)        = {float(b):.8f}")
    print(f"    ℏ_q = (q-1)/q       = {float(hbar_q):.8f}")
    print(f"    u = b·ℏ_q²          = {float(u):.10f}")
    print(f"    1/u                 = {float(1/u):.3f}")
    print(f"    log10(1/u)          = {float(digits_per_rung):.4f}")
    print(f"    => each rung gains ~{float(digits_per_rung):.2f} decimal digits")
    print()

    # ── Part B: N(ε) formula ────────────────────────────────────
    print("  PART B: required truncation order N(ε)")
    print(f"    N ≥ log10(1/ε_target) / {float(digits_per_rung):.3f} − 1")
    print()
    targets = [
        ("100× experimental (7.8 ppb)", mpf("7.8e-9")),
        ("1 ppb",                       mpf("1e-9")),
        ("1 ppt",                       mpf("1e-12")),
        ("1 ppQ (10⁻¹⁵)",               mpf("1e-15")),
    ]
    n_of_eps = []
    print(f"    {'target':32s} {'N ≥':>8s} {'-> N':>6s}")
    for name, eps in targets:
        nreq = -log10(eps) / digits_per_rung - 1
        n_int = int(ceil(nreq))
        n_of_eps.append({"target": name, "epsilon": mp.nstr(eps, 4),
                         "N_lower_bound": float(nreq), "N_required": n_int})
        print(f"    {name:32s} {float(nreq):>8.2f} {n_int:>6d}")
    print()

    # ── Part C: per-rung term sizes + cumulative residual ───────
    print("  PART C: per-rung term size |c_k·u^k| + cumulative residual")
    # Canonical c_k forms (the framework's stated values; NOT fitted here)
    c = {
        2: mpf(-1),               # PROVED Taylor-exact
        3: mpf(-2),               # J_Hopf(q=1); near-match (q₀-dependent)
        4: mpf(-2) * b**4,        # c_3·b⁴; near-match
        5: mpf(-2)**2 * 3 + b,    # c_3²·3 + b; near-match
    }
    print(f"    {'k':>2} {'c_k form':22s} {'|c_k|':>9} {'|c_k·u^k|(ppb)':>16} "
          f"{'cum.resid(ppb)':>16}")
    rung_rows = []
    Q = Q_N2
    forms = {2: "-1 (PROVED)", 3: "J_Hopf(q=1)=-2", 4: "c_3·b⁴", 5: "c_3²·3+b"}
    # N=2 baseline residual
    resid2 = float((Q_N2 - Q_AME) / Q_AME * 1e9)
    print(f"    {2:>2} {forms[2]:22s} {1.0:>9.4f} {'(baseline)':>16s} "
          f"{resid2:>+16.3f}")
    rung_rows.append({"k": 2, "c_k": "-1", "term_ppb": None,
                      "cumulative_residual_ppb": resid2})
    for k in [3, 4, 5]:
        term = c[k] * u**k
        Q = Q * (1 + term)
        resid = float((Q - Q_AME) / Q_AME * 1e9)
        print(f"    {k:>2} {forms[k]:22s} {float(abs(c[k])):>9.4f} "
              f"{float(abs(term)*1e9):>16.3f} {resid:>+16.4f}")
        rung_rows.append({"k": k, "c_k": forms[k],
                          "term_ppb": float(abs(term) * 1e9),
                          "cumulative_residual_ppb": resid})
    print()
    print("    NOTE the non-monotonicity: N=4 residual (+0.055 ppb) is BETTER")
    print("    than N=5 (+0.63 ppb). A convergent series with EXACT c_k would")
    print("    be monotone. The reversal is the experimental signature that")
    print("    c_5 (and c_3, c_4) are q₀-dependent NEAR-MATCHES, not exact.")
    print()

    # ── Part D: q₀-stability floor diagnosis ───────────────────
    print("  PART D: q₀-stability floor diagnosis")
    print("    The TRUE Taylor coefficient of a convergent series is")
    print("    q₀-ANCHOR-INDEPENDENT. A near-match swings across q₀ anchors.")
    print()
    # c_3 empirical at two q₀ anchors (values from the deep-audit record)
    c3_muon_pin = mpf("-2.0097")   # muon-anchored q₀
    c3_mp_pin   = mpf("-2.0693")   # m_p-anchored q₀ (current canonical)
    c3_nominal  = mpf("-2")        # J_Hopf(q=1)
    swing_muon = float(abs((c3_muon_pin - c3_nominal) / c3_nominal) * 100)
    swing_mp   = float(abs((c3_mp_pin - c3_nominal) / c3_nominal) * 100)
    print(f"    c_3 = J_Hopf(q=1) nominal:        {float(c3_nominal):+.4f}")
    print(f"    c_3 empirical @ muon-pin q₀:      {float(c3_muon_pin):+.4f}  "
          f"({swing_muon:.2f}% off nominal)")
    print(f"    c_3 empirical @ m_p-pin  q₀:      {float(c3_mp_pin):+.4f}  "
          f"({swing_mp:.2f}% off nominal)")
    print(f"    swing across anchors:             {abs(swing_mp - swing_muon):.2f}%")
    print()
    print("    A 3% cross-anchor swing >> compute precision (10⁻⁵⁰) ⟹ c_3=-2")
    print("    is a STRUCTURAL NEAR-MATCH, not a Taylor-EXACT coefficient.")
    print("    Per the discipline lock (#1479): 'q₀-dependent residuals are")
    print("    evidence of form-fitting at the test q₀'. CORRECT — but the")
    print("    fix is NOT to drop k≥3; it is to find the exact c_k (Part E).")
    print()

    # ── Part E: the Habiro fix ─────────────────────────────────
    print("  PART E: the Habiro-element fix (parallel α_EM #1511)")
    print("    For α_EM, the next-order factor [2]_q·(1-h²α) was shown to be")
    print("    a HABIRO ELEMENT whose Taylor coefficients are BINOMIAL-EXACT")
    print("    (PR #1511, merged): c_k = 2·C(1/2,k/2)·(1/4)^(k/2). Once the")
    print("    element is named, the c_k are exact, q₀-independent, and the")
    print("    truncation error |c_{N+1}·u^{N+1}| is a rigorous bound.")
    print()
    print("    The Q_β ladder needs the SAME treatment: identify the Q_β")
    print("    Habiro element (the q-series whose Taylor coefficients ARE the")
    print("    c_k). Until then, c_k≥3 stay tier='near-match' and Q_β reports")
    print("    N=2 as the deepest PROVED rung — but the dashboard should")
    print("    ALSO report the N=3 near-match value (beats 100× exp) with an")
    print("    explicit tier tag, NOT silently drop it.")
    print()

    print("=" * 76)
    print(" CANONICAL FRAMING (read before touching c_k wiring)")
    print("=" * 76)
    print()
    print("  1. N is a TRUNCATION ORDER chosen by target precision (Part B),")
    print("     NOT a binary canonicity gate.")
    print("  2. Truncation error after N rungs ≈ |c_{N+1}·u^{N+1}| (Part C).")
    print("  3. c_2 is PROVED Taylor-exact; c_k≥3 are q₀-dependent NEAR-")
    print("     MATCHES (Part D) until a Q_β Habiro element makes them exact")
    print("     (Part E).")
    print("  4. Report TIERED (proved/near-match/fitted), never binary")
    print("     wired/dropped. N=3 beats 100× EXPERIMENTAL with c_3 tagged")
    print("     'near-match' — both facts true simultaneously.")

    # ── Witness ─────────────────────────────────────────────────
    wb.add_data("ladder_step", {
        "u_formula": "b · ℏ_q²",
        "u_value": mp.nstr(u, 20),
        "one_over_u": mp.nstr(1 / u, 12),
        "digits_per_rung_log10_inv_u": mp.nstr(digits_per_rung, 8),
    })
    wb.add_data("N_of_epsilon_formula", "N ≥ log10(1/ε) / log10(1/u) − 1")
    wb.add_data("N_of_epsilon_table", n_of_eps)
    wb.add_data("per_rung", rung_rows)
    wb.add_data("non_monotonicity_note", (
        "N=4 residual (+0.055 ppb) is better than N=5 (+0.63 ppb). A "
        "convergent series with EXACT c_k would be monotone; the reversal "
        "is the signature that c_k≥3 are q₀-dependent near-matches."
    ))
    wb.add_data("q0_stability_floor", {
        "c3_nominal_J_Hopf": "-2",
        "c3_empirical_muon_pin": "-2.0097",
        "c3_empirical_mp_pin": "-2.0693",
        "swing_muon_pct": swing_muon,
        "swing_mp_pct": swing_mp,
        "cross_anchor_swing_pct": abs(swing_mp - swing_muon),
        "verdict": "c_3=-2 is a STRUCTURAL NEAR-MATCH (q₀-dependent), not "
                   "Taylor-exact. >>compute-precision swing ⟹ form-fitting.",
    })
    wb.add_data("habiro_fix", (
        "Identify the Q_β Habiro element (q-series whose Taylor coefficients "
        "ARE the c_k), parallel to the α_EM Habiro element [2]_q·(1-h²α) "
        "(PR #1511). Then c_k become exact + q₀-independent and "
        "|c_{N+1}·u^{N+1}| is a rigorous truncation bound."
    ))
    wb.add_data("canonical_framing", {
        "rule_1": "N is a truncation order chosen by target precision, not a "
                  "binary canonicity gate.",
        "rule_2": "Truncation error after N rungs ≈ |c_{N+1}·u^{N+1}|.",
        "rule_3": "c_2 PROVED Taylor-exact; c_k≥3 are q₀-dependent near-matches "
                  "until a Q_β Habiro element makes them exact.",
        "rule_4": "Report TIERED (proved/near-match/fitted), never binary "
                  "wired/dropped. N=3 beats 100× experimental with c_3 tagged "
                  "near-match — both facts true.",
    })

    wb.add_assertion(
        "N3_beats_100x_experimental_target",
        computed=round(rung_rows[1]["cumulative_residual_ppb"], 2),  # k=3 row
        expected=6.02,
        tolerance=0.5,
        source="At N=3 (c_3 = J_Hopf(q=1) = -2 near-match) the Q_β residual "
               "is +6.0 ppb < 7.8 ppb (100× experimental target). The c_3 "
               "near-match status (q₀-dependent) is a SEPARATE fact from the "
               "experimental match — both reported, neither suppressed.",
    )
    wb.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
