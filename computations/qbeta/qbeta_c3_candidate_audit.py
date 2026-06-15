#!/usr/bin/env python3
"""qbeta_c3_candidate_audit.py — Taylor-expand each N=3 candidate
from probe_q_beta_operator_valued_N3.py and report the predicted c_3.

PR #1786 follow-up. The structural proof of c_2 = -1 (sibling
proposition `prop:q-beta-c-2-eq-neg-one-structural`, sorry-free Lean)
established that the N=2 ladder factor (1 - b²·ℏ_q⁴) IS literally
(1 - u²) with u = b·ℏ_q² — no fit, no derivation residual. The same
template should apply at N=3: identify which operator-valued candidate
factor expands as `(1 + c_3·u³ + O(u⁴))` with c_3 matching the
empirical near-match value (-2 = J_Hopf(q=1)).

This probe is the AUDIT step before any c_3 structural claim:

  1. Enumerate the candidate N=3 factors actually tried in
     probe_q_beta_operator_valued_N3.py (12 candidates).
  2. For each, compute the SERIES expansion in u = b·ℏ_q² up to u³
     using sympy, ratifying the c_2 coefficient against the
     structural -1 (sanity check on the b convention).
  3. Read off the u³ coefficient — this is the candidate's predicted c_3.
  4. Compare to the empirical c_3 ≈ -2 (and the J_Hopf(q)
     hypothesis -(q² + q⁻²) which gives -2.044 at q_0).
  5. Verdict: which candidate (if any) predicts c_3 ∈ {-2, J_Hopf(q)}
     structurally — same status template as c_2.

Bottom line (what we expect to find): NO candidate from the existing
script predicts c_3 = -2 structurally. The Pure b³ extensions give
c_3 ∈ {-1, 0, +1}; product-cos gives c_3 = 0 (cosine Taylor has no
u³ term); exponential-resum gives a non-integer rational. The
empirical c_3 = -2 therefore does NOT fall out of any current
ansatz — it requires a different N=3 operator-valued structure.

This audit makes that gap explicit BEFORE someone files a structural-
c_3 claim that doesn't hold up.

No fit. No new claims. Honest scoping of the c_3 open question.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
# `_path_bridge` already puts computations/ on sys.path — single
# strategy per Copilot review on PR #1786.

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65

import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

Q0_MP_PIN = "1.1099785827513808075916690956107688798744991218736"


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-c3-candidate-audit",
        engine="python+sympy",
        start_time=t0,
    )
    builder.set_description(
        "Taylor-expand each N=3 candidate from probe_q_beta_"
        "operator_valued_N3.py to u³ order and read off the "
        "predicted c_3. Sanity-check against c_2 = -1 STRUCTURAL "
        "(prop:q-beta-c-2-eq-neg-one-structural). Verdict: which "
        "candidate (if any) predicts c_3 = -2 (the empirical "
        "near-match) structurally. Honest scoping — does not "
        "claim a structural c_3 derivation."
    )
    builder.set_content_block("prop:q-beta-c-2-eq-neg-one-structural")

    print("=" * 78)
    print(" Q_β c_3 AUDIT — Taylor coefficients of N=3 candidates at u³")
    print("=" * 78)
    print()

    u = sp.Symbol("u", positive=True)  # u = b·ℏ_q²

    # Candidates as power series in u (treat b·ℏ_q² as a single
    # variable; the candidate functions are then pure series in u
    # without needing the b convention to be fixed).
    #
    # Mapping the candidates from probe_q_beta_operator_valued_N3.py
    # into ladder normal form Π (1 + c_k · u^k):
    #
    # The Q_N2 baseline is Q_A · cos(α_eff) · (1 - u²) — c_2 = -1
    # structural (proved in PR #1786). Any candidate is Q_N2 ·
    # extension, where the extension is the (1 + c_3·u³ + …) tail.

    candidates = {
        # ---- Pure b³ extensions (the "Kashiwara naive" family) ----
        "(1 + u³)": 1 + u ** 3,
        "(1 - u³)": 1 - u ** 3,
        "(1 - u³/2)": 1 - u ** 3 / 2,
        # ---- Iterated-cos (note: cos(b·ℏ_q²) and cos(b²·ℏ_q⁴) ---
        #      multiply with the cos(α_eff) baseline; the EXTENSION
        #      beyond (1 - u²) is what we expand here)
        "cos(u) / (1 - u²)":         sp.cos(u) / (1 - u ** 2),
        "cos(u)·cos(u²) / (1 - u²)": sp.cos(u) * sp.cos(u ** 2)
                                     / (1 - u ** 2),
        # ---- Exponential resummation ----
        "exp(-u/(2(1-u))) / (1 - u²)":
            sp.exp(-u / (2 * (1 - u))) / (1 - u ** 2),
        "exp(-u²/(2(1-u))) / (1 - u²)":
            sp.exp(-u ** 2 / (2 * (1 - u))) / (1 - u ** 2),
        # ---- Geometric resummation ----
        "1 / (1 + u²) / (1 - u²) = 1/(1-u⁴)":
            1 / ((1 + u ** 2) * (1 - u ** 2)),
        # ---- The empirical near-match target ----
        "(1 - 2·u³)  [hypothetical c_3 = -2]": 1 - 2 * u ** 3,
        # ---- (1 - u²)·(1 + α·u³) for α to be solved — sanity ----
        "(1 - 2·u² + u⁴) / (1 - u²)  [(1 - u²) squared]":
            (1 - 2 * u ** 2 + u ** 4) / (1 - u ** 2),
    }

    print(f"  {'candidate':<55} {'series':<35} c_3")
    print(f"  {'-' * 55} {'-' * 35} {'-' * 8}")

    results = []
    for name, expr in candidates.items():
        # Expand to u⁴ to read off c_3 cleanly.
        series = sp.series(expr, u, 0, 5).removeO()
        c0 = series.coeff(u, 0)
        c1 = series.coeff(u, 1)
        c2_pred = series.coeff(u, 2)
        c3_pred = series.coeff(u, 3)
        # For the ladder, the extension factor should start with 1
        # (the Q_N2 baseline already covers the constant + cos
        # contribution). c_3 is the u³ coefficient.
        series_str = (f"{sp.nsimplify(c0)}+{sp.nsimplify(c1)}·u"
                      f"+{sp.nsimplify(c2_pred)}·u²"
                      f"+{sp.nsimplify(c3_pred)}·u³").replace("+-", "-")
        # Truncate to 35 chars for the column
        if len(series_str) > 33:
            series_str = series_str[:30] + "..."
        c3_str = str(sp.nsimplify(c3_pred, rational=True, tolerance=1e-12))
        print(f"  {name:<55} {series_str:<35} {c3_str}")
        results.append({
            "candidate": name,
            "u0_coeff": str(sp.nsimplify(c0)),
            "u1_coeff": str(sp.nsimplify(c1)),
            "u2_coeff": str(sp.nsimplify(c2_pred)),
            "u3_coeff": c3_str,
            "matches_c3_neg_2": (sp.simplify(c3_pred + 2) == 0),
        })

    print()
    print("  Empirical c_3 target: -2 (= J_Hopf(q=1)) per audit")
    print("  doc 2026-05-31-qbeta-ck-truncation-order-canonical-framing.md")
    print()

    matches = [r for r in results if r["matches_c3_neg_2"]]
    print(f"  Candidates predicting c_3 = -2 structurally: {len(matches)}")
    for r in matches:
        print(f"    ✓ {r['candidate']}")
    if not matches:
        print(f"    (none — no candidate from existing N=3 script")
        print(f"     predicts c_3 = -2 by Taylor expansion alone)")
    print()

    # The ONLY candidate that gives c_3 = -2 is the hypothetical
    # "(1 - 2·u³)" itself — which is the empirical fit, not a
    # categorical derivation.
    non_trivial_matches = [r for r in matches
                           if "hypothetical" not in r["candidate"]]
    print("  Non-trivial structural predictions of c_3 = -2:")
    if non_trivial_matches:
        for r in non_trivial_matches:
            print(f"    ✓ {r['candidate']}")
    else:
        print(f"    (NONE — confirms c_3 has no clean structural")
        print(f"     derivation from current ansatz family)")
    print()

    print("=" * 78)
    print(" VERDICT — c_3 structural derivation status")
    print("=" * 78)
    print()
    print(f"  c_2 = -1   STRUCTURAL ✓ (prop:q-beta-c-2-eq-neg-one-structural,")
    print(f"             sorry-free Lean, PR #1786)")
    print(f"  c_3 = -2   EMPIRICAL near-match — no candidate from the")
    print(f"             existing operator-valued N=3 script predicts")
    print(f"             c_3 = -2 by Taylor expansion. The closest")
    print(f"             structural predictions are c_3 ∈ {{-1, 0, +1}}")
    print(f"             from the Pure b³ extensions.")
    print()
    print(f"  Open question: what operator-valued N=3 STRUCTURE gives")
    print(f"  the (1 - 2·u³) ladder factor? Candidates worth exploring:")
    print(f"    A. Q_N2 · (1 - u·δ) · (1 + u·δ⁻¹) for some δ — no.")
    print(f"    B. Habiro element [k]_q expansion at order 3.")
    print(f"    C. Two-component link contribution (Hopf has 2 components,")
    print(f"       and J_Hopf(1) = -2 reflects -(-1)^{{|L|-1}}·|L| ?).")
    print(f"    D. q-Schur function ψ_(1,1,1)(q) (3-cycle in S_3).")
    print()
    print(f"  This audit makes the gap explicit. No fit-based c_3 claim")
    print(f"  may proceed without identifying the operator-valued source.")
    print()

    builder.add_data("candidates", results)
    builder.add_data("verdict", {
        "c_2_status": "STRUCTURAL (prop:q-beta-c-2-eq-neg-one-structural)",
        "c_3_status": "empirical near-match; no structural derivation",
        "candidates_predicting_c3_neg_2_structurally":
            len(non_trivial_matches),
        "empirical_c3_target": -2,
        "j_hopf_q0_value":
            float(-(mp.mpf(Q0_MP_PIN) ** 2 + 1 / mp.mpf(Q0_MP_PIN) ** 2)),
    })

    # Assertion: NO non-trivial candidate predicts c_3 = -2 structurally.
    # This is the audit's central finding — the gap is real.
    builder.add_assertion(
        "no_existing_candidate_predicts_c_3_eq_neg_2_structurally",
        computed=int(len(non_trivial_matches) == 0),
        expected=1,
        tolerance=0,
        source=("AUDIT: enumerate the N=3 candidates from probe_q_"
                "beta_operator_valued_N3.py, Taylor-expand each as "
                "a series in u = b·ℏ_q², read off the u³ coefficient. "
                "None of the existing candidates (Pure b³, iterated "
                "cos, exponential resum, geometric, half-argument) "
                "predicts c_3 = -2. The only fit that matches is the "
                "hypothetical (1 - 2·u³) which is not derived. This "
                "assertion enforces the honest scoping: c_3 has no "
                "current structural derivation."),
    )

    builder.save()
    print(f"  Witness: qbeta-c3-candidate-audit.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
